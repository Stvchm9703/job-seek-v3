import os
from job_library import *

script_dir = os.path.dirname(os.path.abspath(__file__))
#script_dir = os.getcwd()


edited_jobs_after_survey_path = os.path.join(script_dir, 'output', 'edited_jobs_after_survey.csv')
if os.path.exists(edited_jobs_after_survey_path):
    # Load the CSV file into the DataFrame 
    df_new_for_XGboost = pd.read_csv(edited_jobs_after_survey_path)
else:
    print(f"Error: The file {edited_jobs_after_survey_path} does not exist.")
    
    
user_choice_path = os.path.join(script_dir, 'user', '15_comparison_result.json') 
user_choice_data = load_other_data(user_choice_path)

feature_list_for_XGBoost = [
    'PostId',
    'adjusted_job_title_similarity',
    'adjusted_job_industry_similarity',
    'adjusted_company_size',
    'adjusted_job_sector',
    'adjusted_company_culture',
    'adjusted_work_model',
    'adjusted_salary_expectation',
    'adjusted_role_type',
    'descriptions_similarity_to_resume_norm',
    'adjusted_distance_score', #this one is not for selecting feature, but for XGboost training
    #'distance_norm',
    'pay_average_norm'
]

feature_list_job_ranking = feature_list_for_XGBoost
feature_list_job_ranking.remove('PostId')

    

## Creating Feature Difference, using the cleaned data
    
# Ensure 'PostId' is in the DataFrame
if 'PostId' not in df_new_for_XGboost.columns:
    print("Error: 'PostId' column not found in df_new_for_XGboost.")
else:
    # Set 'PostId' as the index for easy access
    job_features = df_new_for_XGboost.set_index('PostId')

# Convert index to string if necessary
job_features.index = job_features.index.astype(str)

# Extract the choices list
choices = user_choice_data['choices']

# Create a DataFrame from the choices
comparisons = pd.DataFrame(choices)

# Ensure job IDs are of the correct type (e.g., integer if needed)
comparisons['job_A_id'] = comparisons['job_A_id'].astype(str)
comparisons['job_B_id'] = comparisons['job_B_id'].astype(str)


# Create feature difference data (X)
X = np.array([create_feature_diff(row, job_features) for _, row in comparisons.iterrows()])

# Create the target variable y
# 'user_choice' is 1 if the user prefers job_A, 0 if job_B
y = comparisons['user_choice'].values.astype(int)
    

## XGBoost
# Train the XGBoost model
model = xgb.XGBClassifier()
model.fit(X, y)
# Predict on the entire dataset
y_pred = model.predict(X)    


# Evaluate the model
'''
accuracy = model.score(X, y)
print(f'Accuracy: {accuracy:.2f}')

# Initialize LOOCV
loo = LeaveOneOut()

# Perform LOOCV
scores = cross_val_score(model, X, y, cv=loo, scoring='accuracy')
print(f"\nLOOCV Accuracy Scores: {scores}")
print(f"Mean LOOCV Accuracy: {scores.mean():.2f}")

# Evaluate the Model
print("\nClassification Report:")
print(classification_report(y, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y, y_pred))

# Feature Importance using tree-based method
feature_importances = pd.Series(model.feature_importances_, index=feature_list_job_ranking).sort_values(ascending=False)
print("\nFeature Importances (XGBoost Tree-Based):")
print(feature_importances)

# Plot Feature Importances
feature_importances.plot(kind='barh')
plt.xlabel('Importance Score')
plt.title('Feature Importances (XGBoost)')
plt.gca().invert_yaxis()
plt.show()

# SHAP Values for Model Interpretation (optional)
explainer = shap.Explainer(model)
shap_values = explainer(X)

# Summary Plot
shap.summary_plot(shap_values, X, feature_names=feature_list_job_ranking)
'''


new_jobs = df_new_for_XGboost

# Generate all possible pairs of new jobs
new_job_ids = new_jobs.index.values
new_job_pairs = [(new_job_ids[i], new_job_ids[j]) for i in range(len(new_job_ids)) for j in range(i + 1, len(new_job_ids))]



# Create a DataFrame to hold scores
job_scores = pd.Series(0, index=new_job_ids, dtype=float)

# Calculate feature differences and predict preferences
for job_A, job_B in new_job_pairs:

    
    # Create the feature difference using the function
    row = {'job_A_id': job_A, 'job_B_id': job_B}
    feature_diff_array = create_feature_diff(row, new_jobs.drop(columns=['PostId'])).reshape(1, -1)
    
    # Predict preference
    prob_A_preferred = model.predict_proba(feature_diff_array)[0, 1]
    
    # Update scores
    job_scores[job_A] += prob_A_preferred
    job_scores[job_B] += (1 - prob_A_preferred)


# Sort the job scores in ascending order
ranked_jobs_descending = job_scores.sort_values(ascending=False)

# Retrieve the corresponding rows from the new_jobs DataFrame
ranked_jobs_df_descending = new_jobs.loc[ranked_jobs_descending.index]

# Add the job scores as a new column
ranked_jobs_df_descending['job_score'] = ranked_jobs_descending.values

ranked_jobs_path = os.path.join(script_dir, 'output', 'ranked_jobs.json') 
ranked_jobs_json = ranked_jobs_df_descending[['PostId', 'job_score']].to_json(ranked_jobs_path, orient='records', indent=4)
#print(ranked_jobs_json)

# Display the ranked jobs in ascending order
#print("Ranked Jobs Descending Order with Scores:\n", ranked_jobs_df_descending[['PostId','job_score']])

#total_score = job_scores.sum()
#print("Total Job Score:", total_score)

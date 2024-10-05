import os
from job_library import *

script_dir = os.path.dirname(os.path.abspath(__file__))
#script_dir = os.getcwd()

## import user survey result (after get the user survey result)
user_survey_path = os.path.join(script_dir, 'user', 'sample-result.json') 
user_survey_data = load_other_data(user_survey_path)

edited_jobs_path = os.path.join(script_dir, 'output', 'edited_jobs.csv')
if os.path.exists(edited_jobs_path):
    # Load the CSV file into the DataFrame 'df_new'
    df_new = pd.read_csv(edited_jobs_path)
else:
    print(f"Error: The file {edited_jobs_path} does not exist.")
    
## load other data
government_public_sector_path = os.path.join(script_dir, 'data', 'GovernmentOrPublicSector.json')
government_public_sector_data = load_other_data(government_public_sector_path)

nonprofit_organizations_path = os.path.join(script_dir, 'data', 'nonprofit_organizations.json')
nonprofit_organizations_data = load_other_data(nonprofit_organizations_path)    


## Calculate User Preference score for each job
df_new['company_size_numeric'] = df_new['CompanyDetail.GroupSize'].map(SIZE_MAPPING).astype(float)
mean_company_size = df_new['company_size_numeric'].mean()
df_new['company_size_numeric'] = df_new['company_size_numeric'].fillna(mean_company_size)

df_new['work_type_numeric'] = df_new['WorkType'].map(WORK_TYPE_MAPPING).astype(float)
mean_work_type = df_new['work_type_numeric'].mean()
df_new['work_type_numeric'] = df_new['work_type_numeric'].fillna(mean_work_type)

adjusted_features = {}
# For example, include in your adjusted features
adjusted_features['descriptions_similarity_to_resume_norm'] = df_new['descriptions_similarity_to_resume_norm']


## handle 10 survey questions' result
for keyword in user_survey_data['keywords']:
    #Q1
    if keyword['keyword'] == 'job_title':
        if keyword['value'] == 'same_job_title':
            #df_new.loc[df_new['job_title_similarity_to_last_job'] >= 0.3 , 'user_preference_score'] += df_new['job_title_similarity_to_last_job']
            #new feature replace 'job_title_similarity_to_last_job'
            df_new['adjusted_job_title_similarity'] = df_new['job_title_similarity_to_last_job']
            feature_weights['adjusted_job_title_similarity'] = 1.0            
        elif keyword['value'] == 'new_job_title':
            #df_new.loc[df_new['job_title_similarity_to_last_job'] < 0.3, 'user_preference_score'] += df_new['job_title_similarity_to_last_job'].max() - df_new['job_title_similarity_to_last_job']
            #new feature replace 'job_title_similarity_to_last_job'
            df_new['adjusted_job_title_similarity'] = 1 - df_new['job_title_similarity_to_last_job']
            feature_weights['adjusted_job_title_similarity'] = 0.8
            
        df_new['adjusted_job_title_similarity'] = df_new['adjusted_job_title_similarity'] / df_new['adjusted_job_title_similarity'].max()    
        
        adjusted_features['adjusted_job_title_similarity'] = df_new['adjusted_job_title_similarity']
        #df_new['user_preference_score'] += df_new['adjusted_job_title_similarity'] * feature_weights['adjusted_job_title_similarity']   
            
            
    #Q2
    elif keyword['keyword'] == 'job_industry':
        if keyword['value'] == 'last_industry':
            #df_new.loc[df_new['job_industry_similarity_to_last_job'] > df_new['job_industry_similarity_to_last_job'].quantile(0.7), 'user_preference_score'] += df_new['job_industry_similarity_to_last_job']
            df_new['adjusted_job_industry_similarity'] = df_new['job_industry_similarity_to_last_job']
            feature_weights['adjusted_job_industry_similarity'] = 0.8
            
        elif keyword['value'] == 'other_industry':
            #df_new.loc[df_new['job_industry_similarity_to_last_job'] < df_new['job_industry_similarity_to_last_job'].quantile(0.3), 'user_preference_score'] += 1 - df_new['job_industry_similarity_to_last_job']
            df_new['adjusted_job_industry_similarity'] = 1 - df_new['job_industry_similarity_to_last_job']
            feature_weights['adjusted_job_industry_similarity'] = 0.5
        
        adjusted_features['adjusted_job_industry_similarity'] = df_new['adjusted_job_industry_similarity']    
        #df_new['user_preference_score'] += df_new['adjusted_job_industry_similarity'] * feature_weights['adjusted_job_industry_similarity']     
            
            
            
    #Q3
    elif keyword['keyword'] == 'company_size':
        if keyword['keyword'] == 'company_size':
            if keyword['value'] == 'small_size':
                preferred_size = 1.5  # Average of SIZE_A and SIZE_B
            elif keyword['value'] == 'medium_size':
                preferred_size = 3.5  # Average of SIZE_C and SIZE_D
            elif keyword['value'] == 'large_size':
                preferred_size = 6.5  # Average of SIZE_E to SIZE_H

        max_size = df_new['company_size_numeric'].max()
        # convert difference to be similiarity by 1 - normalised value
        df_new['adjusted_company_size'] = 1 - (abs(df_new['company_size_numeric'] - preferred_size) / (max_size - 1))
        adjusted_features['adjusted_company_size'] = df_new['adjusted_company_size'] 
        #df_new['user_preference_score'] += df_new['adjusted_company_size'] * feature_weights['adjusted_company_size']

        '''
        if keyword['value'] == 'small_size':
            df_new.loc[(df_new['CompanyDetail.GroupSize'] == 'SIZE_A') | (df_new['CompanyDetail.GroupSize'] == 'SIZE_B'), 'user_preference_score'] += company_size_weight
        elif keyword['value'] == 'medium_size':
            df_new.loc[(df_new['CompanyDetail.GroupSize'] == 'SIZE_C') | (df_new['CompanyDetail.GroupSize'] == 'SIZE_D'), 'user_preference_score'] += company_size_weight
        elif keyword['value'] == 'large_size':
            df_new.loc[(df_new['CompanyDetail.GroupSize'].isin(['SIZE_E', 'SIZE_F', 'SIZE_G', 'SIZE_H'])), 'user_preference_score'] += company_size_weight 
        '''
    
    #Q4
    elif keyword['keyword'] == 'job_sector':    
        if keyword['value'] == 'government_or_public_sector':
            df_new['adjusted_job_sector'] = df_new['CompanyDetail.Industry'].isin(government_public_sector_data['keywords']).astype(int)
        elif keyword['value'] == 'nonprofit_organizations':
            df_new['adjusted_job_sector'] = df_new['CompanyDetail.Industry'].isin(nonprofit_organizations_data['keywords']).astype(int)

        elif keyword['value'] == 'private_sector':
            df_new['adjusted_job_sector'] = (~df_new['CompanyDetail.Industry'].isin(government_public_sector_data['keywords'] + nonprofit_organizations_data['keywords'])).astype(int)
        
        adjusted_features['adjusted_job_sector'] = df_new['adjusted_job_sector']     
        #df_new['user_preference_score'] += df_new['adjusted_job_sector'] * feature_weights['adjusted_job_sector']
            
    
    #Q5
    elif keyword['keyword'] == 'company_culture':
        if keyword['value'] == 'teamwork':
            df_new['adjusted_company_culture'] = df_new['job_teamwork_score']
        elif keyword['value'] == 'growth':
            df_new['adjusted_company_culture'] = df_new['job_growth_score']
        elif keyword['value'] == 'respect':
            df_new['adjusted_company_culture'] = df_new['job_respect_score']
        elif keyword['value'] == 'work_life_balance':
            df_new['adjusted_company_culture'] = df_new['job_work_life_balance_score']

        # Normalize the culture scores 
        df_new['adjusted_company_culture'] = df_new['adjusted_company_culture'] / df_new['adjusted_company_culture'].max()
        
        adjusted_features['adjusted_company_culture'] = df_new['adjusted_company_culture']
        #df_new['user_preference_score'] += df_new['adjusted_company_culture'] * feature_weights['adjusted_company_culture']
    
    #Q6
    elif keyword['keyword'] == 'work_model':
        if keyword['value'] == 'remote':
            df_new['adjusted_work_model'] = df_new['work_from_home_score']
        elif keyword['value'] == 'hybrid':
            df_new['adjusted_work_model'] = df_new['hybrid_score']
        elif keyword['value'] == 'on_site':
            df_new['adjusted_work_model'] = df_new['on_site_score']
            
        adjusted_features['adjusted_work_model']  = df_new['adjusted_work_model'] 
        #df_new['user_preference_score'] += df_new['adjusted_work_model'] * feature_weights['adjusted_work_model']
    
        
    
    #Q7 : Salary type
    elif keyword['keyword'] == 'salary_expectations':
        if keyword['value'] == 'competitive_salary':
            df_new['adjusted_salary_expectation'] = df_new['competitive_salary_score']
        elif keyword['value'] == 'benefits':
            df_new['adjusted_salary_expectation'] = df_new['benefit_score']
        elif keyword['value'] == 'stable_income':
            # Assuming less competitive salary indicates stable income
            df_new['adjusted_salary_expectation'] = 1 - df_new['competitive_salary_score']
        elif keyword['value'] == 'work_life_balance':
            df_new['adjusted_salary_expectation'] = df_new['job_work_life_balance_score']

        df_new['adjusted_salary_expectation'] = df_new['adjusted_salary_expectation'] / df_new['adjusted_salary_expectation'].max()
        adjusted_features['adjusted_salary_expectation']  = df_new['adjusted_salary_expectation']
        #df_new['user_preference_score'] += df_new['adjusted_salary_expectation'] * feature_weights['adjusted_salary_expectation']
        
    #Q8
    
    elif keyword['keyword'] == 'role_type':
        if keyword['value'] == 'fulltime':
            preferred_type = WORK_TYPE_MAPPING['Full time']
        elif keyword['value'] == 'contract':
            preferred_type = WORK_TYPE_MAPPING['Contract/Temp']
        elif keyword['value'] == 'parttime':
            preferred_type = (WORK_TYPE_MAPPING['Part time'] + WORK_TYPE_MAPPING['Casual/Vacation']) / 2

        max_type = max(WORK_TYPE_MAPPING.values())
        df_new['adjusted_role_type'] = 1 - (abs(df_new['work_type_numeric'] - preferred_type) / (max_type - 1))
        
        adjusted_features['adjusted_role_type']  = df_new['adjusted_role_type']
        #df_new['user_preference_score'] += df_new['adjusted_role_type'] * feature_weights['adjusted_role_type']
        
    
    #Q9 company based (foreign or local)
    elif keyword['keyword'] == 'company_scale':

        if keyword['value'] == 'foreign_based':
            df_new['adjusted_company_scale'] = 1 - df_new['headquarter_in_australia'].astype(int)
            feature_weights['adjusted_company_scale'] = 0.4  # Higher importance
            #df_new['user_preference_score'] += df_new['adjusted_company_scale'] * feature_weights['adjusted_company_scale']

        elif keyword['value'] == 'local':
            df_new['adjusted_company_scale'] = df_new['headquarter_in_australia'].astype(int)
            feature_weights['adjusted_company_scale'] = 0.4
            #df_new['user_preference_score'] += df_new['adjusted_company_scale'] * feature_weights['adjusted_company_scale']

        elif keyword['value'] == 'no_preference':
            df_new['adjusted_company_scale'] = df_new['headquarter_in_australia'].astype(int) 
            feature_weights['adjusted_company_scale'] = 0  # Lower importance
            # no adding to user preference score
            
        adjusted_features['adjusted_company_scale']  = df_new['adjusted_company_scale']   
     
    #Q10: Location Distance
    elif keyword['keyword'] == 'location_distance':
        if keyword['value'] == '30_minutes':
            max_distance = 25  # Approximate max distance for 30 minutes commute
            feature_weights['adjusted_distance_score'] = 1.0  # High importance
        elif keyword['value'] == '1_hour':
            max_distance = 50  # Approximate max distance for 1 hour commute
            feature_weights['adjusted_distance_score'] = 0.8
        elif keyword['value'] == 'no_preference':
            max_distance = df_new['distance_km'].max()
            feature_weights['adjusted_distance_score'] = 0.4  # Lower importance

        df_new['adjusted_distance_score'] = df_new['distance_km'].apply(
            lambda x: max(0, (max_distance - x) / max_distance)
        )
        
        adjusted_features['adjusted_distance_score'] = df_new['adjusted_distance_score']

        #df_new['user_preference_score'] += df_new['adjusted_distance_score'] * feature_weights['adjusted_distance_score']



# Normalize the weights
total_weight = sum(feature_weights.values())
feature_weights = {k: v / total_weight for k, v in feature_weights.items()}
#feature_weights = {k: v for k, v in feature_weights.items()}


df_new['user_preference_score'] = sum(
    df_new[feature] * feature_weights[feature] for feature in adjusted_features
)

### K-mean clustering

# Reshape scores for K-Means
scores = df_new['user_preference_score'].values.reshape(-1, 1)

# Decide on the number of clusters
num_clusters = 5

# Apply K-Means clustering
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
df_new['score_cluster'] = kmeans.fit_predict(scores)


### Select Pairs


# List of features and their types
features_info = {
    'adjusted_job_title_similarity': 'continuous',
    'adjusted_job_industry_similarity': 'continuous',
    'adjusted_company_size': 'continuous',
    'adjusted_job_sector': 'categorical',
    'adjusted_company_culture': 'continuous',
    'adjusted_work_model': 'categorical',
    'adjusted_salary_expectation': 'continuous',
    'adjusted_role_type': 'categorical',
    'adjusted_distance_score': 'continuous',
    'descriptions_similarity_to_resume_norm': 'continuous',
    'pay_average_norm': 'continuous',
}

# Initialize variables
pairs_list = []
pair_id = 1
max_pairs = 15  # Number of pairs you want to select

# K-Means Clustering
num_clusters = 5  # Adjust based on your data
scores = df_new['user_preference_score'].values.reshape(-1, 1)
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
df_new['score_cluster'] = kmeans.fit_predict(scores)

# Initialize thresholds and criteria
similarity_threshold = 0.95
difference_threshold = 0.05
min_similarities = 4
min_differences = 3

# Initialize variables for adjustments
adjustment_iterations = 0
max_adjustments = 5  # Maximum number of adjustments to prevent infinite loops

# Loop to adjust criteria if not enough pairs are found
while len(pairs_list) < max_pairs and adjustment_iterations < max_adjustments:
    # Reset pairs_list and job_appearance_counts for a fresh start
    pairs_list = []
    job_appearance_counts = {}
    pair_id = 1

    # Iterate over each cluster
    for cluster_label in df_new['score_cluster'].unique():
        # Get jobs in the current cluster
        cluster_jobs = df_new[df_new['score_cluster'] == cluster_label]
        
        # Ensure there are at least 2 jobs to form pairs
        if len(cluster_jobs) < 2:
            continue  # Skip this cluster
        
        # Get all possible pairs within the cluster
        job_indices = cluster_jobs.index.tolist()
        cluster_pairs = list(combinations(job_indices, 2))
        
        # Shuffle pairs to introduce randomness
        np.random.shuffle(cluster_pairs)
        
        # Iterate over the pairs
        for (job_idx_A, job_idx_B) in cluster_pairs:
            job_A = cluster_jobs.loc[job_idx_A]
            job_B = cluster_jobs.loc[job_idx_B]
            
            # Get the 'PostId' as job IDs
            job_id_A = job_A['PostId']
            job_id_B = job_B['PostId']
            
            # Check if either job has already appeared in 2 pairs
            count_A = job_appearance_counts.get(job_id_A, 0)
            count_B = job_appearance_counts.get(job_id_B, 0)
            
            if count_A >= 2 or count_B >= 2:
                continue  # Skip this pair
            
            # Compute feature similarities and overall similarity
            feature_similarities, avg_similarity = compute_similarity(job_A, job_B, features_info)
            
            # Determine similarities and differences based on thresholds
            similarities = []
            differences = []
            for feature, sim_score in feature_similarities.items():
                if sim_score >= similarity_threshold:
                    similarities.append(feature)
                elif sim_score <= difference_threshold:
                    differences.append(feature)
            
            # Criteria: At least min_similarities similarities and min_differences differences
            if len(similarities) >= min_similarities and len(differences) >= min_differences:
                pair_info = {
                    "pair_id": int(pair_id),
                    "job_A": {
                        "job_id": convert_value(job_id_A),
                        "user_preference_score": float(convert_value(job_A['user_preference_score'])),
                        "features": {feature: convert_value(job_A[feature]) for feature in features_info.keys()}
                    },
                    "job_B": {
                        "job_id": convert_value(job_id_B),
                        "user_preference_score": float(convert_value(job_B['user_preference_score'])),
                        "features": {feature: convert_value(job_B[feature]) for feature in features_info.keys()}
                    },
                    "similarities": similarities,
                    "differences": differences,
                    "overall_similarity": float(avg_similarity)
                }
                pairs_list.append(pair_info)
                pair_id += 1
                
                # Update job appearance counts
                job_appearance_counts[job_id_A] = count_A + 1
                job_appearance_counts[job_id_B] = count_B + 1
                
                # Stop if we've collected enough pairs
                if len(pairs_list) >= max_pairs:
                    break
        
        # Stop if we've collected enough pairs
        if len(pairs_list) >= max_pairs:
            break
    
    # Check if enough pairs were found
    if len(pairs_list) < max_pairs:
        # Adjust thresholds and criteria
        similarity_threshold -= 0.05  # Decrease similarity threshold
        difference_threshold += 0.05  # Increase difference threshold
        min_similarities = max(2, min_similarities - 1)
        min_differences = max(2, min_differences - 1)
        adjustment_iterations += 1
        #print(f"Adjusting thresholds: similarity >= {similarity_threshold}, differences <= {difference_threshold}")
    else:
        break

# Inform the user about the number of pairs found
#print(f"Total pairs found: {len(pairs_list)}")

# Convert the pairs_list to JSON format
json_output = json.dumps(pairs_list, indent=4)

# Optionally, write to a JSON file
with open('job_pairs.json', 'w') as f:
    f.write(json_output)

# Optional: Print the JSON output
#print(json_output)


## select features useful in creating feature difference and XGboost training

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

df_new_for_XGboost = df_new[feature_list_for_XGBoost]

output_edited_jobs_after_survey_path = os.path.join(script_dir, 'output', 'edited_jobs_after_survey.csv')
df_new_for_XGboost.to_csv(output_edited_jobs_after_survey_path)
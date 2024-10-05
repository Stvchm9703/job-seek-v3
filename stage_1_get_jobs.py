import os
from job_library import *

script_dir = os.path.dirname(os.path.abspath(__file__))
#script_dir = os.getcwd()


# -----------------------
# Load Data
# -----------------------

# Load user info
user_info_path = os.path.join(script_dir, 'user', 'user_info.json')
with open(user_info_path, 'r') as f:
    user_info = json.load(f)

# Assign the values from the JSON file to variables
user_location = user_info['user_location']
resume_text = user_info['resume_text']
user_last_job_title = user_info['user_last_job_title']
user_last_job_industry = user_info['user_last_job_industry']
user_targeted_job_title = user_info['user_targeted_job_title']


output_result_0_path = os.path.join(script_dir, 'user', 'output_result_0.json')
df_0 = load_data(output_result_0_path)
df_new = pd.DataFrame()
#print(df_0.shape)

postcode_path = os.path.join(script_dir, 'data', 'au_postcodes.json')
postcode_data = load_other_data(postcode_path)

government_public_sector_path = os.path.join(script_dir, 'data', 'GovernmentOrPublicSector.json')
government_public_sector_data = load_other_data(government_public_sector_path)

nonprofit_organizations_path = os.path.join(script_dir, 'data', 'nonprofit_organizations.json')
nonprofit_organizations_data = load_other_data(nonprofit_organizations_path)

industry_list_path = os.path.join(script_dir, 'data', 'List_of_Industries_Expanded.csv')
df_industry_list = pd.read_csv(industry_list_path)
unique_industry_items = pd.concat([df_industry_list['Level 1 (L1) label'], df_industry_list['Level 2 (L2) label'], df_industry_list['Level 3 (L3) label']]).dropna().unique().tolist()


# -----------------------
# Data Preprocessing
# -----------------------

## Feature conversion & number_conversion
df_new = feature_conversion(df_0, POWERS)

## Location data cleaning function

# Create DataFrame and apply parsing
#df = pd.DataFrame(locations, columns=['location'])
df_0[['suburb', 'city', 'region', 'state']] = df_0['Locations'].apply(
    lambda x: parse_location(x, STATE_MAPPING)
)

#df_0.head(10)

user_lat, user_long = geocode_location(user_location, postcode_data)
# Add distances to the DataFrame
df_new['distance_km'] = calculate_distances(df_0, user_location, postcode_data)
#df_new

##  Fill the missing value in pay range with means
df_new['Locations'] = df_0['Locations']
df_new = preprocess_zeros_nan(df_new, user_location)
df_new.drop(columns=['Locations'], inplace=True)

## Create text similiarities features
job_descriptions = df_0['DebugText']

# Using a pre-trained SBERT model
model = SentenceTransformer('all-MiniLM-L6-v2')
df_new['descriptions_similarity_to_resume'] = calculate_similarity(model, resume_text, job_descriptions)

# Reshape the data to fit the scaler
descriptions_similarity_values = df_new['descriptions_similarity_to_resume'].values.reshape(-1, 1)

scaler = MinMaxScaler(feature_range=(0, 1))

# Fit the scaler to the data and transform
df_new['descriptions_similarity_to_resume_norm'] = scaler.fit_transform(descriptions_similarity_values)



## Calculate user preference score from the survey
df_new['user_preference_score'] = np.zeros(len(df_new))
#df_new

### Compare job title similarity between user's last job title and the job titles in the dataset
df_new['job_title_similarity_to_last_job'] = calculate_similarity(model, user_last_job_title, df_0['PostTitle'])


### Compare job industy between user's last job the jobs in the dataset

df_new['job_industry_similarity_to_last_job'] = calculate_similarity(
    model,
    user_last_job_industry,
    (df_0['CompanyDetail.Industry'].astype(str) + ' ' + df_0['Role'].astype(str))
)

df_new['job_teamwork_score'] = calculate_similarity(model, COLLABORATION_TEAMWORK_TEXT, df_0['DebugText'])
df_new['job_growth_score'] = calculate_similarity(model, INNOVATION_GROWTH_TEXT, df_0['DebugText'])
df_new['job_respect_score'] = calculate_similarity(model, INCLUSIVITY_RESPECT_TEXT, df_0['DebugText'])

# Apply the Jaccard similarity - measure the overlap of the keywords between two sets
#df_new['job_respect_score'] = df_0['DebugText'].apply(lambda text: calculate_jaccard_similarity(text, INCLUSIVITY_RESPECT_TEXT))
# Work from home keywords

df_new['work_from_home_score'] = df_0['DebugText'].str.contains('|'.join(WFH_KEYWORDS), case=False, na=False).astype(int)

# Hybrid keywords

df_new['hybrid_score'] = df_0['DebugText'].str.contains('|'.join(HYBRID_KEYWORDS), case=False, na=False).astype(int)

# Create on_site_score
df_new['on_site_score'] = ((df_new['work_from_home_score'] == 0) & (df_new['hybrid_score'] == 0)).astype(int)


df_new['competitive_salary_score'] = calculate_similarity(model, COMPETITIVE_SALARY_TEXT, df_0['DebugText'])


df_new['benefit_score']= calculate_similarity(model, BENEFIT_TEXT, df_0['DebugText'])


# Normalize 'pay_average' to the range 0 to 1
df_new['PayRangeMin_norm'] = (df_new['PayRangeMin'] - df_new['PayRangeMin'].min()) / (df_new['PayRangeMin'].max() - df_new['PayRangeMin'].min())
df_new['PayRangeMax_norm'] = (df_new['PayRangeMax'] - df_new['PayRangeMax'].min()) / (df_new['PayRangeMax'].max() - df_new['PayRangeMax'].min())
# Alaternate: using percentile as the score
#df_new['pay_percentile'] = df_new['pay_average'].rank(pct=True)

df_new['pay_average_norm'] = (df_new['PayRangeMin_norm'] + df_new['PayRangeMax_norm'])/2

df_new['distance_norm'] = (df_new['distance_km'] - df_new['distance_km'].min()) / (df_new['distance_km'].max() - df_new['distance_km'].min())

df_new['CompanyDetail.GroupSize'] = df_0 ['CompanyDetail.GroupSize']
df_new['CompanyDetail.Industry'] = df_0 ['CompanyDetail.Industry']
df_new['WorkType'] = df_0['WorkType']
df_new['CompanyDetail.HeadQuarters'] = df_0['CompanyDetail.HeadQuarters']

df_new['headquarter_in_australia'] = df_new['CompanyDetail.HeadQuarters'].apply(lambda loc: int(is_location_in_australia(loc, postcode_data, STATE_MAPPING)))

# output the data to storage
output_edited_jobs_path = os.path.join(script_dir, 'output', 'edited_jobs.csv')
df_new.to_csv(output_edited_jobs_path)
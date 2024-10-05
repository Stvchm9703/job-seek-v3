import pandas as pd
import numpy as np
import json
import regex as re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import jaccard_score, classification_report, confusion_matrix
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import LeaveOneOut, cross_val_score
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from itertools import combinations
from sentence_transformers import SentenceTransformer
import xgboost as xgb
import matplotlib.pyplot as plt
import shap


# -----------------------
# Constants and Mappings
# -----------------------

# Collaboration and Teamwork Keywords
COLLABORATION_TEAMWORK_TEXT = [   
    "Collaboration", "Teamwork", "Cooperation", "Communication", "Synergy",
    "Unity", "Partnership", "Coordination", "Support", "Trust",
    "Shared Goals", "Joint Effort", "Group Dynamics", "Collective Responsibility", "Mutual Respect",
    "Collaboration Tools", "Open Dialogue", "Team Spirit", "Collective Intelligence", "Shared Vision",
    "Networking", "Conflict Resolution", "Inclusivity", "Shared Success", "Cohesion",
    "Aligned Objectives", "Accountability", "Delegation", "Brainstorming", "Interdependence",
    "Peer Support", "Collaboration Strategies", "Feedback Loops", "Collaborative Culture", "Team Alignment",
    "Cooperation Skills", "Shared Leadership", "Consensus Building", "Cross-functional Teams", "Agile Teams",
    "Group Problem Solving", "Joint Planning", "Collaborative Innovation", "Team Building", "Effective Communication",
    "Collaborative Decision-making", "Interpersonal Skills", "Open-mindedness", "Facilitation" 
]

# Innovation and Growth Keywords
INNOVATION_GROWTH_TEXT = [
    "Innovation", "Growth", "Creativity", "Continuous Learning", "Professional Development",
    "Disruption", "Adaptability", "Experimentation", "Ideation", "Breakthroughs",
    "Skill Enhancement", "Knowledge Sharing", "Growth Mindset", "Change Management", "Agile Thinking",
    "Learning Culture", "Innovation Strategies", "Futuristic Thinking", "Emerging Technologies", "Research and Development",
    "Personal Growth", "Leadership Development", "Entrepreneurial Spirit", "Innovation Hubs", "Upskilling",
    "Creative Problem Solving", "Visionary Thinking", "Strategic Planning", "Thought Leadership", "Cross-disciplinary Learning",
    "Innovation Labs", "Growth Strategies", "Design Thinking", "Continuous Improvement", "Market Expansion",
    "Knowledge Management", "Talent Development", "Collaborative Innovation", "Learning Opportunities", "Growth Potential",
    "Future-oriented", "Creative Collaboration", "Intrapreneurship", "Growth Hacking", "Digital Transformation",
    "Innovative Solutions", "Transformational Leadership", "Lifelong Learning", "Cultural Innovation", "Strategic Innovation"
]

# Inclusivity and Respect Keywords
INCLUSIVITY_RESPECT_TEXT = [
    "diversity", "inclusion", "inclusive", "belonging", "equal opportunity", 
    "representation", "equity", "accessibility", "fairness", "cultural sensitivity", 
    "welcoming", "open-minded", "multicultural",
    "respect", "dignity", "empathy", "mutual understanding", "tolerance", 
    "courtesy", "kindness", "fair treatment", "non-discrimination", "supportive", 
    "valuing differences", "harassment-free"
]

# Competitive Salary Keywords
COMPETITIVE_SALARY_TEXT = [
    "Bonus", "Base Salary", "Performance Bonus", "Annual Bonus", "Signing Bonus",
    "Commission", "Profit Sharing", "Stock Options", "Equity", "Incentive Compensation",
    "Overtime Pay", "Shift Differential", "Hazard Pay", "Merit Increase", "Salary Package",
    "Pay Scale", "Hourly Rate", "Pay Grade", "Salary Band", "Compensation Package",
    "Profit Bonus", "Retention Bonus", "Longevity Pay", "Severance Pay", "Salary Review",
    "Salary Range", "Pay Increase", "Holiday Pay", "Performance Incentives", "Cash Bonus",
    "Stock Grants", "Restricted Stock Units", "Deferred Compensation", "End-of-Year Bonus", "Longevity Bonus",
    "Salary Structure", "Profit Sharing Plan", "Bonus Structure", "Sales Commission", "Guaranteed Salary",
    "Salary Enhancement", "Pay Raise", "Financial Incentives", "Cash Compensation", "Base Pay",
    "Pay Package", "Pay Rate", "Monetary Compensation", "Deferred Bonus", "Performance-Based Pay",
    "Discretionary Bonus", "Executive Compensation", "Equity Compensation", "Achievement Bonus", "Salary Progression",
    "Anniversary Bonus", "Earnings", "Income", "Fringe Benefits", "Flexible Compensation",
    "Variable Pay", "Tiered Pay", "Market-Competitive Pay", "Signing Incentive", "Competitive Pay",
    "On-Target Earnings", "Incentive Pay", "Quota-Based Pay", "Salary Plus Commission", "Commission Structure",
    "Variable Compensation", "Competitive Base Pay", "Sales Bonus", "Contingency Pay", "Revenue Sharing",
    "Milestone Bonus", "Bonus Pool", "Quota Achievement Bonus", "Base Compensation", "Production Bonus",
    "Sales Incentives", "Differential Pay", "Achievement Pay", "Project-Based Bonus", "Team Bonus",
    "Goal-Based Pay", "Incentive Plan", "Profit-Based Bonus", "Top-Up Pay", "Results-Driven Pay",
    "Compensation Review", "Goal Achievement Bonus", "Salary Progression", "Performance Evaluation Bonus", "Sales Target Bonus"
]

# Benefits Keywords
BENEFIT_TEXT = [
    "Benefits", "Allowance", "Travel Allowance", "Leave Loading", "Superannuation",
    "Super", "Health Insurance", "Dental Insurance", "Vision Insurance", "Life Insurance",
    "Disability Insurance", "Retirement Plan", "401(k) Matching", "Pension Plan", "Paid Time Off",
    "Vacation Pay", "Sick Leave", "Parental Leave", "Maternity Leave", "Paternity Leave",
    "Flexible Spending Account", "Wellness Program", "Gym Membership", "Fitness Reimbursement", 
    "Employee Assistance Program", "Tuition Reimbursement", "Education Assistance", 
    "Childcare Assistance", "Dependent Care", "Meal Allowance", "Housing Allowance",
    "Relocation Assistance", "Company Car", "Car Allowance", "Employee Discounts",
    "Profit Sharing Plan", "Stock Options", "Employee Stock Purchase Plan",
    "Transportation Allowance", "Commuter Benefits", "Professional Development",
    "Certification Reimbursement", "Continuing Education", "Training Programs",
    "Career Development", "Remote Work Stipend", "Home Office Allowance",
    "Phone Allowance", "Internet Allowance", "Work-from-Home Benefits",
    "Flexible Work Hours", "Paid Holidays", "Bereavement Leave",
    "Long Service Leave", "Sabbatical Leave", "Volunteer Time Off",
    "Wellness Days", "Employee Wellness Benefits", 
    "Financial Wellness Programs", "Legal Assistance", 
    "Identity Theft Protection", "Adoption Assistance", 
    "Fertility Benefits", "Pet Insurance", 
    "Relocation Support",  "Retirement Savings Plan",
    "Pension Contributions",  "Fringe Benefits",
    "Paid Parental Leave","Annual Leave","Sick Pay","Casual Leave","Holiday Pay",
    "Special Leave","Annual Bonus","Performance Bonus","Incentive Compensation",
    "Deferred Compensation","Profit Bonus","Signing Bonus","Retention Bonus",
    "Anniversary Bonus","Longevity Pay","Retirement Benefits","Severance Pay",
    "Bonus Structure","Employee Recognition Program","Achievement Awards",
    "Referral Bonus","Milestone Awards","Service Awards","Discounted Travel",
    "Company Events","Social Events","Paid Volunteer Days",
    "Health and Wellness Incentives","salary packaging","Discount hotel rates"
]

# State Mapping Dictionary
STATE_MAPPING = {
    "NSW": "New South Wales",
    "VIC": "Victoria",
    "QLD": "Queensland",
    "WA": "Western Australia",
    "SA": "South Australia",
    "TAS": "Tasmania",
    "ACT": "Australian Capital Territory",
    "NT": "Northern Territory",
    "New South Wales": "New South Wales",
    "Victoria": "Victoria",
    "Queensland": "Queensland",
    "Western Australia": "Western Australia",
    "South Australia": "South Australia",
    "Tasmania": "Tasmania",
    "Australian Capital Territory": "Australian Capital Territory",
    "Northern Territory": "Northern Territory"
}

# Work From Home (WFH) Keywords
WFH_KEYWORDS = [
    'work from home', 'remote work', 'telecommute', 'telecommuting', 'remote position',
    'remote opportunity', 'work remotely', 'flexible working location', 'home-based', 'flexible work arrangements'
]

# Hybrid Work Keywords
HYBRID_KEYWORDS = [
    'hybrid', 'hybrid work', 'hybrid working', 'hybrid role', 'hybrid position', 'hybrid model',
    'split between office and home', 'combination of office and remote', 'partially remote'
]

# Feature Weights
feature_weights = {
    'adjusted_job_title_similarity': 1.0,
    'adjusted_job_industry_similarity': 0.8,
    'adjusted_company_size': 0.7,
    'adjusted_job_sector': 0.7,
    'adjusted_company_culture': 0.6,
    'adjusted_work_model': 0.9,
    'adjusted_salary_expectation': 0.7,
    'adjusted_role_type': 0.8,
    'adjusted_distance_score': 1.0, 
    'descriptions_similarity_to_resume_norm': 1.0
}

# Size Mapping
SIZE_MAPPING = {
    'SIZE_A': 1,
    'SIZE_B': 2,
    'SIZE_C': 3,
    'SIZE_D': 4,
    'SIZE_E': 5,
    'SIZE_F': 6,
    'SIZE_G': 7,
    'SIZE_H': 8
}

# Work Type Mapping
WORK_TYPE_MAPPING = {
    'Full time': 1,
    'Contract/Temp': 2,
    'Part time': 3,
    'Casual/Vacation': 4
}

# Powers Dictionary for Number Conversions
POWERS = {'K': 10 ** 3, 'M': 10 ** 6, 'k': 10 ** 3, 'm': 10 ** 6, 'g': 10 ** 9, 'G': 10 ** 9}



# -----------------------
# Utility Functions
# -----------------------


def load_data(path: str) -> pd.DataFrame:
    from_json = json.load(open(path))
    #print(len(from_json[0]["result"]))
    df = pd.json_normalize(data=from_json[0]["result"])
    df = df.drop(
        columns=[
            "HittedKeywords",
            "CompanyDetail",
            "CompanyDetail.LastUpdate",
            "CompanyDetail.Linkedin",
            "CompanyDetail.Locations",
            "CompanyDetail.ReferenceId",
            "CompanyDetail.id",
            "CompanyDetail.Url",
            # "PostId",
            "PostUrl",
            "ExpiringDate",
            "id",
        ]
    )
    return df


def load_other_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
    

# Function to convert salary strings with K, M, etc.
def number_conversion(s, powers):
    if s[-1] in powers.keys():
        return float(s[:-1]) * powers[s[-1]]
    else:
        return float(s)


# Function to determine the time period in salary
def get_time_period(salary):
    if re.search(r'\bper hour\b|\b/hr\b', salary.lower()):
        return 'hourly'
    elif re.search(r'\bper month\b|\b/month\b', salary.lower()):
        return 'monthly'
    elif re.search(r'\bper week\b|\b/week\b', salary.lower()):
        return 'weekly'
    else:
        return 'yearly'


# Main feature conversion function with WorkType weighting
def feature_conversion(df: pd.DataFrame, powers: dict) -> pd.DataFrame:
    
    # Salary conversion function
    def convert_salary(salary, powers):
        time_period = get_time_period(salary)
        
        # Extract numerical values and modifiers (K, M, etc.)
        wage = re.findall(r"[\d|,|.]+[k|K|m|M|g|G]?", salary)
        wage = [i.replace(',', '') for i in wage]        
        wage = [number_conversion(i, powers) for i in wage if i.strip() != ""]
    
        # Adjust salary based on time period
        if time_period == 'hourly':
            wage = [i * 38 * 52 for i in wage if i is not None]  # Example: 38 hours/week, 52 weeks/year
        elif time_period == 'monthly':
            wage = [i * 12 for i in wage if i is not None]      # 12 months/year
        elif time_period == 'weekly':
            wage = [i * 52 for i in wage if i is not None]      # 52 weeks/year
        # No adjustment needed for 'yearly'
    
        return wage if wage else [np.nan, np.nan]  # Return list of None if no wage found
    
    # Function to extract PayRangeMin and PayRangeMax
    def extract_pay_range(pay_range):
        if len(pay_range) == 2:
            return pd.Series([pay_range[0], pay_range[1]])
        elif len(pay_range) == 1:
            return pd.Series([pay_range[0], pay_range[0]])
        else: 
            return pd.Series([np.nan, np.nan])  # Handle cases where no salary information is found
        
    # Define WorkType weights
    worktype_weights = {
        'Full Time': 1.0,
        'Contract/temp': 0.7,
        'Part Time': 0.5,
        'Casual/vacation': 0.3
    }
    
    # Standardize WorkType entries to match the keys in worktype_weights
    df['WorkType'] = df['WorkType'].str.strip().str.title()
    
    # Apply salary conversion and extract min/max ranges
    df_new_save = pd.DataFrame()
    df_new_save[['PostId']] = df[['PostId']]
    
    # Convert salary and extract pay range
    df_new_save[['PayRangeMin', 'PayRangeMax']] = df.apply(
        lambda row: extract_pay_range(convert_salary(row['PayRange'], powers)), axis=1
    )
    
    # Convert 'WorkType' to categorical
    df["WorkType"] = df["WorkType"].astype("category")
    
    # Map WorkType to weights
    df_new_save['WorkType'] = df['WorkType'].map(worktype_weights)
    
    # Handle WorkTypes not in the mapping by assigning a default weight of 1.0
    df_new_save['WorkType'] = df_new_save['WorkType'].fillna(1.0)
    
    # Apply the weight to PayRangeMin and PayRangeMax
    df_new_save['PayRangeMin'] = df_new_save['PayRangeMin'] * df_new_save['WorkType']
    df_new_save['PayRangeMax'] = df_new_save['PayRangeMax'] * df_new_save['WorkType']
    
    # Drop the 'WorkType' column if it's no longer needed
    df_new_save = df_new_save.drop(columns=['WorkType'])
    
    # Convert other columns to categorical as needed
    df["CompanyDetail.GroupSize"] = df["CompanyDetail.GroupSize"].astype("category")      
    df["CompanyDetail.Industry"] = df["CompanyDetail.Industry"].astype("category")
    
    # Optional: Handle missing PayRangeMin and PayRangeMax by filling with 0 or another strategy
    #df_new_save[['PayRangeMin', 'PayRangeMax']] = df_new_save[['PayRangeMin', 'PayRangeMax']].fillna(0)
    
    # Ensure PayRangeMin is less than or equal to PayRangeMax
    df_new_save['PayRangeMin'] = df_new_save[['PayRangeMin', 'PayRangeMax']].min(axis=1)
    df_new_save['PayRangeMax'] = df_new_save[['PayRangeMin', 'PayRangeMax']].max(axis=1)
    
    return df_new_save


# Function to parse location into suburb, city, and state
def parse_location(location, state_mapping):
    parts = location.split(',')

    if len(parts) == 1:
        # Handle case like "Sydney NSW"
        city_state = parts[0].strip().rsplit(' ', 1)
        if len(city_state) == 2 and city_state[1] in state_mapping:
            return pd.Series(['', city_state[0], '', state_mapping[city_state[1]]])
    
    if len(parts) == 2:
        # Handle cases like "Galiwin'ku, Katherine & Northern Australia NT"
        suburb = parts[0].strip()
        city_region = parts[1].strip().rsplit(' ', 1)[0]  # Strip off the state portion
        state_abbr = parts[1].strip().rsplit(' ', 1)[1]   # Get state abbreviation

        if '&' in city_region:
            city, region = city_region.split('&', 1)
            city = city.strip()  # Take everything before '&' as city
            region = region.strip()  # Take everything after '&' as region
        else:
            city = city_region
            region = ''

        if state_abbr in state_mapping:
            return pd.Series([suburb, city, region, state_mapping[state_abbr]])
    
    if len(parts) == 3:
        # Handle case like "Broadmeadow, Newcastle, Maitland & Hunter NSW"
        suburb = parts[0].strip()
        city = parts[1].strip()
        region_state = parts[2].strip().rsplit(' ', 1)

        if '&' in region_state[0]:
            region = region_state[0].split('&', 1)[0].strip()  # Only take the first word before '&'
        else:
            region = region_state[0].strip()

        state_abbr = region_state[1].strip()
        if state_abbr in state_mapping:
            return pd.Series([suburb, city, region, state_mapping[state_abbr]])

    # Return empty values if no match
    return pd.Series(['', '', '', ''])


# Function to get latitude and longitude of a location
def get_lat_lon(location_name, data):
    for location in data:
        if location['place_name'].lower() == location_name.lower():
            return location['latitude'], location['longitude']
    return None, None

# Example function to calculate the distance between two locations
def haversine_distance(lat1, lon1, lat2, lon2):
    from math import radians, cos, sin, sqrt, atan2

    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    # Differences between the coordinates
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    # Haversine formula
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Distance in kilometers
    distance = R * c
    return distance


# Function to geocode location
def geocode_location(location, data):
    parts = location.split(',')
    fallback_location = parts[0]
    lat, long = get_lat_lon(fallback_location, data)
    
    if not lat or not long:
        # If geocoding fails, try with city
        if len(parts) > 1:
            fallback_location = parts[1].strip()
            lat, long = get_lat_lon(fallback_location, data)
            
        # If still not found, try with region
        if (not lat or not long) and len(parts) > 2:
            fallback_location = parts[2].strip()
            lat, long = get_lat_lon(fallback_location, data)
        
        # If still not found, try with state 
        if (not lat or not long) and len(parts) > 3:
            fallback_location = parts[-1].strip()
            lat, long = get_lat_lon(fallback_location, data)   
    
    return (lat, long) if lat and long else (None, None)


def calculate_distances(df, user_location, postcode_data):
    # Geocode the user's location
    user_lat, user_long = geocode_location(user_location, postcode_data)

    # Initialize an array to hold distances
    distances = []
    
    # Calculate distance for each company location
    for index, row in df.iterrows():
        penalty = 0
        company_lat, company_long = None, None
                # Check if any location fields are available
        if row['suburb']:
            company_lat, company_long = geocode_location(row['suburb'], postcode_data)
            if company_lat == None and company_long == None:
                company_lat, company_long = geocode_location(row['city'], postcode_data)
                penalty +=10
                if company_lat == None and company_long == None:
                    company_lat, company_long = geocode_location(row['region'], postcode_data)
                    penalty +=15
                    if company_lat == None and company_long == None:
                        company_lat, company_long = geocode_location(row['state'], postcode_data)
                        penalty +=30
                
        elif row['city']:
            penalty +=10
            company_lat, company_long = geocode_location(row['city'], postcode_data)
            if company_lat == None and company_long == None:
                    company_lat, company_long = geocode_location(row['region'], postcode_data)
                    penalty +=15
                    if company_lat == None and company_long == None:
                        company_lat, company_long = geocode_location(row['state'], postcode_data)
                        penalty +=30
        elif row['region']:
            penalty +=25
            company_lat, company_long = geocode_location(row['region'], postcode_data)
            if company_lat == None and company_long == None:
                        company_lat, company_long = geocode_location(row['state'], postcode_data)
                        penalty +=30
            
        elif row['state']:
            penalty +=55
            company_lat, company_long = geocode_location(row['state'], postcode_data)
        

        if user_lat and user_long and company_lat and company_long:
            distance = haversine_distance(user_lat, user_long, company_lat, company_long)
          
            distance +=penalty
            
            distances.append(distance)
        else:
            distances.append(None)  # Handle cases where geocoding fails

    return distances


def preprocess_zeros_nan(new_jobs_df, user_location):
    new_jobs_df = new_jobs_df.copy()
    
    # Handle missing values (example: filling NaNs in 'distance_km' with the mean)
    new_jobs_df['distance_km'].fillna(new_jobs_df['distance_km'].mean(), inplace=True)
    
    # Apply condition
    mask = new_jobs_df['Locations'] != user_location
    
    # Fill zeros with the mean
    mean_distance_km = new_jobs_df['distance_km'].mean()
    new_jobs_df.loc[mask, 'distance_km'] = new_jobs_df.loc[mask, 'distance_km'].replace(0, mean_distance_km)
    
    # If 'PayRangeMin' or 'PayRangeMax' are critical, handle NaNs appropriately (e.g., filling with median)
    new_jobs_df['PayRangeMin'].fillna(new_jobs_df['PayRangeMin'].median(), inplace=True)
    
    # Convert 'None' and 'NaN' strings to np.nan
    new_jobs_df['PayRangeMax'].replace(['NaN', 'None'], np.nan, inplace=True)
    
    # Fill NaNs in 'PayRangeMax' with 'PayRangeMin'
    new_jobs_df['PayRangeMax'].fillna(new_jobs_df['PayRangeMin'], inplace=True)
    
    # Ensure 'PayRangeMax' is numeric
    new_jobs_df['PayRangeMax'] = pd.to_numeric(new_jobs_df['PayRangeMax'], errors='coerce')
    
    return new_jobs_df


def calculate_similarity(model, user_parameter, job_parameter):
    # Convert resume and job descriptions into embeddings using SBERT
    user_embedding = model.encode([user_parameter])
    job_embeddings = model.encode(job_parameter)

    # Calculate similarities between the resume and each job description
    similarities = cosine_similarity(user_embedding, job_embeddings)

    # Flatten the similarity array to get a list of similarity scores
    similarity_scores = similarities.flatten()
    
    return similarity_scores


# Function to convert text to binary vector based on the presence of keywords
def text_to_binary_vector(text, keywords):
    vectorizer = CountVectorizer(vocabulary=keywords, binary=True)
    vector = vectorizer.transform([text])
    return vector.toarray().flatten()


# Function to calculate Jaccard similarity with keywords
def calculate_jaccard_similarity(text, keywords):
    text_vector = text_to_binary_vector(text, keywords)
    
    # Create a reference vector where all keywords are considered present
    reference_vector = [1] * len(keywords)
    
    # Calculate Jaccard similarity score
    score = jaccard_score(text_vector, reference_vector, average='binary')
    return score


# Define the is_location_in_australia function with missing value check
def is_location_in_australia(location, postcode_data, state_mapping):
    if pd.isna(location):  # Handle missing values (NaN)
        return False
    
    location = str(location).lower()  # Convert to lowercase for case-insensitive matching
    
    # Step 1: Check if any state or state code is present in the location
    for code, state in state_mapping.items():
        if code.lower() in location or state.lower() in location:
            return True

    # Step 2: Check the postcode data for place name or state code matches
    for entry in postcode_data:
        if entry['place_name'].lower() in location or entry['state_code'].lower() in location:
            return True
    
    return False


# Function to compute similarity between two jobs
def compute_similarity(job_A, job_B, features_info):
    similarities = {}
    total_similarity = 0
    for feature, feature_type in features_info.items():
        value_A = job_A[feature]
        value_B = job_B[feature]
        
        # Handle missing values
        if pd.isnull(value_A) or pd.isnull(value_B):
            sim = 0  # Treat missing values as dissimilar
        else:
            if feature_type == 'continuous':
                sim = 1 - abs(value_A - value_B)
            elif feature_type == 'categorical':
                sim = 1 if value_A == value_B else 0
        similarities[feature] = sim
        total_similarity += sim
    # Compute average similarity
    avg_similarity = total_similarity / len(features_info)
    return similarities, avg_similarity

# Function to convert NumPy data types to native Python types
def convert_value(value):
    if isinstance(value, (np.integer, np.int32, np.int64)):
        return int(value)
    elif isinstance(value, (np.floating, np.float32, np.float64)):
        return float(value)
    elif isinstance(value, np.bool_):
        return bool(value)
    else:
        return value
    
    
# Update the function to handle numerical and categorical data differently
def create_feature_diff(row, job_features):
    job_A = job_features.loc[row['job_A_id']]
    job_B = job_features.loc[row['job_B_id']]
    
    # Separate numerical and categorical columns
    numerical_columns = job_features.select_dtypes(include=[np.number]).columns
    #categorical_columns = job_features.select_dtypes(include=['object', 'bool', 'category']).columns
    
    # Calculate differences for numerical columns
    num_diff = job_A[numerical_columns] - job_B[numerical_columns]
    
    # Calculate differences for categorical columns (1 if different, 0 if the same), but all categorical features are already encoded numerically
    #cat_diff = (job_A[categorical_columns] != job_B[categorical_columns]).astype(int)
    # Concatenate numerical and categorical differences
    #feature_diff = pd.concat([num_diff, cat_diff])
    
    
    feature_diff = num_diff
   
    return feature_diff.values.flatten()
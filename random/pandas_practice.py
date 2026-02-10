# Pandas Practice

"""
PANDAS CHEAT SHEET: From Basics to Interview-Level Methods

1. BASICS:
   - Import: import pandas as pd
   - Series: 1D labeled array (pd.Series([1,2,3], index=['a','b','c']))
   - DataFrame: 2D labeled data structure (pd.DataFrame({'col1': [1,2], 'col2': [3,4]}))

2. CREATING DATAFRAMES:
   - From dict: pd.DataFrame({'A': [1,2], 'B': [3,4]})
   - From list of dicts: pd.DataFrame([{'A':1, 'B':3}, {'A':2, 'B':4}])
   - From CSV: pd.read_csv('file.csv')
   - From Excel: pd.read_excel('file.xlsx')

3. DATA SELECTION:
   - Column: df['col'] or df.col
   - Multiple columns: df[['col1', 'col2']]
   - Rows by index: df.loc[0] or df.iloc[0]
   - Boolean indexing: df[df['col'] > 5]
   - Query: df.query('col > 5')

4. DATA MANIPULATION:
   - Add column: df['new_col'] = df['col1'] + df['col2']
   - Drop column: df.drop('col', axis=1)
   - Rename: df.rename(columns={'old': 'new'})
   - Sort: df.sort_values('col', ascending=False)
   - Reset index: df.reset_index(drop=True)

5. HANDLING MISSING DATA:
   - Check nulls: df.isnull().sum()
   - Drop nulls: df.dropna()
   - Fill nulls: df.fillna(value) or df.fillna(method='ffill')
   - Interpolate: df.interpolate()

6. GROUPING & AGGREGATION:
   - Group by: df.groupby('col').mean()
   - Multiple aggregations: df.groupby('col').agg({'col2': 'sum', 'col3': 'mean'})
   - Transform: df.groupby('col')['col2'].transform('mean')

7. MERGING & JOINING:
   - Concat: pd.concat([df1, df2])
   - Merge: pd.merge(df1, df2, on='key', how='left')
   - Join: df1.join(df2, how='outer')

8. PIVOT TABLES:
   - Basic pivot: df.pivot_table(values='val', index='row', columns='col', aggfunc='mean')
   - With margins: df.pivot_table(..., margins=True)

9. APPLY & MAP FUNCTIONS:
   - Apply to column: df['col'].apply(lambda x: x*2)
   - Apply to DataFrame: df.apply(lambda row: row['A'] + row['B'], axis=1)
   - Map: df['col'].map({'old_val': 'new_val'})

10. STRING OPERATIONS:
    - String methods: df['col'].str.upper(), .str.contains('pattern'), .str.split()
    - Extract: df['col'].str.extract(r'(\d+)')

11. TIME SERIES:
    - To datetime: pd.to_datetime(df['date_col'])
    - Set index: df.set_index('date_col')
    - Resample: df.resample('D').mean()
    - Shift: df['col'].shift(1)

12. ADVANCED METHODS (Interview Favorites):
    - Melt: pd.melt(df, id_vars=['col'], value_vars=['col2', 'col3'])
    - Stack/Unstack: df.stack(), df.unstack()
    - Explode: df.explode('list_col')
    - Cut/Qcut: pd.cut(df['col'], bins=3), pd.qcut(df['col'], q=4)
    - Rank: df['col'].rank(method='dense')
    - Rolling: df['col'].rolling(window=3).mean()
    - Expanding: df['col'].expanding().sum()
    - Diff: df['col'].diff()
    - Pct_change: df['col'].pct_change()

13. PERFORMANCE & MEMORY:
    - Dtypes: df.dtypes, df['col'].astype('int32')
    - Memory usage: df.memory_usage(deep=True)
    - Copy: df.copy(deep=True)
    - Categorical: df['col'].astype('category')

14. COMMON INTERVIEW PATTERNS:
    - Find duplicates: df.duplicated(), df.drop_duplicates()
    - Value counts: df['col'].value_counts()
    - Unique: df['col'].unique()
    - Nlargest/Nsmallest: df.nlargest(5, 'col')
    - Sample: df.sample(n=10, random_state=42)
    - Correlation: df.corr()
    - Describe: df.describe()

15. I/O OPERATIONS:
    - To CSV: df.to_csv('file.csv', index=False)
    - To Excel: df.to_excel('file.xlsx')
    - To JSON: df.to_json('file.json')
    - To SQL: df.to_sql('table', con=engine)

16. MULTI-INDEX:
    - Set multi-index: df.set_index(['col1', 'col2'])
    - Access: df.loc[('val1', 'val2')]
    - Reset: df.reset_index()

17. WINDOW FUNCTIONS:
    - Rolling: df.rolling(window=7).mean()
    - Expanding: df.expanding().std()
    - EWM: df.ewm(span=30).mean()

18. HANDLING LARGE DATASETS:
    - Chunks: pd.read_csv('file.csv', chunksize=1000)
    - Dask integration for very large data
    - Memory optimization: downcast dtypes

19. COMMON INTERVIEW QUESTIONS PATTERNS:
    - Group by with custom aggregation
    - Time series analysis and resampling
    - Handling missing data strategies
    - Pivot tables for data reshaping
    - Apply functions for complex transformations
    - Merging multiple datasets
    - Finding top N per group
    - Rolling statistics calculations

20. BEST PRACTICES:
    - Use vectorized operations over loops
    - Set appropriate dtypes to save memory
    - Use inplace=True for memory efficiency when possible
    - Chain operations: df.pipe(func1).pipe(func2)
    - Use categorical for repeated string values
"""

import pandas as pd

# basic pandas API usage examples

# requests

# ================================
# API USAGE WITH REQUESTS LIBRARY
# ================================

import requests
import json

# 1. BASIC GET REQUEST
def get_example():
    """Basic GET request with JSON response"""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()  # Parse JSON response
        print("GET Response:", json.dumps(data, indent=2))
        return data
    else:
        print(f"Error: {response.status_code}")
        return None

# 2. GET REQUEST WITH PARAMETERS
def get_with_params():
    """GET request with query parameters"""
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {
        'userId': 1,
        '_limit': 3
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        posts = response.json()
        print(f"Retrieved {len(posts)} posts for user 1")
        return posts
    return []

# 3. BASIC POST REQUEST
def post_example():
    """POST request with JSON data"""
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {
        "title": "Sample Post",
        "body": "This is a test post",
        "userId": 1
    }
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 201:  # Created
        created_post = response.json()
        print("POST Created:", json.dumps(created_post, indent=2))
        return created_post
    else:
        print(f"POST Error: {response.status_code}")
        return None

# 4. POST WITH AUTHENTICATION
def post_with_auth():
    """POST request with basic authentication"""
    url = "https://httpbin.org/post"
    data = {"key": "value"}
    
    # Basic auth
    auth = requests.auth.HTTPBasicAuth('username', 'password')
    
    response = requests.post(url, json=data, auth=auth)
    return response.json()

# 5. USING SESSIONS FOR MULTIPLE REQUESTS
def session_example():
    """Using requests.Session for connection reuse and cookie persistence"""
    with requests.Session() as session:
        # Set default headers for all requests in session
        session.headers.update({
            'User-Agent': 'Python-API-Client/1.0',
            'Authorization': 'Bearer your-token-here'
        })
        
        # First request
        response1 = session.get('https://jsonplaceholder.typicode.com/users/1')
        user = response1.json()
        print(f"User: {user['name']}")
        
        # Second request (reuses connection)
        response2 = session.get(f"https://jsonplaceholder.typicode.com/posts?userId={user['id']}")
        posts = response2.json()
        print(f"User has {len(posts)} posts")
        
        return user, posts

# 6. HANDLING ERRORS AND EXCEPTIONS
def api_with_error_handling():
    """Robust API call with error handling"""
    url = "https://jsonplaceholder.typicode.com/posts/99999"  # Non-existent
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises exception for 4xx/5xx status codes
        
        data = response.json()
        return data
        
    except requests.exceptions.Timeout:
        print("Request timed out")
    except requests.exceptions.ConnectionError:
        print("Connection error")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except json.JSONDecodeError:
        print("Invalid JSON response")
    
    return None

# 7. WORKING WITH JSON DATA
def json_manipulation():
    """Examples of working with JSON data from APIs"""
    # Sample API response
    api_response = {
        "users": [
            {"id": 1, "name": "John", "posts": [{"title": "Post 1"}, {"title": "Post 2"}]},
            {"id": 2, "name": "Jane", "posts": [{"title": "Post 3"}]}
        ]
    }
    
    # Convert to DataFrame
    import pandas as pd
    
    # Flatten nested JSON
    users_df = pd.json_normalize(api_response['users'])
    print("Users DataFrame:")
    print(users_df)
    
    # Extract posts
    posts_data = []
    for user in api_response['users']:
        for post in user['posts']:
            posts_data.append({
                'user_id': user['id'],
                'user_name': user['name'],
                'post_title': post['title']
            })
    
    posts_df = pd.DataFrame(posts_data)
    print("\nPosts DataFrame:")
    print(posts_df)
    
    return users_df, posts_df

# 8. ASYNC API CALLS (for multiple requests)
import asyncio
import aiohttp

async def async_api_calls():
    """Asynchronous API calls for better performance with multiple requests"""
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3"
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(session.get(url))
        
        responses = await asyncio.gather(*tasks)
        
        results = []
        for response in responses:
            if response.status == 200:
                data = await response.json()
                results.append(data)
        
        print(f"Retrieved {len(results)} posts asynchronously")
        return results

# 9. EVENT-STREAMING / WEBHOOK HANDLING
def handle_webhook():
    """Example of handling webhook data (common in event engines)"""
    # Simulate webhook payload
    webhook_data = {
        "event": "user.created",
        "timestamp": "2024-01-01T12:00:00Z",
        "data": {
            "user_id": 123,
            "email": "user@example.com",
            "metadata": {"source": "api"}
        }
    }
    
    # Process webhook
    event_type = webhook_data['event']
    user_data = webhook_data['data']
    
    print(f"Processing event: {event_type}")
    print(f"User ID: {user_data['user_id']}")
    
    # Convert to DataFrame for analysis
    df = pd.DataFrame([webhook_data['data']])
    return df

# 10. PAGINATION HANDLING
def handle_pagination():
    """Handling paginated API responses"""
    base_url = "https://jsonplaceholder.typicode.com/posts"
    all_posts = []
    page = 1
    
    while True:
        params = {'_page': page, '_limit': 10}
        response = requests.get(base_url, params=params)
        
        if response.status_code != 200:
            break
            
        posts = response.json()
        if not posts:  # No more data
            break
            
        all_posts.extend(posts)
        page += 1
        
        # Safety check to avoid infinite loops
        if page > 10:
            break
    
    print(f"Retrieved {len(all_posts)} posts total")
    return pd.DataFrame(all_posts)

# Usage examples (uncomment to test)
# get_example()
# get_with_params()
# post_example()
# session_example()
# api_with_error_handling()
# json_manipulation()
# handle_webhook()
# handle_pagination()


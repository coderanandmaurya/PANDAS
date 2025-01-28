import requests
import pandas as pd

# Initialize an empty list to store the results
all_movies = []

# Loop to fetch data from 1 to 428 pages
for i in range(1, 10):
    url = f'https://api.themoviedb.org/3/movie/top_rated?language=en-US&page={i}'
    headers = {
        "accept": "application/json",
        "Authorization": ""
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        # Check if request was successful
        if response.status_code == 200:
            temp_df = pd.DataFrame(response.json()['results'])[['id', 'title', 'overview', 'release_date', 'popularity', 'vote_average', 'vote_count']]
            all_movies.append(temp_df)  # Add the result to the list
            print(f"Fetched page {i}")
        else:
            print(f"Failed to fetch page {i}: Status code {response.status_code}")
            break  # Exit the loop if an error occurs
    except requests.exceptions.RequestException as e:
        print(f"Request error on page {i}: {e}")
        break  # Exit the loop in case of request error

# Combine all data into a single DataFrame
df = pd.concat(all_movies, ignore_index=True)

# Display the first few rows of the combined DataFrame
print(df.head())

# Save the DataFrame to a CSV file (optional)
df.to_csv("top_rated_movies.csv", index=False)

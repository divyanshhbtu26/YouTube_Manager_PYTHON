# 🚀 NOTE TO FUTURE ME:
# This script fetches a list of 5 random numbers between 100 and 1000 using a free public API (randomnumberapi.com).
# It's a simple example of making HTTP requests using the 'requests' library and handling JSON responses.
# Useful for testing, prototyping, or simulating random user-related data. 
# If the API goes offline or rate limits increase, consider mocking the response or using Python's built-in `random` module.

import requests

def fetch_random_user_freeApi():
    url = "http://www.randomnumberapi.com/api/v1.0/random?min=100&max=1000&count=5" 
    response = requests.get(url)
    data = response.json()

    if data:
        return data
    
    else:
        raise Exception("Error fetching data from the API")
    

def main():
    try:
        data = fetch_random_user_freeApi()
        print(data)
    except Exception as e:
        print(str(e))



if __name__ == "__main__":
    main()
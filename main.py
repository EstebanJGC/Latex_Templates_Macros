import requests
import matplotlib.pyplot as plt

# Define API key and endpoint URLs
apikey = "381e75c7a8d05df606626f3472695a3b"
search_url = "https://api.elsevier.com/content/search/scopus"

# Define search query parameters
query = "TITLE-ABS-KEY(deep learning)" # search for documents with "deep learning" in the title, abstract, or keywords.
params = {
    "query": query,
    "apiKey": apikey,
    "count": 25 # this is the max of results I can retrieve from the page
}

'''
for start in [0]:
    params["start"] = start  # Set start parameter to retrieve different pages of results
    response = requests.get(search_url, params=params).json()
    for result in response['search-results']['entry']:
        print(result['dc:title'])
        '''

'''
# Send search request and retrieve total number of search results
response = requests.get(search_url, params=params).json()
total_results = int(response['search-results']['opensearch:totalResults'])

print(f"Total number of search results: {total_results}")
'''

# Define start and end year
start_year = 2010
end_year = 2021

# Initialize list to store number of papers by year
papers_by_year = []

# Iterate over years and retrieve number of papers
for year in range(start_year, end_year+1):
    year_query = f"({query}) AND PUBYEAR = {year}"
    year_params = {
        "query": year_query,
        "apiKey": apikey
    }
    year_response = requests.get(search_url, params=year_params).json()
    year_results = int(year_response['search-results']['opensearch:totalResults'])
    papers_by_year.append(year_results)
    print(f"Number of papers in {year}: {year_results}")

# Plot number of papers by year
years = range(start_year, end_year+1)
plt.plot(years, papers_by_year)
plt.xlabel("Year")
plt.ylabel("Number of Papers")
plt.show()





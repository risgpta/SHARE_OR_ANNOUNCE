import requests
from bs4 import BeautifulSoup

# Define the URL you want to scrape
url = 'https://example.com'  # Replace with the URL you want to scrape

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the web page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract data from the parsed HTML, for example, getting the page title
    page_title = soup.title.string

    # Print the page tsoupitle
    print(f'Page Title: {page_title}')

    # You can now navigate the HTML structure and extract specific data as needed
    # For example, find and print all the links on the page
    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))

else:
    print(f'Failed to retrieve the web page. Status code: {response.status_code}')

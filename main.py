import requests
from bs4 import BeautifulSoup
import json

def fetch_csv_files_from_github(github_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # print(f"Accessing GitHub repository: {github_url}")
        response = requests.get(github_url, headers=headers)
        response.raise_for_status()
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all elements with the specific class
        elements_with_class = soup.find_all('div',class_='react-directory-truncate')
        
        csv_files = {}
        for element in elements_with_class:
            # Find all <a> tags within the current element
            a_tags = element.find_all('a')
            for a in a_tags:
                href = a.get('href')
                text = a.text
                # Check if it's a CSV file
                if href and text.endswith('.csv'):
                    csv_files[text]={
                        "name": text,
                        "url": f"https://github.com{href}" if not href.startswith('http') else href
                    }
            
        list=[]
        for i in csv_files:
            list.append({
            'name':csv_files[i]['name'],
            'url':csv_files[i]['url']
        })
    except Exception as e:
        print(f"Error: {str(e)}")
    return list

if __name__ == "__main__":
    github_url="https://github.com/salmansajidsattar/Microsoft_Fabric_Medallion_Architecture_Project/tree/main/Data"
    print(fetch_csv_files_from_github(github_url))
    # val=fetch_csv_files_from_github(github_url)
    
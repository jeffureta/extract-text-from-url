import requests
from bs4 import BeautifulSoup

def main():
    # prompt the user to enter the URL
    url = input ("Enter the URL: ")

    # Extract the text from the URL
    extracted_text = extract_text_from_url(url)

    # Let the user know that the text has been successfully extracted and saved to a file
    print("Text has been successfully extracted and saved to a file")
    
    # Save the extracted text to a file
    save_to_file(extracted_text)

def extract_text_from_url(url):
    try:
        # Fetch the content of the website
        response = requests.get(url)

        # Check if the request was successful
        response.raise_for_status()  
        
        # Parse the content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract text from the parsed HTML
        text = soup.get_text()
        
        return text

    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None
    
def save_to_file(text):
    with open("extracted-text.txt", "w", encoding="utf-8") as file:
        file.write(text)

main()

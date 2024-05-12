import re

def parse_input(input_text):
    # Regular expression pattern to match names and dates in MM/DD format
    pattern = r'([A-Za-z]+)\s+(\d{1,2}/\d{1,2})'
    
    # List to store extracted names and dates
    extracted_data = []
    
    # Find all matches in the input text
    matches = re.findall(pattern, input_text)
    
    # Iterate over matches and extract names and dates
    for match in matches:
        name, date = match
        extracted_data.append((name, date))
    
    return extracted_data

def main():
    # Input body of strings
    input_text = input("Enter a body of text containing names and dates (MM/DD): ")
    
    # Parse input text and extract names and dates
    extracted_data = parse_input(input_text)
    
    # Print extracted data
    print("Extracted data:")
    for name, date in extracted_data:
        print(f"(\"{name}\", \"{date}\")")

if __name__ == "__main__":
    main()

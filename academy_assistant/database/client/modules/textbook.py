import os
import urllib.parse

def get_module():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    textbook_folder = os.path.join(current_dir, '..', 'textbook_pdfs')
    
    textbooks = []
    
    # Iterate over files in the textbook_pdfs folder
    for filename in os.listdir(textbook_folder):
        if filename.lower().endswith('.pdf'):
            title = os.path.splitext(filename)[0]  # Use the file name (without extension) as the title
            # Construct the URL (update the URL path as needed for your deployment)
            encoded_filename = urllib.parse.quote(filename)
            url = f"https://academy2.selva-research.com/images/textbook_pdfs/{encoded_filename}"
            textbooks.append({
                'title': title,
                'textbook_url': url
            })
    return textbooks
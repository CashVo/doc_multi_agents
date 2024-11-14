# Iterate through the `content_sources` and scrape content from their URLs
# Save the raw data to disk
# A separate loader function will need to load these files back in at run time
# to chunk and index this data for use in a RAG Agent

from llama_index.core import SimpleDirectoryReader
from bs4 import BeautifulSoup as bs
from content_sources import content_sources
import json, csv, requests

def process_data():
    for source in content_sources:
        if source in {"glossary_terms"}:
            process_glossary(source, content_sources[source])
        else:
            process_urls(source, content_sources[source])
    print("Process data completed.")

def process_urls(source, urls):
    full_content = ""
    for url in urls:
        full_content = f'{full_content} \n\nsource: {url} \ncontent: \n'
        response = requests.get(url)
        soup = bs(response.content, "html.parser")
        source_tags = [
            tag for tag in soup.find_all(name=['h1','h2','h3','p','pre', 'dd', 'dt'])
            # Only interested in the "main-content" div
            if any((parent.name == "div" and parent.get("class") == [
                "main-content"
                ]) for parent in tag.parents)
        ]
        # Go through each of the elements and grab the text inside it
        for text in source_tags:
            full_content = full_content + '\n' + text.get_text()
        
    # Now write the content to disk as text file
    with open(f"raw/{source}.txt", "w", encoding="utf-8") as file:
        file.write(full_content)


def process_glossary(source, terms):
    #Write the data to file as a json format
    with open(f"raw/{source}.json", "w", encoding="utf-8") as file:
        json.dump(terms, file)


# Runs this function as a stand-alone script
if __name__ == "__main__":
    process_data()
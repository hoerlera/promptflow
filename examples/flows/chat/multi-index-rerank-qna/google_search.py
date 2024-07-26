from promptflow import tool
import requests
from googlesearch import search
from bs4 import BeautifulSoup

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(query: str) -> list:
    output = []
    results = search(query, num_results=5)
    for url in results:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                paragraphs = soup.find_all('p')
                page_text = "\n".join([p.get_text() for p in paragraphs])
                entry = {"text": page_text[:500],
                    "metadata": {"source": {"filename": url}},
                }
                output.append(entry)
        except:
            continue
    
    return output

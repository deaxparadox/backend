import requests
import json 
from typing import Any

URL: str = "http://localhost:8000/snippets/"
snippet: str = "http://localhost:8000/snippets/{}/"

response: requests.Response | None = None
current_data: str | None = None

def requesting(url: str) -> requests.Response:
    global response
    response = requests.get(url)


def load_data(res: requests.Response | None = None, return_data: bool = False) -> None:
    """
    Return a response to if return_data=True, 
    else return None
    """

    global current_data

    # check if response
    if not response:
        raise RuntimeError("No reponse")

    # load the json data
    if response.status_code == 200:
        current_data = json.loads(response.text)
    else:
        raise RuntimeError("Error reponse")

    # return data or None
    if return_data:
        return current_data
    else:
        return 

def show_data(data: Any | None = None) -> None:
    global current_data, response
    """
    show response text 
    # 
    and set current_data and response to NOne
    """
    if data:
        print(json.dumps(data, indent=4))
    else:
        print(json.dumps(current_data, indent=4))

    current_data, response  = None, None
    return



def main():
    res = requesting(URL)
    data = load_data(return_data=True)
    # show_data()

    for data in data:
        id = data.get("id", None)
        requesting(snippet.format(str(id)))
        load_data()
        show_data()
        

if __name__ == "__main__":
    main()
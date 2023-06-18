import requests

index = input("Enter index of pokemon: ")
target_url = f"http://pokeapi.co/api/v2/pokemon/{index}/"

def make_request():
    response = requests.get(target_url)
    response_json = response.json()
    status_code = response.status_code

    print("HTTP Status Code: ", status_code)
    print(response.headers)
    print("Pokemon Name: ", response_json["name"])

make_request()

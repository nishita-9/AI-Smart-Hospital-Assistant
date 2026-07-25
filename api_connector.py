import requests

def hospital_info():
    url = "https://jsonplaceholder.typicode.com/users/1"

    try:
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            return {
                "Hospital": data["company"]["name"],
                "City": data["address"]["city"]
            }

        else:
            return "Unable to connect to server."

    except Exception:
        return "API Connection Failed."
import requests
import sys


HELLOSALUT_API_URL = "https://fourtonfish.com/hellosalut"

# Define main script
def main():
    """
    Hello, salut!のAPIを叩いてレスポンスをprintするだけ。
    ※ 国コードやグローバルIPからその地域の挨拶を返してくれるAPI
    """
    params = {
        "lang": "ja",
    } 

    response = requests.get(HELLOSALUT_API_URL, params=params)

    if response.status_code != 200:
        raise Exception("Request failed with status code: " + str(response.status_code))

    if response.status_code == 200:
        data = response.json()
        print(data)

if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        message = (
            f"Task failed: {str(err)}"
        )
        print(message)
        sys.exit(1)

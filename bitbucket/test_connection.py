from bitbucket.client import get_session

def test_connection():
    session = get_session()
    response = session.get("https://api.bitbucket.org/2.0/user")

    print("Status:", response.status_code)
    print(response.text)

if __name__ == "__main__":
    test_connection()

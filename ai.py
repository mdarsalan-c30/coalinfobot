import requests

url = "https://chatgpt-api8.p.rapidapi.com/"

# Get user input
user_query = input("Enter your query: ")

payload = [
    {
        "content": user_query,
        "role": "user"
    }
]
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "09df95459amsh5748b5ea502e72dp1742b3jsnb0494b893acb",
    "X-RapidAPI-Host": "chatgpt-api8.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())

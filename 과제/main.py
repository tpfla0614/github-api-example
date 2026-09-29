import requests

url = "https://api.github.com/repos/python/cpython"

response = requests.get(url)

data = response.json()

print("저장소 이름:", data["name"])
print("설명:", data["description"])
print("별 개수:", data["stargazers_count"])
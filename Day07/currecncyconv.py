import requests

url1 = "https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=b0fd1ae062c03692b91b"
print (url)


response = requests.get(url1)
# requests.get(url,params={"q":"Jaipur", "appid"="e9185b28e9969fb7a300801eb026de9c"})
response.content

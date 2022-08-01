import requests as req

res = req.get('http://t1.daumcdn.net/friends/prod/editor/dc8b3d02-a15a-4afa-a88b-989cf2a50476.jpg')

print(res.status_code)

print(res.text)
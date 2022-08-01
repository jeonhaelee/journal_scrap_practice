# 이미지 저장하기
# file_path = 'C:/py_work/day10/kitty-cat-kitten-pet-45201.jpeg'

# img_bin = None

# with open(file_path, 'rb') as f:
#     img_bin = f.read()
    
# with open('test.jpeg', 'wb') as f:
#     f.write(img_bin)
    
# 1. url을 이용해서 웹상의 이미지를 다운로드

url = 'https://images.pexels.com/photos/1543793/pexels-photo-1543793.jpeg?auto=compress&cs=tinysrgb&w=600'
    
import requests as req

res = req.get(url)

# print(res.status_code) # 잘 연결되었는지 확인. 200이 나오면 잘 연결된 것임.

bin_data = res.content

with open('test2.jpeg', 'wb') as f:
    f.write(bin_data)




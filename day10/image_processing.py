from PIL import Image
import numpy as np

im = Image.open("C:/py_work/day10/img/cat_0.jpeg")
# im.show()

# im.size # 이미지 사이즈를 튜플로 알려줌.
# im.width # 이미지 너비
# im.height # 이미지 높이

# 픽셀 정보 가져와서 분석 -> 3차원 배열
im_arr = np.array(im)

# print(im_arr.shape)
# print(im_arr[0][0][0]) # (0, 0) 픽셀의 r값
# print(im_arr[0][0][1]) # (0, 0) 픽셀의 g값
# print(im_arr[0][0][2]) # (0, 0) 픽셀의 b값



### 중복된 이미지 제거
# 1. 이미지를 순회하면서 픽셀을 가져와 대조
# 2. 픽셀 값이 완전히 같으면 동일한 이미지
# 3. 해당 이미지를 삭제.

target_img1 = 'C:/py_work/day10/img/cat_0.jpeg'
target_img2 = 'C:/py_work/day10/img/cat_25.jpeg'
target_img3 = 'C:/py_work/day10/img/cat_3.jpeg'

def compare_img(img1, img2):
    loaded_img1 = Image.open(img1)
    loaded_img2 = Image.open(img2)
    
    if loaded_img1.size != loaded_img2.size:
        return False
    
    img_arr1 = np.array(loaded_img1)
    img_arr2 = np.array(loaded_img2)

    for y in range(loaded_img1.height):
        for x in range(loaded_img1.width):
            # np.array_equal()
            if not np.array_equal(img_arr1[y][x], img_arr2[y][x]):
                return False

    return True


rst = compare_img(target_img1, target_img2)
print(rst)




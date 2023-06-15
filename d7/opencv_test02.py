import cv2
# 01. 일반 이미지
#img = cv2.imread('./images/bambi.jpg')
#cv2.imshow('Original', img)

# 02. 그레이스케일 이미지
#img = cv2.imread('./images/bambi.jpg', cv2.IMREAD_GRAYSCALE)
#cv2.imshow('Original', img)

# 03. 이미지 사이즈 축소
#img = cv2.imread('./images/bambi.jpg', cv2.IMREAD_GRAYSCALE)
#img_small = cv2.resize(img, (200, 120))
#cv2.imshow('small', img_small)

# 04. 원본 그대로 두고 흑백 추가
# img = cv2.imread('./images/bambi.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Original', img)
# cv2.imshow('Gray', gray)

# 05. 이미지 자르기
# img = cv2.imread('./images/bambi.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# height, width, channel = img.shape
# print(height, width, channel)

# img_crop = img[:, :int(width / 2)]        # height, width
# gray_crop = gray[int(width / 2):, :]      # height, width

# cv2.imshow('Original half', img_crop)
# cv2.imshow('Gray half', gray_crop)


# 06. 이미지 블러
img = cv2.imread('./images/bambi.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
height, width, channel = img.shape
print(height, width, channel)

img_crop = img[:, :int(width / 2)]          # height, width
gray_crop = gray[int(width / 2):, :]        # height, width

img_blur = cv2.blur(img_crop, (5,10))       # 숫자가 클수록 더 많이 블러

cv2.imshow('Original half', img_crop)
cv2.imshow('Blur half', img_blur)
cv2.imshow('Gray half', gray_crop)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
class Cartoonizer:
"""Cartoonizer effect
A class that applies a cartoon effect to an image.
The class uses a bilateral filter and adaptive thresholding to create a cartoon
effect.
"""
def _init_(self):
pass
def render(self, img_path):
img_rgb = cv2.imread(img_path) # Correct indentation here!
if img_rgb is None:
raise ValueError(f"Error: Could not read image file '{img_path}'.
Check the file path.")
img_rgb = cv2.resize(img_rgb, (1366, 768))
numDownSamples = 2 # Number of downscaling steps
numBilateralFilters = 50 # Number of bilateral filtering steps
# -- STEP 1: Downsample the image
img_color = img_rgb.copy() for _ in range(numDownSamples):
img_color = cv2.pyrDown(img_color)
# Apply bilateral filter multiple times
for _ in range(numBilateralFilters):
img_color = cv2.bilateralFilter(img_color, 9, 9, 7)
# Upsample the image back to original size
for _ in range(numDownSamples):
img_color = cv2.pyrUp(img_color)
# -- STEP 2 & 3: Convert to grayscale and apply median blur
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
img_blur = cv2.medianBlur(img_gray, 3)
# -- STEP 4: Detect and enhance edges
img_edge = cv2.adaptiveThreshold(img_blur, 255,
cv2.ADAPTIVE_THRESH_MEAN_C,
cv2.THRESH_BINARY, 9, 2)
# -- STEP 5: Convert back to color and combine with color image
img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2BGR)
img_edge = cv2.resize(img_edge, (img_color.shape[1],
img_color.shape[0]))
cartoon = cv2.bitwise_and(img_color, img_edge)
return cartoon
# Initialize Cartoonizer
cartoonizer = Cartoonizer()
# Image file path
file_name = "C:\Users\karth\Desktop\file\screenshot.jpg"
# Ensure this path is correct
# Apply the cartoon effect
cartoon_image = cartoonizer.render(file_name) # Save and display the result
cv2.imwrite("Cartoon_version.jpg", cartoon_image)
cv2.imshow("Cartoon Image", cartoon_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

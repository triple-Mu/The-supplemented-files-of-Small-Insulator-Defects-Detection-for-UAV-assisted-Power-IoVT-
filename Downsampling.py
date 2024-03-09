import cv2

def bicubic_downsampling(image_path, scale_percent):

    img = cv2.imread(image_path)


    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)


    resized = cv2.resize(img, dim, interpolation=cv2.INTER_CUBIC)


    cv2.imshow("Original Image", img)
    cv2.imshow("Downsampled Image using Bicubic Interpolation", resized)


    cv2.waitKey(0)
    cv2.destroyAllWindows()


image_path = 'path_to_your_image.jpg'
scale_percent = 50
bicubic_downsampling(image_path, scale_percent)

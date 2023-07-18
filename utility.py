import os
import cv2


def load_images(input_folder):
    images = []
    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
            img = cv2.imread(os.path.join(input_folder, filename), cv2.IMREAD_GRAYSCALE)
            if img is not None:
                images.append(img)
    return images


def save_images(images, output_folder):
    for i, img in enumerate(images, start=1):
        new_path = os.path.join(output_folder, f"{i}.jpg")
        cv2.imwrite(new_path, img)


def save_image(image, path):
    cv2.imwrite(path, image)


def get_filename(filename):
    name = os.path.splitext(filename)[0]
    return name


def concatenate_filename(filename, string):
    base, ext = os.path.splitext(filename)
    new_filename = f"{base}{string}{ext}"
    return new_filename

import os
import random
import csv

def generate_annotation_files(image_dir, output_dir, num_samples=19):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    classes = [d for d in os.listdir(image_dir) if os.path.isdir(os.path.join(image_dir, d))]

    for target_class in classes:
        print(f"generating annotation file for class: {target_class}")

        target_class_dir = os.path.join(image_dir, target_class)
        annotation_file = os.path.join(output_dir, f"annotation_{target_class}.csv")

        annotations = []
        target_class_images = os.listdir(target_class_dir)
        for image in target_class_images:
            annotations.append((image, 1))

        for other_class in classes:
            if other_class == target_class:
                continue

            other_class_dir = os.path.join(image_dir, other_class)
            other_class_images = os.listdir(other_class_dir)

            sampled_images = random.sample(other_class_images, min(num_samples, len(other_class_images)))
            for image in sampled_images:
                annotations.append((image, 0))

        random.shuffle(annotations)

        with open(annotation_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["filename", "label"])  # Write header
            writer.writerows(annotations)

        print(f"Annotation file for '{target_class}' saved at: {annotation_file}")

image_dir = '/Users/saumyamishra/Desktop/Ashoka/sem 5/Introduction to Machine Learning/final presentation/data'  # Directory containing class subdirectories
output_dir = '/Users/saumyamishra/Desktop/Ashoka/sem 5/Introduction to Machine Learning/final presentation/final_annotation_balanced'  # Directory to save annotation files

generate_annotation_files(image_dir, output_dir)

# import pandas as pd
# import os
# import requests
# from PIL import Image
# from io import BytesIO

# # Load the CSV file
# file_path = "/Users/mac/Downloads/fitzpatrick17k_people_of_color.csv"  # Replace with the path to your CSV file
# df = pd.read_csv(file_path)

# # Base directory where all images will be saved
# base_dir = "/Users/mac/dataset/skin_diseases_images"

# # Create base directory if it doesn't exist
# if not os.path.exists(base_dir):
#     os.makedirs(base_dir)

# # Function to download an image and save it to the appropriate directory
# def save_image(url, folder_path, image_name):
#     try:
#         # Fetch the image from the URL
#         response = requests.get(url)
#         response.raise_for_status()  # Check if the request was successful
#         image = Image.open(BytesIO(response.content))

#         # Create folder if it doesn't exist
#         os.makedirs(folder_path, exist_ok=True)

#         # Save the image
#         image_path = os.path.join(folder_path, f"{image_name}.jpg")
#         image.save(image_path)
#         print(f"Saved: {image_path}")

#     except Exception as e:
#         print(f"Failed to download {url}: {e}")

# # Iterate through each row in the DataFrame and save images accordingly
# for index, row in df.iterrows():
#     label = row['label']
#     three_partition_label = row['three_partition_label']
#     nine_partition_label = row['nine_partition_label']
#     image_url = row['url']
#     image_name = row['md5hash']

#     # Folder paths based on labels
#     label_folder = os.path.join(base_dir, "by_label", label)
#     three_partition_folder = os.path.join(base_dir, "by_three_partition", three_partition_label)
#     nine_partition_folder = os.path.join(base_dir, "by_nine_partition", nine_partition_label)

#     # Save images in different groupings
#     save_image(image_url, label_folder, image_name)
#     save_image(image_url, three_partition_folder, image_name)
#     save_image(image_url, nine_partition_folder, image_name)

import pandas as pd

# Load the original CSV file
file_path = "/Users/mac/Downloads/fitzpatrick17k_people_of_color.csv"  # Replace with your actual file path
df = pd.read_csv(file_path)

# Count occurrences of each disease in the 'label' column
top_diseases = df['label'].value_counts().nlargest(20)

# Extract the top 10 diseases
top_diseases_list = top_diseases.index.tolist()

# Create a CSV file for each of the top 10 diseases
for disease in top_diseases_list:
    # Filter the data for the current disease
    disease_df = df[df['label'] == disease]
    
    # Generate a safe file name for each disease
    safe_disease_name = disease.replace(" ", "_").replace("/", "_")
    
    # Save the filtered data to a new CSV file
    output_path = f"/Users/mac/dataset/{safe_disease_name}.csv"
    disease_df.to_csv(output_path, index=False)
    print(f"Generated CSV file for {disease}: {output_path}")


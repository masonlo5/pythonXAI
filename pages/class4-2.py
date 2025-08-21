import streamlit as st
import os

st.title("picture")
# st.image
st.image("image/mincraft.png", width=300)

image_folder = "image"
image_files = os.listdir(image_folder)
for file in image_files:
    if not file.endswith(('.jpg', '.png', '.jpeg')):
        image_files.remove(file)
st.write(image_files)

image_size = st.number_input("pictures size", min_value=50, max_value=500, step=50, value=50)

for image_file in image_files:
    st.image(f"{image_folder}/{image_file}", width=image_size)

for image_file in image_files:
    st.image(f"{image_folder}/{image_file}", use_container_width=True)

selected_image = st.selectbox("選擇圖片", image_files, index=0)
st.image(f"{image_folder}/{selected_image}", width=300)
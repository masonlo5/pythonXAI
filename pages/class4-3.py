import streamlit as st
import os

st.title("store")
image_folder = "image"
image_files = os.listdir(image_folder)
for file in image_files:
    if not file.endswith(('.jpg', '.png', '.jpeg')):
        image_files.remove(file)

if "products" not in st.session_state:
    st.session_state.products = {}

for image_file in image_files:
    product_name = image_file[:-4]  # Remove file extension
    if product_name not in st.session_state.products:
        st.session_state.products[product_name] = {
            "price": 10,
            "stock": 10,
            "image": f"{image_folder}/{image_file}",
        }
# st.session_state.products
# st.session_state.products = ['mincraft': {'price': 10, 'stock': 10, 'image': 'image/mincraft.png'},
#                           "block": {"price": 10, "stock": 10, "image": "image/block.png"},
#                           "steve": {"price": 10, "stock": 10, "image": "image/steve.png"}
# }
# st.session_state.products["mincraft"]["price"]
# st.session_state.products["block"]["stock"]
# st.session_state.products["steve"]["image"]

st.title("Product Catalog")
cols = st.columns(3)
i = 0

for product_name, details in st.session_state.products.items():
    # inside product_name are the items names, inside detail are the items details and dictionary
    # {"price": 10, "stock": 10, "image": "image/mincraft.png"}
    with cols[i % len(cols)]:
        st.image(details["image"], use_container_width=True)
        st.write(f"### {product_name}")
        st.write(f"Price: ${details['price']}")
        st.write(f"Stock: {details['stock']}")
        if st.button(f"buy {product_name}", key=f"{product_name}"):
            st.session_state.products[product_name]["stock"] -= 1
            st.rerun()
        i += 1

# add resources
st.title("Add Resources")
col_1, col_2, col_3 = st.columns(3)
with col_1:
    selected_product = st.selectbox("Select Product", st.session_state.products.keys())
with col_2:
    new_stock = st.number_input("New Stock", min_value=1, step=1)
    new_price = st.number_input("New Price", min_value=0, step=1)
with col_3:
   if st.button("add resources"):
       st.session_state.products[selected_product]["stock"] += new_stock
       st.session_state.products[selected_product]["price"] = new_price
       st.success("Resources added successfully!")
       st.rerun()


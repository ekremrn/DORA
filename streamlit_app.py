import os
import requests
import streamlit as st

from PIL import Image
from helpers.data_handlers import image_to_base64


API_URL = str(os.getenv("API_URL"))

def expand2square(img_path, background_color):
    pil_img = Image.open(img_path)
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result


def main():
    st.set_page_config(
        page_title="Dora: Product Finder",
        page_icon="./images_and_figs/icon.png",
        initial_sidebar_state="expanded",
    )

    logo_col, title_col = st.columns([1, 3])

    with logo_col:
        st.image("./images_and_figs/long_icon.jpg", use_column_width=True)
    with title_col:
        st.title(
            "Dora: Product Finder",
        )
    st.write("Ürün fotoğrafını yükle ürünü bul")
    st.markdown(
        """
        <style>
        a.product-link{
            color: inherit;
            text-decoration: none;
        }
        .container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            border: 1px solid #E6E6E6;
        }
        .product-card {
            width: 200px;
            margin: 20px;
            padding: 10px;
            border: 1px solid #d3d3d3;
            border-radius: 10px;
            text-align: left;
        }
        .product-image {
            width: 150px;
            height: 150px;
            object-fit: contain;
            margin-bottom: 10px;
        }
        .product-title {
            font-weight: normal;
            font-size: 16px;
            margin-bottom: 5px;
            text-align: left;
        }
        .product-price {
            font-weight: bold;
            margin-bottom: 5px;
            text-align: left;
            color: #b22222;
        }
        .product-brand {
            font-size: 16px;
            font-weight: bold;
            margin-bottom: 5px;
            text-align: left;
        }
        .stButton>button{
            height: 2em;
            margin-top: 40%;
            margin-left: 20%;
            width: 70%;
            font-size: 50px;
            border: 3px solid;
            border-radius: 100px;
            padding: 1px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    uploaded_file = st.file_uploader("Fotoğraf yükle", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        pil_img = expand2square(uploaded_file, "white")
        uploaded_img_col, button_col = st.columns([1, 1])
        with uploaded_img_col:
            st.image(pil_img, caption="Yüklenen Fotoğraf", use_column_width=True)
        with button_col:
            run_button = st.button("Benzer Ürünleri Bul")
        if run_button:
            input_image = Image.open(uploaded_file) 
            request_input = {"data" : image_to_base64(input_image)}
            response = requests.post(API_URL, json=request_input)
            if response.status_code != 200:
                return
            result = response.json()
            cols = st.columns(3)

            for i, product in enumerate(result):

                price = "{} {}".format(product.get("price").get("discounted") 
                                       if product.get("price").get("discounted") 
                                       else product.get("price").get("original"),
                                       product.get("price").get("currency"))
                with cols[i % 3]:
                    st.markdown(
                        """
                        <a class="product-link" href={}>
                            <div class="product-card">
                                <img class="product-image" src="{}" alt="Product Image">
                                <div class="product-brand">{}</div>
                                <div class="product-title">{}</div>
                                <div class="product-price">{}</div>
                            </div>
                        </a>
                        """.format(
                            product.get("url"),
                            product.get("thumb_image").get("platform_url"),
                            product.get("brand"),
                            product.get("name"),
                            price,
                        ),
                        unsafe_allow_html=True,
                    )

                st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()

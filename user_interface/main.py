from PIL import Image
import streamlit as st


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
        page_icon="./images/icon.png",
        initial_sidebar_state="expanded",
    )

    logo_col, title_col = st.columns([1, 3])

    with logo_col:
        st.image("./images/long_icon.jpg", use_column_width=True)
    with title_col:
        st.title(
            "Dora: Product Finder",
        )
    st.write("Gelen fotoğraftakine en çok benzeyen 10 ürünü listeleyen uygulama.")
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
        </style>
        """,
        unsafe_allow_html=True,
    )

    uploaded_file = st.file_uploader("Fotoğraf yükle", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        pil_img = Image.open(uploaded_file)
        uploaded_img_col, button_col = st.columns([1, 1])
        with uploaded_img_col:
            st.image(pil_img, caption="Yüklenen Fotoğraf", use_column_width=True)
        with button_col:
            run_button = st.button("Benzer Ürünleri Bul", use_container_width=True)
        if run_button:
            result = [
                {
                    "title": "Ürün 1",
                    "price": "100 TL",
                    "image": "urun1.jpg",
                    "brand": "abidas",
                    "link": "https://urun1-link.com",
                },
                {
                    "title": "Ürün 2",
                    "price": "150 TL",
                    "image": "urun2.jpg",
                    "brand": "abidas",
                    "link": "https://urun2-link.com",
                },
                {
                    "title": "Ürün 3",
                    "price": "75 TL",
                    "image": "urun3.jpg",
                    "brand": "abidas",
                    "link": "https://urun3-link.com",
                },
                {
                    "title": "Ürün 4",
                    "price": "200 TL",
                    "image": "urun4.jpg",
                    "brand": "abidas",
                    "link": "https://urun4-link.com",
                },
                {
                    "title": "Ürün 5",
                    "price": "120 TL",
                    "image": "urun5.jpg",
                    "brand": "abidas",
                    "link": "https://urun5-link.com",
                },
                {
                    "title": "Ürün 6",
                    "price": "90 TL",
                    "image": "urun6.jpg",
                    "brand": "abidas",
                    "link": "https://urun6-link.com",
                },
                {
                    "title": "Ürün 7",
                    "price": "80 TL",
                    "image": "urun7.jpg",
                    "brand": "abidas",
                    "link": "https://urun7-link.com",
                },
                {
                    "title": "Ürün 8",
                    "price": "160 TL",
                    "image": "urun8.jpg",
                    "brand": "abidas",
                    "link": "https://urun8-link.com",
                },
                {
                    "title": "Ürün 9",
                    "price": "110 TL",
                    "image": "urun9.jpg",
                    "brand": "abidas",
                    "link": "https://urun9-link.com",
                },
                {
                    "title": "Ürün 10",
                    "price": "135 TL",
                    "image": "urun10.jpg",
                    "brand": "abidas",
                    "link": "https://urun10-link.com",
                },
            ]

            cols = st.columns(3)

            for i, product in enumerate(result):
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
                            product["link"],
                            "data:image/jpeg;base64,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",
                            product["brand"],
                            product["title"],
                            product["price"],
                        ),
                        unsafe_allow_html=True,
                    )

                st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()

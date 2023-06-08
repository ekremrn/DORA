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
            result = [
                {
                    "title": "Breaknet Beyaz Erkek Sneaker FX8707",
                    "price": "999 TL",
                    "image": "https://cdn.dsmcdn.com/mnresize/400/-/ty863/product/media/images/20230503/22/338916317/89893993/2/2_org.jpg",
                    "brand": "adidas",
                    "link": "https://www.trendyol.com/adidas/breaknet-beyaz-erkek-sneaker-p-50764295",
                },
                {
                    "title": "Vs Pace Beyaz Erkek Sneaker Gw6665 GW6665",
                    "price": "919 TL",
                    "image": "https://cdn.dsmcdn.com/mnresize/400/-/ty863/product/media/images/20230503/22/338916317/609027415/2/2_org.jpg",
                    "brand": "adidas",
                    "link": "https://www.trendyol.com/adidas/vs-pace-beyaz-erkek-sneaker-gw6665-p-376892778",
                },
                {
                    "title": "Streetcheck Beyaz Kadın Sneaker STREETCHECK",
                    "price": "1.749 TL",
                    "image": "https://cdn.dsmcdn.com/mnresize/1200/1800/ty712/product/media/images/20230203/4/272633299/848043657/1/1_org_zoom.jpg",
                    "brand": "adidas",
                    "link": "https://www.trendyol.com/adidas/streetcheck-beyaz-kadin-sneaker-p-641589486",
                },
                {
                    "title": "Breaknet Court Gy9586 GY9586",
                    "price": "1.200 TL",
                    "image": "https://cdn.dsmcdn.com/mnresize/1200/1800/ty863/product/media/images/20230503/22/338916317/552502959/2/2_org_zoom.jpg",
                    "brand": "adidas",
                    "link": "https://www.trendyol.com/adidas/breaknet-court-gy9586-p-345598082",
                },
                {
                    "title": "Streetcheck Beyaz Kadın Sneaker STREETCHECK",
                    "price": "1.749 TL",
                    "image": "https://cdn.dsmcdn.com/mnresize/1200/1800/ty712/product/media/images/20230203/4/272633299/848043657/1/1_org_zoom.jpg",
                    "brand": "adidas",
                    "link": "https://www.trendyol.com/adidas/streetcheck-beyaz-kadin-sneaker-p-641589486",
                },
                {
                    "title": "Breaknet Beyaz Erkek Sneaker BREAKNET",
                    "price": "1.499 TL",
                    "image": "https://cdn.dsmcdn.com/mnresize/1200/1800/ty536/product/media/images/20220919/11/176877988/573186316/1/1_org_zoom.jpg",
                    "brand": "adidas",
                    "link": "https://www.trendyol.com/adidas/breaknet-beyaz-erkek-sneaker-p-355142090",
                },
                {
                    "title": "Siyah - Sneaker Grand Court 2.0 18077330",
                    "price": "1.129,99 TL",
                    "image": "https://cdn.dsmcdn.com/mnresize/1200/1800/ty524/product/media/images/20220906/20/169905021/560202571/1/1_org_zoom.jpg",
                    "brand": "adidas",
                    "link": "https://www.trendyol.com/adidas/siyah-sneaker-grand-court-2-0-p-349226669",
                },
                {
                    "title": "Sneaker Grand Court 2.0 El K 18037312",
                    "price": "1.129,99 TL",
                    "image": "https://cdn.dsmcdn.com/mnresize/1200/1800/ty773/product/media/images/20230310/21/300624823/882492090/1/1_org_zoom.jpg",
                    "brand": "adidas",
                    "link": "https://www.trendyol.com/adidas/sneaker-grand-court-2-0-el-k-p-666907686",
                },
                {
                    "title": "Erkek Spor Ayakkabı Gy4738 GY4738",
                    "price": "1.299 TL",
                    "image": "https://cdn.dsmcdn.com/mnresize/1200/1800/ty587/product/media/images/20221102/17/205956509/612138696/1/1_org_zoom.jpg",
                    "brand": "adidas",
                    "link": "https://www.trendyol.com/adidas/erkek-spor-ayakkabi-gy4738-p-378785587",
                },
                {
                    "title": "Postmove Beyaz Erkek Sneaker POSTMOVE",
                    "price": "1.749 TL",
                    "image": "https://cdn.dsmcdn.com/mnresize/1200/1800/ty815/product/media/images/20230406/16/319413675/904462641/1/1_org_zoom.jpg",
                    "brand": "adidas",
                    "link": "https://www.trendyol.com/adidas/postmove-beyaz-erkek-sneaker-p-683357712",
                },
                {
                    "title": "Bravada Erkek Beyaz Sneaker Spor Ayakkabı FV8086-100",
                    "price": "1.999 TL",
                    "image": "https://cdn.dsmcdn.com/mnresize/1200/1800/ty806/product/media/images/20230329/12/314696636/899213591/1/1_org_zoom.jpg",
                    "brand": "adidas",
                    "link": "https://www.trendyol.com/adidas/bravada-erkek-beyaz-sneaker-spor-ayakkabi-p-679710431",
                },
                {
                    "title": "Superstar Unisex Beyaz Spor Ayakkabı EG4958-S",
                    "price": "2.749 TL",
                    "image": "https://cdn.dsmcdn.com/mnresize/1200/1800/ty8/product/media/images/20200718/13/5252140/63826381/1/1_org_zoom.jpg",
                    "brand": "adidas",
                    "link": "https://www.trendyol.com/adidas/superstar-unisex-beyaz-spor-ayakkabi-p-35714683",
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
                            product["image"],
                            product["brand"],
                            product["title"],
                            product["price"],
                        ),
                        unsafe_allow_html=True,
                    )

                st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()

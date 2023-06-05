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
    st.title("Dora")
    st.write("Gelen fotoğraftakine en çok benzeyen 10 ürünü listeleyen bir uygulama.")

    uploaded_file = st.file_uploader("Fotoğraf yükle", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Yüklenen Fotoğraf", use_column_width=True)
        if st.button("Benzer Ürünleri Bul"):
            result = [
                {
                    "title": "Ürün 1",
                    "price": "100 TL",
                    "image": "urun1.jpg",
                    "link": "https://urun1-link.com",
                },
                {
                    "title": "Ürün 2",
                    "price": "150 TL",
                    "image": "urun2.jpg",
                    "link": "https://urun2-link.com",
                },
                {
                    "title": "Ürün 3",
                    "price": "75 TL",
                    "image": "urun3.jpg",
                    "link": "https://urun3-link.com",
                },
                {
                    "title": "Ürün 4",
                    "price": "200 TL",
                    "image": "urun4.jpg",
                    "link": "https://urun4-link.com",
                },
                {
                    "title": "Ürün 5",
                    "price": "120 TL",
                    "image": "urun5.jpg",
                    "link": "https://urun5-link.com",
                },
                {
                    "title": "Ürün 6",
                    "price": "90 TL",
                    "image": "urun6.jpg",
                    "link": "https://urun6-link.com",
                },
                {
                    "title": "Ürün 7",
                    "price": "80 TL",
                    "image": "urun7.jpg",
                    "link": "https://urun7-link.com",
                },
                {
                    "title": "Ürün 8",
                    "price": "160 TL",
                    "image": "urun8.jpg",
                    "link": "https://urun8-link.com",
                },
                {
                    "title": "Ürün 9",
                    "price": "110 TL",
                    "image": "urun9.jpg",
                    "link": "https://urun9-link.com",
                },
                {
                    "title": "Ürün 10",
                    "price": "135 TL",
                    "image": "urun10.jpg",
                    "link": "https://urun10-link.com",
                },
            ]

            st.write("Benzer Ürünler:")
            cols = st.columns(5)

            for i, product in enumerate(result):
                with cols[i % 5]:
                    st.markdown(
                        '<hr style="border: 1px solid #d3d3d3;">',
                        unsafe_allow_html=True,
                    )
                    resized_img = expand2square(
                        "./photos/{}".format(product["image"]), "white"
                    )
                    st.image(
                        resized_img, caption=product["title"], use_column_width=True
                    )
                    st.markdown(
                        f"<h3 style='font-weight: bold; margin: 10px 0 0 0;'>{product['title']}</h3>"
                        f"<p style='font-weight: bold; margin: 0;'>Fiyat: {product['price']}</p>",
                        unsafe_allow_html=True,
                    )

                    st.markdown(
                        f'<a href="{product["link"]}" target="_blank" style="display: inline-block; margin-top: 10px;'
                        f"padding: 10px 15px; background-color: #006eff; color: white; text-decoration: none;"
                        f'border-radius: 5px;">'
                        f"Ürüne Git"
                        f"</a>",
                        unsafe_allow_html=True,
                    )


if __name__ == "__main__":
    main()

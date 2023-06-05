import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("<br><br><br><h1 style='text-align: center;'> Welcome to Plantveda! </h1>", unsafe_allow_html=True)
st.sidebar.success("Select an option above.")
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/free-vector/leaves-background-with-metallic-foil_79603-956.jpg?w=1060&t=st=1685090310~exp=1685090910~hmac=fc4e94ffd94b72637dfff54ea8f4510011d1b345539fe01ecd7a5585f36e4393");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
add_bg_from_url()

st.markdown(
    """
   Whether you're an avid gardener, a nature enthusiast, or just curious about the plants around you, our app is here to help you identify and learn about the incredible flora that surrounds us.

🔍 Snap a photo of any plant, flower, or leaf, and let our powerful image recognition technology work its magic. In seconds, you'll receive accurate and detailed information about the plant's name, species, and key characteristics.
"""
)
# for animation use Lottie files
# importing libraries:-
# Pillow library for inserting images
# to insert a fully function contact form use the free service of form submit
# for icons go to the bootstrap icon website

import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import requests


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def home_page():
    st.markdown(
        "<h1 style='color: #FF5733; font-size: 36px; margin-bottom: 20px;'>Mathentics</h1>",
        unsafe_allow_html=True
    )

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

            local_css("style/style.css")

    lottie_coding = load_lottieurl(
        "https://lottie.host/8e891be2-7fff-461f-83e2-5138d8edfbcc/6ZiNes5DlB.json"
    )
    img_lottie_animation = Image.open(
        "images/file1.png"
    )
    img_contact_form = Image.open(
        "images/file2.png"
    )

    with st.container():
        left_column, right_cloumn = st.columns(2)
    with left_column:
        st.write("##")  # we use this to add space in our website
        st.write("##")  # we use this to add space in our website
        st.write(
            """
        Welcome to Mathentics – your JEE prep companion. Unlock your potential with our video solutions for complex topics, tailored to help you understand and excel.
        Get ready with confidence using our realistic mock tests, guiding you towards your exam goals. Mathentics is here to empower your journey towards JEE success.
        """
        )
        st.write("[Youtube  Channel Link >](https://youtube.com/@MathenticsAcademy?si=hPqttrkb_utrN4NW)")

    with right_cloumn:
        st_lottie(lottie_coding, height=300, key="education")

    with st.container():
        st.write("---")
        st.header("My Projects")
        st.write("##")
        image_column, text_column = st.columns(
            (1, 2)
        )  # this shows the second column should be twice as big as the image
    with image_column:
        st.image(img_lottie_animation)

    with text_column:
        st.subheader("Some of my work is projected here")
        st.write(
            """
            It looks like you're requesting information related to mathematics. Could you please provide more specific details about what you're looking for? Are you looking for explanations of specific math concepts, equations, formulas, or something else related to mathematics? The more details you provide, the better I can assist you with your math-related inquiry.
            """
        )
        st.markdown(
            "[Watch Video...](https://youtube.com/@amrendrachaudhary4795?si=cXl-gMp293NkgTDt)"
        )

    with st.container():
        st.write("##")
        image_column, text_column = st.columns(
            (1, 2)
        )  # this shows the second column should be twice as big as the image
    with image_column:
        st.image(img_contact_form)

    with text_column:
        st.subheader("Some of my work is projected here")
        st.write(
            """
            To resolve this issue, you need to ensure that the paths in your code are correctly formatted to avoid Unicode escape errors. Here are a few steps you can take
            """
        )
        st.markdown(
            "[Watch Video...](https://youtube.com/@amrendrachaudhary4795?si=cXl-gMp293NkgTDt)"
        )


def Mock_test():
    st.title("Mock Test")
    st.write("Learn amazing concepts in mock test ")

    with st.expander("Limits"):
        with st.container():
            st.write("##")
            video_column, text_column = st.columns(
                (1, 2)
            )  # this shows the second column should be twice as big as the image
        with video_column:
            st.video("https://youtu.be/yagfIFcHZg4?si=YEOLQID7t2HMaZJf","video/mp4",)

        with text_column:
            st.subheader("Some of my work is projected here")
            st.write(
                """
                To resolve this issue, you need to ensure that the paths in your code are correctly formatted to avoid Unicode escape errors. Here are a few steps you can take
                """
            )

    



def Topic_wise():
    st.title("Topic Wise")
    st.write("Learn through Questions regarding every topic")

    with st.expander("Limits"):
        with st.container():
            st.write("##")
            video_column, text_column = st.columns(
                (1, 2)
            )  # this shows the second column should be twice as big as the image
        with video_column:
            st.video("https://youtu.be/yagfIFcHZg4?si=YEOLQID7t2HMaZJf","video/mp4",)

        with text_column:
            st.subheader("Some of my work is projected here")
            st.write(
                """
                To resolve this issue, you need to ensure that the paths in your code are correctly formatted to avoid Unicode escape errors. Here are a few steps you can take
                """
            )

def contact_page():
    # st.title("Contact Page")
    # st.write("Reach out to us through the Contact Page.")
    # Add a container for the contact form
    with st.container():
        st.header("Get in touch with us!")

        # Add a div with background color
        st.markdown(
            """
            <div style='background-color: #f2f2f2; padding: 20px; border-radius: 10px;'>
                <form action="https://formsubmit.co/mathentics11@gmail.com" method="POST">
                    <input type="hidden" name="_captcha" value="false">
                    <label for="name">Your Name:</label>
                    <input type="text" id="name" name="name" placeholder="Your name" required><br><br>
                    <label for="email">Your Email:</label>
                    <input type="email" id="email" name="email" placeholder="Your email" required><br><br>
                    <label for="message">Your Message:</label>
                    <textarea id="message" name="message" placeholder="Your message here" required></textarea><br><br>
                    <button type="submit" style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px;">Send</button>
                </form>
            </div>
            """,
            unsafe_allow_html=True,
        )


# Set page title and icon
st.set_page_config(
    page_title="My Webpage",
    page_icon=":tada:",
    layout="wide",
)

# Create navigation bar with icons and styles
navigation_icons = {
    "Home": "🏠",
    "Mock Test": "ℹ️",
    "Topic Wise": "📚",
    "Contact": "📞",
}

with st.sidebar:
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            background-color: #333333;
        }
        .sidebar li {
            margin-top: 10px;
            margin-bottom: 10px;
        }
        .sidebar a {
            color: white;
            text-decoration: none;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    selected_page = st.sidebar.radio("Navigation", list(navigation_icons.keys()))

# Display selected page
if selected_page == "Home":
    home_page()
elif selected_page == "Mock Test":
    Mock_test()
elif selected_page == "Topic Wise":
    Topic_wise()
elif selected_page == "Contact":
    contact_page()


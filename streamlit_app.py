import streamlit as st

# -- PAGE SETUP --
about_page = st.Page(
    page="views/aboutme.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)

project_1_page = st.Page(
    page="views/deployments.py",  # Removed leading space
    title="Deployments",
    icon=":material/bar_chart:",
)

project_2_page = st.Page(
    page="views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:"
)

# -- Navigation Setup --
pg = st.navigation(
    {
        "Info":[about_page],
        "Projects":[project_1_page, project_2_page]
    }
)

# -- shared on all pages --
st.logo("assets/125236832_338903670_pythontee.png")
st.sidebar.text("Angel Dev Studio")

# -- Run Navigation --
pg.run()

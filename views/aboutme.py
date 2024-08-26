import streamlit as st
from forms.contact import contact_form

# Columns for profile image and name
col1, col2 = st.columns(2)
with col1:
    st.image("./assets/profile_image.png", width=230)
with col2:
    st.title("K. P. Lines")
    st.write(
        "Senior Automation Developer, providing automation as a service worldwide."
    )

    # Display contact form only if the button is clicked
    if st.button("Contact Me"):
        contact_form()

# Experience and Qualifications
st.write("\n")
st.subheader("Experience")
st.write(
    """
    - 12 Years working with various Automation routines.
    - 5 Years working with automation as a service in a variety of organisations.
    - Capable of planning, development and deployment of automations within a live environment.
    - Strong Knowledge of compliance rules in relation to insolvency.
    """
)

st.write("\n")
st.subheader("Software & Qualifications")
st.write(
    """
    Software proficiency:
    - Fortra Automate.
    - Microsoft Power Automate.
    - Automation Anywhere.
    - Sema4/Robocorp.
    - Python.
    - MySql/Postgre.
    - Powershell.
    - Pabbly Connect.

    Relevant Qualifications:
    - Robocorp Level 1 & 2.
    - Basic and advanced Python 101.
    - Microsoft c# Level 1.
    - Django 101.
    """
)

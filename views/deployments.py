import streamlit as st

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/125236832_338903670_pythontee.png", width=230)
with col2:
    st.title("Current Deployments", anchor = False)
    st.write("not all companies have consented to be disclosed due to 3rd party involvements.\n\n")

# insolvency practicioner robotics.
st.title("Insolvency Practicioner Onboarding.", anchor = False)
st.write("Status: Live")
st.write("""
         Clients: Multiple.
         Current onboarding actions:
         - loading from online portal feeding SQL tables.
         - Creation of Word documents including engagement letters and meeting packs
         - Gathering of information from public sector documents and companies house.
         - Logging of shell records with Docusoft, IPS and Vision Blue software
         - Delivery of electronic Engagement letter to clients.
         - Final uploading and filing of documents with client software and local directories.
         - Performing of complex AML checks, including enhanced AML.
         - Maintaining client compliance.
         """)

# Ecommerce Deployments
st.write("\n")
st.title("E-Commerce Deployments")
st.write("Status: Live")
st.write("""
         Clients: Multiple.
         Current Actions:
         - Multiple robots operating behind the scenes on largest E-commerce platform
         - Gathering of order information from recent orders before pushing directly to client CMS systems directly.
         - Automatic processing of customer messages with custom message banks that run out of hours to maintain SLA for host site.
         - Automated downloading of sales reports, processing and passing through an Evri booking API to automate dispatch of orders.
         - Downloading of purchase orders from Exchange mailbox and comparing drop shipping charges against Purchase orders.
         """)

# Accountancy Deployments
st.write("\n")
st.title("Accountancy Deployments")
st.write("Status: Live")
st.write("""
         Clients: Multiple.
         Current Actions:
         - Compare PDF statements with Sage excel reports to flag any issues with over or under payments.
         - Automate payroll via Care Sector Software (Active People Planner).
         - Automate report generation for Care sector to improve local authority invoising.
         - Automated approval of receipts via the Xero/Hubdoc system.
         - Download and process of Staff holiday and absence reports.
         """)

# Lead Generation
st.write("\n")
st.title("Lead Generation Deployments")
st.write("Status: Live")
st.write("""
         Clients: NDA restricted.
         Current Actions:
         - Monitoring and extraction of new building and planning permissions to send unique introduction email for clients.
         - Monitoring and extraction of data from legal professions to send introduction email for clients.
         """)

# Conveyancing Deployments
st.write("\n")
st.title("Conveyancing Deployments")
st.write("Status: Live")
st.write("""
         Clients: Multiple.
         Current Actions:
         - Retrieve information from Wordpress live forms.
         - Extract the data and feed into LEAP, to generate a case, documentations and finally print.
         """)

# Travel Agencies Deployments
st.write("\n")
st.title("Travel Sector Deployments")
st.write("Status: Live")
st.write("""
         Clients: Multiple.
         Current Actions:
         - Extraction of booking information from email and retrieval of holiday package from SQL tables.
         - Loading of package holidays via Dolphin holiday system.
         """)

# Media Deployments
st.write("\n")
st.title("Media and News outlet Deployments")
st.write("Status: Live")
st.write("""
         Clients: Multiple.
         Current Actions:
         - Retrieve daily publications from PostGres DB
         - Pass each image through Google Vision API to find where it has been used on the web.
         - Create a daily report of usage to billing teams.
         - Store all results in Sharepoint systems remotely.
         """)
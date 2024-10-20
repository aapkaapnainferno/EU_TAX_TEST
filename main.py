import streamlit as st
from dateutil.relativedelta import relativedelta
import openpyxl
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
from io import StringIO
# Page configuration
st.set_page_config(
    page_title="EU Taxonomy",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Define a common background color
bg_color = "#000C66"  # Adjust this color as needed
check_phase1 = False
check_phase2 = False
# CSS style for larger font size
if 'field1' not in st.session_state:
    st.session_state.field1 = ""
if 'field2' not in st.session_state:
    st.session_state.field2 = ""
if 'field3' not in st.session_state:
    st.session_state.field3 = ""
if 'field4' not in st.session_state:
    st.session_state.field4 = ""
if 'field5' not in st.session_state:
    st.session_state.field5 = ""
if 'field9' not in st.session_state:
    st.session_state.field9 = ""
if 'field11' not in st.session_state:
    st.session_state.field11 = ""
if 'field16' not in st.session_state:
    st.session_state.field16 = 0.0
if 'field19' not in st.session_state:
    st.session_state.field19 = 0.0
if 'field27' not in st.session_state:
    st.session_state.field27 = 0.0
if 'field32' not in st.session_state:
    st.session_state.field32 = 0.0
if 'field34' not in st.session_state:
    st.session_state.field34 = 0.0
if 'field37' not in st.session_state:
    st.session_state.field37 = 0.0
if 'field39' not in st.session_state:
    st.session_state.field39 = 0.0
if 'field44' not in st.session_state:
    st.session_state.field44 = 0.0
if 'field47' not in st.session_state:
    st.session_state.field47 = 0.0
if 'field60' not in st.session_state:
    st.session_state.field60 = 0.0
st.markdown(
    """
    <style>
    .big-font-section {
        font-size: 18px !important;
        text-align: center;
    }
    .big-font {
        font-size: 18px !important;
    }
    .center-text {
        text-align: center;
        margin: 0 auto;
        width: 70%; /* Adjust the width as needed */
    }
    .info-button {
        margin-left: 10px;
        background-color: #007BFF;
        border: none;
        color: white;
        padding: 5px 10px;
        border-radius: 50%;
        cursor: pointer;
        display: inline-block;
        width: 30px; /* Adjust the width and height to ensure the button is circular */
        height: 30px; /* Adjust the width and height to ensure the button is circular */
        text-align: center;
        line-height: 20px; /* Align the text vertically in the center */
        float: right;
    }
    .tooltip {
        position: relative;
        display: inline-block;
        cursor: pointer;
        margin-left: 10px;
    }
    .tooltip .tooltiptext {
        visibility: hidden;
        width: 220px;
        background-color: #555;
        color: #fff;
        text-align: center;
        border-radius: 5px;
        padding: 5px 10px;
        position: absolute;
        z-index: 1;
        bottom: 150%; /* Adjust this value to move the tooltip */
        left: 50%;
        margin-left: -110px;
        opacity: 0;
        transition: opacity 0.3s;
        font-size: 15px !important;
    }
    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }
    .bold-hr {
        border: 0;
        height: 5px; /* Adjust height to make it more bold */
        background: #000; /* Change color if needed */
    }
    </style>
    """,
    unsafe_allow_html=True,
)
if 'show_eligibility' not in st.session_state:
        st.session_state.show_eligibility = False

if 'page' not in st.session_state:
    st.session_state.page = 'main'

def continue_to_phase():
    st.session_state.page = 'phase'

def continue_to_phase2():
    st.session_state.page = 'phase2'

def continue_to_dashboard():
    st.session_state.page = 'dashboard'
    
# def go_back_to_main_page():
#     st.session_state.page = 'main'
    # st.session_state.show_eligibility = False
# Sidebar for input fields and logos
if st.session_state.page == 'main':
    with st.sidebar:
        # Logos at the top of the sidebar
        col1, col2 = st.columns((1, 1))
        with col1:
            st.image("egypt.jpg", width=100)
        with col2:
            st.image("eu.jpg", width=100)
        
        st.markdown("# User Details")
        # field1 = ""
        # field2 = ""
        # field3 = ""
        # field4 = ""
        # field5 = ""
        st.session_state.field1 = st.text_input("Username", key='1', placeholder="Enter username")
        st.session_state.field2 = st.text_input("Project", key='2', placeholder="Enter project name")
        st.session_state.field3 = st.text_input("Capacity", key='3', placeholder="Enter capacity in m3/d")
        st.session_state.field4 = st.text_input("Location", key='4', placeholder="Enter location")
        st.session_state.field5 = st.date_input("Date", key='5')

        if st.button('Next') and st.session_state.field1 != "" and st.session_state.field2 != "" and st.session_state.field3 != "" and st.session_state.field4 != "" and st.session_state.field5 != "":
            st.session_state['show_eligibility'] = True

    # Main content
    with st.container():
        col1, col2 = st.columns((1, 5))
        with col1:
            st.image("CL3.png",width=180)
        with col2:
            st.markdown(
                f'<br><br><div style="background-color: {bg_color}; color: white; padding: 5px; border-radius: 15px; margin-bottom: 15px; width: 100%; text-align: center; font-size: 36px; margin-top: -50px;" class="center-text">'
                '<strong>EU-WATER-FIT (Water Assessment and EU Taxonomy Evaluation for Resilient Financing and Investment Tool)</strong>'
                '</div>', unsafe_allow_html=True)

    # Adding some space below the logos
    st.markdown("<br>", unsafe_allow_html=True)

    # Eligibility section (displayed only if Next button is clicked and all fields are filled)
    if st.session_state.get('show_eligibility', False):
        col1, col2 = st.columns((1, 5))
        options1 = ['Click here to select option', 'E36.00', 'F42.9']

        # Eligibility
        with col1:
            st.markdown(
                f'<div style="background-color: #3f3f3f; color: white; padding: 15px; border-radius: 100px; margin-bottom: 15px; width: 100%;" class="big-font-section">'
                '<strong>ELIGIBILITY</strong>'
                '<button class="info-button tooltip" id="info-btn">i'
                '<span class="tooltiptext">Confirm if the Economic Activity matches a suitable Macro Economic Sector as stipulated in the Delegated Acts or Technical Screening Criteria based on Nomenclature of Economic Activities(NACE) code</span>'
                '</div>', unsafe_allow_html=True)
        with col2:
            st.markdown(
                f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                '<strong>Provide the NACE (Nomenclature of Economic Activities) Code for Desalination</strong>'
                '<button class="info-button tooltip" id="info-btn">i'
                '<span class="tooltiptext">Desalination is not assigned a NACE code; however, desalination can be substituted by two other activity codes</span>'
                '</button>'
                '</div>', unsafe_allow_html=True)
            answer1 = st.selectbox('Select your response', options1, label_visibility='collapsed', key='answer1')

            answer2 = ""
            answer3 = ""
            answer4 = 0
            answer5 = 0
            answer6 = 0
            answer7 = 0
            answer8 = 0
            answer9 = []
            answer10 = ""
            answer11 = ""
            answer12 = ""
            if answer1 == 'E36.00':
                st.markdown(
                    f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                    '<strong>Is the desalination activity associated with construction, extension and operation of water collection, treatment and supply systems?</strong>'
                    '<button class="info-button tooltip" id="info-btn">i'
                    '<span class="tooltiptext">Desalination is not assigned a NACE code; however, desalination can be substituted by two other activity codes</span>'
                    '</button>'
                    '</div>', unsafe_allow_html=True)
                answer2 = st.radio('Yes or No?', options=['Yes', 'No'], label_visibility='collapsed')
            elif answer1 == 'Click here to select option':
                st.write("")
            else:
                st.markdown(
                    f'<div style="background-color: #FF6347; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%; text-align: center;" class="big-font">'
                    '<strong>NACE Code F42.9 is not eligible to continue.</strong>'
                    '</div>', unsafe_allow_html=True)

            if answer1 == "E36.00":
                st.markdown(
                    f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                    '<strong>Is the desalination activity associated with renewal of water collection, treatment and supply systems?</strong>'
                    '<button class="info-button tooltip" id="info-btn">i'
                    '<span class="tooltiptext">Desalination is not assigned a NACE code; however, desalination can be substituted by two other activity codes</span>'
                    '</button>'
                    '</div>', unsafe_allow_html=True)
                answer3 = st.radio('Yes or No?2', options=['Yes', 'No'], label_visibility='collapsed')
            if answer2 == "No" and answer3 == "No":
                st.markdown(
                    f'<div style="background-color: #FF6347; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;text-align: center;" class="big-font">'
                    '<strong>The envisioned Activity is Not EU Taxonomy Eligible</strong>'
                    '</div>', unsafe_allow_html=True)
        col3, col4 = st.columns((1, 5))
        with col4:
            if (answer2 == "Yes" or answer3 == "Yes") and answer1 == "E36.00":
                st.markdown(
                    f'<div style="background-color: #00FF00; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%; text-align: center;" class="big-font">'
                    '<strong>The envisioned Activity is EU Taxonomy Eligible</strong>'
                    '</div>', unsafe_allow_html=True)
        if answer2 == "Yes" or answer3 == "Yes":
            st.markdown("<hr class='bold-hr'>", unsafe_allow_html=True)
        col1, col2 = st.columns((1, 5))
        if answer2 == "Yes" or answer3 == "Yes":
            with col1:
                st.markdown(
                    f'<br><div style="background-color: #3f3f3f; color: white; padding: 15px; border-radius: 100px; margin-bottom: 15px; width: 100%;" class="big-font-section">'
                    '<strong>ALIGNMENT</strong>'
                    '<button class="info-button tooltip" id="info-btn">i'
                    '<span class="tooltiptext">Confirm if the Economic Activity provides a "Substantial Contribution" to one environmental objective and will "Do No Significant Harm" (DNSH)  to the remaining five environmental objectives, as designated per sector</span>'
                    '</div>', unsafe_allow_html=True)
            if answer2 == "Yes":
                # Alignment
                with col2:
                    st.markdown(
                        f'<br><div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                        '<strong>What is the net average energy consumption for abstraction and treatment for produced water supply (in kWh/m3)?</strong>'
                        '<button class="info-button tooltip" id="info-btn">i'
                        '<span class="tooltiptext">Should be less than or equal to 0.5</span>'
                        '</div>', unsafe_allow_html=True)
                    answer4 = st.number_input('Enter your response (kWh/m3)', min_value=0.0, step=0.01,label_visibility='collapsed')

                    answer5 = ""
                    st.markdown(
                        f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                        '<strong>What is the Leakage Level associated with this activity?</strong>'
                        '<button class="info-button tooltip" id="info-btn">i'
                        '<span class="tooltiptext">ILI= Current Annual Real Losses (CARL) / Unavoidable Annual Real Losses (UARL)<br>Should be less than or equal to 1.5</span>'
                        '</button>'
                        '</div>', unsafe_allow_html=True)
                    answer5 = st.number_input('Enter your response (kWh/m3)1', min_value=0.0, step=0.01,label_visibility='collapsed')

                    if answer5 > 1.5 or answer4 > 0.5:
                        st.markdown(
                            f'<div style="background-color: #FF6347; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%; text-align: center;" class="big-font">'
                            '<strong>The envisioned Activity is Not EU Taxonomy Eligible</strong>'
                            '</div>', unsafe_allow_html=True)
            if answer3 == "Yes" and answer5 <= 1.5 and answer4 <= 0.5:
                with col2:
                    st.markdown(
                        f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                        '<strong>What is the net average energy consumption compared to own baseline performance average for three years (in kWh/m3)</strong>'
                        '<button class="info-button tooltip" id="info-btn">i'
                        '<span class="tooltiptext">Should be greater than or equal to 20</span>'
                        '</button>'
                        '</div>', unsafe_allow_html=True)
                    answer6 = st.number_input('Enter your response (kWh/m3)', min_value=0.0, max_value=100.0, step=0.01,label_visibility='collapsed')

                    answer7 = ""
                    st.markdown(
                        f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                        '<strong>What is the Leakage Level between the current leakage level averaged over three years, calculated using the ILI of 1.5?</strong>'
                        '<button class="info-button tooltip" id="info-btn">i'
                        '<span class="tooltiptext">Should be greater than or equal to 20</span>'
                        '</button>'
                        '</div>', unsafe_allow_html=True)
                    answer7 = st.number_input('Enter your response (kWh/m3)1', min_value=0.0, max_value=100.0, step=0.01,label_visibility='collapsed')
            #2B
            if (answer2 == "Yes" and (answer5 <= 1.5 and answer4 <= 0.5) and (answer5 != 0.0 and answer4 != 0.0)) or (answer3 == "Yes"  and (answer6 >= 20 and answer7 >= 20)):
                with col2:
                    st.markdown(
                        f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                        '<strong>What is the Greenhouse Gas emissions of your activity (in CO2e/m3)?</strong>'
                        '<button class="info-button tooltip" id="info-btn">i'
                        '<span class="tooltiptext">Should be less than 1080</span>'
                        '</button>'
                        '</div>', unsafe_allow_html=True)
                    answer8 = st.number_input('Enter your response (gCO2e/m3)', min_value=0.0, step=0.01,label_visibility='collapsed')

                    st.markdown(
                        f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                        '<strong>Does your activity significantly harm one of the remaining following Environmental Objectives:</strong>'
                        '</div>', unsafe_allow_html=True)
                    options = {
                            "Option 1": "Sustainable use and protection of water and marine resources",
                            "Option 2": "Transition to a circular economy",
                            "Option 3": "Pollution prevention and control",
                            "Option 4": "Protection and restoration of biodiversity and ecosystems",
                            "Option 5": "None of the above"
                        }
                    for key in options:
                        if key not in st.session_state:
                            st.session_state[key] = False

                    # Handle the logic for deselecting checkboxes before rendering the UI
                    if st.session_state["Option 5"]:
                        for k in options:
                            if k != "Option 5":
                                st.session_state[k] = False
                    else:
                        for k in options:
                            if k != "Option 5" and st.session_state[k]:
                                st.session_state["Option 5"] = False
                                break

                    # Create checkboxes
                    answer9 = {}
                    for key, label in options.items():
                        answer9[key] = st.checkbox(label, key=key)
                    answer9 = [label for key, label in options.items() if answer9[key]]
                if len(answer9) == 1 and ("None of the above" in answer9) and answer8 < 1080:
                    col3, col4 = st.columns((1, 5))
                    with col4:
                        st.markdown(
                        f'<div style="background-color: #00FF00; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%; text-align: center;" class="big-font">'
                        '<strong>The envisioned Activity is EU Taxonomy Eligible</strong>'
                        '</div>', unsafe_allow_html=True)
                    st.markdown("<hr class='bold-hr'>", unsafe_allow_html=True)
                    col1, col2 = st.columns((1, 5))
                    with col1:
                        st.markdown(
                        f'<div style="background-color: #3f3f3f; color: white; padding: 15px; border-radius: 100px; margin-bottom: 15px; width: 100%;" class="big-font-section">'
                        '<strong>MINIMUM SAFEGUARDS</strong>'
                        '</div>', unsafe_allow_html=True)
                    #3A
                    with col2:
                        st.markdown(
                            f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                            '<strong>Did you implement an adequate Human Resources Due Diligence (HRDD)?</strong>'
                            '<button class="info-button tooltip" id="info-btn">i'
                            '<span class="tooltiptext">Promotion and protection of fundamental human rights as outlined in international conventions and agreements.</span>'
                            '</button>'
                            '</div>', unsafe_allow_html=True)
                        answer10 = st.radio('Yes or No?3', options=['Yes', 'No'], label_visibility='collapsed')
                        if answer10 == "No":
                            st.markdown(
                                f'<div style="background-color: #FF6347; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%; text-align: center;" class="big-font">'
                                '<strong>Not Compliant</strong>'
                                '</div>', unsafe_allow_html=True)
                        else:
                            st.markdown(
                                f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                                '<strong>Is there any Signals of abuse to Human Resource?</strong>'
                                '<button class="info-button tooltip" id="info-btn">i'
                                '<span class="tooltiptext">Support for fair labor practices, including ensuring safe working conditions, non- discrimination, and the right to organize and bargain collectively.</span>'
                                '</button>'
                                '</div>', unsafe_allow_html=True)
                            options = {
                                    "Option 1": "Found in breach of labour law or human rights",
                                    "Option 2": "Do not engage with relevant stakeholders",
                                    "Option 3": "None"
                                }
                            answer11 = {key: st.checkbox(label1) for key, label1 in options.items()}
                            answer11 = [label1 for key, label1 in options.items() if answer11[key]]
                            if len(answer11) >= 1 and "None" not in answer11:
                                st.markdown(
                                    f'<div style="background-color: #FF6347; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%; text-align: center;" class="big-font">'
                                    '<strong>Not Compliant</strong>'
                                    '</div>', unsafe_allow_html=True)
                            elif len(answer11) == 1 and "None" in answer11:
                                #3B
                                st.markdown(
                                    f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                                    '<strong>Did any anti-corruption processes took place?</strong>'
                                    '<button class="info-button tooltip" id="info-btn">i'
                                    '<span class="tooltiptext">Implementation of measures to combat bribery and corruption in partner countries.</span>'
                                    '</button>'
                                    '</div>', unsafe_allow_html=True)
                                answer12 = st.radio('Yes or No?4', options=['Yes', 'No'], label_visibility='collapsed')
                                if answer12 == "Yes":
                                    st.markdown(
                                        f'<div style="background-color: #FF6347; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%; text-align: center;" class="big-font">'
                                        '<strong>Not Compliant</strong>'
                                        '</div>', unsafe_allow_html=True)
                                else:
                                    st.markdown(
                                        f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                                        '<strong>Did the company or its senior management, including the senior management of its subsidiaries, has been convicted in court on corruption?</strong>'
                                        '<button class="info-button tooltip" id="info-btn">i'
                                        '<span class="tooltiptext">Assistance in establishing and enforcing anti-corruption policies and practices, aligned with international standards.</span>'
                                        '</button>'
                                        '</div>', unsafe_allow_html=True)
                                    answer13 = st.radio('Yes or No?9', options=['Yes', 'No'], label_visibility='collapsed')
                                    if answer13 == "Yes":
                                        st.markdown(
                                            f'<div style="background-color: #FF6347; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%; text-align: center;" class="big-font">'
                                            '<strong>Not Compliant</strong>'
                                            '</div>', unsafe_allow_html=True)
                                    else:
                                        #3C
                                        st.markdown(
                                            f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                                            '<strong>The company confirms that it treats tax governance and compliance as important elements of oversight, and there are adequate tax risk management strategies and processes in place?</strong>'
                                            '<button class="info-button tooltip" id="info-btn">i'
                                            '<span class="tooltiptext">Collaboration on tax-related matters to promote fair and transparent tax systems.</span>'
                                            '</button>'
                                            '</div>', unsafe_allow_html=True)
                                        answer14 = st.radio('Yes or No?5', options=['Yes', 'No'], label_visibility='collapsed')
                                        if answer14 == "No":
                                            st.markdown(
                                                f'<div style="background-color: #FF6347; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%; text-align: center;" class="big-font">'
                                                '<strong>Not Compliant</strong>'
                                                '</div>', unsafe_allow_html=True)
                                        else:
                                            st.markdown(
                                                f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                                                '<strong>Has the company or its subsidiaries violated the tax laws?</strong>'
                                                '<button class="info-button tooltip" id="info-btn">i'
                                                '<span class="tooltiptext">Support for partner countries in adopting international best practices in tax administration, compliance, and combating tax evasion.</span>'
                                                '</button>'
                                                '</div>', unsafe_allow_html=True)
                                            answer15 = st.radio('Yes or No?6', options=['Yes', 'No'], label_visibility='collapsed')
                                            if answer15 == "Yes":
                                                st.markdown(
                                                    f'<div style="background-color: #FF6347; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%; text-align: center;" class="big-font">'
                                                    '<strong>Not Compliant</strong>'
                                                    '</div>', unsafe_allow_html=True)
                                            else:
                                                st.markdown(
                                                f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                                                '<strong>Does the company promote employee awareness on importance of compliance with all applicable competition laws and regulations?</strong>'
                                                '<button class="info-button tooltip" id="info-btn">i'
                                                '<span class="tooltiptext">Encouragement of open and competitive markets in partner countries to stimulate economic growth and development.</span>'
                                                '</button>'
                                                '</div>', unsafe_allow_html=True)
                                                answer16 = st.radio('Yes or No?7', options=['Yes', 'No'], label_visibility='collapsed')
                                                if answer16 == "No":
                                                    st.markdown(
                                                        f'<div style="background-color: #FF6347; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%; text-align: center;" class="big-font">'
                                                        '<strong>Not Compliant</strong>'
                                                        '</div>', unsafe_allow_html=True)
                                                else:
                                                    st.markdown(
                                                    f'<div style="background-color: {bg_color}; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%;" class="big-font">'
                                                    '<strong>Does the company or its senior management, including the senior management of its subsidiaries, has been convicted on violating competition laws?</strong>'
                                                    '<button class="info-button tooltip" id="info-btn">i'
                                                    '<span class="tooltiptext">Assistance in establishing and enforcing competition laws and regulations to prevent anti-competitive behavior and monopolies .</span>'
                                                    '</button>'
                                                    '</div>', unsafe_allow_html=True)
                                                    answer17 = st.radio('Yes or No?8', options=['Yes', 'No'], label_visibility='collapsed')
                                                    if answer17 == "Yes":
                                                        st.markdown(
                                                            f'<div style="background-color: #FF6347; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%; text-align: center;" class="big-font">'
                                                            '<strong>Not Compliant</strong>'
                                                            '</div>', unsafe_allow_html=True)
                                                    else:
                                                        st.markdown(
                                                            f'<div style="background-color: #00FF00; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%; text-align: center;" class="big-font">'
                                                            '<strong>The envisioned Activity is compliant with the Minimum Safeguards of the EU Taxonomy. And the User can proceed to Financial Assessment.</strong>'
                                                            '</div>', unsafe_allow_html=True)
                                                        if st.session_state.page == 'main':
                                                            st.button("Continue", on_click=continue_to_phase)
                elif len(answer9) >= 1:
                    with col2:
                        st.markdown(
                            f'<div style="background-color: #FF6347; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%; text-align: center;" class="big-font">'
                            '<strong>EU Taxonomy does not align</strong>'
                            '</div>', unsafe_allow_html=True)
            else:
                with col2:
                    st.markdown(
                        f'<div style="background-color: #FF6347; color: white; padding: 15px; border-radius: 10px; margin-bottom: 15px; width: 100%; text-align: center;" class="big-font">'
                        '<strong>EU Taxonomy does not align</strong>'
                        '</div>', unsafe_allow_html=True)
    else:
        st.info("Please fill in all input fields to proceed with eligibility questions.")
#Make changes for the next page here
elif st.session_state.page == 'phase':
    def custom_number_input(label, key, placeholder,value=0.0):
        return st.number_input(label, key=key, step=0.01,value=value,placeholder=placeholder)
    
    def custom_percentage_input(label, key, placeholder,value=0.0):
        return st.number_input(label, key=key, step=0.01,max_value=100.0,value=value,placeholder=placeholder)

    def custom_text_input(label, key, placeholder):
        return st.text_input(label, key=key, placeholder=placeholder)
    
    def custom_date_input(label, key):
        return st.date_input(label, key=key)
    
    def calculate_future_date_months(date, months):
        whole_months = int(months)
        fractional_months = months - whole_months
        future_date = date + relativedelta(months=whole_months)
        additional_days = int(fractional_months * 30)
        future_date += relativedelta(days=additional_days)
        return future_date
    
    def calculate_future_date_years(date, years):
        whole_years = int(years)
        fractional_years = years - whole_years
        future_date = date + relativedelta(years=whole_years)
        additional_days = int(fractional_years * 365)
        future_date += relativedelta(days=additional_days)
        return future_date

    st.markdown(
        f'<div style="background-color: {bg_color}; color: white; padding: 5px; border-radius: 15px; margin-bottom: 15px; width: 100%; text-align: center; font-size: 54px; margin-top: -50px;" class="center-text">'
        '<strong>FINANCIAL ASSESSMENT</strong>'
        '</div>', unsafe_allow_html=True)
    options = ["Select an option","1", "2"]
    st.session_state.field100 = st.selectbox("Is your project a one phase or two phase project?", options, key='100')
    if st.session_state.field100 == "1":
        check_phase1 = True
        check_phase2 = False
    if st.session_state.field100 == "2":
        check_phase1 = True
        check_phase2 = True
    if check_phase1:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown(
            f'<div style="background-color: {bg_color}; color: white; padding: 5px; border-radius: 15px; margin-bottom: 15px; width: 80%; text-align: center; font-size: 36px; margin-top: -50px;" class="center-text">'
            '<strong>Phase 1</strong>'
            '</div>', unsafe_allow_html=True)
        st.session_state.field6 = custom_number_input("Exchange Rate - Phase 1", '6', "Enter")
        st.session_state.fcp1 = custom_date_input("Financial Close - Phase 1", 'fcp1key')
        st.session_state.field7 = custom_date_input("Construction Start Date - Phase 1", '7')
        st.session_state.field8 = custom_number_input("Construction Period(in months) - Phase 1", '8', "Enter")
        if st.session_state.field8 != 0:
            st.session_state.field9 = st.write("Construction End Date: - Phase 1", calculate_future_date_months(st.session_state.field7,st.session_state.field8)) # TBC
            st.session_state.field9 = calculate_future_date_months(st.session_state.field7,st.session_state.field8)
        st.session_state.osdp1 = custom_date_input("Operations Start Date - Phase 1", 'osdp1key')
        st.session_state.field10 = custom_number_input("Operations Period(in Years) - Phase 1", '10', "Enter")
        if st.session_state.field10 != 0:
            st.session_state.oedp1 = st.write("Operations End Date: - Phase 1", calculate_future_date_years(st.session_state.osdp1,st.session_state.field10)) # TBC
            st.session_state.oedp1 = calculate_future_date_years(st.session_state.field9,st.session_state.field10)
        st.session_state.drsdp1 = custom_date_input("Debt Repayment Start Date - Phase 1", 'drsdp1key')
        st.session_state.drtp1 = custom_number_input("Debt Repayment Tenor(in Years) - Phase 1", 'drtp1key', "Enter")
        if st.session_state.drtp1 != 0:
            st.session_state.dredp1 = st.write("Debt Repayment End Date: - Phase 1", calculate_future_date_years(st.session_state.drsdp1,st.session_state.drtp1)) # TBC
            st.session_state.dredp1 = calculate_future_date_years(st.session_state.drsdp1,st.session_state.drtp1)
        st.session_state.cepsp1 = custom_number_input("Capital Expenditure - Pre sensitivity(in LE'000s) - Phase 1", 'cepsp1key', "Enter")
        st.session_state.field12 = custom_percentage_input("Debt Ratio (%) - Phase 1", '12', "Enter") 
        st.session_state.field13 = custom_percentage_input("Equity Ratio (%) - Phase 1", '13', "Enter")
        st.session_state.field14 = custom_percentage_input("Construction Interest Rate (Base Rate %) - Phase 1", '14', "Enter") 
        st.session_state.field15 = custom_percentage_input("Construction Interest Rate (Margin Spread %) - Phase 1",'15', "Enter")
        if st.session_state.field14 != 0 and st.session_state.field15 != 0:
            st.write("All in Rate (%)", st.session_state.field14 + st.session_state.field15) # TBC
            st.session_state.field16 = st.session_state.field14 + st.session_state.field15
        st.session_state.field17 = custom_percentage_input("Operations Interest Rate (Base Rate %) - Phase 1",'17', "Enter")
        st.session_state.field18 = custom_percentage_input("Operations Interest Rate (Margin Spread %) - Phase 1",'18', "Enter")
        if st.session_state.field17 != 0 and st.session_state.field18 != 0:
            st.write("All in Rate (%) - Phase 1", st.session_state.field17 + st.session_state.field18) # TBC
            st.session_state.field19 = st.session_state.field17 + st.session_state.field18
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown(
            f'<div style="background-color: {bg_color}; color: white; padding: 5px; border-radius: 15px; margin-bottom: 15px; width: 80%; text-align: center; font-size: 36px; margin-top: -50px;" class="center-text">'
            '<strong>Phase 1</strong>'
            '</div>', unsafe_allow_html=True)
        col1, col2 = st.columns((1, 1))
        with col1:
            st.session_state.field20 = custom_number_input("Construction Cost - Phase 1", '20',"Enter")
            st.session_state.field21 = custom_number_input("Gross Availability - Phase 1", '21',"Enter")
            st.session_state.field22 = custom_percentage_input("Availibility Factor (%) - Phase 1", '22',"Enter",95.0)
            st.session_state.field23 = custom_percentage_input("Input to Output Ratio (%) - Phase 1", '23',"Enter",100.0)
            st.session_state.field24 = custom_percentage_input("Leakage Ratio/Losses (%) - Phase 1", '24',"Enter",95.0)
            st.session_state.field25 = custom_number_input("Labor Cost (EGP'000) - Phase 1", '25',"Enter")
            st.session_state.field26 = custom_number_input("Maintenance Costs (EGP'000) - Phase 1", '26',"Enter")
            st.session_state.cgp1 = custom_number_input("Chlorine Gas (in LE'000s) - Phase 1",'cgp1key', "Enter",0.0)
            st.session_state.cfltp1 = custom_number_input("Chemical for laboratory test (in LE'000s) - Phase 1",'cfltp1key', "Enter",0.0)
        with col2:
            st.session_state.field27 = custom_number_input("Environment & Performance Monitoring Costs (EGP'000) - Phase 1", '27',"Enter")
            st.session_state.field28 = custom_number_input("Maintenance Cost (EGP'000) - Phase 1", '28',"Enter")
            st.session_state.field29 = custom_number_input("Variable Cost (EGP'000) - Phase 1", '29',"Enter")
            st.session_state.field30 = custom_number_input("Energy Consumption (KW/m³) - Phase 1", '30',"Enter")
            st.session_state.field31 = custom_number_input("Energy Cost (EGP/KW) - Phase 1", '31',"Enter")
            st.session_state.ogsgp1 = custom_number_input("Oil, Gas, Solar, and Gasoline (in LE'000s)  - Phase 1",'ogsgp1key', "Enter",0.0)
            st.session_state.ofo1 = custom_number_input("Other Fixed Opex (in LE'000s)  - Phase 1",'ofo1key', "Enter",0.0)
            if st.session_state.field30 != 0 and st.session_state.field31 != 0:
                st.write("Effective Price (EGP/m³) - Phase 1",st.session_state.field30*st.session_state.field31)
                st.session_state.field32 = st.session_state.field30*st.session_state.field31
            st.session_state.field33 = custom_number_input("RO Replacement Cost (EGP'000) - Phase 1", '33',"Enter")
        if check_phase1 and not check_phase2:
            st.button("Continue", on_click=continue_to_dashboard,key='cont1')
        if check_phase2:
            st.button("Continue", on_click=continue_to_phase2,key='cont2')
elif st.session_state.page == 'phase2':
    def custom_number_input(label, key, placeholder,value=0.0):
        return st.number_input(label, key=key, step=0.01,value=value,placeholder=placeholder)
    
    def custom_percentage_input(label, key, placeholder,value=0.0):
        return st.number_input(label, key=key, step=0.01,max_value=100.0,value=value,placeholder=placeholder)

    def custom_text_input(label, key, placeholder):
        return st.text_input(label, key=key, placeholder=placeholder)
    
    def custom_date_input(label, key):
        return st.date_input(label, key=key)
    
    def calculate_future_date_months(date, months):
        whole_months = int(months)
        fractional_months = months - whole_months
        future_date = date + relativedelta(months=whole_months)
        additional_days = int(fractional_months * 30)
        future_date += relativedelta(days=additional_days)
        return future_date
    
    def calculate_future_date_years(date, years):
        whole_years = int(years)
        fractional_years = years - whole_years
        future_date = date + relativedelta(years=whole_years)
        additional_days = int(fractional_years * 365)
        future_date += relativedelta(days=additional_days)
        return future_date

    st.markdown(
        f'<div style="background-color: {bg_color}; color: white; padding: 5px; border-radius: 15px; margin-bottom: 15px; width: 100%; text-align: center; font-size: 54px; margin-top: -50px;" class="center-text">'
        '<strong>FINANCIAL ASSESSMENT</strong>'
        '</div>', unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(
        f'<div style="background-color: {bg_color}; color: white; padding: 5px; border-radius: 15px; margin-bottom: 15px; width: 80%; text-align: center; font-size: 36px; margin-top: -50px;" class="center-text">'
        '<strong>Phase 2</strong>'
        '</div>', unsafe_allow_html=True)
    st.session_state.fcp2 = custom_date_input("Financial Close - Phase 2", 'fcp2key')
    st.session_state.field35 = custom_date_input("Construction Start Date - Phase 2", '35')
    st.session_state.field36 = custom_number_input("Construction Period(in months) - Phase 2", '36', "Enter",0.0)
    if st.session_state.field36 != 0:
        st.write("Construction End Date:", calculate_future_date_months(st.session_state.field35,st.session_state.field36)) # TBC
        st.session_state.field37 = calculate_future_date_months(st.session_state.field35,st.session_state.field36)
    st.session_state.osdp2 = custom_date_input("Operations Start Date - Phase 2", 'osdp2key')
    st.session_state.field38 = custom_number_input("Operations Period(in months) - Phase 2", '38', "Enter",0.0)
    if st.session_state.field38 != 0:
        st.session_state.oedp2 = st.write("Operations End Date: - Phase 2", calculate_future_date_years(st.session_state.osdp2,st.session_state.field38)) # TBC
        st.session_state.oedp2 = calculate_future_date_years(st.session_state.osdp2,st.session_state.field38)
    st.session_state.drsdp2 = custom_date_input("Debt Repayment Start Date - Phase 2", 'drsdp2key')
    st.session_state.drtp2 = custom_number_input("Debt Repayment Tenor(in Years) - Phase 2", 'drtp2key', "Enter")
    if st.session_state.drtp2 != 0:
        st.session_state.dredp2 = st.write("Debt Repayment End Date: - Phase 2", calculate_future_date_years(st.session_state.drsdp2,st.session_state.drtp2)) # TBC
        st.session_state.dredp2 = calculate_future_date_years(st.session_state.drsdp2,st.session_state.drtp2)
    st.session_state.cepsp2 = custom_number_input("Capital Expenditure - Pre sensitivity (in LE'000s) - Phase 2", 'cepsp1key', "Enter")
    st.session_state.field40 = custom_percentage_input("Debt Ratio (%) - Phase 2", '40', "Enter",0.0) 
    st.session_state.field41 = custom_percentage_input("Equity Ratio (%) - Phase 2", '41', "Enter",0.0)
    st.session_state.field42 = custom_percentage_input("Construction Interest Rate (Base Rate %) - Phase 2", '42', "Enter",0.0) 
    st.session_state.field43 = custom_percentage_input("Construction Interest Rate (Margin Spread %) - Phase 2",'43', "Enter",0.0)
    if st.session_state.field42 != 0 and st.session_state.field43 != 0:
        st.write("All in Rate (%) - Phase 2", st.session_state.field42 + st.session_state.field43) # TBC
        st.session_state.field44 = st.session_state.field42 + st.session_state.field43
    st.session_state.field45 = custom_percentage_input("Operations Interest Rate (Base Rate %) - Phase 2",'45', "Enter",0.0)
    st.session_state.field46 = custom_percentage_input("Operations Interest Rate (Margin Spread %) - Phase 2",'46', "Enter",0.0)
    if st.session_state.field45 != 0 and st.session_state.field46 != 0:
        st.write("All in Rate (%) - Phase 2", st.session_state.field45 + st.session_state.field46) # TBC
        st.session_state.field47 = st.session_state.field45 + st.session_state.field46
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(
        f'<div style="background-color: {bg_color}; color: white; padding: 5px; border-radius: 15px; margin-bottom: 15px; width: 80%; text-align: center; font-size: 36px; margin-top: -50px;" class="center-text">'
        '<strong>Phase 2</strong>'
        '</div>', unsafe_allow_html=True)
    col1, col2 = st.columns((1, 1))
    with col1:
        st.session_state.field48 = custom_number_input("Construction Cost - Phase 2", '48',"Enter",0.0)
        st.session_state.field49 = custom_number_input("Gross Availability - Phase 2", '49',"Enter",0.0)
        st.session_state.field50 = custom_percentage_input("Availibility Factor (%) - Phase 2", '50',"Enter",95.0)
        st.session_state.field51 = custom_percentage_input("Input to Output Ratio (%) - Phase 2", '51',"Enter",100.0)
        st.session_state.field52 = custom_percentage_input("Leakage Ratio/Losses (%) - Phase 2", '52',"Enter",95.0)
        st.session_state.field53 = custom_number_input("Labor Cost (EGP'000) - Phase 2", '53',"Enter",0.0)
        st.session_state.field54 = custom_number_input("Maintenance Costs (EGP'000) - Phase 2", '54',"Enter",0.0)
        st.session_state.cgp2 = custom_number_input("Chlorine Gas (in LE'000s) - Phase 2",'cgp2key', "Enter",0.0)
        st.session_state.cfltp2 = custom_number_input("Chemical for laboratory test (in LE'000s) - Phase 2",'cfltp2key', "Enter",0.0)
    with col2:
        st.session_state.field55 = custom_number_input("Environment & Performance Monitoring Costs (EGP'000) - Phase 2", '55',"Enter",0.0)
        st.session_state.field56 = custom_number_input("Maintenance Cost (EGP'000) - Phase 2", '56',"Enter",0.0)
        st.session_state.field57 = custom_number_input("Variable Cost (EGP'000) - Phase 2", '57',"Enter",0.0)
        st.session_state.field58 = custom_number_input("Energy Consumption (KW/m³) - Phase 2", '58',"Enter",0.0)
        st.session_state.field59 = custom_number_input("Energy Cost (EGP/KW) - Phase 2", '59',"Enter",0.0)
        st.session_state.ogsgp2 = custom_number_input("Oil, Gas, Solar, and Gasoline (in LE'000s)  - Phase 2",'ogsgp2key', "Enter",0.0)
        st.session_state.ofo2 = custom_number_input("Other Fixed Opex (in LE'000s)  - Phase 2",'ofo2key', "Enter",0.0)
        if st.session_state.field58 != 0 and st.session_state.field59 != 0:
            st.write("Effective Price (EGP/m³) - Phase 2",st.session_state.field58*st.session_state.field59)
            st.session_state.field60 = st.session_state.field58*st.session_state.field59
        st.session_state.field61 = custom_number_input("RO Replacement Cost (EGP'000) - Phase 2", '61',"Enter",0.0)
    col1,col2 = st.columns([1,18])
    with col1:
        if st.session_state.page == 'phase2':
            st.button("Back", on_click=continue_to_phase)
    with col2:
        # if st.session_state.page == 'phase2':
        st.button("Continue", on_click=continue_to_dashboard)
elif st.session_state.page == 'dashboard':
    st.markdown(
        f'<div style="background-color: {bg_color}; color: white; padding: 5px; border-radius: 50px; margin-bottom: 15px; width: 80%; text-align: center;font-size: 36px; margin-top: -50px;" class="center-text">'
        '<strong>WELCOME TO THE EU TAXONOMY DASHBOARD</strong>'
        '</div>', unsafe_allow_html=True)
    def load_lottie_url(url: str):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None
    lottie_url1 = "https://assets10.lottiefiles.com/packages/lf20_jcikwtux.json"  # Example URL
    lottie_url2 = "https://lottie.host/da208e68-3a3a-48a9-b73f-17f8925cde2a/zJ0MoRmhHJ.json"
    lottie_animation1 = load_lottie_url(lottie_url1)
    lottie_animation2 = load_lottie_url(lottie_url2)
    st.sidebar.header("Dashboard Navigation")
    options = st.sidebar.radio("Select a page:", ["Data Overview","User Details","Download Report"])
    if  options == "Data Overview":
        st.title("Data Overview")
        st_lottie(lottie_animation1, height=300, key="data_overview")
        st.write("Here you can review detailed data insights.")
    elif options == "User Details":
        col1,col2 = st.columns([3,5])
        with col1:
            st.markdown("<br><br>", unsafe_allow_html=True)
            # st_lottie(lottie_animation1, height=350, key="home1")
            st_lottie(lottie_animation2, height=400, key="home2")
        with col2:
            st.markdown(
            f'<br><div style="background-color: #3f3f3f; color: white; padding: 10px; border-radius: 50px; width:70%; margin-bottom: 15px; font-size: 28px;text-align: center;">'
            '<strong>USER DETAILS</strong>'
            '</div>', unsafe_allow_html=True)
            custom_css = """
            <style>
            .custom-text {
                font-family: 'Arial', sans-serif; /* Change the font family here */
                font-size: 24px; /* Change the text size here */
                color: #333; /* Change the text color here */
                background-color: #FFD700; /* Change the background color here */
                padding: 10px; /* Add some padding if needed */
                border-radius: 50px; /* Optional: Add rounded corners */
                text-align: center;
                margin-bottom: 15px;
                width:70%;
            }
            </style>
            """

            st.markdown(custom_css, unsafe_allow_html=True)

            st.markdown(f'<div class="custom-text">Username: {st.session_state.field1}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="custom-text">Project: {st.session_state.field2}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="custom-text">Capacity: {st.session_state.field3}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="custom-text">Location: {st.session_state.field4}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="custom-text">Date: {st.session_state.field5}</div>', unsafe_allow_html=True)
    elif options == "Download Report":
        st_lottie(lottie_animation1, height=400, key="home3")
        def generate_report():
            data = {
                "Field": ["Username", "Project", "Capacity", "Location", "Option"],
                "Value": [
                    st.session_state.field1,
                    st.session_state.field2,
                    st.session_state.field3,
                    st.session_state.field4,
                    st.session_state.field5
                ]
            }
            df = pd.DataFrame(data)
            
            buffer = StringIO()
            df.to_csv(buffer, index=False)
            return buffer.getvalue()

        # Download button
        csv_report = generate_report()
        st.markdown("""
            <style>
            .download-button {
                display: flex;
                justify-content: center;
                align-items: center;
                
            }
            .download-button a {
                display: inline-block;
                padding: 20px 40px;
                font-size: 18px;
                color: white;
                background-color: #007bff;
                border-radius: 5px;
                text-decoration: none;
                text-align: center;
            }
            .download-button a:hover {
                background-color: #0056b3;
            }
            </style>
            <div class="download-button">
                <a href="data:text/csv;charset=utf-8,{csv_report}" download="report.csv">Download Report</a>
            </div>
        """, unsafe_allow_html=True)
        # st.download_button(
        #     label="Download Report",
        #     data=csv_report,
        #     file_name="report.csv",
        #     mime="text/csv"
        # )

import streamlit as st
from dateutil.relativedelta import relativedelta
from datetime import datetime
# Page configuration
st.set_page_config(
    page_title="EU Taxonomy",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Define a common background color
bg_color = "#000C66"  # Adjust this color as needed
# if 'field48' not in st.session_state:
#     st.session_state.field48 = 0.0
# CSS style for larger font size
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

def continue_to_next_page():
    st.session_state.page = 'next_page'

def continue_to_next_page1():
    st.session_state.page = 'next_page1'

def continue_to_next_page2():
    st.session_state.page = 'next_page2'
    
def go_back_to_main_page():
    st.session_state.page = 'main'
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
        field1 = ""
        field2 = ""
        field3 = ""
        field4 = ""
        field5 = ""
        field1 = st.text_input("Username", key='field1', placeholder="Enter username")
        field2 = st.text_input("Project", key='field2', placeholder="Enter project name")
        field3 = st.text_input("Capacity", key='field3', placeholder="Enter capacity in m3/d")
        field4 = st.text_input("Location", key='field4', placeholder="Enter location")
        # field5 = st.text_input("Date", key='field5', placeholder="Enter date(DD/MM/YYYY)")
        field5 = st.date_input("Date", key='field5')

        if st.button('Next') and field1 != "" and field2 != "" and field3 != "" and field4 != "" and field5 != "":
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
            if (answer2 == "Yes" and (answer5 <= 1.5 and answer4 <= 0.5)) or (answer3 == "Yes"  and (answer6 >= 20 and answer7 >= 20)):
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
                                                        st.button("Continue", on_click=continue_to_next_page)
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
elif st.session_state.page == 'next_page':
    field11 = 0
    field16 = 0
    field19 = 0
    field32 = 0
    def custom_number_input(label, key, placeholder,value=0.0):
        return st.number_input(label, key=key, step=0.01,value=value,placeholder=placeholder)
    
    def custom_percentage_input(label, key, placeholder,value=0.0):
        return st.number_input(label, key=key, step=0.01,max_value=100.0,value=value,placeholder=placeholder)

    def custom_text_input(label, key, placeholder):
        return st.text_input(label, key=key, placeholder=placeholder)
    
    def custom_date_input(label, key):
        return st.date_input(label, key=key)
    
    def calculate_future_date(date, months):
        whole_months = int(months)
        fractional_months = months - whole_months
        future_date = date + relativedelta(months=whole_months)
        additional_days = int(fractional_months * 30)
        future_date += relativedelta(days=additional_days)
        return future_date

    st.markdown(
        f'<div style="background-color: {bg_color}; color: white; padding: 5px; border-radius: 15px; margin-bottom: 15px; width: 100%; text-align: center; font-size: 54px; margin-top: -50px;" class="center-text">'
        '<strong>FINANCIAL ASSESSMENT</strong>'
        '</div>', unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(
        f'<div style="background-color: {bg_color}; color: white; padding: 5px; border-radius: 15px; margin-bottom: 15px; width: 80%; text-align: center; font-size: 36px; margin-top: -50px;" class="center-text">'
        '<strong>Phase 1</strong>'
        '</div>', unsafe_allow_html=True)
    field6 = custom_number_input("Exchange Rate - Phase 1", 'field6', "Enter")
    field7 = custom_date_input("Construction Start Date - Phase 1", 'field7')
    field8 = custom_number_input("Construction Period(in months) - Phase 1", 'field8', "Enter")
    if field8 != 0:
        st.write("Construction End Date: - Phase 1", calculate_future_date(field7,field8)) # TBC
        field9 = calculate_future_date(field7,field8)
    field10 = custom_number_input("Operations Period(in months) - Phase 1", 'field10', "Enter")
    if field10 != 0:
        field11 = st.write("Operations End Date: - Phase 1", calculate_future_date(field9,field10)) # TBC
    field12 = custom_percentage_input("Debt Ratio (%) - Phase 1", 'field12', "Enter") 
    field13 = custom_percentage_input("Equity Ratio (%) - Phase 1", 'field13', "Enter")
    field14 = custom_percentage_input("Construction Interest Rate (Base Rate %) - Phase 1", 'field14', "Enter") 
    field15 = custom_percentage_input("Construction Interest Rate (Margin Spread %) - Phase 1",'field15', "Enter")
    if field14 != 0 and field15 != 0:
        field16 = st.write("All in Rate (%)", field14 + field15) # TBC
    field17 = custom_percentage_input("Operations Interest Rate (Base Rate %) - Phase 1",'field17', "Enter")
    field18 = custom_percentage_input("Operations Interest Rate (Margin Spread %) - Phase 1",'field18', "Enter")
    if field17 != 0 and field18 != 0:
        field19 = st.write("All in Rate (%) - Phase 1", field17 + field18) # TBC
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(
        f'<div style="background-color: {bg_color}; color: white; padding: 5px; border-radius: 15px; margin-bottom: 15px; width: 80%; text-align: center; font-size: 36px; margin-top: -50px;" class="center-text">'
        '<strong>Phase 1</strong>'
        '</div>', unsafe_allow_html=True)
    col1, col2 = st.columns((1, 1))
    with col1:
        field20 = custom_number_input("Construction Cost - Phase 1", 'field20',"Enter")
        field21 = custom_number_input("Gross Availability - Phase 1", 'field21',"Enter")
        field22 = custom_percentage_input("Availibility Factor (%) - Phase 1", 'field22',"Enter",95.0)
        field23 = custom_percentage_input("Input to Output Ratio (%) - Phase 1", 'field23',"Enter",100.0)
        field24 = custom_percentage_input("Leakage Ratio/Losses (%) - Phase 1", 'field24',"Enter",95.0)
        field25 = custom_number_input("Labor Cost (EGP'000) - Phase 1", 'field25',"Enter")
        field26 = custom_number_input("Maintenance Costs (EGP'000) - Phase 1", 'field26',"Enter")
    with col2:
        field27 = custom_number_input("Environment & Performance Monitoring Costs (EGP'000) - Phase 1", 'field27',"Enter")
        field28 = custom_number_input("Maintenance Cost (EGP'000) - Phase 1", 'field28',"Enter")
        field29 = custom_number_input("Variable Cost (EGP'000) - Phase 1", 'field29',"Enter")
        field30 = custom_number_input("Energy Consumption (KW/m³) - Phase 1", 'field30',"Enter")
        field31 = custom_number_input("Energy Cost (EGP/KW) - Phase 1", 'field31',"Enter")
        if field30 != 0 and field31 != 0:
            field32 = st.write("Effective Price (EGP/m³) - Phase 1",field30*field31)
        field33 = custom_number_input("RO Replacement Cost (EGP'000) - Phase 1", 'field33',"Enter")
    st.button("Continue", on_click=continue_to_next_page1)
elif st.session_state.page == 'next_page1':
    field34 = 0
    field39 = 0
    field44 = 0
    field60 = 0
    def custom_number_input(label, key, placeholder,value=0.0):
        return st.number_input(label, key=key, step=0.01,value=value,placeholder=placeholder)
    
    def custom_percentage_input(label, key, placeholder,value=0.0):
        return st.number_input(label, key=key, step=0.01,max_value=100.0,value=value,placeholder=placeholder)

    def custom_text_input(label, key, placeholder):
        return st.text_input(label, key=key, placeholder=placeholder)
    
    def custom_date_input(label, key):
        return st.date_input(label, key=key)
    
    def calculate_future_date(date, months):
        whole_months = int(months)
        fractional_months = months - whole_months
        future_date = date + relativedelta(months=whole_months)
        additional_days = int(fractional_months * 30)
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
    # field34 = custom_number_input("Exchange Rate", 'field34', "Enter",0.0)
    field35 = custom_date_input("Construction Start Date - Phase 2", 'field35')
    field36 = custom_number_input("Construction Period(in months) - Phase 2", 'field36', "Enter",0.0)
    if field36 != 0:
        st.write("Construction End Date:", calculate_future_date(field35,field36)) # TBC
        field37 = calculate_future_date(field35,field36)
    field38 = custom_number_input("Operations Period(in months) - Phase 2", 'field38', "Enter",0.0)
    if field38 != 0:
        field39 = st.write("Operations End Date: - Phase 2", calculate_future_date(field37,field38)) # TBC
    field40 = custom_percentage_input("Debt Ratio (%) - Phase 2", 'field40', "Enter",0.0) 
    field41 = custom_percentage_input("Equity Ratio (%) - Phase 2", 'field41', "Enter",0.0)
    field42 = custom_percentage_input("Construction Interest Rate (Base Rate %) - Phase 2", 'field42', "Enter",0.0) 
    field43 = custom_percentage_input("Construction Interest Rate (Margin Spread %) - Phase 2",'field43', "Enter",0.0)
    if field42 != 0 and field43 != 0:
        field44 = st.write("All in Rate (%) - Phase 2", field42 + field43) # TBC
    field45 = custom_percentage_input("Operations Interest Rate (Base Rate %) - Phase 2",'field45', "Enter",0.0)
    field46 = custom_percentage_input("Operations Interest Rate (Margin Spread %) - Phase 2",'field46', "Enter",0.0)
    if field45 != 0 and field46 != 0:
        field47 = st.write("All in Rate (%) - Phase 2", field45 + field46) # TBC
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(
        f'<div style="background-color: {bg_color}; color: white; padding: 5px; border-radius: 15px; margin-bottom: 15px; width: 80%; text-align: center; font-size: 36px; margin-top: -50px;" class="center-text">'
        '<strong>Phase 2</strong>'
        '</div>', unsafe_allow_html=True)
    col1, col2 = st.columns((1, 1))
    with col1:
        field48 = custom_number_input("Construction Cost - Phase 2", 'field48',"Enter",0.0)
        field49 = custom_number_input("Gross Availability - Phase 2", 'field49',"Enter",0.0)
        field50 = custom_percentage_input("Availibility Factor (%) - Phase 2", 'field50',"Enter",95.0)
        field51 = custom_percentage_input("Input to Output Ratio (%) - Phase 2", 'field51',"Enter",100.0)
        field52 = custom_percentage_input("Leakage Ratio/Losses (%) - Phase 2", 'field52',"Enter",95.0)
        field53 = custom_number_input("Labor Cost (EGP'000) - Phase 2", 'field53',"Enter",0.0)
        field54 = custom_number_input("Maintenance Costs (EGP'000) - Phase 2", 'field54',"Enter",0.0)
    with col2:
        field55 = custom_number_input("Environment & Performance Monitoring Costs (EGP'000) - Phase 2", 'field27',"Enter",0.0)
        field56 = custom_number_input("Maintenance Cost (EGP'000) - Phase 2", 'field28',"Enter",0.0)
        field57 = custom_number_input("Variable Cost (EGP'000) - Phase 2", 'field29',"Enter",0.0)
        field58 = custom_number_input("Energy Consumption (KW/m³) - Phase 2", 'field58',"Enter",0.0)
        field59 = custom_number_input("Energy Cost (EGP/KW) - Phase 2", 'field59',"Enter",0.0)
        if field58 != 0 and field59 != 0:
            field60 = st.write("Effective Price (EGP/m³) - Phase 2",field58*field59)
        field61 = custom_number_input("RO Replacement Cost (EGP'000) - Phase 2", 'field33',"Enter",0.0)
#     st.button("Continue", on_click=continue_to_next_page2)
# elif st.session_state.page == 'next_page2':
#     st.markdown("Dashboard", unsafe_allow_html=True)
#     st.write("Exchange Rate:", st.session_state.field48)
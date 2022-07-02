import streamlit as st
import base64
import pickle
from PIL import Image

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
# Image For Page
image = Image.open('image.png')

col1.header("Telecommunication Customer Churn Prediction App ")
header = '<p style="font-family:sans-serif; color:Grey;">This Web Application can predict if a customer will stay or churn a telecommunication service.</p>'
col1.markdown(header, unsafe_allow_html=True)
subheader = '<p style="font-family:sans-serif; color:Grey;">We created this webapp to help reduce the high rate of customer churn in telecommunication industries.</p>'
col1.markdown(subheader, unsafe_allow_html=True)
col1.write("[![Ayobami's Page](https://img.icons8.com/material-outlined/24/undefined/github.png)](https://github.com/Ayobami6) Ayobami's Page") 
col1.write("[![Project Page](https://img.icons8.com/material-outlined/24/undefined/github.png)](https://github.com/Ayobami6/ProjectCollaboration.github.io) Project Source Code")
col1.write("[![Designegycreatives's Page](https://img.icons8.com/material-outlined/24/undefined/github.png)](https://github.com/Designegycreatives) Designegy Creatives's Page")
col2.image(image)

st.write("Fill in the following details correctly.")

trained_model = pickle.load(
    open('data/customer_churn.pkl', 'rb'))

# creating function to make prediction


def generateprediction(data):

    makeprediction = trained_model.predict(data)
    print(makeprediction)

    if (makeprediction[0] == 'Churned'):
        st.write('The Customer will Churn 😲')
    else:
        st.write('The Customer will Stay 🤑')

# Creating a function for main app interface
# input data

# forms = st.form("forms", clear_on_submit=True)
try:
    Age = col3.text_input('Enter Customer Age')
    Number_of_Dependents = col4.text_input('Enter Number Of Dependent')
    Number_of_Referrals = col3.text_input('Enter Number Of Referrals')
    Tenure_in_Months = col4.text_input('Enter Total Number Of Months')
    Monthly_Charge = col3.text_input('Enter Total Monthly Charges')
    Total_Charges = col4.text_input('Enter Total Charges')
# submit = forms.form_submit_button('Submit')

    default_check = ""

# prediction code
    if st.button('Predict'):
        default_check = generateprediction([[Age, Number_of_Dependents, Number_of_Referrals, Tenure_in_Months,
                                             Monthly_Charge, Total_Charges]])

except:
    pass
st.success(default_check)


# if __name__ == '__app__':
#     app()



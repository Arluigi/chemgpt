import streamlit as st
import requests

query = st.text_input("What is your question? ")

# Endpoint URL to send the input to
url = "https://sharedinfrastorequery-qqs3.zeet-berri.zeet.app/berri_query?proj_path=indexes/svishal2001@gmail.com/c33971a9-f74c-45fe-af90-9aa141cc127e&query="

response = requests.get(url + query)

# Print the response from the endpoint
st.write(response.text)


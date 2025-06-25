import streamlit as st

st.set_page_config(
    layout= 'wide',
    page_title= "Fraude Bancaire"
)

acceuil_page = st.Page("pages/acceuil.py", title="Create entry")
prediction_page = st.Page("pages/prediction.py", title="Prediction",)

pg = st.navigation([acceuil_page, prediction_page], position='hidden')
pg.run()

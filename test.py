import streamlit as st 
from streamlit_calendar import calendar 

st.set_page_config(layout='wide')

st.header('Hello World')

st.markdown('This is a test!')

calendar(
    events=[],
    options={
        "height": "auto",         # full height
        "expandRows": True,
        "initialView": "dayGridMonth",
        "headerToolbar": {
            "left": "prev,next today",
            "center": "title",
            "right": "dayGridMonth,timeGridWeek"
        },
        "slotDuration": "12:00:00",
        "slotLabelFormat": {
            "hour": "numeric",
            "minute": "2-digit",
            "meridiem": "short"     
        },
    },
)
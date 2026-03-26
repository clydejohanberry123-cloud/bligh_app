# import streamlit as st 
# from streamlit_calendar import calendar 

# st.set_page_config(layout='wide')

# st.header('Hello World')

# st.markdown('This is a test!')



# calendar(
#     events=[],
#     options={
#         "height": "auto",         # full height
#         "expandRows": True,
#         "initialView": "dayGridMonth",
#         "headerToolbar": {
#             "left": "prev,next today",
#             "center": "title",
#             "right": "dayGridMonth,timeGridWeek"
#         },
#         "slotDuration": "12:00:00",
#         "slotLabelFormat": {
#             "hour": "numeric",
#             "minute": "2-digit",
#             "meridiem": "short"     
#         },
#     },
# )

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
st.title("Employee Shift Calendar")

html_code = """
<!DOCTYPE html>
<html>
  <head>
    <link href='https://cdn.jsdelivr.net/npm/fullcalendar@6.1.8/main.min.css' rel='stylesheet' />
    <script src='https://cdn.jsdelivr.net/npm/fullcalendar@6.1.8/main.min.js'></script>
    <script src='https://cdn.jsdelivr.net/npm/fullcalendar-scheduler@6.1.8/main.global.min.js'></script>
    <style>
      body { margin: 0; padding: 0; font-family: Arial, Helvetica; }
      #calendar { max-width: 100%; margin: 0 auto; }
    </style>
  </head>
  <body>
    <div id='calendar'></div>
    <script>
      document.addEventListener('DOMContentLoaded', function() {
        var calendarEl = document.getElementById('calendar');

        var calendar = new FullCalendar.Calendar(calendarEl, {
          initialView: 'resourceTimelineWeek',
          resourceAreaHeaderContent: 'Employees',
          resources: [
            { id: 'bligh', title: 'Bligh' },
            { id: 'chris', title: 'Chris' },
            { id: 'james', title: 'James' }
          ],
          events: [
            { id: '1', resourceId: 'bligh', title: 'Surgical', start: '2026-03-26', end: '2026-03-26', color: 'green' },
            { id: '2', resourceId: 'chris', title: 'Leave', start: '2026-03-27', end: '2026-03-27', color: 'red' }
          ],
          height: 'auto'
        });

        calendar.render();
      });
    </script>
  </body>
</html>
"""

components.html(html_code, height=600, scrolling=True)
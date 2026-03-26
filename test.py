import streamlit as st
import calendar

st.set_page_config(layout="wide")

st.title("Employee Shift Calendar - Monthly View (AM/PM)")

# --------------------
# Year & Month selectors side by side
# --------------------
col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    year = st.number_input("Select Year", min_value=2000, max_value=2100, value=2026, step=1)
with col2:
    month = st.selectbox(
        "Select Month", 
        options=list(range(1, 13)),
        format_func=lambda x: calendar.month_name[x]
    )

# --------------------
# Employees and example shift data
# --------------------
employees = ["Berry", "Parker", "Charles", "Abeysuriya", "Foo", "O'Niell"]

shift_data = {
    ("Berry", f"{year}-03-01", "AM"): "Surgical 1",
    ("James", f"{year}-03-01", "PM"): "Placenta 1",
    ("Bligh", f"{year}-03-01", "AM"): "Surgical 2",
    ("Bligh", f"{year}-03-01", "PM"): "Placenta 2",
    ("Kate", f"{year}-03-01", "AM"): "Surgical 3",
    ("Kate", f"{year}-03-01", "PM"): "Placenta 3",

    ("Adam", f"{year}-03-02", "AM"): "Annual Leave",
    ("Chris", f"{year}-03-03", "PM"): "Surgical 2",
}

shift_colors = {
    "Surgical 1": "#FFD700",
    "Surgical 2": "#FFA500",
    "Placenta 1": "#ADD8E6",
    "Annual Leave": "#90EE90"
}

# --------------------
# Build calendar
# --------------------
cal = calendar.Calendar(firstweekday=0)  # Monday first
html = "<div style='display: grid; grid-template-columns: repeat(7, 1fr); gap:5px;'>"

# Weekday headers
weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for wd in weekdays:
    html += f"<div style='font-weight:bold; text-align:center;'>{wd}</div>"

# Days
for day in cal.itermonthdays(year, month):
    if day == 0:
        html += "<div></div>"  # empty padding
    else:
        html += "<div style='border:1px solid #ccc; min-height:80px; padding:2px; font-size:12px;'>"
        html += f"<div style='font-weight:bold; margin-bottom:2px;'>{day}</div>"
        
        # AM/PM columns
        html += "<div style='display:grid; grid-template-columns: 1fr 1fr; gap:2px;'>"
        for slot in ["AM", "PM"]:
            html += f"<div style='border-top:1px solid #ccc; padding:1px; min-height:40px;'>"
            html += f"<div style='font-size:10px; font-weight:bold;'>{slot}</div>"
            for emp in employees:
                date_str = f"{year}-{month:02d}-{day:02d}"
                shift = shift_data.get((emp, date_str, slot), "")
                if shift:
                    color = shift_colors.get(shift, "#eee")
                    html += f"<div style='background:{color}; margin:1px 0; padding:1px; border-radius:2px;'>"
                    html += f"{emp}: {shift}</div>"
            html += "</div>"
        html += "</div>"  # close AM/PM grid
        html += "</div>"  # close day box

html += "</div>"  # close calendar grid

st.markdown(html, unsafe_allow_html=True)
import streamlit as st

st.set_page_config(page_title="College FAQ Chatbot", page_icon="🎓")

st.title("🎓 AI College FAQ Chatbot")
st.write("Ask any question related to college (admission, fees, courses, etc.)")

# Sample FAQ data
faq_data = {
    "admission": "Admission process starts in June. You can apply online through the college website.",
    "fees": "Fees depend on the course. Please check the official fee structure on the website.",
    "courses": "We offer B.Tech, M.Tech, BSc, MSc and other programs.",
    "timing": "College timing is from 9 AM to 5 PM.",
    "hostel": "Hostel facilities are available for both boys and girls."
}

# Function
def get_response(query):
    query = query.lower()
    for key in faq_data:
        if key in query:
            return faq_data[key]
    return "Sorry, I don't understand. Please contact the college office."

# Chat UI
user_input = st.text_input("💬 Ask your question:")

if user_input:
    response = get_response(user_input)
    st.success(response)
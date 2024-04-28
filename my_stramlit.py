import streamlit as st

st.title("PDF Chatbot")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    pdf_text = extract_text_from_pdf(uploaded_file)
    st.write("PDF Uploaded Successfully!")
    st.subheader("Chat with the PDF:")
    user_input = st.text_input("You:", "")
    if st.button("Send"):
        response = generate_response(user_input, pdf_text)
        st.write("Bot:", response)

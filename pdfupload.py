import os
import pdfplumber
import openai
import streamlit as st

# Initialize OpenAI API with your API key
openai.api_key = "sk-proj-PkmTmWIXO4oJL5JFhjSCT3BlbkFJ0IpN1BCK0OKUIXjOy1ay"


# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text


def get_latest_engine():
    try:
        engines = openai.Engine.list()
        return engines[0].id if engines else None
    except Exception as e:
        st.error(f"Error retrieving engine: {e}")
        return None


# Function to generate response using OpenAI API
def generate_response(input_text, pdf_text, engine_id):
    prompt = input_text + "\n\n" + pdf_text
    response = openai.Completion.create(
        engine=engine_id, prompt=prompt, temperature=0.7, max_tokens=50
    )
    return response.choices[0].text.strip()


# Main function to run the Streamlit app
def main():
    st.set_page_config(page_title="PDF Chatbot")

    # File upload section
    uploaded_file = st.file_uploader("Upload PDF", type="pdf")

    if uploaded_file:
        pdf_text = extract_text_from_pdf(uploaded_file)
        st.write("PDF Uploaded Successfully!")
        st.subheader("Chat with the PDF:")

        user_input = st.text_input("You:", "")
        if st.button("Send"):
            engine_id = get_latest_engine()
            if engine_id:
                response = generate_response(user_input, pdf_text, engine_id)
                st.write("Bot:", response)
            else:
                st.error("Failed to retrieve available engine.")


if __name__ == "__main__":
    main()

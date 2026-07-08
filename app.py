import streamlit as st

st.set_page_config(page_title="Feedback Portal", page_icon="💬")

st.title("💬 Feedback Portal")
st.write("Please fill in the details below.")

name = st.text_input("Enter your Name")
email = st.text_input("Enter your Email")
message = st.text_area("Enter your Feedback")

character_count = len(message)
word_count = len(message.split())
estimated_tokens = round(character_count / 4)

if st.button("Submit Feedback"):

    if not name.strip() or not email.strip() or not message.strip():
        st.error("Please complete all the fields before submitting.")

    else:
        st.success(f"Thank you, {name}! Your feedback has been submitted successfully.")

        st.info(f"Estimated Tokens Used: {estimated_tokens}")

        st.write("### Feedback Summary")
        st.write(f"**Email:** {email}")
        st.write(f"**Word Count:** {word_count}")
        st.write(f"**Character Count:** {character_count}")
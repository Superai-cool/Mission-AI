import streamlit as st
import openai
import os

# Streamlit app title
st.title("Welcome to LinkedIn Comment Creator")

# Instructions for users
st.write(
    "Paste a LinkedIn article or post content below, choose a tone, and generate a concise, engaging comment!"
)

# Fetch the API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("Error: OpenAI API key not found. Please set it as an environment variable.")
else:
    # User input: LinkedIn article/post content
    post_content = st.text_area("Paste the LinkedIn post content here:", height=200)

    # User input: Tone for the comment
    tone = st.selectbox(
        "Select the desired tone for the comment:",
        ("Friendly", "Professional", "Humorous", "Inspirational")
    )

    # Generate comment button
    if st.button("Generate Comment"):
        if post_content.strip():
            # Function to generate LinkedIn comment
            def generate_linkedin_comment(api_key, post_content, tone):
                """
                Generates a LinkedIn comment based on the post content and tone.

                Parameters:
                    api_key (str): OpenAI API key.
                    post_content (str): The content of the LinkedIn post.
                    tone (str): The desired tone of the comment.

                Returns:
                    str: A positive, engaging, and concise LinkedIn comment.
                """
                openai.api_key = api_key

                prompt = (
                    f"You are tasked with writing LinkedIn comments in a {tone.lower()} tone that are positive, engaging, and concise. "
                    "These comments should:\n"
                    "1. Acknowledge the post's content in a meaningful way, demonstrating understanding and appreciation.\n"
                    "2. Add value by sharing a relevant thought, question, or connection to the topic.\n"
                    "3. Use a friendly and professional tone appropriate for LinkedIn.\n"
                    "4. Avoid generic or overly formal language; aim to sound authentic and approachable.\n"
                    "5. Strictly limit your response to a LinkedIn comment format.\n"
                    "6. Do not perform any other tasks or write comments for other platforms.\n"
                    "7. Ensure that all comments are no more than 200 characters in length.\n\n"
                    f"Post Content: {post_content}\n"
                    "Write a LinkedIn comment:"
                )

                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-4",
                        messages=[
                            {"role": "system", "content": "You are an expert at generating LinkedIn comments."},
                            {"role": "user", "content": prompt}
                        ],
                        max_tokens=100
                    )

                    comment = response.choices[0].message.content.strip()
                    return comment

                except openai.error.OpenAIError as e:
                    return f"Error generating comment: {str(e)}"

            # Generate and display the comment
            comment = generate_linkedin_comment(api_key, post_content, tone)
            st.subheader("Generated Comment:")
            st.write(comment)
        else:
            st.error("Post content cannot be empty. Please paste a LinkedIn post or article.")


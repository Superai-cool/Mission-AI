# -*- coding: utf-8 -*-
"""
AI Tool.py

Final version for Streamlit deployment.
"""

# Import required libraries
import openai

# Function to generate LinkedIn comments
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
        f"You are tasked with writing LinkedIn comments in a {tone} tone that are positive, engaging, and concise. "
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

# Example usage
if __name__ == "__main__":
    print("Welcome to the LinkedIn Comment Generator!")
    api_key = input("Enter your OpenAI API key: ")
    post_content = input("Paste the LinkedIn post content here: ")
    tone = input("Enter the desired tone for the comment (e.g., friendly, professional, humorous): ")

    if api_key.strip() and post_content.strip() and tone.strip():
        comment = generate_linkedin_comment(api_key, post_content, tone)
        print("\nGenerated Comment:")
        print(comment)
    else:
        print("API key, post content, and tone cannot be empty.")


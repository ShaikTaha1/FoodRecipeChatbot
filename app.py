import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = 'Your API Key'

# Function to generate response from OpenAI
def get_response(prompt, model="gpt-3.5-turbo"):
    try:
        response = openai.ChatCompletion.create(
            model=model,  # or use "gpt-4" if available
            messages=[
                {"role": "system", "content": "You are a knowledgeable chef."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            n=1,
            temperature=0.7,
        )
        return response.choices[0].message['content'].strip()
    except openai.error.OpenAIError as e:
        return f"An error occurred: {e}"

# Streamlit app
def main():
    st.title("Food Recipe Chatbot")
    st.write("Ask me anything about food recipes, cooking tips, and ingredient substitutions!")

    user_query = st.text_input("You: ", "How do I make a chocolate cake?")

    if user_query:
        # Get the response from OpenAI
        response = get_response(user_query)
        st.text_area("Chatbot:", response, height=200)

if __name__ == "__main__":
    main()

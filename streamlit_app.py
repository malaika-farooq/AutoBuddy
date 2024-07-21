import streamlit as st
from together import Together

# Access the API key from Streamlit secrets
together_api_key = st.secrets["TOGETHER_API_KEY"]

# Initialize the Together client with the API key
client = Together(api_key=together_api_key)
# Set page config with title and favicon
st.set_page_config(
    page_title="AutoBuddy🚗⚙🛠",
    page_icon="assets/AutoBuddy.png",
)
# Add custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .sidebar .sidebar-content {
        background-color: #D91320;
    }
    .stButton>button {
        color: #FFFFFF;
        background-color: #D91320;
    }
    .stChatMessage--assistant {
        background-color: #ffe5e5;
    }
    .stChatMessage--user {
        background-color: #e0e0e0;
    }
    .title {
        color: #08214D;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar
st.sidebar.image("assets/AutoBuddy.png", use_column_width=True)
st.sidebar.write("""
**AutoBuddy** is your intelligent assistant for diagnosing vehicle issues. Powered by advanced AI technology, AutoBuddy helps you troubleshoot problems by providing detailed insights and potential solutions. Whether you have a Nissan, Ford, Toyota, or any other vehicle, AutoBuddy is here to assist you.
""")

st.sidebar.header("How to Use AutoBuddy")
st.sidebar.write("""
1. **Enter Your Vehicle Information**:
   - Provide the vehicle company, model, and year.
   - Describe the issue or fault you are experiencing with your vehicle.

2. **Submit the Information**:
   - Use the input field at the bottom of the page to enter the required details.

3. **Get a Response**:
   - AutoBuddy will process your input and generate a detailed response with possible causes and solutions for the issue.

4. **Review and Take Action**:
   - Read the response provided by AutoBuddy and follow the suggested steps to address the vehicle issue.
   - If necessary, consult with a professional mechanic for further assistance.
""")
st.sidebar.markdown("### Social Links:")
st.sidebar.write("🔗 [GitHub](https://www.github.com)")

# Show title and description.
st.markdown('<h1 class="title">AutoBuddy🚗⚙🛠</h1>', unsafe_allow_html=True)
st.write(
    "This is your Auto Buddy that uses Llama3 model to generate solutions to your problems."
)

# Create a session state variable to store the chat messages. This ensures that the
# messages persist across reruns.
if "messages" not in st.session_state:
    st.session_state.messages = []
    instruction = "Hi! This is your AutoBuddy🚗. Please mention the Vehicle Company, Model, Year, the Fault/Issue you are facing. For example; My vehicle company is Nissan, model Sentra 2000, and the issue I am facing is Fuel Pump Failure."
    st.session_state.messages.append({"role": "assistant", "content": instruction})

# Display the existing chat messages via `st.chat_message`.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Create a chat input field to allow the user to enter a message. This will display
# automatically at the bottom of the page.
if prompt := st.chat_input("What is the issue you are facing with your Vehicle?"):

    # Store and display the current prompt.
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate a response using the Together API.
    with st.spinner("Generating response..."):
        try:
            response = client.chat.completions.create(
                model="meta-llama/Llama-3-8b-chat-hf",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            # Collect and concatenate response chunks
            if response.choices and response.choices[0].message:
                full_response = response.choices[0].message.content

                # Stream the full response to the chat using `st.write`
                with st.chat_message("assistant"):
                    st.markdown(full_response)
                
                st.session_state.messages.append({"role": "assistant", "content": full_response})
        except Exception as e:
            st.error(f"An error occurred: {e}")

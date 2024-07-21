# AutoBuddy 🚗⚙🛠

**AutoBuddy** is an intelligent assistant for diagnosing vehicle issues. Powered by advanced AI technology, AutoBuddy helps you troubleshoot problems by providing detailed insights and potential solutions. Whether you have a Nissan, Ford, Toyota, or any other vehicle, AutoBuddy is here to assist you.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Features

- **Vehicle Diagnostics**: Enter your vehicle information and get detailed diagnostics.
- **AI-Powered Insights**: Powered by the Llama3 model, providing accurate and relevant solutions.
- **User-Friendly Interface**: Easy to use with a clean and intuitive interface.
- **Customizable**: Change the appearance with custom CSS.
- **Interactive Sidebar**: Provides detailed instructions and information about the app.

## Installation

To get started with AutoBuddy, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/malaika-farooq/AutoBuddy.git
    cd autobuddy
    ```

2. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Add your Together API key**:
    - Create a file named `secrets.toml` in the `.streamlit` directory:
      ```bash
      mkdir -p .streamlit
      touch .streamlit/secrets.toml
      ```
    - Add your API key to the `secrets.toml` file:
      ```toml
      [secrets]
      TOGETHER_API_KEY = "your_api_key_here"
      ```

## Usage

1. **Run the Streamlit app**:
    ```bash
    streamlit run streamlit_app.py
    ```

2. **Using AutoBuddy**:
    - **Enter Your Vehicle Information**:
      - Provide the vehicle company, model, and year.
      - Describe the issue or fault you are experiencing with your vehicle.
    - **Submit the Information**:
      - Use the input field at the bottom of the page to enter the required details.
    - **Get a Response**:
      - AutoBuddy will process your input and generate a detailed response with possible causes and solutions for the issue.
    - **Review and Take Action**:
      - Read the response provided by AutoBuddy and follow the suggested steps to address the vehicle issue.
      - If necessary, consult with a professional mechanic for further assistance.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*Note: Replace `https://github.com/malaika-farooq/AutoBuddy.git` with your actual GitHub repository URL and `"your_api_key_here"` with your actual Together API key.*

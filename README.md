# BlogWriter: Your AI-Powered Blog Creation Assistant

BlogWriter is a powerful and user-friendly application that leverages OpenAI's GPT-4 and DALL-E models to help you generate high-quality, engaging blog content and visually appealing images. Customize your preferences, and let BlogWriter create the perfect blog tailored to your needs.

## Features

### 1. **AI-Powered Blog Generation**
   - Generates well-structured, engaging, and SEO-friendly blogs using OpenAI's GPT-4.
   - Incorporates custom titles, keywords, and desired word counts.
   - Highlights headings and integrates keywords seamlessly.

### 2. **High-Quality Image Generation**
   - Creates visually appealing images using OpenAI's DALL-E 3 model.
   - Customizes images to match your blog title and theme.
   - Supports up to 5 image generations per blog.

### 3. **User-Friendly Interface**
   - Clean and responsive layout.
   - Sidebar for easy customization of blog preferences.
   - Real-time feedback for generating content and images.

## How to Use

### Prerequisites
- Install Python 3.10.
- Set up a virtual environment and install the required libraries using `pip install -r requirements.txt`.
- Obtain an OpenAI API key and store it in a file named `apikey.py` in the format:
  ```python
  OPENAI_API_KEY = "your_openai_api_key_here"
  ```

### Steps to Run the application
1. Clone the repository. Keep `main.py` and `apikey.py` in same folder
2. Install the dependencies:
  ```python
  pip install -r requirements.txt
  ```
3. Run the application:
  ```python
  streamlit run main.py
  ```

### Generating a Blog
1. **Enter Your Preferences:**
   - **Blog Title:** Provide a title for your blog.
   - **Keywords:** Enter keywords separated by commas to guide the content generation.
   - **Number of Words:** Specify the desired word count for your blog (minimum 200, maximum 1000).
   - **Number of Images:** Select the number of images to generate (maximum of 5).

2. **Generate Your Blog:**
   - Click the **Get My Blog** button in the sidebar.

3. **View Results:**
   - The main page will display:
     - The generated blog content, which can be copied for further use.
     - The created images, which can be downloaded as needed.
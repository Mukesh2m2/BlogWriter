import streamlit as st
import openai
from apikey import OPENAI_API_KEY

# API Configuration
openai.api_key = OPENAI_API_KEY  

# Set Models
text_model = "gpt-4"
image_model = "dall-e-3"

st.set_page_config(layout='wide')

# Website Title and Description
st.markdown("<h1 style='text-align: center; font-size: 50px; color: #4CAF50;'>BlogWriter: Your AI-Powered Blog Creation Assistant</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; font-size: 20px; color: #666666;'>Generate high-quality, engaging blogs effortlessly with AI. Customize your preferences and let BlogWriter do the rest.</h5>", unsafe_allow_html=True)

# Sidebar for inputs
with st.sidebar:
    st.title("Blog Input Preferences")
    st.subheader("Enter preferences for the blog you want to create")

    blog_title = st.text_input("Blog Title", help="Enter a title for your blog post.")
    keywords = st.text_input("Keywords (comma-separated)", help="Enter keywords relevant to your blog.")
    num_words = st.slider("Number of words", min_value=200, max_value=1000, step=100, value=500)
    num_images = st.slider("Number of images", min_value=0, max_value=5, step=1, value=1)
    submit_button = st.button("Get My Blog")

# Blog and Image Generation
if submit_button:
    
    st.markdown('---')  # Separator
    
    # Section for Generated Images
    if num_images > 0:
        st.markdown("### Your Blog Images")
        images = []
        
        # Generate high-quality images using DALL-E 3
        for i in range(num_images):
            with st.spinner(f"Generating image {i+1}..."):
                image_prompt = f"Create a high-quality and creative image for a blog post titled '{blog_title}' that would appeal to an audience interested in {keywords}."
        
                try:
                    image_response = openai.Image.create(
                        model=image_model, 
                        prompt=image_prompt,
                        size="1024x1024",  
                        n=1  
                    )
                    images.append(image_response['data'][0]['url'])
                
                except Exception as e:
                    st.error(f"Error generating image {i+1}: {e}")
        
        # Display images
        if images:
            cols = st.columns(min(3, len(images))) 
            for idx, img_url in enumerate(images):
                cols[idx % len(cols)].image(img_url, caption=f"Generated Image {idx+1}", use_container_width=True)
    
    st.markdown('---')  # Separator

    # Section for Generated Blog Post
    st.markdown("### Your Blog Post")
    if blog_title.strip() == "" or keywords.strip() == "":
        st.error("Please provide a blog title and keywords.")
    else:
        with st.spinner("Generating blog content..."):
            blog_prompt = f"""
            Generate a comprehensive and engaging blog post relevant to the title '{blog_title}' and keywords like {keywords}. 
            Make sure to incorporate these keywords in the blog post. The blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout. Highlight Headings and keywords. 
            """
            
            try:
                blog_response = openai.ChatCompletion.create(
                    model=text_model,
                    messages=[
                        {"role": "system", "content": "You are a creative assistant for blog writing."},
                        {"role": "user", "content": blog_prompt}
                    ]
                )
                blog_content = blog_response['choices'][0]['message']['content'].strip()
                st.success("Blog content generated successfully!")
                st.markdown(blog_content)
                
            except Exception as e:
                st.error(f"Error generating blog content: {e}")




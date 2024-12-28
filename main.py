import streamlit as st

# Streamlit page configuration with a custom icon
st.set_page_config(
    page_title="GLXIW theritikbarnwal",
    page_icon="icon.png",  # Path to your custom icon
    layout="centered"
)

# Custom CSS to set background color and hover effects
st.markdown("""
    <style>
        .stApp {
            background-color: #eeeeee;
        }
        .links a {
            text-decoration: none;
            color: #4C585B;
            margin: 0 10px;
            font-size: 1.1rem;
            transition: transform 0.3s ease, color 0.3s ease;
        }
        .links a:hover {
            color: #FFA500; /* Change color to orange on hover */
            transform: translateY(-5px); /* Move the link up slightly on hover */
        }
        .box {
            transition: transform 0.3s ease, box-shadow 0.3s ease; /* Add transition for smooth effect */
        }
        .box:hover {
            transform: scale(1.05); /* Slightly expand the box on hover */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Add a subtle shadow on hover */
        }
    </style>
""", unsafe_allow_html=True)

# Function to create a styled box with links
def render_box(content, subtext, links):
    st.markdown(f"""
        <style>
            .box-container {{
                display: flex;
                justify-content: center;
                align-items: center;
                height: 85vh; /* Adjust to prevent scrolling */
                padding: 10px; /* Add padding for better responsiveness */
            }}
            .box {{
                padding: 30px;
                background-color: #E0E0E0;
                border-radius: 10px;
                border: 1px solid #696969;
                color: #4C585B;
                max-width: 90%; /* Use percentage for better responsiveness */
                text-align: center;
                transition: transform 0.3s ease, box-shadow 0.3s ease; /* Add transition for smooth effect */
            }}
            .box:hover {{
                transform: scale(1.05); /* Slightly expand the box on hover */
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Add a subtle shadow on hover */
            }}
            .links {{
                margin-top: 15px;
            }}
            .links a {{
                text-decoration: none;
                color: #4C585B;
                margin: 0 10px;
                font-size: 1.1rem;
                transition: transform 0.3s ease, color 0.3s ease;
            }}
            .links a:hover {{
                color: #FFA500; /* Change color to orange on hover */
                transform: translateY(-5px); /* Move the link up slightly on hover */
            }}
        </style>
        <div class="box-container">
            <div class="box">
                {content}
                <p>{subtext}</p>
                <div class="links">
                    {"".join([f'<a href="{url}" target="_blank">{name}</a>' for name, url in links.items()])}
                    
        </div>
        
    """, unsafe_allow_html=True)

# Define links
social_links = {
    "GitHub": "https://github.com/theritikbarnwal",
    "LinkedIn": "https://linkedin.com/in/theritikbarnwal",
    "X": "https://twitter.com/theritikbarnwal",
    "Instagram": "https://instagram.com/theritikbarnwal",
    "Web": "https://theritikbarnwal.streamlit.app/"
}

# Render the main box with links
render_box("Where Concepts Come to Life.", "Explore more.", social_links)

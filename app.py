import streamlit as st
from g1 import generate_response
import json

def main():
    st.set_page_config(page_title="Chanakya", page_icon="🧠", layout="wide")
    
    st.title("Chanakya: A WAY TO SOLVE!!")
    
    st.markdown("""
                
"When it comes to solving equations, humans reign supreme. But are you absolutely certain? Allow us to introduce you to Chanakya — where wisdom meets innovation!"

                """)
    
    st.markdown("Made with ❤ in india !!")
    # Text input for user query
    user_query = st.text_input("Enter your query:", placeholder="e.g: (a+b) ² =a²+2ab+b² ")
    
    if user_query:
        st.write("Generating response...")
        
        # Create empty elements to hold the generated text and total time
        response_container = st.empty()
        time_container = st.empty()
        
        # Generate and display the response
        for steps, total_thinking_time in generate_response(user_query):
            with response_container.container():
                for i, (title, content, thinking_time) in enumerate(steps):
                    # Ensure content is a string
                    if not isinstance(content, str):
                        content = json.dumps(content)
                    if title.startswith("Final Answer"):
                        st.markdown(f"### {title}")
                        if '```' in content:
                            parts = content.split('```')
                            for index, part in enumerate(parts):
                                if index % 2 == 0:
                                    st.markdown(part)
                                else:
                                    if '\n' in part:
                                        lang_line, code = part.split('\n', 1)
                                        lang = lang_line.strip()
                                    else:
                                        lang = ''
                                        code = part
                                    st.code(part, language=lang)
                        else:
                            st.markdown(content.replace('\n', '<br>'), unsafe_allow_html=True)
                    else:
                        with st.expander(title, expanded=True):
                            st.markdown(content.replace('\n', '<br>'), unsafe_allow_html=True)
            
            # Only show total time when it's available at the end
            if total_thinking_time is not None:
                time_container.markdown(f"**Total thinking time: {total_thinking_time:.2f} seconds**")

if __name__ == "__main__":
    main()

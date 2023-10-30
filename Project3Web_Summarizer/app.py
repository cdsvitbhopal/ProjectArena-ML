import streamlit as st
from langchain import OpenAI
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from bs4 import BeautifulSoup
import requests







def generate_response(txt):
    # Instantiate the LLM model
    response = requests.get(txt)
    if response.status_code == 200:
     webpage_content = response.content
    else:
     return "Failed to retrieve the webpage."
    soup = BeautifulSoup(webpage_content, 'html.parser')
    all_p_tags = soup.find_all('p')
    # Find all <span> tags
    all_span_tags = soup.find_all('span')
    text=""
    for p_tag in all_p_tags:
     text+=p_tag.text
    llm = OpenAI(temperature=0, openai_api_key=openai_api_key, model_name="gpt-3.5-turbo-16k")
    # Split text
    text_splitter = CharacterTextSplitter()
    texts = text_splitter.split_text(text)
    # Create multiple documents
    docs = [Document(page_content=t) for t in texts]
    # Text summarization
    chain = load_summarize_chain(llm, chain_type='stuff')
    return chain.run(docs)

# Page title
st.set_page_config(page_title='🌐 Web Summarizer')
st.title('🌐 Web Summarizer')

st.markdown("""
**Web Summarizer**

The Web Summarizer is a convenient tool for quick access to concise, user-friendly summaries of informative articles (like Wikis). 
It streamlines information retrieval by providing a condensed version of extensive articles, making research and knowledge acquisition more efficient and accessible. Perfect for on-the-go learning and fact-checking.

""")

# Text input
txt_input = st.text_input('Enter your URL', '')

# Form to accept user's text input for summarization
result = []
with st.form('summarize_form', clear_on_submit=True):
    openai_api_key = st.text_input('Enter your own OpenAI API Key', type = 'password', disabled=not txt_input)
    submitted = st.form_submit_button('Submit')
    if submitted and openai_api_key.startswith('sk-'):
        with st.spinner('Calculating...'):
            response = generate_response(txt_input)
            result.append(response)
            del openai_api_key

if len(result):
    st.info(response)
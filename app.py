from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
from groq import Groq
from langchain import PromptTemplate
# from langchain import LLMChain, OpenAI
import os
import requests
import streamlit as st

load_dotenv(find_dotenv())

# img2txt
from dotenv import find_dotenv, load_dotenv
from transformers import pipeline

load_dotenv(find_dotenv())
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# img2text function
def img2text(url):
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    text = image_to_text(url)
    # print(text)
    return text

# llm
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

def generate_story_llama(scenario, model="llama3-70b-8192", max_tokens=1024, temperature=1, top_p=1):
    template = """
    You are a storyteller;
    You can generate a short story based on a simple narrative. The story should be no more than 50 words;

    CONTEXT: {scenario}
    STORY:
    """
    prompt_template = PromptTemplate(template=template, input_variables=['scenario'])
    prompt = prompt_template.format(scenario=scenario)

    completion = client.chat.completions.create(
      model=model,
      messages=[
          {
              "role": "user",
              "content": prompt
          }
      ],
      temperature=temperature,
      max_tokens=max_tokens,
      top_p=top_p,
      stream=False,
      stop=None,
  )
    return completion.choices[0].message.content


# tts
def text2speech(message):
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    # API_URL = "https://api-inference.huggingface.co/models/microsoft/speecht5_tts"
    headers = {"Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"}
    payloads = ({
        "inputs": message,
    })

    response = requests.post(API_URL, headers=headers, json=payloads)
    with open('audio.flac', 'wb') as file:
        file.write(response.content)

# Main function
def main():
    st.set_page_config(page_title="Img 2 audio story", page_icon="🤖")
    st.header("Transform Images into Engaging Audio Stories by Danial Namazifard")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "bmp", "webp"])
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
        
        with open(uploaded_file.name, "wb") as file:
            file.write(uploaded_file.getvalue())
        
        scenario = img2text(uploaded_file.name)
        story = generate_story_llama(scenario)
        
        with st.expander("Scenario"):
            st.write(scenario)
        
        with st.expander("Story"):
            st.write(story)
        
        # Add your text-to-speech function here to generate audio file
        text2speech(story)
        
        # Assuming text2speech function saves the audio as 'audio.flac'
        st.audio("audio.flac")

if __name__ == "__main__":
    main()

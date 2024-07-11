# Image-to-Text and Text-to-Speech Mini Project

Transform your images into engaging audio stories using this Streamlit application. This project leverages open source machine learning models in Huggingface to generate text descriptions from images and then create short stories based on those descriptions. The final stories can be converted into audio files for an immersive storytelling experience.

## Streamlit App
You can check out the live Streamlit app [here](https://image2text2speech-hf-lms-ogfqtf3jrnthgqhruntbfc.streamlit.app/).

## Features

- **Image Upload**: Supports various image formats including JPG, JPEG, PNG, BMP, and WEBP.
- **Image-to-Text**: Utilizes a pre-trained image captioning model to generate textual descriptions of uploaded images.
- **Story Generation**: Uses a language model to create short stories based on the generated descriptions.
- **Audio Conversion**: Converts the generated stories into audio files using a text-to-speech model.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/namazifard/image2text2speech-HF-Llama3.git
   cd image2text2speech-HF-Llama3
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables by creating a `.env` file in the project root with your API tokens:

   ```env
   GROQ_API_KEY=your_groq_api_key_here
   HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token_here
   ```

## Usage

1. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Upload an image and watch as the application generates a story and converts it into an audio file.

## Dependencies

- `streamlit`: For creating the web interface.
- `transformers`: Provides the pre-trained image captioning and language models.
- `groq`: Used for interacting with the Groq API.
- `python-dotenv`: For loading environment variables.
- `requests`: For making API calls to Hugging Face.

## Models Used

- **Image-to-Text**: `Salesforce/blip-image-captioning-base`
- **Language Model**: `llama3-70b-8192`
- **Text-to-Speech**: `espnet/kan-bayashi_ljspeech_vits`

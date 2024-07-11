# Image-to-Text and Text-to-Speech Mini Project

Transform your images into engaging audio stories using this Streamlit application. This project leverages machine learning models to generate text descriptions from images and then create short stories based on those descriptions. The final stories can be converted into audio files for an immersive storytelling experience.

## Features

- **Image Upload**: Supports various image formats including JPG, JPEG, PNG, BMP, and WEBP.
- **Image-to-Text**: Utilizes a pre-trained image captioning model to generate textual descriptions of uploaded images.
- **Story Generation**: Uses a language model to create short stories based on the generated descriptions.
- **Audio Conversion**: Converts the generated stories into audio files.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/img2audiostory.git
   cd img2audiostory

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables by creating a `.env` file in the project root with your Groq API key:

   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Usage

1. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Upload an image and watch as the application generates a story and converts it into an audio file.

## File Structure

- `app.py`: The main Streamlit application.
- `requirements.txt`: Lists the dependencies required for the project.
- `.env`: Environment variables file (not included in the repository, must be created).
- `README.md`: Project documentation.

## Dependencies

- `streamlit`: For creating the web interface.
- `transformers`: Provides the pre-trained image captioning and language models.
- `groq`: Used for interacting with the Groq API.
- `python-dotenv`: For loading environment variables.

## Models Used

- **Image-to-Text**: `Salesforce/blip-image-captioning-base` from the Hugging Face Transformers library.
- **Language Model**: `llama3-70b-8192` for story generation.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue to discuss any changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [Hugging Face](https://huggingface.co/) for providing the pre-trained models.
- [Streamlit](https://streamlit.io/) for the easy-to-use web app framework.
- [Groq](https://www.groq.com/) for the API services.


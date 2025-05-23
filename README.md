﻿# text-translator
# English to Hindi Text Translator and Text to Speech Converter

## Description
This is a PyQt5 based GUI application that translates English text to Hindi, converts English text to speech, and saves the translated text as a PDF file. The application is user-friendly and efficient, providing an easy-to-use interface for all the functionalities.

## Features
- Translate English text to Hindi
- Convert English text to speech
- Save translated text as a PDF file

## Prerequisites
- Python ttx3 library
- PyQt5
- gTTS (Google Text-to-Speech)
- googletrans (Google Translate API)
- fpdf (Python PDF library)

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/english-to-hindi-translator.git
    ```

2. Navigate to the project directory:
    ```bash
    cd english-to-hindi-translator
    ```

3. Install the required dependencies:
    ```bash
    pip install pyqt5 gtts googletrans==4.0.0-rc1 fpdf
    ```

## Usage
1. Run the application:
    ```bash
    python main.py
    ```

2. Use the GUI to:
    - Enter the English text you want to translate.
    - Click on "Translate" to get the Hindi translation.
    - Click on "Text to Speech" to hear the English text.
    - Click on "Save as PDF" to save the translated text as a PDF file.
    - Click on "Previous" to see previous translated text.
    - Click on "Next" to see next translated text.

## File Structure
- `main.py`: The main script to run the application.
- `translator.py`: The script containing the translation and text-to-speech logic.
- `gui.py`: The script containing the PyQt5 GUI logic.
- `README.md`: This file.

## Contributing
If you would like to contribute to this project, please create a fork of the repository, make your changes, and submit a pull request. We appreciate all contributions!

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

## Authors
- [Rakesh Soun](https://github.com/Rakesh60772)

## Acknowledgements
- The PyQt5 library for the GUI framework.
- Google Text-to-Speech (gTTS) for the TTS functionality.
- Google Translate API for the translation services.
- The fpdf library for PDF creation.


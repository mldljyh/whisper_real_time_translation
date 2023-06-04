# Real Time Faster-Whisper Transcription & Translation

![Demo gif](demo.gif)

This application is a real-time speech-to-text transcription tool that uses the Faster-Whisper model for transcription and the TranslatePy library for translation. The transcribed and translated content is shown in a semi-transparent pop-up window. The Faster-Whisper model enables efficient speech recognition even on devices with 6GB or less VRAM.

## Installation

To install the dependencies, simply run:

```
pip install -r requirements.txt
```

## Usage

Run the `translation_demo.py` script with the desired arguments to start the real-time transcription and translation. Example command and arguments can be found in the file.

Transcription text and translations will appear in a pop-up window as audio input is detected.

## Customization

The application allows a range of options for customizing the transcription process, including choosing the model, destination language, microphone options, and more. Check the arguments in `translation_demo.py` and modify them as necessary to meet your needs.

## TranscriptionWindow

The `TranscriptionWindow.py` script contains a `TranscriptionWindow` class, which is responsible for displaying the transcription and translation results in a Tkinter-based pop-up window. The `update_text` method of this class handles the translation and display of text in the window.

## Acknowledgements

This demo was created by modifying the [whisper_real_time](https://github.com/davabase/whisper_real_time) repository and uses the [Faster-Whisper](https://github.com/guillaumekln/faster-whisper) model and the [TranslatePy](https://github.com/Animenosekai/translate) library.

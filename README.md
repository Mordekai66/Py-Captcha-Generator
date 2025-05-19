# PyCaptchaGenerator

PyCaptchaGenerator is a Python application that generates both image and audio CAPTCHAs with a simple Tkinter GUI. It provides an effective solution for bot protection and user verification by creating customized CAPTCHA challenges.

## Features

- Generate image CAPTCHAs with customizable text
- Create audio CAPTCHAs by combining individual character sounds
- Simple GUI interface for easy interaction
- Support for random CAPTCHA text generation
- Save generated CAPTCHAs locally for later use

## How It Works

1. The user can either:
   - Enter a custom text string (letters and numbers), **OR**
   - Click "Generate Random" to use an auto-generated CAPTCHA string
2. The user selects whether they want an image or audio CAPTCHA
3. For audio CAPTCHAs:
   - The system takes each character from the input text
   - Combines the corresponding audio files from the Voices folder
   - Saves the final audio file (`captcha.wav`) in the application's working directory
4. For image CAPTCHAs:
   - Uses the `captcha` library to generate an image
   - Displays the image directly in the GUI
   - Saves the image file (`captcha.png`) in the application's working directory

**All generated files are saved in the same directory where the application is running.**

## Usage
1. Run `main.py` to launch the application

2. Choose your input method:
   - Type your custom text (letters/numbers), **or**
   - Click "Generate Random" for auto-generated text

3. Select output format:
   - Image CAPTCHA (visual), **or**
   - Audio CAPTCHA (sound)

4. Click "Generate Captcha" to:
   - Display the image CAPTCHA in the GUI, **and**
   - Create the audio CAPTCHA file

5. Generated files (`captcha.png` and `captcha.wav`) will be saved in:
   - The application's working directory (where you ran the program)

6. You can:
   - View the image directly in the app
   - Play the audio through your system
   - Find both files in your current directory for later use
  

## Future Plans
- Add support for multiple fonts in image CAPTCHAs

- Support additional languages beyond English for audio CAPTCHAs

- Add female voice support (currently only male voice is implemented)

## Requirements

- Python 3.x
- Required packages:
  - `captcha`
  - `tkinter`
  - `wave` (for audio processing)
  - `pyttsx3` (for text-to-speech conversion to generate audio files of letters and digits)

Install requirements with:
```bash
pip install captcha wave pyttsx3
```

## Repository Structure

```bash
PyCaptchaGenerator/
├── .gitignore
├── main.py              # Main application with GUI
├── voice_forge.py       # Audio file combiner utility
├── assets/
│   ├── captcha.png      # Sample generated image CAPTCHA
│   └── captcha.wav      # Sample generated audio CAPTCHA
├── core/
│   ├── audio_captcha.py # Handles audio CAPTCHA generation
│   └── image_captcha.py # Handles image CAPTCHA generation
├── utils/
│   └── random_captcha_text.py # Generates random CAPTCHA text
└── Voices/
    ├── Man/             # Male voice samples
    │   ├── 0.wav        # Number 0 pronunciation
    │   ├── 1.wav        # Number 1 pronunciation
    │   ├── ...
    │   └── z.wav        # Letter Z pronunciation
    └── Woman/           # Female voice samples (future support)
        ├── 0.wav
        ├── 1.wav
        ├── ...
        └── z.wav
```

## Contribution
Contributions are welcome! Please fork the repository and submit pull requests for any improvements or new features.

## License
 project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.

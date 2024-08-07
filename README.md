# Flappy Bird Game

## Description

Flappy Bird is a classic arcade game where the player controls a bird to navigate through pipes. This version of the game allows you to play using two different methods:
- **Spacebar**: Click the spacebar to make the bird jump.
- **Blink Detection**: Use computer vision to control the bird by blinking your eyes.

## Tech Stack

- **Pygame**: For game development and rendering.
- **OpenCV**: For computer vision to detect eye blinks.
- **Haarcascade**: For eye detection in the computer vision process.
- **Tkinter**: For the control panel.

## Features

- **Dual Control Modes**: Play using the spacebar or by blinking your eyes.
- **Real-time Blink Detection**: Control the bird with eye blinks using OpenCV and Haarcascade.
- **User-Friendly Control Panel**: Manage game settings through an intuitive Tkinter interface.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/ChaitanayaK/Flappy-Bird.git
    cd Flappy-Bird
    ```

2. Install the required dependencies:
    To set up a virtual environment and install the required dependencies from a `requirements.txt` file, follow these steps:

      1. **Create a virtual environment:**

         - **On Windows:**
           ```bash
           python -m venv venv
           ```

         - **On macOS/Linux:**
           ```bash
           python3 -m venv venv
           ```

         This will create a virtual environment in a directory named `venv`.

      2. **Activate the virtual environment:**

         - **On Windows:**
           ```bash
           venv\Scripts\activate
           ```

         - **On macOS/Linux:**
           ```bash
           source venv/bin/activate
           ```

         After activation, your command prompt should show `(venv)` indicating that the virtual environment is active.

      3. **Install the required packages from `requirements.txt`:**
         ```bash
         pip install -r requirements.txt
         ```

      These steps will set up the virtual environment and install all the necessary dependencies for Flappy-Bird.

## Usage

1. **Run the Game**:
    ```bash
    python main.py
    ```

2. **Control Methods**:
    - **Spacebar**: Press the spacebar to make the bird jump.
    - **Blink Detection**: Ensure your webcam is active, and the blink detection mode will be enabled automatically.

3. **Control Panel**: Use the Tkinter-based control panel to adjust game settings and switch control modes.

## Screenshots

1. ![Main Menu](assets/main-page.png)
2. ![Game Main Page](assets/game-main.png)
3. ![In Game Page](assets/in-game.png)
4. ![Game Over Page](assets/game-over.png)

## Video Demo

Watch the demo of the game here: [Flappy Bird Demo](assets/video_demo.mp4)

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the creators of Pygame, OpenCV, and Haarcascades for providing the tools used in this project.
- Special thanks to the open-source community for the inspiration and support.

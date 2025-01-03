# HandyControl

A Python-based project that utilizes MediaPipe's hand tracking capabilities for various interactive applications. This repository includes:

-   **Hand Detection:** Implements real-time hand detection using MediaPipe's Hands solution.
-   **Volume Control:** Controls system volume by tracking the distance between thumb and index finger.
-   **Virtual Mouse:** Emulates mouse movement and clicking by tracking finger positions within a designated region.

## Features

-   Real-time hand detection with MediaPipe
-   Interactive volume control using hand gestures
-   Virtual mouse functionality for hands-free interaction
-   Customizable settings for detection and tracking parameters
-   Clear and concise code structure with comments

## Installation

1.  Clone this repository:

    ```bash
    git clone https://github.com/mrunknown101331/HandyControl.git
    ```

2.  Install required dependencies:

    ```bash
    pip install opencv-python mediapipe numpy pynput screeninfo pycaw comtypes
    ```

    *Note:* `comtypes` and `pycaw` are required for volume control on Windows.

## Usage

1.  Run the script:

    ```bash
    python main.py
    ```

    -   For volume control, adjust the detection region and distance threshold in `main.py`.
    -   For virtual mouse, customize the region size and smoothing factor in `main.py`.


## Contributing

We welcome contributions to this project! Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or fix.
3.  Implement your changes and add relevant unit tests (if applicable).
4.  Submit a pull request for review.

## Troubleshooting

-   **Volume Control Issues (Windows):** Ensure you have the necessary audio drivers and permissions. Sometimes running your IDE or terminal as administrator can resolve permission issues.
-   **Performance Issues:** If you experience low frame rates, try reducing the resolution of your camera input or adjusting the `track_conf` parameter in the `HandDetector` class.

## Acknowledgements

This project utilizes the following libraries:

-   [OpenCV](https://opencv.org/)
-   [MediaPipe](https://google.github.io/mediapipe/)
-   [NumPy](https://numpy.org/)
-   [pynput](https://pynput.readthedocs.io/en/latest/)
-   [screeninfo](https://pypi.org/project/screeninfo/)
-   [pycaw](https://github.com/AndreMiras/pycaw)
-   [comtypes](https://pythonhosted.org/comtypes/)

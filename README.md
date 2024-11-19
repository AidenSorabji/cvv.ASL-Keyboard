# cvv.ASL-Keyboard
<a href="https://github.com/AidenSorabji/cvv.ASL-Keyboard" title="Go to GitHub repo"><img src="https://img.shields.io/static/v1?label=AidenSorabji&message=cvv.ASL-Keyboard&color=blue&logo=github" alt="AidenSorabji - cvv.ASL-Keyboard"></a>
<a href="https://python.org" title="Go to Python homepage"><img src="https://img.shields.io/badge/Python-%3E=3.12.4-blue?logo=python&logoColor=white" alt="Made with Python"></a>
<a href="https://www.apple.com/macos/" title="Go to Apple homepage"><img src="https://img.shields.io/badge/OS-macOS-blue?logo=apple&logoColor=white" alt="OS - macOS"></a>
<a href="#license"><img src="https://img.shields.io/badge/License-MIT-blue" alt="License"></a>
<img alt="GitHub followers" src="https://img.shields.io/github/followers/aidensorabji">
<img alt="GitHub followers" src="https://img.shields.io/github/watchers/aidensorabji/cvv.ASL-Keyboard">

Utilizing machine learning within python to convert ASL hand movements into simulated keyboard presses within macOS.

Big thanks to [AkramOM606](https://github.com/AkramOM606) for the bases of this repo, check out his repository on ASL-detection [Here](https://github.com/AkramOM606/American-Sign-Language-Detection/tree/main).

> [!CAUTION]
> Do not use this project nor upload it without crediting me along with [AkramOM606](https://github.com/AkramOM606).

## Table of Contents
1. [Table of Contents](#table-of-contents)
2. [Contributions](#Contributions)
3. [Articles + Image References](#articles--image-references)

      a.  [Articles](#articles) 

      b.  [Joint Tracking Guide](#joint-tracking-guide)

      c.  [ASL Sign Guide](#asl-sign-guide)
4. [Modules](#modules)
5. [Controls](#controls)

      a.  [Left Hand](#left-hand)

      b.  [Right Hand](#right-hand)
6. [Installation](#installation)
7. [Copyright](#copyright)

## Contributions
- [Aiden Sorabji](https://github.com/aidensorabji)
- [AkramOM606](https://github.com/AkramOM606) ([American-Sign-Language-Detection](https://github.com/AkramOM606/American-Sign-Language-Detection/tree/main))

## Articles + Image References
### Articles
- [How to build a Python-based hand tracking application! A beginners Guide](https://medium.com/@luca733/python-based-hand-tracking-application-c3bab8481146)
- [Mediapipe: Fingers counting in Python w/o GPU](https://medium.com/analytics-vidhya/mediapipe-fingers-counting-in-python-w-o-gpu-f9494439090c)
- [pynput Keyboard Bindings](https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key)

### Joint Tracking Guide
<p align="left">
   <a href="https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker" target="_blank"></a>
   <img src="https://raw.githubusercontent.com/AidenSorabji/cvv.ASL-Keyboard/refs/heads/main/images/joint-reference.webp" width="40%">
</p>

I found this really useful starting out with hand and finger detection when determining initially where each joint is by using this image. It helped me  without using an intelligent model classify different hand gestures formed by either the left or right hand. I did this basically by finding out each joints (x,y) coordinates in relation to the width and height of the webcam display area. By finding out where each of the joints are, I could use < or > signs in relation to other joints to semi-create my own gestures. 

> [!NOTE]  
> For this specific project, a negated using this guide as I used a trained model from [AkramOM606](https://github.com/AkramOM606) to detect ASL inputs.

### ASL Sign Guide
<p align="left">
   <a href="https://twitter.com/afcs_seaf/status/1441115154247155712" target="_blank"></a>
   <img src="https://github.com/AidenSorabji/cvv.ASL-Keyboard/blob/main/images/asl-reference.jpg?raw=true" width="40%">
</p>

Pretty helpful reference of ASL signs within the ASL alphabet.

## Modules
- [OpenCV](https://pypi.org/project/opencv-python/)
- [mediapipe](https://github.com/google/mediapipe)
- [TenserFlow](https://www.tensorflow.org)
- [Pillow](https://python-pillow.org)
- [Numpy](https://numpy.org)
- [Pandas](https://pandas.pydata.org)
- [Seaborn](https://seaborn.pydata.org)
- [Scikit-learn](https://scikit-learn.org/stable/)
- [Matplotlib](https://matplotlib.org)
- [pynput](https://pynput.readthedocs.io/en/latest/)

## Controls
### Left Hand
| Control              | Sign |
| :---------------- | :------: |
| Delete        |   H/C   |
| Space           |   L   |
| Exclamation Mark    |  W   |
| Question Mark |  X   |
| Period |  v/u   |

### Right Hand
Use the [ASL Sign Guide](#asl-sign-guide).

## Installation
> [!NOTE]  
> It's recommended to use a virtual environment (```.venv```) when running this repo to minimize module clashing errors. It is also recommended to use a IDE with git support (ex. VSCode)
1. Clone the repository
```
git clone https://github.com/aidensorabji/cvv.Keyboard
cd cvv.Keyboard
```
2. Insure that you have the dependencies installed. If not, run the following command
```
pip install -r requirements.text
```
3. Run main python file
```
python main.py
```
> [!IMPORTANT]
> If you get an error stating: ```Module not found - "No module named"```, try creating a virtual environment (preferably a ```.venv```), then installing the dependencies and re-running ```main.py```. 

## Copyright 
MIT License 

Copyright (c) 2024 Aiden Sorabji

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

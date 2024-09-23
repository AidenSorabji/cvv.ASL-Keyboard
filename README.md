# cvv.ASLkeyboard
Using python modules to convert ASL hand movements into simulated keyboard presses within macOS.

Big thanks to [AkramOM606](https://github.com/AkramOM606) for the bases of this repo, check out his repository on ASL-detection [Here](https://github.com/AkramOM606/American-Sign-Language-Detection/tree/main).

> [!CAUTION]
> Do not use this project nor upload it without crediting me along with [AkramOM606](https://github.com/AkramOM606).
>
> Also this project isn't completely working right now, the vision is but not the keyboard inputs. Please do not follow installation process as of right now.

## Table of Contents
1. [Table of Contents](#table-of-contents)
2. [Contributions](#Contributions)
3. [Articles + Image References](#articles--image-references)

      a. [Articles](#articles) 

      b. [Joint Tracking Guide](#joint-tracking-guide)

      c. [ASL Sign Guide](#asl-sign-guide)
4. [Modules](#modules)
5. [Installation](#installation)
6. [Copyright](#copyright)

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
   <img src="https://raw.githubusercontent.com/AidenSorabji/cvv.Keyboard/refs/heads/main/images/joint-reference.webp" width="40%">
</p>

I found this really useful starting out with hand and finger detection when determining initially where each joint is by using this image. It helped me  without using an intelligent model classify different hand gestures formed by either the left or right hand. I did this basically by finding out each joints (x,y) coordinates in relation to the width and height of the webcam display area. By finding out where each of the joints are, I could use < or > signs in relation to other joints to semi-create my own gestures. 

> [!NOTE]  
> For this specific project, a negated using this guide as I used a trained model from [AkramOM606](https://github.com/AkramOM606) to detect ASL inputs.

### ASL Sign Guide
<p align="left">
   <img src="https://github.com/AidenSorabji/cvv.Keyboard/blob/main/images/asl-reference.jpg?raw=true" width="40%">
</p>

Pretty helpful reference of ASL signs of the alphabet.

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

## Installation
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

> [!NOTE]  
> It's recommended to use a virtual environment (```.venv```) when running this repo to minimize module clashing errors.

## Copyright 
MIT License

Copyright (c) 2024 Aiden Sorabji

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
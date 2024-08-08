# Gaming Website Automation Project

## Overview

This project is designed to automate the management of a gaming website, focusing on price extraction, profit application/removal, and game categorization. By leveraging tools like OCR for text extraction and various automation libraries, this project streamlines the process of managing game pricing and categories.

### Key Features

- **Automatic Price Extraction**: Utilize OCR technology to extract game prices directly from screenshots.
- **Dynamic Discounting**: Automatically apply and remove discounts based on predefined rules.
- **Game Categorization**: Easily manage and categorize games based on their prices and other criteria.
- **Screenshot Capture**: Capture screenshots of the gaming website for further processing and analysis.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- Required Python packages (listed in `requirements.txt`)

### Installation Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/gaming-website-automation.git
   cd gaming-website-automation
2. Install the required Python packages:

  ```bash
  pip install -r requirements.txt
  ```

3. Set up Tesseract OCR by specifying the path in the code (if not already configured):

  ```python
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
  ```
### Usage
Running the Project
To start the automation:

```bash
python App.py
```
### Features

#### 1. Dynamic Discount Calculation

The `discounter(price)` function automatically calculates discounts based on item prices. It applies different discount rates depending on predefined thresholds, ensuring that the correct discount is always applied.

```python
def discounter(price):
    # Discount logic based on price thresholds
```
#### 2. Screenshot Capture
Capture screenshots of the gaming website for processing using the capture_screenshot() function. This feature leverages the mss library and Pillow to handle screen captures efficiently.
```python
def capture_screenshot():
    # Code to capture screenshots
```
#### 3. Image Recognition and Scrolling
The ScrollPointFind(img, top, left, width, height, confidence, scr) function scrolls through a webpage to find a specific image within a designated region. If the image is not found initially, the function scrolls and retries until it is located.
```python
def ScrollPointFind(img, top, left, width, height, confidence, scr):
    # Logic to find an image within specific coordinates and scroll if necessary
```
#### 4. Image Finding and Centering
The ImgFind(img, center=False) function identifies the coordinates of an image on the screen. It can also return the center of the image if needed, using the PyAutoGUI library.
```python
def ImgFind(img, center=False):
    # Logic to find an image on the screen
```
#### 5. Open All Game Links
The FullOpenAllGames(steamdbcheck=False, variablecheck=False) function opens all game links provided in a file. It includes optional checks for SteamDB and other variables to ensure that the correct pages are accessed.
```python
def FullOpenAllGames(steamdbcheck=False, variablecheck=False):
    # Logic to open all game links
```
#### 6. Open a Single Game Link
The FullOpenSingleGames(steamdbcheck=False, variablecheck=False, GameName="") function is designed to open a single game's link. It also includes options for performing checks before opening the link.
```python
def FullOpenSingleGames(steamdbcheck=False, variablecheck=False, GameName=""):
    # Logic to open a single game link
```
#### 7. Open Game Links with Database Checks
Finally, the OpenList(steamdbcheck=False, variablecheck=False, GameName="", db=False) function provides a comprehensive approach to opening game links, including the ability to check against a database.
```python
def OpenList(steamdbcheck=False, variablecheck=False, GameName="", db=False):
    # Logic to open game links with additional checks
```


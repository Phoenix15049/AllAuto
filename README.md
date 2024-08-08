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

# Sobel-Filter_Edge-Detection

Sobel Filter Application is the application which takes an image that is uploaded from the computer, applies the sobel filter to that image, and gives a Sobel Image of that uploaded image.

Sobel Filter is used in image processing and computer vision, particularly within edge detection algorithms where it creates an image emphasising edges.

Sobel Image is the resulting grayscale Image with the detected edges in the original image.

## Table of content
1. [Built With](#bw)
2. [Getting Started](#gs)
3. [Unit Tests](#ut)
4. [File Structure](#fs)


## <a name="bw">Built With</a>
    - Python-Flask
    - HTML
    - CSS

## <a name="gs">Getting Started</a>
To run this application, you need to follow the following steps.\
First of all, you need to have python3 and pip installed. You can find python installation guide [here](https://www.python.org/downloads/) and pip installation guide [here](https://pip.pypa.io/en/stable/installation/). \
Once python and pip are installed, there are various python modules that are also required. \
Before we can install these modules, we need to create a virtual environment to run Flask. Follow the steps [here](https://flask.palletsprojects.com/en/2.0.x/installation/) to create a virtual environment in the application's working directory. <br>

Following is the step by step procedure. <br>

First of all, clone the repository. <br>
    ``` git clone https://github.com/surajgiri7/Sobel-Filter_Edge-Detection.git ```

Aftet that go (cd) to the project folder. <br>
    ``` cd Sobel-Filter_Edge-Detection ```

Install flask: <br>
    ```pip install flask```

Install Virtual Environment .\
    ```pip install virtualenv```

create the Virtual Environment .\
    ```virtualenv env```

### Start the virtual environment.
### for mac and linux
    
    source env/bin/activate

### for windows

    env\Scripts\activate 

Once the terminal with the virtual environment in the application's working directory is ready, enter the following commands to install the required packages.

    pip install -r requirements.txt


Once all the packages are installed, run the following command in the same command line

    export FLASK_APP=app.py
    flask run

Then, open http://127.0.0.1:5000/ in your web browser to view the application.

## <a name="ut">Unit Tests</a>
To Run Unit Tests:

    python3 test_app.py

## Dummy Data for checking the application:
The images included in the Images directory were used for testing the application and also can be used for the application.

## <a name="fs">File Structure</a>
	\Sobel-Filter_Edge-Detection 	# github's branch
    |
    |---\requirements.txt #all the requirements for this project
    |
    |---\README.md # Readme (a guide to the application) describing and instructing how to navigate and run the application in your local device.
    |
    |---\.gitignore # File that contains all the files and folders to be ignored during git push.
    |
    |---\app.py # Includes all the routes and the logic requireed for Sobel Image Processing.
    |
    |---\static
    |	| 
    |   |---\style.css # CSS file for all the CSS needed in this project.
	|---\templates
    |   |
    |   |--- \base.html # Base template that would be applied in all other pages.
    |   |
    |   |--- \index.html # Main homepage of the application.
    |   |
    |   |--- \upload.html # Page for uploading and showing results.
    |   |
    |---\images
    |   |
    |   |--- # All the images used for testing
    

# DSP_Task4
Systems and biomedical engineering, Cairo University.

3rd year, 1st semester.
### Course: Digital signal processing, Task 4

### Members
| Team Members' Names                                  | Section| B.N. |
|------------------------------------------------------|:------:|:----:|
| [Marina Nasser](https://github.com/MarinaNasser)     |    2   |  12  |
| [Yousef Adham ](https://github.com/joeadham)         |    2   |  55  |
|  [Michael Hany](https://github.com/michaelhany510)   |    2   |  14  |
| [Mayar Ehab  ](https://github.com/mayarehab)         |    2   |  41  |

# Image Merger Web Application

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)

This web application enables users to merge two images by extracting either the phase or magnitude from one picture and adding it to the phase or magnitude of the other. The application is built using JavaScript, CSS, Matplolib.byplot, Ajax, and Flask (Python) for the front-end and back-end, respectively.

## Key Features
- The ability to upload two pictures and select the magnitude or phase from each picture
- A square selector that allows users to choose a specific part of each picture to merge
- Real-time display of the output image while the user selects the merged part

## Installation
1. Clone the repository: `git clone https://github.com/<username>/<repository-name>.git`
2. Navigate to the project directory: `cd <repository-name>`
3. Create a virtual environment: `python -m venv env`
4. Activate the virtual environment: `source env/bin/activate`
5. Install the requirements: `pip install -r requirements.txt`

## Usage
1. Start the application: `python app.py`
2. Open your web browser and go to `http://localhost:5000`
3. Upload two images and select the magnitude or phase from each picture
4. Use the square selector to choose a specific part of each picture to merge
5. View the output image in real-time while selecting the merged part



## Screenshots

### Mixing the section with the most information in both phase and magnitude
![1](https://user-images.githubusercontent.com/81246343/235556303-cb2b9693-45da-4b30-9bef-44b9c9d87177.png)


### High pass filter
![2](https://user-images.githubusercontent.com/81246343/235556309-e9823712-ccce-4e0d-a3ad-1e5cff4e8926.png)

### Mixing 2 images
![3](https://user-images.githubusercontent.com/81246343/235556321-5cfe74ed-225d-43d9-a830-7bc236a3bcdb.png)

### Mixing 2 images
![4](https://user-images.githubusercontent.com/81246343/235556326-5148d8bc-0f73-4562-adbe-c9ad4e035b16.png)

## Technologies & Frameworks Used
- JavaScript
- CSS
- Matplolib.byplot
- Ajax
- Flask (Python)

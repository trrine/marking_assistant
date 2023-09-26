# Marking Assistant 📝

![image](https://github.com/trrine/marking_assistant/assets/41973043/e0df6aea-1534-47dd-a122-b6d36bb48133)

## Description

Marking Assistant is a practical tool developed to streamline the process of marking assignments and writing feedback for students. It simplifies the process of creating, managing, and marking assignments. With this app, you can:
- Define assignment tasks with total marks and grading criteria.
- Easily mark tasks by selecting met criteria.
- Automatically calculate student marks and generate feedback.
- Temporarily store results during your session.
- Export results to an Excel file.

As a tutor, I designed Marking Assistant to address the challenges I faced in marking assignments efficiently. It is a handy tool that automates certain tedious processes while keeping the human touch intact.

### Built With
- ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
- ![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)
- ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

## Getting Started

### Prerequisites
* [Python ≥ 3.9](https://www.python.org/downloads/)

### Installation 
1. Clone the repo if you have git.
```
git clone https://github.com/trrine/marking_assistant.git
```
Or press Code➝Download ZIP.

2. Navigate to the location of the requirements file on your system and install the requirements.
```
cd PATH_TO_PROJECT
pip install -r requirements.txt
```
3. Run the following commands to setup the database:
```
python manage.py makemigrations
python manage.py migrate
```

## Starting the App
1. Navigate to the project location.
```
cd PATH_TO_PROJECT
```
2. Start the server
```
python manage.py runserver
```
3. Open your browser and go to:
[http://127.0.0.1:8000](http://127.0.0.1:8000)

## TO DO:
- Write more unit and integration tests
- Add input validation
- Make design responsive

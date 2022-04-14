# Basler_image_capturer
Repository for a simple image gathering app that saves images captured by a Basler camera to folders and generates new folders with a keypress. Handy when capturing masses of images of similar objects. Much faster than using a graphical UI and constantly clicking File -> Save As ->

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

As the code is written in it, you should first install 
- [Python 3.X](https://www.python.org/downloads/). The version used in the development was 3.7.2.

The camera needs the SDK with API so that it can be controlled programmatically. Basler cameras use 
- [Pylon](https://www.baslerweb.com/en/sales-support/downloads/software-downloads/)

### Installing

It is recommed to use virtual environments with the Python projects. First, clone this repository. Then, create the virtual environment inside the project folder. A virtual environment is made like this with a Windows computer:

```
<path_to_python>\python.exe -m venv <name_of_the_environment>
```

The folder with the name <name_of_the_environment> appears. 

If you are using Visual Studio Code, it should detect the virtual environment when opening it inside the project folder. The virtual environment name should be seen in the lower left corner after the interpreter name, i.e. Python 3.7.0 64-bit ('virtual_env'). If it does not, it can be selected manually by cliking the interpreter name -> Enter interpreter path... and browsing to the _<name_of_the_environment>\Scripts\python.exe_ When the virtual environment is activated, its name is in bracket in the terminal before the path. Like this:

```
(virtal_env) C:\Users\<my_id>\<my_fancy_folder>\>
```

The virtual enviroment can be activated manually in Visual Studio Code by opening a new terminal window from the + symbol. Command prompt is recommended. PowerShell may have issues with rights.

Next, install the requirements with the command

```
pip install -r requirements.txt
```

Now, everything should be installed.

### Running the program

Connect the camera to the computer, check with Pylon Viewer that it works and you can connect to it, then (after shutting down Pylon Viewer) run the file **image_capturer.py**. It shows you preview image from the camera. The controls are the following:

**q** - shuts down the program and closes the preview window
**s** - saves the image by a name with a four-indexed number (0000.jpg, 0001.jpg, 0002.jpg, ...) into a given folder and subfolder (can be changed in the code)
**n** - creates a new subfolder with the name <subfolder_stem>## (e.g. part01, part02, part03...) by increasing the index by one
**c** - green crosshair that helps to find the image center on/off (does not show in the saved images)
**+/-** - increases/decreases the exposure time by 100 us

The created folder structure is as follows:

<pre>
├── main_folder
│   ├── <subfolder_stem>01
│   ├── 0000.jpg
│   ├── 0001.jpg
|   ├── 0002.jpg
|   |    ...
│   └── ####.jpg
|   |
│   ├── <subfolder_stem>02
│   ├── <subfolder_stem>03
|   |        ...
│   └── <subfolder_stem>##
</pre>

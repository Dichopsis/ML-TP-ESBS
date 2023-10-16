# Introduction to Machine-Learning Practical

# Goal of this practical

In this practical, I will try to show you how to create a machine-learning model to predict the diabetes risk of patients.  
We will perform data exploration, data processing, model training and evaluation, and finally fine-tuning.
Python is the go-to language for machine-learning and data-science. We will use Jupyter Notebooks through Google Colab to work on this practical. See the next section called _Getting Started_ to import the practical into Google Colab.

# Getting Started

For this practical, we will use Google Colab Notebooks. It is online Python notebooks that allow you to code and use python without installing anything on your side.
Because it is provided by Google, you will need a Google Account for this to work. If you don't want to use a Google service or you want to learn how you would use python in real life (at a job or insternship) please go to the #Advanced Setup section.

**Google Colab usage**

1. Go to: https://colab.research.google.com/
2. On the pop-up to select Notebook, select the Github Tab and enter this link: https://github.com/Dichopsis/ML-TD-ESBS-2 and select the notebook showing (TD2_Machine_Learning.ipynb).
3. You should be able to run the notebook and start writing code! Create a cell and run `print("Hello World")` to check if everything is good!

### **Congratulations** you should now be ready to code for the TD! You should read the second part at least for the informations that it contains ;)

</br>

# Advanced Setup

<details><summary>Click to open</summary>
<p>
This is the hard but worth-it way to install Python and all other stuff. It's worth to try as these are the tools you will use for  sure in any job or internship.
It makes everything run on your computer instead of relying on Google's one. I will briefly explain each tool to you and how to use them.

### The tools and how to install them

1. **Git**  
   To Install Git: [Git](https://git-scm.com/downloads) (should already be installed on all Linux)
   Git is command-line software used in informatics to do code versioning (tracking modifications and updates). In any informatics project you WILL be using it. In this TD we will only use Git to download the TD Code from a GitHub Repository using the command in a terminal:  
   `git clone https://github.com/Dichopsis/ML-TD-ESBS-2.git`.  
   For people that do not want to use Git and could not install it the code is also available as a .zip file [HERE](https://github.com/lambda-science/ML-TD-ESBS-2/archive/refs/heads/main.zip)

2. **Anaconda envrionnement**  
   Anaconda is a python distribution and package manager. It is the preferred way for data-scientist to install Python. We will use Anaconda to install our **python environment**. An environment is a python installation with a specific set of libraries installed. This way we can ensure that we all have the same package installed with the same version.  
   In any Python project, you WILL be using Anaconda environment (or at least Virtual Environement). It is crucial for reproducibility, sharing, and tracking.  
   **To install our environment**  
   If not already done, install Anaconda from: [Anaconda Download Page](https://www.anaconda.com/products/individual#Downloads)  
   After cloning the Git repository, you will find a file named `environment.yml` containing all informations for the Anaconda environment. You can now create the environment using:  
   `conda env create -f environment.yml`  
   Note: If an error occurs such as `conda is not a valid command` you might need to use the anaconda prompt software for the command. Also, environment are heavy (1.5-2gb here) and can take some time to install.  
   You can now activate your environment in your current terminal using:  
   `conda activate TD2_ML`. Your command-line should now look like `(TD2-ML) you@computername:~`  
   (For WINDOWS please use Anaconda Prompt terminal or run `C:\ProgramData\Anaconda3\Scripts\activate base` before `conda activate TD2_ML` if it doesn't work)

3. **Jupyter Notebooks**  
   Jupyter Notebook is the main tool of any data-scientist. It allows you to write and run python code dynamically without reloading all the code, data and variables everytime.  
   It is structured as blocks of code that you can run and edit independently. In this TD, our main worksheet will be the `TD2_Machine_Learning.ipynb` Jupyter Notebook.  
   You have several options to open Jupyter Notebooks.

### Using the Tools

- **The Easy way:** Activate you conda env if not already done. Then run:  
  `jupyter-notebook`  
  Your browser should automatically open a window on Jupyter or you can simply click the link. Please check if you can open the ipynb file and the folder.  
  Note: Don't close the terminal prompt as it would shutdown the Jupyter Server.
- **The 2nd Way:** Use [VSCode](https://code.visualstudio.com/)  
  Install the python extension. VSCode is able to natively open Jupyter Notebook with a great interface and without a server. Just select the right python environment and you're ready to go !

### **Congratulations** You should now be ready to code for the TD. Simply open the .ipynb file using jupyter-notebook or VSCode !

</p>
</details>

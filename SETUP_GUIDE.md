Project Setup Guide
===================

This guide provides step-by-step instructions for setting up the necessary tools and environments to work on this project. Follow these instructions based on your operating system.

* * * * *

Mac Setup
---------

### 1\. Install Xcode Command Line Tools

To develop on a Mac, install the Xcode Command Line Tools, a minimal version of Xcode with essential developer tools.

-   Open Terminal (in Utilities folder under Applications).

-   Run the following command to install:

    `xcode-select --install`

-   Follow the on-screen prompts to complete the installation.

### 2\. Install Python

Ensure you have Python installed by running this command in Terminal:

`python3 --version`

If it results in an error or shows an older version, install the latest Python using Homebrew.

-   If you don't have Homebrew, install it with this command:

    `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

-   Once Homebrew is installed, use it to install Python:

    `brew install python`

Confirm Python is installed by checking the version:

`python3 --version`

### 3\. Install Visual Studio Code

To edit and develop your scripts, Visual Studio Code is recommended.

-   Download Visual Studio Code from its [official website](https://code.visualstudio.com/).
-   Install it by following the instructions on the website.

* * * * *

Windows Setup
-------------

### 1\. Install Visual Studio Build Tools

To set up development tools on Windows, you need Visual Studio Build Tools.

-   Download the installer from the [official website](https://visualstudio.microsoft.com/visual-cpp-build-tools/).
-   Choose "Desktop development with C++" workload and follow the instructions to complete the installation.

### 2\. Install Python

Check if Python is installed by running this command in Command Prompt:

`python --version`

If there's an error or it's outdated, install the latest version of Python:

-   Download Python from its [official website](https://www.python.org/downloads/).
-   During installation, ensure "Add Python to PATH" is checked.

### 3\. Install Visual Studio Code

-   Download and install Visual Studio Code from its [official website](https://code.visualstudio.com/).

* * * * *

Install Git and Clone Repository
--------------------------------

### 1\. Install Git

Git is a version control system that allows you to manage code repositories. You need Git installed to pull and clone the repository.

-   Mac:

    -   If you installed Xcode Command Line Tools, you should already have Git installed.

    -   Confirm by running:

        `git --version`

-   Windows:

    -   Download and install Git from its [official website](https://git-scm.com/downloads).
    -   During installation, use the default options unless you have specific needs.

### 2\. Clone the Repository

To pull the repository, you need its GitHub URL. With Git installed, follow these steps:

-   Open Terminal (Mac) or Command Prompt (Windows).

-   Navigate to a directory where you want to clone the repository. For example, to navigate to the Desktop, use:

    `cd ~/Desktop`

-   Clone the repository using the URL (replace `REPO_URL` with the actual URL):
-   You will find the URL on the main Github page, copy it using the green 'Code' button. 

    `git clone REPO_URL`

### 3\. Navigate to the Repository Directory

After cloning, you need to enter the repository's directory to work on it.

-   If you cloned to the Desktop, navigate to the repository folder:

    `cd REPO_NAME`

Replace `REPO_NAME` with the name of the cloned repository. This should take you to the correct directory, where you can begin working on the project.

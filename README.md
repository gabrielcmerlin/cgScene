# Computer Graphics 3D scene

## Index

- [Computer Graphics 3D scene](#computer-graphics-3d-scene)
  - [Index](#index)
  - [Introduction](#introduction)
  - [How to run](#how-to-run)
    - [Prerequisites](#prerequisites)
      - [Miniconda](#miniconda)
      - [Libraries](#libraries)
      - [Graphic display](#graphic-display)
    - [Main code](#main-code)
  - [Files](#files)
  - [Objects](#objects)
  - [Transformations](#transformations)
  - [Conclusion](#conclusion)

## Introduction

This project was done as part of the Computer Graphics discipline taught in the second semester of 2024 by the professor Jean Roberto Ponciano. 

In this code, a 3D scene was implemented using some graphic tools, such as GLFW to manage windows and OpenGL to handle the graphic computing. Our main goal was to create a landscape using 5 composed objects (combination of primitives - pyramid, cube, sphere, etc) and to move some of them using the keyboard to add geometric transformations.

![GIF of the scene with some objects moving around]()

## How to run

### Prerequisites

Here is described what you must do to have everything needed to run this code.

#### Miniconda

The use of miniconda is recommended in order to prevent already installed packages from having conflicts with the ones we will install next.

1. Download Miniconda installer:

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

2. Run the installer:

```bash
bash Miniconda3-latest-Linux-x86_64.sh
```

3. Create a new environment:

```bash
conda create -n myenv python=3.9
```

4. Activate this environment:

```bash
conda activate myenv
```

#### Libraries

Within your Miniconda environment, install the packages used in the project.

1. Install NumPy:

```bash
pip install numpy==2.0.1
```

2. Install GLFW:

```bash
pip install glfw==2.7.0
```

3. Install OpenGL:

```bash
pip install pyopengl==3.1.7
```

#### Graphic display

One of the members of the duo had trouble running OpenGL on [Wayland](https://wiki.archlinux.org/title/Wayland) display server, but the same code worked just by switching the server to [Xorg](https://wiki.archlinux.org/title/Xorg). So, if this code doesn't work properly on your machine, try changing the display server to Xorg.

Below there is a photo of a Ubuntu 24.04 login screen while switching the display servers.

![Photo of Ubuntu 24.04 login screen while switching display servers](./attachments/xorg.jpg)

### Main code

## Files

## Objects

## Transformations

## Conclusion

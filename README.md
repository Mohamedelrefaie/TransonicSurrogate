# TransonicSurrogate
Surrogate Modeling of the Aerodynamic Performance for Transonic Regime

Our Paper: https://arc.aiaa.org/doi/abs/10.2514/6.2024-2220

Dataset available at: https://drive.google.com/drive/folders/1bBR2myjO1u1LDgk2miiC36WpdbGn4cvU?usp=drive_link

## Overview
This repository presents an in-depth exploration of machine learning models for surrogate modeling of airfoil aerodynamics in the transonic regime. Our project focuses on using ensemble learning methods and deep learning techniques to predict aerodynamic coefficients accurately.

## Models and Dataset
We utilize various models including Random Forest, Gradient Boosting, Support Vector Machines, and Neural Networks. The dataset comprises eight transonic airfoils (RAE2822,
RAE5212, NACA0012, NACA2412, NACA4412, NACA23012, NACA24112, and NACA25112), tested under a range of AoA and Mach numbers, resulting in 1,362 high-fidelity CFD simulations.
Solver: (rhoCentralFoam) Density-based compressible flow solver based on central-upwind schemes of Kurganov and Tadmor
+ 1,362 High-fidelity CFD simulations​
+ OpenFOAM®, rhoCentralFoam solver​
+ Unsteady compressible Euler equations​
+ 128 CPU cores with 4 Nvidia A100 GPUs​
+ 7 mins/simulation

  
## Results and Analysis
Our findings indicate that these models can predict aerodynamic coefficients with high accuracy, achieving an R2 of 99.6% for unseen conditions. Comparative analysis and performance metrics of each model are provided.

## Repository Structure
+ Data: Contains the dataset of airfoil characteristics and flow conditions.
+ Models: Python scripts and Jupyter notebooks for each ML model.
+ Results: Performance evaluations, plots, and comparative analyses.
+ Figures: Visual representations including scatter plots of predictions vs. actual values, feature importance graphs, and density estimations.

## Usage and Contribution
Instructions on how to use the scripts, train models, and analyze results are included. Contributions to enhance model performance or extend dataset are welcome.

## Collaborators and Acknowledgments
Special thanks to the research team from Texas A&M University for their invaluable input and guidance.

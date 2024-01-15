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

The contours demonstrate the efficient capture of the shockwave over the airfoil in our data generation results.

![image](https://github.com/Mohamedelrefaie/TransonicSurrogate/assets/99045424/515eb365-57e1-47c9-bcbb-991b6e106803)

Split the data into training (60%), test (20%), and validation sets (20%).

![image](https://github.com/Mohamedelrefaie/TransonicSurrogate/assets/99045424/affcd048-148e-4dcb-8056-7ee87d90bbbe)

Performance comparison of different models on 𝐶𝑙 

![image](https://github.com/Mohamedelrefaie/TransonicSurrogate/assets/99045424/48a8da11-e06d-4fa7-9afd-4fa5635156d8)

Performance comparison of different models on 𝐶𝑚 

![image](https://github.com/Mohamedelrefaie/TransonicSurrogate/assets/99045424/4b01816b-1d5f-44a6-98b1-3fae928f6d75)


## Repository Structure
+ Data: Contains the dataset of airfoil characteristics and flow conditions.
+ Models: Python scripts and Jupyter notebooks for each ML model.
+ Results: Performance evaluations, plots, and comparative analyses.
+ Figures: Visual representations including scatter plots of predictions vs. actual values, feature importance graphs, and density estimations.

## Usage and Contribution
Instructions on how to use the scripts, train models, and analyze results are included. Contributions to enhance model performance or extend the dataset are welcome.

## Collaborators and Acknowledgments
Special thanks to the research team from Texas A&M University for their invaluable input and guidance.

## Citation

```bibtex
@inbook{doi:10.2514/6.2024-2220,
  author = {Mohamed Elrefaie and Tarek Ayman and Mayar Elrefaie and Eman Sayed and Mahmoud Ayyad and Mohamed M. AbdelRahman},
  title = {Surrogate Modeling of the Aerodynamic Performance for Airfoils in Transonic Regime},
  booktitle = {AIAA SCITECH 2024 Forum},
  chapter = {},
  pages = {},
  doi = {10.2514/6.2024-2220},
  URL = {https://arc.aiaa.org/doi/abs/10.2514/6.2024-2220},
  eprint = {https://arc.aiaa.org/doi/pdf/10.2514/6.2024-2220},
  abstract = {Advancements in generative AI models have notably enhanced the automation of 3D shape generation, presenting transformative possibilities in the design of wings for aerospace applications. The optimization of such shapes relies on a large number of numerical simulations, which pose a computational challenge in the preliminary design stages. In this paper, we compare different machine learning models for surrogate modeling of the aerodynamic performance of airfoils for the transonic regime. We propose a new representation of the airfoils by combining geometric and aerodynamic features to comprehensively characterize the airfoil and its operating flight conditions. A training dataset that includes eight different transonic airfoils was generated, where we examined each airfoil under various operational flight conditions, encompassing a wide range of Angle of Attack (AoA) and freestream Mach numbers (\$M\_{\infty}\$). This resulted in a dataset comprising \$1,362\$ data points. The surrogate models employed in our study are primarily ensemble learning methods, including Random Forest, Gradient Boosting, and Support Vector Machines, complemented by deep learning techniques. We conduct a comparative analysis of these models to evaluate their efficacy in predicting aerodynamic coefficients. Our experiments show that different surrogate models can accurately and efficiently predict aerodynamic coefficients with an \$R^2\$ of \$99.6\\%\$ for unseen flight conditions. The dataset and code used in our study are accessible to the public at: [https://github.com/Mohamedelrefaie/TransonicSurrogate](https://github.com/Mohamedelrefaie/TransonicSurrogate)}

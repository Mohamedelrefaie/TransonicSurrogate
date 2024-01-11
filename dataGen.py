"""
@author: CFD-ML Team (last edit by Tarek Ayman)

This is a data generation code that uses OpenFOAM to solve the Unsteady, Compressible, inviscid NS equations
(Euler equations) for airfoils operating under Transonic conditions. This code iterates over a specified 
delivered blockMesh file for specified Airfoil.

"""

import os, math
import shutil, re
import numpy as np


global AoA,Vinf,height,Mach
angle_array        = np.arange(-math.pi / 90, math.pi / 12, math.pi/360)   # array of AoAs to iterate through
height_array       = np.arange(0, 15000 , 3000)   # array of height to iterate through
Mach_array         = np.arange(0.65, 1.2 , 0.05)  # array of Mach number to iterate through

angle_samples      = len(angle_array)             # no. of angle datasets to produce
height_samples     = len(height_array)            # no. of height datasets to produce
Mach_samples       = len(Mach_array)              # no. of height datasets to produce

# Define the path to train folder directory
output_directory   = "./train/"

# Define the path to OpenFOAM case directory (change it based on the current airfoil)
case_directory     = "./data_NACA0012/"

################################################ Functions ###################################################

def runSim(freestreamX, freestreamY, T, p, rho):
   
    with open("U_template", "rt") as inFile:
        with open("0/U", "wt") as outFile:
            for line in inFile:
                line = line.replace("VEL_X", "{}".format(freestreamX))
                line = line.replace("VEL_Y", "{}".format(freestreamY))
                outFile.write(line)
                
    with open("controlDict_template", "rt") as inFile:
        with open("system/controlDict", "wt") as outFile:
            for line in inFile:
                VEL_INF = math.sqrt(freestreamX**2 + freestreamY**2)
                line    = line.replace("VEL", "{}".format(VEL_INF))
                line    = line.replace("rho_h", "{}".format(rho))
                outFile.write(line)
                
    with open("T_template", "rt") as inFile:
        with open("0/T", "wt") as outFile:
            for line in inFile:
                line = line.replace("T_h", "{}".format(T))
                outFile.write(line)
                
    with open("p_template", "rt") as inFile:
        with open("0/p", "wt") as outFile:
            for line in inFile:
                line = line.replace("p_h", "{}".format(p))
                outFile.write(line)
                
                
    os.system("./Allclean && blockMesh && decomposePar && mpirun -np 10 rhoCentralFoam -parallel && reconstructPar && touch case.foam > foam.log")

def outputProcessing(freestreamX, freestreamY, dataDir=output_directory,ffile='OpenFOAM/postProcessing/forcesCoeffs/0/coefficient.dat'): 

    coefff = np.transpose(np.concatenate((np.array(np.loadtxt(ffile)), np.array([Vinf,height,Mach,AOA]))))
    coeff=np.reshape(coefff,(1,17))

    # check if the file exists
    file_exists = os.path.isfile('train/Data.csv')    
    with open('train/Data.csv', "a") as f:
        if not file_exists:
            # write the header if the file does not exist
            np.savetxt(f, [], fmt='%4.6f', delimiter=',',header="Time,Cd,Cs,Cl,CmRoll,CmPitch,CmYaw,Cd(f),Cd(r),Cs(f),Cs(r),Cl(f),Cl(r),V,h,Mach,AOA")
        np.savetxt(f, coeff, fmt='%4.6f', delimiter=',')
    print("\tsaving in Data.csv")

def get_airfoil_name(case_directory):
    
    match = re.search(r'data_(\w+)', case_directory)
    if match:
        return match.group(1)
    else:
        return 'unknown_airfoil'
   
       
def copy_openfoam_to_train_and_rename(case_directory, height, mach_number, angle_of_attack):
    
    # Get the current directory
    current_directory = os.getcwd()

    # Define the source folder path
    source_folder = os.path.join(current_directory, 'OpenFOAM')

    # Define the destination folder path (in the "train" directory)
    destination_folder = os.path.join(current_directory, 'train')

    # Create the "train" folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # Copy the "OpenFOAM" folder to the "train" folder
    destination_openfoam_folder = os.path.join(destination_folder, 'OpenFOAM')
    shutil.copytree(source_folder, destination_openfoam_folder)

    print(f'Folder copied to: {destination_openfoam_folder}')

    # Get the airfoil name from the case directory
    airfoil_name = get_airfoil_name(case_directory)

    # Define the new name for the "OpenFOAM" folder
    new_folder_name = f'{airfoil_name}_H{height}_M{mach_number}_AoA{angle_of_attack}'

    # Rename the "OpenFOAM" folder to the new name
    os.rename(destination_openfoam_folder, os.path.join(destination_folder, new_folder_name))

    print(f'Folder renamed to: {os.path.join(destination_folder, new_folder_name)}')

################################################ main #####################################################

#for i in range(height_samples):
    '''
    gamma  = 1.4
    R      = 286.9
    height = height_array[i]
    T      = 15.04-0.00649*height+273.1
    p      = 101290*((T/288.08)**5.256)
    rho    = p/(R*T)
    a      = math.sqrt(gamma*R*T)
    height = height_array[i]
    '''   
for i in range(Mach_samples):
   
    gamma  = 1.4
    R      = 286.9
    # These values are at sea level (h=0), after investigating we see that the
    # effect of the height is not significant when solving the inviscid case
    height = 0
    p = 101400.9309
    rho = 1.2266
    T = 288.14
    a = math.sqrt(gamma*R*T)
    Mach = Mach_array[i]
        
    for j in range(angle_samples):
       angle = angle_array[j]
       global AoA,Vinf
       print("Run {}:".format(j))
       print("\tusing NACA 0012 airfoil")

            
       length = Mach*a                   
  
       AoA  = angle                      # rad
       AOA  = (angle* 180) /math.pi      # degree
       Vinf = length                     # Freestream Velocity
       fsX  = math.cos(angle) * length   # Freestream Velocity X
       fsY  = math.sin(angle) * length   # Freestream Velocity Y

       print("\tUsing velocity %5.3f, height %5.3f, Mach %5.3f, angle %5.3f" %(length, height, Mach, AOA))
       print("\tResulting freestream vel x,y: {},{}".format(fsX,fsY))

       os.chdir("./OpenFOAM/")
       runSim(fsX, fsY, T, p, rho)
       os.chdir("..")

       outputProcessing(fsX, fsY)
       print("\tdone")
            
       # Copy "OpenFOAM" to the "train" folder and rename based on operating conditions
       copy_openfoam_to_train_and_rename(case_directory, height, Mach, AOA)

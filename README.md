# Forest and Land Fires Haze Trajectory Web Apps
![Screenshot from 2023-08-05 05-24-17 (1)](https://github.com/noval-di/app-haze/assets/78836819/3be20712-86c2-4e7d-a9d3-65e4a93607bd)
Forest and Land Fires Haze Trajectory Web Apps used to build simulations and display visualization of smoke haze trajectories due to forest and land fires. The simulation was built using the Pysplit module and the Hysplit Desktop Application, and using Folium as the visualization module.

## Environment Setup
1.	Hysplit Desktop application which can be accessed via https://www.ready.noaa.gov/HYSPLIT.php
2.	Folium library which can be accessed via https://python-visualization.github.io/folium/
3.	Python Packages:
    *	PySplit >= 0.3.5
    *	Numpy >= 1.6
    *	Matplotlib >= 1.2
    *	Basemap >= 1.0
    *	GeoPandas >= 0.1
    *	Cartopy >= 0.15
    *	django_tables2 >= 2.6.0

## Installation
1. Download all the packages and libraries needed.
2. Clone the repo
   ```python
   git clone https://github.com/noval-di/app-haze
   ```
3. Download and Install the Hysplit Desktop application because requires a local installation of HYSPLIT. The location of the `hyts_std` executable must be known.
   ![Screenshot from 2023-09-08 07-52-15](https://github.com/noval-di/app-haze/assets/78836819/a3b7dd60-b539-4ecf-9ea7-94985c27cc71)
4. In each developed simulation module requires three arguments indicate locations of the HYSPLIT working directory, the desired and existing trajectory storage directory, and the directory that contains the meteorology files.
   ![Screenshot from 2023-09-08 07-50-51](https://github.com/noval-di/app-haze/assets/78836819/d4929498-71f8-452e-9ba2-e0a88dfd1e6a)
5. The Pysplit package used has modifications made to obtain more specific output names. Modifications were made by adding the string coordinate attribute to the trajectory_generator.py file and then adding it to the trajname argument.
   ```sh
   str_coordinates=''.join(str(num).replace('.','').replace(',','')  for num in coordinates)
   
   trajname = (basename + m_str + '{:04}'.format(a) + season + fnameyr + "{0:02}{1:02}{2:02}".format(m, d, h) + str_coordinates)
   ```
   ![Screenshot from 2023-09-08 07-53-11](https://github.com/noval-di/app-haze/assets/78836819/c1eb26f8-8162-4753-8302-c83fb50639c6)
6. Forest and Land Fires Haze Trajectory Web Apps are ready to use.
   

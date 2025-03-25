# Metadata

Two types of metadata are provided in the dowloaded archive. 
The first type is metadata for the  rupture realizations and the second type is metadata for the ground motion histories. 
The metadata for the realizations is provided in a file titled ``Simulations_Flatfile.xlsx``, and includes three sets of information:
- A general description of the simulated earthquake including the region name, corresponding region code, and the realization number.
- Fault rupture parameters, including fault geometry characterized by the fault name; rupture geometry defined by fault length and width, depth to top of rupture, dip, strike, and rake; earthquake magnitude and hypocenter location; the rupture model utilized in the regional simulations (e.g., the *Graves-Pitarka* kinematic rupture model) and slip characteristics. 
A  graphic that displays the slip, slip-rate and rise time across the fault rupture is also provided to assist in interpretation.

- Simulation model parameters, which include maximum frequency resolved, minimum shear wave velocity included in the model (Vsmin), surface grid spacing that defines the distance between computational nodes in the simulation model, output spacing that provides distance between the down-sampled grid points where ground motion data is available, and the geologic velocity model utilized in the simulation (e.g., the USGS velocity model for SFBA).

For each region, the metadata for the ground motions of all realizations are provided in a separate file. 
The metadata includes two sets of information; the first set includes the *name*, *latitude* and *longitude* coordinates of the grid point, the vertical elevation of the grid point from sea level, the 2D cartesian coordinates of the grid point in the computational model domain (with X and Y axes in the fault normal and parallel directions respectively), the $V_{s30}$, and the depth at which the shear-wave velocity reaches $1.0 \mathrm{~km} / \mathrm{s}$ and $2.5 \mathrm{~km} / \mathrm{s}(\mathrm{Z} 1.0$ and Z $2.5$ at the location of the grid point. 
The second set consists of the distance parameters ( $R_{jb}$ , $R_{\mathrm{rup}}$ and $R_x$ ) and peak ground motion values (*RotD50*, *PGA*, *PGV*, and *PGD*). 
The file for the SFBA region is titled ``Hayward_M7_GMs_Flatfile.xlsx``.
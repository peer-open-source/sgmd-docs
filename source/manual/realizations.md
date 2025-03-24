# Realizations

After selecting the region, the next window allows the user to search for ground motions across multiple realizations and multiple parameters . Several points to consider when using the Search are listed below:

```{eval-rst}
.. figure:: figures/inputs.png
   :align: center
   :width: 50%

```

- Users can select any number of realizations of interest; at least one realization must be selected. 
  Each *realization* represents a unique earthquake, and it is recommended that users make themselves familiar with all the 50 realizations, details of which are provided in the file [`Simulations_Flatfile.xlsx`](Simulations_Flatfile.xlsx).

- All search parameters are initially deactivated. Users can activate the parameters of interest using the Switch buttons (Figures 3-6). 
  At least one parameter must be activated for the search, and users can utilize as many parameters as needed. For example:
  - Figure 3 shows a search for all ground motions in Realizations 1 and 2, and Realizations with patches 4 and 5 within a region defined by latitude boundaries of $37.68^{\circ}$ and $37.72^{\circ}$ and longitude boundaries of $-122.30^{\circ}$ and $-121.90^{\circ}$.
  - Figure 4 shows a search for all ground motions in the same region, but only those with $\mathrm{V}_{\mathrm{s} 30}$ between $300 \mathrm{~m} / \mathrm{s}$ and $500 \mathrm{~m} / \mathrm{s}$.
  - Figure 5 shows a search for all ground motions in the same region but only those with $\mathrm{V}_{\mathrm{s} 30}$ between $300 \mathrm{~m} / \mathrm{s}$ and $500 \mathrm{~m} / \mathrm{s}$, and $\mathrm{R}_{\mathrm{jb}}$ between 10 km and 20 km .
  - Figure 6 shows a search for all ground motions with PGV between $0.8 \mathrm{~m} / \mathrm{s}$ and $1.0 \mathrm{~m} / \mathrm{s}$ in Realizations 1-10, and Realizations with Patches 1-10.

- If a user wants to search for a specific location, such as the site of a building or a bridge, they should set the maximum latitude equal to the minimum latitude and the maximum longitude equal to the minimum longitude. 
  This search finds ground motions at the locations closest to the specified coordinates. 
  The distances between the specified location and the locations of the identified motions are provided in a summary file titled *"Distance Results."*
- Search parameters are described in {ref}`parameters`.


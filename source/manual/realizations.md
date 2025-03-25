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
  At least one parameter must be activated for the search, and users can utilize as many parameters as needed.

- If a user wants to search for a specific location, such as the site of a building or a bridge, they should set the maximum latitude equal to the minimum latitude and the maximum longitude equal to the minimum longitude. 
  This search finds ground motions at the locations closest to the specified coordinates. 
  The distances between the specified location and the locations of the identified motions are provided in a summary file titled *"Distance Results."*
- Search parameters are described in {ref}`parameters`.


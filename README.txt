John M Gregoire 26 Jan 2014

All code written by John Gregoire.

for analyzing UVvis data (especially transmission) combined with echem experiments
example course of action for taking raw data to visualizer .pck's:
1. setup AM1.5 spectrum in am15 folder and GenAM15.py
2. setup analysis routines in pck_opt_withechem_FCN.py
3. setup calls to those functions in batchrun_opt_eche.py
4. combine the different optical and echem results using combine_opt_eche_pcks.py

# Quantum Gravity in 1d
################Explanation to go here###############
## Run instructions
To run this code first we will need to set up a new virtual environment. You will need python3.8 or later, pip and the virtual environment package (venv).
To create the virtual environment run 

` python3 -m venv {ENV NAME}`

To activate this run the command `source {ENV NAME}/bin/activate` you should now be in the python virtual environment. 
Now you can install all the requirements using the command 

`pip install requirements.txt`

you should now have all the requirements to run this code. From the command line now run the bash script `run_dirac_1d.sh` using `bash run_dirac_1d.sh` or make it executable via `chmod u+x run_dirac_1d.sh`.
After the code has ran a .gif file should appear with a gif of the evolution over time of the probability distribution. 

- To look at the wave function change the `PLOT_WF` variable in `dirac_1d.py` from False to True.
- To examine the system in a situation where mass varies in space change the `VAR_MASS` variable from False to True

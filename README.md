HieraGen is still under development. Future releases and bug fixes are likely so please check out repository regularly.

We are currently working on cleaning up the code and aggregating setting flags to make the code more user friendly. 

A detailed descritpion of the HieraGen algorithm is provided here: http://homepages.inf.ed.ac.uk/vnagaraj/papers/isca20.pdf
A detailed descritpion of the ProtoGen algorithm is provided here: http://homepages.inf.ed.ac.uk/vnagaraj/papers/isca18a.pdf

If you have questions, you want to contribute or simply report any bugs, please contact: hiera.gen at ed.ac.uk


Please edit Murphi path in /Murphi/MurphiTemp/tmpmakefile

Requirements:
Python 3.5 or higher
Packages: antlr-python3-runtime 3.4; colorama 0.3.9; tabulate 0.8.2

To run the HieraGen (hierachical protocols) testbench encompassing a set of different protocol combinations execute:
python3 HieraGenTestBench.py

To run the ProtoGen (flat protocols) testbench encompassing a set of different protocols execute:
python3 ProtoGen.py



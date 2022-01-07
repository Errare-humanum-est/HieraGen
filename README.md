# HieraGen

HieraGen is still under development. Future releases and bug fixes are likely so please check out repository regularly. 

Update: [HeteroGen](https://github.com/Errare-humanum-est/HeteroGen) has been released. While HeteroGen and HieraGen are currently orthogonal in functionality they will soon be merged into a new release.
  
A detailed descritpion of the HieraGen (ISCA'20) algorithm is provided here: [HieraGen ISCA'20](https://github.com/Errare-humanum-est/HieraGen/blob/ea8e95fe8d50eed9e49118ac1d402da54767d696/ISCA_HieraGen.pdf)

A detailed descritpion of the ProtoGen (ISCA'18) algorithm is provided here: [ProtoGen ISCA'18](https://github.com/Errare-humanum-est/ProtoGen/blob/e11c9b88f626dd03c5fa5d6fc947db32d25d5ea9/ISCA_ProtoGen.pdf)



If you have questions, you want to contribute or simply report any bugs, please contact: hiera.gen at ed.ac.uk

## Setup
Please edit Murphi path in: **/Murphi/MurphiTemp/tmpmakefile**  

Requirements:  
Python 3.5 or higher  
  - antlr-python3-runtime 3.4
  - colorama 0.3.9
  - tabulate 0.8.2

To run the HieraGen (hierachical protocols) testbench encompassing a set of different protocol combinations execute:  
```
python3 HieraGenTestBench.py
```

To run the ProtoGen (flat protocols) testbench encompassing a set of different protocols execute:  
```
python3 ProtoGen.py
```



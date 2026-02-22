 grid nlrflap.cgd
 solution nlrflap.cfl
 units fss
 zone 1
 subset  j 1 1 k all i 29 177 
 zone 2
 subset  j 1 1 k all i 21 159 
 variables x; Cp scale -1
 genplot output cp.gen
 plot data cp.gen
 quit

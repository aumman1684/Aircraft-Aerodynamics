 grid nlrflap.cgd
 solution nlrflap.cfl
 units fss
 zone 1
 surface  j 1 1 k all i 29 177 
 zone 2
 surface  j 1 1 k all i 21 159 
 integrate force output forces.lis iviscous -
     reference length 1.0 -
     reference area 1.0 -
     reference moment 0.25 0.0 0.0
 quit

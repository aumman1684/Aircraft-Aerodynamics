 grid nlrflap.cgd
 solution nlrflap.cfl
 units fss
 zone 1
 subset i 165 j 1 last k 1 1
 variables ds; x; y; z; u; v; T
 genplot output bl.gen
 quit

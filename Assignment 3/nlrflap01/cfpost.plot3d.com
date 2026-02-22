 grid nlrflap.cgd
 solution nlrflap.cfl
 units fss
 zone 1
 zone 2
 subset i all j all k all
 plot3d x nlrflap_blank.x q nlrflap.q unformatted blank
 quit

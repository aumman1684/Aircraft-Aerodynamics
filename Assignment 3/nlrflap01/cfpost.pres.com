 grid n3d.cgd
 solution n3d.cfl
 units fss
 subset i all j all k all
 zone 1
 zone 2
 variables p
 cut at z 1.5
 genplot surface output pres.m overwrite
 plot color contours edge data pres.m
 quit

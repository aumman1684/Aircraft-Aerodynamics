 grid n3d.cgd
 solution n3d.cfl
 units fss
 subset i all j all k all
 zone 1
 zone 2
 variables M
 cut at z 1.5
 genplot surface output mach.m overwrite
 contour increment 0.05
 plot color contours edge data mach.m
 quit

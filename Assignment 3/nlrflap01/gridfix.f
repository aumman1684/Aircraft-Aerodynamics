      program gridfix

      parameter ( nim=205, njm=59, nkm=1, nbm=2 )

      dimension x(nim,njm,nkm,nbm)
      dimension y(nim,njm,nkm,nbm)
      dimension z(nim,njm,nkm,nbm)

      dimension ni(nbm), nj(nbm), nk(nbm)

      open ( unit=7, file='nlrflap_orig.x', form='unformatted' )
      
      read (7) nb
      read (7) ( ni(m), nj(m), nk(m), m = 1, nb )
      do  m = 1, nb
        read (7) ((( x(i,j,k,m), i=1,ni(m)), j=1,nj(m)), k=1,nk(m)),
     &           ((( y(i,j,k,m), i=1,ni(m)), j=1,nj(m)), k=1,nk(m)),
     &           ((( z(i,j,k,m), i=1,ni(m)), j=1,nj(m)), k=1,nk(m))
      enddo

      xte = x(29,1,1,1)

c...Scale all grid points so that xte = 1.0.  Also set z=1.0.

      fac = 1.0 / xte 

      do  m = 1, nb
        do  i = 1, ni(m)
          do  j = 1, nj(m)
            do  k = 1, nk(m)
              x(i,j,k,m) = x(i,j,k,m) * fac
              y(i,j,k,m) = y(i,j,k,m) * fac
              z(i,j,k,m) = 1.0
            enddo
          enddo
        enddo
      enddo

c...Write out the new grid.

      open ( unit=8, file='nlrflap.x', form='unformatted' )
      
      write (8) nb
      write (8) ( ni(m), nj(m), nk(m), m = 1, nb )
      do  m = 1, nb
        write(8) ((( x(i,j,k,m), i=1,ni(m)), j=1,nj(m)), k=1,nk(m)),
     &           ((( y(i,j,k,m), i=1,ni(m)), j=1,nj(m)), k=1,nk(m)),
     &           ((( z(i,j,k,m), i=1,ni(m)), j=1,nj(m)), k=1,nk(m))
      enddo

      stop
      end


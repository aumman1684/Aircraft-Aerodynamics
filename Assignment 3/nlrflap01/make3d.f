      program make3d

      parameter ( nim=205, njm=59, nkm=2, nbm=2 )

      dimension x(nim,njm,nkm,nbm)
      dimension y(nim,njm,nkm,nbm)
      dimension z(nim,njm,nkm,nbm)
      dimension ib(nim,njm,nkm,nbm)
      dimension q(nim,njm,nkm,nbm,5)

      dimension ni(nbm), nj(nbm), nk(nbm)

      open ( unit=7, file='nlrflap_blank.x', form='unformatted' )
      
      read (7) nb
      read (7) ( ni(m), nj(m), nk(m), m = 1, nb )
      do  m = 1, nb
        read (7) ((( x(i,j,k,m), i=1,ni(m)), j=1,nj(m)), k=1,nk(m)),
     &           ((( y(i,j,k,m), i=1,ni(m)), j=1,nj(m)), k=1,nk(m)),
     &           ((( z(i,j,k,m), i=1,ni(m)), j=1,nj(m)), k=1,nk(m)),
     &           ((( ib(i,j,k,m), i=1,ni(m)), j=1,nj(m)), k=1,nk(m))
      enddo

      open ( unit=8, file='nlrflap.q', form='unformatted' )
      
      read (8) nb
      read (8) ( ni(m), nj(m), nk(m), m = 1, nb )
      do  m = 1, nb
        read (8) t1, t2, t3, t4
        read (8)((((q(i,j,k,m,n),i=1,ni(m)),j=1,nj(m)),k=1,nk(m)),n=1,5)
      enddo

c...Copy to m=2.

      do  m = 1, nb
        do  i = 1, ni(m)
          do  j = 1, nj(m)
            x(i,j,2,m) = x(i,j,1,m)
            y(i,j,2,m) = y(i,j,1,m)
            z(i,j,2,m) = 2.0
           ib(i,j,2,m) = ib(i,j,1,m)
            do  n = 1, 5
              q(i,j,2,m,n) = q(i,j,1,m,n)
            enddo
          enddo
        enddo
      enddo
      
      nk(1) = 2
      nk(2) = 2

c...Write out the new grid and solution.

      open ( unit=10, file='n3d.x', form='unformatted' )
      write (10) nb
      write (10) ( ni(m), nj(m), nk(m), m = 1, nb )
      do  m = 1, nb
        write(10) ((( x(i,j,k,m), i=1,ni(m)), j=1,nj(m)), k=1,nk(m)),
     &            ((( y(i,j,k,m), i=1,ni(m)), j=1,nj(m)), k=1,nk(m)),
     &            ((( z(i,j,k,m), i=1,ni(m)), j=1,nj(m)), k=1,nk(m)),
     &           ((( ib(i,j,k,m), i=1,ni(m)), j=1,nj(m)), k=1,nk(m))
      enddo

      open ( unit=11, file='n3d.q', form='unformatted' )
      
      write (11) nb
      write (11) ( ni(m), nj(m), nk(m), m = 1, nb )
      do  m = 1, nb
        write (11) t1, t2, t3, t4
        write (11) 
     &    ((((q(i,j,k,m,n),i=1,ni(m)),j=1,nj(m)),k=1,nk(m)),n=1,5)
      enddo

      stop
      end


program gauss
implicit none
real :: s1,s2,s3,s4,s5,mu1x,mu2x,mu3x,mu4x,mu5x,mu1y,mu2y,mu3y,mu4y,mu5y
real :: f1,f2,f3,f4,f5,x,y,a1,a2,a3,a4,a5
real*8 :: pi
integer :: i,j

open(100,file='data.csv')
pi=2.0d0*dasin(1.0d0)


s1=100.0
s2=s1
s3=s1
s4=s1
s5=s1

mu1x=150.0
mu1y=150.0
mu2x=150.0
mu2y=750.0
mu3x=350.0
mu3y=800.0
mu4x=500.0
mu4y=500.0
mu5x=850.0
mu5y=850.0

a1=1000.0
a2=a1
a3=a1
a4=a1
a5=a1
write(100,*)'x,','y,','f'
do i=0,100
 x=100.0+i*10.0
 do j=1,100
  y=100.0+j*10.
  f1=(a1/(sqrt(2.0d0*pi)*s1))*exp(-(0.5d0/(s1**2))*((x-mu1x)**2.0+(y-mu1y)**2.0))
  f2=(a2/(sqrt(2.0d0*pi)*s2))*exp(-(0.5d0/(s2**2))*((x-mu2x)**2.0+(y-mu2y)**2.0))
  f3=(a3/(sqrt(2.0d0*pi)*s3))*exp(-(0.5d0/(s3**2))*((x-mu3x)**2.0+(y-mu3y)**2.0))
  f4=(a4/(sqrt(2.0d0*pi)*s4))*exp(-(0.5d0/(s4**2))*((x-mu4x)**2.0+(y-mu4y)**2.0))
  f5=(a5/(sqrt(2.0d0*pi)*s5))*exp(-(0.5d0/(s5**2))*((x-mu5x)**2.0+(y-mu5y)**2.0))
  
  write(100,*) x,',',y,',',f1+f2+f3+f4+f5+0.0000001
  
 enddo
enddo


close(100)

write(*,*) 'programa finalizado'
pause

end program gauss
# In this program, I will display a triangli like this:
    #
   ###
  #####
 #######
#########

n=input('Enter the size of your triangle: ')
n=int(n)
star='*'
blank=' '
i=n     # compte the number of blanks
j=1     # compte the number of stars
k=0
while j != n+1:
    print((blank*i)+(star*j)+(star*k)+(blank*i))
    i=i-1
    j=j+1
    k=k+1

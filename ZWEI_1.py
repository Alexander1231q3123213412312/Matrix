from ZWEI import add,positive_elements,max_elements,modified_matrix,final_matrix
n=int(input("Enter the number list items: "))
a=[]
c=[]
g=[]

add(n,a,g)

T=positive_elements(n,a)

if(T>=0):
    print("column with not positive elements: ",T)
else:
    print("don't column with not positive elements: ")

c=max_elements(n,a,c)
print("Max element's:",c)

g=modified_matrix(n,g,c)

final_matrix(n,g,c)

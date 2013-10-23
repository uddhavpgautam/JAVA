txt=open("lol.txt","r")  #ucitava datoteku(ovdje treba ici stdin umjesto txt jel)
sve=txt.readlines()      #ucitavam retke
n=len(sve)
sve1=[]
praznine=[]
konacna=[]

i=0  
while i<n:
 sve[i]=sve[i].split(" ")         #razdvajam rijeci po retcima
 i=i+1

i=0
while i<n:
    j=0
    m=len(sve[i])
    while j<m:
        if j>0:
            sve[i][j]=list(sve[i][j])  
            
            sve[i][j].insert(0," ")           #umetanje praznina
        j=j+1
    i=i+1

i=0
n=len(sve)
while i<n:
    j=0
    m=len(sve[i])
    while j<m:
        sve1.append(list(sve[i][j]))    #nova lista, razdvajanje slova u rijecima
        j=j+1
    i=i+1

n=len(sve1)
i=0
while i<n:
 konacna=konacna+sve1[i]            #konacna lista,svako slovo je poseban element
 i=i+1

print konacna
from flask import Flask , render_template , request,url_for
n=Flask(__name__)

@n.route('/')

def age():

    return render_template('index.html')
@n.route('/',methods=['POST'])
def age1():

    na=request.form['name']

    da1=request.form['dob']

    da2=request.form['cur']

    gen=request.form['gg']

    d=len(da1)

    dd=len(da2)


    gh=d-1

    hg=dd-1

    l1=[]

    l2=[]


    da11=''

    da22=''

    for i in range(d):

        if da1[i]!='-':

            da11=da11+da1[i]

        else:

            l1.append(da11)
            da11=''

        if gh==i:

            l1.append(da11)    

    for i in range(dd):

        if da2[i]!='-':

            da22=da22+da2[i]

        else:

            l2.append(da22)
            da22=''

        if gh==i:

            l2.append(da22)   
    l1.reverse()

    l2.reverse()         
    
    dayf1=int(l1[0])

    dayf2=int(l1[1])

    dayf3=int(l1[2])

    dayc1=int(l2[0])

    dayc2=int(l2[1])

    dayc3=int(l2[2])

    day=0
    month=0
    year=0

    for i in range(dayf1,dayc1+1):

        day=day+1
    for i in range(dayf2,dayc2):

        month=month+1
    for i in range(dayf3,dayc3):

        year=year+1
    if dayf2==12:

        

        year=year-1

        while month!=dayc2:

            month=month+1  
    
    if dayf1>dayc1:


        while dayf1!=dayc1:

              day=day+1 
              dayf1=dayf1+1

              if dayf1==30:

                  dayf1=0   
    if dayf2>dayc2 and dayf2!=12:

        year=year-1


        while dayf2!=dayc2:

            month=month+1

            dayf2=dayf2+1

            if dayf2==12:

                dayf2=0   
    if dayf3==dayc3:

        year=0                      



    

         










    return render_template('agedis.html',date1=day,month1=month,year1=year,gender1=gen,n=na,dof=da1)

if __name__== '__main__':

    n.run(debug=True)

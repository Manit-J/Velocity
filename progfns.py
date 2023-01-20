#PROGRAM FUNCTIONS
from texttable import Texttable #MODULE TO MAKE TABLES

#CONNECTION WITH SQL 
import mysql.connector
mydb=mysql.connector.connect(host='localhost', user='root', passwd='root' )
mycursor=mydb.cursor()

mycursor.execute("use velocity")
mycursor.execute("SET SESSION group_concat_max_len = 8192")

def maketable(record):
    table =Texttable(90) 
    table.add_rows(record)
    return table.draw()

def truncate(value):
    uvalue=""
    for i in value:
        for j in value:
            if j=="(" or j==")" or j==",":
                pass
            else:
                uvalue=uvalue+str(j)
    return uvalue



def itenary():
    sno=0
    cost=0
    while True:
        cost=0
        sno=sno+1
        people=int(input("Enter the number of people:"))
        doa=input("enter date of arrival of destination:")
        #CITY CHOICE
        print("Choose city:")
        mycursor.execute("select city,vcost_per_day from cities ")
        cities=mycursor.fetchall()
        print(maketable([["city" , "vcost_per_day"]]+cities))
        city=input("enter city which you want to visit:")
        d=[city]
        mycursor.execute("select vcost_per_day from cities where city=%s" , d)
        vcost_per_day=mycursor.fetchone()
        cost=cost+int(truncate(vcost_per_day))*people

        #SIGHTS CHOICE 
        print("Choose sights to visit:")
        mycursor.execute("select sight from sights s where s.city_id=(select city_id from cities where city=%s)" , d)
        sights=mycursor.fetchall()
        print(maketable([["sights"]] + sights))
        sights=list(input("enter sights with comma between them :") . split(","))
        #DAYS 
        days=int(input("enter the number of days you want to spend in this city, keeping in mind the number of sights chosen :"))
        #HOTELS CHOICE
        print("Choose your Hotel:")
        mycursor.execute("select hotel from hotels where city_id=(select city_id from cities where city=%s)" , d) 
        hotels=mycursor.fetchall()
        print(maketable([["hotels"]] + hotels))
        hotel=input("enter the hotel where you wish to stay:")
        h=[hotel]
        mycursor.execute("select stay_cost from hotels where hotel=%s" , h)
        stay_cost=mycursor.fetchone()
        cost=cost+int(truncate(stay_cost))*people

        cost=cost*days
        #TRANSPORT CHOICE
        mycursor.execute("select ptickets, ttickets from tcost where city_id=(select city_id from cities where city=%s)" , d)
        transport=mycursor.fetchall()
        print(maketable([["plane tickets cost" , "train tickets cost"]] + transport))
        modetransport=input("How would you like to travel ? Plane>1 Train>2 : ")
        for i in sights:
            if modetransport=="1":
                mycursor.execute("select ptickets from tcost where city_id=(select city_id from cities where city=%s)" , d)
                ptickets=mycursor.fetchone()
                cost=cost+int(truncate(ptickets))*people
                data=[sno, doa, days,city, i, hotel, "plane" , cost]
                mycursor.execute("insert into itenary values (%s , %s, %s, %s , %s, %s, %s,%s)" , data)
                mydb.commit()
            elif modetransport=="2":
                mycursor.execute("select ttickets from tcost where city_id=(select city_id from cities where city=%s)" , d)
                ttickets=mycursor.fetchone()
                cost=cost+int(truncate(ttickets))*people
                data=[sno, doa, days,city, i, hotel, "train" , cost]
                mycursor.execute("insert into itenary values (%s , %s, %s, %s , %s, %s, %s ,%s)" , data)
                mydb.commit()
        c=input("Do you wish to continue ? yes>y no>n :")
        if c=="y":
            continue
        else:
            mycursor.execute("select SNo, DOA, No_Of_Days, city, GROUP_CONCAT(sights SEPARATOR '\n' ) as 'Places Of Visit', place_of_stay, transport , max(cost)  from  itenary group by SNo")
            records=mycursor.fetchall()
            print(maketable([["SNo" , "DOA" , "Number Of Days" , "City" , "Places Of Visit" , "Place Of Stay" , "Mode Of Transport" , "Cost"]] + records))
            mycursor.execute("select sum(cost) from itenary")
            totalcost=mycursor.fetchone()
            totalcost=int(truncate(totalcost))
            print("The Total Approximate Cost for the trip is:" , totalcost)
            mycursor.execute("delete from itenary")
            mydb.commit()
            com=input("Do you wish to compare by making another itenary? yes>y no>n :")
            if com=="y":
                csno=0
                ccost=0
                while True:
                    ccost=0
                    csno=csno+1
                    cpeople=int(input("Enter the number of people:"))
                    cdoa=input("enter date of arrival of destination:")
                    #CITY CHOICE
                    print("Choose city:")
                    mycursor.execute("select city,vcost_per_day from cities ")
                    ccities=mycursor.fetchall()
                    print(maketable([["city" , "vcost_per_day"]]+ccities))
                    ccity=input("enter city which you want to visit:")
                    cd=[ccity]
                    mycursor.execute("select vcost_per_day from cities where city=%s" , cd)
                    cvcost_per_day=mycursor.fetchone()
                    ccost=ccost+int(truncate(cvcost_per_day))*cpeople

                    #SIGHTS CHOICE 
                    mycursor.execute("select sight from sights s where s.city_id=(select city_id from cities where city=%s)" , cd)
                    csights=mycursor.fetchall()
                    print(maketable([["sights"]] + csights))
                    csights=list(input("enter sights with comma between them :") . split(","))
                    #DAYS 
                    cdays=int(input("enter the number of days you want to spend in this city, keeping in mind the number of sights chosen:"))
                    #HOTELS CHOICE
                    mycursor.execute("select hotel from hotels where city_id=(select city_id from cities where city=%s)" , cd) 
                    chotels=mycursor.fetchall()
                    print(maketable([["hotels"]] + chotels))
                    chotel=input("enter the hotel where you wish to stay:")
                    ch=[chotel]
                    mycursor.execute("select stay_cost from hotels where hotel=%s" , ch)
                    cstay_cost=mycursor.fetchone()
                    ccost=ccost+int(truncate(cstay_cost))*cpeople

                    ccost=ccost*cdays
                    #TRANSPORT CHOICE
                    mycursor.execute("select ptickets, ttickets from tcost where city_id=(select city_id from cities where city=%s)" , cd)
                    ctransport=mycursor.fetchall()
                    print(maketable([["plane tickets cost" , "train tickets cost"]] + ctransport))
                    cmodetransport=input("How would you like to travel ? Plane>1 Train>2 : ")
                    for ci in csights:
                        if cmodetransport=="1":
                            mycursor.execute("select ptickets from tcost where city_id=(select city_id from cities where city=%s)" , cd)
                            cptickets=mycursor.fetchone()
                            ccost=ccost+int(truncate(cptickets))*cpeople
                            cdata=[csno, cdoa, cdays,ccity, ci, chotel, "plane" , ccost]
                            mycursor.execute("insert into citenary values (%s , %s, %s, %s , %s, %s, %s,%s)" , cdata)
                            mydb.commit()
                        elif modetransport=="2":
                            mycursor.execute("select ttickets from tcost where city_id=(select city_id from cities where city=%s)" , cd)
                            cttickets=mycursor.fetchone()
                            ccost=ccost+int(truncate(cttickets))*cpeople
                            cdata=[csno, cdoa, cdays,ccity, ci, chotel, "train" , ccost]
                            mycursor.execute("insert into citenary values (%s , %s, %s, %s , %s, %s, %s ,%s)" , cdata)
                            mydb.commit()
                    cc=input("Do you wish to continue ? yes>y no>n :")
                    if cc=="y":
                        continue
                    else:
                        mycursor.execute("select SNo, DOA, No_Of_Days, city, GROUP_CONCAT(sights SEPARATOR '\n' ) as 'Places Of Visit', place_of_stay, transport , max(cost)  from  citenary group by SNo")
                        crecords=mycursor.fetchall()
                        print(maketable([["SNo" , "DOA" , "Number Of Days" , "City" , "Places Of Visit" , "Place Of Stay" , "Mode Of Transport" , "Cost"]] + crecords))
                        mycursor.execute("select sum(cost) from citenary")
                        ctotalcost=mycursor.fetchone()
                        ctotalcost=int(truncate(ctotalcost))
                        mycursor.execute("delete from citenary")
                        mydb.commit()
                        print("The Total Approximate Cost for your trip is:" , ctotalcost)
                        if ctotalcost<totalcost:
                            print("Velocity recommends the new itenary as it is more economical.")
                            print("Thank You for using Velocity!")
                            exit()
                        elif ctotalcost>totalcost:
                            print("Velocity recommends the older itenary as it is more economical.")
                            print("Thank You for using Velocity!")
                            exit()
                        else:
                            print("The totalcost of your new itenary is same as that of old one. Hence, Velocity encourages you to choose the itenary which meets maximum number of your requirements and expectations.")
                            print("Thank You for using Velocity !")
                            exit()
            elif com=="n":
                print("Velocity recommends that you save your itenary.")
                print("Thank You for using Velocity!")
                exit()
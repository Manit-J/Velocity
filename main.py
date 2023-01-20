#MODULES IMPORTED
import progfns
import mysql.connector
mydb=mysql.connector.connect(host='localhost', user='root', passwd='root' )
mycursor=mydb.cursor()



#INTRODUCTION
print("Welcome To Velocity - An Itenary Making Software")
print("It's easy to work with. Just give us the data and we'll plan your perfect trip!")
print()
while True:
	print("If you are the manager who wants to make an itenary on behalf of someone, press 1")
	print("If you are the admin, press 2")
	a=input("enter your choice :")

	if a=="1":
		progfns.itenary()

	elif a=="2":
		#admin account
		passwd=input("enter password:")
		if passwd=="admin":
			print("welcome admin.")
			mycursor.execute("use velocity")
			while True:
				c=input("Menu: 1>add data 2>delete data 3>update data 4>search data :")
				if c=="1":
					print("choose table:")
					mycursor.execute("show tables")
					tables=mycursor.fetchall()
					print(progfns.maketable(tables))
					table=input("enter the table:")
					if table=="cities":
						mycursor.execute("select * from cities")
						rec=mycursor.fetchall()
						print(progfns.maketable(rec))
						city=input("enter city name you want to add:")
						city_id=input("enter city_id of the city:")
						vcost=int(input("enter visiting cost per day:"))
						d=[city, city_id, vcost]
						mycursor.execute("insert into cities values(%s,%s,%s)" , d)
						mydb.commit()
						print("row inserted.")

					elif table=="hotels":
						mycursor.execute("select * from hotels")
						rec=mycursor.fetchall()
						print(progfns.maketable(rec))
						city_id=input("enter city_id of the city:")
						hotel=input("enter hotel name:")
						stay_cost=int(input("enter visiting cost per day:"))
						hotel_id=input("enter hotel_id:")
						d=[city_id, hotel, stay_cost , hotel_id]
						mycursor.execute("insert into hotels values(%s,%s,%s,%s)" , d)
						mydb.commit()
						print("row inserted.")
					elif table=="sights":
						mycursor.execute("select * from sights")
						rec=mycursor.fetchall()
						print(progfns.maketable(rec))
						city_id=input("enter city_id of the city:")
						sight=input("enter sight:")
						sight_id=input("enter sight_id:")
						d=[city_id, sight, sight_id]
						mycursor.execute("insert into sights values(%s,%s,%s)" , d)
						mydb.commit()
						print("row inserted.")
					elif table=="tcost":
						mycursor.execute("select * from tcost")
						rec=mycursor.fetchall()
						print(progfns.maketable(rec))
						city_id=input("enter city_id of the city:")
						ptickets=int(input("enter price of plane tickets:"))
						ttickets=int(input("enter price of train tickets:"))
						d=[city_id, ptickets, ttickets]
						mycursor.execute("insert into tcost values(%s,%s,%s)" , d)
						mydb.commit()
						print("row inserted.")
				elif c=="2":
					print("choose table:")
					mycursor.execute("show tables")
					tables=mycursor.fetchall()
					print(progfns.maketable(tables))
					table=input("enter the table:")
					if table=="cities":
						mycursor.execute("select * from cities")
						rec=mycursor.fetchall()
						print(progfns.maketable(rec))
						city_id=input("enter city_id of the city:")
						d=[city_id]
						mycursor.execute("delete from cities where city_id=%s" , d)
						mydb.commit()
						print("row deleted.")

					elif table=="hotels":
						mycursor.execute("select * from hotels")
						rec=mycursor.fetchall()
						print(progfns.maketable(rec))
						hotel_id=input("enter hotel_id")
						d=[hotel_id]
						mycursor.execute("delete from hotels where hotel_id=%s" , d)
						mydb.commit()
						print("row deleted.")
					elif table=="sights":
						mycursor.execute("select * from sights")
						rec=mycursor.fetchall()
						print(progfns.maketable(rec))
						sight_id=input("enter sight_id:")
						d=[sight_id]
						mycursor.execute("delete from sights where sight_id=%s" , d)
						mydb.commit()
						print("row deleted.")
					elif table=="tcost":
						mycursor.execute("select * from tcost")
						rec=mycursor.fetchall()
						print(progfns.maketable(rec))
						city_id=input("enter city_id of the city:")
						d=[city_id]
						mycursor.execute("delete from tcost where city_id=%s" , d)
						mydb.commit()
						print("row deleted.")
				elif c=="3":
					print("choose table:")
					mycursor.execute("show tables")
					tables=mycursor.fetchall()
					print(progfns.maketable(tables))
					table=input("enter the table:")
					if table=="cities":
						mycursor.execute("select * from cities")
						rec=mycursor.fetchall()
						print(progfns.maketable(rec))
						ocity_id=input("enter the city_id of the row which you want to update:")
						city=input("enter new city name :")
						city_id=input("enter new city_id of the city:")
						vcost=int(input("enter new visiting cost per day:"))
						d=[city, city_id, vcost, ocity_id]
						mycursor.execute("update cities set city=%s,city_id=%s, vcost_per_day=%s where city_id=%s" , d)
						mydb.commit()
						print("row updated.")

					elif table=="hotels":
						mycursor.execute("select * from hotels")
						rec=mycursor.fetchall()
						print(progfns.maketable(rec))
						ohotel_id=input("enter the hotel_id of the row which you want to update:")
						nhotel_id=input("enter the new hotel_id: ")
						city_id=input("enter new city_id:")
						hotel=input("enter new hotel name :")
						stay_cost=input("enter new stay_cost of the city:")
						d=[city_id, hotel, stay_cost, nhotel_id , ohotel_id]
						mycursor.execute("update hotels set city_id=%s,hotel=%s, stay_cost=%s, hotel_id=%s where hotel_id=%s" , d)
						mydb.commit()
						print("row updated.")
					elif table=="sights":
						mycursor.execute("select * from sights")
						rec=mycursor.fetchall()
						print(progfns.maketable(rec))
						osight_id=input("enter the sight_id of the row which you want to update:")
						mycursor.execute("delete from sights where sight_id=%s" , [osight_id])
						mydb.commit()
						sight=input("enter new sight name :")
						city_id=input("enter new city_id of the city:")
						nsight_id=input("enter new sight_id:")
						d=[city_id, sight , nsight_id]
						mycursor.execute("insert into sights values(%s,%s,%s)" , d)
						mydb.commit()
						print("row updated.")
					elif table=="tcost":
						mycursor.execute("select * from tcost")
						rec=mycursor.fetchall()
						print(progfns.maketable(rec))
						ocity_id=input("enter the city_id of the row which you want to update:")
						ptickets=int(input("enter new plane tickets cost:"))
						city_id=input("enter new city_id of the city:")
						ttickets=int(input("enter new train tickets cost:"))
						d=[city_id,ptickets,ttickets,ocity_id]
						mycursor.execute("update tcost set city_id=%s, ptickets=%s, ttickets=%s where city_id=%s" , d)
						mydb.commit()
						print("row updated.")
				elif c=="4":
					print("choose table:")
					mycursor.execute("show tables")
					tables=mycursor.fetchall()
					print(progfns.maketable(tables))
					table=input("enter the table:")
					if table=="cities":
						city=input("enter city name:")
						mycursor.execute("select * from cities where city=%s" , [city])
						rec=mycursor.fetchone()
						print(rec)

					elif table=="hotels":
						city=input("enter city name:")
						mycursor.execute("select * from hotels where city_id=(select city_id from cities where city=%s)" , [city])
						rec=mycursor.fetchall()
						print(rec)
					elif table=="sights":
						city=input("enter city name:")
						mycursor.execute("select * from sights where city_id=(select city_id from cities where city=%s)" , [city])
						rec=mycursor.fetchall()
						print(rec)
					elif table=="tcost":
						city=input("enter city name:")
						mycursor.execute("select * from tcost where city_id=(select city_id from cities where city=%s)" , [city])
						rec=mycursor.fetchall()
						print(rec)
				c=input("Do you wish to continue? yes>y no>n :")
				if c=="n":
					print("Thank you for using Velocity!")
					exit()

		else:
			exit()



import mysql.connector

# DATABASE CONNECTION
try:
    mydb = mysql.connector.connect(
        host="127.0.0.1", # Your host
        user="YOUR USERNAME",
        password= "YOUR PASSWORD",
        auth_plugin = "mysql_native_password",
        database = "project" # Enter Your DB Name
    )
    mycursor = mydb.cursor()
except:
    print("Database Connection Error")
    exit()
# FIRST SELECTION MENU WHAT OPERATION WILL YOU DO
def operation_select():
    while True: # Endless while loop to navigate through the menu.
        print("What you want to do?")
        print(" 1- READ FROM DATABASE\n 2- WRITE TO DATABASE\n 3- DELETE FROM DB\n q- QUIT")
        operation_selector = input()
        # Call the method according to input parameter.
        if(operation_selector == "1"):
            read_from_db()
        elif(operation_selector == "2"):
            insert_data()
        elif(operation_selector == "3"):
            delete_from_db()
        elif(operation_selector == "q"):
            break
# When you select the operation than you should select the topic which you want to do operation inside it
def select_content(): 
    print("Select the content (1,3)\n")
    content = input(" 1- Book\n 2- Car\n 3- Movie\n" )
    return content
# This method to insert data to the table.
def insert_data():
    
    while True: # Again endless while loop to navigate inside the menu.
        selected_menu = select_content() # Input to select the content to make operation.
        
        if(selected_menu == "1"):      # in Book Table
            print("You are in BOOK Table")
            #id = int(input("Enter id"))   we won't take id from user. It's automatic.
            #Take parameters from user
            b_name = input("\nEnter Book Name\n")
            author = input("\nEnter Author\n")
            b_genres = input("\nEnter Genres\n")
            b_date = input("\nEnter date - ../../..\n")
            ısbn = input("\nEnter ISBN Value\n")
            #Takes the parameters ordered and assing them to the inside of the query.
            book_sql = "INSERT INTO BOOK_DATA (book_name, author, genres, date, ISBN) VALUES ('{}','{}','{}','{}','{}')".format(b_name,author,b_genres,b_date,ısbn)
            print(mycursor.rowcount, "Book added succesfully.")
            mycursor.execute(book_sql) #Executes the given query
            mydb.commit() # Sends a COMMIT statement to the MySQL server. Since by default Connector/Python does not autocommit, 
                          # it is important to call this method after every transaction that modifies data for tables that use transactional storage engines


        elif (selected_menu == "2"):
            print("You are in CAR Table")

            brand = input("Enter Car Brand\n")
            car_model = input("Enter Car Model\n")
            year = input("Enter Year\n")
            price = input("Enter Price ($)\n")
            #Takes the parameters ordered and assing them to the inside of the query.
            car_sql = "INSERT INTO CAR_DATA (brand, car_model, year, price) VALUES ('{}','{}','{}','${}')".format(brand,car_model,year,price)
            print("Car added Succesfully")
            mycursor.execute(car_sql) #Executes the given query
            mydb.commit()

        elif(selected_menu == "3"):
            print("You are in FILM Table")

            f_name = input("\nEnter Movie Name\n")
            f_genres = input("\n Enter the genres\n")
            publishDate = input("\nEnter publis year\n")
            director = input("\nEnter the director\n")
            starOfTheFilm = input("\nEnter the star of the film\n")
            #Takes the parameters ordered and assing them to the inside of the query.
            movie_sql = "INSERT INTO MOVIE_DATA (movie_name, movie_genres, publish_date, director, star) VALUES ('{}','{}','{}','{}','{}')".format(f_name,f_genres,publishDate,director,starOfTheFilm)
            print(mycursor.rowcount, "Film added succesfully.")
            mycursor.execute(movie_sql) #Executes the given query
            mydb.commit()
        # at the and of the operation asks what you want to do continue or no. If user says 'NO'(n) then it route user to upper menu.
        finisher = input("Want to do another operation in here or go to upper menu(y/n)\n") 
        if(finisher == "n"):
            break
        else:
            continue
# Delete data from database.
def delete_from_db():
    while True:
        
        selected_menu = select_content() # Select the header which you want to do opration.
        
        if(selected_menu == "1"):  # In book table
            print("FROM BOOK TABLE")
            print("  1- by ID\n 2- by Book Name\n 3- by Author\n 4- by Genres\n 5- by date(../../..)\n 6- by ISBN\n 7- Whole data")
            query_selector = input("Enter the selection (1,7)")
            # Select the parameter which you will use to select and delete the data.
            # Than take the input from user than assign it to the query.
            if(query_selector == "1"):  
                book_id = input(" Enter Book ID\n ")
                bsql1 = "DELETE FROM book_data WHERE id = '%s' ORDER BY id " % (book_id)
                executer(bsql1) # Calls executer method and give the query inside it.

            elif(query_selector == "2"):
                name = input(" Enter Book Name\n ")
                bsql2 = "DELETE FROM book_data WHERE book_name = '%s' ORDER BY id " % (name) 
                executer(bsql2)
                
            elif(query_selector == "3"):
                book_author = input(" Enter Book Author\n")
                bsql3 = "DELETE FROM book_data WHERE author = '%s' ORDER BY id " % (book_author) 
                executer(bsql3)

            elif(query_selector == "4"):
                book_genres = input(" Enter Book Genres\n ")
                bsql4 = "DELETE FROM book_data WHERE genres = '%s' ORDER BY id" % (book_genres) 
                executer(bsql4)
            
            elif(query_selector == "5"):
                book_date = input(" Enter Book Date (./../....)\n ")
                bsql5 = "DELETE FROM book_data WHERE date = '%s' ORDER BY id" % (book_date) 
                executer(bsql5)

            elif(query_selector == "6"):
                book_isbn = input(" Enter Book ISBN\n ")
                bsql6 = "DELETE FROM book_data WHERE ISBN = '%s' ORDER BY id" % (book_isbn) 
                executer(bsql6)
            
            elif(query_selector == "7"): 
                bsql7 = "DELETE FROM book_data ORDER BY id"
                executer(bsql7)

            else: # If the input is invalid error message.
                print("Invalid Input") 
                continue #Continue to the menu.
        
        if(selected_menu == "2"): # In car table
            print("FROM CAR TABLE")
            print("  1- by Brand\n 2- by Car Model\n 3- by Year\n 4- by Price\n 5- Whole Data")
            query_selector = input("Enter the selection (1,5)")

            #Select what parameter will you use to select and delete data.
            if(query_selector == "1"):
                car_brand = input(" Enter Car Brand\n ")
                csql1 = "DELETE FROM car_data WHERE brand = '%s' ORDER BY brand" % (car_brand) 
                executer(csql1)
            
            elif(query_selector == "2"):
                car_model = input(" Enter Car Model\n ")
                csql2 = "DELETE FROM car_data WHERE car_model = '%s' ORDER BY brand" % (car_model) 
                executer(csql2)
                
            elif(query_selector == "3"):
                car_year = input(" Enter Car Year\n ")
                csql3 = "DELETE FROM car_data WHERE year = '%s' ORDER BY brand" % (car_year) 
                executer(csql3)
                
            elif(query_selector == "4"):
                car_price_min = input(" Enter Min Price $\n ")
                car_price_max = input(" Enter Max Price $\n")
                csql4 = "DELETE FROM car_data WHERE price BETWEEN '$%s' AND '$%s' ORDER BY brand" % (car_price_min,car_price_max) 
                executer(csql4)
                
            elif(query_selector == "5"):
                csql5 = "DELETE FROM car_data ORDER BY brand"
                executer(csql5)
            else:
                print("Invalid Input")
                continue
            
        if(selected_menu == "3"): # In Movie table
            print("FROM MOVIE TABLE")
            print("  1- by Movie Name\n 2- by Genres\n 3- by Publish Date\n 4- by Director\n 5- by Star of the Movie\n 6- Whole Data")
            query_selector = input("Enter the selection (1,6)")
            #Select what parameter will you use to select and delete data.
            if(query_selector == "1"):
                    movie_name = input(" Enter Movie Name\n ")
                    msql1 = "DELETE FROM movie_data WHERE movie_name = '%s' ORDER BY movie_genres" % (movie_name) 
                    executer(msql1)
                        
            elif(query_selector == "2"):
                    movie_genres = input(" Enter Movie Genres\n ")
                    msql2 = "DELETE FROM movie_data WHERE movie_genres = '%s' ORDER BY movie_genres" % (movie_genres) 
                    executer(msql2)
                    
            elif(query_selector == "3"):
                    movie_publish = input(" Enter Movie Publish Date (./../....)\n")
                    msql3 = "DELETE FROM movie_data WHERE publish_date = '%s' ORDER BY movie_genres" % (movie_publish) 
                    executer(msql3)
                    
            elif(query_selector == "4"):
                    movie_director = input(" Enter Movie Director\n ")
                    msql4 = "DELETE FROM movie_data WHERE director = '%s' ORDER BY movie_genres" % (movie_director) 
                    executer(msql4)
                    
            elif(query_selector == "5"):
                    movie_star = input(" Enter Star of the Movie\n ")
                    msql5 = "DELETE FROM movie_data WHERE star = '%s' ORDER BY movie_genres" % (movie_star) 
                    executer(msql5)
                    
            elif(query_selector == "6"):
                    msql6 = "DELETE FROM movie_data ORDER BY movie_genres" 
                    executer(msql6)
            else:
                    print("Invalid Input")
            # at the and of the operation asks what you want to do continue or no. If user says 'NO'(n) then it route user to upper menu.
            finisher = input("Want to do another operation in here or go to upper menu(y/n)\n") 
            if(finisher == "n"):
                break
            else:
                continue
# For read data from database.
def read_from_db():
    while True: # To navigate inside the menu

        content_selector = select_content()
        #Select the parameter area to make operation.
        if(content_selector == "1"):
            print("FROM BOOK TABLE")
            print("  1- by ID\n 2- by Book Name\n 3- by Author\n 4- by Genres\n 5- by date(../../..)\n 6- by ISBN\n 7- Whole data")
            query_selector = input("\nEnter the selection (1,7)")
            # After selection takes input from user than assign that value to the query.
            if(query_selector == "1"): 
                book_id = input(" Enter Book ID\n ")
                bsql1 = "SELECT * FROM book_data WHERE id = '%s' ORDER BY id " % (book_id)
                read_for_book(bsql1) #calls read_for_book() method and give inside it query. 

            elif(query_selector == "2"):
                name = input(" Enter Book Name\n ")
                bsql2 = "SELECT * FROM book_data WHERE book_name = '%s' ORDER BY id " % (name) 
                read_for_book(bsql2)
               
            elif(query_selector == "3"):
                book_author = input(" Enter Book Author\n")
                bsql3 = "SELECT * FROM book_data WHERE author = '%s' ORDER BY id " % (book_author) 
                read_for_book(bsql3)

            elif(query_selector == "4"):
                book_genres = input(" Enter Book Genres\n ")
                bsql4 = "SELECT * FROM book_data WHERE genres = '%s' ORDER BY id" % (book_genres) 
                read_for_book(bsql4)
        
            elif(query_selector == "5"):
                book_date = input(" Enter Book Date (./../....)\n ")
                bsql5 = "SELECT * FROM book_data WHERE date = '%s' ORDER BY id" % (book_date) 
                read_for_book(bsql5)

            elif(query_selector == "6"):
                book_isbn = input(" Enter Book ISBN\n ")
                bsql6 = "SELECT * FROM book_data WHERE ISBN = '%s' ORDER BY id" % (book_isbn) 
                read_for_book(bsql6)
            elif(query_selector == "7"): 
                bsql7 = "SELECT * FROM book_data ORDER BY id"
                read_for_book(bsql7)

            else:
                print("Invalid Input")
                continue

        if(content_selector == "2"):
            print("FROM CAR TABLE")
            print("  1- by Brand\n 2- by Car Model\n 3- by Year\n 4- by Price\n 5- Whole Data")
            query_selector = input("Enter the selection (1,5)")

            if(query_selector == "1"):
                car_brand = input(" Enter Car Brand\n ")
                csql1 = "SELECT * FROM car_data WHERE brand = '%s' ORDER BY brand" % (car_brand) 
                read_for_car(csql1)
        
            elif(query_selector == "2"):
                car_model = input(" Enter Car Model\n ")
                csql2 = "SELECT * FROM car_data WHERE car_model = '%s' ORDER BY brand" % (car_model) 
                read_for_car(csql2)
            
            elif(query_selector == "3"):
                car_year = input(" Enter Car Year\n ")
                csql3 = "SELECT * FROM car_data WHERE year = '%s' ORDER BY brand" % (car_year) 
                read_for_car(csql3)
            
            elif(query_selector == "4"):
                car_price_min = input(" Enter Min Price $\n ")
                car_price_max = input(" Enter Max Price $\n")
                csql4 = "SELECT * FROM car_data WHERE price BETWEEN '%s' AND '%s'" % (car_price_min,car_price_max) 
                read_for_car(csql4)
            
            elif(query_selector == "5"):
                csql5 = "SELECT * FROM car_data ORDER BY brand"
                read_for_car(csql5)
            else:
                print("Invalid Input")
                continue

        if(content_selector == "3"):
            print("FROM MOVIE TABLE")
            print("  1- by Movie Name\n 2- by Genres\n 3- by Publish Date\n 4- by Director\n 5- by Star of the Movie\n 6- Whole Data")
            query_selector = input("Enter the selection (1,6)")

            if(query_selector == "1"):
                movie_name = input(" Enter Movie Name\n ")
                msql1 = "SELECT * FROM movie_data WHERE movie_name = '%s' ORDER BY movie_genres" % (movie_name) 
                read_for_movie(msql1)
                  
            elif(query_selector == "2"):
                movie_genres = input(" Enter Movie Genres\n ")
                msql2 = "SELECT * FROM movie_data WHERE movie_genres = '%s' ORDER BY movie_genres" % (movie_genres) 
                read_for_movie(msql2)
            
            elif(query_selector == "3"):
                movie_publish = input(" Enter Movie Publish Date (./../....)\n")
                msql3 = "SELECT * FROM movie_data WHERE publish_date = '%s' ORDER BY movie_genres" % (movie_publish) 
                read_for_movie(msql3)
            
            elif(query_selector == "4"):
                movie_director = input(" Enter Movie Director\n ")
                msql4 = "SELECT * FROM movie_data WHERE director = '%s' ORDER BY movie_genres" % (movie_director) 
                read_for_movie(msql4)
            
            elif(query_selector == "5"):
                movie_star = input(" Enter Star of the Movie\n ")
                msql5 = "SELECT * FROM movie_data WHERE star = '%s' ORDER BY movie_genres" % (movie_star) 
                read_for_movie(msql5)
            
            elif(query_selector == "6"):
                msql6 = "SELECT * FROM movie_data ORDER BY movie_genres" 
                read_for_movie(msql6)
            else:
                print("Invalid Input")

        finisher = input("Want to do another operation (y/n)\n")
        if(finisher == "n"):
            break
        else:
            continue   

# To won't read same operations many times wrote them by a method.
def read_for_car(sql):
    try:
        mycursor.execute(sql)  #Executes the given query.
        results = mycursor.fetchall() # Assign the datas to results which came from that query. 
        # If query does not contain anything returns an error message. 
        if len(results) == 0:
            print("Data couldn't found")
        else: # Else writes them with an order
            for i in results:
                brand = i[0]
                model = i[1]
                year = i[2]
                price = i[3]
                print("Brand = {}, Model = {}, Year = {}, Price = {}".format(brand,model,year,price))
    except:
            print("Data couldn't found")

def read_for_book(sql):
    try:
        mycursor.execute(sql)
        results = mycursor.fetchall()
        if len(results) == 0:
            print("Data couldn't found")
        else:
            for i in results:
                id = i[0]
                name = i[1]
                author = i[2]
                genres = i[3]
                date = i[4]
                isbn = i[5]
                print("ID = {}, Book Name = {}, Author = {}, Genres = {}, Date = {}, ISBN = {}".format(id,name,author,genres,date,isbn))
    except:
        print("Data couldn't read")
            
def read_for_movie(sql):
    try:
        mycursor.execute(sql)
        results = mycursor.fetchall()
        if(len(results) == 0):
            print("Data couldn't found")
        else:
            for i in results:
                mov_name = i[0]
                mov_genres = i[1]
                director = i[2]
                publish_date = i[3]
                star = i[4]
                print("Movie Name = {}, Genres = {}, Director = {}, Publish Date = {}, Star = {}".format(mov_name,mov_genres,director,publish_date,star))
    except:
            print("Data couldn't read")

def executer(sql): # Execures the given query
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "deleted succesfully")


#insert_data()
#read_from_db()

operation_select()

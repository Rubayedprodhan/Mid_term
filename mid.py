class Hall:
    def __init__(self,row,col,hall):
        self.seats = [[0 for i in range(col)] 
                      for j in range(row)]
        self.show_list =[]
        self.row =row
        self.col =col
        self.hall =hall



    def entry_show(self,id,movie_name,time):

        show ={'id': id,'movie_name':movie_name,'time':time}

        self.show_list.append(show)




    def book_seats(self, seat_book):
        for row,col in seat_book:
            if 1 <= row<=self.row and 1<=col<=self.col:

                if self.seats[row ][col] == 0:
                    self.seats[row ][col] = 1

                else:

                
                    print("Seat is Booked")
            else:

                print("Invalid Seat")



    def view_list(self):

        for show in self.show_list:
            print(show)


    def available_seats(self):

        for row in self.seats:
            print(" ".join(map(str,row)))


class StarCinema:
    def __init__(self):
        self.hall_dict={}


    def entry_hall(self,hall):
        self.hall_dict[hall.hall] = hall


    def hall_by_number(self,hall_number):
        return self.hall_dict.get(hall_number)


hall1 = Hall(3,2,8)

hall2 = Hall(3,2,11)



hall1.entry_show('555','The Godfather','19:00 AM')
hall2.entry_show('666','Citizen Kane', '1:00 PM')



cinema = StarCinema()
cinema.entry_hall(hall1)
cinema.entry_hall(hall2)



while True:

    print("1.Shows")
    print("2.Available Seats")
    print("3.Book Tickets")
    print("4.Exit")

    option = input("choice the option : ")

    if option=='1':

        for hall_number, hall in cinema.hall_dict.items():
            print(f"Hall Number: {hall_number}")

            hall.view_list()

        print()



    elif option == '2':


        hall_number = int(input("Enter hall number: "))
        hall = cinema.hall_by_number(hall_number)

        if hall:
            hall.available_seats()
        else:
            print("Hall not Availble.")


    elif option == '3':


        hall_number = int(input("Enter Hall id:"))
        hall = cinema.hall_by_number(hall_number)
        if hall:
            show_id = input("Enter Show ID: ")

            seat_count = int(input("Enter the seats Number: "))

            booking_seats = []
            for i in range(seat_count):

                seat_input = input(f"Enter Seat {i+1} (row-col): ")

                seat = tuple(map(int, seat_input.split('-')))

                booking_seats.append(seat)

            hall.book_seats(show_id, booking_seats)
            print("Your seat is booked ")
        else:
            print("Hall not Availble.")



    elif option == '4':
        break
    else:
        print("please more again")

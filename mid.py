class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._initialize_seats()


    def _initialize_seats(self):
        seats = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
        self._seats[self._hall_no] = seats


    def entry_show(self, show_id, movie_name, time):
        show = (show_id, movie_name, time)
        self._show_list.append(show)
       
        self._seats[show_id] = [[0 for _ in range(self._cols)] 
                                for _ in range(self._rows)]


    def book_seats(self, show_id, seat_book):
        if show_id not in self._seats:
            print("Invalid Show ID")
            return


        seats = self._seats[show_id]

        for row, col in seat_book:
            if not (0 <= row < self._rows and 0 <= col < self._cols):
                print(f"Invalid Seat ({row}, {col})")
                continue


            if seats[row][col] == 1:
                print(f"Seat ({row}, {col}) is already booked")
            else:
                seats[row][col] = 1
                print(f"Seat ({row}, {col}) booked successfully")


    def view_show_list(self):
        print("Shows running:")
        for show in self._show_list:
            print(show)


    def view_available_seats(self, show_id):
        if show_id not in self._seats:
            print("Invalid Show ID")
            return


        print("Available seats:")
        seats = self._seats[show_id]
        for i, row in enumerate(seats):
            for j, seat in enumerate(row):
                if seat == 0:
                    print(f"({i}, {j})", end=" ")
            print() 



class StarCinema:
    def __init__(self):
        self._hall_list = []

    def entry_hall(self, hall):
        self._hall_list.append(hall)

    def view_all_shows(self):
        print("All Shows:")
        for hall in self._hall_list:
            hall.view_show_list()

    def view_available_seats(self, hall_no):
        hall = self.get_hall_by_number(hall_no)
        if hall:
            show_id = input("Enter Show ID: ")
            hall.view_available_seats(show_id)
        else:
            print("Hall not found")

    def book_tickets(self, hall_no):
        hall = self.get_hall_by_number(hall_no)
        if hall:
            show_id = input("Enter Show ID: ")
            cnt = int(input("Enter the Number of Seats: "))
            booking_seats = []
            for _ in range(cnt):
                seat_input = input(f"Enter Seat {_ + 1} (row-col): ")
                seat = tuple(map(int, seat_input.split('-')))
                booking_seats.append(seat)
            hall.book_seats(show_id, booking_seats)
        else:
            print("Hall not found")

    def get_hall_by_number(self, hall_no):
        for hall in self._hall_list:
            if hall._hall_no == hall_no:
                return hall
        return None




cinema = StarCinema()
hall1 = Hall(5, 5, 1)
hall1.entry_show('100', 'Avengers', '12:00 PM')
hall2 = Hall(6, 6, 2)
hall2.entry_show('101', 'Spider-Man', '3:00 PM')
cinema.entry_hall(hall1)
cinema.entry_hall(hall2)



while True:
    print("1. View all shows")
    print("2. View available seats")
    print("3. Book tickets")
    print("4. Exit")
    option = input("Enter your choice: ")


    if option == '1':
        cinema.view_all_shows()


    elif option == '2':
        hall_no = input("Enter Hall Number: ")
        cinema.view_available_seats(hall_no)


    elif option == '3':
        hall_no = input("Enter Hall Number: ")
        cinema.book_tickets(hall_no)


    elif option == '4':
        break

    else:
        print("Invalid option. Please try again.")

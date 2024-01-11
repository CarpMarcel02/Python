import tkinter as tk
from tkinter import colorchooser, ttk

from PIL import Image, ImageTk


class MainFrame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.attributes("-fullscreen", True)
        self.title("Main Menu")

        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        # Create a dictionary to hold the frames
        self.frames = {}
        self.rows = 0
        self.collumns = 0
        self.wait = 0

        self.player_option_var = tk.IntVar(value=1)  # Default to player 1 being selected

        self.current_player = 0

        # Main Menu frame
        self.create_main_menu()
        self.create_play_game()
        self.create_player_vs_computer()
        self.player_vs_player()
        self.player_vs_easyAI()
        self.player_vs_mediumAI()
        self.player_vs_hardAI()
        self.game_buttons = []
        self.show_frame("MainMenu")

    def create_main_menu(self):
        main_menu_frame = tk.Frame(self)
        main_menu_frame.pack(fill="both", expand=True)
        self.frames["MainMenu"] = main_menu_frame

        bg_image_path = r"E:\Python\4InARow\poza editata.png"
        bg_image = ImageTk.PhotoImage(Image.open(bg_image_path).resize((self.screen_width, self.screen_height)))

        canvas = tk.Canvas(main_menu_frame, width=self.screen_width, height=self.screen_height)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg_image, anchor="nw")
        canvas.image = bg_image  # Keep a reference so it's not garbage collected

        button_image_path = r"E:\Python\4InARow\chatframe.png"
        button_image = ImageTk.PhotoImage(Image.open(button_image_path).resize((150, 50)))

        button = tk.Button(
            canvas,
            image=button_image,
            command=lambda: self.show_frame("PlayGame"),
            text="Play Game",
            font=("Belinsky", 14),
            compound="center",
            fg="black",
            borderwidth=0,
            highlightthickness=0
        )

        button.image = button_image  # Keep a reference so it's not garbage collected
        button_window = canvas.create_window(self.screen_width // 2, self.screen_height // 3, anchor="center",
                                             window=button)

        self.add_exit_button(main_menu_frame, canvas)
        return main_menu_frame

    def update_player_selection(self):
        selected_option = self.player_option_var.get()
        print(f"Selected option is: {'Player 1' if selected_option == 1 else 'Bot'}")

    def create_play_game(self):
        play_game_frame = tk.Frame(self)
        self.frames["PlayGame"] = play_game_frame

        bg_image_path = r"E:\Python\4InARow\poza needitata.jpg"
        # Simplify the background to a solid color for visibility checking
        bg_image = ImageTk.PhotoImage(Image.open(bg_image_path).resize((self.screen_width, self.screen_height)))

        canvas = tk.Canvas(play_game_frame, width=self.screen_width, height=self.screen_height)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg_image, anchor="nw")
        canvas.image = bg_image  # Keep a reference

        # Temporary label for context
        label = tk.Label(play_game_frame, text="Choose an option", font=("Helvetica", 24), bg='light blue')
        label.pack(pady=50)

        button_image_path = r"E:\Python\4InARow\chatframe.png"
        button_image = ImageTk.PhotoImage(Image.open(button_image_path).resize((190, 50)))

        # Simplified button without an image for testing
        back_button = tk.Button(
            play_game_frame,
            text="Back to Main Menu",
            image=button_image,
            font=("Helvetica", 14),
            command=lambda: self.show_frame("MainMenu"),
            compound="center",
            fg="black",
            borderwidth=0,
            highlightthickness=0
        )
        back_button.image = button_image
        button_window = canvas.create_window(
            self.screen_width // 2, self.screen_height - 550,  # Adjust position as needed
            window=back_button
        )

        play_vs_player = tk.Button(
            play_game_frame,
            text="Player Vs Player",
            image=button_image,
            font=("Helvetica", 14),
            command=lambda: self.show_frame("PlayerVsPlayer"),
            compound="center",
            fg="black",
            borderwidth=0,
            highlightthickness=0
        )
        play_vs_player.image = button_image
        button_window = canvas.create_window(
            self.screen_width // 2, self.screen_height - 750,  # Adjust position as needed
            window=play_vs_player
        )

        play_vs_computer = tk.Button(
            play_game_frame,
            text="Player Vs Computer",
            image=button_image,
            font=("Helvetica", 14),
            command=lambda: self.show_frame("PlayerVsComputer"),
            compound="center",
            fg="black",
            borderwidth=0,
            highlightthickness=0
        )
        play_vs_computer.image = button_image
        button_window = canvas.create_window(
            self.screen_width // 2, self.screen_height - 650,  # Adjust position as needed
            window=play_vs_computer
        )

        play_game_frame.pack_forget()

        self.add_exit_button(play_game_frame, canvas)

        return play_game_frame

    def create_player_vs_computer(self):
        play_vs_computer_frame = tk.Frame(self)
        self.frames["PlayerVsComputer"] = play_vs_computer_frame
        print("Player vs Computer frame created")

        bg_image_path = r"E:\Python\4InARow\poza needitata.jpg"
        # Simplify the background to a solid color for visibility checking
        bg_image = ImageTk.PhotoImage(Image.open(bg_image_path).resize((self.screen_width, self.screen_height)))

        canvas = tk.Canvas(play_vs_computer_frame, width=self.screen_width, height=self.screen_height)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg_image, anchor="nw")
        canvas.image = bg_image  # Keep a reference

        # Temporary label for context
        label = tk.Label(play_vs_computer_frame, text="Choose an option", font=("Helvetica", 24), bg='light blue')
        label.pack(pady=50)

        button_image_path = r"E:\Python\4InARow\chatframe.png"
        button_image = ImageTk.PhotoImage(Image.open(button_image_path).resize((190, 50)))

        # Simplified button without an image for testing
        back_button = tk.Button(
            play_vs_computer_frame,
            text="Back to Play Menu",
            image=button_image,
            font=("Helvetica", 14),
            command=lambda: self.show_frame("PlayGame"),
            compound="center",
            fg="black",
            borderwidth=0,
            highlightthickness=0
        )
        back_button.image = button_image
        button_window = canvas.create_window(
            self.screen_width // 2, self.screen_height - 450,  # Adjust position as needed
            window=back_button
        )
        easy_mode = tk.Button(
            play_vs_computer_frame,
            text="Easy Mode",
            image=button_image,
            font=("Helvetica", 14),
            command=lambda: self.show_frame("PlayerVsEasyBot"),
            compound="center",
            fg="black",
            borderwidth=0,
            highlightthickness=0
        )
        easy_mode.image = button_image
        button_window = canvas.create_window(
            self.screen_width // 2, self.screen_height - 750,  # Adjust position as needed
            window=easy_mode
        )
        medium_mode = tk.Button(
            play_vs_computer_frame,
            text="Medium Mode",
            image=button_image,
            font=("Helvetica", 14),
            command=lambda: self.show_frame("PlayerVsMediumBot"),
            compound="center",
            fg="black",
            borderwidth=0,
            highlightthickness=0
        )
        medium_mode.image = button_image
        button_window = canvas.create_window(
            self.screen_width // 2, self.screen_height - 650,  # Adjust position as needed
            window=medium_mode
        )
        hard_mode = tk.Button(
            play_vs_computer_frame,
            text="Hard Mode",
            image=button_image,
            font=("Helvetica", 14),
            command=lambda: self.show_frame("PlayerVsHardBot"),
            compound="center",
            fg="black",
            borderwidth=0,
            highlightthickness=0
        )
        hard_mode.image = button_image
        button_window = canvas.create_window(
            self.screen_width // 2, self.screen_height - 550,  # Adjust position as needed
            window=hard_mode
        )

        play_vs_computer_frame.pack_forget()

        self.add_exit_button(play_vs_computer_frame, canvas)

        return play_vs_computer_frame

    def player_vs_player(self):
        player_vs_player_frame = tk.Frame(self)
        self.frames["PlayerVsPlayer"] = player_vs_player_frame

        bg_image_path = r"E:\Python\4InARow\player_vs_player.png"
        # Simplify the background to a solid color for visibility checking
        bg_image = ImageTk.PhotoImage(Image.open(bg_image_path).resize((self.screen_width, self.screen_height)))

        canvas = tk.Canvas(player_vs_player_frame, width=self.screen_width, height=self.screen_height)
        canvas.pack(fill="both", expand=True)

        canvas.create_image(0, 0, image=bg_image, anchor="nw")
        canvas.image = bg_image  # Keep a reference

        button_image_path = r"E:\Python\4InARow\chatframe.png"
        button_image = ImageTk.PhotoImage(Image.open(button_image_path).resize((190, 50)))

        back_button = tk.Button(
            player_vs_player_frame,
            text="Back",
            image=button_image,
            font=("Helvetica", 14),
            command=lambda: self.show_frame("PlayGame"),
            compound="center",
            fg="black",
            borderwidth=0,
            relief='flat',
            highlightthickness=0
        )

        back_button.image = button_image
        button_window = canvas.create_window(
            self.screen_width // 2 - 130, self.screen_height - 305,  # Adjust position as needed
            window=back_button
        )

        row_select = tk.Spinbox(player_vs_player_frame, from_=6, to=10, wrap=True)
        canvas.create_window(1037, 568, window=row_select)

        column_select = tk.Spinbox(player_vs_player_frame, from_=7, to=13, wrap=True)
        canvas.create_window(1094, 603, window=column_select)

        player1_entry = tk.Entry(player_vs_player_frame)
        player1_entry_window = canvas.create_window(866, 287, window=player1_entry)

        player2_entry = tk.Entry(player_vs_player_frame)
        player2_entry_window = canvas.create_window(1166, 287, window=player2_entry)

        self.player1_radiobutton = ttk.Radiobutton(
            player_vs_player_frame,
            variable=self.player_option_var,
            value=1,  # The value this radiobutton represents
            command=self.update_player_selection
        )
        canvas.create_window(935, 680, window=self.player1_radiobutton)

        self.player2_radiobutton = ttk.Radiobutton(
            player_vs_player_frame,
            variable=self.player_option_var,
            value=2,  # The value this radiobutton represents
            command=self.update_player_selection
        )
        canvas.create_window(1180, 680, window=self.player2_radiobutton)

        color_player_1 = tk.Button(player_vs_player_frame, text="    ", bg="white",
                                   command=lambda: self.choose_color(color_player_1))
        button_window = canvas.create_window(805, 260, window=color_player_1)  # Position the button at (100, 100)

        color_player_2 = tk.Button(player_vs_player_frame, text="    ", bg="white",
                                   command=lambda: self.choose_color(color_player_2))
        button_window = canvas.create_window(1105, 260, window=color_player_2)  # Position the button at (100, 100)

        button_image_path = r"E:\Python\4InARow\chatframe.png"
        button_image = ImageTk.PhotoImage(Image.open(button_image_path).resize((190, 50)))

        player_vs_player_frame.pack_forget()

        self.add_exit_button(player_vs_player_frame, canvas)

        play_button = tk.Button(
            player_vs_player_frame,
            text="Play",
            image=button_image,
            font=("Helvetica", 14),
            compound="center",
            fg="black",
            borderwidth=0,
            relief='flat',
            highlightthickness=0,
            command=lambda: self.start_game(
                color_player_1.cget('bg'), color_player_2.cget('bg'),
                player1_entry.get(), player2_entry.get(),
                int(row_select.get()), int(column_select.get()),
                self.player_option_var.get()  # Pass the value of the option variable
            )
        )
        play_button.image = button_image
        button_window = canvas.create_window(
            self.screen_width // 2 + 130, self.screen_height - 305,  # Adjust position as needed
            window=play_button
        )

        return player_vs_player_frame

    def start_game(self, player1_color, player2_color, player1_name, player2_name, rows, columns, player1_is_checked):
        if "GameInterface" not in self.frames:
            self.create_game_interface(player1_color, player2_color, player1_name, player2_name, rows, columns,
                                       player1_is_checked)

        self.show_frame("GameInterface")
        if player1_is_checked == 1:
            self.current_player = 1
        else:
            self.current_player = 2

    def handle_button_click(self, row, col, player1_color, player2_color):
        if self.wait == 0:
            current_button = self.game_buttons[row][col]
            if player1_color == 'white':
                player1_color = 'yellow'
            if player2_color == 'white':
                player2_color = 'red'
            copy_row = row
            copy_collumn = col
            if current_button['bg'] == 'white':  # Check if the button hasn't been clicked
                if self.current_player == 1:
                    current_color = player1_color
                else:
                    current_color = player2_color
                self.game_buttons[row][col]['bg'] = 'white'

                self.animate_button_change(row, col, row, current_color, player1_color, player2_color)

    def animate_button_change(self, row, col, initial_row, current_color, player1_color, player2_color, delay=100):
        if row >= self.rows or self.game_buttons[row][col]['bg'] != 'white':
            # Stop the animation when we reach the bottom or a non-white button
            # print(f" ce pana mea  {row},{self.rows},{col} ")
            self.wait = 0
            self.switch_player_turn()
            winner = self.player_has_won(player1_color, player2_color)
            if winner == 1:
                print("1 First player has won ")
            elif winner == 2:
                print("1 Second player has won ")
            elif winner == 3:
                print("Game is draw")
            else:
                print("Meciul nu s-a terminat")

            return

        self.wait = 1
        self.game_buttons[initial_row][col]['bg'] = 'white'

        if row > 0:
            # Only revert the previous button to white if it's not the initially clicked button
            self.game_buttons[row - 1][col]['bg'] = 'white'
        self.game_buttons[row][col]['bg'] = current_color

        self.after(delay, lambda: self.animate_button_change(row + 1, col, initial_row, current_color, player1_color,
                                                             player2_color))

    def switch_player_turn(self):
        # Switch turns
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1

    def player_has_won(self, player1_color, player2_color):
        # for i in range(self.rows):
        #     for j in range(self.collumns):
        #         print(f" {i} {j}", end=" ")
        #     print()
        # for i in range(self.rows):
        #     for j in range(self.collumns):
        #         print(self.game_buttons[i][j]['bg'], end=' ')
        #     print()
        gasit = 0
        for i in range(self.rows):
            for j in range(self.collumns):
                if self.game_buttons[i][j]['bg'] == 'white':
                    gasit = 1
                else:
                    culoare = self.game_buttons[i][j]['bg']
                    # print(f"da frate {i} {j} {self.rows} {self.collumns}")
                    if i + 1 < self.rows and i + 3 < self.rows:
                        if self.game_buttons[i + 1][j]['bg'] == culoare:  # PE COLOANA DACA SUNT 4
                            if self.game_buttons[i + 2][j]['bg'] == culoare and self.game_buttons[i + 3][j][
                                'bg'] == culoare:
                                if culoare == player1_color:
                                    return 1
                                else:
                                    if culoare == player2_color:
                                        return 2
                    if j + 1 < self.collumns and j + 3 < self.collumns:
                        if self.game_buttons[i][j + 1]['bg'] == culoare:  # PE LINIE DACA SUNT 4
                            if self.game_buttons[i][j + 2]['bg'] == culoare and self.game_buttons[i][j + 3][
                                'bg'] == culoare:
                                if culoare == player1_color:
                                    return 1
                                else:
                                    if culoare == player2_color:
                                        return 2
                    if i + 1 < self.rows and j + 1 < self.collumns and i + 3 < self.rows and j + 3 < self.collumns:
                        if self.game_buttons[i + 1][j + 1]['bg'] == culoare:  # PE DIAG PRINCIPALA DACA SUNT 4
                            if self.game_buttons[i + 2][j + 2]['bg'] == culoare and self.game_buttons[i + 3][j + 3][
                                'bg'] == culoare:
                                if culoare == player1_color:
                                    return 1
                                else:
                                    if culoare == player2_color:
                                        return 2
                    if i - 1 > -1 and j + 1 < self.collumns and i - 3 > -1 and j + 3 < self.collumns:
                        if self.game_buttons[i - 1][j + 1]['bg'] == culoare:  # PE DIAG secundara DACA SUNT 4
                            if self.game_buttons[i - 2][j + 2]['bg'] == culoare and self.game_buttons[i - 3][j + 3][
                                'bg'] == culoare:
                                if culoare == player1_color:
                                    return 1
                                else:
                                    if culoare == player2_color:
                                        return 2
        if gasit == 0:
            return 3
        else:
            return 0

    def create_game_interface(self, player1_color, player2_color, player1_name, player2_name, rows, columns,
                              player1_is_checked):
        game_interface_frame = tk.Frame(self)
        self.frames["GameInterface"] = game_interface_frame
        self.rows = rows
        self.collumns = columns
        # Define the size of the buttons (adjust as necessary)
        if columns < 11 and rows < 9:
            button_width = 20  # Width in text units
            button_height = 6  # Height in text units
            total_button_width = button_width * columns
            total_button_height = button_height * rows

            padding_width = (self.screen_width // 2) - (total_button_width) - 60 * columns
            padding_height = (self.screen_height // 2) - (total_button_height) - 40 * rows
        else:
            button_width = 15  # Width in text units
            button_height = 5  # Height in text units
            total_button_width = button_width * columns
            total_button_height = button_height * rows
            padding_width = (self.screen_width // 2) - (total_button_width) - 45 * columns
            padding_height = (self.screen_height // 2) - (total_button_height) - 30 * rows

        self.turn_indicator = tk.Label(game_interface_frame, text='Player 1', bg=player1_color, width=10)
        self.turn_indicator.grid(row=0, columnspan=columns)

        print(f" asta este self.screen_width {self.screen_width}")
        print(f" asta este self.screen_height {self.screen_height}")

        print(f" asta este total_button_width {total_button_width}")
        print(f" asta este total_button_height {total_button_height}")

        print(f" asta este padding_width {padding_width}")
        print(f" asta este padding_height {padding_height}")

        # Add padding frames to push the button grid to the center
        top_padding = tk.Frame(game_interface_frame, height=padding_height, width=self.screen_width)
        top_padding.grid(row=0, columnspan=columns + 2)
        left_padding = tk.Frame(game_interface_frame, width=padding_width)
        left_padding.grid(row=1, column=0, rowspan=rows)

        self.game_buttons = [[None for _ in range(columns)] for _ in range(rows)]

        for i in range(rows):
            for j in range(columns):
                button = tk.Button(
                    game_interface_frame,
                    bg='white',
                    width=button_width,
                    height=button_height,
                    command=lambda row=i, col=j: self.handle_button_click(row, col, player1_color, player2_color)

                )
                # Place buttons in the grid with padding on top and left
                button.grid(row=i + 1, column=j + 1)
                button.bind('<Button-1>',
                            lambda event, r=i, c=j: self.handle_button_click(r, c, player1_color, player2_color))
                self.game_buttons[i][j] = button

        right_padding = tk.Frame(game_interface_frame, width=padding_width)
        right_padding.grid(row=1, column=columns + 1, rowspan=rows)
        bottom_padding = tk.Frame(game_interface_frame, height=padding_height, width=self.screen_width)
        bottom_padding.grid(row=rows + 1, columnspan=columns + 2)

        game_interface_frame.pack(expand=True, fill='both')

        return game_interface_frame

    def update_player_selection(self):
        player = 1 if self.player_option_var.get() == 1 else 2
        print(f"{player} selected")

    def player_vs_easyAI(self):
        player_vs_easyAI = tk.Frame(self)
        self.frames["PlayerVsEasyBot"] = player_vs_easyAI

        bg_image_path = r"E:\Python\4InARow\player_vs_bot.png"
        # Simplify the background to a solid color for visibility checking
        bg_image = ImageTk.PhotoImage(Image.open(bg_image_path).resize((self.screen_width, self.screen_height)))

        canvas = tk.Canvas(player_vs_easyAI, width=self.screen_width, height=self.screen_height)
        canvas.pack(fill="both", expand=True)

        canvas.create_image(0, 0, image=bg_image, anchor="nw")
        canvas.image = bg_image  # Keep a reference

        button_image_path = r"E:\Python\4InARow\chatframe.png"
        button_image = ImageTk.PhotoImage(Image.open(button_image_path).resize((190, 50)))

        play_button = tk.Button(
            player_vs_easyAI,
            text="Play",
            image=button_image,
            font=("Helvetica", 14),
            compound="center",
            fg="black",
            borderwidth=0,
            relief='flat',
            highlightthickness=0
        )

        play_button.image = button_image
        button_window = canvas.create_window(
            self.screen_width // 2 + 130, self.screen_height - 305,  # Adjust position as needed
            window=play_button
        )

        back_button = tk.Button(
            player_vs_easyAI,
            text="Back",
            image=button_image,
            font=("Helvetica", 14),
            command=lambda: self.show_frame("PlayGame"),
            compound="center",
            fg="black",
            borderwidth=0,
            relief='flat',
            highlightthickness=0
        )

        back_button.image = button_image
        button_window = canvas.create_window(
            self.screen_width // 2 - 130, self.screen_height - 305,  # Adjust position as needed
            window=back_button
        )

        row_select = tk.Spinbox(player_vs_easyAI, from_=6, to=10, wrap=True)
        canvas.create_window(1037, 568, window=row_select)

        column_select = tk.Spinbox(player_vs_easyAI, from_=7, to=13, wrap=True)
        canvas.create_window(1094, 603, window=column_select)

        player1_entry = tk.Entry(player_vs_easyAI)
        player1_entry_window = canvas.create_window(866, 287, window=player1_entry)

        # player2_entry = tk.Entry(player_vs_easyAI)
        # player2_entry_window = canvas.create_window(1166, 287, window=player2_entry)

        self.player1_radiobutton = ttk.Radiobutton(
            player_vs_easyAI,
            variable=self.player_option_var,
            value=1,  # The value this radiobutton represents
            command=self.update_player_selection
        )
        canvas.create_window(935, 680, window=self.player1_radiobutton)

        self.player2_radiobutton = ttk.Radiobutton(
            player_vs_easyAI,
            variable=self.player_option_var,
            value=2,  # The value this radiobutton represents
            command=self.update_player_selection
        )
        canvas.create_window(1180, 680, window=self.player2_radiobutton)

        color_player_1 = tk.Button(player_vs_easyAI, text="    ", bg="white",
                                   command=lambda: self.choose_color(color_player_1))
        button_window = canvas.create_window(805, 260, window=color_player_1)  # Position the button at (100, 100)

        color_player_2 = tk.Button(player_vs_easyAI, text="    ", bg="white",
                                   command=lambda: self.choose_color(color_player_2))
        button_window = canvas.create_window(1105, 260, window=color_player_2)  # Position the button at (100, 100)

        button_image_path = r"E:\Python\4InARow\chatframe.png"
        button_image = ImageTk.PhotoImage(Image.open(button_image_path).resize((190, 50)))

        player_vs_easyAI.pack_forget()

        self.add_exit_button(player_vs_easyAI, canvas)

        return player_vs_easyAI

    def player_vs_mediumAI(self):
        player_vs_mediumbot = tk.Frame(self)
        self.frames["PlayerVsMediumBot"] = player_vs_mediumbot

        bg_image_path = r"E:\Python\4InARow\player_vs_bot.png"
        # Simplify the background to a solid color for visibility checking
        bg_image = ImageTk.PhotoImage(Image.open(bg_image_path).resize((self.screen_width, self.screen_height)))

        canvas = tk.Canvas(player_vs_mediumbot, width=self.screen_width, height=self.screen_height)
        canvas.pack(fill="both", expand=True)

        canvas.create_image(0, 0, image=bg_image, anchor="nw")
        canvas.image = bg_image  # Keep a reference

        button_image_path = r"E:\Python\4InARow\chatframe.png"
        button_image = ImageTk.PhotoImage(Image.open(button_image_path).resize((190, 50)))

        play_button = tk.Button(
            player_vs_mediumbot,
            text="Play",
            image=button_image,
            font=("Helvetica", 14),
            compound="center",
            fg="black",
            borderwidth=0,
            relief='flat',
            highlightthickness=0
        )

        play_button.image = button_image
        button_window = canvas.create_window(
            self.screen_width // 2 + 130, self.screen_height - 305,  # Adjust position as needed
            window=play_button
        )

        back_button = tk.Button(
            player_vs_mediumbot,
            text="Back",
            image=button_image,
            font=("Helvetica", 14),
            command=lambda: self.show_frame("PlayGame"),
            compound="center",
            fg="black",
            borderwidth=0,
            relief='flat',
            highlightthickness=0
        )

        back_button.image = button_image
        button_window = canvas.create_window(
            self.screen_width // 2 - 130, self.screen_height - 305,  # Adjust position as needed
            window=back_button
        )

        row_select = tk.Spinbox(player_vs_mediumbot, from_=6, to=10, wrap=True)
        canvas.create_window(1037, 568, window=row_select)

        column_select = tk.Spinbox(player_vs_mediumbot, from_=7, to=13, wrap=True)
        canvas.create_window(1094, 603, window=column_select)

        player1_entry = tk.Entry(player_vs_mediumbot)
        player1_entry_window = canvas.create_window(866, 287, window=player1_entry)

        # player2_entry = tk.Entry(player_vs_easyAI)
        # player2_entry_window = canvas.create_window(1166, 287, window=player2_entry)

        self.player1_radiobutton = ttk.Radiobutton(
            player_vs_mediumbot,
            variable=self.player_option_var,
            value=1,  # The value this radiobutton represents
            command=self.update_player_selection
        )
        canvas.create_window(935, 680, window=self.player1_radiobutton)

        self.player2_radiobutton = ttk.Radiobutton(
            player_vs_mediumbot,
            variable=self.player_option_var,
            value=2,  # The value this radiobutton represents
            command=self.update_player_selection
        )
        canvas.create_window(1180, 680, window=self.player2_radiobutton)

        color_player_1 = tk.Button(player_vs_mediumbot, text="    ", bg="white",
                                   command=lambda: self.choose_color(color_player_1))
        button_window = canvas.create_window(805, 260, window=color_player_1)  # Position the button at (100, 100)

        color_player_2 = tk.Button(player_vs_mediumbot, text="    ", bg="white",
                                   command=lambda: self.choose_color(color_player_2))
        button_window = canvas.create_window(1105, 260, window=color_player_2)  # Position the button at (100, 100)

        button_image_path = r"E:\Python\4InARow\chatframe.png"
        button_image = ImageTk.PhotoImage(Image.open(button_image_path).resize((190, 50)))

        player_vs_mediumbot.pack_forget()

        self.add_exit_button(player_vs_mediumbot, canvas)

        return player_vs_mediumbot

    def player_vs_hardAI(self):
        player_vs_hardbot = tk.Frame(self)
        self.frames["PlayerVsHardBot"] = player_vs_hardbot

        bg_image_path = r"E:\Python\4InARow\player_vs_bot.png"
        # Simplify the background to a solid color for visibility checking
        bg_image = ImageTk.PhotoImage(Image.open(bg_image_path).resize((self.screen_width, self.screen_height)))

        canvas = tk.Canvas(player_vs_hardbot, width=self.screen_width, height=self.screen_height)
        canvas.pack(fill="both", expand=True)

        canvas.create_image(0, 0, image=bg_image, anchor="nw")
        canvas.image = bg_image  # Keep a reference

        button_image_path = r"E:\Python\4InARow\chatframe.png"
        button_image = ImageTk.PhotoImage(Image.open(button_image_path).resize((190, 50)))

        play_button = tk.Button(
            player_vs_hardbot,
            text="Play",
            image=button_image,
            font=("Helvetica", 14),
            compound="center",
            fg="black",
            borderwidth=0,
            relief='flat',
            highlightthickness=0
        )

        play_button.image = button_image
        button_window = canvas.create_window(
            self.screen_width // 2 + 130, self.screen_height - 305,  # Adjust position as needed
            window=play_button
        )

        back_button = tk.Button(
            player_vs_hardbot,
            text="Back",
            image=button_image,
            font=("Helvetica", 14),
            command=lambda: self.show_frame("PlayGame"),
            compound="center",
            fg="black",
            borderwidth=0,
            relief='flat',
            highlightthickness=0
        )

        back_button.image = button_image
        button_window = canvas.create_window(
            self.screen_width // 2 - 130, self.screen_height - 305,  # Adjust position as needed
            window=back_button
        )

        row_select = tk.Spinbox(player_vs_hardbot, from_=6, to=10, wrap=True)
        canvas.create_window(1037, 568, window=row_select)

        column_select = tk.Spinbox(player_vs_hardbot, from_=7, to=13, wrap=True)
        canvas.create_window(1094, 603, window=column_select)

        player1_entry = tk.Entry(player_vs_hardbot)
        player1_entry_window = canvas.create_window(866, 287, window=player1_entry)

        # player2_entry = tk.Entry(player_vs_easyAI)
        # player2_entry_window = canvas.create_window(1166, 287, window=player2_entry)

        self.player1_radiobutton = ttk.Radiobutton(
            player_vs_hardbot,
            variable=self.player_option_var,
            value=1,
            command=self.update_player_selection
        )
        canvas.create_window(935, 680, window=self.player1_radiobutton)

        self.player2_radiobutton = ttk.Radiobutton(
            player_vs_hardbot,
            variable=self.player_option_var,
            value=2,
            command=self.update_player_selection
        )
        canvas.create_window(1180, 680, window=self.player2_radiobutton)

        color_player_1 = tk.Button(player_vs_hardbot, text="    ", bg="white",
                                   command=lambda: self.choose_color(color_player_1))
        button_window = canvas.create_window(805, 260, window=color_player_1)  # Position the button at (100, 100)

        color_player_2 = tk.Button(player_vs_hardbot, text="    ", bg="white",
                                   command=lambda: self.choose_color(color_player_2))
        button_window = canvas.create_window(1105, 260, window=color_player_2)  # Position the button at (100, 100)

        button_image_path = r"E:\Python\4InARow\chatframe.png"
        button_image = ImageTk.PhotoImage(Image.open(button_image_path).resize((190, 50)))

        player_vs_hardbot.pack_forget()

        self.add_exit_button(player_vs_hardbot, canvas)

        return player_vs_hardbot

    def show_frame(self, name):
        print(f"Attempting to show frame: {name}")  # Debug statement
        frame = self.frames[name]
        # Hide all frames first
        for f in self.frames.values():
            f.pack_forget()
        # Show the desired frame
        frame.pack(fill="both", expand=True)
        frame.tkraise()
        print(f"{name} should now be visible.")

    def choose_color(self, button):
        color = colorchooser.askcolor(title="Choose a color")
        if color[1]:  # Check if a color was chosen (user didn't click Cancel)
            button.configure(bg=color[1])  # Set the background color of the button

    def add_exit_button(self, frame, canvas):
        exit_button_image_path = r"E:\Python\4InARow\exit_button.png"
        original_image = Image.open(exit_button_image_path)
        resized_image = original_image.resize((25, 25))  # Resize to 25x25 or size of your choice
        exit_button_image = ImageTk.PhotoImage(resized_image)

        exit_button = tk.Button(
            frame,
            image=exit_button_image,
            command=self.close_application,
            borderwidth=0,
            highlightthickness=0,
            bg='white',
            activebackground='white'
        )
        exit_button.image = exit_button_image  # Keep a reference
        exit_button_window = canvas.create_window(
            self.screen_width - 1,  # X position - Adjust as needed
            1,  # Y position - Adjust as needed
            anchor="ne",
            window=exit_button
        )

    def close_application(self):
        # This method will be called when the exit button is clicked
        self.destroy()  # This will close the application


if __name__ == "__main__":
    app = MainFrame()
    app.mainloop()

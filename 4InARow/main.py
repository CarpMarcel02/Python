import tkinter as tk
from tkinter import colorchooser, ttk
from tkinter import messagebox
import random

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
        self.bot_plays_first = 0
        self.result_label = tk.Label(self, text="", font=("Helvetica", 20))

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
                self.player_option_var.get(), player1_entry.get(), player2_entry.get()
            )
        )
        play_button.image = button_image
        button_window = canvas.create_window(
            self.screen_width // 2 + 130, self.screen_height - 305,  # Adjust position as needed
            window=play_button
        )

        return player_vs_player_frame

    def start_game(self, player1_color, player2_color, player1_name, player2_name, rows, columns, player1_is_checked,
                   player1_entry, player2_entry):
        self.wait = 0
        if player1_entry == "":
            player1_entry = "Player 1"
        if player2_entry == "":
            player2_entry = "Player 2"
        # Always create a new game interface when starting a new game.
        if "GameInterface" in self.frames:
            self.frames["GameInterface"].destroy()
            del self.frames["GameInterface"]  # Ensure the reference is deleted.

        # Now, create a new game interface frame.
        self.create_game_interface(player1_color, player2_color, player1_name, player2_name, rows, columns,
                                   player1_is_checked, player1_entry, player2_entry)

        # if player2_name == "Bot_Hard" or player2_name == "Bot_Medium" or player2_name == "Bot_Easy" :
        #     self.current_player = 0
        print("ciocolata Albastra")
        print(player1_is_checked)


        self.show_frame("GameInterface")
        if player1_is_checked == 1:
            self.current_player = 1
        else:
            if player1_is_checked == 2 and player2_entry !="Bot_Easy" and player2_entry !="Bot_Medium" and player2_entry !="Bot_Hard":
                self.current_player = 2
            else:
                self.current_player = 0
                self.bot_plays_first = 1
                self.animate_button_change(self.rows, 0, self.rows, player2_color, player1_color, player2_color,
                                           player1_entry, player2_entry)

    def handle_button_click(self, row, col, player1_color, player2_color, player1_entry, player2_entry):
        if self.wait == 0:
            #print("Aici ma blochez")
            current_button = self.game_buttons[row][col]
            if player1_color == 'white':
                player1_color = 'yellow'
            if player2_color == 'white':
                player2_color = 'red'
            #print("Aici ma blochez")

            copy_row = row
            copy_collumn = col
            if current_button['bg'] == 'white':  # Check if the button hasn't been clicked
                if self.current_player == 1:
                    current_color = player1_color
                else:
                    current_color = player2_color
                #print("Aici ma blochez")

                self.game_buttons[row][col]['bg'] = 'white'


                print(f"apelez functia cu {row}{col}")

                self.animate_button_change(row, col, row, current_color, player1_color, player2_color, player1_entry,
                                           player2_entry)

    def animate_button_change(self, row, col, initial_row, current_color, player1_color, player2_color, player1_entry,
                              player2_entry, delay=100):
        if  (row >= self.rows or self.game_buttons[row][col]['bg'] != 'white') or self.bot_plays_first == 1:  # cand a cazut culoarea pe ultima casuta


            self.wait = 0
            if self.bot_plays_first == 0:
                self.switch_player_turn()
            over = 0
            winner = 0
            winner = self.player_has_won(player1_color, player2_color)
            message = ""
            if winner == 1:
                over = 1
                message = f"{player1_entry} has won!"  # Assuming player1_entry is a tk.Entry widget
            elif winner == 2:
                over = 1
                message = f"{player2_entry} has won!"  # Assuming player2_entry is a tk.Entry widget
            elif winner == 3:
                over = 1
                message = "Game is draw"
            if over == 1:
                button_image_path = r"E:\Python\4InARow\chatframe.png"
                button_image = ImageTk.PhotoImage(Image.open(button_image_path).resize((190, 50)))
                back_button = tk.Button(
                    self,
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
                back_button.place(relx=0.5, rely=0.1, anchor="n")
                back_button.lift()
                self.result_label.config(text=message, fg="green", bg="white")
                self.result_label.config(width=20, height=2)
                self.update_idletasks()  # Update the geometry of the window
                self.result_label.lift()
                self.update()
                self.result_label.place(relx=0.5, rely=0, anchor="n")  # Place label at the top center of the window
                for row_buttons in self.game_buttons:
                    for button in row_buttons:
                        button.config(state=tk.DISABLED)
                        button.unbind('<Button-1>')

            if (self.current_player == 2 and player2_entry == "Bot_Easy" and winner == 0) or self.bot_plays_first == 1 :
                    if self.bot_plays_first == 1:
                        self.bot_plays_first = 0
                        self.handle_button_click(0, (self.collumns - 1) // 2, player1_color, player2_color,
                                                 player1_entry,
                                                 player2_entry)

                    random_number = random.randint(0, self.collumns - 1)
                    if self.game_buttons[0][random_number]['bg'] != "white":
                        random_number = random.randint(0, self.collumns - 1)
                        print("am fost aici icsde")

                        while self.game_buttons[0][random_number]['bg'] != "white":
                            print("am fost aici xD")
                            random_number = random.randint(0, self.collumns - 1)

                    print(random_number)
                    current_color = player2_color
                    self.handle_button_click(0, random_number, player1_color, player2_color, player1_entry,
                                               player2_entry)
            if (self.current_player == 2 and player2_entry == "Bot_Medium" and winner == 0) or self.bot_plays_first == 1:
                    if self.bot_plays_first == 1:
                        self.bot_plays_first = 0
                        self.handle_button_click(0, (self.collumns - 1) // 2, player1_color, player2_color,
                                                 player1_entry,
                                                 player2_entry)
                    for i in range(self.rows):  # in caz de botul poate castiga
                        for j in range(self.collumns):
                            if i - 1 > -1:  # in caz de are situatie de win fix deasupra lui gen pe coloana
                                if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i - 1][j][
                                    'bg'] == player2_color and self.game_buttons[i - 2][j]['bg'] == player2_color and \
                                        self.game_buttons[i - 3][j]['bg'] == "white":
                                    print("botul castiga prin alegerea de a plasa deasupra pe coloana")
                                    self.handle_button_click(0, j, player1_color, player2_color,
                                                             player1_entry,
                                                             player2_entry)
                            if i == self.rows - 1 and j + 3 < self.collumns:  # in caz de are situatie de win pe dreapta si e ultima linie gen
                                if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i][j + 1][
                                    'bg'] == player2_color and self.game_buttons[i][j + 2]['bg'] == player2_color and \
                                        self.game_buttons[i][j + 3]['bg'] == "white":
                                    print("botul castiga prin alegerea la dreapta pe linia cea mai dejos")
                                    self.handle_button_click(0, j + 3, player1_color, player2_color,
                                                             player1_entry,
                                                             player2_entry)
                            if i != self.rows - 1 and j + 3 < self.collumns:  # in caz de are situatie de win pe dreapta si nu e ultima linie gen
                                if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i][j + 1][
                                    'bg'] == player2_color and self.game_buttons[i][j + 2]['bg'] == player2_color and \
                                        self.game_buttons[i][j + 3]['bg'] == "white" and \
                                        self.game_buttons[i + 1][j + 3]['bg'] != "white":
                                    print("botul castiga prin alegerea la dreapta dar nu e linia de jos")
                                    self.handle_button_click(0, j + 3, player1_color, player2_color,
                                                             player1_entry,
                                                             player2_entry)
                            if i == self.rows - 1 and j - 3 > -1:  # in caz de are situatie de win pe dreapta si nu e ultima linie gen
                                if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i][j - 1][
                                    'bg'] == player2_color and self.game_buttons[i][j - 2]['bg'] == player2_color and \
                                        self.game_buttons[i][j - 3]['bg'] == "white":
                                    print("botul castiga prin alegerea la stanga dar  e si pee linia de jos")
                                    self.handle_button_click(0, j - 3, player1_color, player2_color,
                                                             player1_entry,
                                                             player2_entry)
                            if i != self.rows - 1 and j - 3 > -1:  # in caz de are situatie de win pe dreapta si nu e ultima linie gen
                                if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i][j - 1][
                                    'bg'] == player2_color and self.game_buttons[i][j - 2]['bg'] == player2_color and \
                                        self.game_buttons[i][j - 3]['bg'] == "white" and \
                                        self.game_buttons[i + 1][j - 3]['bg'] != "white":
                                    print("botul castiga prin alegerea la dreapta dar nu e linia de jos")
                                    self.handle_button_click(0, j - 3, player1_color, player2_color,
                                                             player1_entry,
                                                             player2_entry)
                            if i - 3 > -1 and j + 3 < self.collumns:  # in cazz de castiga pe diagonala secundara
                                if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i - 1][j + 1][
                                    'bg'] == player2_color and self.game_buttons[i - 2][j + 2][
                                    'bg'] == player2_color and self.game_buttons[i - 3][j + 3]['bg'] == "white" and \
                                        self.game_buttons[i - 1][j + 2]['bg'] != "white":
                                    print("botul castiga prin alegerea la diagonala secundara")
                                    self.handle_button_click(0, j + 3, player1_color, player2_color,
                                                             player1_entry,
                                                             player2_entry)
                            if i - 3 > -1 and j - 3 > -1:  # in cazz de castiga pe diagonala principala
                                if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i - 1][j - 1][
                                    'bg'] == player2_color and self.game_buttons[i - 2][j - 2][
                                    'bg'] == player2_color and self.game_buttons[i - 3][j - 3]['bg'] == "white" and \
                                        self.game_buttons[i - 2][j - 3]['bg'] != "white":
                                    print("botul castiga prin alegerea la diagonala principala")
                                    self.handle_button_click(0, j - 3, player1_color, player2_color,
                                                             player1_entry,
                                                             player2_entry)
                    for i in range(self.rows):  # in caz de botul poate bloca inamicul sa castigee
                        for j in range(self.collumns):
                            if i - 1 > -1:  # in caz de poate bloca inamicu de a pune 4 pe o coloana
                                if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i - 1][j][
                                    'bg'] == player1_color and self.game_buttons[i - 2][j]['bg'] == player1_color and \
                                        self.game_buttons[i - 3][j]['bg'] == "white":
                                    print("botul blocheaza prin alegerea de a plasa deasupra pe coloana")
                                    self.handle_button_click(0, j, player1_color, player2_color,
                                                             player1_entry,
                                                             player2_entry)
                            if i == self.rows - 1 and j + 3 < self.collumns:  # in caz de are situatie de blocaj pe dreapta si e ultima linie gen
                                if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i][j + 1][
                                    'bg'] == player1_color and self.game_buttons[i][j + 2]['bg'] == player1_color and \
                                        self.game_buttons[i][j + 3]['bg'] == "white":
                                    print("botul blocheaza prin alegerea la dreapta pe linia cea mai dejos")
                                    self.handle_button_click(0, j + 3, player1_color, player2_color,
                                                             player1_entry,
                                                             player2_entry)
                            if i != self.rows - 1 and j + 3 < self.collumns:  # in caz de are situatie de blocaj pe dreapta si nu e ultima linie gen
                                if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i][j + 1][
                                    'bg'] == player1_color and self.game_buttons[i][j + 2]['bg'] == player1_color and \
                                        self.game_buttons[i][j + 3]['bg'] == "white" and \
                                        self.game_buttons[i + 1][j + 3]['bg'] != "white":
                                    print("botul blocheaza prin alegerea la dreapta dar nu e linia de jos")
                                    self.handle_button_click(0, j + 3, player1_color, player2_color,
                                                             player1_entry,
                                                             player2_entry)
                            if i == self.rows - 1 and j - 3 > -1:  # in caz de are situatie de blocaj pe dreapta si nu e ultima linie gen
                                if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i][j - 1][
                                    'bg'] == player1_color and self.game_buttons[i][j - 2]['bg'] == player1_color and \
                                        self.game_buttons[i][j - 3]['bg'] == "white":
                                    print("botul blocheaza prin alegerea la stanga dar  e si pee linia de jos")
                                    self.handle_button_click(0, j - 3, player1_color, player2_color,
                                                             player1_entry,
                                                             player2_entry)
                            if i != self.rows - 1 and j - 3 > -1:  # in caz de are situatie de blocaj pe dreapta si nu e ultima linie gen
                                if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i][j - 1][
                                    'bg'] == player1_color and self.game_buttons[i][j - 2]['bg'] == player1_color and \
                                        self.game_buttons[i][j - 3]['bg'] == "white" and \
                                        self.game_buttons[i + 1][j - 3]['bg'] != "white":
                                    print("botul blocheaza prin alegerea la dreapta dar nu e linia de jos")
                                    self.handle_button_click(0, j - 3, player1_color, player2_color,
                                                             player1_entry,
                                                             player2_entry)
                            if i == self.rows - 1 and j - 3 > -1:  # in caz pe ultima linie la inamic ii lipseste o patratica mai exact a doua
                                if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i][j - 1]['bg'] == "white" and self.game_buttons[i][j - 2]['bg'] == player1_color and self.game_buttons[i][j - 3]['bg'] == player1_color:
                                    print("botul blocheaza punand pe a doua pozitie unde ii lipseste inamicului")
                                    self.handle_button_click(0, j - 1, player1_color, player2_color, player1_entry,
                                                             player2_entry)
                            if i == self.rows - 1 and j - 3 > -1:  # in caz de pe fix ultima linie si lipseste penultima bucata pentru a face blbocaj
                                if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i][j - 1]['bg'] == player1_color and self.game_buttons[i][j - 2]['bg'] == "white" and self.game_buttons[i][j - 3]['bg'] == player1_color:
                                    print("botul blocheaza punand pe a treia pozitie unde ii lipseste inamicului")

                                    self.handle_button_click(0, j - 2, player1_color, player2_color,
                                                             player1_entry,
                                                             player2_entry)
                            if i - 3 > -1 and j + 3 < self.collumns:  # in cazz de blocaj pe diagonala secundara
                                if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i - 1][j + 1]['bg'] == player1_color and self.game_buttons[i - 2][j + 2]['bg'] == player1_color and self.game_buttons[i - 3][j + 3]['bg'] == "white" and self.game_buttons[i - 2][j + 3]['bg'] != "white":
                                    print("botul blocheaza prin alegerea la diagonala secundara")
                                    self.handle_button_click(0, j + 3, player1_color, player2_color,
                                                             player1_entry,
                                                             player2_entry)
                            if i - 3 > -1 and j - 3 > -1:  # in cazz de blocaj pe diagonala principala
                                if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i - 1][j - 1][
                                    'bg'] == player1_color and self.game_buttons[i - 2][j - 2][
                                    'bg'] == player1_color and self.game_buttons[i - 3][j - 3]['bg'] == "white" and \
                                        self.game_buttons[i - 2][j - 3]['bg'] != "white":
                                    print("botul blocheaza prin alegerea la diagonala principala")
                                    self.handle_button_click(0, j - 3, player1_color, player2_color,
                                                             player1_entry,
                                                             player2_entry)
                    for i in range(self.rows):  #a 3 a piesa
                        for j in range(self.collumns):
                            if self.game_buttons[i][j]['bg'] == player2_color:
                                count = 1
                                if i + 1 < self.rows and i + 2 < self.rows:  # coloana sus
                                    if self.game_buttons[i + 1][j]['bg'] == player2_color and \
                                            self.game_buttons[i + 2][j][
                                                'bg'] == "white":  ## nus sterg nik pan aciic
                                        count += 2
                                    if count == 3:
                                        if self.game_buttons[i - 2][j]['bg'] == "white":
                                            self.handle_button_click(0, j, player1_color, player2_color,
                                                                     player1_entry, player2_entry)

                                if j + 1 < self.collumns and j + 2 < self.collumns:  # linie si tre sa fac si de la stanga la dreapta si dreapta la stanga
                                    if self.game_buttons[i][j + 1]['bg'] == player2_color and \
                                            self.game_buttons[i][j + 2]['bg'] == "white":
                                        count += 2
                                    if count == 3:
                                        if i + 1 < self.rows :
                                            if self.game_buttons[i + 1][j + 2]['bg'] != "white":  # la dreapta
                                                self.handle_button_click(0, j + 2, player1_color, player2_color,
                                                                         player1_entry, player2_entry)
                                        if j - 1 > -1 and i + 1 < self.rows:
                                            if self.game_buttons[i + 1][j - 1]['bg'] != "white":  # la sttanga
                                                self.handle_button_click(0, j - 1, player1_color, player2_color,
                                                                         player1_entry, player2_entry)

                                if i - 1 > -1 and j - 1 > -1 and i - 2 < -1 and j - 2 > -1:  # diagonala  principala
                                    if self.game_buttons[i - 1][j - 1]['bg'] == player2_color:
                                        count += 2
                                    if count == 3:
                                        if self.game_buttons[i - 1][j - 3]['bg'] != "white":  # self.game_buttons[i][j+1]['bg'] != "white" and#
                                            self.handle_button_click(0, j - 3, player1_color, player2_color,
                                                                     player1_entry,
                                                                     player2_entry)
                                if i - 1 > -1 and j + 1 < self.collumns and i - 2 > -1 and j + 2 < self.collumns:  # diagonala secundara
                                    if self.game_buttons[i - 1][j + 1]['bg'] == player2_color:
                                        count += 2
                                    if count == 3:
                                        if self.game_buttons[i - 1][j + 2]['bg'] != "white":
                                            self.handle_button_click(0, j + 2, player1_color, player2_color,
                                                                     player1_entry,
                                                                     player2_entry)
                    random_number = random.randint(0, self.collumns - 1)
                    if self.game_buttons[0][random_number]['bg'] != "white":
                        random_number = random.randint(0, self.collumns - 1)
                        while self.game_buttons[0][random_number]['bg'] != "white":
                            random_number = random.randint(0, self.collumns - 1)


                    current_color = player2_color
                    self.handle_button_click(0, random_number, player1_color, player2_color, player1_entry,
                                             player2_entry)
            if (self.current_player == 2 and player2_entry == "Bot_Hard" and winner == 0) or self.bot_plays_first == 1:
                print("Bot_HARD")
                if  self.bot_plays_first == 1:
                    self.bot_plays_first = 0
                    self.handle_button_click(0, (self.collumns - 1) // 2, player1_color, player2_color,
                                             player1_entry,
                                             player2_entry)

                for i in range(self.rows): # in caz de botul poate castiga punand pe ultima linie piesa
                    for j in range(self.collumns):
                        if  i - 1 > -1:  # in caz de are situatie de win fix deasupra lui gen pe coloana
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i - 1][j]['bg'] == player2_color and self.game_buttons[i - 2][j]['bg'] == player2_color and self.game_buttons[i - 3][j]['bg'] == "white":
                                print("botul castiga prin alegerea de a plasa deasupra pe coloana")
                                self.handle_button_click(0, j, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i == self.rows - 1 and j + 3 < self.collumns: # in caz de are situatie de win pe dreapta si e ultima linie gen
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i][j + 1]['bg'] == player2_color and self.game_buttons[i][j + 2]['bg'] == player2_color and self.game_buttons[i][j + 3]['bg'] == "white":
                                print("botul castiga prin alegerea la dreapta pe linia cea mai dejos")
                                self.handle_button_click(0, j + 3, player1_color, player2_color,
                                                         player1_entry,
                                                        player2_entry)
                        if i != self.rows - 1 and j + 3 < self.collumns:  # in caz de are situatie de win pe dreapta si nu e ultima linie gen
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i][j + 1]['bg'] == player2_color and self.game_buttons[i][j + 2]['bg'] == player2_color and self.game_buttons[i][j + 3]['bg'] == "white" and self.game_buttons[i + 1][j + 3]['bg'] != "white":
                                print("botul castiga prin alegerea la dreapta dar nu e linia de jos")
                                self.handle_button_click(0, j + 3, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i == self.rows - 1 and j - 3 > -1:  # in caz de are situatie de win pe stanga si  e ultima linie gen
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i][j - 1]['bg'] == player2_color and self.game_buttons[i][j - 2]['bg'] == player2_color and self.game_buttons[i][j - 3]['bg'] == "white":
                                print("botul castiga prin alegerea la stanga dar  e si pee linia de jos")
                                self.handle_button_click(0, j - 3, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i != self.rows - 1 and j - 3 > -1:  # in caz de are situatie de win pe stanga si nu e ultima linie gen
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i][j - 1]['bg'] == player2_color and self.game_buttons[i][j - 2]['bg'] == player2_color and self.game_buttons[i][j - 3]['bg'] == "white" and self.game_buttons[i + 1][j - 3]['bg'] != "white":
                                print("botul castiga prin alegerea la dreapta dar nu e linia de jos")
                                self.handle_button_click(0, j - 3, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 3 > -1 and j + 3 < self.collumns: # in cazz de castiga pe diagonala secundara
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i-1][j+1]['bg'] == player2_color and self.game_buttons[i-2][j+2]['bg'] == player2_color and self.game_buttons[i-3][j+3]['bg'] == "white" and  self.game_buttons[i-1][j+2]['bg'] != "white":
                                print("botul castiga prin alegerea la diagonala secundara")
                                self.handle_button_click(0, j + 3, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 3 > -1 and j - 3 > -1: # in cazz de castiga pe diagonala principala
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i-1][j-1]['bg'] == player2_color and self.game_buttons[i-2][j-2]['bg'] == player2_color and self.game_buttons[i-3][j-3]['bg'] == "white" and  self.game_buttons[i-2][j-3]['bg'] != "white":
                                print("botul castiga prin alegerea la diagonala principala")
                                self.handle_button_click(0, j - 3, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                for i in range(self.rows): # in caz de botul poate castiga daca ii lipseste o piesa pe a 3-a pozitie
                    for j in range(self.collumns):
                        if i != self.rows - 1 and j + 3 < self.collumns:  # in caz de are situatie de win pe dreapta si nu e ultima linie gen si doar a 3 treia piesa lipseste
                             if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i][j + 1]['bg'] == player2_color and self.game_buttons[i][j + 2]['bg'] == "white" and self.game_buttons[i][j + 3]['bg'] == player2_color and self.game_buttons[i + 1][j + 2]['bg'] != "white":
                                print("botul castiga prin alegerea la dreapta dar nu e linia de jos fix dupa 2 patratteele")
                                self.handle_button_click(0, j + 2, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i != self.rows - 1 and j - 3 > -1:  # in caz de are situatie de win pe stanga si nu e ultima linie gen
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i][j - 1]['bg'] == player2_color and self.game_buttons[i][j - 2]['bg'] == "white" and self.game_buttons[i][j - 3]['bg'] == player2_color and self.game_buttons[i + 1][j - 2]['bg'] != "white":
                                print("botul castiga prin alegerea la dreapta dar nu e linia de jos fix dupa 2 patratteele")
                                self.handle_button_click(0, j - 2, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)

                        if i - 3 > -1 and j + 3 < self.collumns: # in cazz de castiga pe diagonala secundara
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i-1][j+1]['bg'] == player2_color and self.game_buttons[i-2][j+2]['bg'] == "white" and self.game_buttons[i-3][j+3]['bg'] == player2_color and  self.game_buttons[i-1][j+2]['bg'] != "white":
                                print("botul castiga prin alegerea la diagonala secundara fix dupa 2 patratteele")
                                self.handle_button_click(0, j - 2, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 3 > -1 and j - 3 > -1: # in cazz de castiga pe diagonala principala
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i-1][j-1]['bg'] == player2_color and self.game_buttons[i-2][j-2]['bg'] == "white" and self.game_buttons[i-3][j-3]['bg'] == player2_color and  self.game_buttons[i-1][j-2]['bg'] != "white":
                                print("botul castiga prin alegerea la diagonala principala fix dupa 2 patratteele")
                                self.handle_button_click(0, j - 3, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                for i in range(self.rows): # in caz de botul poate castiga daca ii lipseste o piesa pe a 2-a pozitie
                    for j in range(self.collumns):
                        if i != self.rows - 1 and j + 3 < self.collumns:  # in caz de are situatie de win pe dreapta si nu e ultima linie gen si doar a 3 treia piesa lipseste
                             if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i][j + 1]['bg'] == "white" and self.game_buttons[i][j + 2]['bg'] == player2_color and self.game_buttons[i][j + 3]['bg'] == player2_color and self.game_buttons[i + 1][j + 1]['bg'] != "white":
                                print("botul castiga prin alegerea la dreapta cu o patratica dar nu e linia de jos")
                                self.handle_button_click(0, j + 1, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i != self.rows - 1 and j - 3 > -1:  # in caz de are situatie de win pe stanga si nu e ultima linie gen
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i][j - 1]['bg'] == "white" and self.game_buttons[i][j - 2]['bg'] == player2_color and self.game_buttons[i][j - 3]['bg'] == player2_color and self.game_buttons[i + 1][j - 1]['bg'] != "white":
                                print("botul castiga prin alegerea la stanga  cu o patratica dar nu e linia de jos")
                                self.handle_button_click(0, j - 1, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 3 > -1 and j + 3 < self.collumns: # in cazz de castiga pe diagonala secundara
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i-1][j+1]['bg'] == "white" and self.game_buttons[i-2][j+2]['bg'] == player2_color and self.game_buttons[i-3][j+3]['bg'] == player2_color and  self.game_buttons[i][j+1]['bg'] != "white":
                                print("botul castiga prin alegerea la diagonala secundara fix urmatorea patratica")
                                self.handle_button_click(0, j + 1, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 3 > -1 and j - 3 > -1: # in cazz de castiga pe diagonala principala
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i-1][j-1]['bg'] == "white" and self.game_buttons[i-2][j-2]['bg'] == player2_color and self.game_buttons[i-3][j-3]['bg'] == player2_color and  self.game_buttons[i][j-1]['bg'] != "white":
                                print("botul castiga prin alegerea la diagonala principala fix urmatorea patratica")
                                self.handle_button_click(0, j - 1, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                for i in range(self.rows):  # in caz de botul poate castiga daca ii lipseste prima piesa dintr- diagonala
                    for j in range(self.collumns):
                        if i - 2 > -1 and j + 2 < self.collumns and i + 1 < self.rows and j - 1 > -1 and i + 1 != self.rows:  # diagonala secundara
                            if self.game_buttons[i][j]['bg'] == player2_color  and self.game_buttons[i - 1][j + 1][
                                'bg'] == player2_color and self.game_buttons[i - 2][j + 2]['bg'] == player2_color and \
                                    self.game_buttons[i + 1][j - 1]['bg'] == "white" and \
                                    self.game_buttons[i + 2][j - 1]['bg'] != "white":
                                print(" puune prima bucata din diagonala secundara dar nu e primma bucata nu e pe prima linie")
                                self.handle_button_click(0, j - 1, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 2 > -1 and j + 2 < self.collumns and i + 1 < self.rows and j - 1 > -1 and i + 1 == self.rows:  # diagonala secundara
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i - 1][j + 1][
                                'bg'] == player2_color and self.game_buttons[i - 2][j + 2]['bg'] == player2_color and \
                                    self.game_buttons[i + 1][j - 1]['bg'] == "white":
                                print(
                                    " puune prima bucata din diagonala secundara dar nu e primma bucata este pe prima linie")
                                self.handle_button_click(0, j - 1, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 2 > -1 and j - 2 > -1 and i + 1 < self.rows and j + 1 < self.collumns and i + 1 == self.rows:  ## diagoanala principala si singuru care lipseste e pe ultima linie
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i - 1][j - 1][
                                'bg'] == player2_color and self.game_buttons[i - 2][j - 2]['bg'] == player2_color and \
                                    self.game_buttons[i + 1][j + 1]['bg'] == "white":
                                print(
                                    " puune prima bucata din diagonala principala si primma bucata este pe prima linie gen")
                                self.handle_button_click(0, j + 1, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 2 > -1 and j - 2 > -1 and i + 1 < self.rows and j + 1 < self.collumns and i + 1 != self.rows:  ## diagoanala principala si singuru care lipseste e pe ultima linie
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i - 1][j - 1][
                                'bg'] == player2_color and self.game_buttons[i - 2][j - 2]['bg'] == player2_color and \
                                    self.game_buttons[i + 1][j + 1]['bg'] == "white" and \
                                    self.game_buttons[i + 2][j + 1]['bg'] != "white":
                                print(
                                    " puune prima bucata din diagonala principala si primma bucata este pe prima linie gen")
                                self.handle_button_click(0, j + 1, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)

                for i in range(self.rows): # in caz de botul poate bloca inamicul sa castigee
                    for j in range(self.collumns):
                        if  i - 1 > -1:  # in caz de poate bloca inamicu de a pune 4 pe o coloana
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i - 1][j]['bg'] == player1_color and self.game_buttons[i - 2][j]['bg'] == player1_color and self.game_buttons[i - 3][j]['bg'] == "white":
                                print("botul blocheaza prin alegerea de a plasa deasupra pe coloana")
                                self.handle_button_click(0, j, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i == self.rows - 1 and j + 3 < self.collumns: # in caz de are situatie de blocaj pe dreapta si e ultima linie gen
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i][j + 1]['bg'] == player1_color and self.game_buttons[i][j + 2]['bg'] == player1_color and self.game_buttons[i][j + 3]['bg'] == "white":
                                print("botul blocheaza prin alegerea la dreapta pe linia cea mai dejos")
                                self.handle_button_click(0, j + 3, player1_color, player2_color,
                                                         player1_entry,
                                                        player2_entry)
                        if i != self.rows - 1 and j + 3 < self.collumns:  # in caz de are situatie de blocaj pe dreapta si nu e ultima linie gen
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i][j + 1]['bg'] == player1_color and self.game_buttons[i][j + 2]['bg'] == player1_color and self.game_buttons[i][j + 3]['bg'] == "white" and self.game_buttons[i + 1][j + 3]['bg'] != "white":
                                print("botul blocheaza prin alegerea la dreapta dar nu e linia de jos")
                                self.handle_button_click(0, j + 3, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i == self.rows - 1 and j - 3 > -1:  # in caz de are situatie de blocaj pe dreapta si nu e ultima linie gen
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i][j - 1]['bg'] == player1_color and self.game_buttons[i][j - 2]['bg'] == player1_color and self.game_buttons[i][j - 3]['bg'] == "white":
                                print("botul blocheaza prin alegerea la stanga dar  e si pee linia de jos")
                                self.handle_button_click(0, j - 3, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i != self.rows - 1 and j - 3 > -1:  # in caz de are situatie de blocaj pe dreapta si nu e ultima linie gen
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i][j - 1]['bg'] == player1_color and self.game_buttons[i][j - 2]['bg'] == player1_color and self.game_buttons[i][j - 3]['bg'] == "white" and self.game_buttons[i + 1][j - 3]['bg'] != "white":
                                print("botul blocheaza prin alegerea la dreapta dar nu e linia de jos")
                                self.handle_button_click(0, j - 3, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 3 > -1 and j + 3 < self.collumns: # in cazz de blocaj pe diagonala secundara
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i - 1][j + 1]['bg'] == player1_color and self.game_buttons[i - 2][j + 2]['bg'] == player1_color and self.game_buttons[i - 3][j + 3]['bg'] == "white" and self.game_buttons[i - 2][j + 3]['bg'] != "white":
                                print("botul blocheaza prin alegerea la diagonala secundara")
                                self.handle_button_click(0, j + 3, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 3 > -1 and j - 3 > -1: # in cazz de blocaj pe diagonala principala
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i-1][j-1]['bg'] == player1_color and self.game_buttons[i-2][j-2]['bg'] == player1_color and self.game_buttons[i-3][j-3]['bg'] == "white" and  self.game_buttons[i-2][j-3]['bg'] != "white":
                                print("botul blocheaza prin alegerea la diagonala principala")
                                self.handle_button_click(0, j - 3, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                for i in range(self.rows): # in caz de botul poate bloca daca inamicului ii lipseste o piesa doar de pe a 3-a pozitie, nu ultima
                    for j in range(self.collumns):
                        if i != self.rows - 1 and j + 3 < self.collumns:  # in caz de are situatie de win pe dreapta si nu e ultima linie gen si doar a 3 treia piesa lipseste
                             if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i][j + 1]['bg'] == player1_color and self.game_buttons[i][j + 2]['bg'] == "white" and self.game_buttons[i][j + 3]['bg'] == player1_color and self.game_buttons[i + 1][j + 2]['bg'] != "white":
                                print("botul blocheaza prin alegerea la dreapta dar nu e linia de jos fix dupa 2 patratteele")
                                self.handle_button_click(0, j + 2, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i != self.rows - 1 and j - 3 > -1:  # in caz de are situatie de win pe stanga si nu e ultima linie gen
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i][j - 1]['bg'] == player1_color and self.game_buttons[i][j - 2]['bg'] == "white" and self.game_buttons[i][j - 3]['bg'] == player1_color and self.game_buttons[i + 1][j - 2]['bg'] != "white":
                                print("botul blocheaza prin alegerea la dreapta dar nu e linia de jos fix dupa 2 patratteele")
                                self.handle_button_click(0, j - 2, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i == self.rows - 1 and j - 3 > -1: # in caz de pe fix ultima linie si lipseste 1 bucata si trebuie sa blocheze
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i][j - 1]['bg'] == player1_color and self.game_buttons[i][j - 2]['bg'] == "white" and self.game_buttons[i][j - 3]['bg'] == player1_color :
                                self.handle_button_click(0, j - 2, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 3 > -1 and j + 3 < self.collumns: # in cazz de castiga pe diagonala secundara
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i-1][j+1]['bg'] == player1_color and self.game_buttons[i-2][j+2]['bg'] == "white" and self.game_buttons[i-3][j+3]['bg'] == player1_color and  self.game_buttons[i-1][j+2]['bg'] != "white":
                                print("botul blocheaza prin alegerea la diagonala secundara fix dupa 2 patratteele")
                                self.handle_button_click(0, j - 2, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 3 > -1 and j - 3 > -1: # in cazz de castiga pe diagonala principala
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i-1][j-1]['bg'] == player1_color and self.game_buttons[i-2][j-2]['bg'] == "white" and self.game_buttons[i-3][j-3]['bg'] == player1_color and  self.game_buttons[i-1][j-2]['bg'] != "white":
                                print("botul blocheaza prin alegerea la diagonala principala fix dupa 2 patratteele")
                                self.handle_button_click(0, j - 3, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)

                for i in range(self.rows): # in caz de botul poate bloca inamicul daca ii lipseste o piesa de pe a doua pozitie
                    for j in range(self.collumns):
                        if i != self.rows - 1 and j + 3 < self.collumns:  # in caz de are situatie de win pe dreapta si nu e ultima linie gen si doar a 3 treia piesa lipseste
                             if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i][j + 1]['bg'] == "white" and self.game_buttons[i][j + 2]['bg'] == player1_color and self.game_buttons[i][j + 3]['bg'] == player1_color and self.game_buttons[i + 1][j + 1]['bg'] != "white":
                                print("botul bloecheaza prin alegerea la dreapta cu o patratica dar nu e linia de jos")
                                self.handle_button_click(0, j + 1, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i != self.rows - 1 and j - 3 > -1:  # in caz de are situatie de win pe stanga si nu e ultima linie gen
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i][j - 1]['bg'] == "white" and self.game_buttons[i][j - 2]['bg'] == player1_color and self.game_buttons[i][j - 3]['bg'] == player1_color and self.game_buttons[i + 1][j - 1]['bg'] != "white":
                                print("botul bloecheaza prin alegerea la stanga  cu o patratica dar nu e linia de jos")
                                self.handle_button_click(0, j - 1, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i == self.rows - 1 and j - 3 > -1: # in caz pe ultima linie la inamic ii lipseste o patratica mai exact a doua
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i][j - 1]['bg'] == "white" and self.game_buttons[i][j - 2]['bg'] == player1_color and self.game_buttons[i][j - 3]['bg'] == player1_color :
                                self.handle_button_click(0, j - 1, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 3 > -1 and j + 3 < self.collumns: # in cazz de castiga pe diagonala secundara
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i-1][j+1]['bg'] == "white" and self.game_buttons[i-2][j+2]['bg'] == player1_color and self.game_buttons[i-3][j+3]['bg'] == player1_color and  self.game_buttons[i][j+1]['bg'] != "white":
                                print("botul bloecheaza prin alegerea la diagonala secundara fix urmatorea patratica")
                                self.handle_button_click(0, j + 1, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 3 > -1 and j - 3 > -1: # in cazz de castiga pe diagonala principala
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i-1][j-1]['bg'] == "white" and self.game_buttons[i-2][j-2]['bg'] == player1_color and self.game_buttons[i-3][j-3]['bg'] == player1_color and  self.game_buttons[i][j-1]['bg'] != "white":
                                print("botul bloecheaza prin alegerea la diagonala principala fix urmatorea patratica")
                                self.handle_button_click(0, j - 1, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                for i in range(self.rows):  # in caz de botul poate bloca daca inamicului ii lipseste prima piesa dintr- diagonala
                    for j in range(self.collumns):
                        if i - 2 > -1 and j + 2 < self.collumns and i + 2 < self.rows and j - 1 > -1 and i+2 !=self.rows: # diagonala secundara
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i - 1][j + 1]['bg'] == player1_color and self.game_buttons[i - 2][j + 2]['bg'] == player1_color and self.game_buttons[i + 1][j - 1]['bg'] == "white" and self.game_buttons[i + 2][j - 1]['bg'] != "white":
                                    print(" puune prima bucata din diagonala secundara dar nu e primma bucata nu e pe prima linie")
                                    self.handle_button_click(0, j - 1, player1_color, player2_color,
                                                             player1_entry,
                                                             player2_entry)
                        if i - 2 > -1 and j + 2 < self.collumns and i + 1 < self.rows and j - 1 > -1 and i+1 ==self.rows: # diagonala secundara
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i - 1][j + 1]['bg'] == player1_color and self.game_buttons[i - 2][j + 2]['bg'] == player1_color and self.game_buttons[i + 1][j - 1]['bg'] == "white" :
                                    print(" puune prima bucata din diagonala secundara dar nu e primma bucata este pe prima linie")
                                    self.handle_button_click(0, j - 1, player1_color, player2_color,
                                                             player1_entry,
                                                             player2_entry)
                        if i - 2 > -1 and j - 2 > -1 and i + 1 < self.rows and j + 1 < self.collumns and i+1 == self.rows:## diagoanala principala si singuru care lipseste e pe ultima linie
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i - 1][j - 1]['bg'] == player1_color and self.game_buttons[i - 2][j - 2]['bg'] == player1_color and self.game_buttons[i + 1][j + 1]['bg'] == "white" :
                                print(" puune prima bucata din diagonala principala si primma bucata este pe prima linie gen")
                                self.handle_button_click(0, j + 1, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 2 > -1 and j - 2 > -1 and i + 1 < self.rows and j + 1 < self.collumns and i+1 != self.rows:## diagoanala principala si singuru care lipseste e pe ultima linie
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i - 1][j - 1]['bg'] == player1_color and self.game_buttons[i - 2][j - 2]['bg'] == player1_color and self.game_buttons[i + 1][j + 1]['bg'] == "white" and  self.game_buttons[i + 2][j + 1]['bg'] != "white":
                                print(" puune prima bucata din diagonala principala si primma bucata este pe prima linie gen")
                                self.handle_button_click(0, j + 1, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                print("2222222222222222222222")

                gasit = 0

                for i in range(self.rows):
                    for j in range(self.collumns):
                        if self.game_buttons[i][j]['bg'] == player2_color:
                            gasit = 1
                if gasit == 0: # nu am pus nici o culoare inca
                    if self.game_buttons[self.rows - 1][(self.collumns - 1) // 2]['bg'] == "white": #daca fix mijlocu e liber pune acolo
                        self.handle_button_click(0, (self.collumns - 1) // 2, player1_color, player2_color,
                                                 player1_entry,
                                                 player2_entry)
                    else: self.handle_button_click(0, (self.collumns - 1) // 2 + 1, player1_color, player2_color,
                                                 player1_entry,
                                                 player2_entry)
                for i in range(self.rows):  # cam are o piesa pusa, o gaseste si incearca sa o continue
                    for j in range(self.collumns):
                        if self.game_buttons[i][j]['bg'] == player2_color:
                            if j + 1 < self.collumns and self.game_buttons[i][j+1]['bg'] == "white":#in caz ca are piesa o continua pe dreapta
                                self.handle_button_click(0, j + 1 , player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                            else:
                                if i - 1 > -1 and self.game_buttons[i-1][j]['bg'] == "white":#in caz ca are piesa o continua pe sus
                                    print("pun deasupra un patratell")
                                    self.handle_button_click(0, j , player1_color, player2_color,
                                                             player1_entry,
                                                             player2_entry)
                                elif j - 1 > -1 and self.game_buttons[i][j-1]['bg'] == "white": #in caz ca are piesa o continua pe stanga
                                    print("pun in stanga un patratell")
                                    self.handle_button_click(0, j-1, player1_color, player2_color,
                                                             player1_entry,
                                                             player2_entry)
                                elif j + 1 < self.collumns and self.game_buttons[i][j+1]['bg'] != "white":
                                    print(f"pun piesa sus dreeapta la inceput la botulet {i}{j}")
                                    self.handle_button_click(0, j + 1, player1_color, player2_color,
                                                             player1_entry,
                                                             player2_entry)
                                elif j - 1 > -1 and self.game_buttons[i][j-1]['bg'] != "white":
                                    print(f"pun piesa sus stanga la inceput la botulet {i}{j}")
                                    self.handle_button_click(0, j - 1, player1_color, player2_color,
                                                             player1_entry,
                                                             player2_entry)

            return
        self.wait = 1
        self.game_buttons[initial_row][col]['bg'] = 'white'

        if row > 0:
            # Only revert the previous button to white if it's not the initially clicked button
            self.game_buttons[row - 1][col]['bg'] = 'white'
        self.game_buttons[row][col]['bg'] = current_color

        self.after(delay, lambda: self.animate_button_change(row + 1, col, initial_row, current_color, player1_color,
                                                             player2_color, player1_entry, player2_entry))

    def switch_player_turn(self):
        # Switch turns
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1

    def player_has_won(self, player1_color, player2_color):

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
                              player1_is_checked, player1_entry, player2_entry):
        game_interface_frame = tk.Frame(self)
        self.frames["GameInterface"] = game_interface_frame
        self.rows = rows
        self.collumns = columns


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
                    command=lambda row=i, col=j: self.handle_button_click(row, col, player1_color, player2_color,
                                                                          player1_entry, player2_entry)

                )
                # Place buttons in the grid with padding on top and left
                button.grid(row=i + 1, column=j + 1)
                button.bind('<Button-1>',
                            lambda event, r=i, c=j: self.handle_button_click(r, c, player1_color, player2_color,
                                                                             player1_entry, player2_entry))
                self.game_buttons[i][j] = button

        right_padding = tk.Frame(game_interface_frame, width=padding_width)
        right_padding.grid(row=1, column=columns + 1, rowspan=rows)
        bottom_padding = tk.Frame(game_interface_frame, height=padding_height, width=self.screen_width)
        bottom_padding.grid(row=rows + 1, columnspan=columns + 2)

        game_interface_frame.pack(expand=True, fill='both')

        return game_interface_frame

    def update_player_selection(self):
        player = 1 if self.player_option_var.get() == 1 else 2
    def player_vs_hardAI(self):
        player_vs_hardbot = tk.Frame(self)
        self.frames["PlayerVsHardBot"] = player_vs_hardbot

        bg_image_path = r"E:\Python\4InARow\player_vs_bot.png"

        bg_image = ImageTk.PhotoImage(Image.open(bg_image_path).resize((self.screen_width, self.screen_height)))

        canvas = tk.Canvas(player_vs_hardbot, width=self.screen_width, height=self.screen_height)
        canvas.pack(fill="both", expand=True)

        canvas.create_image(0, 0, image=bg_image, anchor="nw")
        canvas.image = bg_image  # Keep a reference

        button_image_path = r"E:\Python\4InARow\chatframe.png"
        button_image = ImageTk.PhotoImage(Image.open(button_image_path).resize((190, 50)))

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
        player2_entry = "Bot_Hard"
        play_button = tk.Button(
            player_vs_hardbot,
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
                player1_entry.get(), player2_entry,
                int(row_select.get()), int(column_select.get()),
                self.player_option_var.get(), player1_entry.get(), player2_entry
            )
        )

        play_button.image = button_image
        button_window = canvas.create_window(
            self.screen_width // 2 + 130, self.screen_height - 305,  # Adjust position as needed
            window=play_button
        )

        player_vs_hardbot.pack_forget()

        self.add_exit_button(player_vs_hardbot, canvas)

        return player_vs_hardbot
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

        player2_entry = "Bot_Medium"

        play_button = tk.Button(
            player_vs_mediumbot,
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
                player1_entry.get(), player2_entry,
                int(row_select.get()), int(column_select.get()),
                self.player_option_var.get(), player1_entry.get(), player2_entry
            )
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

    def player_vs_easyAI(self):
        player_vs_easyAI = tk.Frame(self)
        self.frames["PlayerVsEasyBot"] = player_vs_easyAI

        bg_image_path = r"E:\Python\4InARow\player_vs_bot.png"

        bg_image = ImageTk.PhotoImage(Image.open(bg_image_path).resize((self.screen_width, self.screen_height)))

        canvas = tk.Canvas(player_vs_easyAI, width=self.screen_width, height=self.screen_height)
        canvas.pack(fill="both", expand=True)

        canvas.create_image(0, 0, image=bg_image, anchor="nw")
        canvas.image = bg_image  # Keep a reference

        button_image_path = r"E:\Python\4InARow\chatframe.png"
        button_image = ImageTk.PhotoImage(Image.open(button_image_path).resize((190, 50)))

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

        player2_entry = "Bot_Easy"

        play_button = tk.Button(
            player_vs_easyAI,
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
                player1_entry.get(), player2_entry,
                int(row_select.get()), int(column_select.get()),
                self.player_option_var.get(), player1_entry.get(), player2_entry
            )
        )

        play_button.image = button_image
        button_window = canvas.create_window(
            self.screen_width // 2 + 130, self.screen_height - 305,  # Adjust position as needed
            window=play_button
        )

        self.add_exit_button(player_vs_easyAI, canvas)

        return player_vs_easyAI





    def show_frame(self, name):
        frame = self.frames[name]
        # Hide all frames first
        for f in self.frames.values():
            f.pack_forget()
        # Show the desired frame
        frame.pack(fill="both", expand=True)
        frame.tkraise()

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

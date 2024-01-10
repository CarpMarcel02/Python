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
            command=lambda:  self.show_frame("PlayGame"),
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

        self.add_exit_button(main_menu_frame,canvas)
        return main_menu_frame

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

        self.add_exit_button(play_game_frame,canvas)

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

        self.add_exit_button(play_vs_computer_frame,canvas)


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

        row_select = tk.Spinbox(player_vs_player_frame, from_=5, to=10, wrap=True)
        canvas.create_window(1037, 568, window=row_select)

        column_select = tk.Spinbox(player_vs_player_frame, from_=5, to=10, wrap=True)
        canvas.create_window(1094, 603, window=column_select)

        player1_entry = tk.Entry(player_vs_player_frame)
        player1_entry_window = canvas.create_window(866, 287, window=player1_entry)


        player2_entry = tk.Entry(player_vs_player_frame)
        player2_entry_window = canvas.create_window(1166, 287, window=player2_entry)

        self.player_checkbutton_var = tk.BooleanVar(value=False)

        # Player 1 Checkbutton
        self.player1_checkbutton = ttk.Checkbutton(
            player_vs_player_frame,
            variable=self.player_checkbutton_var,
            command=lambda: self.update_player_check(1)
        )
        canvas.create_window(935, 680, window=self.player1_checkbutton)

        # Player 2 Checkbutton
        self.player2_checkbutton = ttk.Checkbutton(
            player_vs_player_frame,
            variable=self.player_checkbutton_var,
            command=lambda: self.update_player_check(2)
        )
        canvas.create_window(1180, 680, window=self.player2_checkbutton)

        color_player_1 = tk.Button(player_vs_player_frame, text="    ", bg="white", command=lambda: self.choose_color(color_player_1))
        button_window = canvas.create_window(805, 260, window=color_player_1)  # Position the button at (100, 100)

        color_player_2 = tk.Button(player_vs_player_frame, text="    ", bg="white", command=lambda: self.choose_color(color_player_2))
        button_window = canvas.create_window(1105, 260, window=color_player_2)  # Position the button at (100, 100)

        button_image_path = r"E:\Python\4InARow\chatframe.png"
        button_image = ImageTk.PhotoImage(Image.open(button_image_path).resize((190, 50)))



        player_vs_player_frame.pack_forget()

        self.add_exit_button(player_vs_player_frame,canvas)

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
                self.player_checkbutton_var.get())
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

    def create_game_interface(self, player1_color, player2_color, player1_name, player2_name, rows, columns,
                              player1_is_checked):
        game_interface_frame = tk.Frame(self)
        self.frames["GameInterface"] = game_interface_frame
        self.game_buttons = [[None for _ in range(columns)] for _ in range(rows)]  # Initialize the game grid

        for i in range(rows):
            for j in range(columns):
                button = tk.Button(
                    game_interface_frame,
                    bg='white',  # Start with a white background
                    width=10,  # Width of the button, adjust as necessary
                    height=3,  # Height of the button, adjust as necessary
                    command=lambda row=i, col=j: self.handle_button_click(row, col)
                )
                button.grid(row=i, column=j)  # Place the button in the grid
                self.game_buttons[i][j] = button  # Store the button reference

        game_interface_frame.pack()

    def handle_button_click(self, row, col):
        # This method will handle the logic when a game button is clicked
        # For example, check whose turn it is, update the button color, and check for a win condition
        current_color = "red" if self.player_checkbutton_var.get() == 1 else "yellow"  # Example logic
        self.game_buttons[row][col]['bg'] = current_color  # Update button color
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

        row_select = tk.Spinbox(player_vs_easyAI, from_=5, to=10, wrap=True)
        canvas.create_window(1037, 568, window=row_select)

        column_select = tk.Spinbox(player_vs_easyAI, from_=5, to=10, wrap=True)
        canvas.create_window(1094, 603, window=column_select)

        player1_entry = tk.Entry(player_vs_easyAI)
        player1_entry_window = canvas.create_window(866, 287, window=player1_entry)

        # player2_entry = tk.Entry(player_vs_easyAI)
        # player2_entry_window = canvas.create_window(1166, 287, window=player2_entry)

        self.player_checkbutton_var = tk.BooleanVar(value=False)

        # Player 1 Checkbutton
        self.player1_checkbutton = ttk.Checkbutton(
            player_vs_easyAI,
            variable=self.player_checkbutton_var,
            command=lambda: self.update_player_check(1)
        )
        canvas.create_window(935, 680, window=self.player1_checkbutton)

        # Player 2 Checkbutton
        self.player2_checkbutton = ttk.Checkbutton(
            player_vs_easyAI,
            variable=self.player_checkbutton_var,
            command=lambda: self.update_player_check(2)
        )
        canvas.create_window(1180, 680, window=self.player2_checkbutton)

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

        row_select = tk.Spinbox(player_vs_mediumbot, from_=5, to=10, wrap=True)
        canvas.create_window(1037, 568, window=row_select)

        column_select = tk.Spinbox(player_vs_mediumbot, from_=5, to=10, wrap=True)
        canvas.create_window(1094, 603, window=column_select)

        player1_entry = tk.Entry(player_vs_mediumbot)
        player1_entry_window = canvas.create_window(866, 287, window=player1_entry)

        # player2_entry = tk.Entry(player_vs_easyAI)
        # player2_entry_window = canvas.create_window(1166, 287, window=player2_entry)

        self.player_checkbutton_var = tk.BooleanVar(value=False)

        # Player 1 Checkbutton
        self.player1_checkbutton = ttk.Checkbutton(
            player_vs_mediumbot,
            variable=self.player_checkbutton_var,
            command=lambda: self.update_player_check(1)
        )
        canvas.create_window(935, 680, window=self.player1_checkbutton)

        # Player 2 Checkbutton
        self.player2_checkbutton = ttk.Checkbutton(
            player_vs_mediumbot,
            variable=self.player_checkbutton_var,
            command=lambda: self.update_player_check(2)
        )
        canvas.create_window(1180, 680, window=self.player2_checkbutton)

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

        row_select = tk.Spinbox(player_vs_hardbot, from_=5, to=10, wrap=True)
        canvas.create_window(1037, 568, window=row_select)

        column_select = tk.Spinbox(player_vs_hardbot, from_=5, to=10, wrap=True)
        canvas.create_window(1094, 603, window=column_select)

        player1_entry = tk.Entry(player_vs_hardbot)
        player1_entry_window = canvas.create_window(866, 287, window=player1_entry)

        # player2_entry = tk.Entry(player_vs_easyAI)
        # player2_entry_window = canvas.create_window(1166, 287, window=player2_entry)

        self.player_checkbutton_var = tk.BooleanVar(value=False)

        # Player 1 Checkbutton
        self.player1_checkbutton = ttk.Checkbutton(
            player_vs_hardbot,
            variable=self.player_checkbutton_var,
            command=lambda: self.update_player_check(1)
        )
        canvas.create_window(935, 680, window=self.player1_checkbutton)

        # Player 2 Checkbutton
        self.player2_checkbutton = ttk.Checkbutton(
            player_vs_hardbot,
            variable=self.player_checkbutton_var,
            command=lambda: self.update_player_check(2)
        )
        canvas.create_window(1180, 680, window=self.player2_checkbutton)

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

    def update_player_check(self, selected):
        if selected == 1 and self.player1_checkbutton.instate(['selected']):  # If player 1's checkbox is selected
            self.player2_checkbutton.state(['!selected'])  # Deselect player 2's checkbox
        elif selected == 2 and self.player2_checkbutton.instate(['selected']):  # If player 2's checkbox is selected
            self.player1_checkbutton.state(['!selected'])  # Deselect player 1's checkbox

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

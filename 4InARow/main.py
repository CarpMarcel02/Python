import tkinter as tk
from tkinter import colorchooser, ttk
import random
import sys

from PIL import Image, ImageTk


class MainFrame(tk.Tk):
    """
        MainFrame is the primary window for the 4-in-a-Row game application.

        This class extends the Tkinter Tk class and sets up the main window,
        including full-screen attributes, the main menu, and frames for the
        game modes such as Player vs Player or Player vs Computer.


        """

    def __init__(self):
        """
            The constructor initializes the basic things that make this game work, like the screen width or the screen_height,
            and also keeps some attributes that are necessary in the game.

                       Attributes:
            screen_width (int): The width of the screen.
            screen_height (int): The height of the screen.
            frames (dict): A dictionary holding the different frames of the game.
            rows (int): The number of rows the game will have.
            columns (int): The number of columns the game will have.
            wait (int): A flag indicating if the game that basically doesn`t allow the
                        opponent to place his tile until the other one has dropped and
                        also wait`s for the bot to do his turn. While the person it`s waiting
                        for the enemy`s tile to go down, the program will decide if the game is over or not
            player_option_var (tk.IntVar): A variable that basically represents which player will start the game.
            current_player (int): This variable indicates which players turns is.
            bot_plays_first (int): Indicates if the bot start`s first or not.
            result_label (tk.Label): The label will print out the message on the screen at the end of the game.
            game_buttons (list): game_buttons basically is like a matrix that keeps count of the buttons.
               """
        super().__init__()
        self.attributes("-fullscreen", True)
        self.title("Main Menu")

        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        self.frames = {}
        self.rows = 0
        self.collumns = 0
        self.wait = 0

        self.player_option_var = tk.IntVar(value=1)

        self.current_player = 0
        self.bot_plays_first = 0
        self.result_label = tk.Label(self, text="", font=("Helvetica", 20))

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
        """
                I made this class in the purpose of creating an actual game, that wouldn`t be launched from the terminal
                , basically it`s useless for the class presentation, but I would like to keep it so I could add some more
                things in this project and afterwards to use it in my CV

                Attributes:
                        main_menu_frame (tk.Frame): A frame widget that serves as the container for the main menu.
                        bg_image_path (str): The file path of the background image that would be used in order to obtain the picture.
                        bg_image (PhotoImage): This attribute represents exactly the picture I want to get from the path.
                        canvas (tk.Canvas): The canvas represents the place in which I add elements.
                        button_image_path (str): Exactly the same thing like the previous path, but this one leads to a button frame.
                        button_image (PhotoImage): This is the image for the button frame.
                        button (tk.Button): The 'Play Game' button redirects to another frame.
                        button_window (Canvas window): I used this attribute in order to place exactly where I wanted the 'PLay Game' button.
                Returns:
                        tk.Frame: The frame for the main menu.

                       """
        main_menu_frame = tk.Frame(self)
        main_menu_frame.pack(fill="both", expand=True)
        self.frames["MainMenu"] = main_menu_frame

        bg_image_path = r"E:\Python\4InARow\poza editata.png"
        bg_image = ImageTk.PhotoImage(Image.open(bg_image_path).resize((self.screen_width, self.screen_height)))

        canvas = tk.Canvas(main_menu_frame, width=self.screen_width, height=self.screen_height)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg_image, anchor="nw")
        canvas.image = bg_image

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

        button.image = button_image
        button_window = canvas.create_window(self.screen_width // 2, self.screen_height // 3, anchor="center",
                                             window=button)

        self.add_exit_button(main_menu_frame, canvas)
        return main_menu_frame

    def create_play_game(self):
        """
                    This class makes the frame in which if you started the program normally by running it, not in the terminal,
                    it would be a meniu in which you could choose between player versus player or player versus bot.
                    This method is almost the same with the previous one, but contains more buttons.

                    Attributes:
                            play_game_frame (tk.Frame): A frame widget that serves as the container for the play menu.
                            bg_image_path (str): The file path of the background image that would be used in order to obtain the picture.
                            bg_image (PhotoImage): This attribute represents exactly the picture I want to get from the path.
                            canvas (tk.Canvas): The canvas represents the place in which I add elements.
                            button_image_path (str): Exactly the same thing like the previous path, but this one leads to a button frame.
                            button_image (PhotoImage): This is the image for the button frame.
                            button (tk.Button): I have 3 buttons, the first one for going to the Player vs Player lobby, the second
                                                one will go to another menu in which you chose the difficulty of the bot, and one more button for
                                                going back.
                            button_window (Canvas window): I used this attribute in order to place exactly where I wanted the 'PLay Game' button.
                    Returns:
                            tk.Frame: The frame for choosing the game type menu.

                               """
        play_game_frame = tk.Frame(self)
        self.frames["PlayGame"] = play_game_frame

        bg_image_path = r"E:\Python\4InARow\poza needitata.jpg"

        bg_image = ImageTk.PhotoImage(Image.open(bg_image_path).resize((self.screen_width, self.screen_height)))

        canvas = tk.Canvas(play_game_frame, width=self.screen_width, height=self.screen_height)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg_image, anchor="nw")
        canvas.image = bg_image

        button_image_path = r"E:\Python\4InARow\chatframe.png"
        button_image = ImageTk.PhotoImage(Image.open(button_image_path).resize((190, 50)))

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
            self.screen_width // 2, self.screen_height - 550,
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
            self.screen_width // 2, self.screen_height - 750,
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
            self.screen_width // 2, self.screen_height - 650,
            window=play_vs_computer
        )

        play_game_frame.pack_forget()

        self.add_exit_button(play_game_frame, canvas)

        return play_game_frame

    def create_player_vs_computer(self):
        """
                            This function is almost the same with the previous one, creates the menu for choosing which
                            difficulty of the bot you want to face.

                            Attributes:
                                    play_game_frame (tk.Frame): A frame widget that serves as the container for the play menu.
                                    bg_image_path (str): The file path of the background image that would be used in order to obtain the picture.
                                    bg_image (PhotoImage): This attribute represents exactly the picture I want to get from the path.
                                    canvas (tk.Canvas): The canvas represents the place in which I add elements.
                                    button_image_path (str): Exactly the same thing like the previous path, but this one leads to a button frame.
                                    button_image (PhotoImage): This is the image for the button frame.
                                    button (tk.Button): I have 4 buttons, the first one for the easy bot, the second
                                                        one for the medium bot, the third one for the hard bot and the fourth is in case you might
                                                        reconsider and play against another player, not a bot.
                                    button_window (Canvas window): I used this attribute in order to place exactly where I want my buttons
                            Returns:
                                    tk.Frame: The frame for tthe player versus computer.

                                       """
        play_vs_computer_frame = tk.Frame(self)
        self.frames["PlayerVsComputer"] = play_vs_computer_frame

        bg_image_path = r"E:\Python\4InARow\poza needitata.jpg"
        bg_image = ImageTk.PhotoImage(Image.open(bg_image_path).resize((self.screen_width, self.screen_height)))

        canvas = tk.Canvas(play_vs_computer_frame, width=self.screen_width, height=self.screen_height)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg_image, anchor="nw")
        canvas.image = bg_image

        button_image_path = r"E:\Python\4InARow\chatframe.png"
        button_image = ImageTk.PhotoImage(Image.open(button_image_path).resize((190, 50)))

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
            self.screen_width // 2, self.screen_height - 450,
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
            self.screen_width // 2, self.screen_height - 750,
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
            self.screen_width // 2, self.screen_height - 650,
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
            self.screen_width // 2, self.screen_height - 550,
            window=hard_mode
        )

        play_vs_computer_frame.pack_forget()

        self.add_exit_button(play_vs_computer_frame, canvas)

        return play_vs_computer_frame

    def player_vs_player(self):
        """
          This method creates the interface for the player versus player. In here you can choose the collor you want
          your tile to be, to write the player`s name, to choose the number of rows/columns and to chose who starts first

          Attributes:
              player_vs_player_frame (tk.Frame): A frame to hold all widgets for the player versus player setup.
              bg_image_path (str): The file path of the background image that would be used in order to obtain the picture.
              bg_image (PhotoImage): This attribute represents exactly the picture I want to get from the path.
              canvas (tk.Canvas): The canvas represents the place in which I add elements.
              back_button (tk.Button): A button for going to the previous menu.
              row_select (tk.Spinbox): This spinbox will represent the number of rows .
              column_select (tk.Spinbox): This spinbox will represent the number of columns .
              player1_entry (tk.Entry): This entry widget will hold the name of the first player.
              player2_entry (tk.Entry): This entry widget will hold the name of the second player.
              player1_radiobutton (ttk.Radiobutton): This radio button will decide who goes first.
              player2_radiobutton (ttk.Radiobutton):  This radio button will decide who goes first.
              color_player_1 (tk.Button): A button to choose the color for player 1.
              color_player_2 (tk.Button): A button to choose the color for player 2.
              play_button (tk.Button): A button to start the game.

          Returns:
              tk.Frame: The frame for the Player versus Player interface.
          """
        player_vs_player_frame = tk.Frame(self)
        self.frames["PlayerVsPlayer"] = player_vs_player_frame

        bg_image_path = r"E:\Python\4InARow\player_vs_player.png"
        bg_image = ImageTk.PhotoImage(Image.open(bg_image_path).resize((self.screen_width, self.screen_height)))

        canvas = tk.Canvas(player_vs_player_frame, width=self.screen_width, height=self.screen_height)
        canvas.pack(fill="both", expand=True)

        canvas.create_image(0, 0, image=bg_image, anchor="nw")
        canvas.image = bg_image

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
            self.screen_width // 2 - 130, self.screen_height - 305,
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
            value=1
        )
        canvas.create_window(935, 680, window=self.player1_radiobutton)

        self.player2_radiobutton = ttk.Radiobutton(
            player_vs_player_frame,
            variable=self.player_option_var,
            value=2
        )
        canvas.create_window(1180, 680, window=self.player2_radiobutton)

        color_player_1 = tk.Button(player_vs_player_frame, text="    ", bg="white",
                                   command=lambda: self.choose_color(color_player_1))
        button_window = canvas.create_window(805, 260, window=color_player_1)

        color_player_2 = tk.Button(player_vs_player_frame, text="    ", bg="white",
                                   command=lambda: self.choose_color(color_player_2))
        button_window = canvas.create_window(1105, 260, window=color_player_2)

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
            self.screen_width // 2 + 130, self.screen_height - 305,
            window=play_button
        )

        return player_vs_player_frame

    def create_game_interface(self, player1_color, player2_color, player1_name, player2_name, rows, columns,
                              player1_is_checked, player1_entry, player2_entry):
        """
           This function will create the main setup of the game, basically it will see what size to make the game tiles
            by the number of rows/columns, creates the matrix of the game buttons and assign them the function that makes
            this game work. It doesn`t really need all the parameters, but I gave them in order to give them the button
            the function that make them work
           Parameters:
               player1_color (str): Player 1 color.
               player2_color (str): Player 2 color.
               player1_name (str): Player 1 name.
               player2_name (str): Player 2 name.
               rows (int): Number of rows.
               columns (int): Number of columns.
               player1_is_checked (int): Based on this will know if the first player starts or not.
               player1_entry (str): Player 1 type.
               player2_entry (str): Player 2 type.

           The method adjusts the size of the buttons and the padding around the grid based on the number of rows and columns to ensure a balanced layout. Each button is bound to a click event handler.

           Returns:
               tk.Frame: The game board interface.
           """
        game_interface_frame = tk.Frame(self)
        rows = int(rows)
        columns = int(columns)
        self.frames["GameInterface"] = game_interface_frame
        self.rows = rows
        self.collumns = columns

        if columns < 11 and rows < 9:
            button_width = 20
            button_height = 6
            total_button_width = button_width * columns
            total_button_height = button_height * rows

            padding_width = (self.screen_width // 2) - (total_button_width) - 60 * columns
            padding_height = (self.screen_height // 2) - (total_button_height) - 40 * rows
        else:
            button_width = 15
            button_height = 5
            total_button_width = button_width * columns
            total_button_height = button_height * rows
            padding_width = (self.screen_width // 2) - (total_button_width) - 45 * columns
            padding_height = (self.screen_height // 2) - (total_button_height) - 30 * rows

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

    def player_vs_easyAI(self):
        """
                            This method creates the interface for the player versus easy bot. In here you can choose the color you want
                            your tile to be, to write the player name, to choose the number of rows/columns and to chose who starts first
                            Attributes:
                                player_vs_easyAI (tk.Frame): A frame to hold all widgets for the player versus bot setup.
                                bg_image_path (str): The file path of the background image that would be used in order to obtain the picture.
                                bg_image (PhotoImage): This attribute represents exactly the picture I want to get from the path.
                                button_image_path (str): The file path of the button image that would be used in order to obtain the picture.
                                row_select (tk.Spinbox):  This spinbox will represent the number of rows .
                                column_select (tk.Spinbox): This spinbox will represent the number of columns .
                                player1_entry (tk.Entry): This entry widget will hold the name of the first player.
                                player1_radiobutton (ttk.Radiobutton): This radio button will decide who goes first.
                                color_player_1 (tk.Button): A button to choose the color for player 1.
                                color_player_2 (tk.Button): A button to choose the color for the bot.
                                play_button (tk.Button): A button to start the game.


                            Returns:
                                tk.Frame: The frame for the Player versus easy bot interface.
                            """
        player_vs_easyAI = tk.Frame(self)
        self.frames["PlayerVsEasyBot"] = player_vs_easyAI

        bg_image_path = r"E:\Python\4InARow\player_vs_bot.png"

        bg_image = ImageTk.PhotoImage(Image.open(bg_image_path).resize((self.screen_width, self.screen_height)))

        canvas = tk.Canvas(player_vs_easyAI, width=self.screen_width, height=self.screen_height)
        canvas.pack(fill="both", expand=True)

        canvas.create_image(0, 0, image=bg_image, anchor="nw")
        canvas.image = bg_image

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
            self.screen_width // 2 - 130, self.screen_height - 305,
            window=back_button
        )

        row_select = tk.Spinbox(player_vs_easyAI, from_=6, to=10, wrap=True)
        canvas.create_window(1037, 568, window=row_select)

        column_select = tk.Spinbox(player_vs_easyAI, from_=7, to=13, wrap=True)
        canvas.create_window(1094, 603, window=column_select)

        player1_entry = tk.Entry(player_vs_easyAI)
        player1_entry_window = canvas.create_window(866, 287, window=player1_entry)

        self.player1_radiobutton = ttk.Radiobutton(
            player_vs_easyAI,
            variable=self.player_option_var,
            value=1
        )
        canvas.create_window(935, 680, window=self.player1_radiobutton)

        self.player2_radiobutton = ttk.Radiobutton(
            player_vs_easyAI,
            variable=self.player_option_var,
            value=2
        )
        canvas.create_window(1180, 680, window=self.player2_radiobutton)

        color_player_1 = tk.Button(player_vs_easyAI, text="    ", bg="white",
                                   command=lambda: self.choose_color(color_player_1))
        button_window = canvas.create_window(805, 260, window=color_player_1)

        color_player_2 = tk.Button(player_vs_easyAI, text="    ", bg="white",
                                   command=lambda: self.choose_color(color_player_2))
        button_window = canvas.create_window(1105, 260, window=color_player_2)

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
            self.screen_width // 2 + 130, self.screen_height - 305,
            window=play_button
        )

        self.add_exit_button(player_vs_easyAI, canvas)

        return player_vs_easyAI

    def player_vs_mediumAI(self):
        """
                    This method creates the interface for the player versus medium bot. In here you can choose the color you want
                    your tile to be, to write the player name, to choose the number of rows/columns and to chose who starts first
                    Attributes:
                        player_vs_mediumbot (tk.Frame): A frame to hold all widgets for the player versus bot setup.
                        bg_image_path (str): The file path of the background image that would be used in order to obtain the picture.
                        bg_image (PhotoImage): This attribute represents exactly the picture I want to get from the path.
                        button_image_path (str): The file path of the button image that would be used in order to obtain the picture.
                        row_select (tk.Spinbox):  This spinbox will represent the number of rows .
                        column_select (tk.Spinbox): This spinbox will represent the number of columns .
                        player1_entry (tk.Entry): This entry widget will hold the name of the first player.
                        player1_radiobutton (ttk.Radiobutton): This radio button will decide who goes first.
                        color_player_1 (tk.Button): A button to choose the color for player 1.
                        color_player_2 (tk.Button): A button to choose the color for the bot.
                        play_button (tk.Button): A button to start the game.


                    Returns:
                        tk.Frame: The frame for the Player versus medium bot interface.
                    """
        player_vs_mediumbot = tk.Frame(self)
        self.frames["PlayerVsMediumBot"] = player_vs_mediumbot

        bg_image_path = r"E:\Python\4InARow\player_vs_bot.png"

        bg_image = ImageTk.PhotoImage(Image.open(bg_image_path).resize((self.screen_width, self.screen_height)))

        canvas = tk.Canvas(player_vs_mediumbot, width=self.screen_width, height=self.screen_height)
        canvas.pack(fill="both", expand=True)

        canvas.create_image(0, 0, image=bg_image, anchor="nw")
        canvas.image = bg_image

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
            self.screen_width // 2 + 130, self.screen_height - 305,
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
            self.screen_width // 2 - 130, self.screen_height - 305,
            window=back_button
        )

        row_select = tk.Spinbox(player_vs_mediumbot, from_=6, to=10, wrap=True)
        canvas.create_window(1037, 568, window=row_select)

        column_select = tk.Spinbox(player_vs_mediumbot, from_=7, to=13, wrap=True)
        canvas.create_window(1094, 603, window=column_select)

        player1_entry = tk.Entry(player_vs_mediumbot)
        player1_entry_window = canvas.create_window(866, 287, window=player1_entry)

        self.player1_radiobutton = ttk.Radiobutton(
            player_vs_mediumbot,
            variable=self.player_option_var,
            value=1
        )
        canvas.create_window(935, 680, window=self.player1_radiobutton)

        self.player2_radiobutton = ttk.Radiobutton(
            player_vs_mediumbot,
            variable=self.player_option_var,
            value=2
        )
        canvas.create_window(1180, 680, window=self.player2_radiobutton)

        color_player_1 = tk.Button(player_vs_mediumbot, text="    ", bg="white",
                                   command=lambda: self.choose_color(color_player_1))
        button_window = canvas.create_window(805, 260, window=color_player_1)

        color_player_2 = tk.Button(player_vs_mediumbot, text="    ", bg="white",
                                   command=lambda: self.choose_color(color_player_2))
        button_window = canvas.create_window(1105, 260, window=color_player_2)

        button_image_path = r"E:\Python\4InARow\chatframe.png"
        button_image = ImageTk.PhotoImage(Image.open(button_image_path).resize((190, 50)))

        player_vs_mediumbot.pack_forget()

        self.add_exit_button(player_vs_mediumbot, canvas)

        return player_vs_mediumbot

    def player_vs_hardAI(self):
        """
            This method creates the interface for the player versus hard bot. In here you can choose the color you want
            your tile to be, to write the player name, to choose the number of rows/columns and to chose who starts first
            Attributes:
                player_vs_hardbot (tk.Frame): A frame to hold all widgets for the player versus bot setup.
                bg_image_path (str): The file path of the background image that would be used in order to obtain the picture.
                bg_image (PhotoImage): This attribute represents exactly the picture I want to get from the path.
                button_image_path (str): The file path of the button image that would be used in order to obtain the picture.
                row_select (tk.Spinbox):  This spinbox will represent the number of rows .
                column_select (tk.Spinbox): This spinbox will represent the number of columns .
                player1_entry (tk.Entry): This entry widget will hold the name of the first player.
                player1_radiobutton (ttk.Radiobutton): This radio button will decide who goes first.
                color_player_1 (tk.Button): A button to choose the color for player 1.
                color_player_2 (tk.Button): A button to choose the color for the bot.
                play_button (tk.Button): A button to start the game.


            Returns:
                tk.Frame: The frame for the Player versus hard bot interface.
            """
        player_vs_hardbot = tk.Frame(self)
        self.frames["PlayerVsHardBot"] = player_vs_hardbot

        bg_image_path = r"E:\Python\4InARow\player_vs_bot.png"

        bg_image = ImageTk.PhotoImage(Image.open(bg_image_path).resize((self.screen_width, self.screen_height)))

        canvas = tk.Canvas(player_vs_hardbot, width=self.screen_width, height=self.screen_height)
        canvas.pack(fill="both", expand=True)

        canvas.create_image(0, 0, image=bg_image, anchor="nw")
        canvas.image = bg_image

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
            self.screen_width // 2 - 130, self.screen_height - 305,
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
            value=1
        )
        canvas.create_window(935, 680, window=self.player1_radiobutton)

        self.player2_radiobutton = ttk.Radiobutton(
            player_vs_hardbot,
            variable=self.player_option_var,
            value=2
        )
        canvas.create_window(1180, 680, window=self.player2_radiobutton)

        color_player_1 = tk.Button(player_vs_hardbot, text="    ", bg="white",
                                   command=lambda: self.choose_color(color_player_1))
        button_window = canvas.create_window(805, 260, window=color_player_1)

        color_player_2 = tk.Button(player_vs_hardbot, text="    ", bg="white",
                                   command=lambda: self.choose_color(color_player_2))
        button_window = canvas.create_window(1105, 260, window=color_player_2)

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
            self.screen_width // 2 + 130, self.screen_height - 305,
            window=play_button
        )

        player_vs_hardbot.pack_forget()

        self.add_exit_button(player_vs_hardbot, canvas)

        return player_vs_hardbot

    def start_game(self, player1_color, player2_color, player1_name, player2_name, rows, columns, player1_is_checked,
                   player1_entry, player2_entry):
        """
           Initiates the game and will basically decide exactly who starts first

           Parameters:
               player1_color (str): The color of player 1.
               player2_color (str): The color of player 1.
               player1_name (str): The name of player 1.
               player2_name (str): The name of player 2.
               rows (int): The number of rows.
               columns (int): The number of columns.
               player1_is_checked (int): Shows who starts first.
               player1_entry (str): Type of opponent player.
               player2_entry (str): Type of opponent player

           This method sets the current player and initializes the game interface with the specified settings.
           It also handles the setup for bot players in case of a player versus computer game mode.
           """
        self.wait = 0
        if player1_entry == "":
            player1_entry = "Player 1"
        if player2_entry == "":
            player2_entry = "Player 2"
        if "GameInterface" in self.frames:
            self.frames["GameInterface"].destroy()
            del self.frames["GameInterface"]

        self.create_game_interface(player1_color, player2_color, player1_name, player2_name, rows, columns,
                                   player1_is_checked, player1_entry, player2_entry)

        player1_is_checked = int(player1_is_checked)

        self.show_frame("GameInterface")
        if player1_is_checked == 1:
            self.current_player = 1
        else:
            if player1_is_checked == 2 and player2_entry != "Bot_Easy" and player2_entry != "Bot_Medium" and player2_entry != "Bot_Hard":
                self.current_player = 2
            else:
                if player2_entry == "Bot_Easy" or player2_entry == "Bot_Medium" or player2_entry == "Bot_Hard":
                    self.current_player = 0
                    self.bot_plays_first = 1
                    self.animate_button_change(self.rows, 0, self.rows, player2_color, player1_color, player2_color,
                                               player1_entry, player2_entry)

    def handle_button_click(self, row, col, player1_color, player2_color, player1_entry, player2_entry):
        """
           When a button is clicked durring the game this function is called and is preparing the setup for the animate_button_change.
           Parameters:
               row (int): Number of rows.
               col (int): Number of columns.
               player1_color (str): Player 1 color.
               player2_color (str): Player 2 color.
               player1_entry (str): Player 1 name.
               player2_entry (str): Player 2 name, or the bot name.

            It wait`s for the class variable wait to turn 0 in order for a button to be able to clicked again.
           """
        if self.wait == 0:
            current_button = self.game_buttons[row][col]
            if player1_color == 'white':
                player1_color = 'yellow'
            if player2_color == 'white':
                player2_color = 'red'

            if current_button['bg'] == 'white':
                if self.current_player == 1:
                    current_color = player1_color
                else:
                    current_color = player2_color


                self.animate_button_change(row, col, row, current_color, player1_color, player2_color, player1_entry,
                                           player2_entry)

    def animate_button_change(self, row, col, initial_row, current_color, player1_color, player2_color, player1_entry,
                              player2_entry, delay=100):
        """

            When it`s a player turn it will make the class variable wait 1 so it could recall the function in order for the buttons
            to make the effect of dropping. On the other hand, while the other player is waiting to finish the animation the game
            will check if the game is over or not.
            In case the second player is a bot, here is the implementation of the bots, the easy bot is designed to put only
            random tiles in the game, the medium bot will check for win situations and methods to block the enemy, and the hard bot
            will check for more win situations and more complex ones and the same for block situations for the enemy

           Parameters:
               row (int): Number of rows.
               col (int): Number of columns.
               initial_row (int): This variable helps in order for the drop effect, it will keep the position from where the drop started.
               current_color (str): The color to be applied to the button.
               player1_color (str): Player 1 color.
               player2_color (str): Player 2 color.
               player1_entry (str):  Player 1 name.
               player2_entry (str): Player 2 name, or the identifier of the bot.
               delay (int, optional): Time delay for the drop effect of the buttons. The delay is considered in milliseconds (ms).

           This method is called recursevly.
           """
        if (row >= self.rows or self.game_buttons[row][col]['bg'] != 'white') or self.bot_plays_first == 1:
            self.wait = 0
            if self.bot_plays_first == 0:
                self.switch_player_turn()
            over = 0
            winner = 0
            winner = self.player_has_won(player1_color, player2_color)
            message = ""
            if winner == 1:
                over = 1
                message = f"{player1_entry} has won!"
            elif winner == 2:
                over = 1
                message = f"{player2_entry} has won!"
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
                self.update_idletasks()
                self.result_label.lift()
                self.update()
                self.result_label.place(relx=0.5, rely=0, anchor="n")
                for row_buttons in self.game_buttons:
                    for button in row_buttons:
                        button.config(state=tk.DISABLED)
                        button.unbind('<Button-1>')

            if (self.current_player == 2 and player2_entry == "Bot_Easy" and winner == 0) or self.bot_plays_first == 1:
                if self.bot_plays_first == 1:
                    self.bot_plays_first = 0
                    self.handle_button_click(0, (self.collumns - 1) // 2, player1_color, player2_color,
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
            if (
                    self.current_player == 2 and player2_entry == "Bot_Medium" and winner == 0) or self.bot_plays_first == 1:
                if self.bot_plays_first == 1:
                    self.bot_plays_first = 0
                    self.handle_button_click(0, (self.collumns - 1) // 2, player1_color, player2_color,
                                             player1_entry,
                                             player2_entry)
                for i in range(self.rows):
                    for j in range(self.collumns):
                        if i - 1 > -1:
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i - 1][j][
                                'bg'] == player2_color and self.game_buttons[i - 2][j]['bg'] == player2_color and \
                                    self.game_buttons[i - 3][j]['bg'] == "white":
                                print("botul castiga prin alegerea de a plasa deasupra pe coloana")
                                self.handle_button_click(0, j, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i == self.rows - 1 and j + 3 < self.collumns:
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i][j + 1][
                                'bg'] == player2_color and self.game_buttons[i][j + 2]['bg'] == player2_color and \
                                    self.game_buttons[i][j + 3]['bg'] == "white":
                                print("botul castiga prin alegerea la dreapta pe linia cea mai dejos")
                                self.handle_button_click(0, j + 3, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i != self.rows - 1 and j + 3 < self.collumns:
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
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i][j - 1][
                                'bg'] == "white" and self.game_buttons[i][j - 2]['bg'] == player1_color and \
                                    self.game_buttons[i][j - 3]['bg'] == player1_color:
                                print("botul blocheaza punand pe a doua pozitie unde ii lipseste inamicului")
                                self.handle_button_click(0, j - 1, player1_color, player2_color, player1_entry,
                                                         player2_entry)
                        if i == self.rows - 1 and j - 3 > -1:  # in caz de pe fix ultima linie si lipseste penultima bucata pentru a face blbocaj
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i][j - 1][
                                'bg'] == player1_color and self.game_buttons[i][j - 2]['bg'] == "white" and \
                                    self.game_buttons[i][j - 3]['bg'] == player1_color:
                                print("botul blocheaza punand pe a treia pozitie unde ii lipseste inamicului")

                                self.handle_button_click(0, j - 2, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 3 > -1 and j + 3 < self.collumns:  # in cazz de blocaj pe diagonala secundara
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i - 1][j + 1][
                                'bg'] == player1_color and self.game_buttons[i - 2][j + 2]['bg'] == player1_color and \
                                    self.game_buttons[i - 3][j + 3]['bg'] == "white" and \
                                    self.game_buttons[i - 2][j + 3]['bg'] != "white":
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
                for i in range(self.rows):  # a 3 a piesa
                    for j in range(self.collumns):
                        if self.game_buttons[i][j]['bg'] == player2_color:
                            count = 1
                            if i + 1 < self.rows and i + 2 < self.rows:  # coloana sus
                                if self.game_buttons[i + 1][j]['bg'] == player2_color and \
                                        self.game_buttons[i + 2][j][
                                            'bg'] == "white":
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
                                    if i + 1 < self.rows:
                                        if self.game_buttons[i + 1][j + 2]['bg'] != "white":  # la dreapta
                                            self.handle_button_click(0, j + 2, player1_color, player2_color,
                                                                     player1_entry, player2_entry)
                                    if j - 1 > -1 and i + 1 < self.rows:
                                        if self.game_buttons[i + 1][j - 1]['bg'] != "white":  # la stanga
                                            self.handle_button_click(0, j - 1, player1_color, player2_color,
                                                                     player1_entry, player2_entry)

                            if i - 1 > -1 and j - 1 > -1 and i - 2 < -1 and j - 2 > -1:  # diagonala  principala
                                if self.game_buttons[i - 1][j - 1]['bg'] == player2_color:
                                    count += 2
                                if count == 3:
                                    if self.game_buttons[i - 1][j - 3]['bg'] != "white":
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
                if self.bot_plays_first == 1:
                    self.bot_plays_first = 0
                    self.handle_button_click(0, (self.collumns - 1) // 2, player1_color, player2_color,
                                             player1_entry,
                                             player2_entry)

                for i in range(self.rows):  # in caz de botul poate castiga punand pe ultima linie piesa
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
                                    self.game_buttons[i][j + 3]['bg'] == "white" and self.game_buttons[i + 1][j + 3][
                                'bg'] != "white":
                                print("botul castiga prin alegerea la dreapta dar nu e linia de jos")
                                self.handle_button_click(0, j + 3, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i == self.rows - 1 and j - 3 > -1:  # in caz de are situatie de win pe stanga si  e ultima linie gen
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i][j - 1][
                                'bg'] == player2_color and self.game_buttons[i][j - 2]['bg'] == player2_color and \
                                    self.game_buttons[i][j - 3]['bg'] == "white":
                                print("botul castiga prin alegerea la stanga dar  e si pee linia de jos")
                                self.handle_button_click(0, j - 3, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i != self.rows - 1 and j - 3 > -1:  # in caz de are situatie de win pe stanga si nu e ultima linie gen
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i][j - 1][
                                'bg'] == player2_color and self.game_buttons[i][j - 2]['bg'] == player2_color and \
                                    self.game_buttons[i][j - 3]['bg'] == "white" and self.game_buttons[i + 1][j - 3][
                                'bg'] != "white":
                                print("botul castiga prin alegerea la dreapta dar nu e linia de jos")
                                self.handle_button_click(0, j - 3, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 3 > -1 and j + 3 < self.collumns:  # in caz de castiga pe diagonala secundara
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i - 1][j + 1][
                                'bg'] == player2_color and self.game_buttons[i - 2][j + 2]['bg'] == player2_color and \
                                    self.game_buttons[i - 3][j + 3]['bg'] == "white" and \
                                    self.game_buttons[i - 1][j + 2]['bg'] != "white":
                                print("botul castiga prin alegerea la diagonala secundara")
                                self.handle_button_click(0, j + 3, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 3 > -1 and j - 3 > -1:  # in caz de castiga pe diagonala principala
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i - 1][j - 1][
                                'bg'] == player2_color and self.game_buttons[i - 2][j - 2]['bg'] == player2_color and \
                                    self.game_buttons[i - 3][j - 3]['bg'] == "white" and \
                                    self.game_buttons[i - 2][j - 3]['bg'] != "white":
                                print("botul castiga prin alegerea la diagonala principala")
                                self.handle_button_click(0, j - 3, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                for i in range(self.rows):  # in caz de botul poate castiga daca i lipseste o piesa pe a 3-a pozitie
                    for j in range(self.collumns):
                        if i != self.rows - 1 and j + 3 < self.collumns:  # in caz de are situatie de win pe dreapta si nu e ultima linie gen si doar a 3 treia piesa lipseste
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i][j + 1][
                                'bg'] == player2_color and self.game_buttons[i][j + 2]['bg'] == "white" and \
                                    self.game_buttons[i][j + 3]['bg'] == player2_color and \
                                    self.game_buttons[i + 1][j + 2]['bg'] != "white":
                                print(
                                    "botul castiga prin alegerea la dreapta dar nu e linia de jos fix dupa 2 patratteele")
                                self.handle_button_click(0, j + 2, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i != self.rows - 1 and j - 3 > -1:  # in caz de are situatie de win pe stanga si nu e ultima linie gen
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i][j - 1][
                                'bg'] == player2_color and self.game_buttons[i][j - 2]['bg'] == "white" and \
                                    self.game_buttons[i][j - 3]['bg'] == player2_color and \
                                    self.game_buttons[i + 1][j - 2]['bg'] != "white":
                                print(
                                    "botul castiga prin alegerea la dreapta dar nu e linia de jos fix dupa 2 patratteele")
                                self.handle_button_click(0, j - 2, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)

                        if i - 3 > -1 and j + 3 < self.collumns:  # in cazz de castiga pe diagonala secundara
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i - 1][j + 1][
                                'bg'] == player2_color and self.game_buttons[i - 2][j + 2]['bg'] == "white" and \
                                    self.game_buttons[i - 3][j + 3]['bg'] == player2_color and \
                                    self.game_buttons[i - 1][j + 2]['bg'] != "white":
                                print("botul castiga prin alegerea la diagonala secundara fix dupa 2 patratteele")
                                self.handle_button_click(0, j - 2, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 3 > -1 and j - 3 > -1:  # in cazz de castiga pe diagonala principala
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i - 1][j - 1][
                                'bg'] == player2_color and self.game_buttons[i - 2][j - 2]['bg'] == "white" and \
                                    self.game_buttons[i - 3][j - 3]['bg'] == player2_color and \
                                    self.game_buttons[i - 1][j - 2]['bg'] != "white":
                                print("botul castiga prin alegerea la diagonala principala fix dupa 2 patratteele")
                                self.handle_button_click(0, j - 3, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                for i in range(self.rows):  # in caz de botul poate castiga daca ii lipseste o piesa pe a 2-a pozitie
                    for j in range(self.collumns):
                        if i != self.rows - 1 and j + 3 < self.collumns:  # in caz de are situatie de win pe dreapta si nu e ultima linie gen si doar a 3 treia piesa lipseste
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i][j + 1][
                                'bg'] == "white" and self.game_buttons[i][j + 2]['bg'] == player2_color and \
                                    self.game_buttons[i][j + 3]['bg'] == player2_color and \
                                    self.game_buttons[i + 1][j + 1]['bg'] != "white":
                                print("botul castiga prin alegerea la dreapta cu o patratica dar nu e linia de jos")
                                self.handle_button_click(0, j + 1, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i != self.rows - 1 and j - 3 > -1:  # in caz de are situatie de win pe stanga si nu e ultima linie gen
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i][j - 1][
                                'bg'] == "white" and self.game_buttons[i][j - 2]['bg'] == player2_color and \
                                    self.game_buttons[i][j - 3]['bg'] == player2_color and \
                                    self.game_buttons[i + 1][j - 1]['bg'] != "white":
                                print("botul castiga prin alegerea la stanga  cu o patratica dar nu e linia de jos")
                                self.handle_button_click(0, j - 1, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 3 > -1 and j + 3 < self.collumns:  # in cazz de castiga pe diagonala secundara
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i - 1][j + 1][
                                'bg'] == "white" and self.game_buttons[i - 2][j + 2]['bg'] == player2_color and \
                                    self.game_buttons[i - 3][j + 3]['bg'] == player2_color and \
                                    self.game_buttons[i][j + 1]['bg'] != "white":
                                print("botul castiga prin alegerea la diagonala secundara fix urmatorea patratica")
                                self.handle_button_click(0, j + 1, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 3 > -1 and j - 3 > -1:  # in cazz de castiga pe diagonala principala
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i - 1][j - 1][
                                'bg'] == "white" and self.game_buttons[i - 2][j - 2]['bg'] == player2_color and \
                                    self.game_buttons[i - 3][j - 3]['bg'] == player2_color and \
                                    self.game_buttons[i][j - 1]['bg'] != "white":
                                print("botul castiga prin alegerea la diagonala principala fix urmatorea patratica")
                                self.handle_button_click(0, j - 1, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                for i in range(
                        self.rows):  # in caz de botul poate castiga daca ii lipseste prima piesa dintr- diagonala
                    for j in range(self.collumns):
                        if i - 2 > -1 and j + 2 < self.collumns and i + 1 < self.rows and j - 1 > -1 and i + 1 != self.rows:  # diagonala secundara
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i - 1][j + 1][
                                'bg'] == player2_color and self.game_buttons[i - 2][j + 2]['bg'] == player2_color and \
                                    self.game_buttons[i + 1][j - 1]['bg'] == "white" and \
                                    self.game_buttons[i + 2][j - 1]['bg'] != "white":
                                print(
                                    " puune prima bucata din diagonala secundara dar nu e primma bucata nu e pe prima linie")
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
                        if i - 2 > -1 and j - 2 > -1 and i + 1 < self.rows and j + 1 < self.collumns and i + 1 == self.rows:  # diagoanala principala si singuru care lipseste e pe ultima linie
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i - 1][j - 1][
                                'bg'] == player2_color and self.game_buttons[i - 2][j - 2]['bg'] == player2_color and \
                                    self.game_buttons[i + 1][j + 1]['bg'] == "white":
                                print(
                                    " puune prima bucata din diagonala principala si primma bucata este pe prima linie gen")
                                self.handle_button_click(0, j + 1, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 2 > -1 and j - 2 > -1 and i + 2 < self.rows and j + 1 < self.collumns and i + 2 != self.rows:  # diagoanala principala si singuru care lipseste e pe ultima linie
                            if self.game_buttons[i][j]['bg'] == player2_color and self.game_buttons[i - 1][j - 1][
                                'bg'] == player2_color and self.game_buttons[i - 2][j - 2]['bg'] == player2_color and \
                                    self.game_buttons[i + 1][j + 1]['bg'] == "white" and \
                                    self.game_buttons[i + 2][j + 1]['bg'] != "white":
                                print(
                                    " puune prima bucata din diagonala principala si primma bucata este pe prima linie gen")
                                self.handle_button_click(0, j + 1, player1_color, player2_color,
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
                                    self.game_buttons[i][j + 3]['bg'] == "white" and self.game_buttons[i + 1][j + 3][
                                'bg'] != "white":
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
                                    self.game_buttons[i][j - 3]['bg'] == "white" and self.game_buttons[i + 1][j - 3][
                                'bg'] != "white":
                                print("botul blocheaza prin alegerea la dreapta dar nu e linia de jos")
                                self.handle_button_click(0, j - 3, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 3 > -1 and j + 3 < self.collumns:  # in cazz de blocaj pe diagonala secundara
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i - 1][j + 1][
                                'bg'] == player1_color and self.game_buttons[i - 2][j + 2]['bg'] == player1_color and \
                                    self.game_buttons[i - 3][j + 3]['bg'] == "white" and \
                                    self.game_buttons[i - 2][j + 3]['bg'] != "white":
                                print("botul blocheaza prin alegerea la diagonala secundara")
                                self.handle_button_click(0, j + 3, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 3 > -1 and j - 3 > -1:  # in cazz de blocaj pe diagonala principala
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i - 1][j - 1][
                                'bg'] == player1_color and self.game_buttons[i - 2][j - 2]['bg'] == player1_color and \
                                    self.game_buttons[i - 3][j - 3]['bg'] == "white" and \
                                    self.game_buttons[i - 2][j - 3]['bg'] != "white":
                                print("botul blocheaza prin alegerea la diagonala principala")
                                self.handle_button_click(0, j - 3, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                for i in range(
                        self.rows):  # in caz de botul poate bloca daca inamicului ii lipseste o piesa doar de pe a 3-a pozitie, nu ultima
                    for j in range(self.collumns):
                        if i != self.rows - 1 and j + 3 < self.collumns:  # in caz de are situatie de win pe dreapta si nu e ultima linie gen si doar a 3 treia piesa lipseste
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i][j + 1][
                                'bg'] == player1_color and self.game_buttons[i][j + 2]['bg'] == "white" and \
                                    self.game_buttons[i][j + 3]['bg'] == player1_color and \
                                    self.game_buttons[i + 1][j + 2]['bg'] != "white":
                                print(
                                    "botul blocheaza prin alegerea la dreapta dar nu e linia de jos fix dupa 2 patratteele")
                                self.handle_button_click(0, j + 2, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i != self.rows - 1 and j - 3 > -1:  # in caz de are situatie de win pe stanga si nu e ultima linie gen
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i][j - 1][
                                'bg'] == player1_color and self.game_buttons[i][j - 2]['bg'] == "white" and \
                                    self.game_buttons[i][j - 3]['bg'] == player1_color and \
                                    self.game_buttons[i + 1][j - 2]['bg'] != "white":
                                print(
                                    "botul blocheaza prin alegerea la dreapta dar nu e linia de jos fix dupa 2 patratteele")
                                self.handle_button_click(0, j - 2, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i == self.rows - 1 and j - 3 > -1:  # in caz de pe fix ultima linie si lipseste 1 bucata si trebuie sa blocheze
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i][j - 1][
                                'bg'] == player1_color and self.game_buttons[i][j - 2]['bg'] == "white" and \
                                    self.game_buttons[i][j - 3]['bg'] == player1_color:
                                self.handle_button_click(0, j - 2, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 3 > -1 and j + 3 < self.collumns:  # in cazz de castiga pe diagonala secundara
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i - 1][j + 1][
                                'bg'] == player1_color and self.game_buttons[i - 2][j + 2]['bg'] == "white" and \
                                    self.game_buttons[i - 3][j + 3]['bg'] == player1_color and \
                                    self.game_buttons[i - 1][j + 2]['bg'] != "white":
                                print("botul blocheaza prin alegerea la diagonala secundara fix dupa 2 patratteele")
                                self.handle_button_click(0, j - 2, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 3 > -1 and j - 3 > -1:  # in cazz de castiga pe diagonala principala
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i - 1][j - 1][
                                'bg'] == player1_color and self.game_buttons[i - 2][j - 2]['bg'] == "white" and \
                                    self.game_buttons[i - 3][j - 3]['bg'] == player1_color and \
                                    self.game_buttons[i - 1][j - 2]['bg'] != "white":
                                print("botul blocheaza prin alegerea la diagonala principala fix dupa 2 patratteele")
                                self.handle_button_click(0, j - 3, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)

                for i in range(
                        self.rows):  # in caz de botul poate bloca inamicul daca ii lipseste o piesa de pe a doua pozitie
                    for j in range(self.collumns):
                        if i != self.rows - 1 and j + 3 < self.collumns:  # in caz de are situatie de win pe dreapta si nu e ultima linie gen si doar a 3 treia piesa lipseste
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i][j + 1][
                                'bg'] == "white" and self.game_buttons[i][j + 2]['bg'] == player1_color and \
                                    self.game_buttons[i][j + 3]['bg'] == player1_color and \
                                    self.game_buttons[i + 1][j + 1]['bg'] != "white":
                                print("botul bloecheaza prin alegerea la dreapta cu o patratica dar nu e linia de jos")
                                self.handle_button_click(0, j + 1, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i != self.rows - 1 and j - 3 > -1:  # in caz de are situatie de win pe stanga si nu e ultima linie gen
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i][j - 1][
                                'bg'] == "white" and self.game_buttons[i][j - 2]['bg'] == player1_color and \
                                    self.game_buttons[i][j - 3]['bg'] == player1_color and \
                                    self.game_buttons[i + 1][j - 1]['bg'] != "white":
                                print("botul bloecheaza prin alegerea la stanga  cu o patratica dar nu e linia de jos")
                                self.handle_button_click(0, j - 1, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i == self.rows - 1 and j - 3 > -1:  # in caz pe ultima linie la inamic ii lipseste o patratica mai exact a doua
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i][j - 1][
                                'bg'] == "white" and self.game_buttons[i][j - 2]['bg'] == player1_color and \
                                    self.game_buttons[i][j - 3]['bg'] == player1_color:
                                self.handle_button_click(0, j - 1, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 3 > -1 and j + 3 < self.collumns:  # in cazz de castiga pe diagonala secundara
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i - 1][j + 1][
                                'bg'] == "white" and self.game_buttons[i - 2][j + 2]['bg'] == player1_color and \
                                    self.game_buttons[i - 3][j + 3]['bg'] == player1_color and \
                                    self.game_buttons[i][j + 1]['bg'] != "white":
                                print("botul bloecheaza prin alegerea la diagonala secundara fix urmatorea patratica")
                                self.handle_button_click(0, j + 1, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 3 > -1 and j - 3 > -1:  # in cazz de castiga pe diagonala principala
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i - 1][j - 1][
                                'bg'] == "white" and self.game_buttons[i - 2][j - 2]['bg'] == player1_color and \
                                    self.game_buttons[i - 3][j - 3]['bg'] == player1_color and \
                                    self.game_buttons[i][j - 1]['bg'] != "white":
                                print("botul bloecheaza prin alegerea la diagonala principala fix urmatorea patratica")
                                self.handle_button_click(0, j - 1, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                for i in range(
                        self.rows):  # in caz de botul poate bloca daca inamicului ii lipseste prima piesa dintr- diagonala
                    for j in range(self.collumns):
                        if i - 2 > -1 and j + 2 < self.collumns and i + 2 < self.rows and j - 1 > -1 and i + 2 != self.rows:  # diagonala secundara
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i - 1][j + 1][
                                'bg'] == player1_color and self.game_buttons[i - 2][j + 2]['bg'] == player1_color and \
                                    self.game_buttons[i + 1][j - 1]['bg'] == "white" and \
                                    self.game_buttons[i + 2][j - 1]['bg'] != "white":
                                print(
                                    " puune prima bucata din diagonala secundara dar nu e primma bucata nu e pe prima linie")
                                self.handle_button_click(0, j - 1, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 2 > -1 and j + 2 < self.collumns and i + 1 < self.rows and j - 1 > -1 and i + 2 == self.rows:  # diagonala secundara
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i - 1][j + 1][
                                'bg'] == player1_color and self.game_buttons[i - 2][j + 2]['bg'] == player1_color and \
                                    self.game_buttons[i + 1][j - 1]['bg'] == "white":
                                print(
                                    " pune prima bucata din diagonala secundara dar nu e primma bucata este pe prima linie")
                                self.handle_button_click(0, j - 1, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 2 > -1 and j - 2 > -1 and i + 1 < self.rows and j + 1 < self.collumns and i + 2 == self.rows:  # diagoanala principala si singuru care lipseste e pe ultima linie
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i - 1][j - 1][
                                'bg'] == player1_color and self.game_buttons[i - 2][j - 2]['bg'] == player1_color and \
                                    self.game_buttons[i + 1][j + 1]['bg'] == "white":
                                print(
                                    " puune prima bucata din diagonala principala si primma bucata este pe prima linie gen")
                                self.handle_button_click(0, j + 1, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                        if i - 2 > -1 and j - 2 > -1 and i + 1 < self.rows and j + 1 < self.collumns and i + 1 != self.rows:  # diagoanala principala si singuru care lipseste e pe ultima linie
                            if self.game_buttons[i][j]['bg'] == player1_color and self.game_buttons[i - 1][j - 1][
                                'bg'] == player1_color and self.game_buttons[i - 2][j - 2]['bg'] == player1_color and \
                                    self.game_buttons[i + 1][j + 1]['bg'] == "white" and \
                                    self.game_buttons[i + 2][j + 1]['bg'] != "white":
                                print(
                                    " puune prima bucata din diagonala principala si primma bucata este pe prima linie gen")
                                self.handle_button_click(0, j + 1, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)

                gasit = 0

                for i in range(self.rows):
                    for j in range(self.collumns):
                        if self.game_buttons[i][j]['bg'] == player2_color:
                            gasit = 1
                if gasit == 0:  # nu am pus nici o culoare inca
                    if self.game_buttons[self.rows - 1][(self.collumns - 1) // 2][
                        'bg'] == "white":  # daca fix mijlocu e liber pune acolo
                        self.handle_button_click(0, (self.collumns - 1) // 2, player1_color, player2_color,
                                                 player1_entry,
                                                 player2_entry)
                    else:
                        self.handle_button_click(0, (self.collumns - 1) // 2 + 1, player1_color, player2_color,
                                                 player1_entry,
                                                 player2_entry)
                for i in range(self.rows):  # cam are o piesa pusa, o gaseste si incearca sa o continue
                    for j in range(self.collumns):
                        if self.game_buttons[i][j]['bg'] == player2_color:
                            if j + 1 < self.collumns and self.game_buttons[i][j + 1][
                                'bg'] == "white":  # in caz ca are piesa o continua pe dreapta
                                self.handle_button_click(0, j + 1, player1_color, player2_color,
                                                         player1_entry,
                                                         player2_entry)
                            else:
                                if i - 1 > -1 and self.game_buttons[i - 1][j][
                                    'bg'] == "white":  # in caz ca are piesa o continua pe sus
                                    self.handle_button_click(0, j, player1_color, player2_color,
                                                             player1_entry,
                                                             player2_entry)
                                elif j - 1 > -1 and self.game_buttons[i][j - 1][
                                    'bg'] == "white":  # in caz ca are piesa o continua pe stanga
                                    self.handle_button_click(0, j - 1, player1_color, player2_color,
                                                             player1_entry,
                                                             player2_entry)
                                elif j + 1 < self.collumns and self.game_buttons[i][j + 1]['bg'] != "white":
                                    self.handle_button_click(0, j + 1, player1_color, player2_color,
                                                             player1_entry,
                                                             player2_entry)
                                elif j - 1 > -1 and self.game_buttons[i][j - 1]['bg'] != "white":
                                    self.handle_button_click(0, j - 1, player1_color, player2_color,
                                                             player1_entry,
                                                             player2_entry)

            return
        self.wait = 1
        self.game_buttons[initial_row][col]['bg'] = 'white'

        if row > 0:
            self.game_buttons[row - 1][col]['bg'] = 'white'
        self.game_buttons[row][col]['bg'] = current_color

        self.after(delay, lambda: self.animate_button_change(row + 1, col, initial_row, current_color, player1_color,
                                                             player2_color, player1_entry, player2_entry))

    def switch_player_turn(self):
        """
            This method is called each time a player has done a move in order to
             change the current_player variable so the next button pressed will have a different color
           """
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1

    def player_has_won(self, player1_color, player2_color):
        """
           This method will see if there is a winner on the game board
           Parameters:
               player1_color (str): Player 1 color.
               player2_color (str): Player 1 color.

           Returns:
               int: Returns 1 if Player 1 has won,
                            2 if Player 2 or Bot has won,
                            3 for a draw (no empty spaces),
                            0 if the game is still ongoing.

           """
        gasit = 0
        for i in range(self.rows):
            for j in range(self.collumns):
                if self.game_buttons[i][j]['bg'] == 'white':
                    gasit = 1
                else:
                    culoare = self.game_buttons[i][j]['bg']
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

    def show_frame(self, name):
        """
           This function when called will display the frame needed.
           Parameters:
               name (str): The name of the frame that will be displayed.

           """
        frame = self.frames[name]
        for f in self.frames.values():
            f.pack_forget()
        frame.pack(fill="both", expand=True)
        frame.tkraise()

    def choose_color(self, button):
        """
            Will open a color pallet and will make the button the color the player will choose.

            Parameters:
                button (tk.Button): The button widget whose background color is to be changed.

            """
        color = colorchooser.askcolor(title="Choose a color")
        if color[1]:
            button.configure(bg=color[1])

    def add_exit_button(self, frame, canvas):
        """
          This method will create an exit button with an image and place it in the top right corner of the canvas.
          Parameters:
              frame (tk.Frame): The frame in which the exit button will be placed.
              canvas (tk.Canvas): The exact canvas in which the button will be placed.

          """
        exit_button_image_path = r"E:\Python\4InARow\exit_button.png"
        original_image = Image.open(exit_button_image_path)
        resized_image = original_image.resize((25, 25))
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
        exit_button.image = exit_button_image
        exit_button_window = canvas.create_window(
            self.screen_width - 1,
            1,
            anchor="ne",
            window=exit_button
        )

    def close_application(self):
        """
            This method is binded to the exit button and make the destroy operation.
            """
        self.destroy()


if __name__ == "__main__":
    """
        This is the main of the 4 In a Row application
        It will take 4 arguments from the terminal and will call up the MainFrame of the application. 
        With the 4 arguments will call the start_game method of the app. Afterwards it will enter the loop so the app
        will stop only by exact commands.
        Usage:
            4inaRow.py <enemyType> <cell_x> <cell_y> [firstPlayer]

        Arguments:
            enemyType (str): The type of enemy to play against ("Bot_Easy", "Bot_Medium", "Bot_Hard" or player).
            cell_x (int): The number of cells the game is going to have.
            cell_y (int): The number of columns the game is going to have.
            firstPlayer (int): Indicates which player starts first (1 for player 1, 2 for player 2 or bot).

        """
    if len(sys.argv) != 5:
        print("Usage: 4inaRow.py <enemyType> <cell_x> <cell_y> [firstPlayer]")
        sys.exit(1)

    enemy_type = sys.argv[1]
    cell_x = sys.argv[2]
    cell_y = sys.argv[3]
    first_player = sys.argv[4]

    app = MainFrame()
    player1_color = "white"
    player2_color = "white"
    player1_name = ""
    player2_name = ""
    app.start_game(player1_color, player2_color, player1_name, player2_name, cell_x, cell_y, first_player, player1_name,
                   enemy_type)
    app.mainloop()

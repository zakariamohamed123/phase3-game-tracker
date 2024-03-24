class Player:
    def __init__(self, username):
        self.username = username
        # A player has many results.
        self._results = []
        # One player can play many games.
        self._games = []

    def __repr__(self):
        return f" <Player(username: `{self.username}`)>"
    
    # Initialize property: `Player.username`
    @property
    def username(self):
        return self._username
    
    # Functionalize property with setter: `Player.username`
    @username.setter
    def username(self, username):
        # Create validations for player's username:
        #   -> Must be a string.
        #   -> Must be inclusively between 2 and 16 characters.
        #   -> Can be changed after instantiation.
        USERNAME_IS_STR = (type(username) == str)
        USERNAME_IS_APPROPRIATE_LENGTH = (2 <= len(username) <= 16)

        # Conditionally validate property to set property
        if USERNAME_IS_STR and USERNAME_IS_APPROPRIATE_LENGTH:
            self._username = username
        else:
            raise Exception("`Player.username` did not pass validation!")

    # Add functionality to `Player.results()`
    def access_all_results(self, new_result=None):
        # Get access to Result class via relative import
        from solutions.result import Result

        # Create validations for data type (Result) and instantiation of property
        RESULT_IS_REAL = (new_result is not None)
        RESULT_IS_RESULT = (isinstance(new_result, Result))

        # Conditionally validate property to extend list of properties
        if RESULT_IS_REAL and RESULT_IS_RESULT:
            self._results.append(new_result)
        return self._results

    def access_played_games(self, new_game=None):
        # Get access to Game class via relative import
        from solutions.game import Game

        # Create validations for data type (Game) and instantiation of property
        GAME_IS_REAL = (new_game is not None)
        GAME_IS_GAME = (isinstance(new_game, Game))
        GAME_IS_UNIQUE = (new_game not in self._games)

        # Conditionally validate property to extend list of properties
        if GAME_IS_REAL and GAME_IS_GAME and GAME_IS_UNIQUE:
            self._games.append(new_game)
        return self._games

    def check_if_game_has_been_played(self, game):
        # Check if game is in current player's played games
        if game in self.access_played_games():
            return True
        else:
            return False

    def calculate_play_frequency_for_game(self, game):
        # Check if player has ever played current game
        if game in self.access_played_games():
            # Set gameplay counter to iterate later
            gameplay_counter = 0
            # Check all player results for game matches and iterate counter
            for result in self.access_all_results():
                if game == result.game:
                    gameplay_counter += 1
            return gameplay_counter
        else:
            return 0
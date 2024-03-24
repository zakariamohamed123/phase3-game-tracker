class Game:
    def __init__(self, title):
        self.title = title
        # A game has many results.
        self._results = []
        # One game can have many players.
        self._players = []

    def __repr__(self):
        return f" <Game(title: `{self.title}`)>"

    # Initialize property: `Game.title`
    @property
    def title(self):
        return self._title
    
    # Functionalize property with setter: `Game.title`
    @title.setter
    def title(self, title):
        # Create validations for game's title:
        #   -> Must be a string.
        #   -> Must be longer than 0 characters.
        #   -> Cannot be changed after instantiation.
        TITLE_IS_STR = (type(title) == str)
        TITLE_IS_NOT_EMPTY = (len(title) > 0)
        TITLE_ALREADY_EXISTS = (not hasattr(self, "title"))

        # Conditionally validate property to set property
        if TITLE_IS_STR and TITLE_IS_NOT_EMPTY and TITLE_ALREADY_EXISTS:
            self._title = title
        else:
            raise Exception("`Coffee.title` did not pass validation!")

    # Add functionality to `Game.results()`
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

    def access_current_players(self, new_player=None):
        # Get access to Player class via relative import
        from solutions.player import Player

        # Create validations for data type (Player) and instantiation of property
        PLAYER_IS_REAL = (new_player is not None)
        PLAYER_IS_PLAYER = (isinstance(new_player, Player))
        PLAYER_IS_UNIQUE = (new_player not in self._players)

        # Conditionally validate property to extend list of properties
        if PLAYER_IS_REAL and PLAYER_IS_PLAYER and PLAYER_IS_UNIQUE:
            self._players.append(new_player)
        return self._players

    def calculate_average_score_for_player(self, player):
        # Create total score tracker and counter for matching player scores
        sum_of_all_scores, num_of_relevant_scores = 0, 0
        # Iterate through results to find matching player scores
        for result in self._results:
            if result.player == player:
                # Add player-matched score to tracker and increment counter
                sum_of_all_scores += result.score
                num_of_relevant_scores += 1
        # Divide total score sum by incremented counter to get average
        return sum_of_all_scores / num_of_relevant_scores
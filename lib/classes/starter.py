class Game:
    def __init__(self, title):
        self.title = title

    def access_all_results(self):
        pass

    def access_current_players(self):
        pass

    def calculate_average_score_for_player(self, player):
        pass


class Player:
    def __init__(self, username):
        self.username = username

    def access_all_results(self):
        pass

    def access_played_games(self):
        pass

    def check_if_game_has_been_played(self, game):
        pass

    def calculate_play_frequency_for_game(self, game):
        pass


class Result:
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        


""" Write some testing code here! """
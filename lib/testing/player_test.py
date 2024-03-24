import pytest

from classes.starter import Player, Game, Result

# from solutions.player import Player
# from solutions.game import Game
# from solutions.result import Result



class TestPlayer:
    """[TESTING SUITE FOR <Player>]"""

    def test_has_username(self):
        """ INITS AND PROPS: A player must be initialized with a username. """
        player = Player("Saaammmm")
        assert player.username == "Saaammmm"

    def test_username_is_mutable_string(self):
        """ INITS AND PROPS: A player's username must be a mutable string. """
        player = Player("Saaammmm")
        assert isinstance(player.username, str)

        player.username = "ActuallyTopher"
        assert player.username == "ActuallyTopher"

        with pytest.raises(Exception):
            player.username = 2

    def test_title_len(self):
        """ INITS AND PROPS: A player's username must be inclusively between 2 and 16 characters in length. """
        player = Player("Saaammmm")

        assert hasattr(player, "username")
        assert 2 <= len(player.username) <= 16

        with pytest.raises(Exception):
            Player("y")

        with pytest.raises(Exception):
            Player("this_username_is_too_long")

    def test_has_many_results(self):
        """ OBJECT RELATIONS: A player must be able to associate to many results. """
        game = Game("Skribbl.io")
        player_1 = Player("Saaammmm")
        player_2 = Player("ActuallyTopher")
        result_1 = Result(player_1, game, 2000)
        result_2 = Result(player_1, game, 3500)
        result_3 = Result(player_2, game, 190)

        assert len(player_1.access_all_results()) == 2
        assert result_1 in player_1.access_all_results()
        assert result_2 in player_1.access_all_results()
        assert result_3 not in player_1.access_all_results()
        assert result_3 in player_2.access_all_results()

    def test_results_of_type_result(self):
        """ OBJECT RELATIONS: A player's results must each be of type <Result>. """
        game = Game("Skribbl.io")
        player = Player("Saaammmm")
        Result(player, game, 2000)
        Result(player, game, 3500)

        assert isinstance(player.access_all_results()[0], Result)
        assert isinstance(player.access_all_results()[1], Result)

    def test_has_many_games(self):
        """ OBJECT RELATIONS: A player must be able to associate to many games. """
        game = Game("Skribbl.io")
        game_2 = Game("Scattegories")
        game_3 = Game("Codenames")

        player_1 = Player("Nick")
        player_2 = Player("Saaammm")
        Result(player_1, game, 5000)
        Result(player_2, game_2, 19)
        Result(player_1, game_3, 10)

        assert game in player_1.access_played_games()
        assert game_2 not in player_1.access_played_games()
        assert game_3 in player_1.access_played_games()
        assert game_2 in player_2.access_played_games()

    def test_games_of_type_game(self):
        """ OBJECT RELATIONS: A player's games must each be of type <Game>. """
        game = Game("Skribbl.io")
        game_2 = Game("Scattegories")
        player = Player("Ari")
        Result(player, game, 5000)
        Result(player, game_2, 17)

        assert isinstance(player.access_played_games()[0], Game)
        assert isinstance(player.access_played_games()[1], Game)

    def test_games_are_unique(self):
        """ OBJECT RELATIONS: A player's games must all be unique. """
        game_1 = Game("Skribbl.io")
        game_2 = Game("Codenames")
        player = Player("Nick")
        Result(player, game_1, 5000)
        Result(player, game_2, 19)
        Result(player, game_1, 100)

        assert len(set(player.access_played_games())) == len(player.access_played_games())
        assert len(player.access_played_games()) == 2

    def test_has_played_game(self):
        """ AGGREGATES: From the context of a player, one should be able to check if a given game has been previously played. """
        game_1 = Game("Skribbl.io")
        game_2 = Game("Scattegories")
        player_1 = Player("Saaammmm")
        player_2 = Player("ActuallyTopher")
        Result(player_1, game_1, 2000)
        Result(player_1, game_2, 3500)
        Result(player_2, game_1, 190)

        assert player_1.check_if_game_has_been_played(game_1) == True
        assert player_1.check_if_game_has_been_played(game_2) == True
        assert player_2.check_if_game_has_been_played(game_1) == True
        assert player_2.check_if_game_has_been_played(game_2) == False

    def test_has_num_times_played(self):
        """ AGGREGATES: From the context of a player, one should be able to calculate the number of times a given game has been played by that player. """
        game_1 = Game("Skribbl.io")
        game_2 = Game("Scattegories")
        player_1 = Player("Saaammmm")
        player_2 = Player("ActuallyTopher")
        Result(player_1, game_1, 2000)
        Result(player_1, game_2, 19)
        Result(player_1, game_1, 1900)
        Result(player_2, game_2, 9)

        assert player_1.calculate_play_frequency_for_game(game_1) == 2
        assert player_1.calculate_play_frequency_for_game(game_2) == 1
        assert player_2.calculate_play_frequency_for_game(game_1) == 0
        assert player_2.calculate_play_frequency_for_game(game_2) == 1

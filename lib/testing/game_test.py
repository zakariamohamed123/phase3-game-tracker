import pytest

from classes.starter import Player, Game, Result

# from solutions.player import Player
# from solutions.game import Game
# from solutions.result import Result


class TestGame:
    """[TESTING SUITE FOR <Game>]"""

    def test_has_title(self):
        """ INITS AND PROPS: A game must be initialized with a title. """
        game_1 = Game("Skribbl.io")
        game_2 = Game("Jenga")

        assert game_1.title == "Skribbl.io"
        assert game_2.title == "Jenga"

    def test_title_is_immutable_string(self):
        """ INITS AND PROPS: A game's title must be an immutable string. """
        game = Game("Skribbl.io")
        assert isinstance(game.title, str)

        with pytest.raises(Exception):
            game.title = "not Skribbl.io"

    def test_title_len(self):
        """ INITS AND PROPS: A game's title must be greater than 0 characters. """
        game = Game("Skribbl.io")

        assert hasattr(game, "title")
        assert len(game.title) > 0

        with pytest.raises(Exception):
            Game("")

    def test_has_many_results(self):
        """ OBJECT RELATIONS: A game must be able to associate to many results. """
        game = Game("Skribbl.io")
        game_2 = Game("Scattegories")
        player = Player("Saaammmm")
        result_1 = Result(player, game, 2000)
        result_2 = Result(player, game, 3500)
        result_3 = Result(player, game_2, 19)

        assert len(game.access_all_results()) == 2
        assert result_1 in game.access_all_results()
        assert result_2 in game.access_all_results()
        assert result_3 not in game.access_all_results()

    def test_results_of_type_result(self):
        """ OBJECT RELATIONS: A game's results must each be of type <Result>. """
        game = Game("Skribbl.io")
        player = Player("Saaammmm")
        Result(player, game, 2000)
        Result(player, game, 3500)

        assert isinstance(game.access_all_results()[0], Result)
        assert isinstance(game.access_all_results()[1], Result)

    def test_has_many_players(self):
        """ OBJECT RELATIONS: A game must be able to associate to many players. """
        game = Game("Skribbl.io")

        player = Player("Nick")
        player_2 = Player("Ari")
        player_3 = Player("Saaammmm")
        Result(player, game, 5000)
        Result(player_2, game, 4999)

        assert player in game.access_current_players()
        assert player_2 in game.access_current_players()
        assert player_3 not in game.access_current_players()

    def test_players_of_type_player(self):
        """ OBJECT RELATIONS: A game's players must each be of type <Player>. """
        game = Game("Skribbl.io")
        player = Player("Nick")
        player_2 = Player("Ari")
        Result(player, game, 5000)
        Result(player_2, game, 4999)

        assert isinstance(game.access_current_players()[0], Player)
        assert isinstance(game.access_current_players()[1], Player)

    def test_has_unique_players(self):
        """ OBJECT RELATIONS: A game's players must all be unique. """
        game = Game("Skribbl.io")

        player = Player("Nick")
        player_2 = Player("Ari")
        Result(player, game, 5000)
        Result(player_2, game, 4999)

        assert len(set(game.access_current_players())) == len(game.access_current_players())
        assert len(game.access_current_players()) == 2

    def test_average_score(self):
        """ AGGREGATES: From the context of a game, one should be able to calculate a given player's average score. """
        game = Game("Skribbl.io")
        player = Player("Nick")
        Result(player, game, 5000)
        Result(player, game, 4999)
        Result(player, game, 5000)
        Result(player, game, 4999)

        assert game.calculate_average_score_for_player(player) == 4999.5
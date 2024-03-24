import pytest

from classes.starter import Player, Game, Result

# from solutions.player import Player
# from solutions.game import Game
# from solutions.result import Result



class TestResults:
    """[TESTING SUITE FOR <Result>]"""

    def test_has_score(self):
        """ INITS AND PROPS: A result must be initialized with a score. """
        game = Game("Skribbl.io")
        player = Player("Nick")
        result_1 = Result(player, game, 2000)
        result_2 = Result(player, game, 5000)

        assert result_1.score == 2000
        assert result_2.score == 5000

    def test_score_is_immutable_int(self):
        """ INITS AND PROPS: A resultant score must be an immutable integer. """
        game = Game("Skribbl.io")
        player = Player("Nick")
        result_1 = Result(player, game, 2000)
        assert isinstance(result_1.score, int)

        with pytest.raises(Exception):
            Result(player, game, "500")

        with pytest.raises(Exception):
            Result(player, game, 400.99)

    def test_score_is_valid(self):
        """ INITS AND PROPS: A resultant score must be inclusively between 1 and 5000 in magnitude. """
        game = Game("Skribbl.io")
        player = Player("Nick")
        result = Result(player, game, 5000)

        assert 1 <= result.score <= 5000

        with pytest.raises(Exception):
            result.score = 5001

        with pytest.raises(Exception):
            result.score = 0

    def test_has_a_player(self):
        """ OBJECT RELATIONS: A result must be able to associate to a single player. """
        game = Game("Skribbl.io")
        player_1 = Player("Tricia")
        player_2 = Player("Bianca")
        result_1 = Result(player_1, game, 3000)
        result_2 = Result(player_2, game, 3000)

        assert result_1.player == player_1
        assert result_2.player == player_2

    def test_player_of_type_player(self):
        """ OBJECT RELATIONS: A resultant player must be of type <Player>. """
        game = Game("Scattegories")
        player = Player("Kyle")
        player_2 = Player("Brett")
        result_1 = Result(player, game, 9)
        result_2 = Result(player_2, game, 10)

        assert isinstance(result_1.player, Player)
        assert isinstance(result_2.player, Player)

    def test_has_a_game(self):
        """ OBJECT RELATIONS: A result must be able to associate to a single game. """
        game_1 = Game("Skribbl.io")
        game_2 = Game("Codenames")
        player_1 = Player("Ja'Vonn")
        result_1 = Result(player_1, game_1, 8)
        result_2 = Result(player_1, game_2, 3000)

        assert result_1.game == game_1
        assert result_2.game == game_2

    def test_game_of_type_game(self):
        """ OBJECT RELATIONS: A resultant game must be of type <Game>. """
        game_1 = Game("Skribbl.io")
        game_2 = Game("Codenames")
        player = Player("Kyle")
        result_1 = Result(player, game_1, 2000)
        result_2 = Result(player, game_2, 5000)

        assert isinstance(result_1.game, Game)
        assert isinstance(result_2.game, Game)

    def test_get_all_results(self):
        """ OBJECT RELATIONS: A result should inherently track all instances of itself. """
        Result.all_results = []
        game = Game("Codenames")
        player_1 = Player("Ja'Vonn")
        player_2 = Player("Brett")
        result_1 = Result(player_1, game, 2)
        result_2 = Result(player_2, game, 5)

        assert len(Result.all_results) == 2
        assert result_1 in Result.all_results
        assert result_2 in Result.all_results
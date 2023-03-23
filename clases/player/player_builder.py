from .player import Player
from .iplayer_decorator import IPlayerDecorator
from .decorators import PlayerMoveDecorator, PlayerShootingDecorator


class PlayerBuilder:
    def __init__(self, player: Player):
        self.player = player

    def add_movement(self, x, y):
        self.player = PlayerMoveDecorator(self.player, self.player.groups(), x=x, y=y)
        return self

    def add_shooting(self):
        self.player = PlayerShootingDecorator(self.player, self.player.groups())
        return self

    def create_player(self) -> IPlayerDecorator:
        return self.player

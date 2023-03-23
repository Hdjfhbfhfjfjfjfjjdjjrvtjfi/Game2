from pygame.sprite import Sprite, AbstractGroup
from pygame import Surface, Rect, Mask
from pygame.key import ScancodeWrapper


class IPlayer(Sprite):
    image: Surface
    rect: Rect
    mask: Mask
    keys: ScancodeWrapper
    mouse_keys: tuple[bool, bool, bool]
    mouse_coordinates: tuple[int, int]
    health: int

    def update(self, *groups: AbstractGroup) -> None:
        raise NotImplementedError

    def take_damage(self, damage: int) -> None:
        raise NotImplementedError

    def kill_player(self) -> None:
        raise NotImplementedError

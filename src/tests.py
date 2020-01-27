import pytest

from src.roles import Hero, WildBeast
from src.game import game, Game

def test_hero():
    hero = Hero()

    assert isinstance(hero, Hero)

def test_beast():
    beast = WildBeast()

    assert isinstance(beast, WildBeast)

def test_game():
    assert isinstance(game, Game)
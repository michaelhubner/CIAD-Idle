import pygame

from game import GameStateMaschine


def main():

    pygame.init()
    game = GameStateMaschine()
    game.run()


if __name__ == '__main__':
    main()


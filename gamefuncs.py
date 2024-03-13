# - GAME FUNCTIONS -

import pathlib, os, random, time
import colortx as ctx
import gametimer as gtr



def game_folder_path():
    return pathlib.Path(__file__).parent.absolute()


def score_folder():
    return str(game_folder_path()) + "/score"


def score_file(uname):
    return str(game_folder_path()) + "/score/" + uname


def this_is_not_a_number():
    print(ctx.red(" Ceci n'est pas un nombre... "))


def save_score(usave, umn, pname, uatt, gameovertime):
    if usave == "o":
        with open(score_file(pname), 'w') as sf:
            sf.writelines([str(umn), "\n", str(uatt), "\n", gameovertime])
        print(ctx.green(" Score enregistré.\n"))
        # return  # - For replay game -
        print(ctx.magenta(" A bientot :)\n"))
        exit()
    elif usave == "n":
        print(ctx.red(" Score non enregistré. \n"))
        #return  # - For replay game -
        print(ctx.magenta(" A bientot :)\n"))
        exit()
    else:
        print(ctx.red(" Mauvais choix !\n"))

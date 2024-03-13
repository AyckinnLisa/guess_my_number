#!usr/bin/env python3
# -*- coding: utf-8 -*-

# =======================================================================
# =   GUESS MY NUMBER                                                   =
# =      - Version   : 1.0                                              =
# =      - Author    : Ayckinn                                          =
# =      - Mail      : ayckinn@icloud.com                               =
# =      - Release   : March 05' 2024                                   =
# =      - Github    : https://github.com/AyckinnLisa?tab=repositories  =
# =      - Copyright : ©2017-2024                                       =
# =======================================================================

# -- Python modules --
import os, random
# -- Personnal modules --
import colortx as ctx
import gamefuncs as gf
import gametimer as gtr


def main():
    os.system('clear')

    try:
        welcome = " Bienvenue dans le jeu GUESS MY NUMBER"
        welcome_mid_txt = int(len(welcome)/2)

        lisa_here = "Je suis LISA"
        lisa_mid_txt = int(len(lisa_here)/2)

        center_txt = " " * (welcome_mid_txt - lisa_mid_txt)

        print(ctx.green(''' 
 ===================================================== 
 =                  GUESS MY NUMBER                  =
 =                        v1.0                       =
 =               ©2017-2024 - @Ayckinn               =
 =                 ayckinn@icloud.com                =
 =  https://github.com/AyckinnLisa?tab=repositories  = 
 =====================================================\n\n'''))
        print(welcome)
        print(center_txt, lisa_here)

        player = input("\n\n Quel est ton nom ? ")

        # - Check user's datas -
        if os.path.exists(gf.score_file(player)):
            print("\n Contente de te revoir", ctx.magenta(f"{player.title()}"), "!")
            with open(gf.score_file(player), 'r') as scf:
                score_data = scf.readlines()
                # --[*.strip = read line without (\n)]--
                print(("-" * 42))
                print((" " * 5), "Données de jeu précédent :")
                print((" " * 8), "- Partie : 1 ->", ctx.blue(score_data[0].strip()))
                print((" " * 8), "- Tentative(s) :", ctx.yellow(score_data[1].strip()))
                print((" " * 8), "- Temps en secondes :", ctx.green(score_data[2]))
                print("-" * 42)
        else:
            print("\n Bonjour", ctx.magenta(f"{player.title()}"), ":)")
            print(ctx.blue("\n Tu n'as pas encore de données de jeu."))
            print("\n", "-" * 45)

        # - Start game -
        while True:
            try:
                user_max_number = int(input("\n Choisis le nombre maximum pour ta partie : "))

                if user_max_number <= 9 or user_max_number > 10000:
                    print(ctx.red(" Ce nombre n'est pas autorisé."), end = "")
                    print(ctx.red(" Choisis un nombre entre 10 et 10000"))
                    continue   # - continue = Reset loop -
                else:
                    # - Lisa choose a number -
                    lisa_number = random.randint(1, user_max_number)
                    print("\n", "-" * 45)
                    print(f"\n Bien. J'ai choisis un nombre entre 1 et {user_max_number}")
                    print(" A toi de le deviner !")

                    print("\n Pour quitter le jeu, appuies sur", ctx.red("CTRL+C."))
                    print(ctx.green(" !! BONNE CHANCE !!\n"))
                    input(" Appuies sur " + ctx.red("Entrée") + " quand tu es prêt(e) à jouer... ")

                    user_attempt = 1
                    gtr.start_timer()

                    while True:  # - Game loop -
                        try:  # - If entry is not a number
                            user_number = int(input("\n Choisi un nombre : "))
                        except ValueError:
                            gf.this_is_not_a_number()
                            user_attempt += 1
                            continue

                        if user_number < 1 or user_number > user_max_number:
                            print(ctx.red(" Hors jeu !"))
                            user_attempt += 1
                        else:
                            if user_number < lisa_number:
                                print(ctx.cyan(" Trop petit..."))
                                user_attempt += 1
                            elif user_number > lisa_number:
                                print(ctx.yellow(" Trop grand..."))
                                user_attempt += 1
                            else:
                                print(ctx.green(f"\n BRAVO {player.upper()} !"), end = "")
                                print(" J'avais bien choisis le", ctx.blue(lisa_number))

                                print(f" Score : {ctx.magenta(user_attempt)} tentative(s) en ", end = "")
                                print(f"{ctx.yellow(gtr.stop_timer())} secondes.\n")

                                # - Freeze timer otherwise, time continues until exit program -
                                GAME_OVER_TIME = str(gtr.stop_timer())
                                while True:
                                    # - Save the score in the personnal user's file -
                                    user_save = input("\n Veux-tu sauvegarder ton score (o/n) ? ")
                                    if user_save == "o" or user_save == "n":
                                        if not os.path.exists(gf.score_folder()) and user_save == "o":
                                            os.mkdir(gf.score_folder())
                                            gf.save_score(user_save, user_max_number, player, user_attempt, GAME_OVER_TIME)
                                        else :
                                            gf.save_score(user_save, user_max_number, player, user_attempt, GAME_OVER_TIME)                                
                                    else:
                                        print(ctx.red(" Mauvais choix !"))
                                        continue

            except ValueError:
                gf.this_is_not_a_number()
                continue
            
    except KeyboardInterrupt:
        print(ctx.red("\n\n GAME OVER !!\n"))


if __name__ == '__main__':
    main()
    
# ====================================================================== #
# = - Si c'est difficile à expliquer, alors c'est une mauvaise idée  - = #
# = - If it's hard to explain, it's a bad idea                       - = #
# ====================================================================== #
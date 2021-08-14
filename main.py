import os
import random
import webbrowser


def play_random_episode():
    path = r"D:\TV Series\F.R.I.E.N.D.S\\"
    season_list = os.listdir(path)
    season_number = random.randint(0, len(season_list))
    path = path + season_list.__getitem__(season_number)
    episode_list = os.listdir(path)
    episode_number = random.randint(0, len(episode_list))
    path = path + "\\" + episode_list.__getitem__(episode_number)
    webbrowser.open(path)


if __name__ == '__main__':
    play_random_episode()

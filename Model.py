import glob


class Model:

    def __init__(self):
        self.database_name = "databases/words_ee.db"
        # loeme piltide failinimed kaustast listi
        self.image_files = glob.glob("images/*.png")
        self.new_word = None  # suvaline sõna andmebaasist
        self.user_word = []
        self.all_user_chars = []  # valesti sisestatud tähed
        self.counter = 0  # vigade lugeja (saab teada ka listi pikkusega)
        self.player_name = "UNKNOWN"
        self.leaderboard_file = "leaderboard.txt"
        self.score_data = []

class Gallows:
    words = []
    def __init__(self ,game_over=False):
        self.game_over = game_over
        self.words = []

    def play(self, word):
        if not self.words:
            self.words.append(word)
            return self.words
        last_word = self.words[len(self.words) - 1]
        if last_word[len(last_word) - 1:] == word[0:1] and word not in self.words:
            self.words.append(word)
            return self.words
        else:
            self.game_over = True
            return "game over"

    def restart(self):
        self.game_over = False
        self.words.clear()
        return "game restarted"




if __name__ == '__main__':
    my_gallows = Gallows()
    my_gallows.play('apple')# ➞ ['apple']
    my_gallows.play('ear')# ➞ ['apple', 'ear']
    my_gallows.play('rhino')# ➞ ['apple', 'ear', 'rhino']
    print(my_gallows.words)# ➞ ['apple', 'ear', 'rhino']
    # Words should be accessible.
    my_gallows.restart()# ➞ "game restarted"
    # Words list should be set back to empty.
    my_gallows.play('hostess')# ➞ ['hostess']
    my_gallows.play('stash')# ➞ ['hostess', 'stash']
    my_gallows.play('hostess')# ➞ "game over"
    # Words cannot have already been said.
    my_gallows.play('apple')# ➞ ['apple']
    my_gallows.play('ear')# ➞ ['apple', 'ear']
    my_gallows.play('rhino')## ➞ ['apple', 'ear', 'rhino']
    # Corn does not start with an "o".
    my_gallows.play('corn')# ➞"game over"
    print(my_gallows.words)# ➞ ['apple', 'ear', 'rhino']
    my_gallows.restart()# ➞ "game restarted"
    print(my_gallows.words)# ➞ []
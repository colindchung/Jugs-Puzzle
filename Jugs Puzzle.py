'''
jug class defines a jug which has a current volume and a constant capacity
capacity must never be less than volume
'''

class jug:

    def __init__(self, vol, cap):

        if vol <= cap:
            self.vol = vol
            self.cap = cap
        else:
            print("ERROR. VOLUME EXCEEDS CAPACITY")

    def __str__(self):
        return "(" + str(self.vol) + "/" + str(self.cap) + ")"

    def spillinto(self, jug):
        while (self.vol > 0) and (jug.vol < jug.cap):
            jug.vol += 1
            self.vol += -1


'''
JugPuzzle class runs the game. Takes user input and calls upon the jug class accordingly
'''
class JugPuzzle:

    def main_game(self):

        jug0 = jug(8,8)
        jug1 = jug(0,5)
        jug2 = jug(0,3)
        moves = 0
        jugs = [jug0, jug1, jug2]
        while not ((jug0.vol == 4) and (jug1.vol == 4)):
            print(str(moves) + " 0:" + str(jugs[0]) + " 1:" + str(jugs[1]) + " 2:" + str(jugs[2]))
            spill = input("spill from jug: ")
            into = input("into: ")
            if (spill == '0' or spill == '1' or spill == '2') and (into == '0' or into == '1' or into == '2') and (spill != into):
                spill = int(spill)
                into = int(into)
                jugs[spill].spillinto(jugs[into])
                moves += 1
            else:
                print('')
                print("Input Not Valid. Try Again")
                print('')

        print("Puzzle finished! You solved it in " + str(moves) + " moves!")

if __name__ == "__main__":
    game = JugPuzzle()
    game.main_game()



'''Implement a class called Player that represents a cricket player. The Player class should have a method called play() which prints "The player is playing cricket. Derive two classes, Batsman and Bowler, from the Player class. Override the play() method in each derived class to print "The batsman is batting" and "The bowler is bowling", respectively. Write a program to create objects of both the Batsman and Bowler classes and call the play() method for each object. '''


class player:

  def play(self):
    print("the player is playing cricket.")

class Batsman(player):

      def play(self):
        print("the Batsman is batting.")

class Bowler(player):
          def play(self):
            print("the bowler is bowling.")
            

batsman =Batsman()
bowler  =Bowler()

batsman.play()
bowler.play()

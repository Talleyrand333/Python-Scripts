import random
class user:
    def __init__(self):
        self.movie=''
        self.tries=5
        self.clue=''
        self.guess=[]
        self.wrong=[]
        self.display=''.join(self.guess)
    def pick(self):
        files=open('movie.txt','r')
        file=files.readlines()
        file=str(file)
        file=file.split(',')
        file=random.choice(file)
        file=file.split(':')
        movie=file[0]
        clue=file[1]
        self.movie=movie
        self.movie_=list(self.movie)
        self.clue=clue
        for each in self.movie:
            if each.isalnum()==True:
                self.guess.append('-')
            elif each==' ':
                self.guess.append(' ')
        self.display=''.join(self.guess)
        return
    def guesser(self):
        print('Fill in the blanks to reveal the movie {} Type \'clue\' to ask for a clue.'.format(''.join(self.guess)))
        guess=input(': ')
        movie_=list(self.movie)
        if guess in movie_:
            print('Right choice!!')
            posi=[c for c,elem in enumerate(self.movie)if elem==guess]
            for i in posi:
                self.guess[i]=guess
        elif guess=='clue':
            print('Clue:{}'.format(self.clue))
            self.tries-=2
        else:
            print('there is no such letter here')
            self.tries-=1
            self.wrong.append(guess)
        print('Tries Left: {}'.format(self.tries))
        print('Wrong guesses:{}'.format(self.wrong))
        if self.tries==0:
            print('the name of the movie is {}'.format(self.movie))
        return

    def game(self):
        self.pick()
        while self.guess!=self.movie_ and self.tries>0:
            self.guesser()
        print("Congrats your movie is {}".format(self.movie))
        return

a=user()
a.game()

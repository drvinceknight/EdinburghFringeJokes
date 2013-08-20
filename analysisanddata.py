#!/usr/bin/env python
"""
File for analysis of joke data from Edinburgh Fringe festival. These jokes and rankings taken from BBC website.
"""
import matplotlib.pyplot as plt
from pylab import polyfit, poly1d

jd = [
        [2013, 'Rob Auton', 1, "I heard a rumour that Cadbury is bringing out an oriental chocolate bar. Could be a Chinese Wispa."],
        [2013, 'Alex Horne',  2, "I used to work in a shoe-recycling shop. It was sole-destroying."],
        [2013, 'Alfie Moore', 3,"I'm in a same-sex marriage... the sex is always the same."],
        [2013, 'Tim Vine', 4, "My friend told me he was going to a fancy dress party as an Italian island. I said to him 'Don't be Sicily'."],
        [2013, 'Gary Delaney', 5, "I can give you the cause of anaphylactic shock in a nutshell."],
        [2013, 'Phil Wang', 6, "The Pope is a lot like Doctor Who. He never dies, just keeps being replaced by white men."],
        [2013, 'Marcus Brigstocke', 7, "You know you are fat when you hug a child and it gets lost."],
        [2013, 'Liam Williams', 8, "The universe implodes. No matter."],
        [2013, 'Bobby Mair', 9, "I was adopted at birth and have never met my mum. That makes it very difficult to enjoy any lapdance."],
        [2013, 'Chris Coltrane', 10, "The good thing about lending someone your time machine is that you basically get it back immediately."],
        [2012, 'Stewart Francis', 1, "You know who really gives kids a bad name? Posh and Becks."],
        [2012, 'Tim Vince', 2, "Last night me and my girlfriend watched three DVDs back to back. Luckily I was the one facing the telly. "],
        [2012, 'Will Marsh', 3, "I was raised as an only child, which really annoyed my sister."],
        [2012, 'Rob Beckett', 4, "You know you're working class when your TV is bigger than your book case."],
        [2012, 'Chris Turner', 5, "I'm good friends with 25 letters of the alphabet... I don't know Y."],
        [2012, 'Tim Vine', 6, "I took part in the sun tanning Olympics - I just got Bronze."],
        [2012, 'George Ryegold', 7, "Pornography is often frowned upon, but that's only because I'm concentrating."],
        [2012, 'Stewart Francis', 8,  "I saw a documentary on how ships are kept together. Riveting!"],
        [2012, 'Lou Sanders',  9, "I waited an hour for my starter so I complained: 'It's not rocket salad."],
        [2012, 'Nish Kumar', 10, "My mum's so pessimistic, that if there was an Olympics for pessimism... she wouldn't fancy her chances."],
        [2011, 'Nick Helm', 1, "I needed a password eight characters long so I picked Snow White and the Seven Dwarves."],
        [2011, 'Tim Vine', 2, "Crime in multi-storey car parks. That is wrong on so many different levels."],
        [2011, 'Hannibal Buress', 3, "People say 'I'm taking it one day at a time'. You know what? So is everybody. That's how time works."],
        [2011, 'Tim Key', 4, "Drive-Thru McDonalds was more expensive than I thought... once you've hired the car..."],
        [2011, 'Matt Kirshen', 5, "I was playing chess with my friend and he said, 'Let's make this interesting'. So we stopped playing chess."],
        [2011, 'Sarah Millican', 6, "My mother told me, you don't have to put anything in your mouth you don't want to. Then she made me eat broccoli, which felt like double standards."],
        [2011, 'Alan Sharp', 7, "I was in a band which we called The Prevention, because we hoped people would say we were better than The Cure."],
        [2011, 'Mark Watson', 8, "Someone asked me recently - what would I rather give up, food or sex. Neither! I'm not falling for that one again, wife."],
        [2011, 'Andrew Lawrence', 9, "I admire these phone hackers. I think they have a lot of patience. I can't even be bothered to check my OWN voicemails."],
        [2011, 'DeAnne Smith', 10,  "My friend died doing what he loved ... Heroin."],
        [2010, 'Tim Vine', 1, "I've just been on a once-in-a-lifetime holiday. I'll tell you what, never again."],
        [2010, 'David Gibson', 2, "I'm currently dating a couple of anorexics. Two birds, one stone."],
        [2010, 'Emo Philips', 3, "I picked up a hitch hiker. You've got to when you hit them."],
        [2010, 'Jack Whitehall', 4, "I bought one of those anti-bullying wristbands when they first came out. I say 'bought', I actually stole it off a short, fat ginger kid."],
        [2010, 'Gary Delaney', 5, "As a kid I was made to walk the plank. We couldn't afford a dog."],
        [2010, 'John Bishop', 6, "Being an England supporter is like being the over-optimistic parents of the fat kid on sports day."],
        [2010, 'Bo Burnham', 7, "What do you call a kid with no arms and an eyepatch? Names."],
        [2010, 'Gary Delaney', 8, "Dave drowned. So at the funeral we got him a wreath in the shape of a lifebelt. Well, it's what he would have wanted."],
        [2010, 'Robert White', 9, "For Vanessa Feltz, life is like a box of chocolates: Empty."],
        [2010, 'Gareth Richards', 10, "Wooden spoons are great. You can either use them to prepare food. Or, if you can't be bothered with that, just write a number on one and walk into a pub..."],
        [2009, 'Dan Antopolski', 1, "Hedgehogs - why can't they just share the hedge?"],
        [2009, 'Paddy Lennox', 2, "I was watching the London Marathon and saw one runner dressed as a chicken and another runner dressed as an egg. I thought: 'This could be interesting'."],
        [2009, 'Sarah Millican', 3, "I had my boobs measured and bought a new bra. Now I call them Joe Cocker and Jennifer Warnes because they're up where they belong."],
        [2009, 'Zoe Lyons', 4, "I went on a girls' night out recently. The invitation said 'dress to kill'. I went as Rose West."],
        [2009, 'Jack Whitehal', 5, "I'm sure wherever my dad is; he's looking down on us. He's not dead, just very condescending."],
        [2009, 'Adam Hills', 6, "Going to Starbucks for coffee is like going to prison for sex. You know you're going to get it, but it's going to be rough."],
        [2009, 'Marcus Brigstocke', 7, "To the people who've got iPhones: you just bought one, you didn't invent it!"],
        [2009, 'Rhod Gilbert', 8, "A spa hotel? It's like a normal hotel, only in reception there's a picture of a pebble."],
        [2009, 'Dan Antopolski', 9, "I've been reading the news about there being a civil war in Madagascar. Well, I've seen it six times and there isn't."],
        [2009, 'Simon Brodkin', 10, "I started so many fights at my school - I had that attention-deficit disorder. So I didn't finish a lot of them."]
        ]

class Joke():
    def __init__(self, jokedata):
        self.year = jokedata[0]
        self.author = jokedata[1]
        self.rank = jokedata[2]
        self.joke = jokedata[3]

class Author():
    def __init__(self, name):
        self.name = name
        self.jokes = {}
    def addjoke(self, joke):
        if joke.year in self.jokes:
            self.jokes[joke.year].append([joke.rank, joke.joke])
        else:
            self.jokes[joke.year] = [[joke.rank, joke.joke]]

def mean(l):
    return sum(l) / len(l)

if __name__ == '__main__':
    jokeslist = []
    authorsdict = {}
    for row in jd:
        jokeslist.append(Joke(row))

    for joke in jokeslist:
        if joke.author in authorsdict:
            authorsdict[joke.author].addjoke(joke)
        else:
            authorsdict[joke.author] = Author(joke.author)
            authorsdict[joke.author].addjoke(joke)

    # Get min rank vs number of jokes
    nbrofjokesvrank = []
    for author in authorsdict:
        a = authorsdict[author]
        nbrofjokesvrank.append([len(a.jokes), min([min([j[0] for j in a.jokes[year]]) for year in a.jokes])])

    x = [e[0] for e in nbrofjokesvrank]
    y = [e[1] for e in nbrofjokesvrank]
    plt.figure
    plt.scatter(x, y)
    plt.savefig('nbrofjokesvrank.png')
    plt.close()

    # Get mean min rank vs number of jokes
    nbrofjokesvmean = []
    for author in authorsdict:
        a = authorsdict[author]
        nbrofjokesvmean.append([len(a.jokes), mean([min([j[0] for j in a.jokes[year]]) for year in a.jokes])])

    x = [e[0] for e in nbrofjokesvmean]
    y = [e[1] for e in nbrofjokesvmean]
    plt.figure
    plt.scatter(x, y)
    plt.savefig('nbrofjokesvmean.png')
    plt.close()

    # Get box plot of mean rank by number of jokes
    boxes = [[] for e in range(max([len(authorsdict[author].jokes) for author in authorsdict]))]
    for author in authorsdict:
        a = authorsdict[author]
        boxes[len(a.jokes) - 1].append(mean([j[0] for year in a.jokes for j in a.jokes[year] ]))
    plt.figure
    plt.boxplot(boxes)
    plt.xlabel('Number of jokes')
    plt.ylabel('Mean rank')
    plt.savefig('boxplotofmeanrankvnbrofjokes.png')
    plt.close()

    # Get box plot of min rank by number of jokes
    boxes = [[] for e in range(max([len(authorsdict[author].jokes) for author in authorsdict]))]
    for author in authorsdict:
        a = authorsdict[author]
        boxes[len(a.jokes) - 1].append(min([j[0] for year in a.jokes for j in a.jokes[year] ]))
    plt.figure
    plt.boxplot(boxes)
    plt.xlabel('Number of jokes')
    plt.ylabel('Min rank')
    plt.savefig('boxplotofminrankvnbrofjokes.png')
    plt.close()


    # Get histogram of length of jokes
    jokelengths = [len(joke.joke) for joke in jokeslist]
    plt.figure
    plt.hist(jokelengths)
    plt.xlabel('Joke length')
    plt.ylabel('Frequency')
    plt.savefig('histofjokelengths.png')
    plt.close()

    # Get scatter plot of joke rank vs length of joke
    x = []
    y = []
    for joke in jokeslist:
        x.append(len(joke.joke))
        y.append(joke.rank)
    fit = polyfit(x, y, 1)
    fit_fn = poly1d(fit)
    plt.figure
    plt.scatter(x,y)
    plt.plot(x, [fit_fn(x) for x in x], color='red')
    plt.xlabel('Joke length')
    plt.ylabel('Rank')
    plt.savefig('scatterofrankvlength.png')
    plt.close()

    # Some natural language processing

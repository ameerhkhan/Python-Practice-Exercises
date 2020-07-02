#SQLlite is extremely useful for small to medium sized applications when data is going to stay on the disk
#can also be used for testing database operations before porting to other SQL based systems.

import sqlite3

class Students:

    def __init__(self, first, last, score):
        self.first = first
        self.last = last
        self.score = score
    

    @property
    def fullname(self):
        return('{} {}'.format(self.first, self.last))

    @property
    def __repr__(self):
        return("Students('{}', '{}', '{}')".format(self.first, self.last, self.score))
import logging
#{ Basic method adding a logger to file.
logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s;%(levelname)s\t\t%(name)s %(message)s')

file_handler = logging.FileHandler('employeesnew.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


#}

# logging.basicConfig(filename='employees.log', level=logging.INFO, 
#         format='%(asctime)s;%(levelname)s\t\t%(name)s %(message)s' 
#          )

class Employee:
    
    def __init__(self, first, last):
        self.first = first
        self.last = last

        # logging.info('Created Employee {} {}'.format(self.fullname, self.email))
        logger.info('Created Employee {} {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return('{}.{}@email.com'.format(self.first, self.last))
    
    @property
    def fullname(self):
        return('{} {}'.format(self.first, self.last))


emp1 = Employee('Khan', 'Ameer')
emp2 = Employee('Corey', 'Schafer')
emp3 = Employee('Electro', 'Boom')
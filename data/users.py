import dataclasses


@dataclasses.dataclass
class User:
    firstname: str
    lastname: str
    email: str
    gender: str
    phone: int
    dob: str
    mob: str
    yob: str
    subjects: str
    hobbies: str
    avatar: str
    address: str
    state: str
    city: str




admin = User(firstname='Hugo',
             lastname='Boss',
             email='test@email.com',
             gender='Female',
             phone=1234567891,
             dob='22',
             mob='June',
             yob='1990',
             subjects='Computer Science',
             hobbies='Sports',
             avatar='foto.jpg',
             address='New York',
             state='NCR',
             city='Delhi')
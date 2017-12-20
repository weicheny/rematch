import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = True
SECRET_KEY = 'Pr0f3ss0r-ArmS-Is-Br1T1sH'

BASE_URL = 'http://localhost:5000'
PAGINATION_PER_PAGE = 5

# How often, in seconds, to look for and clean up stale posts.
CLEANUP_INTERVAL = 24 * 60 * 60

# the address from which the server sends email
FROM_EMAIL = ''

# topic tags for research listings
TAGS = [
        'artificial intelligence',
        'computer architecture',
        'computational biology',
        'databases',
        'education',
        'graphics',
        'mathematics',
        'human computer interaction',
        'operating systems',
        'networking',
        'programming languages',
        'scientific computing',
        'security',
        'theory',
        'natural language processing',
        'distributed systems',
        'robotics',
        'information processing',
        'information theory',
        'computer vision',
        'ethics',
        'design',
        'compilers',
        'machine learning',
        'algorithms',
        'computer performance analysis',
        'cryptography',
        'software engineering',
        'cognitive science',
        'data science',
        'data mining'
        'neural networks',
        'deep learning',
        'other',
        'java',
        'c',
        'c#',
        'c++',
        'python',
        'ocaml',
        'javascript',
        'mongodb',
        'sql',
        'nosql',
        'r',
        'php',
        'xml',
        'android',
        'swift',
        'objective-c',
        'matlab',
        'ruby',
        'rust',
        'unix',
        'linux',
        'windows',
        'assembly',
    ]

COURSES = [
    'INFO 2450',
    'INFO 3300',
    'INFO 3450',
    'INFO 4300',
    'INFO 5300',
    'CS 1109',
    'CS 1110',
    'CS 1112',
    'CS 1114',
    'CS 1115',
    'CS 1130',
    'CS 1132',
    'CS 1133',
    'CS 1142',
    'CS 1300',
    'CS 1610',
    'CS 1620',
    'CS 1710',
    'CS 1810',
    'CS 2024',
    'CS 2043',
    'CS 2048',
    'CS 2049',
    'CS 2110',
    'CS 2111',
    'CS 2112',
    'CS 2300',
    'CS 2770',
    'CS 2800',
    'CS 2850',
    'CS 3110',
    'CS 3152',
    'CS 3220',
    'CS 3300',
    'CS 3410',
    'CS 3420',
    'CS 3758',
    'CS 4090',
    'CS 4110',
    'CS 4120',
    'CS 4121',
    'CS 4152',
    'CS 4154',
    'CS 4210',
    'CS 4220',
    'CS 4300',
    'CS 4320',
    'CS 4321',
    'CS 4410',
    'CS 4411',
    'CS 4420',
    'CS 4620',
    'CS 4621',
    'CS 4654',
    'CS 4670',
    'CS 4700',
    'CS 4701',
    'CS 4732',
    'CS 4740',
    'CS 4744',
    'CS 4750',
    'CS 4752',
    'CS 4754',
    'CS 4758',
    'CS 4775',
    'CS 4780',
    'CS 4786',
    'CS 4810',
    'CS 4812',
    'CS 4814',
    'CS 4820',
    'CS 4830',
    'CS 4840',
    'CS 4850',
    'CS 4852',
    'CS 4860',
    'CS 4998',
    'CS 4999',
    'CS 5091',
    'CS 5092',
    'CS 5093',
    'CS 5094',
    'CS 5110',
    'CS 5114',
    'CS 5120',
    'CS 5121',
    'CS 5150',
    'CS 5152',
    'CS 5153',
    'CS 5220',
    'CS 5223',
    'CS 5300',
    'CS 5304',
    'CS 5306',
    'CS 5320',
    'CS 5321',
    'CS 5356',
    'CS 5412',
    'CS 5413',
    'CS 5414',
    'CS 5420',
    'CS 5422',
    'CS 5430',
    'CS 5431',
    'CS 5434',
    'CS 5435',
    'CS 5436',
    'CS 5437',
    'CS 5438',
    'CS 5450',
    'CS 5454',
    'CS 5460',
    'CS 5540',
    'CS 5555',
    'CS 5620',
    'CS 5621',
    'CS 5625',
    'CS 5643',
    'CS 5660',
    'CS 5670',
    'CS 5682',
    'CS 5722',
    'CS 5724',
    'CS 5740',
    'CS 5750',
    'CS 5752',
    'CS 5761',
    'CS 5780',
    'CS 5785',
    'CS 5786',
    'CS 5830',
    'CS 5831',
    'CS 5840',
    'CS 5846',
    'CS 5854',
    'CS 5860',
    'CS 5998',
    'CS 5999',
    'CS 6110',
    'CS 6112',
    'CS 6113',
    'CS 6114',
    'CS 6115',
    'CS 6116',
    'CS 6117',
    'CS 6118',
    'CS 6210',
    'CS 6220',
    'CS 6320',
    'CS 6360',
    'CS 6410',
    'CS 6431',
    'CS 6452',
    'CS 6453',
    'CS 6460',
    'CS 6620',
    'CS 6630',
    'CS 6640',
    'CS 6644',
    'CS 6650',
    'CS 6670',
    'CS 6700',
    'CS 6702',
    'CS 6740',
    'CS 6741',
    'CS 6742',
    'CS 6746',
    'CS 6751',
    'CS 6756',
    'CS 6758',
    'CS 6764',
    'CS 6766',
    'CS 6780',
    'CS 6782',
    'CS 6783',
    'CS 6784',
    'CS 6788',
    'CS 6810',
    'CS 6820',
    'CS 6822',
    'CS 6825',
    'CS 6830',
    'CS 6832',
    'CS 6840',
    'CS 6850',
    'CS 6860',
    'CS 6862',
    'CS 7090',
    'CS 7190',
    'CS 7192',
    'CS 7290',
    'CS 7390',
    'CS 7412',
    'CS 7490',
    'CS 7493',
    'CS 7594',
    'CS 7670',
    'CS 7690',
    'CS 7790',
    'CS 7792',
    'CS 7794',
    'CS 7796',
    'CS 7890',
    'CS 7893',
    'CS 7999',
]

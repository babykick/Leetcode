'''
   leetcode
   --------
   Auto scrap the problem information with solution code template created

   :copyright: (c) 2017 by babykick.
   :author: babykick

'''
import os
import re
import datetime
from collections import namedtuple

import requests
from bs4 import BeautifulSoup
import click


BASE_URL = 'https://leetcode.com/problems/{problem_name}/'
COOKIES_RAW = """
LEETCODE_SESSION=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImJhYnlraWNrQDE2My5jb20iLCJ1c2VyX3NsdWciOiJiYWJ5a2ljazE2M2NvbSIsIl9hdXRoX3VzZXJfaWQiOiI1NDQ5NiIsInRpbWVzdGFtcCI6IjIwMTctMDQtMDcgMDA6MzQ6MjIuMDQ1OTE1KzAwOjAwIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJpZCI6NTQ0OTYsIl9zZXNzaW9uX2V4cGlyeSI6MTIwOTYwMCwiX2F1dGhfdXNlcl9oYXNoIjoiYThkOTRkODJmMmJmZWE0MWU2YTk2M2NlYmQ4NmRkOGMxNDRjNGZlMCIsImVtYWlsIjoiYmFieWtpY2tAMTYzLmNvbSJ9.GEy80G5RRcZHiydyuukjVV4ZUX5iEeoOVo4FfptrHdw; express.sid=s%3ANP9IS4wHjstyXbLJ8JEvLcQLdQcOUYtn.FkHJPgJ%2FBNFGep2STc7RWvvwEMN7Bc6ABb%2BNxtAoyIc; csrftoken=foO40MbfzaBKJfXohs4OMVqllD550SorP1Kje4AdXfUTakvf0zdRchzwiSlkvvM2; _ga=GA1.2.1056595494.1491525212; __atuvc=2%7C14; __atuvs=58e6e095f1abae55001
""" 
COOKIES = dict(map(str.strip, s.split('=')) for s in COOKIES_RAW.strip().split(';'))

session = requests.Session()
session.cookies.update(COOKIES)
session.headers.update({'user-agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'})

RE_CODE = re.compile(r"{'value': 'python', 'text': 'Python', 'defaultCode': '(.*?)'", re.M)

TEMPLATE = """'''
{url}

Problem:
{description}
    
Example:
{example}

:author: babykick
:date: {date}
'''


{python_default_code}


if __name__ == '__main__':
    test_cases = [
        # tuple of (input, output)
        (, ),
        (, )
    ]
    
    for sample in test_cases:
        inp, outp = sample
        assert(Solution().hammingDistance(*inp) == outp)
    
"""

Problem = namedtuple('Problem', ['name', 'description', 'example', 'python_default_code'])


def get_url(name):
    if 'http' in name:
        return name
    url = BASE_URL.format(problem_name=name)
    return url


def fetch(url):
    print('fetch', url)
    name = url.split('/problems/')[1].split('/')[0]
    r = session.get(url)
    default_code = RE_CODE.search(r.text)
    if default_code:
        code = default_code.group(1)
        lines = code.split(r'\u000D\u000A')
        default_code = '\n'.join(lines)
        default_code = default_code.replace(r'\u0022', '"')
  
    soup = BeautifulSoup(r.text, 'lxml')
    q = soup.find(class_='question-content')
    desc = '\n'.join(sect.text for sect in q.find_all('p')[1:-2]).strip()
    example = q.find('pre')
    if not example:
        example = q.find_all('p')[-2]
    example = example.text.strip()
    return Problem(name, desc, example, default_code)
    
 
def uniform(name):
    return name.replace('-', '_') \
               .replace(' ', '_') \
               .replace('\t','_')


def make_template(**context):
    return TEMPLATE.format(**context)


@click.command()
@click.argument('name')
def main(name):
    url = get_url(name)
    problem = fetch(url)
    if not os.path.isdir('progress'):
        os.makedirs('progress')
    out_path = 'progress/{}.py'.format(problem.name)
    func_name = problem.python_default_code.split('def ')[1].split('(')[0]
    template = make_template(**problem._asdict(), func_name=func_name, url=url, date=datetime.datetime.now().strftime('%Y-%m-%d'))
    with open(out_path, 'w') as fp:
        fp.write(template)
        print('Wrote to', out_path)


if __name__ == '__main__':
    main()
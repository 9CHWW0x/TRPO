from github import Github
from os.path import isfile, join
from os import environ, listdir

def main():
    token = environ.get('GH_TOKEN')
    job = environ.get('JOB')

    filename = '/tmp/{}.log'.format(job)
    with open(filename) as f:
        body = f.read()

    if (body.strip() == ''):
        return

    g = Github(token)

    repo = g.get_repo('9CHWW0x/TRPO')
    issue = repo.get_issue(1)
    START_BODY = '## Travis {} result'.format(job)
    comment = None
    for c in issue.get_comments():
        if c.body.startswith(START_BODY):
            comment = c

    body = '{}\n```\n{}\n```'.format(START_BODY, body)
    if comment:
        comment.edit(body)
    else:
        issue.create_comment(body)

if __name__ == "__main__":
    main()

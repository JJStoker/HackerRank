import re

email_pattern = re.compile('(^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{0,3}$)')

def fun(s):
    return bool(re.findall(email_pattern.match, s))

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

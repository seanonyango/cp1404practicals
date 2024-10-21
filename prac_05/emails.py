"""
Word Occurrences
Estimate: 20 minutes
Actual:16 minutes
"""
email_to_names = {}
email = input('email: ')
while email != "":
    segments = email.split('@')
    names = segments[0].split('.')
    full_name = " ".join(name.title() for name in names)
    yes_or_no = input(f"Is your name {full_name}? (y/n): ")
    if yes_or_no == 'y':
        email_to_names[email] = full_name
    email = input('email: ')

for email in email_to_names:
    print(f"{email_to_names[email]} ({email}) ")

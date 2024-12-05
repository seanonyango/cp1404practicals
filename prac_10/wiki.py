"""
CP1404 - Practical 10
Wikipedia API & Python Library
"""

import wikipedia

def main():
    print("Enter a wiki page title")
    user_input = input(">>> ")
    while user_input != "":
        try:
            page = wikipedia.page(user_input, auto_suggest=False)
            print(f"Title: {page.title}")
            print(f"URL: {page.url}")
            print(f"Summary: {page.summary}")
        except wikipedia.exceptions.DisambiguationError as e:
            print("Disambiguation error. Options are:")
            for option in e.options:
                print(option)
        except wikipedia.exceptions.PageError:
            print("Page not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        user_input = input(">>> ")
    print("Done")

if __name__ == "__main__":
    main()

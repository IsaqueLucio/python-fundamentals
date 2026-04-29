"""
Exercise 1.2: Text Formatter
File: 02_text_formatter.py

Rules:
1. Create a function called 'format_text' that takes two parameters: 'text' (a string) and 'style' (a string).
2. The 'style' parameter should have a default value of "upper".
3. If the style is "upper", print the text in all uppercase (use text.upper()).
4. If the style is "lower", print the text in all lowercase (use text.lower()).
5. If the style is "title", print the text with the first letter of each word capitalized (use text.title()).
6. Test the function with all three styles.
"""

def format_text(text="", style="upper"):
    if text != "":
        if style == "upper":
            print(text.upper())
        elif style == "lower":
            print(text.lower())
        elif style == "title":
            print(text.title())
    else:
        print("No text informed, nothing to format.")

format_text("")
format_text("testing default style")
format_text("testing the upper when request", "upper")
format_text("TESTING THE LOWER", "lower")
format_text("testing the title", "title")
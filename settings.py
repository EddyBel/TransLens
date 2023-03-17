# Indicates if the translation is fixed and automatic
AUTOMATIC = False

# program functionality
# OPTIONS:
# * TRANSLATE
# * TRANSCRIBE
MODE = "TRANSCRIBE"

# Language to be searched for in the image
# If the variable is set to None the model will try to identify the language automatically, but it is recommended to assign a language beforehand for better results.
# * None
VIEW_LANG = None

# Language to which the text will be translated
TRANSLATE_LANG = "es"

# Guide window transparency level
TRANSPARENCE = 200

# Title that will have the guide window
TITLE_WINDOW = "Select the area of translation"

# Path where Tesseract is installed, especially looking for its execution file.
PATH_TESSERACT = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
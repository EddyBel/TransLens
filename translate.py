from settings import TRANSLATE_LANG
import translators as ts


class Translate:

    """
    Class that encapsulates the functionality of translating text into another language.
    It uses the "translators" library to do the translations.
    """

    def __init__(self) -> None:
        """
        Initializes an instance of the "Translate" class.
        By default, it sets the language to Spanish.
        """

        # Initializes the "language" variable with the value "es", which represents the Spanish language
        self.language = TRANSLATE_LANG

    def translate_list(self, list_texts: list) -> list:
        """Translates a list of texts to the language indicated in the "language" variable.

        Args:
            list_texts (list): List of texts to translate.

        Returns:
            list: List of translated texts.
        """

        # Initializes the empty list that will contain the translated texts
        texts = []
        # Loop through each text in the received list
        for text in list_texts:
            # Translates the text to the language indicated in "language" and adds the translated text to the "texts" list
            texts.append(ts.translate_text(text, to_language=self.language))
        return texts  # Returns the list of translated texts

    def translate(self, text: str) -> str:
        """Translates a text to the language indicated in the "language" variable.

        Args:
            text (str): Text to translate.

        Returns:
            str: Translated text
        """

        # Translates the text to the language indicated in "language" and returns it.
        return ts.translate_text(text, to_language=self.language)

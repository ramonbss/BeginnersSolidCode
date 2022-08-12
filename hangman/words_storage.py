from typing import List


class HangMang_Words:

    @staticmethod
    def get_words_from_file(word_list_file_path: str) -> List[str]:

        with open(word_list_file_path, 'r') as words_file:
            hang_man_words = [word for word in words_file.readlines()]
            return hang_man_words

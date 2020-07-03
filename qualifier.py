"""
Use this file to write your solution for the Summer Code Jam 2020 Qualifier.

Important notes for submission:

- Do not change the names of the two classes included below. The test suite we
  will use to test your submission relies on existence these two classes.

- You can leave the `ArticleField` class as-is if you do not wish to tackle the
  advanced requirements.

- Do not include "debug"-code in your submission. This means that you should
  remove all debug prints and other debug statements before you submit your
  solution.
"""
import datetime
import typing
import re


class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    def __init__(self, field_type: typing.Type[typing.Any]):
        pass


class Article:
    """The `Article` class you need to write for the qualifier."""
    article_count = 0

    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self._content = content
        
        self.id = Article.article_count
        Article.article_count += 1

        self.last_edited = None
    
    @property
    def content(self) -> str:
        return self._content

    @content.setter
    def content(self, content: str) -> None:
        self._content = content
        self.last_edited = datetime.datetime.now()

    def __repr__(self) -> str:
        repr_str = '<Article '
        repr_str += 'title=' + '"' + self.title + '" '
        repr_str += 'author=' + "'" + self.author + "' "
        repr_str += 'publication_date=' + "'" + self.publication_date.isoformat() + "'>"
        return repr_str

    def __len__(self) -> int:
        return len(self.content)

    def __ge__(self, other) -> bool:
        return self.publication_date >= other.publication_date

    def __le__(self, other) -> bool:
        return self.publication_date <= other.publication_date

    def __gt__(self, other) -> bool:
        return self.publication_date > other.publication_date

    def __lt__(self, other) -> bool:
        return self.publication_date < other.publication_date
    
    def __eq__(self, other) -> bool:
        return self.publication_date == other.publication_date


    def short_introduction(self, n_characters: int) -> str:
        if n_characters <= len(self.content):
            ending_index = max(self.content.rfind(' ', 0, n_characters+1), self.content.rfind('\n', 0, n_characters+1))
            return self.content[:ending_index]
        else:   
            return self.content

    def most_common_words(self, n_words: int) -> typing.Dict[str, int]:
        common_words = {}
        last_index = 0
        word_list = []

        if n_words == 0:
            return common_words

        for i in range(len(self.content)):
            if self.content[i].isalpha() == False:
                word_list.append(self.content[last_index:i])
                last_index = i+1

        word_list.append(self.content[last_index:])

        word_list = [word.lower() for word in word_list if word.isalpha() == True]
        
        sorted_word_list = sorted(word_list, key=lambda x: (-word_list.count(x), word_list.index(x)))

        for word in sorted_word_list:
            if word in common_words:
                continue
            common_words[word] = word_list.count(word)
            n_words -= 1
            if n_words <= 0:
                break
        
        return common_words


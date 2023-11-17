# your code goes here!
class Anagram:
  def __init__(self, word):
    self.word = word 

  def match(self, word_list):
    matching = []
    for word in word_list:
      if self.is_anagram(word):
        matching.append(word)
    return matching

  def is_anagram(self, other_word):
    return sorted(self.word.lower()) == sorted(other_word.lower())
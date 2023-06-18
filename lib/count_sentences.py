#!/usr/bin/env python3

class MyString():

  def __init__(self, value = " "):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")

  @property
  def value(self):
      return self._value
    
  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    print("The value must be a string.")

  def is_sentence(self):
    suffix = "."
    return self.value.endswith(suffix)
    
    #   return True
    # else:
    #   return False
    
  def is_question(self):
    suffix = "?"
    return self.value.endswith(suffix)
  
  def is_exclamation(self):
    suffix = "!"
    return self.value.endswith(suffix)

  def count_sentences(self):
    self.value = self.value.replace("?", ".")
    self.value = self.value.replace("!", ".", 1)
    self.value = self.value.replace("...", ".")
    print(self.value)

    return self.value.count(".")



print((MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...").count_sentences()))
    
    # if value.endswith("."):
    #   return True
    # else:
    #   return False


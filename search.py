with open("words") as words:
  for word in words:
    word = word.strip()
    if len(word) == 5:
      score = 0
      for letter in "aeiou":
        if letter in word:
          score += 1 
      if score >= 4:
        print(word)



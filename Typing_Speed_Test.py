import time
import random

sentence = ["The quick brown fox jumps over the lazy dog.", "I love Python.","The sky is blue."]
sentence = random.choice(sentence)
print(sentence)

start_time = time.time()
user_input = input("write this sentence:")
end_time = time.time()
correct = 0
wrong = 0

for i in range(len(user_input)):
  
  if user_input[i] == sentence[i]:
    correct = correct + 1
    
  else:
    wrong = wrong + 1
    
time_taken = round(end_time - start_time, 2)

cps = round(len(sentence) / time_taken, 2)
wpm = (cps / 5) * 60

print("Your speed was", wpm, ".")
print(wpm, "Words per minute.")
print(cps, "Clicks per second.")
print(correct, "Characters correct.")
print(wrong, "Characters wrong.")

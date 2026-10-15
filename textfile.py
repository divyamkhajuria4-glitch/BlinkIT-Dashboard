s = "i like pyhton and i like ai"
words = s.split()
freq ={}
for w in words:
    freq[w] = freq.get(w,0)+1
print(freq)
print(freq['i'])
#WordCount.py
#Name: Miguel Alvarado
#Date: 2/26/2026
#Assignment: Lab 6

def main():
  textFile = open("gettysberg.txt", 'r')
  lineCount = 0
  wordCount = 0
  letterCount = 0
  for line in textFile:
    lineCount = lineCount + 1
    wordCount = wordCount + len(line.split())
    letterCount = letterCount + len(line)

  print("Lines:", lineCount)
  print("Words:", wordCount)
  print("Letters:", letterCount)


if __name__ == '__main__':
  main()

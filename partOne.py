def main():
    slow = input("Input ")
    myFunction(slow)

def myFunction(text):
  text =str.replace(text,' ', '...')
  print(text)
main()

import sys

def spelling_test(s, l):
    if not s:
        return True

    for index, word in enumerate(l):
        if s.startswith(word):
            l.pop(index)
            if spelling_test(s[len(word):], l):
                return True
            
    return False

def main():
    s = input()
    lines = sys.stdin.readlines()
    word_list = [line.strip() for line in lines]
    print(spelling_test(s, word_list))

if __name__ == "__main__":
    main()

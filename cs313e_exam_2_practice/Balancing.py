def generate_pd(n):
    if n % 2 == 1 or n == 0:
        return []

    ans = []
    backtrack(ans, n)
    return ans



def backtrack(ans, n, curr_balanced = None, num_left = 0, num_right = 0):
...


def main():
    n = int(input())

    print(generate_pd(n))

if __name__ == "__main__":
    main()

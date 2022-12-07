from kmp import kmp_search
import time


def main():
    print(kmp_search("ababcabcabababdac", "ababdac"))
    print(kmp_search("Some real text to show reliability of algo", "re"))
    print(kmp_search("Some real text to show reliability of algo", "vendetta"))


if __name__ == '__main__':
    start = time.process_time()
    main()
    end = time.process_time()
    print(end - start)

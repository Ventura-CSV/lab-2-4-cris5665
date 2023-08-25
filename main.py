def main():
    ##################################################
    # Comlete your code here
    ##################################################
    original_str = "Python Programming"
    sub1= original_str.replace("Python Programming", "Python ")
    sub2= original_str.replace("Python Programming", "Programming")
    merge_str= sub1 + sub2
    print(sub1)
    print(sub2)
    print(merge_str)
    pass


if __name__ == '__main__':
    main()

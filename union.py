if __name__ == "__main__":
    NumEnglish = input("Number of students for English Newspaper: ")
    RollEnglish = set(map(int, input("Roll number of students for English Newspaper: ").split()))
    NumFrench = input("Number of students for French Newspaper: ")
    RollFrench = set(map(int, input("Roll number of students for French Newspaper: ").split()))
    print (len(RollEnglish.union(RollFrench)))
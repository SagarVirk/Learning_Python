class MaxNo:
    def lists(self):
        n = int(input("Enter number of elements : "))
        lists=list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]
        lists = [int(i) for i in lists]
        max = lists[0]
        for number in lists:
            if number > max:
                max = number
        lists = max
        print(lists)



h = MaxNo()
h.lists()




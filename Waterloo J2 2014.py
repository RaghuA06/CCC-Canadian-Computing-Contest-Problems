# Raghu Alluri

num = int(input())
votes = input().upper()

if len(votes) == num:
    A = votes.count('A')
    B = votes.count('B')
    if A > B:
        print('A')
    elif B > A:
        print('B')
    elif A == B:
        print('Tie')

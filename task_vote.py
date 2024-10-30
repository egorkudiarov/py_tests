def vote(votes: list[int]) -> int:
    unique_votes = list(set(votes))
    return max([(votes.count(v), v) for v in unique_votes])[1]
"""
if __name__ == '__main__':
    print(vote([1,1,1,2,3]))
    print(vote([1,2,3,2,2]))
"""
# map color to number
C = {
        0 : 'orange',
        1 : 'yellow',
        2 : 'blue',
        3 : 'green'
}

# 2D array to answer
def find_majority(Ranks: list) -> (list, list):
    # find totals
    Totals = [0, 0, 0, 0]
    for row in range(len(Ranks)):
        for col in range(len(Ranks[0])):
            Totals[col] += Ranks[row][col]
    print(Totals)
    # find majority
    ans = []
    for i, total in enumerate(Totals):
        if total == max(Totals):
            ans.append(C[i])
    return (ans, Totals)

def check_for_duplicates(Ranks: list) -> bool:
    return not all([len(set(row)) == len(row) for row in Ranks])


import sys

def isValidGuess(boggle2d, text, verbose):
    # Get size of boggle2d
    # Check pre-conditions
    rows = len(boggle2d)
    assert rows > 0
    cols = len(boggle2d[0])
    assert cols > 0

    assert len(text) > 0

    # Assume false
    isValid = False

    for i in range(0, rows):
        for j in range(0, cols):

            # Run modified DFS for each initial letter of text
            if boggle2d[i][j] == text[0]:

                # initialize visit graph with all zeros
                isVisited = [[0] * cols for r in range(rows)]

                # index to denote position in text
                index = 0

                # visit init letter
                if dfsVisit(boggle2d, isVisited, i, j, rows, cols, index, text, verbose) == True:
                    isValid = True
                    break

    if verbose:
        if isValid:
            print text, 'is a valid guess'
        else:
            print text, 'is NOT a valid guess'

    return isValid

#depth first search
def dfsVisit(boggle2d, isVisited, i, j, rows, cols, index, text, verbose):

    # color visited
    isVisited[i][j] = 1

    # If we reached last letter and visited then terminate successfully
    if index == len(text) - 1:
        return True

    else:
        # traverse neighbors
        for [ni, nj] in adj(i, j, rows, cols):

            # path is unvisited and fits patterns
            if isVisited[ni][nj] == 0 and boggle2d[ni][nj] == text[index + 1]:
                return dfsVisit(boggle2d, isVisited, ni, nj, rows, cols, index + 1, text, verbose)

        return False


def adj(i, j, rows, cols):
    assert i >= 0 and j >= 0 and rows >= 0 and cols >= 0 and i < rows and j < cols

    neighbors = []

    if i > 0:
        if j > 0:
            neighbors.append([i - 1, j - 1])
        neighbors.append([i - 1, j])
        if j < cols - 1:
            neighbors.append([i - 1, j + 1])

    if j > 0:
        neighbors.append([i, j - 1])

    if j < cols - 1:
        neighbors.append([i, j + 1])

    if i < rows - 1:
        if j > 0:
            neighbors.append([i + 1, j - 1])
        neighbors.append([i + 1, j])
        if j < cols - 1:
            neighbors.append([i + 1, j + 1])

    return neighbors


if __name__ == '__main__':

    if len(sys.argv) == 3:

        # Read boggle array file
        try:
            with open(sys.argv[1]) as textFile:
                boggle2d = [line.split() for line in textFile]
        except Exception as e:
            print 'ERROR: cannot read/parse input file for boggle array. Each line must contain a single row of the array. Letters must be seperated with a space.'

        word = sys.argv[2]

        # Check if valid guess
        print isValidGuess(boggle2d, word, False)

    else:
        print 'usage: python GuessController.py <boggle_2d_array.txt> <test_word>'

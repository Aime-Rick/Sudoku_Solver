from backtracking_solving_method import Backtracking

def solve_sudoku(file_path):
    char_lists = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line_list = []
                for char in line.rstrip('\n'):
                    if char.isdigit() in range(1,10):
                        line_list.append(int(char))
                    else:
                        line_list.append(0)
                char_lists.append(line_list)
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except IOError:
        print(f"An error occurred while reading the file at {file_path}.")
    
    gameboard = Backtracking(char_lists)
    print(f'Puzzle to solve:\n{gameboard}')
    if gameboard.solver():
        print(f'Solved puzzle:\n{gameboard}')
    else:
        print('The provided puzzle is unsolvable.')
    return gameboard


# Vous pouvez modifier le contenu du fichier exemple_sudoku.txt pour résoudre un nouvel exemple sudoku.
 
solve_sudoku('exemple_sudoku.txt')

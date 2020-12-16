def paint_cell(cell):
    pass


def possible_moves(i, j, cells, N, queue, move):
    if N + 1 > i + 1 and N - 1 > j >= 0 and cells[i + 1][j][2] == 0 and move > 0 and cells[i + 1][j] not in queue:
        queue.append(cells[i + 1][j])
        paint_cell(cells[i + 1][j])
        possible_moves(i + 1, j, cells, N, queue, move - 1)
    if i - 1 >= 0 and N - 1 > j >= 0 and cells[i - 1][j][2] == 0 and move > 0 and cells[i - 1][j] not in queue:
        queue.append(cells[i - 1][j])
        paint_cell(cells[i - 1][j])
        possible_moves(i - 1, j, cells, N, queue, move - 1)
    if N + 1 > i >= 0 and N - 1 > j + 1 and cells[i][j + 1][2] == 0 and move > 0 and cells[i][j + 1] not in queue:
        queue.append(cells[i][j + 1])
        paint_cell(cells[i][j + 1])
        possible_moves(i, j + 1, cells, N, queue, move - 1)
    if N + 1 > i >= 0 and j - 1 >= 0 and cells[i][j - 1][2] == 0 and move > 0 and cells[i][j - 1] not in queue:
        queue.append(cells[i][j - 1])
        paint_cell(cells[i][j - 1])
        possible_moves(i, j - 1, cells, N, queue, move - 1)

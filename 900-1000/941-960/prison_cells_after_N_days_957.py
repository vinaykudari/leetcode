
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

------------------------------Pattern-Matching---------------------------

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        N = N%14
        if N == 0:
            N = 14
        for _ in range(N):
            prev = cells.copy()
            cells[0] = cells[7] = 0
            for i in range(1, 7):
                if prev[i-1] == prev[i+1]:
                    cells[i] = 1
                else:
                    cells[i] = 0
        return cells

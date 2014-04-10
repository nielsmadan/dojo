//Any live cell with fewer than two live neighbours dies, as if caused by under-population.
//Any live cell with two or three live neighbours lives on to the next generation.
//Any live cell with more than three live neighbours dies, as if by overcrowding.
//Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
object GameOfLife {
  def main(args: Array[String]) {}
}

class Board(cols: Int, rows: Int) {
  var cells: List[List[Cell]] =
    for (i <- List.range(0, cols))
      yield for (j <- List.range(0, rows))
        yield DeadCell

  def getCell(col: Int, row: Int) = {
    cells(col)(row)
  }

  def setCell(col: Int, row: Int, newCell: Cell) = {
    val updatedCellsCol = cells(col).updated(row,newCell)
    cells = cells.updated(col, updatedCellsCol)
  }

  def isCellOnBoard(col: Int, row: Int) = {
    (row >= 0 && row < cells(0).length) && (col >= 0 && col < cells.length)
  }

  def getNeighbors(col: Int, row: Int) = {
    for (
        i <- List.range(col - 1, col + 2);
        j <- List.range(row - 1, row + 2)  if ((i != col  || j != row) && isCellOnBoard(i, j))
      )
      yield cells(i)(j)
  }

  def countAliveNeighbors(col: Int, row: Int): Int = {
    getNeighbors(col, row).count((x: Cell) => ! x.isDead)
  }

  def isAliveNextGen(aliveNeighborCount: Int, currentCell: Cell) = (aliveNeighborCount, currentCell) match {
    case (3, _) => AliveCell
    case (2, AliveCell) => AliveCell
    case _ => DeadCell
  }

  def nextGeneration() = {
    val newBoard = new Board(cells.length, cells(0).length)

    for (colIndex <- List.range(0, cells.length); rowIndex <- List.range(0, cells(0).length)) {
      val cell = getCell(colIndex, rowIndex)
      val aliveNeighborCount = countAliveNeighbors(colIndex, rowIndex)
      newBoard.setCell(colIndex, rowIndex, isAliveNextGen(aliveNeighborCount, cell))
    }

    newBoard
  }
}

trait Cell {
  val isDead: Boolean
}

object AliveCell extends Cell  {
  override val isDead = false
}

object DeadCell extends Cell  {
  override val isDead = true
}

import collection.mutable.Stack
import org.scalatest._

class GameOfLifeSpec extends FlatSpec with Matchers {
  it should "construct a board with dead cells" in {
    val board: Board = new Board(1, 1)
    board.getCell(0, 0).isDead should be (true)
  }

  it should "be possible to make a cell be alive" in {
    val board: Board = new Board(1, 1)
    board.setCell(0, 0, AliveCell)
    board.getCell(0, 0).isDead should be (false)
  }

  it should "construct a bigger board with dead cells" in {
    val board: Board = new Board(2, 1)
    board.getCell(0, 0).isDead should be (true)
    board.getCell(1, 0).isDead should be (true)
  }

  it should "be possible to have both alive and dead cells on a board" in {
    val board: Board = new Board(2, 1)
    board.setCell(0, 0, AliveCell)
    board.getCell(0, 0).isDead should be (false)
    board.getCell(1, 0).isDead should be (true)
  }

  it should "get no neighbors for a board with only one cell" in {
    val board: Board = new Board(1, 1)
    val neighbors: List[Cell] = board.getNeighbors(0, 0)
    neighbors.isEmpty should be (true)
  }

  it should "return 8 dead neighbors for the middle cell of a newly constructed 3x3 board" in {
    val board: Board = new Board(3, 3)
    val neighbors: List[Cell] = board.getNeighbors(1, 1)
    val expectedNeighbors: List[Cell] = for (i <- List.range(0, 8)) yield DeadCell

    neighbors should be (expectedNeighbors)
  }


  it should "return a combination of 8 dead and alive cells on a 3x3 board with some alive cells" in {
    val board: Board = new Board(3, 3)
    board.setCell(1, 2, AliveCell)

    val neighbors: List[Cell] = board.getNeighbors(1, 1)
    var expectedNeighbors: List[Cell] = for (i <- List.range(0, 8)) yield DeadCell

    expectedNeighbors = expectedNeighbors.updated(4, AliveCell)
    neighbors should be (expectedNeighbors)
  }

  it should "return three neighbors for a corner cell" in {
    val board: Board = new Board(3, 3)
    var expectedNeighbors: List[Cell] = for (i <- List.range(0, 3)) yield DeadCell

    board.getNeighbors(0, 0) should be (expectedNeighbors)
    board.getNeighbors(0, 2) should be (expectedNeighbors)
    board.getNeighbors(2, 0) should be (expectedNeighbors)
    board.getNeighbors(2, 2) should be (expectedNeighbors)
  }

  it should "return no alive neighbors for a cell on a board with all dead cells" in {
    val board: Board = new Board(3, 3)

    board.countAliveNeighbors(1, 1) should be (0)
  }

  it should "return the correct number of alive cells when there is a mix" in {
    val board: Board = new Board(3, 3)
    board.setCell(0, 0, AliveCell)
    board.setCell(1, 0, AliveCell)
    board.setCell(2, 0, AliveCell)

    board.countAliveNeighbors(1, 1) should be (3)
  }

  it should "a board with no alive cells stays dead" in {
    val board: Board = new Board(3, 3)
    val newBoard = board.nextGeneration()
    newBoard.countAliveNeighbors(1,1) should be (0)
    newBoard.getCell(1,1).isDead should be (true)
  }

  it should "a board with a 2x2 box stays the same" in {
    val board: Board = new Board(4, 4)
    board.setCell(1, 1, AliveCell)
    board.setCell(1, 2, AliveCell)
    board.setCell(2, 1, AliveCell)
    board.setCell(2, 2, AliveCell)

    val newBoard = board.nextGeneration()

    newBoard.countAliveNeighbors(1, 1) should be (3)
    newBoard.getCell(1,1).isDead should be (false)

    newBoard.countAliveNeighbors(1, 2) should be (3)
    newBoard.getCell(1,2).isDead should be (false)

    newBoard.countAliveNeighbors(2, 1) should be (3)
    newBoard.getCell(2,1).isDead should be (false)

    newBoard.countAliveNeighbors(2, 2) should be (3)
    newBoard.getCell(2, 2).isDead should be (false)
  }

  it should "a board with a vertical three cell bar will change orientation" in {
    val board: Board = new Board(3, 3)
    board.setCell(1, 0, AliveCell)
    board.setCell(1, 1, AliveCell)
    board.setCell(1, 2, AliveCell)

    val newBoard = board.nextGeneration()

    newBoard.countAliveNeighbors(0, 1) should be (1)
    newBoard.getCell(0, 1).isDead should be (false)

    newBoard.countAliveNeighbors(1, 1) should be (2)
    newBoard.getCell(1, 1).isDead should be (false)

    newBoard.countAliveNeighbors(2, 1) should be (1)
    newBoard.getCell(2, 1).isDead should be (false)
  }
}

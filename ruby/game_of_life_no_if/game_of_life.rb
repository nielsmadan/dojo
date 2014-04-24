module AliveNextGen
    def add_yourself_next_gen(board)
        board += [AliveNoNeighbors.new(@x, @y)]
    end
end

module DeadNextGen
    def add_yourself_next_gen(board)
        board
    end
end

module CurrentlyDead
    def add_yourself(neighbor_set)

    end
end

# 1. get set of all neighbors of all alive cells
# 2. convert AliveNoNeighbors, DeadNoNeighbors
# 3. for each cell, add all alive neighbors
# 4. keep all cells that are alive next gen

class GameOfLife
    def initialize(alive_cells)
        @board = alive_cells
    end

    def get_candidates()
        candidates = Set.new @board.collect{| cell | AliveNoNeighbors.new(cell.x, cell.y)}

        @board.each do | cell |
            candidates += get_neighbors(cell)
            # neighbors = get_neighbors(cell)

            # neighbors.each do | n |
            #     @candidates.append(n)
            # end
        end

        candidates
    end

    def get_neighbors(cell)
        Set.new [DeadNoNeighbors.new(cell.x - 1, cell.y - 1),
                 DeadNoNeighbors.new(cell.x - 1, cell.y),
                 DeadNoNeighbors.new(cell.x, cell.y - 1),
                 DeadNoNeighbors.new(cell.x + 1, cell.y - 1),
                 DeadNoNeighbors.new(cell.x - 1, cell.y + 1),
                 DeadNoNeighbors.new(cell.x, cell.y + 1),
                 DeadNoNeighbors.new(cell.x + 1, cell.y),
                 DeadNoNeighbors.new(cell.x + 1, cell.y + 1)]
    end

    def get_alive_neighbors(cell)

    end

    def next_gen()
        candidates = get_candidates

        new_board = Set.new

        candidates.each do | candidate |
            alive_neighbors = get_alive_neighbors(candidate)

            alive_neighbors.each do | _ |
                candidates = candidates.delete(candidate)
                candidates += candidate.add_neighbor()
            end
        end

        candidates.each do | cell |
            new_board = cell.add_yourself_next_gen(new_board)
        end

        @board = new_board
    end

end

class Cell
    attr_reader :x, :y

    def initialize(x = 0, y = 0)
        @x = x
        @y = y
    end

    def eql?(other)
        @x == other.x && @y == other.y
    end

    def hash
        0
    end
end

class DeadNoNeighbors < Cell
    include DeadNextGen

    def add_neighbor
        return DeadOneNeighbor.new
    end
end

class DeadOneNeighbor < Cell
    include DeadNextGen

    def add_neighbor
        return DeadTwoNeighbors.new
    end
end

class DeadTwoNeighbors < Cell
    include DeadNextGen

    def add_neighbor
        return DeadThreeNeighbors.new
    end
end

class DeadThreeNeighbors < Cell
    include AliveNextGen

    def add_neighbor
        return DeadTooManyNeighbors.new
    end
end

class DeadTooManyNeighbors < Cell
    include DeadNextGen

    def add_neighbor
        return DeadTooManyNeighbors.new
    end
end

# -------------------------------------------------------------------
# -------------------------------------------------------------------
# -------------------------------------------------------------------

class AliveNoNeighbors < Cell
    include DeadNextGen

    def add_neighbor
        return AliveOneNeighbor.new
    end
end

class AliveOneNeighbor < Cell
    include DeadNextGen

    def add_neighbor
        return AliveTwoNeighbors.new
    end
end

class AliveTwoNeighbors < Cell
    include AliveNextGen

    def add_neighbor
        return AliveThreeNeighbors.new
    end
end

class AliveThreeNeighbors < Cell
    include AliveNextGen

    def add_neighbor
        return AliveTooManyNeighbors.new
    end
end

class AliveTooManyNeighbors < Cell
    include DeadNextGen

    def add_neighbor
        return AliveTooManyNeighbors.new
    end
end

require_relative 'game_of_life'

describe GameOfLife do
    it "return surrounding cells for the cell (1, 1)" do
        expected_set = Set.new [DeadNoNeighbors.new(0, 0), DeadNoNeighbors.new(0, 1), DeadNoNeighbors.new(1, 0),
                                DeadNoNeighbors.new(2, 0), DeadNoNeighbors.new(0, 2), DeadNoNeighbors.new(1, 2),
                                DeadNoNeighbors.new(2, 1), DeadNoNeighbors.new(2, 2)]

        GameOfLife.new([]).get_neighbors(DeadNoNeighbors.new(1, 1)).should eq(expected_set)
    end

    it "return surrounding cells for the cell (0, 0)" do
        expected_set = Set.new [DeadNoNeighbors.new(-1, -1), DeadNoNeighbors.new(-1, 0), DeadNoNeighbors.new(0, -1),
                                DeadNoNeighbors.new(1, -1), DeadNoNeighbors.new(-1, 1), DeadNoNeighbors.new(0, 1),
                                DeadNoNeighbors.new(1, 0), DeadNoNeighbors.new(1, 1)]

        GameOfLife.new([]).get_neighbors(DeadNoNeighbors.new(0, 0)).should eq(expected_set)
    end

    it "return all candidate alive cells for cell (0, 0)" do
        expected_set = Set.new [DeadNoNeighbors.new(-1, -1), DeadNoNeighbors.new(-1, 0), DeadNoNeighbors.new(0, -1),
                                DeadNoNeighbors.new(1, -1), DeadNoNeighbors.new(-1, 1), DeadNoNeighbors.new(0, 1),
                                DeadNoNeighbors.new(1, 0), DeadNoNeighbors.new(1, 1), AliveNoNeighbors.new(0, 0)]

        GameOfLife.new(Set.new [Cell.new(0, 0)]).get_candidates().should eq(expected_set)
    end

    it "return all candidate alive cells for cells (0, 0) and (1, 1)" do
        expected_set = Set.new [DeadNoNeighbors.new(-1, -1), DeadNoNeighbors.new(-1, 0), DeadNoNeighbors.new(0, -1),
                                DeadNoNeighbors.new(1, -1), DeadNoNeighbors.new(-1, 1), DeadNoNeighbors.new(0, 1),
                                DeadNoNeighbors.new(1, 0), DeadNoNeighbors.new(1, 1), AliveNoNeighbors.new(0, 0),
                                AliveNoNeighbors.new(1, 1), DeadNoNeighbors.new(2, 1), DeadNoNeighbors.new(1, 2),
                                DeadNoNeighbors.new(2, 2), DeadNoNeighbors.new(2, 0), DeadNoNeighbors.new(0, 2)]

        GameOfLife.new(Set.new [Cell.new(0, 0), Cell.new(1, 1)]).get_candidates().should eq(expected_set)
    end
end

describe AliveTwoNeighbors do
    it "should add an AliveNoNeighbors cell if asked to add itself" do
        cell = AliveTwoNeighbors.new(2, 1)
        next_gen_board = Set.new()
        next_gen_board = cell.add_yourself_next_gen(next_gen_board)
        next_gen_board.first.should be_an_instance_of AliveNoNeighbors
        next_gen_board.first.x.should eql(cell.x)
        next_gen_board.first.y.should eql(cell.y)
    end
end

describe DeadNoNeighbors do
    it "should return DeadOneNeighbor if a neighbor is added" do
        cell = DeadNoNeighbors.new()
        new_cell = cell.add_neighbor()
        new_cell.should be_an_instance_of DeadOneNeighbor
    end

    it "should add nothing to board if asked to add itself" do
        cell = DeadNoNeighbors.new()
        next_gen_board = Set.new()
        next_gen_board = cell.add_yourself_next_gen(next_gen_board)
        next_gen_board.should eql(Set.new)
    end
end

describe DeadOneNeighbor do
    it "should return DeadTwoNeighbors if a neighbor is added" do
        cell = DeadOneNeighbor.new()
        new_cell = cell.add_neighbor()
        new_cell.should be_an_instance_of DeadTwoNeighbors
    end
end

describe DeadTwoNeighbors do
    it "should return DeadTwoNeighbors if a neighbor is added" do
        cell = DeadTwoNeighbors.new()
        new_cell = cell.add_neighbor()
        new_cell.should be_an_instance_of DeadThreeNeighbors
    end
end

describe DeadThreeNeighbors do
    it "should return DeadTooManyNeighbors if a neighbor is added" do
        cell = DeadThreeNeighbors.new()
        new_cell = cell.add_neighbor()
        new_cell.should be_an_instance_of DeadTooManyNeighbors
    end
end

describe DeadTooManyNeighbors do
    it "should return DeadTooManyNeighbors if a neighbor is added" do
        cell = DeadTooManyNeighbors.new()
        new_cell = cell.add_neighbor()
        new_cell.should be_an_instance_of DeadTooManyNeighbors
    end
end

# -------------------------------------------------------------------
# -------------------------------------------------------------------
# -------------------------------------------------------------------

describe AliveNoNeighbors do
    it "should return AliveOneNeighbor if a neighbor is added" do
        cell = AliveNoNeighbors.new()
        new_cell = cell.add_neighbor()
        new_cell.should be_an_instance_of AliveOneNeighbor
    end
end

describe AliveOneNeighbor do
    it "should return AliveTwoNeighbors if a neighbor is added" do
        cell = AliveOneNeighbor.new()
        new_cell = cell.add_neighbor()
        new_cell.should be_an_instance_of AliveTwoNeighbors
    end
end

describe AliveTwoNeighbors do
    it "should return AliveTwoNeighbors if a neighbor is added" do
        cell = AliveTwoNeighbors.new()
        new_cell = cell.add_neighbor()
        new_cell.should be_an_instance_of AliveThreeNeighbors
    end
end

describe AliveThreeNeighbors do
    it "should return AliveTooManyNeighbors if a neighbor is added" do
        cell = AliveThreeNeighbors.new()
        new_cell = cell.add_neighbor()
        new_cell.should be_an_instance_of AliveTooManyNeighbors
    end
end

describe AliveTooManyNeighbors do
    it "should return AliveTooManyNeighbors if a neighbor is added" do
        cell = AliveTooManyNeighbors.new()
        new_cell = cell.add_neighbor()
        new_cell.should be_an_instance_of AliveTooManyNeighbors
    end
end

from agents import Direction
from agents import ReflexVacuumAgent, ModelBasedVacuumAgent, TrivialVacuumEnvironment

def test_move_forward():
    d = Direction("up")
    l1 = d.move_forward((0,0))
    assert l1 == (0,-1)
    d = Direction(Direction.R)
    l1 = d.move_forward((0,0))
    assert l1 == (1,0)
    d = Direction(Direction.D)
    l1 = d.move_forward((0,0))
    assert l1 == (0,1)
    d = Direction("left")
    l1 = d.move_forward((0,0))
    assert l1 == (-1,0)
    l2 = d.move_forward((1,0))
    assert l2 == (0,0)

def test_add():
    d = Direction(Direction.U)
    l1 = d + "right"
    l2 = d + "left"
    assert l1.direction == Direction.R
    assert l2.direction == Direction.L
    d = Direction("right")
    l1 = d.__add__(Direction.L)
    l2 = d.__add__(Direction.R)
    assert l1.direction == "up"
    assert l2.direction == "down"
    d = Direction("down")
    l1 = d.__add__("right")
    l2 = d.__add__("left")
    assert l1.direction == Direction.L
    assert l2.direction == Direction.R
    d = Direction(Direction.L)
    l1 = d + Direction.R
    l2 = d + Direction.L
    assert l1.direction == Direction.U
    assert l2.direction == Direction.D #fixed

def test_ReflexVacuumAgent() :
    # create an object of the ReflexVacuumAgent
    agent = ReflexVacuumAgent()
    # create an object of TrivialVacuumEnvironment
    environment = TrivialVacuumEnvironment()
    # add agent to the environment
    environment.add_thing(agent)
    # run the environment
    environment.run()
    # check final status of the environment
    assert environment.status == {(1,0):'Clean' , (0,0) : 'Clean'}

def test_ModelBasedVacuumAgent() :
    # create an object of the ModelBasedVacuumAgent
    agent = ModelBasedVacuumAgent()
    # create an object of TrivialVacuumEnvironment
    environment = TrivialVacuumEnvironment()
    # add agent to the environment
    environment.add_thing(agent)
    # run the environment
    environment.run()
    # check final status of the environment
    assert environment.status == {(1,0):'Clean' , (0,0) : 'Clean'}

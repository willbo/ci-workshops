import TravisCIWorkshop


def test_hello_world_works():
    assert TravisCIWorkshop.say_hello() == "Hello world!"


def test_hello_world_fails():
    assert TravisCIWorkshop.say_hello() == "Goodbye, cruel world!"

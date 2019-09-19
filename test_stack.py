from stackclass import MyStack

def test_size():
    s = MyStack()
    assert(s.size() == 0)
    s.push(1)
    assert(s.size() == 1)
    s.push(2)
    assert(s.size() == 2)
    s.pop()
    assert(s.size() == 1)

def test_is_empty():
    s = MyStack()
    assert(s.is_empty())
    s.push(1)
    assert(s.is_empty() == False)
    s.pop()
    assert(s.is_empty())

def test_top():
    s = MyStack()
    s.push(1)
    assert(s.top() == 1)
    s.push(2)
    assert(s.top() == 2)
    s.pop()
    assert(s.top() == 1)
    try:
        s = MyStack()
        s.top()
    except IndexError:
        print("Stack mustn`t be empty")

def test_pop():
    s = MyStack()
    s.push(1)
    s.pop()
    assert(s.size() == 0)
    s.push(1)
    s.push(2)
    s.pop()
    assert(s.size() == 1)
    assert(s.data[0] == 1)
    try:
        s = MyStack()
        s.pop()
    except IndexError:
        print("Stack mustn`t be empty")

def test_push():
    s = MyStack()
    s.push(1)
    assert(s.is_empty() == False)
    s.push(2)
    s.push(3)
    assert(s.top() == 3)

def test_repr():
    s = MyStack()
    assert(s.__repr__() == "MyStack('empty')")
    s.push(1)
    s.push(2)
    assert(s.__repr__() == "MyStack(1, 2)")

"""
* 스택(stack)이란 쌓아 올린다는 것을 의미한다. 
* 따라서 스택 자료구조라는 것은 책을 쌓는 것처럼 차곡차곡 쌓아 올린 형태의 자료구조를 말한다. 

* [Node Class]
* - item
* - pointer : 다음 node를 가리키므로 다음 node를 저장하고 아무것도 가리키지 않으면 None을 저장한다.

* [LinkedList]
* - head : 가장 첫 번째 node, node가 없으면 None을 저장한다.
* - length : int 타입, 현재 노드(데이터)의 개수를 의미한다.

* [Stack] : LinkedList를 상속받는다.
* - push(item) : Stack 자료구조에 item을 받아 노드로 만든 다음 밀어넣는다.
* - pop() : Stack 자료구조에서 마지막 node를 제거하고 해당 Item을 반환한다.
"""

"""
from typing import Optional, TypeVar, Generic

T = TypeVar("T", int, str, float)


class Node(Generic[T]):
    __slots__ = ("item", "pointer")

    def __init__(self, item: Generic[T], pointer: Optional["Node[T]"] = None):
        self.item = item
        self.pointer = pointer


class LinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None
        self.length = 0

    def __str__(self) -> str:
        result: str = ""
        if self.head is None:
            return result
        cur_node = self.head
        result += f"{cur_node.item}"
        while cur_node.pointer is not None:
            cur_node = cur_node.pointer
            result += f", {cur_node.item}"
        return result


# Generic[T] should typically come last in the base class list, but due to how Python's type system works, it needs to be placed after concrete classes
class Stack(LinkedList, Generic[T]):

    def push(self, item: T) -> None:
        new_node = Node(item=item)
        new_node.pointer = self.head  # 새 노드가 기존 head를 가리키게 함
        self.head = new_node  # head를 새 노드로 업데이트
        self.length += 1  # 스택 길이 증가

    def pop(self) -> T:
        if self.head is None:
            return IndexError("pop from empty stack")

        popped_item = self.head.item
        self.head = self.head.pointer
        self.length -= 1
        return popped_item

    def is_empty(self) -> bool:
        return self.head is None

    def peek(self) -> T:
        if not self.head:
            raise IndexError("peek from empty stack")
        return self.head.item


class Queue(LinkedList, Generic[T]):

    def __init__(self):
        super().__init__()
        self.tail: Optional[Node[T]] = None

    def enqueue(self, item: T) -> None:
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.pointer = new_node
            self.tail = new_node
        self.length += 1

    def dequeue(self) -> T:
        if self.head is None:
            raise IndexError("dequeue from empty queue")

        dequeued_item = self.head.item
        self.head = self.head.pointer
        if self.head is None:
            self.tail = None
        self.length -= 1
        return dequeued_item

if __name__ == "__main__":
    queue = Queue[int]()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue)
    print(queue.length)
    print("큐에서 dequeue한 값:", queue.dequeue())  # 출력: 큐에서 dequeue한 값: 10
    print("큐에서 dequeue한 값:", queue.dequeue())

if __name__ == "__main__":
    stack = Stack[int]()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack)
    print("스택에서 pop한 값:", stack.pop())  # 출력: 스택에서 pop한 값: 30
    print("스택에서 pop한 값:", stack.pop())

if __name__ == "__main__":
    # 1. 기본 기능 테스트
    def test_basic_operations():
        stack = Stack[int]()
        stack.push(1)
        stack.push(2)
        assert stack.pop() == 2
        assert stack.pop() == 1
        print("기본 기능 테스트 통과!")

    # 2. 에러 처리 테스트
    def test_error_handling():
        stack = Stack[str]()
        try:
            stack.pop()
            assert False, "비어있는 스택에서 pop 시 예외가 발생해야 함"
        except IndexError:
            print("에러 처리 테스트 통과!")

    # 3. 다양한 타입 테스트
    def test_multiple_types():
        stack_int = Stack[int]()
        stack_str = Stack[str]()
        stack_int.push(1)
        stack_str.push("hello")
        assert isinstance(stack_int.pop(), int)
        assert isinstance(stack_str.pop(), str)
        print("타입 테스트 통과!")

    # 모든 테스트 실행
    # test_basic_operations()
    # test_error_handling()
    # test_multiple_types()
"""

# Linkedlist 상속 안하는 방법
"""
* 스택(stack)이란 쌓아 올린다는 것을 의미한다. 
* 따라서 스택 자료구조라는 것은 책을 쌓는 것처럼 차곡차곡 쌓아 올린 형태의 자료구조를 말한다. 

* [Node Class]
* - item
* - pointer : 다음 node를 가리키므로 다음 node를 저장하고 아무것도 가리키지 않으면 None을 저장한다.

* [LinkedList]
* - head : 가장 첫 번째 node, node가 없으면 None을 저장한다.
* - length : int 타입, 현재 노드(데이터)의 개수를 의미한다.

* [Stack]
* - 내부적으로 LinkedList를 포함(composition)한다.
* - push(item) : Stack 자료구조에 item을 받아 노드로 만든 다음 밀어넣는다.
* - pop() : Stack 자료구조에서 마지막 node를 제거하고 해당 Item을 반환한다.

* [Queue]
* - 내부적으로 LinkedList를 포함(composition)한다.
* - enqueue(item) : Queue 자료구조에 item을 받아 노드로 만든 다음 추가한다.
* - dequeue() : Queue 자료구조에서 첫 번째 node를 제거하고 해당 Item을 반환한다.
"""

from typing import Optional, TypeVar, Generic

T = TypeVar("T", int, str, float)


class Node(Generic[T]):
    __slots__ = ("item", "pointer")

    def __init__(self, item: T, pointer: Optional["Node[T]"] = None):
        self.item = item
        self.pointer = pointer


class LinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None
        self.length = 0

    def __str__(self) -> str:
        values: list[str] = []
        current = self.head
        while current:
            values.append(str(current.item))
            current = current.pointer
        return ",".join(values)

    def push(self, item: T) -> None:
        new_node = Node(item=item)
        new_node.pointer = self.head  # 새 노드가 기존 head를 가리키게 함
        self.head = new_node  # head를 새 노드로 업데이트
        self.length += 1  # 리스트 길이 증가

    def pop_node(self) -> T:
        """
        LinkedList에서 노드를 제거하고 아이템을 반환합니다.
        스택의 pop과 큐의 dequeue에 사용됩니다.
        """
        if self.head is None:
            raise IndexError("pop from empty list")
        popped_item = self.head.item
        self.head = self.head.pointer
        self.length -= 1
        return popped_item

    def append(self, item: T) -> None:
        """
        LinkedList의 꼬리에 노드를 추가합니다.
        Queue의 enqueue에 사용됩니다.
        """
        new_node = Node(item=item)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.pointer:
                current = current.pointer
            current.pointer = new_node
        self.length += 1


class Stack(Generic[T]):
    def __init__(self):
        self.linked_list = LinkedList[T]()  # 내부에 LinkedList 인스턴스를 포함

    def push(self, item: T) -> None:
        self.linked_list.push(item)  # LinkedList의 push 메서드 호출

    def pop(self) -> T:
        return self.linked_list.pop_node()  # LinkedList의 pop_node 메서드 호출

    def is_empty(self) -> bool:
        return self.linked_list.head is None

    def peek(self) -> T:
        if self.linked_list.head is None:
            raise IndexError("peek from empty stack")
        return self.linked_list.head.item

    def __str__(self) -> str:
        return str(self.linked_list)  # LinkedList의 __str__ 메서드 사용


class Queue(Generic[T]):
    def __init__(self):
        self.linked_list = LinkedList[T]()  # 내부에 LinkedList 인스턴스를 포함
        self.tail: Optional[Node[T]] = None  # 큐의 꼬리를 추적

    def enqueue(self, item: T) -> None:
        self.linked_list.append(item)
        if self.linked_list.length == 1:
            self.tail = self.linked_list.head
        else:
            # tail을 업데이트할 필요 없이 append 메서드가 이미 연결함
            pass

    def dequeue(self) -> T:
        return self.linked_list.pop_node()

    def is_empty(self) -> bool:
        return self.linked_list.head is None

    def __str__(self) -> str:
        return str(self.linked_list)  # LinkedList의 __str__ 메서드 사용


# 테스트 코드
if __name__ == "__main__":
    # Stack 테스트
    stack = Stack[int]()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(f"Stack 상태: {stack}")  # 출력: Stack 상태: 30,20,10
    print("스택에서 pop한 값:", stack.pop())  # 출력: 스택에서 pop한 값: 30
    print("스택에서 pop한 값:", stack.pop())  # 출력: 스택에서 pop한 값: 20
    print(f"스택 상태: {stack}")  # 출력: 스택 상태: 10

    # Queue 테스트
    queue = Queue[int]()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(f"Queue 상태: {queue}")  # 출력: Queue 상태: 10,20,30
    print("큐에서 dequeue한 값:", queue.dequeue())  # 출력: 큐에서 dequeue한 값: 10
    print("큐에서 dequeue한 값:", queue.dequeue())  # 출력: 큐에서 dequeue한 값: 20
    print(f"Queue 상태: {queue}")  # 출력: Queue 상태: 30

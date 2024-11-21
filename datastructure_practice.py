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

from typing import Optional
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

    # O(n) 시간 복잡도
    # def enqueue(self, item: T) -> None:
    #     new_node = Node(item)
    #     if self.head is None:
    #         self.head = new_node
    #     else:
    #         cur_node = self.head
    #         while cur_node.pointer is not None:
    #             cur_node = cur_node.pointer
    #         cur_node.pointer = new_node

    #     self.length += 1

    # 위 코드의 시간복잡도(리스트의 끝까지 순회)는 아래와 같이 O(1) 시간 복잡도로 해결 가능

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

'''
if __name__ == "__main__":
    queue = Queue[int]()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue)
    print(queue.length)
    print("큐에서 dequeue한 값:", queue.dequeue())  # 출력: 큐에서 dequeue한 값: 10
    print("큐에서 dequeue한 값:", queue.dequeue())
''
"""
if __name__ == "__main__":
    stack = Stack[int]()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack)
    print("스택에서 pop한 값:", stack.pop())  # 출력: 스택에서 pop한 값: 30
    print("스택에서 pop한 값:", stack.pop())
"""
"""
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

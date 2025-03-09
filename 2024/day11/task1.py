import time


# solving this problem using linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_data(filename):
    return list(map(int, open(filename).read().split()))


def decide_category(num):
    # 0 - If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    # 1 - Even Digits
    # 2 - None of the above rules apply
    if num == 0:
        return 0
    if len(str(num)) % 2 == 0:
        return 1
    return 2


def linked_list_count(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count


def solve(nums, blinks):
    list_head = head = ListNode(nums[0])
    for num in nums[1:]:
        node = ListNode(num)
        head.next = node
        head = head.next

    for _ in range(blinks):
        head = list_head
        while head:
            category = decide_category(head.val)
            if category == 0:
                head.val = 1
            elif category == 2:
                head.val *= 2024
            else:
                temp = head.val
                num_digits = len(str(temp))
                half_digits = num_digits // 2
                divisor = 10**half_digits
                head.val = temp // divisor
                node = ListNode(temp % divisor)
                node.next = head.next
                head.next = node
                head = head.next
            head = head.next
    return linked_list_count(list_head)


if __name__ == "__main__":
    start_time = time.time()
    data = get_data("data.txt")
    result = solve(data, 25)
    print(result)
    end_time = time.time()
    print(f"execution time: {(end_time - start_time):.06f} seconds")

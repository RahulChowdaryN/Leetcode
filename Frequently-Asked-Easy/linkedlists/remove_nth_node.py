length = 0
current = head
while current is not None:
    length = length + 1
    current = current.next
cnt = length - n
l = 0
prev = None
cu = head
while cu is not None:
    l = l + 1
    if l == cnt + 1:
        break
    prev = cu
    cu = cu.next
if prev:
    prev.next = cu.next
else:
    if length == 1:
        head = None
    else:
        head = head.next
return head
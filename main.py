import random

def main_process(boxes, num_attempts):
    for prisoner in range(n_prisoners):
        found = False
        box_to_open = prisoner
        for _ in range(num_attempts):
            if boxes[box_to_open] == prisoner:
                found = True
                break
            box_to_open = boxes[box_to_open]
        if not found:
            return False
    return True

if __name__ == '__main__':
    n_prisoners = 100
    boxes = list(range(n_prisoners))
    
    random.shuffle(boxes)
    num_attempts = n_prisoners // 2
    success = main_process(boxes, num_attempts)

    if success:
        print("성공!!!")
    else:
        print("실패...")
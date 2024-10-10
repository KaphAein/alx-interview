#!/usr/bin/python3
'''Locked Boxes Module'''


def canUnlockAll(boxes):
    '''Locked Boxes Function'''
    opened_boxes = set([0])
    keys = set(boxes[0])

    while keys:
        new_key = keys.pop()
        if new_key < len(boxes) and new_key not in opened_boxes:
            opened_boxes.add(new_key)
            keys.update(boxes[new_key])

    return len(opened_boxes) == len(boxes)

#!/usr/bin/python3

"""
Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
"""
def canUnlockAll(boxes):
	if type(boxes) is not list:
		return False
	elif (len(boxes)) == 0:
        	return False
    	for k in range(1, len(boxes) - 1):
        	boxes_checked = False
       		for idx in range(len(boxes)):
            		boxes_checked = k in boxes[idx] and k != idx
            	if boxes_checked:
                	break
        if boxes_checked is False:
            	return boxes_checked
    	return True

#  File: Meet.py

#  Description: Determine earlist meet time interval for two people

#  Student Name: Austine Do

#  Student UT EID: ahd589

#  Course Name: CS 313E

#  Unique Number: 52590

import sys

'''
    person1: List[List[int]]
    person2: List[List[int]]
    duration: int
    return type: List[int]
'''
def earliestPossibleMeeting(person1, person2, duration):
	# returns empty list in the case neither people have free dates
	if not person1 or not person2:
		return []

	earliest_meeting = []

	for p1_interval in person1:
		for p2_interval in person2:
			start = max(p1_interval[0], p2_interval[0])
			end = min(p1_interval[1], p2_interval[1])

			if end - start >= duration:
				earliest_meeting = [start, start + duration]

	return earliest_meeting


def main():
        #test_cases()

	# read the input data and create a list of lists for each person
	f = sys.stdin
	# read in the duration
	dur = int(f.readline().strip())
	# person 1's number of avalible slots
	num1 = int(f.readline().strip())
	p1 = []
	for x in range(num1):
		line = f.readline()
		l = line.strip().split()
		tmp = [int(l[0]), int(l[1])]
		p1.append(tmp)

	# person 2's number of avalible slots
	num2 = int(f.readline().strip())
	p2 = []
	for x in range(num2):
		line = f.readline()
		l = line.strip().split()
		tmp = [int(l[0]), int(l[1])]
		p2.append(tmp)

	print(earliestPossibleMeeting(p1,p2,dur))

if __name__ == "__main__":
  main()

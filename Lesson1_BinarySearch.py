"""
Jovian.ai

Lesson 1:
	Binary Search
	>> Determine the start (low) and end position (high) of the list
	>> Get the middle element of the list
	>> If the middle element == query, query is FOUND
		** list is in increasing order **
	>> If the query is greater than the middle element:
		>> Query must be on the left side of the middle emelemt, high = middle-1
	>> If the query is smaller tha the middle element:
		>> Query must be on the right side of the middle element, low = middle+1
	
	Run the loop while the low is less than the high
		>> if the conditional statement has been broken:
			>> return 0

"""




cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
output = 3


def find_query(cards, query):
	low = 0
	high = len(cards) - 1

	while low <= high:
		mid = (high + low) // 2
		mid_element = cards[mid]

		if mid_element == query:
			return f"Found at {mid}"
		elif mid_element < query:
			high = mid - 1
		elif mid_element > query:
			low = mid + 1

		return 0

search = find_query(cards, query)
print(search)

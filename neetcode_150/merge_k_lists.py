import heapq


class Solution:
    def mergeKLists(self, lists):
        heap = []

        # Step 1: Push the first element of each list into the heap
        for i, lst in enumerate(lists):
            if lst:  # Ensure the list is not empty
                heapq.heappush(
                    heap, (lst[0], i, 0)
                )  # (value, list_index, element_index)

        result = []

        # Step 2: Extract the min element and push the next element from the same list
        while heap:
            value, list_index, element_index = heapq.heappop(heap)
            result.append(value)

            # Push the next element from the same list
            if element_index + 1 < len(lists[list_index]):
                heapq.heappush(
                    heap,
                    (
                        lists[list_index][element_index + 1],
                        list_index,
                        element_index + 1,
                    ),
                )

        return result

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key=lambda x: x.start)

        cache = []   # stores end time of meetings in each room

        for e in intervals:
            assigned = False

            for i in range(len(cache)):
                if cache[i] <= e.start:   # room becomes free
                    cache[i] = e.end
                    assigned = True
                    break

            if not assigned:
                cache.append(e.end)

        return len(cache)
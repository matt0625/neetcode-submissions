class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # strategy: for each car, calculate the time it reaches the destination at target (O(n))
        # then we can iterate once more and compare the times to the ones ahead of it initially
        # if larger, creates a fleet 
        # need to sort by position descending in order to compare only cars who are nearest
        
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        target_times = []
        for pos, vel in cars:
            distance_left = target - pos
            target_times.append(distance_left/vel)

        fleets = 1
        last_fleet_time = target_times[0]
        for i in range(1, len(target_times)):
            time = target_times[i]
            if time > last_fleet_time:
                fleets += 1
                last_fleet_time = time

        return fleets
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        fleet_time = 0.0
        fleet = 0

        for pos, spd in sorted(zip(position, speed), reverse=True):
            time = (target - pos) / spd

            if time > fleet_time:
                fleet_time = time
                fleet += 1
        
        return fleet
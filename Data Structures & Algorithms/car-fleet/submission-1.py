class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        We had a clunky logic in the solution above, while all we need to know is if two cars will meet before the
        destination.
        The key here is comparing the arrival time as if there is no congestion, noted as t_i
        if t_i > t_prev, no meet up, t_prev = t_i, car_fleet + 1, move to next car
        else, meet up, move to next car
        """
        car_fleet = 0
        t_prev = 0
        n = len(position)
        if n == 0:
            return 0
        pos_speed_pair = list(sorted(zip(position, speed), key=lambda pair: pair[0], reverse=True))

        for pos, spd in pos_speed_pair:
            t_i = (target - pos) / spd
            if t_i > t_prev:
                t_prev = t_i
                car_fleet += 1

        return car_fleet
        
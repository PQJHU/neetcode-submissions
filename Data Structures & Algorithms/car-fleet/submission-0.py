class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        A car can only meet another car if and only if one car is ahead of another while the speed is lower
        if we sort the cars by their positions, from closest to the destination to farthest
        inspired by the daily_temperature question, we can use a variable to bookkeep if the blocking car
        car_fleet = 0
        blocking_car = 1
        sort the position and speed lists by position

        for i = 1, ... n-1:
            compare position and speed between car i and blocking car
            if catch up, car_fleet += 1, keep the same blocking car
            if not catch up, move blocking to car i
            catching up criteria:
            catching up time t = (p_2 - p_1)/(s_1 -s_2),
            catching up position p_1+s_1 * t <=dest

        or, maybe another way counting down the car_fleet from n, if meet up, car_fleet -=1
        """
        car_fleet = 0
        n = len(position)
        pos_speed = list(sorted(zip(position, speed), key=lambda pair: pair[0], reverse=True))
        blocking_car = 0
        for i in range(1, n):

            # block_car_idx = blocking_car[-1]
            former_pos, former_speed = pos_speed[blocking_car][0], pos_speed[blocking_car][1]
            latter_pos, latter_speed = pos_speed[i][0], pos_speed[i][1]

            if former_speed >= latter_speed:
                # eliminate the situation of same speed
                if latter_pos != former_pos:
                    # doesn't catch up for former car
                    blocking_car = i
                    car_fleet += 1
            else:
                # could catch up
                catch_time = (latter_pos-former_pos)/(former_speed - latter_speed)
                catch_pos = former_pos + former_speed * catch_time

                if catch_time < 0 or catch_pos > target:
                    # not catch up
                    blocking_car = i
                    car_fleet += 1
                # catch up, the latter car essentially becomes the former car, so the block car is still the former
        return car_fleet + 1        
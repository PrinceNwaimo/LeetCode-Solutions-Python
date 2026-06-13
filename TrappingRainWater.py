from turtle import right


class TrappingRainWater:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_seen_right = 0
        max_seen_left = 0
        max_seen = [0] * len(height)
        rain_water = 0
        
        for i in range(len(height) - 1, -1, -1):
            if height[i] > max_seen_right:
                max_seen[i] = height[i]
                max_seen_right = height[i]
            else:
                max_seen[i] = max_seen_right
        
        for i in range(0, len(height)):
            if height[i] > max_seen_left:
                max_seen_left = height[i]
            rain_water = rain_water + max(0, min(max_seen[i], max_seen_left) - height[i])
        
        return rain_water
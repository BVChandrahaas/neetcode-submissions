class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        astro_stack = []

        for asteroid in asteroids:
            destroyed = False

            while astro_stack and astro_stack[-1] >=0 and asteroid < 0:
                if abs(asteroid) > astro_stack[-1]:
                    astro_stack.pop()
                    # astro_stack.append(asteroid)
                elif abs(asteroid) < astro_stack[-1]:
                    destroyed = True
                    break
                elif abs(asteroid) == astro_stack[-1]:
                    astro_stack.pop()
                    destroyed = True
                    break
            if not destroyed:
                astro_stack.append(asteroid)

        return astro_stack


        
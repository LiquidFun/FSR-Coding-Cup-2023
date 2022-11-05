target_width = int(input())
bricks = [int(a) for a in input().split()]
assert len(bricks) == 3
assert 1 <= target_width <= 1e9
assert all(0 <= a <= 1e9 for a in bricks)


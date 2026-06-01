from sol import Solution

def test_ship_within_days():
    solver = Solution()
    
    # Test case 1 (User's example)
    weights1 = [3, 2, 2, 4, 1, 4]
    days1 = 3
    # Expected: 6
    assert solver.shipWithinDays(weights1, days1) == 6, f"Failed Case 1. Expected 6, got {solver.shipWithinDays(weights1, days1)}"
    
    # Test case 2 (LeetCode standard example 1)
    weights2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    days2 = 5
    # Expected: 15
    assert solver.shipWithinDays(weights2, days2) == 15, f"Failed Case 2. Expected 15, got {solver.shipWithinDays(weights2, days2)}"

    # Test case 3 (LeetCode standard example 2)
    weights3 = [3, 2, 2, 4, 1, 4]
    days3 = 3
    # Expected: 6
    assert solver.shipWithinDays(weights3, days3) == 6, f"Failed Case 3"

    # Test case 4 (LeetCode standard example 3)
    weights4 = [1, 2, 3, 1, 1]
    days4 = 4
    # Expected: 3
    assert solver.shipWithinDays(weights4, days4) == 3, f"Failed Case 4. Expected 3, got {solver.shipWithinDays(weights4, days4)}"

    print("All tests passed successfully!")

if __name__ == "__main__":
    test_ship_within_days()

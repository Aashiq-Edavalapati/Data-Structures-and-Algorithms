# -----------------------------------------------------------------------------
# Problem: Lemonade Change
# -----------------------------------------------------------------------------
# @question:
# Each lemonade costs $5. Customers pay with either $5, $10, or $20 bills.
# You must provide correct change for each customer in the order they arrive.
#
# Return True if you can serve all customers with proper change, False otherwise.
#
# -----------------------------------------------------------------------------
# @pattern: Greedy (Always give change in the best possible way now)
# - For a $5 bill: just collect it.
# - For a $10 bill: must give one $5 as change.
# - For a $20 bill: prefer giving one $10 + one $5 (keep $5 bills safe),
#   else give three $5 bills.
#
# Why Greedy Works:
# * Greedy-choice property:
#   Giving back change with larger bills first keeps smaller bills
#   for flexibility later.
# * Optimal substructure:
#   After each transaction, the state (count of $5s and $10s) reduces
#   to the same smaller problem.
#
# Greedy Pattern:
# - "Extreme First" → always use the largest bill possible for change.
#
# -----------------------------------------------------------------------------
# @method (easy steps):
# 1. Track counts of $5 and $10 bills.
# 2. Iterate through each bill:
#    - If bill == 5 → increment fives.
#    - If bill == 10 → need one $5 as change.
#    - If bill == 20 → try (10 + 5) first, else (5 + 5 + 5).
#    - If not possible → return False.
# 3. If all customers processed → return True.
# Time Complexity: O(N)
# Space Complexity: O(1)

# ==============================================================================

def canSell(bills):
    """
    Simulates the lemonade change problem using a greedy approach.
    """
    fives, tens = 0, 0

    for bill in bills:
        if bill == 5:
            fives += 1
        elif bill == 10:
            if fives < 1:
                return False
            fives -= 1
            tens += 1
        else:  # bill == 20
            if tens > 0 and fives > 0:
                tens -= 1
                fives -= 1
            elif fives >= 3:
                fives -= 3
            else:
                return False
    return True

# -----------------------------------------------------------------------------
# Test Cases
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    testCases = [
        [5, 5, 5, 10, 20],  # True → change always possible
        [5, 5, 10, 10, 20],  # False → last $20 can't be changed
        [5, 5, 5, 5, 10, 20],  # True → enough 5s for last change
        [5, 10, 5, 10, 20],  # False → not enough small bills
        [5, 5, 10],  # True → easy changes
        [5, 20],  # False → no change for $20
        [5, 5, 5, 5, 5, 10, 10, 10, 20],  # True → multiple big changes
    ]

    # Dry run for a failing test case: [5, 5, 10, 10, 20]
    # Initial state: fives = 0, tens = 0
    #
    # 1. bill = 5:
    #    fives becomes 1.
    #    State: fives = 1, tens = 0
    #
    # 2. bill = 5:
    #    fives becomes 2.
    #    State: fives = 2, tens = 0
    #
    # 3. bill = 10:
    #    fives is >= 1, so we give one $5 as change.
    #    fives becomes 1, tens becomes 1.
    #    State: fives = 1, tens = 1
    #
    # 4. bill = 10:
    #    fives is >= 1, so we give one $5 as change.
    #    fives becomes 0, tens becomes 2.
    #    State: fives = 0, tens = 2
    #
    # 5. bill = 20:
    #    Check for one $10 and one $5:
    #    tens > 0 and fives > 0 is (2 > 0 and 0 > 0) which is False.
    #    Check for three $5s:
    #    fives >= 3 is (0 >= 3) which is False.
    #    Neither change combination is possible.
    #    Return False.

    i = 0
    for bills in testCases:
        print(f'TestCase {i}: {canSell(bills)}')
        i += 1
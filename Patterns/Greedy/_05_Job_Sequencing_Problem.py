class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def maxProfit(jobs):
    jobs.sort(key=lambda job: job.profit, reverse=True)
    scheduled = [-1] * (max(jobs, key=lambda job:job.deadline).deadline + 1)

    profit = 0
    for job in jobs:
        for i in range(job.deadline, 0, -1):
            if scheduled[i] == -1:
                profit += job.profit
                scheduled[i] = job.id
                break
    
    return profit

if __name__ == '__main__':
    testCases = [
        [Job(1,4,40), Job(2,1,10), Job(3,1,40), Job(4,1,30)],
        [Job(6,2,80), Job(3,6,70), Job(4,6,65), Job(2,5,60), Job(5,4,25), Job(8,2,22), Job(1,4,20), Job(7,2,10)]
    ]

    i = 0
    for jobs in testCases:
        print(f'TestCase {i}: {maxProfit(jobs)}')
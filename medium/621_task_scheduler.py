# Task Scheduler
# hash map, counting, greedy

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # counting, hash table, greedy, sorting, heap

        # freq map
        count = {}

        for task in tasks:
            count[task] = count.get(task, 0) + 1 # returns 0 if count dne

        # greedy condition - prioritize task with max frequency
        maxfreq = max(count.values()) # what is max freq
        k = sum(1 for c in count.values() if c == maxfreq) # how many other tasks also have maxfreq

        skeleton = (maxfreq - 1) * (n + 1) + k

        return max(len(tasks), skeleton)

        # CPU interval skeleton w turnaround n
        # (maxf items)(n turnaround)(maxf items)(n turnaround)(k items) 

        # number of "blocks" + last block (wihtout cooldown)
        # n + 1 because 1 is the maxfreq item we picked

        # also, even if there are more tasks, they will be lower in frequency
        # this means they can be scheduled anywhere in the sequence without having to worry about creating overhead

        """
        Ex: AAABBBCCCDD, n = 2
        skeleton: A _ _ A _ _ A 
        filling in:  A, B, C, A, B, C, A, B, C
        adding D: A, B, C, A, B, C, A, B, C, D, D # obviously not allowed
        - but D can be placed anywhere now since it's lower in frequency
        final: A, B, C, D, A, B, C, D, A, B, C
        - D doesn't create extra overhead, therefore skeleton is only based on largest frequency value
        """
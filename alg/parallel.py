import multiprocessing as mp
import numpy as np

# Recursive Helper Function for Parallel Sum
def _Sum(nums: [int], connection, process_num: int):

    # Base Case: Out of Usable Processes or Only one Element in List
    if len(nums) <= 1 or process_num <= 0:
        connection.send(sum(nums)) # Return the sequential sum of numbers
        connection.close()
        return

    mid = len(nums) // 2

    # Left Recursion
    left_parent_conn, left_child_conn = mp.Pipe()
    left_process = mp.Process(target = _Sum, args = (nums[:mid], left_child_conn, process_num - 1))

    # Right Recursion
    right_parent_conn, right_child_conn = mp.Pipe()
    right_process = mp.Process(target = _Sum, args = (nums[mid:], right_child_conn, process_num - 1))

    # Start both recursions
    left_process.start()
    right_process.start()

    # Combining the Left and Right Recursions
    left_val = left_parent_conn.recv()
    right_val = right_parent_conn.recv()

    connection.send(left_val + right_val)
    connection.close()

    left_process.join()
    right_process.join()

def Sum(nums: [int]):

    ''' We don't want to instantiate more processes than cores we have available.
    Since 2^n processes are created for each recursion, we only want to pass a max of
    log_2(n) processes for the recursion. Once we run out of processes, we should
    return the sequential sum for the remaining values in nums
    '''

    processors = mp.cpu_count()
    max_processes = np.floor(np.log2(processors))


    # Create process and pipeline for return value
    parent_conn, child_conn = mp.Pipe()

    main_process = mp.Process(target = _Sum, args = (nums, child_conn, max_processes))

    # Collect the values
    main_process.start()
    value = parent_conn.recv() # Blocks further program execution until finished

    # Cleanup
    parent_conn.close()
    main_process.join() # close the process and all its children

    return value
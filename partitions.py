# Import required library
from sympy.utilities.iterables import partitions
from collections import defaultdict
import pprint

# Function to compute bounded part distributions for an integer
def create_partitions(k, max_part):
    """
    Computes a summary of how parts of size 1, 2, ..., max_part are distributed
    in all partitions of integers from start_k to end_k (inclusive),
    with each part size bounded by max_part.

    Returns:
        A dictionary: { k: {(count_of_1s, count_of_2s, count_of_3s): frequency, ...}, ... }
    """
    partitions_result = {}

    # Dictionary to store frequencies of each part-count tuple
    distribution_counts = defaultdict(int)

    # Generate all partitions of k, each returned as a dict: {part_size: count}
    all_partitions = [
        partition for partition in partitions(k)
        if all(part_size <= max_part for part_size in partition)
    ]

    # Count how many 1s, 2s, and 3s in each valid partition
    for partition_dict in all_partitions:
        count_1s = partition_dict.get(1, 0)
        count_2s = partition_dict.get(2, 0)
        count_3s = partition_dict.get(3, 0)
        distribution_counts[(count_1s, count_2s, count_3s)] += 1

    # Store the distribution summary for this value of k
    partitions_result   = dict(distribution_counts)

    return partitions_result

# Function to compute bounded part distributions for a range of integers
def create_from_range(start_k, end_k, max_part):
    partitions_range = {}
    # create partitions in range of integers
    for k in range(start_k, end_k + 1):
        partitions_result = create_partitions(k, max_part)
        partitions_range[k] = dict(partitions_result)
    return partitions_range
# ----------------------------
# Set parameters
start_k = 40       # Start of range
end_k = 60         # End of range
max_part = 3       # Maximum allowed part size

# Run the analysis
distribution_summary = create_from_range(start_k, end_k, max_part)

# ----------------------------
# Example: Print distribution summary for integers from start_k to end_k
print(f"\nDistribution of partitions of {start_k} using only parts ≤ {max_part}:\n")
pprint.pprint(distribution_summary)

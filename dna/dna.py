import csv
import sys


def main():
    if not len(sys.argv) == 3:
        sys.exit("No Command line arguments provided")
    lis = list()
    csv_file = sys.argv[1]
    with open(csv_file) as file:
        dna_tests = file.readline().strip().split(",")
        read = csv.DictReader(file, fieldnames=dna_tests)
        for line in read:
            lis.append(line)

    with open(sys.argv[2]) as file:
        line = file.readline()
    dna = dict()
    dna_tests.remove("name")
    for test in dna_tests:
        dna[test] = longest_match(line, test)
    for person in lis:
        found = True
        for tes in dna_tests:
            if not int(person[tes]) == dna[tes]:
                found = False
                break
        if found == True:
            print(person["name"])
            return
    print("No Match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run

if __name__ == '__main__':
    main()

def rolling_hash_count_distinct_permutations(pattern, text):
    '''
    15/15 solution with rolling hash technique
    Args:
        pattern:
        text:

    Returns:
    '''
    BASE = 11111 # commonly used prime number, for hashing, which reduce collision (duplicated hash value for different string)
    MOD = 100000000007

    len_pattern = len(pattern)
    len_text = len(text)

    if len_pattern > len_text:
        return 0

    # Precompute the hash and frequency arrays
    pattern_freq = [0] * 26
    text_freq = [0] * 26
    current_hash = 0

    for i in range(len_pattern):
        pattern_freq[ord(pattern[i]) - ord('a')] += 1
        text_freq[ord(text[i]) - ord('a')] += 1
        # Compute hash for the initial window
        current_hash = (current_hash * BASE + (ord(text[i]) - ord('a'))) % MOD

    # Precompute power of the base (BASE^(len_pattern-1) % MOD)
    pow_base = pow(BASE, len_pattern - 1, MOD)

    # Compute initial hash and frequency arrays
    unique_hashes = set()

    # Check the first window
    if pattern_freq == text_freq:
        unique_hashes.add(current_hash)

    # Sliding window over the text
    for i in range(len_pattern, len_text):
        # Outgoing and incoming characters
        outgoing_char = text[i - len_pattern]
        incoming_char = text[i]

        # Update the frequency array
        text_freq[ord(outgoing_char) - ord('a')] -= 1
        text_freq[ord(incoming_char) - ord('a')] += 1

        # Update the rolling hash
        # Remove the effect of the outgoing character
        current_hash = (current_hash - (ord(outgoing_char) - ord('a')) * pow_base + MOD) % MOD
        # Shift left (equivalent to multiplying by the base)
        current_hash = (current_hash * BASE) % MOD
        # Add the new incoming character
        current_hash = (current_hash + (ord(incoming_char) - ord('a'))) % MOD

        # Compare the current window with the pattern frequencies
        if pattern_freq == text_freq:
            unique_hashes.add(current_hash)

    # Return the number of distinct permutations
    return len(unique_hashes)


# Example usage
pattern = input().strip()
text = input().strip()
result = rolling_hash_count_distinct_permutations(pattern, text)
print(result)

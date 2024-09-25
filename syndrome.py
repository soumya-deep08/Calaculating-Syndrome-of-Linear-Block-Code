import numpy as np

def calculate_syndrome(received, H):
    """
    Calculate the syndrome for a given received vector and parity-check matrix H.
    
    Parameters:
    received (list or numpy array): The received codeword.
    H (numpy array): The parity-check matrix.

    Returns:
    numpy array: The syndrome vector.
    """
    # Convert the received codeword to a numpy array
    received = np.array(received)
    
    # Compute the syndrome
    syndrome = np.mod(np.dot(received, H.T), 2)
    return syndrome

def transmit_codeword(codeword):
    """
    Simulate the transmission of a codeword. (In real scenarios, this would involve sending over a channel.)
    
    Parameters:
    codeword (list or numpy array): The codeword to be transmitted.

    Returns:
    numpy array: The received codeword (potentially with errors introduced).
    """
    # For simplicity, we assume the received codeword is the same as the transmitted one.
    # In practice, you might introduce errors here to simulate a real transmission channel.
    return np.array(codeword)

def introduce_error(codeword, error_positions):
    """
    Introduce errors into a codeword at specified positions.
    
    Parameters:
    codeword (list or numpy array): The original codeword.
    error_positions (list): The positions at which errors should be introduced.

    Returns:
    numpy array: The codeword with errors introduced.
    """
    codeword_with_errors = np.array(codeword)
    for pos in error_positions:
        codeword_with_errors[pos] ^= 1  # Flip the bit at the specified position
    return codeword_with_errors

# Example usage
H = np.array([[1, 0, 1, 0, 1, 0, 1],
              [0, 1, 1, 0, 0, 1, 1],
              [0, 0, 0, 1, 1, 1, 1]])  # Parity-check matrix

# Generate a random codeword (for simplicity, a random binary vector)
np.random.seed(0)  # For reproducibility
codeword = np.random.randint(0, 2, size=7)

print('Original Codeword:', codeword)

# Transmit the codeword (in practice, this would involve actual transmission)
transmitted_codeword = transmit_codeword(codeword)
print('Transmitted Codeword:', transmitted_codeword)

# Introduce errors to simulate a real transmission (example: flip bits at positions 2 and 5)
error_positions = [2, 5]
received_codeword = introduce_error(transmitted_codeword, error_positions)
print('Received Codeword with Errors:', received_codeword)

# Calculate the syndrome
syndrome = calculate_syndrome(received_codeword, H)
print('Syndrome:', syndrome)
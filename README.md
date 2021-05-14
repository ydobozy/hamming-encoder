# hamming-encoder
Python function which takes a binary sequence as an input and outputs the sequence after hamming encoding has been applied. 
All input errors are handled by printing Error
Input must be in binary.

# hamming-decoder
Python function which takes a binary sequence as an input and outputs the sequence after error detection/correction and hamming decoding have been applied. 
Assuming the even parity states whether the received code is correct or wrong. Single error detection only.
All input errors are handled by printing Error
Input must be in binary.


# Position and sum check
Redundant bits are placed at bit positions of powers of 2.
Each bit covers all bit positions whose binary representation includes a 1 in the ith position. Parity bit will sum the bits covered.
(source: https://www.tutorialspoint.com/error-correcting-codes-hamming-codes).



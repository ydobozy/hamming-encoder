def hammingEncode(num):
    try:
        int(num, 2) # check if poss to convert input base 2 to decimal (1 operation only)
    except:
            return "Error: Input must be binary!"
    # find number of parity bits needed in the binary sequence        
    nbrparitybits = 0
    #print(len(num))
    while 2.**nbrparitybits <= len(num) +nbrparitybits:
        nbrparitybits+=1
        
    print("Number of positions needed: ",nbrparitybits)
    #Create the new data word, setting the parity bits to 0
    encoded=[]
    j=0
    k=0
    for i in range(len(num)+nbrparitybits): #lenght of the output sequence
        if i+1 == 2**(j):   #if index is a parity bit index, value set to 0
            encoded.append(0)
            j+=1
        else:
            encoded.append(int(num[k]))
            k+=1   #else next value taken from input
    
    # Calculate the parity for each parity bit
    # sum values that covers all redundant bit at i position whose binary representation
    #includes a 1 in the ith position. Check parity with mode division
    for p in range(nbrparitybits):
        sum=0
        for index in range(p+1,len(encoded)+1):
            index_bin=str(bin(index))
            if index_bin[-(p+1)]=="1":  # index covering the parity check
                sum+=encoded[index-1] # collect value
        if sum%2>0:
            encoded[(2**p)-1]=1
    
    encoded_str = [str(int) for int in encoded]         
    return ''.join(encoded_str)

def hammingDecode(num):
    try:
        int(num, 2) # check if poss to convert input base 2 to decimal (1 operation only)
    except:
            return "Error: Input must be binary!"
    # find number of parity bits needed in the binary sequence        
    nbrparitybits = 0
    #print(len(num))
    while 2.**nbrparitybits <= len(num):
        nbrparitybits+=1
        
    #Create list with parity bit index to be removed after error detection
    index_paritybit=[]
    j=0
    for i in range(len(num)): #lenght of the output sequence
        if i+1 == 2**(j):   #if index is a parity bit index, value set to 0
            index_paritybit.append(i)
            j+=1
    
    decoded=list(num)
    j=0
    k=0
    corrupted_bit_index=0
    # Calculate the parity for each parity bit
    # sum values that covers all redundant bit at i position whose binary representation
    #includes a 1 in the ith position. Check parity with mode division
    #if parity 1, error detected, parity bit index added to find position
    for p in range(nbrparitybits):
        sum=0
        for index in range(p+1,len(decoded)+1):
            index_bin=str(bin(index))
            if index_bin[-(p+1)]=="1":  # index covering the parity check
                sum+=int(decoded[index-1]) # collect value
        if sum%2>0:
            corrupted_bit_index+=2.**p
    #if final corrupted_bit_index different from 0, error detected and index given        
    if corrupted_bit_index!=0:
        print("Error was detected at position: ", int(corrupted_bit_index))
        correction=int(decoded[int(corrupted_bit_index)-1])
        correction ^= 1 #flip wrong bit
        print("Bit changed from %d to %d" %(int(decoded[int(corrupted_bit_index)-1]),correction))
        decoded[int(corrupted_bit_index)-1]=correction
        
    else:
        print("No error detected")
    
    for ele in sorted(index_paritybit, reverse = True): 
            del decoded[ele] 
            
    decoded_str = [str(int) for int in decoded]         
    return ''.join(decoded_str)

codeWord=input("Enter the word to encode: ")
#"0110101" "10011010"
print("Word %s encoded is %s" %(codeWord,hammingEncode(codeWord)))

word_Received=input("Enter the word to be checked and decoded: ")
 
print("Original word is: ",hammingDecode(word_Received))
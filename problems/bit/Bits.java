/**
 * Utility methods with bit manipulation.
 *
 * @author Zexi Jesse Zhuang
 */
public class Bits {

    /**
     * Counts number of 1 bits in a {@code long} variable.
     *
     * @param x input long variable
     */
    public static long bitCountLong(long x) { // uint64_t
        long m1  = 0x5555555555555555L; //binary: 0101...
        long m2  = 0x3333333333333333L; //binary: 00110011..
        long m4  = 0x0f0f0f0f0f0f0f0fL; //binary:  4 zeros,  4 ones ...
        long m8  = 0x00ff00ff00ff00ffL; //binary:  8 zeros,  8 ones ...
        long m16 = 0x0000ffff0000ffffL; //binary: 16 zeros, 16 ones ...
        long m32 = 0x00000000ffffffffL; //binary: 32 zeros, 32 ones
        long hff = 0xffffffffffffffffL; //binary: all ones
        long h01 = 0x0101010101010101L; //the sum of 256 to the power of 0,1,2,3...
                
        x = (x & m1 ) + ((x >>>  1) & m1 ); //put count of each  2 bits into those  2 bits 
        x = (x & m2 ) + ((x >>>  2) & m2 ); //put count of each  4 bits into those  4 bits 
        x = (x & m4 ) + ((x >>>  4) & m4 ); //put count of each  8 bits into those  8 bits 
        x = (x & m8 ) + ((x >>>  8) & m8 ); //put count of each 16 bits into those 16 bits 
        x = (x & m16) + ((x >>> 16) & m16); //put count of each 32 bits into those 32 bits 
        x = (x & m32) + ((x >>> 32) & m32); //put count of each 64 bits into those 64 bits 
        return x;
    }

    /**
     * 5 constant operations, from JDK
     * 
     * @param input int variable
     */
    public static int bitCount(int i) {
        // HD, Figure 5-2
        // put count of each 2 bits into those 2 bits
        i = i - ((i >>> 1) & 0x55555555); // 01
        // put count of each 4 bits into those 4 bits
        i = (i & 0x33333333) + ((i >>> 2) & 0x33333333); // 0011
        // put count of each 8 bits into those 8 bits
        i = (i + (i >>> 4)) & 0x0f0f0f0f;// 0000 1111
        // put count of each 16 bits into those 8 bits
        i = i + (i >>> 8);
        // put count of each 32 bits into lowest 16 bits
        i = i + (i >>> 16);
        // return i;
        return i & 0x3f; // 0011,1111 (32 is 10,0000)
    }

}

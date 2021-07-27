

# Convert unsigned int32 to signed int32

def UI32toI32(self, u32):
    if u32>0x7FFFFFFF:
        return u32 - 4294967296
    else:
        return u32

    

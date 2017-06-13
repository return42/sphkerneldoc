.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/lz4.h

.. _`lz4_compressbound`:

LZ4_compressBound
=================

.. c:function:: int LZ4_compressBound(size_t isize)

    Max. output size in worst case szenarios

    :param size_t isize:
        Size of the input data

.. _`lz4_compressbound.return`:

Return
------

Max. size LZ4 may output in a "worst case" szenario
(data not compressible)

.. _`lz4_compress_default`:

LZ4_compress_default
====================

.. c:function:: int LZ4_compress_default(const char *source, char *dest, int inputSize, int maxOutputSize, void *wrkmem)

    Compress data from source to dest

    :param const char \*source:
        source address of the original data

    :param char \*dest:
        output buffer address of the compressed data

    :param int inputSize:
        size of the input data. Max supported value is LZ4_MAX_INPUT_SIZE

    :param int maxOutputSize:
        full or partial size of buffer 'dest'
        which must be already allocated

    :param void \*wrkmem:
        address of the working memory.
        This requires 'workmem' of LZ4_MEM_COMPRESS.

.. _`lz4_compress_default.description`:

Description
-----------

Compresses 'sourceSize' bytes from buffer 'source'
into already allocated 'dest' buffer of size 'maxOutputSize'.
Compression is guaranteed to succeed if
'maxOutputSize' >= LZ4_compressBound(inputSize).
It also runs faster, so it's a recommended setting.
If the function cannot compress 'source' into a more limited 'dest' budget,
compression stops \*immediately\*, and the function result is zero.
As a consequence, 'dest' content is not valid.

.. _`lz4_compress_default.return`:

Return
------

Number of bytes written into buffer 'dest'
(necessarily <= maxOutputSize) or 0 if compression fails

.. _`lz4_compress_fast`:

LZ4_compress_fast
=================

.. c:function:: int LZ4_compress_fast(const char *source, char *dest, int inputSize, int maxOutputSize, int acceleration, void *wrkmem)

    As LZ4_compress_default providing an acceleration param

    :param const char \*source:
        source address of the original data

    :param char \*dest:
        output buffer address of the compressed data

    :param int inputSize:
        size of the input data. Max supported value is LZ4_MAX_INPUT_SIZE

    :param int maxOutputSize:
        full or partial size of buffer 'dest'
        which must be already allocated

    :param int acceleration:
        acceleration factor

    :param void \*wrkmem:
        address of the working memory.
        This requires 'workmem' of LZ4_MEM_COMPRESS.

.. _`lz4_compress_fast.description`:

Description
-----------

Same as \ :c:func:`LZ4_compress_default`\ , but allows to select an "acceleration"
factor. The larger the acceleration value, the faster the algorithm,
but also the lesser the compression. It's a trade-off. It can be fine tuned,
with each successive value providing roughly +~3% to speed.
An acceleration value of "1" is the same as regular \ :c:func:`LZ4_compress_default`\ 
Values <= 0 will be replaced by LZ4_ACCELERATION_DEFAULT, which is 1.

.. _`lz4_compress_fast.return`:

Return
------

Number of bytes written into buffer 'dest'
(necessarily <= maxOutputSize) or 0 if compression fails

.. _`lz4_compress_destsize`:

LZ4_compress_destSize
=====================

.. c:function:: int LZ4_compress_destSize(const char *source, char *dest, int *sourceSizePtr, int targetDestSize, void *wrkmem)

    Compress as much data as possible from source to dest

    :param const char \*source:
        source address of the original data

    :param char \*dest:
        output buffer address of the compressed data

    :param int \*sourceSizePtr:
        will be modified to indicate how many bytes where read
        from 'source' to fill 'dest'. New value is necessarily <= old value.

    :param int targetDestSize:
        Size of buffer 'dest' which must be already allocated

    :param void \*wrkmem:
        address of the working memory.
        This requires 'workmem' of LZ4_MEM_COMPRESS.

.. _`lz4_compress_destsize.description`:

Description
-----------

Reverse the logic, by compressing as much data as possible
from 'source' buffer into already allocated buffer 'dest'
of size 'targetDestSize'.
This function either compresses the entire 'source' content into 'dest'
if it's large enough, or fill 'dest' buffer completely with as much data as
possible from 'source'.

.. _`lz4_compress_destsize.return`:

Return
------

Number of bytes written into 'dest' (necessarily <= targetDestSize)
or 0 if compression fails

.. _`lz4_decompress_fast`:

LZ4_decompress_fast
===================

.. c:function:: int LZ4_decompress_fast(const char *source, char *dest, int originalSize)

    Decompresses data from 'source' into 'dest'

    :param const char \*source:
        source address of the compressed data

    :param char \*dest:
        output buffer address of the uncompressed data
        which must be already allocated with 'originalSize' bytes

    :param int originalSize:
        is the original and therefore uncompressed size

.. _`lz4_decompress_fast.description`:

Description
-----------

Decompresses data from 'source' into 'dest'.
This function fully respect memory boundaries for properly formed
compressed data.
It is a bit faster than \ :c:func:`LZ4_decompress_safe`\ .
However, it does not provide any protection against intentionally
modified data stream (malicious input).
Use this function in trusted environment only
(data to decode comes from a trusted source).

.. _`lz4_decompress_fast.return`:

Return
------

number of bytes read from the source buffer
or a negative result if decompression fails.

.. _`lz4_decompress_safe`:

LZ4_decompress_safe
===================

.. c:function:: int LZ4_decompress_safe(const char *source, char *dest, int compressedSize, int maxDecompressedSize)

    Decompression protected against buffer overflow

    :param const char \*source:
        source address of the compressed data

    :param char \*dest:
        output buffer address of the uncompressed data
        which must be already allocated

    :param int compressedSize:
        is the precise full size of the compressed block

    :param int maxDecompressedSize:
        is the size of 'dest' buffer

.. _`lz4_decompress_safe.description`:

Description
-----------

Decompresses data fom 'source' into 'dest'.
If the source stream is detected malformed, the function will
stop decoding and return a negative result.
This function is protected against buffer overflow exploits,
including malicious data packets. It never writes outside output buffer,
nor reads outside input buffer.

.. _`lz4_decompress_safe.return`:

Return
------

number of bytes decompressed into destination buffer
(necessarily <= maxDecompressedSize)
or a negative result in case of error

.. _`lz4_decompress_safe_partial`:

LZ4_decompress_safe_partial
===========================

.. c:function:: int LZ4_decompress_safe_partial(const char *source, char *dest, int compressedSize, int targetOutputSize, int maxDecompressedSize)

    Decompress a block of size 'compressedSize' at position 'source' into buffer 'dest'

    :param const char \*source:
        source address of the compressed data

    :param char \*dest:
        output buffer address of the decompressed data which must be
        already allocated

    :param int compressedSize:
        is the precise full size of the compressed block.

    :param int targetOutputSize:
        the decompression operation will try
        to stop as soon as 'targetOutputSize' has been reached

    :param int maxDecompressedSize:
        is the size of destination buffer

.. _`lz4_decompress_safe_partial.description`:

Description
-----------

This function decompresses a compressed block of size 'compressedSize'
at position 'source' into destination buffer 'dest'
of size 'maxDecompressedSize'.
The function tries to stop decompressing operation as soon as
'targetOutputSize' has been reached, reducing decompression time.
This function never writes outside of output buffer,
and never reads outside of input buffer.
It is therefore protected against malicious data packets.

.. _`lz4_decompress_safe_partial.return`:

Return
------

the number of bytes decoded in the destination buffer
(necessarily <= maxDecompressedSize)
or a negative result in case of error

.. _`lz4_compress_hc`:

LZ4_compress_HC
===============

.. c:function:: int LZ4_compress_HC(const char *src, char *dst, int srcSize, int dstCapacity, int compressionLevel, void *wrkmem)

    Compress data from \`src\` into \`dst\`, using HC algorithm

    :param const char \*src:
        source address of the original data

    :param char \*dst:
        output buffer address of the compressed data

    :param int srcSize:
        size of the input data. Max supported value is LZ4_MAX_INPUT_SIZE

    :param int dstCapacity:
        full or partial size of buffer 'dst',
        which must be already allocated

    :param int compressionLevel:
        Recommended values are between 4 and 9, although any
        value between 1 and LZ4HC_MAX_CLEVEL will work.
        Values >LZ4HC_MAX_CLEVEL behave the same as 16.

    :param void \*wrkmem:
        address of the working memory.
        This requires 'wrkmem' of size LZ4HC_MEM_COMPRESS.

.. _`lz4_compress_hc.description`:

Description
-----------

Compress data from 'src' into 'dst', using the more powerful
but slower "HC" algorithm. Compression is guaranteed to succeed if
\`dstCapacity >= LZ4_compressBound(srcSize)

Return : the number of bytes written into 'dst' or 0 if compression fails.

.. _`lz4_resetstreamhc`:

LZ4_resetStreamHC
=================

.. c:function:: void LZ4_resetStreamHC(LZ4_streamHC_t *streamHCPtr, int compressionLevel)

    Init an allocated 'LZ4_streamHC_t' structure

    :param LZ4_streamHC_t \*streamHCPtr:
        pointer to the 'LZ4_streamHC_t' structure

    :param int compressionLevel:
        Recommended values are between 4 and 9, although any
        value between 1 and LZ4HC_MAX_CLEVEL will work.
        Values >LZ4HC_MAX_CLEVEL behave the same as 16.

.. _`lz4_resetstreamhc.description`:

Description
-----------

An LZ4_streamHC_t structure can be allocated once
and re-used multiple times.
Use this function to init an allocated \`LZ4_streamHC_t\` structure
and start a new compression.

.. _`lz4_loaddicthc`:

LZ4_loadDictHC
==============

.. c:function:: int LZ4_loadDictHC(LZ4_streamHC_t *streamHCPtr, const char *dictionary, int dictSize)

    Load a static dictionary into LZ4_streamHC

    :param LZ4_streamHC_t \*streamHCPtr:
        pointer to the LZ4HC_stream_t

    :param const char \*dictionary:
        dictionary to load

    :param int dictSize:
        size of dictionary

.. _`lz4_loaddicthc.description`:

Description
-----------

Use this function to load a static dictionary into LZ4HC_stream.
Any previous data will be forgotten, only 'dictionary'
will remain in memory.
Loading a size of 0 is allowed.

Return : dictionary size, in bytes (necessarily <= 64 KB)

.. _`lz4_compress_hc_continue`:

LZ4_compress_HC_continue
========================

.. c:function:: int LZ4_compress_HC_continue(LZ4_streamHC_t *streamHCPtr, const char *src, char *dst, int srcSize, int maxDstSize)

    Compress 'src' using data from previously compressed blocks as a dictionary using the HC algorithm

    :param LZ4_streamHC_t \*streamHCPtr:
        Pointer to the previous 'LZ4_streamHC_t' structure

    :param const char \*src:
        source address of the original data

    :param char \*dst:
        output buffer address of the compressed data,
        which must be already allocated

    :param int srcSize:
        size of the input data. Max supported value is LZ4_MAX_INPUT_SIZE

    :param int maxDstSize:
        full or partial size of buffer 'dest'
        which must be already allocated

.. _`lz4_compress_hc_continue.description`:

Description
-----------

These functions compress data in successive blocks of any size, using
previous blocks as dictionary. One key assumption is that previous
blocks (up to 64 KB) remain read-accessible while
compressing next blocks. There is an exception for ring buffers,
which can be smaller than 64 KB.
Ring buffers scenario is automatically detected and handled by
\ :c:func:`LZ4_compress_HC_continue`\ .
Before starting compression, state must be properly initialized,
using \ :c:func:`LZ4_resetStreamHC`\ .
A first "fictional block" can then be designated as
initial dictionary, using \ :c:func:`LZ4_loadDictHC`\  (Optional).
Then, use \ :c:func:`LZ4_compress_HC_continue`\ 
to compress each successive block. Previous memory blocks
(including initial dictionary when present) must remain accessible
and unmodified during compression.
'dst' buffer should be sized to handle worst case scenarios, using
\ :c:func:`LZ4_compressBound`\ , to ensure operation success.
If, for any reason, previous data blocks can't be preserved unmodified
in memory during next compression block,
you must save it to a safer memory space, using \ :c:func:`LZ4_saveDictHC`\ .
Return value of \ :c:func:`LZ4_saveDictHC`\  is the size of dictionary
effectively saved into 'safeBuffer'.

.. _`lz4_compress_hc_continue.return`:

Return
------

Number of bytes written into buffer 'dst'  or 0 if compression fails

.. _`lz4_savedicthc`:

LZ4_saveDictHC
==============

.. c:function:: int LZ4_saveDictHC(LZ4_streamHC_t *streamHCPtr, char *safeBuffer, int maxDictSize)

    Save static dictionary from LZ4HC_stream

    :param LZ4_streamHC_t \*streamHCPtr:
        pointer to the 'LZ4HC_stream_t' structure

    :param char \*safeBuffer:
        buffer to save dictionary to, must be already allocated

    :param int maxDictSize:
        size of 'safeBuffer'

.. _`lz4_savedicthc.description`:

Description
-----------

If previously compressed data block is not guaranteed
to remain available at its memory location,
save it into a safer place (char \*safeBuffer).
Note : you don't need to call \ :c:func:`LZ4_loadDictHC`\  afterwards,
dictionary is immediately usable, you can therefore call
\ :c:func:`LZ4_compress_HC_continue`\ .

Return : saved dictionary size in bytes (necessarily <= maxDictSize),
or 0 if error.

.. _`lz4_resetstream`:

LZ4_resetStream
===============

.. c:function:: void LZ4_resetStream(LZ4_stream_t *LZ4_stream)

    Init an allocated 'LZ4_stream_t' structure

    :param LZ4_stream_t \*LZ4_stream:
        pointer to the 'LZ4_stream_t' structure

.. _`lz4_resetstream.description`:

Description
-----------

An LZ4_stream_t structure can be allocated once
and re-used multiple times.
Use this function to init an allocated \`LZ4_stream_t\` structure
and start a new compression.

.. _`lz4_loaddict`:

LZ4_loadDict
============

.. c:function:: int LZ4_loadDict(LZ4_stream_t *streamPtr, const char *dictionary, int dictSize)

    Load a static dictionary into LZ4_stream

    :param LZ4_stream_t \*streamPtr:
        pointer to the LZ4_stream_t

    :param const char \*dictionary:
        dictionary to load

    :param int dictSize:
        size of dictionary

.. _`lz4_loaddict.description`:

Description
-----------

Use this function to load a static dictionary into LZ4_stream.
Any previous data will be forgotten, only 'dictionary'
will remain in memory.
Loading a size of 0 is allowed.

Return : dictionary size, in bytes (necessarily <= 64 KB)

.. _`lz4_savedict`:

LZ4_saveDict
============

.. c:function:: int LZ4_saveDict(LZ4_stream_t *streamPtr, char *safeBuffer, int dictSize)

    Save static dictionary from LZ4_stream

    :param LZ4_stream_t \*streamPtr:
        pointer to the 'LZ4_stream_t' structure

    :param char \*safeBuffer:
        buffer to save dictionary to, must be already allocated

    :param int dictSize:
        size of 'safeBuffer'

.. _`lz4_savedict.description`:

Description
-----------

If previously compressed data block is not guaranteed
to remain available at its memory location,
save it into a safer place (char \*safeBuffer).
Note : you don't need to call \ :c:func:`LZ4_loadDict`\  afterwards,
dictionary is immediately usable, you can therefore call
\ :c:func:`LZ4_compress_fast_continue`\ .

Return : saved dictionary size in bytes (necessarily <= dictSize),
or 0 if error.

.. _`lz4_compress_fast_continue`:

LZ4_compress_fast_continue
==========================

.. c:function:: int LZ4_compress_fast_continue(LZ4_stream_t *streamPtr, const char *src, char *dst, int srcSize, int maxDstSize, int acceleration)

    Compress 'src' using data from previously compressed blocks as a dictionary

    :param LZ4_stream_t \*streamPtr:
        Pointer to the previous 'LZ4_stream_t' structure

    :param const char \*src:
        source address of the original data

    :param char \*dst:
        output buffer address of the compressed data,
        which must be already allocated

    :param int srcSize:
        size of the input data. Max supported value is LZ4_MAX_INPUT_SIZE

    :param int maxDstSize:
        full or partial size of buffer 'dest'
        which must be already allocated

    :param int acceleration:
        acceleration factor

.. _`lz4_compress_fast_continue.description`:

Description
-----------

Compress buffer content 'src', using data from previously compressed blocks
as dictionary to improve compression ratio.
Important : Previous data blocks are assumed to still
be present and unmodified !
If maxDstSize >= LZ4_compressBound(srcSize),
compression is guaranteed to succeed, and runs faster.

.. _`lz4_compress_fast_continue.return`:

Return
------

Number of bytes written into buffer 'dst'  or 0 if compression fails

.. _`lz4_setstreamdecode`:

LZ4_setStreamDecode
===================

.. c:function:: int LZ4_setStreamDecode(LZ4_streamDecode_t *LZ4_streamDecode, const char *dictionary, int dictSize)

    Instruct where to find dictionary

    :param LZ4_streamDecode_t \*LZ4_streamDecode:
        the 'LZ4_streamDecode_t' structure

    :param const char \*dictionary:
        dictionary to use

    :param int dictSize:
        size of dictionary

.. _`lz4_setstreamdecode.description`:

Description
-----------

Use this function to instruct where to find the dictionary.
Setting a size of 0 is allowed (same effect as reset).

.. _`lz4_setstreamdecode.return`:

Return
------

1 if OK, 0 if error

.. _`lz4_decompress_safe_continue`:

LZ4_decompress_safe_continue
============================

.. c:function:: int LZ4_decompress_safe_continue(LZ4_streamDecode_t *LZ4_streamDecode, const char *source, char *dest, int compressedSize, int maxDecompressedSize)

    Decompress blocks in streaming mode

    :param LZ4_streamDecode_t \*LZ4_streamDecode:
        the 'LZ4_streamDecode_t' structure

    :param const char \*source:
        source address of the compressed data

    :param char \*dest:
        output buffer address of the uncompressed data
        which must be already allocated

    :param int compressedSize:
        is the precise full size of the compressed block

    :param int maxDecompressedSize:
        is the size of 'dest' buffer

.. _`lz4_decompress_safe_continue.description`:

Description
-----------

These decoding function allows decompression of multiple blocks
in "streaming" mode.
Previously decoded blocks \*must\* remain available at the memory position
where they were decoded (up to 64 KB)
In the case of a ring buffers, decoding buffer must be either :
- Exactly same size as encoding buffer, with same update rule
(block boundaries at same positions) In which case,
the decoding & encoding ring buffer can have any size,
including very small ones ( < 64 KB).
- Larger than encoding buffer, by a minimum of maxBlockSize more bytes.
maxBlockSize is implementation dependent.
It's the maximum size you intend to compress into a single block.
In which case, encoding and decoding buffers do not need
to be synchronized, and encoding ring buffer can have any size,
including small ones ( < 64 KB).
- \_At least\_ 64 KB + 8 bytes + maxBlockSize.
In which case, encoding and decoding buffers do not need to be
synchronized, and encoding ring buffer can have any size,
including larger than decoding buffer. W
Whenever these conditions are not possible, save the last 64KB of decoded
data into a safe buffer, and indicate where it is saved
using \ :c:func:`LZ4_setStreamDecode`\ 

.. _`lz4_decompress_safe_continue.return`:

Return
------

number of bytes decompressed into destination buffer
(necessarily <= maxDecompressedSize)
or a negative result in case of error

.. _`lz4_decompress_fast_continue`:

LZ4_decompress_fast_continue
============================

.. c:function:: int LZ4_decompress_fast_continue(LZ4_streamDecode_t *LZ4_streamDecode, const char *source, char *dest, int originalSize)

    Decompress blocks in streaming mode

    :param LZ4_streamDecode_t \*LZ4_streamDecode:
        the 'LZ4_streamDecode_t' structure

    :param const char \*source:
        source address of the compressed data

    :param char \*dest:
        output buffer address of the uncompressed data
        which must be already allocated with 'originalSize' bytes

    :param int originalSize:
        is the original and therefore uncompressed size

.. _`lz4_decompress_fast_continue.description`:

Description
-----------

These decoding function allows decompression of multiple blocks
in "streaming" mode.
Previously decoded blocks \*must\* remain available at the memory position
where they were decoded (up to 64 KB)
In the case of a ring buffers, decoding buffer must be either :
- Exactly same size as encoding buffer, with same update rule
(block boundaries at same positions) In which case,
the decoding & encoding ring buffer can have any size,
including very small ones ( < 64 KB).
- Larger than encoding buffer, by a minimum of maxBlockSize more bytes.
maxBlockSize is implementation dependent.
It's the maximum size you intend to compress into a single block.
In which case, encoding and decoding buffers do not need
to be synchronized, and encoding ring buffer can have any size,
including small ones ( < 64 KB).
- \_At least\_ 64 KB + 8 bytes + maxBlockSize.
In which case, encoding and decoding buffers do not need to be
synchronized, and encoding ring buffer can have any size,
including larger than decoding buffer. W
Whenever these conditions are not possible, save the last 64KB of decoded
data into a safe buffer, and indicate where it is saved
using \ :c:func:`LZ4_setStreamDecode`\ 

.. _`lz4_decompress_fast_continue.return`:

Return
------

number of bytes decompressed into destination buffer
(necessarily <= maxDecompressedSize)
or a negative result in case of error

.. _`lz4_decompress_safe_usingdict`:

LZ4_decompress_safe_usingDict
=============================

.. c:function:: int LZ4_decompress_safe_usingDict(const char *source, char *dest, int compressedSize, int maxDecompressedSize, const char *dictStart, int dictSize)

    Same as \ :c:func:`LZ4_setStreamDecode`\  followed by \ :c:func:`LZ4_decompress_safe_continue`\ 

    :param const char \*source:
        source address of the compressed data

    :param char \*dest:
        output buffer address of the uncompressed data
        which must be already allocated

    :param int compressedSize:
        is the precise full size of the compressed block

    :param int maxDecompressedSize:
        is the size of 'dest' buffer

    :param const char \*dictStart:
        pointer to the start of the dictionary in memory

    :param int dictSize:
        size of dictionary

.. _`lz4_decompress_safe_usingdict.description`:

Description
-----------

These decoding function works the same as
a combination of \ :c:func:`LZ4_setStreamDecode`\  followed by
\ :c:func:`LZ4_decompress_safe_continue`\ 
It is stand-alone, and don'tn eed a LZ4_streamDecode_t structure.

.. _`lz4_decompress_safe_usingdict.return`:

Return
------

number of bytes decompressed into destination buffer
(necessarily <= maxDecompressedSize)
or a negative result in case of error

.. _`lz4_decompress_fast_usingdict`:

LZ4_decompress_fast_usingDict
=============================

.. c:function:: int LZ4_decompress_fast_usingDict(const char *source, char *dest, int originalSize, const char *dictStart, int dictSize)

    Same as \ :c:func:`LZ4_setStreamDecode`\  followed by \ :c:func:`LZ4_decompress_fast_continue`\ 

    :param const char \*source:
        source address of the compressed data

    :param char \*dest:
        output buffer address of the uncompressed data
        which must be already allocated with 'originalSize' bytes

    :param int originalSize:
        is the original and therefore uncompressed size

    :param const char \*dictStart:
        pointer to the start of the dictionary in memory

    :param int dictSize:
        size of dictionary

.. _`lz4_decompress_fast_usingdict.description`:

Description
-----------

These decoding function works the same as
a combination of \ :c:func:`LZ4_setStreamDecode`\  followed by
\ :c:func:`LZ4_decompress_safe_continue`\ 
It is stand-alone, and don'tn eed a LZ4_streamDecode_t structure.

.. _`lz4_decompress_fast_usingdict.return`:

Return
------

number of bytes decompressed into destination buffer
(necessarily <= maxDecompressedSize)
or a negative result in case of error

.. This file was automatic generated / don't edit.


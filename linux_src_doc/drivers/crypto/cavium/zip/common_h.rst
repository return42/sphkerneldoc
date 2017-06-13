.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/cavium/zip/common.h

.. _`zip_operation`:

struct zip_operation
====================

.. c:type:: struct zip_operation

    common data structure for comp and decomp operations

.. _`zip_operation.definition`:

Definition
----------

.. code-block:: c

    struct zip_operation {
        u8 *input;
        u8 *output;
        u64 ctx_addr;
        u64 history;
        u32 input_len;
        u32 input_total_len;
        u32 output_len;
        u32 output_total_len;
        u32 csum;
        u32 flush;
        u32 format;
        u32 speed;
        u32 ccode;
        u32 lzs_flag;
        u32 begin_file;
        u32 history_len;
        u32 end_file;
        u32 compcode;
        u32 bytes_read;
        u32 bits_processed;
        u32 sizeofptr;
        u32 sizeofzops;
    }

.. _`zip_operation.members`:

Members
-------

input
    Next input byte is read from here

output
    Next output byte written here

ctx_addr
    Inflate context buffer address

history
    Pointer to the history buffer

input_len
    Number of bytes available at next_in

input_total_len
    Total number of input bytes read

output_len
    Remaining free space at next_out

output_total_len
    Total number of bytes output so far

csum
    Checksum value of the uncompressed data

flush
    Flush flag

format
    Format (depends on stream's wrap)

speed
    Speed depends on stream's level

ccode
    Compression code ( stream's strategy)

lzs_flag
    Flag for LZS support

begin_file
    Beginning of file indication for inflate

history_len
    Size of the history data

end_file
    Ending of the file indication for inflate

compcode
    Completion status of the ZIP invocation

bytes_read
    Input bytes read in current instruction

bits_processed
    Total bits processed for entire file

sizeofptr
    To distinguish between ILP32 and LP64

sizeofzops
    Optional just for padding

.. _`zip_operation.description`:

Description
-----------

This structure is used to maintain the required meta data for the
comp and decomp operations.

.. This file was automatic generated / don't edit.


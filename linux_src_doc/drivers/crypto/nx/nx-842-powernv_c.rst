.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/nx/nx-842-powernv.c

.. _`setup_indirect_dde`:

setup_indirect_dde
==================

.. c:function:: void setup_indirect_dde(struct data_descriptor_entry *dde, struct data_descriptor_entry *ddl, unsigned int dde_count, unsigned int byte_count)

    Setup an indirect DDE

    :param dde:
        *undescribed*
    :type dde: struct data_descriptor_entry \*

    :param ddl:
        *undescribed*
    :type ddl: struct data_descriptor_entry \*

    :param dde_count:
        *undescribed*
    :type dde_count: unsigned int

    :param byte_count:
        *undescribed*
    :type byte_count: unsigned int

.. _`setup_indirect_dde.description`:

Description
-----------

The DDE is setup with the the DDE count, byte count, and address of
first direct DDE in the list.

.. _`setup_direct_dde`:

setup_direct_dde
================

.. c:function:: unsigned int setup_direct_dde(struct data_descriptor_entry *dde, unsigned long pa, unsigned int len)

    Setup single DDE from buffer

    :param dde:
        *undescribed*
    :type dde: struct data_descriptor_entry \*

    :param pa:
        *undescribed*
    :type pa: unsigned long

    :param len:
        *undescribed*
    :type len: unsigned int

.. _`setup_direct_dde.description`:

Description
-----------

The DDE is setup with the buffer and length.  The buffer must be properly
aligned.  The used length is returned.

.. _`setup_direct_dde.return`:

Return
------

N    Successfully set up DDE with N bytes

.. _`setup_ddl`:

setup_ddl
=========

.. c:function:: int setup_ddl(struct data_descriptor_entry *dde, struct data_descriptor_entry *ddl, unsigned char *buf, unsigned int len, bool in)

    Setup DDL from buffer

    :param dde:
        *undescribed*
    :type dde: struct data_descriptor_entry \*

    :param ddl:
        *undescribed*
    :type ddl: struct data_descriptor_entry \*

    :param buf:
        *undescribed*
    :type buf: unsigned char \*

    :param len:
        *undescribed*
    :type len: unsigned int

    :param in:
        *undescribed*
    :type in: bool

.. _`setup_ddl.return`:

Return
------

0          Successfully set up DDL

.. _`wait_for_csb`:

wait_for_csb
============

.. c:function:: int wait_for_csb(struct nx842_workmem *wmem, struct coprocessor_status_block *csb)

    :param wmem:
        *undescribed*
    :type wmem: struct nx842_workmem \*

    :param csb:
        *undescribed*
    :type csb: struct coprocessor_status_block \*

.. _`nx842_exec_icswx`:

nx842_exec_icswx
================

.. c:function:: int nx842_exec_icswx(const unsigned char *in, unsigned int inlen, unsigned char *out, unsigned int *outlenp, void *workmem, int fc)

    compress/decompress data using the 842 algorithm

    :param in:
        input buffer pointer
    :type in: const unsigned char \*

    :param inlen:
        input buffer size
    :type inlen: unsigned int

    :param out:
        output buffer pointer
    :type out: unsigned char \*

    :param outlenp:
        output buffer size pointer
    :type outlenp: unsigned int \*

    :param workmem:
        working memory buffer pointer, size determined by
        nx842_powernv_driver.workmem_size
    :type workmem: void \*

    :param fc:
        function code, see CCW Function Codes in nx-842.h
    :type fc: int

.. _`nx842_exec_icswx.description`:

Description
-----------

(De)compression provided by the NX842 coprocessor on IBM PowerNV systems.
This compresses or decompresses the provided input buffer into the provided
output buffer.

Upon return from this function \ ``outlen``\  contains the length of the
output data.  If there is an error then \ ``outlen``\  will be 0 and an
error will be specified by the return code from this function.

The \ ``workmem``\  buffer should only be used by one function call at a time.

.. _`nx842_exec_icswx.return`:

Return
------

0          Success, output of length \ ``outlenp``\  stored in the buffer at \ ``out``\ 
-ENODEV    Hardware unavailable
-ENOSPC    Output buffer is to small
-EMSGSIZE  Input buffer too large
-EINVAL    buffer constraints do not fix nx842_constraints
-EPROTO    hardware error during operation
-ETIMEDOUT hardware did not complete operation in reasonable time
-EINTR     operation was aborted

.. _`nx842_exec_vas`:

nx842_exec_vas
==============

.. c:function:: int nx842_exec_vas(const unsigned char *in, unsigned int inlen, unsigned char *out, unsigned int *outlenp, void *workmem, int fc)

    compress/decompress data using the 842 algorithm

    :param in:
        input buffer pointer
    :type in: const unsigned char \*

    :param inlen:
        input buffer size
    :type inlen: unsigned int

    :param out:
        output buffer pointer
    :type out: unsigned char \*

    :param outlenp:
        output buffer size pointer
    :type outlenp: unsigned int \*

    :param workmem:
        working memory buffer pointer, size determined by
        nx842_powernv_driver.workmem_size
    :type workmem: void \*

    :param fc:
        function code, see CCW Function Codes in nx-842.h
    :type fc: int

.. _`nx842_exec_vas.description`:

Description
-----------

(De)compression provided by the NX842 coprocessor on IBM PowerNV systems.
This compresses or decompresses the provided input buffer into the provided
output buffer.

Upon return from this function \ ``outlen``\  contains the length of the
output data.  If there is an error then \ ``outlen``\  will be 0 and an
error will be specified by the return code from this function.

The \ ``workmem``\  buffer should only be used by one function call at a time.

.. _`nx842_exec_vas.return`:

Return
------

0          Success, output of length \ ``outlenp``\  stored in the buffer
at \ ``out``\ 
-ENODEV    Hardware unavailable
-ENOSPC    Output buffer is to small
-EMSGSIZE  Input buffer too large
-EINVAL    buffer constraints do not fix nx842_constraints
-EPROTO    hardware error during operation
-ETIMEDOUT hardware did not complete operation in reasonable time
-EINTR     operation was aborted

.. _`nx842_powernv_compress`:

nx842_powernv_compress
======================

.. c:function:: int nx842_powernv_compress(const unsigned char *in, unsigned int inlen, unsigned char *out, unsigned int *outlenp, void *wmem)

    Compress data using the 842 algorithm

    :param in:
        input buffer pointer
    :type in: const unsigned char \*

    :param inlen:
        input buffer size
    :type inlen: unsigned int

    :param out:
        output buffer pointer
    :type out: unsigned char \*

    :param outlenp:
        output buffer size pointer
    :type outlenp: unsigned int \*

    :param wmem:
        *undescribed*
    :type wmem: void \*

.. _`nx842_powernv_compress.description`:

Description
-----------

Compression provided by the NX842 coprocessor on IBM PowerNV systems.
The input buffer is compressed and the result is stored in the
provided output buffer.

Upon return from this function \ ``outlen``\  contains the length of the
compressed data.  If there is an error then \ ``outlen``\  will be 0 and an
error will be specified by the return code from this function.

.. _`nx842_powernv_compress.return`:

Return
------

see \ ``nx842_powernv_exec``\ ()

.. _`nx842_powernv_decompress`:

nx842_powernv_decompress
========================

.. c:function:: int nx842_powernv_decompress(const unsigned char *in, unsigned int inlen, unsigned char *out, unsigned int *outlenp, void *wmem)

    Decompress data using the 842 algorithm

    :param in:
        input buffer pointer
    :type in: const unsigned char \*

    :param inlen:
        input buffer size
    :type inlen: unsigned int

    :param out:
        output buffer pointer
    :type out: unsigned char \*

    :param outlenp:
        output buffer size pointer
    :type outlenp: unsigned int \*

    :param wmem:
        *undescribed*
    :type wmem: void \*

.. _`nx842_powernv_decompress.description`:

Description
-----------

Decompression provided by the NX842 coprocessor on IBM PowerNV systems.
The input buffer is decompressed and the result is stored in the
provided output buffer.

Upon return from this function \ ``outlen``\  contains the length of the
decompressed data.  If there is an error then \ ``outlen``\  will be 0 and an
error will be specified by the return code from this function.

.. _`nx842_powernv_decompress.return`:

Return
------

see \ ``nx842_powernv_exec``\ ()

.. This file was automatic generated / don't edit.


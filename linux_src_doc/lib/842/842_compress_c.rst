.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/842/842_compress.c

.. _`sw842_compress`:

sw842_compress
==============

.. c:function:: int sw842_compress(const u8 *in, unsigned int ilen, u8 *out, unsigned int *olen, void *wmem)

    :param in:
        *undescribed*
    :type in: const u8 \*

    :param ilen:
        *undescribed*
    :type ilen: unsigned int

    :param out:
        *undescribed*
    :type out: u8 \*

    :param olen:
        *undescribed*
    :type olen: unsigned int \*

    :param wmem:
        *undescribed*
    :type wmem: void \*

.. _`sw842_compress.description`:

Description
-----------

Compress the uncompressed buffer of length \ ``ilen``\  at \ ``in``\  to the output buffer
\ ``out``\ , using no more than \ ``olen``\  bytes, using the 842 compression format.

.. _`sw842_compress.return`:

Return
------

0 on success, error on failure.  The \ ``olen``\  parameter
will contain the number of output bytes written on success, or
0 on error.

.. This file was automatic generated / don't edit.


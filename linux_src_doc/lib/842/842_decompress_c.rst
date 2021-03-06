.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/842/842_decompress.c

.. _`sw842_decompress`:

sw842_decompress
================

.. c:function:: int sw842_decompress(const u8 *in, unsigned int ilen, u8 *out, unsigned int *olen)

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

.. _`sw842_decompress.description`:

Description
-----------

Decompress the 842-compressed buffer of length \ ``ilen``\  at \ ``in``\ 
to the output buffer \ ``out``\ , using no more than \ ``olen``\  bytes.

The compressed buffer must be only a single 842-compressed buffer,
with the standard format described in the comments in 842.h
Processing will stop when the 842 "END" template is detected,
not the end of the buffer.

.. _`sw842_decompress.return`:

Return
------

0 on success, error on failure.  The \ ``olen``\  parameter
will contain the number of output bytes written on success, or
0 on error.

.. This file was automatic generated / don't edit.


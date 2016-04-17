.. -*- coding: utf-8; mode: rst -*-

================
842_decompress.c
================


.. _`sw842_decompress`:

sw842_decompress
================

.. c:function:: int sw842_decompress (const u8 *in, unsigned int ilen, u8 *out, unsigned int *olen)

    :param const u8 \*in:

        *undescribed*

    :param unsigned int ilen:

        *undescribed*

    :param u8 \*out:

        *undescribed*

    :param unsigned int \*olen:

        *undescribed*



.. _`sw842_decompress.description`:

Description
-----------


Decompress the 842-compressed buffer of length ``ilen`` at ``in``
to the output buffer ``out``\ , using no more than ``olen`` bytes.

The compressed buffer must be only a single 842-compressed buffer,
with the standard format described in the comments in 842.h
Processing will stop when the 842 "END" template is detected,
not the end of the buffer.



.. _`sw842_decompress.returns`:

Returns
-------

0 on success, error on failure.  The ``olen`` parameter
will contain the number of output bytes written on success, or
0 on error.


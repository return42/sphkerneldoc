.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/boot/decompress.c

.. _`partial_decompress`:

partial_decompress
==================

.. c:function:: long partial_decompress(void *inbuf, unsigned long input_size, void *outbuf, unsigned long output_size, unsigned long _skip)

    decompresses part or all of a compressed buffer

    :param inbuf:
        input buffer
    :type inbuf: void \*

    :param input_size:
        length of the input buffer
    :type input_size: unsigned long

    :param outbuf:
        input buffer
    :type outbuf: void \*

    :param output_size:
        length of the input buffer
        \ ``skip``\          number of output bytes to ignore
    :type output_size: unsigned long

    :param _skip:
        *undescribed*
    :type _skip: unsigned long

.. _`partial_decompress.description`:

Description
-----------

This function takes compressed data from inbuf, decompresses and write it to
outbuf. Once output_size bytes are written to the output buffer, or the
stream is exhausted the function will return the number of bytes that were
decompressed. Otherwise it will return whatever error code the decompressor
reported (NB: This is specific to each decompressor type).

The skip functionality is mainly there so the program and discover
the size of the compressed image so that it can ask firmware (if present)
for an appropriately sized buffer.

.. This file was automatic generated / don't edit.


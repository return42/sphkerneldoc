.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/decnet/dn_nsp_in.c

.. _`dn_check_idf`:

dn_check_idf
============

.. c:function:: int dn_check_idf(unsigned char **pptr, int *len, unsigned char max, unsigned char follow_on)

    Check an image data field format is correct.

    :param pptr:
        Pointer to pointer to image data
    :type pptr: unsigned char \*\*

    :param len:
        Pointer to length of image data
    :type len: int \*

    :param max:
        The maximum allowed length of the data in the image data field
    :type max: unsigned char

    :param follow_on:
        Check that this many bytes exist beyond the end of the image data
    :type follow_on: unsigned char

.. _`dn_check_idf.return`:

Return
------

0 if ok, -1 on error

.. This file was automatic generated / don't edit.


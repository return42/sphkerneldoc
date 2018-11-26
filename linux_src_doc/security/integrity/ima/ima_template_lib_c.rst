.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/integrity/ima/ima_template_lib.c

.. _`ima_parse_buf`:

ima_parse_buf
=============

.. c:function:: int ima_parse_buf(void *bufstartp, void *bufendp, void **bufcurp, int maxfields, struct ima_field_data *fields, int *curfields, unsigned long *len_mask, int enforce_mask, char *bufname)

    Parses lengths and data from an input buffer

    :param bufstartp:
        Buffer start address.
    :type bufstartp: void \*

    :param bufendp:
        Buffer end address.
    :type bufendp: void \*

    :param bufcurp:
        Pointer to remaining (non-parsed) data.
    :type bufcurp: void \*\*

    :param maxfields:
        Length of fields array.
    :type maxfields: int

    :param fields:
        Array containing lengths and pointers of parsed data.
    :type fields: struct ima_field_data \*

    :param curfields:
        Number of array items containing parsed data.
    :type curfields: int \*

    :param len_mask:
        Bitmap (if bit is set, data length should not be parsed).
    :type len_mask: unsigned long \*

    :param enforce_mask:
        Check if curfields == maxfields and/or bufcurp == bufendp.
    :type enforce_mask: int

    :param bufname:
        String identifier of the input buffer.
    :type bufname: char \*

.. _`ima_parse_buf.return`:

Return
------

0 on success, -EINVAL on error.

.. This file was automatic generated / don't edit.


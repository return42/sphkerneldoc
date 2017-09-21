.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/integrity/ima/ima_template_lib.c

.. _`ima_parse_buf`:

ima_parse_buf
=============

.. c:function:: int ima_parse_buf(void *bufstartp, void *bufendp, void **bufcurp, int maxfields, struct ima_field_data *fields, int *curfields, unsigned long *len_mask, int enforce_mask, char *bufname)

    Parses lengths and data from an input buffer

    :param void \*bufstartp:
        Buffer start address.

    :param void \*bufendp:
        Buffer end address.

    :param void \*\*bufcurp:
        Pointer to remaining (non-parsed) data.

    :param int maxfields:
        Length of fields array.

    :param struct ima_field_data \*fields:
        Array containing lengths and pointers of parsed data.

    :param int \*curfields:
        Number of array items containing parsed data.

    :param unsigned long \*len_mask:
        Bitmap (if bit is set, data length should not be parsed).

    :param int enforce_mask:
        Check if curfields == maxfields and/or bufcurp == bufendp.

    :param char \*bufname:
        String identifier of the input buffer.

.. _`ima_parse_buf.return`:

Return
------

0 on success, -EINVAL on error.

.. This file was automatic generated / don't edit.


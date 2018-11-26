.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/dccp/ccid.c

.. _`ccid_get_builtin_ccids`:

ccid_get_builtin_ccids
======================

.. c:function:: int ccid_get_builtin_ccids(u8 **ccid_array, u8 *array_len)

    Populate a list of built-in CCIDs

    :param ccid_array:
        pointer to copy into
    :type ccid_array: u8 \*\*

    :param array_len:
        value to return length into
    :type array_len: u8 \*

.. _`ccid_get_builtin_ccids.description`:

Description
-----------

This function allocates memory - caller must see that it is freed after use.

.. This file was automatic generated / don't edit.


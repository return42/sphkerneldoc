.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ntfs/collate.c

.. _`ntfs_collate`:

ntfs_collate
============

.. c:function:: int ntfs_collate(ntfs_volume *vol, COLLATION_RULE cr, const void *data1, const int data1_len, const void *data2, const int data2_len)

    collate two data items using a specified collation rule

    :param vol:
        ntfs volume to which the data items belong
    :type vol: ntfs_volume \*

    :param cr:
        collation rule to use when comparing the items
    :type cr: COLLATION_RULE

    :param data1:
        first data item to collate
    :type data1: const void \*

    :param data1_len:
        length in bytes of \ ``data1``\ 
    :type data1_len: const int

    :param data2:
        second data item to collate
    :type data2: const void \*

    :param data2_len:
        length in bytes of \ ``data2``\ 
    :type data2_len: const int

.. _`ntfs_collate.description`:

Description
-----------

Collate the two data items \ ``data1``\  and \ ``data2``\  using the collation rule \ ``cr``\ 
and return -1, 0, ir 1 if \ ``data1``\  is found, respectively, to collate before,
to match, or to collate after \ ``data2``\ .

For speed we use the collation rule \ ``cr``\  as an index into two tables of
function pointers to call the appropriate collation function.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/xfs/libxfs/xfs_btree.c

.. _`xfs_btree_sblock_v5hdr_verify`:

xfs_btree_sblock_v5hdr_verify
=============================

.. c:function:: xfs_failaddr_t xfs_btree_sblock_v5hdr_verify(struct xfs_buf *bp)

    - verify the v5 fields of a short-format btree block

    :param bp:
        buffer containing the btree block
    :type bp: struct xfs_buf \*

.. _`xfs_btree_sblock_verify`:

xfs_btree_sblock_verify
=======================

.. c:function:: xfs_failaddr_t xfs_btree_sblock_verify(struct xfs_buf *bp, unsigned int max_recs)

    - verify a short-format btree block

    :param bp:
        buffer containing the btree block
    :type bp: struct xfs_buf \*

    :param max_recs:
        maximum records allowed in this btree node
    :type max_recs: unsigned int

.. This file was automatic generated / don't edit.


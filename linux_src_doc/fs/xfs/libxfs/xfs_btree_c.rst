.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/xfs/libxfs/xfs_btree.c

.. _`xfs_btree_sblock_v5hdr_verify`:

xfs_btree_sblock_v5hdr_verify
=============================

.. c:function:: xfs_failaddr_t xfs_btree_sblock_v5hdr_verify(struct xfs_buf *bp)

    - verify the v5 fields of a short-format btree block

    :param struct xfs_buf \*bp:
        buffer containing the btree block

.. _`xfs_btree_sblock_verify`:

xfs_btree_sblock_verify
=======================

.. c:function:: xfs_failaddr_t xfs_btree_sblock_verify(struct xfs_buf *bp, unsigned int max_recs)

    - verify a short-format btree block

    :param struct xfs_buf \*bp:
        buffer containing the btree block

    :param unsigned int max_recs:
        maximum records allowed in this btree node

.. This file was automatic generated / don't edit.


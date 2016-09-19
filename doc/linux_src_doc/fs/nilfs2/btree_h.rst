.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/btree.h

.. _`nilfs_btree_path`:

struct nilfs_btree_path
=======================

.. c:type:: struct nilfs_btree_path

    A path on which B-tree operations are executed

.. _`nilfs_btree_path.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_btree_path {
        struct buffer_head *bp_bh;
        struct buffer_head *bp_sib_bh;
        int bp_index;
        union nilfs_bmap_ptr_req bp_oldreq;
        union nilfs_bmap_ptr_req bp_newreq;
        struct nilfs_btnode_chkey_ctxt bp_ctxt;
        void (*bp_op)(struct nilfs_bmap *, struct nilfs_btree_path *,int, __u64 *, __u64 *);
    }

.. _`nilfs_btree_path.members`:

Members
-------

bp_bh
    buffer head of node block

bp_sib_bh
    buffer head of sibling node block

bp_index
    index of child node

bp_oldreq
    ptr end request for old ptr

bp_newreq
    ptr alloc request for new ptr

bp_ctxt
    *undescribed*

bp_op
    rebalance operation

.. This file was automatic generated / don't edit.


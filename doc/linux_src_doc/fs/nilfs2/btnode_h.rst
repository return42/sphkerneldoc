.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/btnode.h

.. _`nilfs_btnode_chkey_ctxt`:

struct nilfs_btnode_chkey_ctxt
==============================

.. c:type:: struct nilfs_btnode_chkey_ctxt

    change key context

.. _`nilfs_btnode_chkey_ctxt.definition`:

Definition
----------

.. code-block:: c

    struct nilfs_btnode_chkey_ctxt {
        __u64 oldkey;
        __u64 newkey;
        struct buffer_head *bh;
        struct buffer_head *newbh;
    }

.. _`nilfs_btnode_chkey_ctxt.members`:

Members
-------

oldkey
    old key of block's moving content

newkey
    new key for block's content

bh
    buffer head of old buffer

newbh
    buffer head of new buffer

.. This file was automatic generated / don't edit.


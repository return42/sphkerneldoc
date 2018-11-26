.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/btnode.c

.. _`nilfs_btnode_delete`:

nilfs_btnode_delete
===================

.. c:function:: void nilfs_btnode_delete(struct buffer_head *bh)

    delete B-tree node buffer

    :param bh:
        buffer to be deleted
    :type bh: struct buffer_head \*

.. _`nilfs_btnode_delete.description`:

Description
-----------

\ :c:func:`nilfs_btnode_delete`\  invalidates the specified buffer and delete the page
including the buffer if the page gets unbusy.

.. _`nilfs_btnode_prepare_change_key`:

nilfs_btnode_prepare_change_key
===============================

.. c:function:: int nilfs_btnode_prepare_change_key(struct address_space *btnc, struct nilfs_btnode_chkey_ctxt *ctxt)

    prepare to move contents of the block for old key to one of new key. the old buffer will not be removed, but might be reused for new buffer. it might return -ENOMEM because of memory allocation errors, and might return -EIO because of disk read errors.

    :param btnc:
        *undescribed*
    :type btnc: struct address_space \*

    :param ctxt:
        *undescribed*
    :type ctxt: struct nilfs_btnode_chkey_ctxt \*

.. _`nilfs_btnode_commit_change_key`:

nilfs_btnode_commit_change_key
==============================

.. c:function:: void nilfs_btnode_commit_change_key(struct address_space *btnc, struct nilfs_btnode_chkey_ctxt *ctxt)

    commit the change_key operation prepared by \ :c:func:`prepare_change_key`\ .

    :param btnc:
        *undescribed*
    :type btnc: struct address_space \*

    :param ctxt:
        *undescribed*
    :type ctxt: struct nilfs_btnode_chkey_ctxt \*

.. _`nilfs_btnode_abort_change_key`:

nilfs_btnode_abort_change_key
=============================

.. c:function:: void nilfs_btnode_abort_change_key(struct address_space *btnc, struct nilfs_btnode_chkey_ctxt *ctxt)

    abort the change_key operation prepared by \ :c:func:`prepare_change_key`\ .

    :param btnc:
        *undescribed*
    :type btnc: struct address_space \*

    :param ctxt:
        *undescribed*
    :type ctxt: struct nilfs_btnode_chkey_ctxt \*

.. This file was automatic generated / don't edit.


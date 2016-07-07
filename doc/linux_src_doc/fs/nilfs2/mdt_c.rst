.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/mdt.c

.. _`nilfs_mdt_get_block`:

nilfs_mdt_get_block
===================

.. c:function:: int nilfs_mdt_get_block(struct inode *inode, unsigned long blkoff, int create, void (*) init_block (struct inode *, struct buffer_head *, void *, struct buffer_head **out_bh)

    read or create a buffer on meta data file.

    :param struct inode \*inode:
        inode of the meta data file

    :param unsigned long blkoff:
        block offset

    :param int create:
        create flag

    :param (void (\*) init_block (struct inode \*, struct buffer_head \*, void \*):
        initializer used for newly allocated block

    :param struct buffer_head \*\*out_bh:
        output of a pointer to the buffer_head

.. _`nilfs_mdt_get_block.description`:

Description
-----------

\ :c:func:`nilfs_mdt_get_block`\  looks up the specified buffer and tries to create
a new buffer if \ ``create``\  is not zero.  On success, the returned buffer is
assured to be either existing or formatted using a buffer lock on success.
\ ``out_bh``\  is substituted only when zero is returned.

.. _`nilfs_mdt_get_block.return-value`:

Return Value
------------

On success, it returns 0. On error, the following negative
error code is returned.

\ ``-ENOMEM``\  - Insufficient memory available.

\ ``-EIO``\  - I/O error

\ ``-ENOENT``\  - the specified block does not exist (hole block)

\ ``-EROFS``\  - Read only filesystem (for create mode)

.. _`nilfs_mdt_find_block`:

nilfs_mdt_find_block
====================

.. c:function:: int nilfs_mdt_find_block(struct inode *inode, unsigned long start, unsigned long end, unsigned long *blkoff, struct buffer_head **out_bh)

    find and get a buffer on meta data file.

    :param struct inode \*inode:
        inode of the meta data file

    :param unsigned long start:
        start block offset (inclusive)

    :param unsigned long end:
        end block offset (inclusive)

    :param unsigned long \*blkoff:
        block offset

    :param struct buffer_head \*\*out_bh:
        place to store a pointer to buffer_head struct

.. _`nilfs_mdt_find_block.description`:

Description
-----------

\ :c:func:`nilfs_mdt_find_block`\  looks up an existing block in range of
[\ ``start``\ , \ ``end``\ ] and stores pointer to a buffer head of the block to
\ ``out_bh``\ , and block offset to \ ``blkoff``\ , respectively.  \ ``out_bh``\  and
\ ``blkoff``\  are substituted only when zero is returned.

.. _`nilfs_mdt_find_block.return-value`:

Return Value
------------

On success, it returns 0. On error, the following negative
error code is returned.

\ ``-ENOMEM``\  - Insufficient memory available.

\ ``-EIO``\  - I/O error

\ ``-ENOENT``\  - no block was found in the range

.. _`nilfs_mdt_delete_block`:

nilfs_mdt_delete_block
======================

.. c:function:: int nilfs_mdt_delete_block(struct inode *inode, unsigned long block)

    make a hole on the meta data file.

    :param struct inode \*inode:
        inode of the meta data file

    :param unsigned long block:
        block offset

.. _`nilfs_mdt_delete_block.return-value`:

Return Value
------------

On success, zero is returned.
On error, one of the following negative error code is returned.

\ ``-ENOMEM``\  - Insufficient memory available.

\ ``-EIO``\  - I/O error

.. _`nilfs_mdt_forget_block`:

nilfs_mdt_forget_block
======================

.. c:function:: int nilfs_mdt_forget_block(struct inode *inode, unsigned long block)

    discard dirty state and try to remove the page

    :param struct inode \*inode:
        inode of the meta data file

    :param unsigned long block:
        block offset

.. _`nilfs_mdt_forget_block.description`:

Description
-----------

\ :c:func:`nilfs_mdt_forget_block`\  clears a dirty flag of the specified buffer, and
tries to release the page including the buffer from a page cache.

.. _`nilfs_mdt_forget_block.return-value`:

Return Value
------------

On success, 0 is returned. On error, one of the following
negative error code is returned.

\ ``-EBUSY``\  - page has an active buffer.

\ ``-ENOENT``\  - page cache has no page addressed by the offset.

.. _`nilfs_mdt_clear`:

nilfs_mdt_clear
===============

.. c:function:: void nilfs_mdt_clear(struct inode *inode)

    do cleanup for the metadata file

    :param struct inode \*inode:
        inode of the metadata file

.. _`nilfs_mdt_destroy`:

nilfs_mdt_destroy
=================

.. c:function:: void nilfs_mdt_destroy(struct inode *inode)

    release resources used by the metadata file

    :param struct inode \*inode:
        inode of the metadata file

.. _`nilfs_mdt_setup_shadow_map`:

nilfs_mdt_setup_shadow_map
==========================

.. c:function:: int nilfs_mdt_setup_shadow_map(struct inode *inode, struct nilfs_shadow_map *shadow)

    setup shadow map and bind it to metadata file

    :param struct inode \*inode:
        inode of the metadata file

    :param struct nilfs_shadow_map \*shadow:
        shadow mapping

.. _`nilfs_mdt_save_to_shadow_map`:

nilfs_mdt_save_to_shadow_map
============================

.. c:function:: int nilfs_mdt_save_to_shadow_map(struct inode *inode)

    copy bmap and dirty pages to shadow map

    :param struct inode \*inode:
        inode of the metadata file

.. _`nilfs_mdt_restore_from_shadow_map`:

nilfs_mdt_restore_from_shadow_map
=================================

.. c:function:: void nilfs_mdt_restore_from_shadow_map(struct inode *inode)

    restore dirty pages and bmap state

    :param struct inode \*inode:
        inode of the metadata file

.. _`nilfs_mdt_clear_shadow_map`:

nilfs_mdt_clear_shadow_map
==========================

.. c:function:: void nilfs_mdt_clear_shadow_map(struct inode *inode)

    truncate pages in shadow map caches

    :param struct inode \*inode:
        inode of the metadata file

.. This file was automatic generated / don't edit.


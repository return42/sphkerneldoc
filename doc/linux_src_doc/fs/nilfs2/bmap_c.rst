.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/bmap.c

.. _`nilfs_bmap_lookup_at_level`:

nilfs_bmap_lookup_at_level
==========================

.. c:function:: int nilfs_bmap_lookup_at_level(struct nilfs_bmap *bmap, __u64 key, int level, __u64 *ptrp)

    find a data block or node block

    :param struct nilfs_bmap \*bmap:
        bmap

    :param __u64 key:
        key

    :param int level:
        level

    :param __u64 \*ptrp:
        place to store the value associated to \ ``key``\ 

.. _`nilfs_bmap_lookup_at_level.description`:

Description
-----------

\ :c:func:`nilfs_bmap_lookup_at_level`\  finds a record whose key
matches \ ``key``\  in the block at \ ``level``\  of the bmap.

.. _`nilfs_bmap_lookup_at_level.return-value`:

Return Value
------------

On success, 0 is returned and the record associated with \ ``key``\ 
is stored in the place pointed by \ ``ptrp``\ . On error, one of the following
negative error codes is returned.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

\ ``-ENOENT``\  - A record associated with \ ``key``\  does not exist.

.. _`nilfs_bmap_insert`:

nilfs_bmap_insert
=================

.. c:function:: int nilfs_bmap_insert(struct nilfs_bmap *bmap, __u64 key, unsigned long rec)

    insert a new key-record pair into a bmap

    :param struct nilfs_bmap \*bmap:
        bmap

    :param __u64 key:
        key

    :param unsigned long rec:
        record

.. _`nilfs_bmap_insert.description`:

Description
-----------

\ :c:func:`nilfs_bmap_insert`\  inserts the new key-record pair specified
by \ ``key``\  and \ ``rec``\  into \ ``bmap``\ .

.. _`nilfs_bmap_insert.return-value`:

Return Value
------------

On success, 0 is returned. On error, one of the following
negative error codes is returned.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

\ ``-EEXIST``\  - A record associated with \ ``key``\  already exist.

.. _`nilfs_bmap_seek_key`:

nilfs_bmap_seek_key
===================

.. c:function:: int nilfs_bmap_seek_key(struct nilfs_bmap *bmap, __u64 start, __u64 *keyp)

    seek a valid entry and return its key

    :param struct nilfs_bmap \*bmap:
        bmap struct

    :param __u64 start:
        start key number

    :param __u64 \*keyp:
        place to store valid key

.. _`nilfs_bmap_seek_key.description`:

Description
-----------

\ :c:func:`nilfs_bmap_seek_key`\  seeks a valid key on \ ``bmap``\ 
starting from \ ``start``\ , and stores it to \ ``keyp``\  if found.

.. _`nilfs_bmap_seek_key.return-value`:

Return Value
------------

On success, 0 is returned. On error, one of the following
negative error codes is returned.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

\ ``-ENOENT``\  - No valid entry was found

.. _`nilfs_bmap_delete`:

nilfs_bmap_delete
=================

.. c:function:: int nilfs_bmap_delete(struct nilfs_bmap *bmap, __u64 key)

    delete a key-record pair from a bmap

    :param struct nilfs_bmap \*bmap:
        bmap

    :param __u64 key:
        key

.. _`nilfs_bmap_delete.description`:

Description
-----------

\ :c:func:`nilfs_bmap_delete`\  deletes the key-record pair specified by
\ ``key``\  from \ ``bmap``\ .

.. _`nilfs_bmap_delete.return-value`:

Return Value
------------

On success, 0 is returned. On error, one of the following
negative error codes is returned.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

\ ``-ENOENT``\  - A record associated with \ ``key``\  does not exist.

.. _`nilfs_bmap_truncate`:

nilfs_bmap_truncate
===================

.. c:function:: int nilfs_bmap_truncate(struct nilfs_bmap *bmap, __u64 key)

    truncate a bmap to a specified key

    :param struct nilfs_bmap \*bmap:
        bmap

    :param __u64 key:
        key

.. _`nilfs_bmap_truncate.description`:

Description
-----------

\ :c:func:`nilfs_bmap_truncate`\  removes key-record pairs whose keys are
greater than or equal to \ ``key``\  from \ ``bmap``\ .

.. _`nilfs_bmap_truncate.return-value`:

Return Value
------------

On success, 0 is returned. On error, one of the following
negative error codes is returned.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

.. _`nilfs_bmap_clear`:

nilfs_bmap_clear
================

.. c:function:: void nilfs_bmap_clear(struct nilfs_bmap *bmap)

    free resources a bmap holds

    :param struct nilfs_bmap \*bmap:
        bmap

.. _`nilfs_bmap_clear.description`:

Description
-----------

\ :c:func:`nilfs_bmap_clear`\  frees resources associated with \ ``bmap``\ .

.. _`nilfs_bmap_propagate`:

nilfs_bmap_propagate
====================

.. c:function:: int nilfs_bmap_propagate(struct nilfs_bmap *bmap, struct buffer_head *bh)

    propagate dirty state

    :param struct nilfs_bmap \*bmap:
        bmap

    :param struct buffer_head \*bh:
        buffer head

.. _`nilfs_bmap_propagate.description`:

Description
-----------

\ :c:func:`nilfs_bmap_propagate`\  marks the buffers that directly or
indirectly refer to the block specified by \ ``bh``\  dirty.

.. _`nilfs_bmap_propagate.return-value`:

Return Value
------------

On success, 0 is returned. On error, one of the following
negative error codes is returned.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

.. _`nilfs_bmap_lookup_dirty_buffers`:

nilfs_bmap_lookup_dirty_buffers
===============================

.. c:function:: void nilfs_bmap_lookup_dirty_buffers(struct nilfs_bmap *bmap, struct list_head *listp)

    :param struct nilfs_bmap \*bmap:
        bmap

    :param struct list_head \*listp:
        pointer to buffer head list

.. _`nilfs_bmap_assign`:

nilfs_bmap_assign
=================

.. c:function:: int nilfs_bmap_assign(struct nilfs_bmap *bmap, struct buffer_head **bh, unsigned long blocknr, union nilfs_binfo *binfo)

    assign a new block number to a block

    :param struct nilfs_bmap \*bmap:
        bmap

    :param struct buffer_head \*\*bh:
        *undescribed*

    :param unsigned long blocknr:
        block number

    :param union nilfs_binfo \*binfo:
        block information

.. _`nilfs_bmap_assign.description`:

Description
-----------

\ :c:func:`nilfs_bmap_assign`\  assigns the block number \ ``blocknr``\  to the
buffer specified by \ ``bh``\ .

.. _`nilfs_bmap_assign.return-value`:

Return Value
------------

On success, 0 is returned and the buffer head of a newly
create buffer and the block information associated with the buffer are
stored in the place pointed by \ ``bh``\  and \ ``binfo``\ , respectively. On error, one
of the following negative error codes is returned.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

.. _`nilfs_bmap_mark`:

nilfs_bmap_mark
===============

.. c:function:: int nilfs_bmap_mark(struct nilfs_bmap *bmap, __u64 key, int level)

    mark block dirty

    :param struct nilfs_bmap \*bmap:
        bmap

    :param __u64 key:
        key

    :param int level:
        level

.. _`nilfs_bmap_mark.description`:

Description
-----------

\ :c:func:`nilfs_bmap_mark`\  marks the block specified by \ ``key``\  and \ ``level``\ 
as dirty.

.. _`nilfs_bmap_mark.return-value`:

Return Value
------------

On success, 0 is returned. On error, one of the following
negative error codes is returned.

\ ``-EIO``\  - I/O error.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

.. _`nilfs_bmap_test_and_clear_dirty`:

nilfs_bmap_test_and_clear_dirty
===============================

.. c:function:: int nilfs_bmap_test_and_clear_dirty(struct nilfs_bmap *bmap)

    test and clear a bmap dirty state

    :param struct nilfs_bmap \*bmap:
        bmap

.. _`nilfs_bmap_test_and_clear_dirty.description`:

Description
-----------

\ :c:func:`nilfs_test_and_clear`\  is the atomic operation to test and
clear the dirty state of \ ``bmap``\ .

.. _`nilfs_bmap_test_and_clear_dirty.return-value`:

Return Value
------------

1 is returned if \ ``bmap``\  is dirty, or 0 if clear.

.. _`nilfs_bmap_read`:

nilfs_bmap_read
===============

.. c:function:: int nilfs_bmap_read(struct nilfs_bmap *bmap, struct nilfs_inode *raw_inode)

    read a bmap from an inode

    :param struct nilfs_bmap \*bmap:
        bmap

    :param struct nilfs_inode \*raw_inode:
        on-disk inode

.. _`nilfs_bmap_read.description`:

Description
-----------

\ :c:func:`nilfs_bmap_read`\  initializes the bmap \ ``bmap``\ .

.. _`nilfs_bmap_read.return-value`:

Return Value
------------

On success, 0 is returned. On error, the following negative
error code is returned.

\ ``-ENOMEM``\  - Insufficient amount of memory available.

.. _`nilfs_bmap_write`:

nilfs_bmap_write
================

.. c:function:: void nilfs_bmap_write(struct nilfs_bmap *bmap, struct nilfs_inode *raw_inode)

    write back a bmap to an inode

    :param struct nilfs_bmap \*bmap:
        bmap

    :param struct nilfs_inode \*raw_inode:
        on-disk inode

.. _`nilfs_bmap_write.description`:

Description
-----------

\ :c:func:`nilfs_bmap_write`\  stores \ ``bmap``\  in \ ``raw_inode``\ .

.. This file was automatic generated / don't edit.


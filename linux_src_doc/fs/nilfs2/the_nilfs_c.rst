.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/the_nilfs.c

.. _`alloc_nilfs`:

alloc_nilfs
===========

.. c:function:: struct the_nilfs *alloc_nilfs(struct block_device *bdev)

    allocate a nilfs object

    :param struct block_device \*bdev:
        block device to which the_nilfs is related

.. _`alloc_nilfs.return-value`:

Return Value
------------

On success, pointer to the_nilfs is returned.
On error, NULL is returned.

.. _`destroy_nilfs`:

destroy_nilfs
=============

.. c:function:: void destroy_nilfs(struct the_nilfs *nilfs)

    destroy nilfs object

    :param struct the_nilfs \*nilfs:
        nilfs object to be released

.. _`nilfs_store_log_cursor`:

nilfs_store_log_cursor
======================

.. c:function:: int nilfs_store_log_cursor(struct the_nilfs *nilfs, struct nilfs_super_block *sbp)

    load log cursor from a super block

    :param struct the_nilfs \*nilfs:
        nilfs object

    :param struct nilfs_super_block \*sbp:
        buffer storing super block to be read

.. _`nilfs_store_log_cursor.description`:

Description
-----------

\ :c:func:`nilfs_store_log_cursor`\  reads the last position of the log
containing a super root from a given super block, and initializes
relevant information on the nilfs object preparatory for log
scanning and recovery.

.. _`load_nilfs`:

load_nilfs
==========

.. c:function:: int load_nilfs(struct the_nilfs *nilfs, struct super_block *sb)

    load and recover the nilfs

    :param struct the_nilfs \*nilfs:
        the_nilfs structure to be released

    :param struct super_block \*sb:
        super block isntance used to recover past segment

.. _`load_nilfs.description`:

Description
-----------

\ :c:func:`load_nilfs`\  searches and load the latest super root,
attaches the last segment, and does recovery if needed.
The caller must call this exclusively for simultaneous mounts.

.. _`nilfs_nrsvsegs`:

nilfs_nrsvsegs
==============

.. c:function:: unsigned long nilfs_nrsvsegs(struct the_nilfs *nilfs, unsigned long nsegs)

    calculate the number of reserved segments

    :param struct the_nilfs \*nilfs:
        nilfs object

    :param unsigned long nsegs:
        total number of segments

.. _`init_nilfs`:

init_nilfs
==========

.. c:function:: int init_nilfs(struct the_nilfs *nilfs, struct super_block *sb, char *data)

    initialize a NILFS instance.

    :param struct the_nilfs \*nilfs:
        the_nilfs structure

    :param struct super_block \*sb:
        super block

    :param char \*data:
        mount options

.. _`init_nilfs.description`:

Description
-----------

\ :c:func:`init_nilfs`\  performs common initialization per block device (e.g.
reading the super block, getting disk layout information, initializing
shared fields in the_nilfs).

.. _`init_nilfs.return-value`:

Return Value
------------

On success, 0 is returned. On error, a negative error
code is returned.

.. This file was automatic generated / don't edit.


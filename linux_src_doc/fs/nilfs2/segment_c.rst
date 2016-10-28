.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nilfs2/segment.c

.. _`nilfs_transaction_begin`:

nilfs_transaction_begin
=======================

.. c:function:: int nilfs_transaction_begin(struct super_block *sb, struct nilfs_transaction_info *ti, int vacancy_check)

    start indivisible file operations.

    :param struct super_block \*sb:
        super block

    :param struct nilfs_transaction_info \*ti:
        nilfs_transaction_info

    :param int vacancy_check:
        flags for vacancy rate checks

.. _`nilfs_transaction_begin.description`:

Description
-----------

\ :c:func:`nilfs_transaction_begin`\  acquires a reader/writer semaphore, called
the segment semaphore, to make a segment construction and write tasks
exclusive.  The function is used with \ :c:func:`nilfs_transaction_commit`\  in pairs.
The region enclosed by these two functions can be nested.  To avoid a
deadlock, the semaphore is only acquired or released in the outermost call.

This function allocates a nilfs_transaction_info struct to keep context
information on it.  It is initialized and hooked onto the current task in
the outermost call.  If a pre-allocated struct is given to \ ``ti``\ , it is used
instead; otherwise a new struct is assigned from a slab.

When \ ``vacancy_check``\  flag is set, this function will check the amount of
free space, and will wait for the GC to reclaim disk space if low capacity.

.. _`nilfs_transaction_begin.return-value`:

Return Value
------------

On success, 0 is returned. On error, one of the following
negative error code is returned.

\ ``-ENOMEM``\  - Insufficient memory available.

\ ``-ENOSPC``\  - No space left on device

.. _`nilfs_transaction_commit`:

nilfs_transaction_commit
========================

.. c:function:: int nilfs_transaction_commit(struct super_block *sb)

    commit indivisible file operations.

    :param struct super_block \*sb:
        super block

.. _`nilfs_transaction_commit.description`:

Description
-----------

\ :c:func:`nilfs_transaction_commit`\  releases the read semaphore which is
acquired by \ :c:func:`nilfs_transaction_begin`\ . This is only performed
in outermost call of this function.  If a commit flag is set,
\ :c:func:`nilfs_transaction_commit`\  sets a timer to start the segment
constructor.  If a sync flag is set, it starts construction
directly.

.. _`nilfs_segctor_reset_segment_buffer`:

nilfs_segctor_reset_segment_buffer
==================================

.. c:function:: int nilfs_segctor_reset_segment_buffer(struct nilfs_sc_info *sci)

    reset the current segment buffer

    :param struct nilfs_sc_info \*sci:
        nilfs_sc_info

.. _`nilfs_segctor_begin_construction`:

nilfs_segctor_begin_construction
================================

.. c:function:: int nilfs_segctor_begin_construction(struct nilfs_sc_info *sci, struct the_nilfs *nilfs)

    setup segment buffer to make a new log

    :param struct nilfs_sc_info \*sci:
        nilfs_sc_info

    :param struct the_nilfs \*nilfs:
        nilfs object

.. _`nilfs_segctor_start_timer`:

nilfs_segctor_start_timer
=========================

.. c:function:: void nilfs_segctor_start_timer(struct nilfs_sc_info *sci)

    set timer of background write

    :param struct nilfs_sc_info \*sci:
        nilfs_sc_info

.. _`nilfs_segctor_start_timer.description`:

Description
-----------

If the timer has already been set, it ignores the new request.
This function MUST be called within a section locking the segment
semaphore.

.. _`nilfs_flush_segment`:

nilfs_flush_segment
===================

.. c:function:: void nilfs_flush_segment(struct super_block *sb, ino_t ino)

    trigger a segment construction for resource control

    :param struct super_block \*sb:
        super block

    :param ino_t ino:
        inode number of the file to be flushed out.

.. _`nilfs_construct_segment`:

nilfs_construct_segment
=======================

.. c:function:: int nilfs_construct_segment(struct super_block *sb)

    construct a logical segment

    :param struct super_block \*sb:
        super block

.. _`nilfs_construct_segment.return-value`:

Return Value
------------

On success, 0 is retured. On errors, one of the following
negative error code is returned.

\ ``-EROFS``\  - Read only filesystem.

\ ``-EIO``\  - I/O error

\ ``-ENOSPC``\  - No space left on device (only in a panic state).

\ ``-ERESTARTSYS``\  - Interrupted.

\ ``-ENOMEM``\  - Insufficient memory available.

.. _`nilfs_construct_dsync_segment`:

nilfs_construct_dsync_segment
=============================

.. c:function:: int nilfs_construct_dsync_segment(struct super_block *sb, struct inode *inode, loff_t start, loff_t end)

    construct a data-only logical segment

    :param struct super_block \*sb:
        super block

    :param struct inode \*inode:
        inode whose data blocks should be written out

    :param loff_t start:
        start byte offset

    :param loff_t end:
        end byte offset (inclusive)

.. _`nilfs_construct_dsync_segment.return-value`:

Return Value
------------

On success, 0 is retured. On errors, one of the following
negative error code is returned.

\ ``-EROFS``\  - Read only filesystem.

\ ``-EIO``\  - I/O error

\ ``-ENOSPC``\  - No space left on device (only in a panic state).

\ ``-ERESTARTSYS``\  - Interrupted.

\ ``-ENOMEM``\  - Insufficient memory available.

.. _`nilfs_segctor_accept`:

nilfs_segctor_accept
====================

.. c:function:: void nilfs_segctor_accept(struct nilfs_sc_info *sci)

    record accepted sequence count of log-write requests

    :param struct nilfs_sc_info \*sci:
        segment constructor object

.. _`nilfs_segctor_notify`:

nilfs_segctor_notify
====================

.. c:function:: void nilfs_segctor_notify(struct nilfs_sc_info *sci, int mode, int err)

    notify the result of request to caller threads

    :param struct nilfs_sc_info \*sci:
        segment constructor object

    :param int mode:
        mode of log forming

    :param int err:
        error code to be notified

.. _`nilfs_segctor_construct`:

nilfs_segctor_construct
=======================

.. c:function:: int nilfs_segctor_construct(struct nilfs_sc_info *sci, int mode)

    form logs and write them to disk

    :param struct nilfs_sc_info \*sci:
        segment constructor object

    :param int mode:
        mode of log forming

.. _`nilfs_segctor_thread`:

nilfs_segctor_thread
====================

.. c:function:: int nilfs_segctor_thread(void *arg)

    main loop of the segment constructor thread.

    :param void \*arg:
        pointer to a struct nilfs_sc_info.

.. _`nilfs_segctor_thread.description`:

Description
-----------

\ :c:func:`nilfs_segctor_thread`\  initializes a timer and serves as a daemon
to execute segment constructions.

.. _`nilfs_segctor_destroy`:

nilfs_segctor_destroy
=====================

.. c:function:: void nilfs_segctor_destroy(struct nilfs_sc_info *sci)

    destroy the segment constructor.

    :param struct nilfs_sc_info \*sci:
        nilfs_sc_info

.. _`nilfs_segctor_destroy.description`:

Description
-----------

\ :c:func:`nilfs_segctor_destroy`\  kills the segctord thread and frees
the nilfs_sc_info struct.
Caller must hold the segment semaphore.

.. _`nilfs_attach_log_writer`:

nilfs_attach_log_writer
=======================

.. c:function:: int nilfs_attach_log_writer(struct super_block *sb, struct nilfs_root *root)

    attach log writer

    :param struct super_block \*sb:
        super block instance

    :param struct nilfs_root \*root:
        root object of the current filesystem tree

.. _`nilfs_attach_log_writer.description`:

Description
-----------

This allocates a log writer object, initializes it, and starts the
log writer.

.. _`nilfs_attach_log_writer.return-value`:

Return Value
------------

On success, 0 is returned. On error, one of the following
negative error code is returned.

\ ``-ENOMEM``\  - Insufficient memory available.

.. _`nilfs_detach_log_writer`:

nilfs_detach_log_writer
=======================

.. c:function:: void nilfs_detach_log_writer(struct super_block *sb)

    destroy log writer

    :param struct super_block \*sb:
        super block instance

.. _`nilfs_detach_log_writer.description`:

Description
-----------

This kills log writer daemon, frees the log writer object, and
destroys list of dirty files.

.. This file was automatic generated / don't edit.


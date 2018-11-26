.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/relay.c

.. _`relay_mmap_buf`:

relay_mmap_buf
==============

.. c:function:: int relay_mmap_buf(struct rchan_buf *buf, struct vm_area_struct *vma)

    - mmap channel buffer to process address space

    :param buf:
        relay channel buffer
    :type buf: struct rchan_buf \*

    :param vma:
        vm_area_struct describing memory to be mapped
    :type vma: struct vm_area_struct \*

.. _`relay_mmap_buf.description`:

Description
-----------

     Returns 0 if ok, negative on error

     Caller should already have grabbed mmap_sem.

.. _`relay_alloc_buf`:

relay_alloc_buf
===============

.. c:function:: void *relay_alloc_buf(struct rchan_buf *buf, size_t *size)

    allocate a channel buffer

    :param buf:
        the buffer struct
    :type buf: struct rchan_buf \*

    :param size:
        total size of the buffer
    :type size: size_t \*

.. _`relay_alloc_buf.description`:

Description
-----------

     Returns a pointer to the resulting buffer, \ ``NULL``\  if unsuccessful. The
     passed in size will get page aligned, if it isn't already.

.. _`relay_create_buf`:

relay_create_buf
================

.. c:function:: struct rchan_buf *relay_create_buf(struct rchan *chan)

    allocate and initialize a channel buffer

    :param chan:
        the relay channel
    :type chan: struct rchan \*

.. _`relay_create_buf.description`:

Description
-----------

     Returns channel buffer if successful, \ ``NULL``\  otherwise.

.. _`relay_destroy_channel`:

relay_destroy_channel
=====================

.. c:function:: void relay_destroy_channel(struct kref *kref)

    free the channel struct

    :param kref:
        target kernel reference that contains the relay channel
    :type kref: struct kref \*

.. _`relay_destroy_channel.description`:

Description
-----------

     Should only be called from \ :c:func:`kref_put`\ .

.. _`relay_destroy_buf`:

relay_destroy_buf
=================

.. c:function:: void relay_destroy_buf(struct rchan_buf *buf)

    destroy an rchan_buf struct and associated buffer

    :param buf:
        the buffer struct
    :type buf: struct rchan_buf \*

.. _`relay_remove_buf`:

relay_remove_buf
================

.. c:function:: void relay_remove_buf(struct kref *kref)

    remove a channel buffer

    :param kref:
        target kernel reference that contains the relay buffer
    :type kref: struct kref \*

.. _`relay_remove_buf.description`:

Description
-----------

     Removes the file from the filesystem, which also frees the
     rchan_buf_struct and the channel buffer.  Should only be called from
     \ :c:func:`kref_put`\ .

.. _`relay_buf_empty`:

relay_buf_empty
===============

.. c:function:: int relay_buf_empty(struct rchan_buf *buf)

    boolean, is the channel buffer empty?

    :param buf:
        channel buffer
    :type buf: struct rchan_buf \*

.. _`relay_buf_empty.description`:

Description
-----------

     Returns 1 if the buffer is empty, 0 otherwise.

.. _`relay_buf_full`:

relay_buf_full
==============

.. c:function:: int relay_buf_full(struct rchan_buf *buf)

    boolean, is the channel buffer full?

    :param buf:
        channel buffer
    :type buf: struct rchan_buf \*

.. _`relay_buf_full.description`:

Description
-----------

     Returns 1 if the buffer is full, 0 otherwise.

.. _`wakeup_readers`:

wakeup_readers
==============

.. c:function:: void wakeup_readers(struct irq_work *work)

    wake up readers waiting on a channel

    :param work:
        contains the channel buffer
    :type work: struct irq_work \*

.. _`wakeup_readers.description`:

Description
-----------

     This is the function used to defer reader waking

.. _`__relay_reset`:

__relay_reset
=============

.. c:function:: void __relay_reset(struct rchan_buf *buf, unsigned int init)

    reset a channel buffer

    :param buf:
        the channel buffer
    :type buf: struct rchan_buf \*

    :param init:
        1 if this is a first-time initialization
    :type init: unsigned int

.. _`__relay_reset.description`:

Description
-----------

     See \ :c:func:`relay_reset`\  for description of effect.

.. _`relay_reset`:

relay_reset
===========

.. c:function:: void relay_reset(struct rchan *chan)

    reset the channel

    :param chan:
        the channel
    :type chan: struct rchan \*

.. _`relay_reset.description`:

Description
-----------

     This has the effect of erasing all data from all channel buffers
     and restarting the channel in its initial state.  The buffers
     are not freed, so any mappings are still in effect.

     NOTE. Care should be taken that the channel isn't actually
     being used by anything when this call is made.

.. _`relay_close_buf`:

relay_close_buf
===============

.. c:function:: void relay_close_buf(struct rchan_buf *buf)

    close a channel buffer

    :param buf:
        channel buffer
    :type buf: struct rchan_buf \*

.. _`relay_close_buf.description`:

Description
-----------

     Marks the buffer finalized and restores the default callbacks.
     The channel buffer and channel buffer data structure are then freed
     automatically when the last reference is given up.

.. _`relay_open`:

relay_open
==========

.. c:function:: struct rchan *relay_open(const char *base_filename, struct dentry *parent, size_t subbuf_size, size_t n_subbufs, struct rchan_callbacks *cb, void *private_data)

    create a new relay channel

    :param base_filename:
        base name of files to create, \ ``NULL``\  for buffering only
    :type base_filename: const char \*

    :param parent:
        dentry of parent directory, \ ``NULL``\  for root directory or buffer
    :type parent: struct dentry \*

    :param subbuf_size:
        size of sub-buffers
    :type subbuf_size: size_t

    :param n_subbufs:
        number of sub-buffers
    :type n_subbufs: size_t

    :param cb:
        client callback functions
    :type cb: struct rchan_callbacks \*

    :param private_data:
        user-defined data
    :type private_data: void \*

.. _`relay_open.description`:

Description
-----------

     Returns channel pointer if successful, \ ``NULL``\  otherwise.

     Creates a channel buffer for each cpu using the sizes and
     attributes specified.  The created channel buffer files
     will be named base_filename0...base_filenameN-1.  File
     permissions will be \ ``S_IRUSR``\ .

     If opening a buffer (@parent = NULL) that you later wish to register
     in a filesystem, call \ :c:func:`relay_late_setup_files`\  once the \ ``parent``\  dentry
     is available.

.. _`relay_late_setup_files`:

relay_late_setup_files
======================

.. c:function:: int relay_late_setup_files(struct rchan *chan, const char *base_filename, struct dentry *parent)

    triggers file creation

    :param chan:
        channel to operate on
    :type chan: struct rchan \*

    :param base_filename:
        base name of files to create
    :type base_filename: const char \*

    :param parent:
        dentry of parent directory, \ ``NULL``\  for root directory
    :type parent: struct dentry \*

.. _`relay_late_setup_files.description`:

Description
-----------

     Returns 0 if successful, non-zero otherwise.

     Use to setup files for a previously buffer-only channel created
     by \ :c:func:`relay_open`\  with a NULL parent dentry.

     For example, this is useful for perfomring early tracing in kernel,
     before VFS is up and then exposing the early results once the dentry
     is available.

.. _`relay_switch_subbuf`:

relay_switch_subbuf
===================

.. c:function:: size_t relay_switch_subbuf(struct rchan_buf *buf, size_t length)

    switch to a new sub-buffer

    :param buf:
        channel buffer
    :type buf: struct rchan_buf \*

    :param length:
        size of current event
    :type length: size_t

.. _`relay_switch_subbuf.description`:

Description
-----------

     Returns either the length passed in or 0 if full.

     Performs sub-buffer-switch tasks such as invoking callbacks,
     updating padding counts, waking up readers, etc.

.. _`relay_subbufs_consumed`:

relay_subbufs_consumed
======================

.. c:function:: void relay_subbufs_consumed(struct rchan *chan, unsigned int cpu, size_t subbufs_consumed)

    update the buffer's sub-buffers-consumed count

    :param chan:
        the channel
    :type chan: struct rchan \*

    :param cpu:
        the cpu associated with the channel buffer to update
    :type cpu: unsigned int

    :param subbufs_consumed:
        number of sub-buffers to add to current buf's count
    :type subbufs_consumed: size_t

.. _`relay_subbufs_consumed.description`:

Description
-----------

     Adds to the channel buffer's consumed sub-buffer count.
     subbufs_consumed should be the number of sub-buffers newly consumed,
     not the total consumed.

     NOTE. Kernel clients don't need to call this function if the channel
     mode is 'overwrite'.

.. _`relay_close`:

relay_close
===========

.. c:function:: void relay_close(struct rchan *chan)

    close the channel

    :param chan:
        the channel
    :type chan: struct rchan \*

.. _`relay_close.description`:

Description
-----------

     Closes all channel buffers and frees the channel.

.. _`relay_flush`:

relay_flush
===========

.. c:function:: void relay_flush(struct rchan *chan)

    close the channel

    :param chan:
        the channel
    :type chan: struct rchan \*

.. _`relay_flush.description`:

Description
-----------

     Flushes all channel buffers, i.e. forces buffer switch.

.. _`relay_file_open`:

relay_file_open
===============

.. c:function:: int relay_file_open(struct inode *inode, struct file *filp)

    open file op for relay files

    :param inode:
        the inode
    :type inode: struct inode \*

    :param filp:
        the file
    :type filp: struct file \*

.. _`relay_file_open.description`:

Description
-----------

     Increments the channel buffer refcount.

.. _`relay_file_mmap`:

relay_file_mmap
===============

.. c:function:: int relay_file_mmap(struct file *filp, struct vm_area_struct *vma)

    mmap file op for relay files

    :param filp:
        the file
    :type filp: struct file \*

    :param vma:
        the vma describing what to map
    :type vma: struct vm_area_struct \*

.. _`relay_file_mmap.description`:

Description
-----------

     Calls upon \ :c:func:`relay_mmap_buf`\  to map the file into user space.

.. _`relay_file_poll`:

relay_file_poll
===============

.. c:function:: __poll_t relay_file_poll(struct file *filp, poll_table *wait)

    poll file op for relay files

    :param filp:
        the file
    :type filp: struct file \*

    :param wait:
        poll table
    :type wait: poll_table \*

.. _`relay_file_poll.description`:

Description
-----------

     Poll implemention.

.. _`relay_file_release`:

relay_file_release
==================

.. c:function:: int relay_file_release(struct inode *inode, struct file *filp)

    release file op for relay files

    :param inode:
        the inode
    :type inode: struct inode \*

    :param filp:
        the file
    :type filp: struct file \*

.. _`relay_file_release.description`:

Description
-----------

     Decrements the channel refcount, as the filesystem is
     no longer using it.

.. _`relay_file_read_subbuf_avail`:

relay_file_read_subbuf_avail
============================

.. c:function:: size_t relay_file_read_subbuf_avail(size_t read_pos, struct rchan_buf *buf)

    return bytes available in sub-buffer

    :param read_pos:
        file read position
    :type read_pos: size_t

    :param buf:
        relay channel buffer
    :type buf: struct rchan_buf \*

.. _`relay_file_read_start_pos`:

relay_file_read_start_pos
=========================

.. c:function:: size_t relay_file_read_start_pos(size_t read_pos, struct rchan_buf *buf)

    find the first available byte to read

    :param read_pos:
        file read position
    :type read_pos: size_t

    :param buf:
        relay channel buffer
    :type buf: struct rchan_buf \*

.. _`relay_file_read_start_pos.description`:

Description
-----------

     If the \ ``read_pos``\  is in the middle of padding, return the
     position of the first actually available byte, otherwise
     return the original value.

.. _`relay_file_read_end_pos`:

relay_file_read_end_pos
=======================

.. c:function:: size_t relay_file_read_end_pos(struct rchan_buf *buf, size_t read_pos, size_t count)

    return the new read position

    :param buf:
        relay channel buffer
    :type buf: struct rchan_buf \*

    :param read_pos:
        file read position
    :type read_pos: size_t

    :param count:
        number of bytes to be read
    :type count: size_t

.. This file was automatic generated / don't edit.


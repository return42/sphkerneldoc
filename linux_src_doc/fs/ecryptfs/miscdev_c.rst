.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ecryptfs/miscdev.c

.. _`ecryptfs_miscdev_poll`:

ecryptfs_miscdev_poll
=====================

.. c:function:: __poll_t ecryptfs_miscdev_poll(struct file *file, poll_table *pt)

    :param file:
        dev file
    :type file: struct file \*

    :param pt:
        dev poll table (ignored)
    :type pt: poll_table \*

.. _`ecryptfs_miscdev_poll.description`:

Description
-----------

Returns the poll mask

.. _`ecryptfs_miscdev_open`:

ecryptfs_miscdev_open
=====================

.. c:function:: int ecryptfs_miscdev_open(struct inode *inode, struct file *file)

    :param inode:
        inode of miscdev handle (ignored)
    :type inode: struct inode \*

    :param file:
        file for miscdev handle
    :type file: struct file \*

.. _`ecryptfs_miscdev_open.description`:

Description
-----------

Returns zero on success; non-zero otherwise

.. _`ecryptfs_miscdev_release`:

ecryptfs_miscdev_release
========================

.. c:function:: int ecryptfs_miscdev_release(struct inode *inode, struct file *file)

    :param inode:
        inode of fs/ecryptfs/euid handle (ignored)
    :type inode: struct inode \*

    :param file:
        file for fs/ecryptfs/euid handle
    :type file: struct file \*

.. _`ecryptfs_miscdev_release.description`:

Description
-----------

This keeps the daemon registered until the daemon sends another
ioctl to fs/ecryptfs/ctl or until the kernel module unregisters.

Returns zero on success; non-zero otherwise

.. _`ecryptfs_send_miscdev`:

ecryptfs_send_miscdev
=====================

.. c:function:: int ecryptfs_send_miscdev(char *data, size_t data_size, struct ecryptfs_msg_ctx *msg_ctx, u8 msg_type, u16 msg_flags, struct ecryptfs_daemon *daemon)

    :param data:
        Data to send to daemon; may be NULL
    :type data: char \*

    :param data_size:
        Amount of data to send to daemon
    :type data_size: size_t

    :param msg_ctx:
        Message context, which is used to handle the reply. If
        this is NULL, then we do not expect a reply.
    :type msg_ctx: struct ecryptfs_msg_ctx \*

    :param msg_type:
        Type of message
    :type msg_type: u8

    :param msg_flags:
        Flags for message
    :type msg_flags: u16

    :param daemon:
        eCryptfs daemon object
    :type daemon: struct ecryptfs_daemon \*

.. _`ecryptfs_send_miscdev.description`:

Description
-----------

Add msg_ctx to queue and then, if it exists, notify the blocked
miscdevess about the data being available. Must be called with
ecryptfs_daemon_hash_mux held.

Returns zero on success; non-zero otherwise

.. _`ecryptfs_miscdev_read`:

ecryptfs_miscdev_read
=====================

.. c:function:: ssize_t ecryptfs_miscdev_read(struct file *file, char __user *buf, size_t count, loff_t *ppos)

    format and send message from queue

    :param file:
        miscdevfs handle
    :type file: struct file \*

    :param buf:
        User buffer into which to copy the next message on the daemon queue
    :type buf: char __user \*

    :param count:
        Amount of space available in \ ``buf``\ 
    :type count: size_t

    :param ppos:
        Offset in file (ignored)
    :type ppos: loff_t \*

.. _`ecryptfs_miscdev_read.description`:

Description
-----------

Pulls the most recent message from the daemon queue, formats it for
being sent via a miscdevfs handle, and copies it into \ ``buf``\ 

Returns the number of bytes copied into the user buffer

.. _`ecryptfs_miscdev_response`:

ecryptfs_miscdev_response
=========================

.. c:function:: int ecryptfs_miscdev_response(struct ecryptfs_daemon *daemon, char *data, size_t data_size, u32 seq)

    miscdevess response to message previously sent to daemon

    :param daemon:
        *undescribed*
    :type daemon: struct ecryptfs_daemon \*

    :param data:
        Bytes comprising struct ecryptfs_message
    :type data: char \*

    :param data_size:
        sizeof(struct ecryptfs_message) + data len
    :type data_size: size_t

    :param seq:
        Sequence number for miscdev response packet
    :type seq: u32

.. _`ecryptfs_miscdev_response.description`:

Description
-----------

Returns zero on success; non-zero otherwise

.. _`ecryptfs_miscdev_write`:

ecryptfs_miscdev_write
======================

.. c:function:: ssize_t ecryptfs_miscdev_write(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    handle write to daemon miscdev handle

    :param file:
        File for misc dev handle
    :type file: struct file \*

    :param buf:
        Buffer containing user data
    :type buf: const char __user \*

    :param count:
        Amount of data in \ ``buf``\ 
    :type count: size_t

    :param ppos:
        Pointer to offset in file (ignored)
    :type ppos: loff_t \*

.. _`ecryptfs_miscdev_write.description`:

Description
-----------

Returns the number of bytes read from \ ``buf``\ 

.. _`ecryptfs_init_ecryptfs_miscdev`:

ecryptfs_init_ecryptfs_miscdev
==============================

.. c:function:: int ecryptfs_init_ecryptfs_miscdev( void)

    :param void:
        no arguments
    :type void: 

.. _`ecryptfs_init_ecryptfs_miscdev.description`:

Description
-----------

Messages sent to the userspace daemon from the kernel are placed on
a queue associated with the daemon. The next read against the
miscdev handle by that daemon will return the oldest message placed
on the message queue for the daemon.

Returns zero on success; non-zero otherwise

.. _`ecryptfs_destroy_ecryptfs_miscdev`:

ecryptfs_destroy_ecryptfs_miscdev
=================================

.. c:function:: void ecryptfs_destroy_ecryptfs_miscdev( void)

    :param void:
        no arguments
    :type void: 

.. _`ecryptfs_destroy_ecryptfs_miscdev.description`:

Description
-----------

All of the daemons must be exorcised prior to calling this
function.

.. This file was automatic generated / don't edit.


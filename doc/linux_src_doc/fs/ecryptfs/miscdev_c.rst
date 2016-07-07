.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/ecryptfs/miscdev.c

.. _`ecryptfs_miscdev_poll`:

ecryptfs_miscdev_poll
=====================

.. c:function:: unsigned int ecryptfs_miscdev_poll(struct file *file, poll_table *pt)

    :param struct file \*file:
        dev file

    :param poll_table \*pt:
        dev poll table (ignored)

.. _`ecryptfs_miscdev_poll.description`:

Description
-----------

Returns the poll mask

.. _`ecryptfs_miscdev_open`:

ecryptfs_miscdev_open
=====================

.. c:function:: int ecryptfs_miscdev_open(struct inode *inode, struct file *file)

    :param struct inode \*inode:
        inode of miscdev handle (ignored)

    :param struct file \*file:
        file for miscdev handle

.. _`ecryptfs_miscdev_open.description`:

Description
-----------

Returns zero on success; non-zero otherwise

.. _`ecryptfs_miscdev_release`:

ecryptfs_miscdev_release
========================

.. c:function:: int ecryptfs_miscdev_release(struct inode *inode, struct file *file)

    :param struct inode \*inode:
        inode of fs/ecryptfs/euid handle (ignored)

    :param struct file \*file:
        file for fs/ecryptfs/euid handle

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

    :param char \*data:
        Data to send to daemon; may be NULL

    :param size_t data_size:
        Amount of data to send to daemon

    :param struct ecryptfs_msg_ctx \*msg_ctx:
        Message context, which is used to handle the reply. If
        this is NULL, then we do not expect a reply.

    :param u8 msg_type:
        Type of message

    :param u16 msg_flags:
        Flags for message

    :param struct ecryptfs_daemon \*daemon:
        eCryptfs daemon object

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

    :param struct file \*file:
        miscdevfs handle

    :param char __user \*buf:
        User buffer into which to copy the next message on the daemon queue

    :param size_t count:
        Amount of space available in \ ``buf``\ 

    :param loff_t \*ppos:
        Offset in file (ignored)

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

    :param struct ecryptfs_daemon \*daemon:
        *undescribed*

    :param char \*data:
        Bytes comprising struct ecryptfs_message

    :param size_t data_size:
        sizeof(struct ecryptfs_message) + data len

    :param u32 seq:
        Sequence number for miscdev response packet

.. _`ecryptfs_miscdev_response.description`:

Description
-----------

Returns zero on success; non-zero otherwise

.. _`ecryptfs_miscdev_write`:

ecryptfs_miscdev_write
======================

.. c:function:: ssize_t ecryptfs_miscdev_write(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    handle write to daemon miscdev handle

    :param struct file \*file:
        File for misc dev handle

    :param const char __user \*buf:
        Buffer containing user data

    :param size_t count:
        Amount of data in \ ``buf``\ 

    :param loff_t \*ppos:
        Pointer to offset in file (ignored)

.. _`ecryptfs_miscdev_write.description`:

Description
-----------

Returns the number of bytes read from \ ``buf``\ 

.. _`ecryptfs_init_ecryptfs_miscdev`:

ecryptfs_init_ecryptfs_miscdev
==============================

.. c:function:: int ecryptfs_init_ecryptfs_miscdev( void)

    :param  void:
        no arguments

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

    :param  void:
        no arguments

.. _`ecryptfs_destroy_ecryptfs_miscdev.description`:

Description
-----------

All of the daemons must be exorcised prior to calling this
function.

.. This file was automatic generated / don't edit.


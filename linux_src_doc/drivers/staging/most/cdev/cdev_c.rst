.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/most/cdev/cdev.c

.. _`comp_open`:

comp_open
=========

.. c:function:: int comp_open(struct inode *inode, struct file *filp)

    implements the syscall to open the device

    :param inode:
        inode pointer
    :type inode: struct inode \*

    :param filp:
        file pointer
    :type filp: struct file \*

.. _`comp_open.description`:

Description
-----------

This stores the channel pointer in the private data field of
the file structure and activates the channel within the core.

.. _`comp_close`:

comp_close
==========

.. c:function:: int comp_close(struct inode *inode, struct file *filp)

    implements the syscall to close the device

    :param inode:
        inode pointer
    :type inode: struct inode \*

    :param filp:
        file pointer
    :type filp: struct file \*

.. _`comp_close.description`:

Description
-----------

This stops the channel within the core.

.. _`comp_write`:

comp_write
==========

.. c:function:: ssize_t comp_write(struct file *filp, const char __user *buf, size_t count, loff_t *offset)

    implements the syscall to write to the device

    :param filp:
        file pointer
    :type filp: struct file \*

    :param buf:
        pointer to user buffer
    :type buf: const char __user \*

    :param count:
        number of bytes to write
    :type count: size_t

    :param offset:
        offset from where to start writing
    :type offset: loff_t \*

.. _`comp_read`:

comp_read
=========

.. c:function:: ssize_t comp_read(struct file *filp, char __user *buf, size_t count, loff_t *offset)

    implements the syscall to read from the device

    :param filp:
        file pointer
    :type filp: struct file \*

    :param buf:
        pointer to user buffer
    :type buf: char __user \*

    :param count:
        number of bytes to read
    :type count: size_t

    :param offset:
        offset from where to start reading
    :type offset: loff_t \*

.. _`comp_disconnect_channel`:

comp_disconnect_channel
=======================

.. c:function:: int comp_disconnect_channel(struct most_interface *iface, int channel_id)

    disconnect a channel

    :param iface:
        pointer to interface instance
    :type iface: struct most_interface \*

    :param channel_id:
        channel index
    :type channel_id: int

.. _`comp_disconnect_channel.description`:

Description
-----------

This frees allocated memory and removes the cdev that represents this
channel in user space.

.. _`comp_rx_completion`:

comp_rx_completion
==================

.. c:function:: int comp_rx_completion(struct mbo *mbo)

    completion handler for rx channels

    :param mbo:
        pointer to buffer object that has completed
    :type mbo: struct mbo \*

.. _`comp_rx_completion.description`:

Description
-----------

This searches for the channel linked to this MBO and stores it in the local
fifo buffer.

.. _`comp_tx_completion`:

comp_tx_completion
==================

.. c:function:: int comp_tx_completion(struct most_interface *iface, int channel_id)

    completion handler for tx channels

    :param iface:
        pointer to interface instance
    :type iface: struct most_interface \*

    :param channel_id:
        channel index/ID
    :type channel_id: int

.. _`comp_tx_completion.description`:

Description
-----------

This wakes sleeping processes in the wait-queue.

.. _`comp_probe`:

comp_probe
==========

.. c:function:: int comp_probe(struct most_interface *iface, int channel_id, struct most_channel_config *cfg, char *name)

    probe function of the driver module

    :param iface:
        pointer to interface instance
    :type iface: struct most_interface \*

    :param channel_id:
        channel index/ID
    :type channel_id: int

    :param cfg:
        pointer to actual channel configuration
    :type cfg: struct most_channel_config \*

    :param name:
        name of the device to be created
    :type name: char \*

.. _`comp_probe.description`:

Description
-----------

This allocates achannel object and creates the device node in /dev

Returns 0 on success or error code otherwise.

.. This file was automatic generated / don't edit.


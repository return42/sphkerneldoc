.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/dvb-core/dvb_ca_en50221.c

.. _`findstr`:

findstr
=======

.. c:function:: char *findstr(char *haystack, int hlen, char *needle, int nlen)

    :param haystack:
        Buffer to look in.
    :type haystack: char \*

    :param hlen:
        Number of bytes in haystack.
    :type hlen: int

    :param needle:
        Buffer to find.
    :type needle: char \*

    :param nlen:
        Number of bytes in needle.
    :type nlen: int

.. _`findstr.return`:

Return
------

Pointer into haystack needle was found at, or NULL if not found.

.. _`dvb_ca_en50221_wait_if_status`:

dvb_ca_en50221_wait_if_status
=============================

.. c:function:: int dvb_ca_en50221_wait_if_status(struct dvb_ca_private *ca, int slot, u8 waitfor, int timeout_hz)

    Wait for flags to become set on the STATUS register on a CAM interface, checking for errors and timeout.

    :param ca:
        CA instance.
    :type ca: struct dvb_ca_private \*

    :param slot:
        Slot on interface.
    :type slot: int

    :param waitfor:
        Flags to wait for.
    :type waitfor: u8

    :param timeout_hz:
        Timeout in milliseconds.
    :type timeout_hz: int

.. _`dvb_ca_en50221_wait_if_status.return`:

Return
------

0 on success, nonzero on error.

.. _`dvb_ca_en50221_link_init`:

dvb_ca_en50221_link_init
========================

.. c:function:: int dvb_ca_en50221_link_init(struct dvb_ca_private *ca, int slot)

    Initialise the link layer connection to a CAM.

    :param ca:
        CA instance.
    :type ca: struct dvb_ca_private \*

    :param slot:
        Slot id.
    :type slot: int

.. _`dvb_ca_en50221_link_init.return`:

Return
------

0 on success, nonzero on failure.

.. _`dvb_ca_en50221_read_tuple`:

dvb_ca_en50221_read_tuple
=========================

.. c:function:: int dvb_ca_en50221_read_tuple(struct dvb_ca_private *ca, int slot, int *address, int *tuple_type, int *tuple_length, u8 *tuple)

    Read a tuple from attribute memory.

    :param ca:
        CA instance.
    :type ca: struct dvb_ca_private \*

    :param slot:
        Slot id.
    :type slot: int

    :param address:
        Address to read from. Updated.
    :type address: int \*

    :param tuple_type:
        Tuple id byte. Updated.
    :type tuple_type: int \*

    :param tuple_length:
        Tuple length. Updated.
    :type tuple_length: int \*

    :param tuple:
        Dest buffer for tuple (must be 256 bytes). Updated.
    :type tuple: u8 \*

.. _`dvb_ca_en50221_read_tuple.return`:

Return
------

0 on success, nonzero on error.

.. _`dvb_ca_en50221_parse_attributes`:

dvb_ca_en50221_parse_attributes
===============================

.. c:function:: int dvb_ca_en50221_parse_attributes(struct dvb_ca_private *ca, int slot)

    Parse attribute memory of a CAM module, extracting Config register, and checking it is a DVB CAM module.

    :param ca:
        CA instance.
    :type ca: struct dvb_ca_private \*

    :param slot:
        Slot id.
    :type slot: int

.. _`dvb_ca_en50221_parse_attributes.return`:

Return
------

0 on success, <0 on failure.

.. _`dvb_ca_en50221_set_configoption`:

dvb_ca_en50221_set_configoption
===============================

.. c:function:: int dvb_ca_en50221_set_configoption(struct dvb_ca_private *ca, int slot)

    Set CAM's configoption correctly.

    :param ca:
        CA instance.
    :type ca: struct dvb_ca_private \*

    :param slot:
        Slot containing the CAM.
    :type slot: int

.. _`dvb_ca_en50221_read_data`:

dvb_ca_en50221_read_data
========================

.. c:function:: int dvb_ca_en50221_read_data(struct dvb_ca_private *ca, int slot, u8 *ebuf, int ecount)

    This function talks to an EN50221 CAM control interface. It reads a buffer of data from the CAM. The data can either be stored in a supplied buffer, or automatically be added to the slot's rx_buffer.

    :param ca:
        CA instance.
    :type ca: struct dvb_ca_private \*

    :param slot:
        Slot to read from.
    :type slot: int

    :param ebuf:
        If non-NULL, the data will be written to this buffer. If NULL,
        the data will be added into the buffering system as a normal
        fragment.
    :type ebuf: u8 \*

    :param ecount:
        Size of ebuf. Ignored if ebuf is NULL.
    :type ecount: int

.. _`dvb_ca_en50221_read_data.return`:

Return
------

Number of bytes read, or < 0 on error

.. _`dvb_ca_en50221_write_data`:

dvb_ca_en50221_write_data
=========================

.. c:function:: int dvb_ca_en50221_write_data(struct dvb_ca_private *ca, int slot, u8 *buf, int bytes_write)

    This function talks to an EN50221 CAM control interface. It writes a buffer of data to a CAM.

    :param ca:
        CA instance.
    :type ca: struct dvb_ca_private \*

    :param slot:
        Slot to write to.
    :type slot: int

    :param buf:
        The data in this buffer is treated as a complete link-level packet to
        be written.
    :type buf: u8 \*

    :param bytes_write:
        Size of ebuf.
    :type bytes_write: int

.. _`dvb_ca_en50221_write_data.return`:

Return
------

Number of bytes written, or < 0 on error.

.. _`dvb_ca_en50221_slot_shutdown`:

dvb_ca_en50221_slot_shutdown
============================

.. c:function:: int dvb_ca_en50221_slot_shutdown(struct dvb_ca_private *ca, int slot)

    A CAM has been removed => shut it down.

    :param ca:
        CA instance.
    :type ca: struct dvb_ca_private \*

    :param slot:
        Slot to shut down.
    :type slot: int

.. _`dvb_ca_en50221_camchange_irq`:

dvb_ca_en50221_camchange_irq
============================

.. c:function:: void dvb_ca_en50221_camchange_irq(struct dvb_ca_en50221 *pubca, int slot, int change_type)

    A CAMCHANGE IRQ has occurred.

    :param pubca:
        CA instance.
    :type pubca: struct dvb_ca_en50221 \*

    :param slot:
        Slot concerned.
    :type slot: int

    :param change_type:
        One of the DVB_CA_CAMCHANGE\_\* values.
    :type change_type: int

.. _`dvb_ca_en50221_camready_irq`:

dvb_ca_en50221_camready_irq
===========================

.. c:function:: void dvb_ca_en50221_camready_irq(struct dvb_ca_en50221 *pubca, int slot)

    A CAMREADY IRQ has occurred.

    :param pubca:
        CA instance.
    :type pubca: struct dvb_ca_en50221 \*

    :param slot:
        Slot concerned.
    :type slot: int

.. _`dvb_ca_en50221_frda_irq`:

dvb_ca_en50221_frda_irq
=======================

.. c:function:: void dvb_ca_en50221_frda_irq(struct dvb_ca_en50221 *pubca, int slot)

    An FR or DA IRQ has occurred.

    :param pubca:
        CA instance.
    :type pubca: struct dvb_ca_en50221 \*

    :param slot:
        Slot concerned.
    :type slot: int

.. _`dvb_ca_en50221_thread_wakeup`:

dvb_ca_en50221_thread_wakeup
============================

.. c:function:: void dvb_ca_en50221_thread_wakeup(struct dvb_ca_private *ca)

    :param ca:
        CA instance.
    :type ca: struct dvb_ca_private \*

.. _`dvb_ca_en50221_thread_update_delay`:

dvb_ca_en50221_thread_update_delay
==================================

.. c:function:: void dvb_ca_en50221_thread_update_delay(struct dvb_ca_private *ca)

    :param ca:
        CA instance.
    :type ca: struct dvb_ca_private \*

.. _`dvb_ca_en50221_poll_cam_gone`:

dvb_ca_en50221_poll_cam_gone
============================

.. c:function:: int dvb_ca_en50221_poll_cam_gone(struct dvb_ca_private *ca, int slot)

    :param ca:
        CA instance.
    :type ca: struct dvb_ca_private \*

    :param slot:
        Slot to process.
        return:: 0 .. no change
        1 .. CAM state changed
    :type slot: int

.. _`dvb_ca_en50221_thread_state_machine`:

dvb_ca_en50221_thread_state_machine
===================================

.. c:function:: void dvb_ca_en50221_thread_state_machine(struct dvb_ca_private *ca, int slot)

    :param ca:
        CA instance.
    :type ca: struct dvb_ca_private \*

    :param slot:
        Slot to process.
    :type slot: int

.. _`dvb_ca_en50221_io_do_ioctl`:

dvb_ca_en50221_io_do_ioctl
==========================

.. c:function:: int dvb_ca_en50221_io_do_ioctl(struct file *file, unsigned int cmd, void *parg)

    :param file:
        File concerned.
    :type file: struct file \*

    :param cmd:
        IOCTL command.
    :type cmd: unsigned int

    :param parg:
        Associated argument.
    :type parg: void \*

.. _`dvb_ca_en50221_io_do_ioctl.note`:

NOTE
----

CA_SEND_MSG/CA_GET_MSG ioctls have userspace buffers passed to them.

.. _`dvb_ca_en50221_io_do_ioctl.return`:

Return
------

0 on success, <0 on error.

.. _`dvb_ca_en50221_io_ioctl`:

dvb_ca_en50221_io_ioctl
=======================

.. c:function:: long dvb_ca_en50221_io_ioctl(struct file *file, unsigned int cmd, unsigned long arg)

    :param file:
        File concerned.
    :type file: struct file \*

    :param cmd:
        IOCTL command.
    :type cmd: unsigned int

    :param arg:
        Associated argument.
    :type arg: unsigned long

.. _`dvb_ca_en50221_io_ioctl.return`:

Return
------

0 on success, <0 on error.

.. _`dvb_ca_en50221_io_write`:

dvb_ca_en50221_io_write
=======================

.. c:function:: ssize_t dvb_ca_en50221_io_write(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    :param file:
        File structure.
    :type file: struct file \*

    :param buf:
        Source buffer.
    :type buf: const char __user \*

    :param count:
        Size of source buffer.
    :type count: size_t

    :param ppos:
        Position in file (ignored).
    :type ppos: loff_t \*

.. _`dvb_ca_en50221_io_write.return`:

Return
------

Number of bytes read, or <0 on error.

.. _`dvb_ca_en50221_io_read`:

dvb_ca_en50221_io_read
======================

.. c:function:: ssize_t dvb_ca_en50221_io_read(struct file *file, char __user *buf, size_t count, loff_t *ppos)

    :param file:
        File structure.
    :type file: struct file \*

    :param buf:
        Destination buffer.
    :type buf: char __user \*

    :param count:
        Size of destination buffer.
    :type count: size_t

    :param ppos:
        Position in file (ignored).
    :type ppos: loff_t \*

.. _`dvb_ca_en50221_io_read.return`:

Return
------

Number of bytes read, or <0 on error.

.. _`dvb_ca_en50221_io_open`:

dvb_ca_en50221_io_open
======================

.. c:function:: int dvb_ca_en50221_io_open(struct inode *inode, struct file *file)

    :param inode:
        Inode concerned.
    :type inode: struct inode \*

    :param file:
        File concerned.
    :type file: struct file \*

.. _`dvb_ca_en50221_io_open.return`:

Return
------

0 on success, <0 on failure.

.. _`dvb_ca_en50221_io_release`:

dvb_ca_en50221_io_release
=========================

.. c:function:: int dvb_ca_en50221_io_release(struct inode *inode, struct file *file)

    :param inode:
        Inode concerned.
    :type inode: struct inode \*

    :param file:
        File concerned.
    :type file: struct file \*

.. _`dvb_ca_en50221_io_release.return`:

Return
------

0 on success, <0 on failure.

.. _`dvb_ca_en50221_io_poll`:

dvb_ca_en50221_io_poll
======================

.. c:function:: __poll_t dvb_ca_en50221_io_poll(struct file *file, poll_table *wait)

    :param file:
        File concerned.
    :type file: struct file \*

    :param wait:
        poll wait table.
    :type wait: poll_table \*

.. _`dvb_ca_en50221_io_poll.return`:

Return
------

Standard poll mask.

.. _`dvb_ca_en50221_init`:

dvb_ca_en50221_init
===================

.. c:function:: int dvb_ca_en50221_init(struct dvb_adapter *dvb_adapter, struct dvb_ca_en50221 *pubca, int flags, int slot_count)

    :param dvb_adapter:
        DVB adapter to attach the new CA device to.
    :type dvb_adapter: struct dvb_adapter \*

    :param pubca:
        The dvb_ca instance.
    :type pubca: struct dvb_ca_en50221 \*

    :param flags:
        Flags describing the CA device (DVB_CA_FLAG\_\*).
    :type flags: int

    :param slot_count:
        Number of slots supported.
    :type slot_count: int

.. _`dvb_ca_en50221_init.return`:

Return
------

0 on success, nonzero on failure

.. _`dvb_ca_en50221_release`:

dvb_ca_en50221_release
======================

.. c:function:: void dvb_ca_en50221_release(struct dvb_ca_en50221 *pubca)

    :param pubca:
        The associated dvb_ca instance.
    :type pubca: struct dvb_ca_en50221 \*

.. This file was automatic generated / don't edit.


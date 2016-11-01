.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/dvb-core/dvb_ca_en50221.c

.. _`findstr`:

findstr
=======

.. c:function:: char *findstr(char *haystack, int hlen, char *needle, int nlen)

    :param char \*haystack:
        Buffer to look in.

    :param int hlen:
        Number of bytes in haystack.

    :param char \*needle:
        Buffer to find.

    :param int nlen:
        Number of bytes in needle.
        \ ``return``\  Pointer into haystack needle was found at, or NULL if not found.

.. _`dvb_ca_en50221_check_camstatus`:

dvb_ca_en50221_check_camstatus
==============================

.. c:function:: int dvb_ca_en50221_check_camstatus(struct dvb_ca_private *ca, int slot)

    Check CAM status.

    :param struct dvb_ca_private \*ca:
        *undescribed*

    :param int slot:
        *undescribed*

.. _`dvb_ca_en50221_wait_if_status`:

dvb_ca_en50221_wait_if_status
=============================

.. c:function:: int dvb_ca_en50221_wait_if_status(struct dvb_ca_private *ca, int slot, u8 waitfor, int timeout_hz)

    Wait for flags to become set on the STATUS register on a CAM interface, checking for errors and timeout.

    :param struct dvb_ca_private \*ca:
        CA instance.

    :param int slot:
        Slot on interface.

    :param u8 waitfor:
        Flags to wait for.

    :param int timeout_hz:
        *undescribed*

.. _`dvb_ca_en50221_wait_if_status.description`:

Description
-----------

@return 0 on success, nonzero on error.

.. _`dvb_ca_en50221_link_init`:

dvb_ca_en50221_link_init
========================

.. c:function:: int dvb_ca_en50221_link_init(struct dvb_ca_private *ca, int slot)

    Initialise the link layer connection to a CAM.

    :param struct dvb_ca_private \*ca:
        CA instance.

    :param int slot:
        Slot id.

.. _`dvb_ca_en50221_link_init.description`:

Description
-----------

@return 0 on success, nonzero on failure.

.. _`dvb_ca_en50221_read_tuple`:

dvb_ca_en50221_read_tuple
=========================

.. c:function:: int dvb_ca_en50221_read_tuple(struct dvb_ca_private *ca, int slot, int *address, int *tupleType, int *tupleLength, u8 *tuple)

    Read a tuple from attribute memory.

    :param struct dvb_ca_private \*ca:
        CA instance.

    :param int slot:
        Slot id.

    :param int \*address:
        Address to read from. Updated.

    :param int \*tupleType:
        Tuple id byte. Updated.

    :param int \*tupleLength:
        Tuple length. Updated.

    :param u8 \*tuple:
        Dest buffer for tuple (must be 256 bytes). Updated.

.. _`dvb_ca_en50221_read_tuple.description`:

Description
-----------

@return 0 on success, nonzero on error.

.. _`dvb_ca_en50221_parse_attributes`:

dvb_ca_en50221_parse_attributes
===============================

.. c:function:: int dvb_ca_en50221_parse_attributes(struct dvb_ca_private *ca, int slot)

    Parse attribute memory of a CAM module, extracting Config register, and checking it is a DVB CAM module.

    :param struct dvb_ca_private \*ca:
        CA instance.

    :param int slot:
        Slot id.

.. _`dvb_ca_en50221_parse_attributes.description`:

Description
-----------

@return 0 on success, <0 on failure.

.. _`dvb_ca_en50221_set_configoption`:

dvb_ca_en50221_set_configoption
===============================

.. c:function:: int dvb_ca_en50221_set_configoption(struct dvb_ca_private *ca, int slot)

    Set CAM's configoption correctly.

    :param struct dvb_ca_private \*ca:
        CA instance.

    :param int slot:
        Slot containing the CAM.

.. _`dvb_ca_en50221_read_data`:

dvb_ca_en50221_read_data
========================

.. c:function:: int dvb_ca_en50221_read_data(struct dvb_ca_private *ca, int slot, u8 *ebuf, int ecount)

    This function talks to an EN50221 CAM control interface. It reads a buffer of data from the CAM. The data can either be stored in a supplied buffer, or automatically be added to the slot's rx_buffer.

    :param struct dvb_ca_private \*ca:
        CA instance.

    :param int slot:
        Slot to read from.

    :param u8 \*ebuf:
        If non-NULL, the data will be written to this buffer. If NULL,
        the data will be added into the buffering system as a normal fragment.

    :param int ecount:
        Size of ebuf. Ignored if ebuf is NULL.

.. _`dvb_ca_en50221_read_data.description`:

Description
-----------

@return Number of bytes read, or < 0 on error

.. _`dvb_ca_en50221_write_data`:

dvb_ca_en50221_write_data
=========================

.. c:function:: int dvb_ca_en50221_write_data(struct dvb_ca_private *ca, int slot, u8 *buf, int bytes_write)

    This function talks to an EN50221 CAM control interface. It writes a buffer of data to a CAM.

    :param struct dvb_ca_private \*ca:
        CA instance.

    :param int slot:
        Slot to write to.

    :param u8 \*buf:
        *undescribed*

    :param int bytes_write:
        *undescribed*

.. _`dvb_ca_en50221_write_data.description`:

Description
-----------

@return Number of bytes written, or < 0 on error.

.. _`dvb_ca_en50221_slot_shutdown`:

dvb_ca_en50221_slot_shutdown
============================

.. c:function:: int dvb_ca_en50221_slot_shutdown(struct dvb_ca_private *ca, int slot)

    A CAM has been removed => shut it down.

    :param struct dvb_ca_private \*ca:
        CA instance.

    :param int slot:
        Slot to shut down.

.. _`dvb_ca_en50221_camchange_irq`:

dvb_ca_en50221_camchange_irq
============================

.. c:function:: void dvb_ca_en50221_camchange_irq(struct dvb_ca_en50221 *pubca, int slot, int change_type)

    A CAMCHANGE IRQ has occurred.

    :param struct dvb_ca_en50221 \*pubca:
        *undescribed*

    :param int slot:
        Slot concerned.

    :param int change_type:
        One of the DVB_CA_CAMCHANGE\_\* values.

.. _`dvb_ca_en50221_camready_irq`:

dvb_ca_en50221_camready_irq
===========================

.. c:function:: void dvb_ca_en50221_camready_irq(struct dvb_ca_en50221 *pubca, int slot)

    A CAMREADY IRQ has occurred.

    :param struct dvb_ca_en50221 \*pubca:
        *undescribed*

    :param int slot:
        Slot concerned.

.. _`dvb_ca_en50221_frda_irq`:

dvb_ca_en50221_frda_irq
=======================

.. c:function:: void dvb_ca_en50221_frda_irq(struct dvb_ca_en50221 *pubca, int slot)

    :param struct dvb_ca_en50221 \*pubca:
        *undescribed*

    :param int slot:
        Slot concerned.

.. _`dvb_ca_en50221_thread_wakeup`:

dvb_ca_en50221_thread_wakeup
============================

.. c:function:: void dvb_ca_en50221_thread_wakeup(struct dvb_ca_private *ca)

    :param struct dvb_ca_private \*ca:
        CA instance.

.. _`dvb_ca_en50221_thread_update_delay`:

dvb_ca_en50221_thread_update_delay
==================================

.. c:function:: void dvb_ca_en50221_thread_update_delay(struct dvb_ca_private *ca)

    :param struct dvb_ca_private \*ca:
        CA instance.

.. _`dvb_ca_en50221_thread`:

dvb_ca_en50221_thread
=====================

.. c:function:: int dvb_ca_en50221_thread(void *data)

    :param void \*data:
        *undescribed*

.. _`dvb_ca_en50221_io_do_ioctl`:

dvb_ca_en50221_io_do_ioctl
==========================

.. c:function:: int dvb_ca_en50221_io_do_ioctl(struct file *file, unsigned int cmd, void *parg)

    :param struct file \*file:
        File concerned.

    :param unsigned int cmd:
        IOCTL command.

    :param void \*parg:
        *undescribed*

.. _`dvb_ca_en50221_io_do_ioctl.note`:

NOTE
----

CA_SEND_MSG/CA_GET_MSG ioctls have userspace buffers passed to them.

.. _`dvb_ca_en50221_io_do_ioctl.description`:

Description
-----------

@return 0 on success, <0 on error.

.. _`dvb_ca_en50221_io_ioctl`:

dvb_ca_en50221_io_ioctl
=======================

.. c:function:: long dvb_ca_en50221_io_ioctl(struct file *file, unsigned int cmd, unsigned long arg)

    :param struct file \*file:
        File concerned.

    :param unsigned int cmd:
        IOCTL command.

    :param unsigned long arg:
        Associated argument.

.. _`dvb_ca_en50221_io_ioctl.description`:

Description
-----------

@return 0 on success, <0 on error.

.. _`dvb_ca_en50221_io_write`:

dvb_ca_en50221_io_write
=======================

.. c:function:: ssize_t dvb_ca_en50221_io_write(struct file *file, const char __user *buf, size_t count, loff_t *ppos)

    :param struct file \*file:
        File structure.

    :param const char __user \*buf:
        Source buffer.

    :param size_t count:
        Size of source buffer.

    :param loff_t \*ppos:
        Position in file (ignored).

.. _`dvb_ca_en50221_io_write.description`:

Description
-----------

@return Number of bytes read, or <0 on error.

.. _`dvb_ca_en50221_io_read_condition`:

dvb_ca_en50221_io_read_condition
================================

.. c:function:: int dvb_ca_en50221_io_read_condition(struct dvb_ca_private *ca, int *result, int *_slot)

    :param struct dvb_ca_private \*ca:
        *undescribed*

    :param int \*result:
        *undescribed*

    :param int \*_slot:
        *undescribed*

.. _`dvb_ca_en50221_io_read`:

dvb_ca_en50221_io_read
======================

.. c:function:: ssize_t dvb_ca_en50221_io_read(struct file *file, char __user *buf, size_t count, loff_t *ppos)

    :param struct file \*file:
        File structure.

    :param char __user \*buf:
        Destination buffer.

    :param size_t count:
        Size of destination buffer.

    :param loff_t \*ppos:
        Position in file (ignored).

.. _`dvb_ca_en50221_io_read.description`:

Description
-----------

@return Number of bytes read, or <0 on error.

.. _`dvb_ca_en50221_io_open`:

dvb_ca_en50221_io_open
======================

.. c:function:: int dvb_ca_en50221_io_open(struct inode *inode, struct file *file)

    :param struct inode \*inode:
        Inode concerned.

    :param struct file \*file:
        File concerned.

.. _`dvb_ca_en50221_io_open.description`:

Description
-----------

@return 0 on success, <0 on failure.

.. _`dvb_ca_en50221_io_release`:

dvb_ca_en50221_io_release
=========================

.. c:function:: int dvb_ca_en50221_io_release(struct inode *inode, struct file *file)

    :param struct inode \*inode:
        Inode concerned.

    :param struct file \*file:
        File concerned.

.. _`dvb_ca_en50221_io_release.description`:

Description
-----------

@return 0 on success, <0 on failure.

.. _`dvb_ca_en50221_io_poll`:

dvb_ca_en50221_io_poll
======================

.. c:function:: unsigned int dvb_ca_en50221_io_poll(struct file *file, poll_table *wait)

    :param struct file \*file:
        File concerned.

    :param poll_table \*wait:
        poll wait table.

.. _`dvb_ca_en50221_io_poll.description`:

Description
-----------

@return Standard poll mask.

.. _`dvb_ca_en50221_init`:

dvb_ca_en50221_init
===================

.. c:function:: int dvb_ca_en50221_init(struct dvb_adapter *dvb_adapter, struct dvb_ca_en50221 *pubca, int flags, int slot_count)

    :param struct dvb_adapter \*dvb_adapter:
        DVB adapter to attach the new CA device to.

    :param struct dvb_ca_en50221 \*pubca:
        *undescribed*

    :param int flags:
        Flags describing the CA device (DVB_CA_FLAG\_\*).

    :param int slot_count:
        Number of slots supported.

.. _`dvb_ca_en50221_init.description`:

Description
-----------

@return 0 on success, nonzero on failure

.. _`dvb_ca_en50221_release`:

dvb_ca_en50221_release
======================

.. c:function:: void dvb_ca_en50221_release(struct dvb_ca_en50221 *pubca)

    :param struct dvb_ca_en50221 \*pubca:
        *undescribed*

.. This file was automatic generated / don't edit.


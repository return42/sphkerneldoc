.. -*- coding: utf-8; mode: rst -*-

=========
rio_drv.h
=========


.. _`rio_local_read_config_32`:

rio_local_read_config_32
========================

.. c:function:: int rio_local_read_config_32 (struct rio_mport *port, u32 offset, u32 *data)

    Read 32 bits from local configuration space

    :param struct rio_mport \*port:
        Master port

    :param u32 offset:
        Offset into local configuration space

    :param u32 \*data:
        Pointer to read data into



.. _`rio_local_read_config_32.description`:

Description
-----------

Reads 32 bits of data from the specified offset within the local
device's configuration space.



.. _`rio_local_write_config_32`:

rio_local_write_config_32
=========================

.. c:function:: int rio_local_write_config_32 (struct rio_mport *port, u32 offset, u32 data)

    Write 32 bits to local configuration space

    :param struct rio_mport \*port:
        Master port

    :param u32 offset:
        Offset into local configuration space

    :param u32 data:
        Data to be written



.. _`rio_local_write_config_32.description`:

Description
-----------

Writes 32 bits of data to the specified offset within the local
device's configuration space.



.. _`rio_local_read_config_16`:

rio_local_read_config_16
========================

.. c:function:: int rio_local_read_config_16 (struct rio_mport *port, u32 offset, u16 *data)

    Read 16 bits from local configuration space

    :param struct rio_mport \*port:
        Master port

    :param u32 offset:
        Offset into local configuration space

    :param u16 \*data:
        Pointer to read data into



.. _`rio_local_read_config_16.description`:

Description
-----------

Reads 16 bits of data from the specified offset within the local
device's configuration space.



.. _`rio_local_write_config_16`:

rio_local_write_config_16
=========================

.. c:function:: int rio_local_write_config_16 (struct rio_mport *port, u32 offset, u16 data)

    Write 16 bits to local configuration space

    :param struct rio_mport \*port:
        Master port

    :param u32 offset:
        Offset into local configuration space

    :param u16 data:
        Data to be written



.. _`rio_local_write_config_16.description`:

Description
-----------

Writes 16 bits of data to the specified offset within the local
device's configuration space.



.. _`rio_local_read_config_8`:

rio_local_read_config_8
=======================

.. c:function:: int rio_local_read_config_8 (struct rio_mport *port, u32 offset, u8 *data)

    Read 8 bits from local configuration space

    :param struct rio_mport \*port:
        Master port

    :param u32 offset:
        Offset into local configuration space

    :param u8 \*data:
        Pointer to read data into



.. _`rio_local_read_config_8.description`:

Description
-----------

Reads 8 bits of data from the specified offset within the local
device's configuration space.



.. _`rio_local_write_config_8`:

rio_local_write_config_8
========================

.. c:function:: int rio_local_write_config_8 (struct rio_mport *port, u32 offset, u8 data)

    Write 8 bits to local configuration space

    :param struct rio_mport \*port:
        Master port

    :param u32 offset:
        Offset into local configuration space

    :param u8 data:
        Data to be written



.. _`rio_local_write_config_8.description`:

Description
-----------

Writes 8 bits of data to the specified offset within the local
device's configuration space.



.. _`rio_read_config_32`:

rio_read_config_32
==================

.. c:function:: int rio_read_config_32 (struct rio_dev *rdev, u32 offset, u32 *data)

    Read 32 bits from configuration space

    :param struct rio_dev \*rdev:
        RIO device

    :param u32 offset:
        Offset into device configuration space

    :param u32 \*data:
        Pointer to read data into



.. _`rio_read_config_32.description`:

Description
-----------

Reads 32 bits of data from the specified offset within the
RIO device's configuration space.



.. _`rio_write_config_32`:

rio_write_config_32
===================

.. c:function:: int rio_write_config_32 (struct rio_dev *rdev, u32 offset, u32 data)

    Write 32 bits to configuration space

    :param struct rio_dev \*rdev:
        RIO device

    :param u32 offset:
        Offset into device configuration space

    :param u32 data:
        Data to be written



.. _`rio_write_config_32.description`:

Description
-----------

Writes 32 bits of data to the specified offset within the
RIO device's configuration space.



.. _`rio_read_config_16`:

rio_read_config_16
==================

.. c:function:: int rio_read_config_16 (struct rio_dev *rdev, u32 offset, u16 *data)

    Read 16 bits from configuration space

    :param struct rio_dev \*rdev:
        RIO device

    :param u32 offset:
        Offset into device configuration space

    :param u16 \*data:
        Pointer to read data into



.. _`rio_read_config_16.description`:

Description
-----------

Reads 16 bits of data from the specified offset within the
RIO device's configuration space.



.. _`rio_write_config_16`:

rio_write_config_16
===================

.. c:function:: int rio_write_config_16 (struct rio_dev *rdev, u32 offset, u16 data)

    Write 16 bits to configuration space

    :param struct rio_dev \*rdev:
        RIO device

    :param u32 offset:
        Offset into device configuration space

    :param u16 data:
        Data to be written



.. _`rio_write_config_16.description`:

Description
-----------

Writes 16 bits of data to the specified offset within the
RIO device's configuration space.



.. _`rio_read_config_8`:

rio_read_config_8
=================

.. c:function:: int rio_read_config_8 (struct rio_dev *rdev, u32 offset, u8 *data)

    Read 8 bits from configuration space

    :param struct rio_dev \*rdev:
        RIO device

    :param u32 offset:
        Offset into device configuration space

    :param u8 \*data:
        Pointer to read data into



.. _`rio_read_config_8.description`:

Description
-----------

Reads 8 bits of data from the specified offset within the
RIO device's configuration space.



.. _`rio_write_config_8`:

rio_write_config_8
==================

.. c:function:: int rio_write_config_8 (struct rio_dev *rdev, u32 offset, u8 data)

    Write 8 bits to configuration space

    :param struct rio_dev \*rdev:
        RIO device

    :param u32 offset:
        Offset into device configuration space

    :param u8 data:
        Data to be written



.. _`rio_write_config_8.description`:

Description
-----------

Writes 8 bits of data to the specified offset within the
RIO device's configuration space.



.. _`rio_send_doorbell`:

rio_send_doorbell
=================

.. c:function:: int rio_send_doorbell (struct rio_dev *rdev, u16 data)

    Send a doorbell message to a device

    :param struct rio_dev \*rdev:
        RIO device

    :param u16 data:
        Doorbell message data



.. _`rio_send_doorbell.description`:

Description
-----------

Send a doorbell message to a RIO device. The doorbell message
has a 16-bit info field provided by the ``data`` argument.



.. _`rio_init_mbox_res`:

rio_init_mbox_res
=================

.. c:function:: void rio_init_mbox_res (struct resource *res, int start, int end)

    Initialize a RIO mailbox resource

    :param struct resource \*res:
        resource struct

    :param int start:
        start of mailbox range

    :param int end:
        end of mailbox range



.. _`rio_init_mbox_res.description`:

Description
-----------

This function is used to initialize the fields of a resource
for use as a mailbox resource.  It initializes a range of
mailboxes using the start and end arguments.



.. _`rio_init_dbell_res`:

rio_init_dbell_res
==================

.. c:function:: void rio_init_dbell_res (struct resource *res, u16 start, u16 end)

    Initialize a RIO doorbell resource

    :param struct resource \*res:
        resource struct

    :param u16 start:
        start of doorbell range

    :param u16 end:
        end of doorbell range



.. _`rio_init_dbell_res.description`:

Description
-----------

This function is used to initialize the fields of a resource
for use as a doorbell resource.  It initializes a range of
doorbell messages using the start and end arguments.



.. _`rio_device`:

RIO_DEVICE
==========

.. c:function:: RIO_DEVICE ( dev,  ven)

    macro used to describe a specific RIO device

    :param dev:
        the 16 bit RIO device ID

    :param ven:
        the 16 bit RIO vendor ID



.. _`rio_device.description`:

Description
-----------

This macro is used to create a struct rio_device_id that matches a
specific device.  The assembly vendor and assembly device fields
will be set to ``RIO_ANY_ID``\ .



.. _`rio_add_outb_message`:

rio_add_outb_message
====================

.. c:function:: int rio_add_outb_message (struct rio_mport *mport, struct rio_dev *rdev, int mbox, void *buffer, size_t len)

    Add RIO message to an outbound mailbox queue

    :param struct rio_mport \*mport:
        RIO master port containing the outbound queue

    :param struct rio_dev \*rdev:
        RIO device the message is be sent to

    :param int mbox:
        The outbound mailbox queue

    :param void \*buffer:
        Pointer to the message buffer

    :param size_t len:
        Length of the message buffer



.. _`rio_add_outb_message.description`:

Description
-----------

Adds a RIO message buffer to an outbound mailbox queue for
transmission. Returns 0 on success.



.. _`rio_add_inb_buffer`:

rio_add_inb_buffer
==================

.. c:function:: int rio_add_inb_buffer (struct rio_mport *mport, int mbox, void *buffer)

    Add buffer to an inbound mailbox queue

    :param struct rio_mport \*mport:
        Master port containing the inbound mailbox

    :param int mbox:
        The inbound mailbox number

    :param void \*buffer:
        Pointer to the message buffer



.. _`rio_add_inb_buffer.description`:

Description
-----------

Adds a buffer to an inbound mailbox queue for reception. Returns
0 on success.



.. _`rio_get_inb_message`:

rio_get_inb_message
===================

.. c:function:: void *rio_get_inb_message (struct rio_mport *mport, int mbox)

    Get A RIO message from an inbound mailbox queue

    :param struct rio_mport \*mport:
        Master port containing the inbound mailbox

    :param int mbox:
        The inbound mailbox number



.. _`rio_get_inb_message.description`:

Description
-----------

Get a RIO message from an inbound mailbox queue. Returns 0 on success.



.. _`rio_name`:

rio_name
========

.. c:function:: const char *rio_name (struct rio_dev *rdev)

    Get the unique RIO device identifier

    :param struct rio_dev \*rdev:
        RIO device



.. _`rio_name.description`:

Description
-----------

Get the unique RIO device identifier. Returns the device
identifier string.



.. _`rio_get_drvdata`:

rio_get_drvdata
===============

.. c:function:: void *rio_get_drvdata (struct rio_dev *rdev)

    Get RIO driver specific data

    :param struct rio_dev \*rdev:
        RIO device



.. _`rio_get_drvdata.description`:

Description
-----------

Get RIO driver specific data. Returns a pointer to the
driver specific data.



.. _`rio_set_drvdata`:

rio_set_drvdata
===============

.. c:function:: void rio_set_drvdata (struct rio_dev *rdev, void *data)

    Set RIO driver specific data

    :param struct rio_dev \*rdev:
        RIO device

    :param void \*data:
        Pointer to driver specific data



.. _`rio_set_drvdata.description`:

Description
-----------

Set RIO driver specific data. device struct driver data pointer
is set to the ``data`` argument.


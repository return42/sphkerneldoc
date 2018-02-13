.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/industrialio-buffer.c

.. _`iio_buffer_read_first_n_outer`:

iio_buffer_read_first_n_outer
=============================

.. c:function:: ssize_t iio_buffer_read_first_n_outer(struct file *filp, char __user *buf, size_t n, loff_t *f_ps)

    chrdev read for buffer access

    :param struct file \*filp:
        File structure pointer for the char device

    :param char __user \*buf:
        Destination buffer for iio buffer read

    :param size_t n:
        First n bytes to read

    :param loff_t \*f_ps:
        Long offset provided by the user as a seek position

.. _`iio_buffer_read_first_n_outer.description`:

Description
-----------

This function relies on all buffer implementations having an
iio_buffer as their first element.

.. _`iio_buffer_read_first_n_outer.return`:

Return
------

negative values corresponding to error codes or ret != 0
        for ending the reading activity

.. _`iio_buffer_poll`:

iio_buffer_poll
===============

.. c:function:: __poll_t iio_buffer_poll(struct file *filp, struct poll_table_struct *wait)

    poll the buffer to find out if it has data

    :param struct file \*filp:
        File structure pointer for device access

    :param struct poll_table_struct \*wait:
        Poll table structure pointer for which the driver adds
        a wait queue

.. _`iio_buffer_poll.return`:

Return
------

(EPOLLIN | EPOLLRDNORM) if data is available for reading
        or 0 for other cases

.. _`iio_buffer_wakeup_poll`:

iio_buffer_wakeup_poll
======================

.. c:function:: void iio_buffer_wakeup_poll(struct iio_dev *indio_dev)

    Wakes up the buffer waitqueue

    :param struct iio_dev \*indio_dev:
        The IIO device

.. _`iio_buffer_wakeup_poll.description`:

Description
-----------

Wakes up the event waitqueue used for \ :c:func:`poll`\ . Should usually
be called when the device is unregistered.

.. _`iio_buffer_set_attrs`:

iio_buffer_set_attrs
====================

.. c:function:: void iio_buffer_set_attrs(struct iio_buffer *buffer, const struct attribute **attrs)

    Set buffer specific attributes

    :param struct iio_buffer \*buffer:
        The buffer for which we are setting attributes

    :param const struct attribute \*\*attrs:
        Pointer to a null terminated list of pointers to attributes

.. _`iio_scan_mask_set`:

iio_scan_mask_set
=================

.. c:function:: int iio_scan_mask_set(struct iio_dev *indio_dev, struct iio_buffer *buffer, int bit)

    set particular bit in the scan mask

    :param struct iio_dev \*indio_dev:
        the iio device

    :param struct iio_buffer \*buffer:
        the buffer whose scan mask we are interested in

    :param int bit:
        the bit to be set.

.. _`iio_scan_mask_set.description`:

Description
-----------

Note that at this point we have no way of knowing what other
buffers might request, hence this code only verifies that the
individual buffers request is plausible.

.. _`iio_demux_table`:

struct iio_demux_table
======================

.. c:type:: struct iio_demux_table

    table describing demux memcpy ops

.. _`iio_demux_table.definition`:

Definition
----------

.. code-block:: c

    struct iio_demux_table {
        unsigned from;
        unsigned to;
        unsigned length;
        struct list_head l;
    }

.. _`iio_demux_table.members`:

Members
-------

from
    index to copy from

to
    index to copy to

length
    how many bytes to copy

l
    list head used for management

.. _`iio_validate_scan_mask_onehot`:

iio_validate_scan_mask_onehot
=============================

.. c:function:: bool iio_validate_scan_mask_onehot(struct iio_dev *indio_dev, const unsigned long *mask)

    Validates that exactly one channel is selected

    :param struct iio_dev \*indio_dev:
        the iio device

    :param const unsigned long \*mask:
        scan mask to be checked

.. _`iio_validate_scan_mask_onehot.description`:

Description
-----------

Return true if exactly one bit is set in the scan mask, false otherwise. It
can be used for devices where only one channel can be active for sampling at
a time.

.. _`iio_push_to_buffers`:

iio_push_to_buffers
===================

.. c:function:: int iio_push_to_buffers(struct iio_dev *indio_dev, const void *data)

    push to a registered buffer.

    :param struct iio_dev \*indio_dev:
        iio_dev structure for device.

    :param const void \*data:
        Full scan.

.. _`iio_buffer_release`:

iio_buffer_release
==================

.. c:function:: void iio_buffer_release(struct kref *ref)

    Free a buffer's resources

    :param struct kref \*ref:
        Pointer to the kref embedded in the iio_buffer struct

.. _`iio_buffer_release.description`:

Description
-----------

This function is called when the last reference to the buffer has been
dropped. It will typically free all resources allocated by the buffer. Do not
call this function manually, always use \ :c:func:`iio_buffer_put`\  when done using a
buffer.

.. _`iio_buffer_get`:

iio_buffer_get
==============

.. c:function:: struct iio_buffer *iio_buffer_get(struct iio_buffer *buffer)

    Grab a reference to the buffer

    :param struct iio_buffer \*buffer:
        The buffer to grab a reference for, may be NULL

.. _`iio_buffer_get.description`:

Description
-----------

Returns the pointer to the buffer that was passed into the function.

.. _`iio_buffer_put`:

iio_buffer_put
==============

.. c:function:: void iio_buffer_put(struct iio_buffer *buffer)

    Release the reference to the buffer

    :param struct iio_buffer \*buffer:
        The buffer to release the reference for, may be NULL

.. _`iio_device_attach_buffer`:

iio_device_attach_buffer
========================

.. c:function:: void iio_device_attach_buffer(struct iio_dev *indio_dev, struct iio_buffer *buffer)

    Attach a buffer to a IIO device

    :param struct iio_dev \*indio_dev:
        The device the buffer should be attached to

    :param struct iio_buffer \*buffer:
        The buffer to attach to the device

.. _`iio_device_attach_buffer.description`:

Description
-----------

This function attaches a buffer to a IIO device. The buffer stays attached to
the device until the device is freed. The function should only be called at
most once per device.

.. This file was automatic generated / don't edit.


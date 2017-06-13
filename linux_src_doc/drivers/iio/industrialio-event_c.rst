.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/industrialio-event.c

.. _`iio_event_interface`:

struct iio_event_interface
==========================

.. c:type:: struct iio_event_interface

    chrdev interface for an event line

.. _`iio_event_interface.definition`:

Definition
----------

.. code-block:: c

    struct iio_event_interface {
        wait_queue_head_t wait;
        DECLARE_KFIFO(det_events# struct iio_event_data# 16;
        struct list_head dev_attr_list;
        unsigned long flags;
        struct attribute_group group;
        struct mutex read_lock;
    }

.. _`iio_event_interface.members`:

Members
-------

wait
    wait queue to allow blocking reads of events

16
    *undescribed*

dev_attr_list
    list of event interface sysfs attribute

flags
    file operations related flags including busy flag.

group
    event interface sysfs attribute group

read_lock
    lock to protect kfifo read operations

.. _`iio_push_event`:

iio_push_event
==============

.. c:function:: int iio_push_event(struct iio_dev *indio_dev, u64 ev_code, s64 timestamp)

    try to add event to the list for userspace reading

    :param struct iio_dev \*indio_dev:
        IIO device structure

    :param u64 ev_code:
        What event

    :param s64 timestamp:
        When the event occurred

.. _`iio_push_event.note`:

Note
----

The caller must make sure that this function is not running
concurrently for the same indio_dev more than once.

This function may be safely used as soon as a valid reference to iio_dev has
been obtained via \ :c:func:`iio_device_alloc`\ , but any events that are submitted
before \ :c:func:`iio_device_register`\  has successfully completed will be silently
discarded.

.. _`iio_event_poll`:

iio_event_poll
==============

.. c:function:: unsigned int iio_event_poll(struct file *filep, struct poll_table_struct *wait)

    poll the event queue to find out if it has data

    :param struct file \*filep:
        File structure pointer to identify the device

    :param struct poll_table_struct \*wait:
        Poll table pointer to add the wait queue on

.. _`iio_event_poll.return`:

Return
------

(POLLIN \| POLLRDNORM) if data is available for reading
or a negative error code on failure

.. _`iio_device_wakeup_eventset`:

iio_device_wakeup_eventset
==========================

.. c:function:: void iio_device_wakeup_eventset(struct iio_dev *indio_dev)

    Wakes up the event waitqueue

    :param struct iio_dev \*indio_dev:
        The IIO device

.. _`iio_device_wakeup_eventset.description`:

Description
-----------

Wakes up the event waitqueue used for \ :c:func:`poll`\  and blocking \ :c:func:`read`\ .
Should usually be called when the device is unregistered.

.. This file was automatic generated / don't edit.


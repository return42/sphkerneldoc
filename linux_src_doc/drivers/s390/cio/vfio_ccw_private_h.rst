.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/cio/vfio_ccw_private.h

.. _`vfio_ccw_private`:

struct vfio_ccw_private
=======================

.. c:type:: struct vfio_ccw_private


.. _`vfio_ccw_private.definition`:

Definition
----------

.. code-block:: c

    struct vfio_ccw_private {
        struct subchannel *sch;
        int state;
        struct completion *completion;
        atomic_t avail;
        struct mdev_device *mdev;
        struct notifier_block nb;
        struct ccw_io_region *io_region;
        struct channel_program cp;
        struct irb irb;
        union scsw scsw;
        struct eventfd_ctx *io_trigger;
        struct work_struct io_work;
    }

.. _`vfio_ccw_private.members`:

Members
-------

sch
    pointer to the subchannel

state
    internal state of the device

completion
    synchronization helper of the I/O completion

avail
    available for creating a mediated device

mdev
    pointer to the mediated device

nb
    notifier for vfio events

io_region
    MMIO region to input/output I/O arguments/results

cp
    channel program for the current I/O operation

irb
    irb info received from interrupt

scsw
    scsw info

io_trigger
    eventfd ctx for signaling userspace I/O results

io_work
    work for deferral process of I/O handling

.. This file was automatic generated / don't edit.


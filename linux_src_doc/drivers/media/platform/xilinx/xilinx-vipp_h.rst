.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/xilinx/xilinx-vipp.h

.. _`xvip_composite_device`:

struct xvip_composite_device
============================

.. c:type:: struct xvip_composite_device

    Xilinx Video IP device structure

.. _`xvip_composite_device.definition`:

Definition
----------

.. code-block:: c

    struct xvip_composite_device {
        struct v4l2_device v4l2_dev;
        struct media_device media_dev;
        struct device *dev;
        struct v4l2_async_notifier notifier;
        struct list_head dmas;
        u32 v4l2_caps;
    }

.. _`xvip_composite_device.members`:

Members
-------

v4l2_dev
    V4L2 device

media_dev
    media device

dev
    (OF) device

notifier
    V4L2 asynchronous subdevs notifier

dmas
    list of DMA channels at the pipeline output and input

v4l2_caps
    V4L2 capabilities of the whole device (see VIDIOC_QUERYCAP)

.. This file was automatic generated / don't edit.


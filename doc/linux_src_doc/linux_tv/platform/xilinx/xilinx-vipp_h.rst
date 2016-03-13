.. -*- coding: utf-8; mode: rst -*-

=============
xilinx-vipp.h
=============



.. _xref_struct_xvip_composite_device:

struct xvip_composite_device
============================

.. c:type:: struct xvip_composite_device

    Xilinx Video IP device structure



Definition
----------

.. code-block:: c

  struct xvip_composite_device {
    struct v4l2_device v4l2_dev;
    struct media_device media_dev;
    struct device * dev;
    struct v4l2_async_notifier notifier;
    struct list_head entities;
    unsigned int num_subdevs;
    struct list_head dmas;
    u32 v4l2_caps;
  };



Members
-------

:``struct v4l2_device v4l2_dev``:
    V4L2 device

:``struct media_device media_dev``:
    media device

:``struct device * dev``:
    (OF) device

:``struct v4l2_async_notifier notifier``:
    V4L2 asynchronous subdevs notifier

:``struct list_head entities``:
    entities in the graph as a list of xvip_graph_entity

:``unsigned int num_subdevs``:
    number of subdevs in the pipeline

:``struct list_head dmas``:
    list of DMA channels at the pipeline output and input

:``u32 v4l2_caps``:
    V4L2 capabilities of the whole device (see VIDIOC_QUERYCAP)




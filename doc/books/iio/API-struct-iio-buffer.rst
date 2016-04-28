.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-iio-buffer:

=================
struct iio_buffer
=================

*man struct iio_buffer(9)*

*4.6.0-rc5*

general buffer structure


Synopsis
========

.. code-block:: c

    struct iio_buffer {
      int length;
      int bytes_per_datum;
      struct attribute_group * scan_el_attrs;
      long * scan_mask;
      bool scan_timestamp;
      const struct iio_buffer_access_funcs * access;
      struct list_head scan_el_dev_attr_list;
      struct attribute_group scan_el_group;
      wait_queue_head_t pollq;
      bool stufftoread;
      struct list_head demux_list;
      void * demux_bounce;
      struct list_head buffer_list;
      struct kref ref;
      unsigned int watermark;
    };


Members
=======

length
    [DEVICE] number of datums in buffer

bytes_per_datum
    [DEVICE] size of individual datum including timestamp

scan_el_attrs
    [DRIVER] control of scan elements if that scan mode control method
    is used

scan_mask
    [INTERN] bitmask used in masking scan mode elements

scan_timestamp
    [INTERN] does the scan mode include a timestamp

access
    [DRIVER] buffer access functions associated with the implementation.

scan_el_dev_attr_list
    [INTERN] list of scan element related attributes.

scan_el_group
    [DRIVER] attribute group for those attributes not created from the
    iio_chan_info array.

pollq
    [INTERN] wait queue to allow for polling on the buffer.

stufftoread
    [INTERN] flag to indicate new data.

demux_list
    [INTERN] list of operations required to demux the scan.

demux_bounce
    [INTERN] buffer for doing gather from incoming scan.

buffer_list
    [INTERN] entry in the devices list of current buffers.

ref
    [INTERN] reference count of the buffer.

watermark
    [INTERN] number of datums to wait for poll/read.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

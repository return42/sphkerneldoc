.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-vb2-buffer-state:

=====================
enum vb2_buffer_state
=====================

*man enum vb2_buffer_state(9)*

*4.6.0-rc5*

current video buffer state


Synopsis
========

.. code-block:: c

    enum vb2_buffer_state {
      VB2_BUF_STATE_DEQUEUED,
      VB2_BUF_STATE_PREPARING,
      VB2_BUF_STATE_PREPARED,
      VB2_BUF_STATE_QUEUED,
      VB2_BUF_STATE_REQUEUEING,
      VB2_BUF_STATE_ACTIVE,
      VB2_BUF_STATE_DONE,
      VB2_BUF_STATE_ERROR
    };


Constants
=========

VB2_BUF_STATE_DEQUEUED
    buffer under userspace control

VB2_BUF_STATE_PREPARING
    buffer is being prepared in videobuf

VB2_BUF_STATE_PREPARED
    buffer prepared in videobuf and by the driver

VB2_BUF_STATE_QUEUED
    buffer queued in videobuf, but not in driver

VB2_BUF_STATE_REQUEUEING
    re-queue a buffer to the driver

VB2_BUF_STATE_ACTIVE
    buffer queued in driver and possibly used in a hardware operation

VB2_BUF_STATE_DONE
    buffer returned from driver to videobuf, but not yet dequeued to
    userspace

VB2_BUF_STATE_ERROR
    same as above, but the operation on the buffer has ended with an
    error, which will be reported to the userspace when it is dequeued


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

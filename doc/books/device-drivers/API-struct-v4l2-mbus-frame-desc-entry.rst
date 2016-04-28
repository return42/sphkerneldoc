.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-v4l2-mbus-frame-desc-entry:

=================================
struct v4l2_mbus_frame_desc_entry
=================================

*man struct v4l2_mbus_frame_desc_entry(9)*

*4.6.0-rc5*

media bus frame description structure


Synopsis
========

.. code-block:: c

    struct v4l2_mbus_frame_desc_entry {
      u16 flags;
      u32 pixelcode;
      u32 length;
    };


Members
=======

flags
    V4L2_MBUS_FRAME_DESC_FL_* flags

pixelcode
    media bus pixel code, valid if FRAME_DESC_FL_BLOB is not set

length
    number of octets per frame, valid if
    V4L2_MBUS_FRAME_DESC_FL_BLOB is set


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-v4l2-mbus-frame-desc:

===========================
struct v4l2_mbus_frame_desc
===========================

*man struct v4l2_mbus_frame_desc(9)*

*4.6.0-rc5*

media bus data frame description


Synopsis
========

.. code-block:: c

    struct v4l2_mbus_frame_desc {
      struct v4l2_mbus_frame_desc_entry entry[V4L2_FRAME_DESC_ENTRY_MAX];
      unsigned short num_entries;
    };


Members
=======

entry[V4L2_FRAME_DESC_ENTRY_MAX]
    frame descriptors array

num_entries
    number of entries in ``entry`` array


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

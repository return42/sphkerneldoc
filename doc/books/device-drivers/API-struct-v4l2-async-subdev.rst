
.. _API-struct-v4l2-async-subdev:

========================
struct v4l2_async_subdev
========================

*man struct v4l2_async_subdev(9)*

*4.6.0-rc1*

sub-device descriptor, as known to a bridge


Synopsis
========

.. code-block:: c

    struct v4l2_async_subdev {
      enum v4l2_async_match_type match_type;
      union match;
      struct list_head list;
    };


Members
=======

match_type
    type of match that will be used

match
    union of per-bus type matching data sets

list
    used to link struct v4l2_async_subdev objects, waiting to be probed, to a notifier->waiting list

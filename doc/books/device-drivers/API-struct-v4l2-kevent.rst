.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-v4l2-kevent:

==================
struct v4l2_kevent
==================

*man struct v4l2_kevent(9)*

*4.6.0-rc5*

Internal kernel event struct.


Synopsis
========

.. code-block:: c

    struct v4l2_kevent {
      struct list_head list;
      struct v4l2_subscribed_event * sev;
      struct v4l2_event event;
    };


Members
=======

list
    List node for the v4l2_fh->available list.

sev
    Pointer to parent v4l2_subscribed_event.

event
    The event itself.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

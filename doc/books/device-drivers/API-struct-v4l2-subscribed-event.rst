.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-v4l2-subscribed-event:

============================
struct v4l2_subscribed_event
============================

*man struct v4l2_subscribed_event(9)*

*4.6.0-rc5*

Internal struct representing a subscribed event.


Synopsis
========

.. code-block:: c

    struct v4l2_subscribed_event {
      struct list_head list;
      u32 type;
      u32 id;
      u32 flags;
      struct v4l2_fh * fh;
      struct list_head node;
      const struct v4l2_subscribed_event_ops * ops;
      unsigned elems;
      unsigned first;
      unsigned in_use;
      struct v4l2_kevent events[];
    };


Members
=======

list
    List node for the v4l2_fh->subscribed list.

type
    Event type.

id
    Associated object ID (e.g. control ID). 0 if there isn't any.

flags
    Copy of v4l2_event_subscription->flags.

fh
    Filehandle that subscribed to this event.

node
    List node that hooks into the object's event list (if there is one).

ops
    v4l2_subscribed_event_ops

elems
    The number of elements in the events array.

first
    The index of the events containing the oldest available event.

in_use
    The number of queued events.

events[]
    An array of ``elems`` events.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

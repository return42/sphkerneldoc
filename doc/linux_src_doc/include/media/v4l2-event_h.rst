.. -*- coding: utf-8; mode: rst -*-

============
v4l2-event.h
============

.. _`v4l2_kevent`:

struct v4l2_kevent
==================

.. c:type:: struct v4l2_kevent

    Internal kernel event struct.



Definition
----------

.. code-block:: c

  struct v4l2_kevent {
    struct list_head list;
    struct v4l2_subscribed_event * sev;
    struct v4l2_event event;
  };



Members
-------

:``list``:
    List node for the v4l2_fh->available list.

:``sev``:
    Pointer to parent v4l2_subscribed_event.

:``event``:
    The event itself.



.. _`v4l2_subscribed_event`:

struct v4l2_subscribed_event
============================

.. c:type:: struct v4l2_subscribed_event

    Internal struct representing a subscribed event.



Definition
----------

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
-------

:``list``:
    List node for the v4l2_fh->subscribed list.

:``type``:
    Event type.

:``id``:
    Associated object ID (e.g. control ID). 0 if there isn't any.

:``flags``:
    Copy of v4l2_event_subscription->flags.

:``fh``:
    Filehandle that subscribed to this event.

:``node``:
    List node that hooks into the object's event list (if there is one).

:``ops``:
    v4l2_subscribed_event_ops

:``elems``:
    The number of elements in the events array.

:``first``:
    The index of the events containing the oldest available event.

:``in_use``:
    The number of queued events.

:``events[]``:
    An array of ``elems`` events.



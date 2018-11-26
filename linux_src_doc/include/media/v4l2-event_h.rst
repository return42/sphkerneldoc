.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/v4l2-event.h

.. _`v4l2_kevent`:

struct v4l2_kevent
==================

.. c:type:: struct v4l2_kevent

    Internal kernel event struct.

.. _`v4l2_kevent.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_kevent {
        struct list_head list;
        struct v4l2_subscribed_event *sev;
        struct v4l2_event event;
    }

.. _`v4l2_kevent.members`:

Members
-------

list
    List node for the v4l2_fh->available list.

sev
    Pointer to parent v4l2_subscribed_event.

event
    The event itself.

.. _`v4l2_subscribed_event_ops`:

struct v4l2_subscribed_event_ops
================================

.. c:type:: struct v4l2_subscribed_event_ops

    Subscribed event operations.

.. _`v4l2_subscribed_event_ops.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_subscribed_event_ops {
        int (*add)(struct v4l2_subscribed_event *sev, unsigned int elems);
        void (*del)(struct v4l2_subscribed_event *sev);
        void (*replace)(struct v4l2_event *old, const struct v4l2_event *new);
        void (*merge)(const struct v4l2_event *old, struct v4l2_event *new);
    }

.. _`v4l2_subscribed_event_ops.members`:

Members
-------

add
    Optional callback, called when a new listener is added

del
    Optional callback, called when a listener stops listening

replace
    Optional callback that can replace event 'old' with event 'new'.

merge
    Optional callback that can merge event 'old' into event 'new'.

.. _`v4l2_subscribed_event`:

struct v4l2_subscribed_event
============================

.. c:type:: struct v4l2_subscribed_event

    Internal struct representing a subscribed event.

.. _`v4l2_subscribed_event.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_subscribed_event {
        struct list_head list;
        u32 type;
        u32 id;
        u32 flags;
        struct v4l2_fh *fh;
        struct list_head node;
        const struct v4l2_subscribed_event_ops *ops;
        unsigned int elems;
        unsigned int first;
        unsigned int in_use;
        struct v4l2_kevent events[];
    }

.. _`v4l2_subscribed_event.members`:

Members
-------

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
    List node that hooks into the object's event list
    (if there is one).

ops
    v4l2_subscribed_event_ops

elems
    The number of elements in the events array.

first
    The index of the events containing the oldest available event.

in_use
    The number of queued events.

events
    An array of \ ``elems``\  events.

.. _`v4l2_event_dequeue`:

v4l2_event_dequeue
==================

.. c:function:: int v4l2_event_dequeue(struct v4l2_fh *fh, struct v4l2_event *event, int nonblocking)

    Dequeue events from video device.

    :param fh:
        pointer to struct v4l2_fh
    :type fh: struct v4l2_fh \*

    :param event:
        pointer to struct v4l2_event
    :type event: struct v4l2_event \*

    :param nonblocking:
        if not zero, waits for an event to arrive
    :type nonblocking: int

.. _`v4l2_event_queue`:

v4l2_event_queue
================

.. c:function:: void v4l2_event_queue(struct video_device *vdev, const struct v4l2_event *ev)

    Queue events to video device.

    :param vdev:
        pointer to \ :c:type:`struct video_device <video_device>`\ 
    :type vdev: struct video_device \*

    :param ev:
        pointer to \ :c:type:`struct v4l2_event <v4l2_event>`\ 
    :type ev: const struct v4l2_event \*

.. _`v4l2_event_queue.description`:

Description
-----------

The event will be queued for all \ :c:type:`struct v4l2_fh <v4l2_fh>`\  file handlers.

.. note::
   The driver's only responsibility is to fill in the type and the data
   fields.The other fields will be filled in by  V4L2.

.. _`v4l2_event_queue_fh`:

v4l2_event_queue_fh
===================

.. c:function:: void v4l2_event_queue_fh(struct v4l2_fh *fh, const struct v4l2_event *ev)

    Queue events to video device.

    :param fh:
        pointer to \ :c:type:`struct v4l2_fh <v4l2_fh>`\ 
    :type fh: struct v4l2_fh \*

    :param ev:
        pointer to \ :c:type:`struct v4l2_event <v4l2_event>`\ 
    :type ev: const struct v4l2_event \*

.. _`v4l2_event_queue_fh.description`:

Description
-----------


The event will be queued only for the specified \ :c:type:`struct v4l2_fh <v4l2_fh>`\  file handler.

.. note::
   The driver's only responsibility is to fill in the type and the data
   fields.The other fields will be filled in by  V4L2.

.. _`v4l2_event_pending`:

v4l2_event_pending
==================

.. c:function:: int v4l2_event_pending(struct v4l2_fh *fh)

    Check if an event is available

    :param fh:
        pointer to \ :c:type:`struct v4l2_fh <v4l2_fh>`\ 
    :type fh: struct v4l2_fh \*

.. _`v4l2_event_pending.description`:

Description
-----------

Returns the number of pending events.

.. _`v4l2_event_subscribe`:

v4l2_event_subscribe
====================

.. c:function:: int v4l2_event_subscribe(struct v4l2_fh *fh, const struct v4l2_event_subscription *sub, unsigned int elems, const struct v4l2_subscribed_event_ops *ops)

    Subscribes to an event

    :param fh:
        pointer to \ :c:type:`struct v4l2_fh <v4l2_fh>`\ 
    :type fh: struct v4l2_fh \*

    :param sub:
        pointer to \ :c:type:`struct v4l2_event_subscription <v4l2_event_subscription>`\ 
    :type sub: const struct v4l2_event_subscription \*

    :param elems:
        size of the events queue
    :type elems: unsigned int

    :param ops:
        pointer to \ :c:type:`struct v4l2_subscribed_event_ops <v4l2_subscribed_event_ops>`\ 
    :type ops: const struct v4l2_subscribed_event_ops \*

.. _`v4l2_event_subscribe.description`:

Description
-----------

.. note::

   if @elems is zero, the framework will fill in a default value,
   with is currently 1 element.

.. _`v4l2_event_unsubscribe`:

v4l2_event_unsubscribe
======================

.. c:function:: int v4l2_event_unsubscribe(struct v4l2_fh *fh, const struct v4l2_event_subscription *sub)

    Unsubscribes to an event

    :param fh:
        pointer to \ :c:type:`struct v4l2_fh <v4l2_fh>`\ 
    :type fh: struct v4l2_fh \*

    :param sub:
        pointer to \ :c:type:`struct v4l2_event_subscription <v4l2_event_subscription>`\ 
    :type sub: const struct v4l2_event_subscription \*

.. _`v4l2_event_unsubscribe_all`:

v4l2_event_unsubscribe_all
==========================

.. c:function:: void v4l2_event_unsubscribe_all(struct v4l2_fh *fh)

    Unsubscribes to all events

    :param fh:
        pointer to \ :c:type:`struct v4l2_fh <v4l2_fh>`\ 
    :type fh: struct v4l2_fh \*

.. _`v4l2_event_subdev_unsubscribe`:

v4l2_event_subdev_unsubscribe
=============================

.. c:function:: int v4l2_event_subdev_unsubscribe(struct v4l2_subdev *sd, struct v4l2_fh *fh, struct v4l2_event_subscription *sub)

    Subdev variant of \ :c:func:`v4l2_event_unsubscribe`\ 

    :param sd:
        pointer to \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ 
    :type sd: struct v4l2_subdev \*

    :param fh:
        pointer to \ :c:type:`struct v4l2_fh <v4l2_fh>`\ 
    :type fh: struct v4l2_fh \*

    :param sub:
        pointer to \ :c:type:`struct v4l2_event_subscription <v4l2_event_subscription>`\ 
    :type sub: struct v4l2_event_subscription \*

.. _`v4l2_event_subdev_unsubscribe.description`:

Description
-----------

.. note::

     This function should be used for the &struct v4l2_subdev_core_ops
     %unsubscribe_event field.

.. _`v4l2_src_change_event_subscribe`:

v4l2_src_change_event_subscribe
===============================

.. c:function:: int v4l2_src_change_event_subscribe(struct v4l2_fh *fh, const struct v4l2_event_subscription *sub)

    helper function that calls \ :c:func:`v4l2_event_subscribe`\  if the event is \ ``V4L2_EVENT_SOURCE_CHANGE``\ .

    :param fh:
        pointer to struct v4l2_fh
    :type fh: struct v4l2_fh \*

    :param sub:
        pointer to \ :c:type:`struct v4l2_event_subscription <v4l2_event_subscription>`\ 
    :type sub: const struct v4l2_event_subscription \*

.. _`v4l2_src_change_event_subdev_subscribe`:

v4l2_src_change_event_subdev_subscribe
======================================

.. c:function:: int v4l2_src_change_event_subdev_subscribe(struct v4l2_subdev *sd, struct v4l2_fh *fh, struct v4l2_event_subscription *sub)

    Variant of \ :c:func:`v4l2_event_subscribe`\ , meant to subscribe only events of the type \ ``V4L2_EVENT_SOURCE_CHANGE``\ .

    :param sd:
        pointer to \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ 
    :type sd: struct v4l2_subdev \*

    :param fh:
        pointer to \ :c:type:`struct v4l2_fh <v4l2_fh>`\ 
    :type fh: struct v4l2_fh \*

    :param sub:
        pointer to \ :c:type:`struct v4l2_event_subscription <v4l2_event_subscription>`\ 
    :type sub: struct v4l2_event_subscription \*

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma-buf/sw_sync.c

.. _`sync_timeline_create`:

sync_timeline_create
====================

.. c:function:: struct sync_timeline *sync_timeline_create(const char *name)

    creates a sync object

    :param name:
        sync_timeline name
    :type name: const char \*

.. _`sync_timeline_create.description`:

Description
-----------

Creates a new sync_timeline. Returns the sync_timeline object or NULL in
case of error.

.. _`sync_timeline_signal`:

sync_timeline_signal
====================

.. c:function:: void sync_timeline_signal(struct sync_timeline *obj, unsigned int inc)

    signal a status change on a sync_timeline

    :param obj:
        sync_timeline to signal
    :type obj: struct sync_timeline \*

    :param inc:
        num to increment on timeline->value
    :type inc: unsigned int

.. _`sync_timeline_signal.description`:

Description
-----------

A sync implementation should call this any time one of it's fences
has signaled or has an error condition.

.. _`sync_pt_create`:

sync_pt_create
==============

.. c:function:: struct sync_pt *sync_pt_create(struct sync_timeline *obj, unsigned int value)

    creates a sync pt

    :param obj:
        parent sync_timeline
    :type obj: struct sync_timeline \*

    :param value:
        value of the fence
    :type value: unsigned int

.. _`sync_pt_create.description`:

Description
-----------

Creates a new sync_pt (fence) as a child of \ ``parent``\ .  \ ``size``\  bytes will be
allocated allowing for implementation specific data to be kept after
the generic sync_timeline struct. Returns the sync_pt object or
NULL in case of error.

.. This file was automatic generated / don't edit.


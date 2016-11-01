.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma-buf/sw_sync.c

.. _`sync_timeline_create`:

sync_timeline_create
====================

.. c:function:: struct sync_timeline *sync_timeline_create(const char *name)

    creates a sync object

    :param const char \*name:
        sync_timeline name

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

    :param struct sync_timeline \*obj:
        sync_timeline to signal

    :param unsigned int inc:
        num to increment on timeline->value

.. _`sync_timeline_signal.description`:

Description
-----------

A sync implementation should call this any time one of it's fences
has signaled or has an error condition.

.. _`sync_pt_create`:

sync_pt_create
==============

.. c:function:: struct sync_pt *sync_pt_create(struct sync_timeline *obj, int size, unsigned int value)

    creates a sync pt

    :param struct sync_timeline \*obj:
        *undescribed*

    :param int size:
        size to allocate for this pt

    :param unsigned int value:
        *undescribed*

.. _`sync_pt_create.description`:

Description
-----------

Creates a new sync_pt as a child of \ ``parent``\ .  \ ``size``\  bytes will be
allocated allowing for implementation specific data to be kept after
the generic sync_timeline struct. Returns the sync_pt object or
NULL in case of error.

.. This file was automatic generated / don't edit.


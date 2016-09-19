.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/android/sync.h

.. _`sync_timeline_ops`:

struct sync_timeline_ops
========================

.. c:type:: struct sync_timeline_ops

    sync object implementation ops

.. _`sync_timeline_ops.definition`:

Definition
----------

.. code-block:: c

    struct sync_timeline_ops {
        const char *driver_name;
        int (*has_signaled)(struct fence *fence);
        void (*timeline_value_str)(struct sync_timeline *timeline, char *str,int size);
        void (*fence_value_str)(struct fence *fence, char *str, int size);
    }

.. _`sync_timeline_ops.members`:

Members
-------

driver_name
    name of the implementation

has_signaled
    returns:
    1 if pt has signaled
    0 if pt has not signaled
    <0 on error

timeline_value_str
    fill str with the value of the sync_timeline's counter

fence_value_str
    fill str with the value of the fence

.. _`sync_timeline`:

struct sync_timeline
====================

.. c:type:: struct sync_timeline

    sync object

.. _`sync_timeline.definition`:

Definition
----------

.. code-block:: c

    struct sync_timeline {
        struct kref kref;
        const struct sync_timeline_ops *ops;
        char name[32];
        bool destroyed;
        int context;
        int value;
        struct list_head child_list_head;
        spinlock_t child_list_lock;
        struct list_head active_list_head;
        #ifdef CONFIG_DEBUG_FS
        struct list_head sync_timeline_list;
        #endif
    }

.. _`sync_timeline.members`:

Members
-------

kref
    reference count on fence.

ops
    ops that define the implementation of the sync_timeline

name
    name of the sync_timeline. Useful for debugging

destroyed
    set when sync_timeline is destroyed

context
    *undescribed*

value
    *undescribed*

child_list_head
    list of children sync_pts for this sync_timeline

child_list_lock
    lock protecting \ ``child_list_head``\ , destroyed, and
    fence.status

active_list_head
    list of active (unsignaled/errored) sync_pts

sync_timeline_list
    membership in global sync_timeline_list

.. _`sync_timeline_create`:

sync_timeline_create
====================

.. c:function:: struct sync_timeline *sync_timeline_create(const struct sync_timeline_ops *ops, int size, const char *name)

    creates a sync object

    :param const struct sync_timeline_ops \*ops:
        specifies the implementation ops for the object

    :param int size:
        size to allocate for this obj

    :param const char \*name:
        sync_timeline name

.. _`sync_timeline_create.description`:

Description
-----------

Creates a new sync_timeline which will use the implementation specified by
\ ``ops``\ .  \ ``size``\  bytes will be allocated allowing for implementation specific
data to be kept after the generic sync_timeline struct. Returns the
sync_timeline object or NULL in case of error.

.. _`sync_timeline_destroy`:

sync_timeline_destroy
=====================

.. c:function:: void sync_timeline_destroy(struct sync_timeline *obj)

    destroys a sync object

    :param struct sync_timeline \*obj:
        sync_timeline to destroy

.. _`sync_timeline_destroy.description`:

Description
-----------

A sync implementation should call this when the \ ``obj``\  is going away
(i.e. module unload.)  \ ``obj``\  won't actually be freed until all its children
fences are freed.

.. _`sync_timeline_signal`:

sync_timeline_signal
====================

.. c:function:: void sync_timeline_signal(struct sync_timeline *obj)

    signal a status change on a sync_timeline

    :param struct sync_timeline \*obj:
        sync_timeline to signal

.. _`sync_timeline_signal.description`:

Description
-----------

A sync implementation should call this any time one of it's fences
has signaled or has an error condition.

.. _`sync_pt_create`:

sync_pt_create
==============

.. c:function:: struct fence *sync_pt_create(struct sync_timeline *parent, int size)

    creates a sync pt

    :param struct sync_timeline \*parent:
        fence's parent sync_timeline

    :param int size:
        size to allocate for this pt

.. _`sync_pt_create.description`:

Description
-----------

Creates a new fence as a child of \ ``parent``\ .  \ ``size``\  bytes will be
allocated allowing for implementation specific data to be kept after
the generic sync_timeline struct. Returns the fence object or
NULL in case of error.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma-buf/sync_debug.h

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
        char name[32];
        u64 context;
        int value;
        struct list_head child_list_head;
        spinlock_t child_list_lock;
        struct list_head active_list_head;
        struct list_head sync_timeline_list;
    }

.. _`sync_timeline.members`:

Members
-------

kref
    reference count on fence.

name
    name of the sync_timeline. Useful for debugging

context
    *undescribed*

value
    *undescribed*

child_list_head
    list of children sync_pts for this sync_timeline

child_list_lock
    lock protecting \ ``child_list_head``\  and fence.status

active_list_head
    list of active (unsignaled/errored) sync_pts

sync_timeline_list
    membership in global sync_timeline_list

.. _`sync_pt`:

struct sync_pt
==============

.. c:type:: struct sync_pt

    sync_pt object

.. _`sync_pt.definition`:

Definition
----------

.. code-block:: c

    struct sync_pt {
        struct fence base;
        struct list_head child_list;
        struct list_head active_list;
    }

.. _`sync_pt.members`:

Members
-------

base
    base fence object

child_list
    sync timeline child's list

active_list
    sync timeline active child's list

.. This file was automatic generated / don't edit.


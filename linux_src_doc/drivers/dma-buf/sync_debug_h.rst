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
        char name;
        u64 context;
        int value;
        struct rb_root pt_tree;
        struct list_head pt_list;
        spinlock_t lock;
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

pt_tree
    rbtree of active (unsignaled/errored) sync_pts

pt_list
    list of active (unsignaled/errored) sync_pts

lock
    lock protecting \ ``pt_list``\  and \ ``value``\ 

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
        struct dma_fence base;
        struct list_head link;
        struct rb_node node;
    }

.. _`sync_pt.members`:

Members
-------

base
    base fence object

link
    link on the sync timeline's list

node
    node in the sync timeline's tree

.. This file was automatic generated / don't edit.


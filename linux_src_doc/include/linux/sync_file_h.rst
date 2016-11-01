.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/sync_file.h

.. _`sync_file`:

struct sync_file
================

.. c:type:: struct sync_file

    sync file to export to the userspace

.. _`sync_file.definition`:

Definition
----------

.. code-block:: c

    struct sync_file {
        struct file *file;
        struct kref kref;
        char name[32];
    #ifdef CONFIG_DEBUG_FS
        struct list_head sync_file_list;
    #endif
        wait_queue_head_t wq;
        struct fence *fence;
        struct fence_cb cb;
    }

.. _`sync_file.members`:

Members
-------

file
    file representing this fence

kref
    reference count on fence.

name
    name of sync_file.  Useful for debugging

sync_file_list
    membership in global file list

wq
    wait queue for fence signaling

fence
    fence with the fences in the sync_file

cb
    fence callback information

.. This file was automatic generated / don't edit.


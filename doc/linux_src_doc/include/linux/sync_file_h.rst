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
        int num_fences;
        wait_queue_head_t wq;
        atomic_t status;
        struct sync_file_cb cbs[];
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

num_fences
    number of sync_pts in the fence

wq
    wait queue for fence signaling

status
    0: signaled, >0:active, <0: error

cbs
    sync_pts callback information

.. This file was automatic generated / don't edit.


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
        char user_name[32];
    #ifdef CONFIG_DEBUG_FS
        struct list_head sync_file_list;
    #endif
        wait_queue_head_t wq;
        unsigned long flags;
        struct dma_fence *fence;
        struct dma_fence_cb cb;
    }

.. _`sync_file.members`:

Members
-------

file
    file representing this fence

user_name

    Name of the sync file provided by userspace, for merged fences.
    Otherwise generated through driver callbacks (in which case the
    entire array is 0).

sync_file_list
    membership in global file list

wq
    wait queue for fence signaling

flags
    flags for the sync_file

fence
    fence with the fences in the sync_file

cb
    fence callback information

.. _`sync_file.flags`:

flags
-----

POLL_ENABLED: whether userspace is currently \ :c:func:`poll`\ 'ing or not

.. This file was automatic generated / don't edit.


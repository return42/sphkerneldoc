.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_flip_work.h

.. _`flip-utils`:

flip utils
==========

Util to queue up work to run from work-queue context after flip/vblank.
Typically this can be used to defer unref of framebuffer's, cursor
bo's, etc until after vblank.  The APIs are all thread-safe.
Moreover, drm_flip_work_queue_task and drm_flip_work_queue can be called
in atomic context.

.. _`drm_flip_task`:

struct drm_flip_task
====================

.. c:type:: struct drm_flip_task

    flip work task

.. _`drm_flip_task.definition`:

Definition
----------

.. code-block:: c

    struct drm_flip_task {
        struct list_head node;
        void *data;
    }

.. _`drm_flip_task.members`:

Members
-------

node
    list entry element

data
    data to pass to \ :c:type:`drm_flip_work.func <drm_flip_work>`\ 

.. _`drm_flip_work`:

struct drm_flip_work
====================

.. c:type:: struct drm_flip_work

    flip work queue

.. _`drm_flip_work.definition`:

Definition
----------

.. code-block:: c

    struct drm_flip_work {
        const char *name;
        drm_flip_func_t func;
        struct work_struct worker;
        struct list_head queued;
        struct list_head commited;
        spinlock_t lock;
    }

.. _`drm_flip_work.members`:

Members
-------

name
    debug name

func
    callback fxn called for each committed item

worker
    worker which calls \ ``func``\ 

queued
    queued tasks

commited
    commited tasks

lock
    lock to access queued and commited lists

.. This file was automatic generated / don't edit.


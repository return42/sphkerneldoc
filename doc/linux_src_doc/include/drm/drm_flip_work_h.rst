.. -*- coding: utf-8; mode: rst -*-

===============
drm_flip_work.h
===============

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



Definition
----------

.. code-block:: c

  struct drm_flip_task {
    struct list_head node;
    void * data;
  };



Members
-------

:``node``:
    list entry element

:``data``:
    data to pass to work->func



.. _`drm_flip_work`:

struct drm_flip_work
====================

.. c:type:: struct drm_flip_work

    flip work queue



Definition
----------

.. code-block:: c

  struct drm_flip_work {
    const char * name;
    drm_flip_func_t func;
    struct work_struct worker;
    struct list_head queued;
    struct list_head commited;
    spinlock_t lock;
  };



Members
-------

:``name``:
    debug name

:``func``:
    callback fxn called for each committed item

:``worker``:
    worker which calls ``func``

:``queued``:
    queued tasks

:``commited``:
    commited tasks

:``lock``:
    lock to access queued and commited lists




.. _API-struct-drm-flip-work:

====================
struct drm_flip_work
====================

*man struct drm_flip_work(9)*

*4.6.0-rc1*

flip work queue


Synopsis
========

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
=======

name
    debug name

func
    callback fxn called for each committed item

worker
    worker which calls ``func``

queued
    queued tasks

commited
    commited tasks

lock
    lock to access queued and commited lists

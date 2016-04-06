
.. _API-struct-drm-flip-task:

====================
struct drm_flip_task
====================

*man struct drm_flip_task(9)*

*4.6.0-rc1*

flip work task


Synopsis
========

.. code-block:: c

    struct drm_flip_task {
      struct list_head node;
      void * data;
    };


Members
=======

node
    list entry element

data
    data to pass to work->func

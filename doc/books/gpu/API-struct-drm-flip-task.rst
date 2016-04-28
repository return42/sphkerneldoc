.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-drm-flip-task:

====================
struct drm_flip_task
====================

*man struct drm_flip_task(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

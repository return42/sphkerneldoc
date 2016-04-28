.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-vb2-vmarea-handler:

=========================
struct vb2_vmarea_handler
=========================

*man struct vb2_vmarea_handler(9)*

*4.6.0-rc5*

common vma refcount tracking handler


Synopsis
========

.. code-block:: c

    struct vb2_vmarea_handler {
      atomic_t * refcount;
      void (* put) (void *arg);
      void * arg;
    };


Members
=======

refcount
    pointer to refcount entry in the buffer

put
    callback to function that decreases buffer refcount

arg
    argument for ``put`` callback


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

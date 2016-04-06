
.. _API-struct-vb2-vmarea-handler:

=========================
struct vb2_vmarea_handler
=========================

*man struct vb2_vmarea_handler(9)*

*4.6.0-rc1*

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

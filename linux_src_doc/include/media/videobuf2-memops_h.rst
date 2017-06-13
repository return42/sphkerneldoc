.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/videobuf2-memops.h

.. _`vb2_vmarea_handler`:

struct vb2_vmarea_handler
=========================

.. c:type:: struct vb2_vmarea_handler

    common vma refcount tracking handler

.. _`vb2_vmarea_handler.definition`:

Definition
----------

.. code-block:: c

    struct vb2_vmarea_handler {
        refcount_t *refcount;
        void (*put)(void *arg);
        void *arg;
    }

.. _`vb2_vmarea_handler.members`:

Members
-------

refcount
    pointer to refcount entry in the buffer

put
    callback to function that decreases buffer refcount

arg
    argument for \ ``put``\  callback

.. This file was automatic generated / don't edit.


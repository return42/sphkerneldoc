.. -*- coding: utf-8; mode: rst -*-

=============
ttm_bo_util.c
=============


.. _`ttm_buffer_object_transfer`:

ttm_buffer_object_transfer
==========================

.. c:function:: int ttm_buffer_object_transfer (struct ttm_buffer_object *bo, struct ttm_buffer_object **new_obj)

    :param struct ttm_buffer_object \*bo:
        A pointer to a struct ttm_buffer_object.

    :param struct ttm_buffer_object \*\*new_obj:
        A pointer to a pointer to a newly created ttm_buffer_object,
        holding the data of ``bo`` with the old placement.



.. _`ttm_buffer_object_transfer.description`:

Description
-----------

This is a utility function that may be called after an accelerated move
has been scheduled. A new buffer object is created as a placeholder for
the old data while it's being copied. When that buffer object is idle,
it can be destroyed, releasing the space of the old placement.



.. _`ttm_buffer_object_transfer.returns`:

Returns
-------

!0: Failure.


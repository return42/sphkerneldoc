.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/android/binder.c

.. _`binder_validate_object`:

binder_validate_object
======================

.. c:function:: size_t binder_validate_object(struct binder_buffer *buffer, u64 offset)

    checks for a valid metadata object in a buffer.

    :param struct binder_buffer \*buffer:
        binder_buffer that we're parsing.

    :param u64 offset:
        offset in the buffer at which to validate an object.

.. _`binder_validate_object.return`:

Return
------

If there's a valid metadata object at \ ``offset``\  in \ ``buffer``\ , the
size of that object. Otherwise, it returns zero.

.. _`binder_validate_ptr`:

binder_validate_ptr
===================

.. c:function:: struct binder_buffer_object *binder_validate_ptr(struct binder_buffer *b, binder_size_t index, binder_size_t *start, binder_size_t num_valid)

    validates binder_buffer_object in a binder_buffer.

    :param struct binder_buffer \*b:
        binder_buffer containing the object

    :param binder_size_t index:
        index in offset array at which the binder_buffer_object is
        located

    :param binder_size_t \*start:
        points to the start of the offset array

    :param binder_size_t num_valid:
        the number of valid offsets in the offset array

.. _`binder_validate_ptr.return`:

Return
------

If \ ``index``\  is within the valid range of the offset array
described by \ ``start``\  and \ ``num_valid``\ , and if there's a valid
binder_buffer_object at the offset found in index \ ``index``\ 
of the offset array, that object is returned. Otherwise,
\ ``NULL``\  is returned.
Note that the offset found in index \ ``index``\  itself is not
verified; this function assumes that \ ``num_valid``\  elements
from \ ``start``\  were previously verified to have valid offsets.

.. _`binder_validate_fixup`:

binder_validate_fixup
=====================

.. c:function:: bool binder_validate_fixup(struct binder_buffer *b, binder_size_t *objects_start, struct binder_buffer_object *buffer, binder_size_t fixup_offset, struct binder_buffer_object *last_obj, binder_size_t last_min_offset)

    validates pointer/fd fixups happen in order.

    :param struct binder_buffer \*b:
        transaction buffer
        \ ``objects_start``\        start of objects buffer

    :param binder_size_t \*objects_start:
        *undescribed*

    :param struct binder_buffer_object \*buffer:
        binder_buffer_object in which to fix up

    :param binder_size_t fixup_offset:
        *undescribed*

    :param struct binder_buffer_object \*last_obj:
        last binder_buffer_object that we fixed up in

    :param binder_size_t last_min_offset:
        minimum fixup offset in \ ``last_obj``\ 

.. _`binder_validate_fixup.return`:

Return
------

%true if a fixup in buffer \ ``buffer``\  at offset \ ``offset``\  is
allowed.

For safety reasons, we only allow fixups inside a buffer to happen
at increasing offsets; additionally, we only allow fixup on the last
buffer object that was verified, or one of its parents.

.. _`binder_validate_fixup.example-of-what-is-allowed`:

Example of what is allowed
--------------------------


A
B (parent = A, offset = 0)
C (parent = A, offset = 16)
D (parent = C, offset = 0)
E (parent = A, offset = 32) // min_offset is 16 (C.parent_offset)

.. _`binder_validate_fixup.decreasing-offsets-within-the-same-parent`:

Decreasing offsets within the same parent
-----------------------------------------


A
C (parent = A, offset = 16)
B (parent = A, offset = 0) // decreasing offset within A

Referring to a parent that wasn't the last object or any of its parents:
A
B (parent = A, offset = 0)
C (parent = A, offset = 0)
C (parent = A, offset = 16)
D (parent = B, offset = 0) // B is not A or any of A's parents

.. This file was automatic generated / don't edit.


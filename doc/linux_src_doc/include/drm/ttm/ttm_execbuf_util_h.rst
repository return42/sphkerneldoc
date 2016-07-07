.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/ttm/ttm_execbuf_util.h

.. _`ttm_validate_buffer`:

struct ttm_validate_buffer
==========================

.. c:type:: struct ttm_validate_buffer


.. _`ttm_validate_buffer.definition`:

Definition
----------

.. code-block:: c

    struct ttm_validate_buffer {
        struct list_head head;
        struct ttm_buffer_object *bo;
        bool shared;
    }

.. _`ttm_validate_buffer.members`:

Members
-------

head
    list head for thread-private list.

bo
    refcounted buffer object pointer.

shared
    should the fence be added shared?

.. _`ttm_eu_backoff_reservation`:

ttm_eu_backoff_reservation
==========================

.. c:function:: void ttm_eu_backoff_reservation(struct ww_acquire_ctx *ticket, struct list_head *list)

    :param struct ww_acquire_ctx \*ticket:
        ww_acquire_ctx from reserve call

    :param struct list_head \*list:
        thread private list of ttm_validate_buffer structs.

.. _`ttm_eu_backoff_reservation.description`:

Description
-----------

Undoes all buffer validation reservations for bos pointed to by
the list entries.

.. _`ttm_eu_reserve_buffers`:

ttm_eu_reserve_buffers
======================

.. c:function:: int ttm_eu_reserve_buffers(struct ww_acquire_ctx *ticket, struct list_head *list, bool intr, struct list_head *dups)

    :param struct ww_acquire_ctx \*ticket:
        [out] ww_acquire_ctx filled in by call, or NULL if only
        non-blocking reserves should be tried.

    :param struct list_head \*list:
        thread private list of ttm_validate_buffer structs.

    :param bool intr:
        should the wait be interruptible

    :param struct list_head \*dups:
        [out] optional list of duplicates.

.. _`ttm_eu_reserve_buffers.description`:

Description
-----------

Tries to reserve bos pointed to by the list entries for validation.
If the function returns 0, all buffers are marked as "unfenced",
taken off the lru lists and are not synced for write CPU usage.

If the function detects a deadlock due to multiple threads trying to
reserve the same buffers in reverse order, all threads except one will
back off and retry. This function may sleep while waiting for
CPU write reservations to be cleared, and for other threads to
unreserve their buffers.

If intr is set to true, this function may return -ERESTARTSYS if the
calling process receives a signal while waiting. In that case, no
buffers on the list will be reserved upon return.

If dups is non NULL all buffers already reserved by the current thread
(e.g. duplicates) are added to this list, otherwise -EALREADY is returned
on the first already reserved buffer and all buffers from the list are
unreserved again.

Buffers reserved by this function should be unreserved by
a call to either \ :c:func:`ttm_eu_backoff_reservation`\  or
\ :c:func:`ttm_eu_fence_buffer_objects`\  when command submission is complete or
has failed.

.. _`ttm_eu_fence_buffer_objects`:

ttm_eu_fence_buffer_objects
===========================

.. c:function:: void ttm_eu_fence_buffer_objects(struct ww_acquire_ctx *ticket, struct list_head *list, struct fence *fence)

    :param struct ww_acquire_ctx \*ticket:
        ww_acquire_ctx from reserve call

    :param struct list_head \*list:
        thread private list of ttm_validate_buffer structs.

    :param struct fence \*fence:
        The new exclusive fence for the buffers.

.. _`ttm_eu_fence_buffer_objects.description`:

Description
-----------

This function should be called when command submission is complete, and
it will add a new sync object to bos pointed to by entries on \ ``list``\ .
It also unreserves all buffers, putting them on lru lists.

.. This file was automatic generated / don't edit.


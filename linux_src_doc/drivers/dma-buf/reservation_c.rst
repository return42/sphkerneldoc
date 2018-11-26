.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma-buf/reservation.c

.. _`reservation-object-overview`:

Reservation Object Overview
===========================

The reservation object provides a mechanism to manage shared and
exclusive fences associated with a buffer.  A reservation object
can have attached one exclusive fence (normally associated with
write operations) or N shared fences (read operations).  The RCU
mechanism is used to protect read access to fences from locked
write-side updates.

.. _`reservation_object_reserve_shared`:

reservation_object_reserve_shared
=================================

.. c:function:: int reservation_object_reserve_shared(struct reservation_object *obj)

    Reserve space to add a shared fence to a reservation_object.

    :param obj:
        reservation object
    :type obj: struct reservation_object \*

.. _`reservation_object_reserve_shared.description`:

Description
-----------

Should be called before \ :c:func:`reservation_object_add_shared_fence`\ .  Must
be called with obj->lock held.

RETURNS
Zero for success, or -errno

.. _`reservation_object_add_shared_fence`:

reservation_object_add_shared_fence
===================================

.. c:function:: void reservation_object_add_shared_fence(struct reservation_object *obj, struct dma_fence *fence)

    Add a fence to a shared slot

    :param obj:
        the reservation object
    :type obj: struct reservation_object \*

    :param fence:
        the shared fence to add
    :type fence: struct dma_fence \*

.. _`reservation_object_add_shared_fence.description`:

Description
-----------

Add a fence to a shared slot, obj->lock must be held, and
\ :c:func:`reservation_object_reserve_shared`\  has been called.

.. _`reservation_object_add_excl_fence`:

reservation_object_add_excl_fence
=================================

.. c:function:: void reservation_object_add_excl_fence(struct reservation_object *obj, struct dma_fence *fence)

    Add an exclusive fence.

    :param obj:
        the reservation object
    :type obj: struct reservation_object \*

    :param fence:
        the shared fence to add
    :type fence: struct dma_fence \*

.. _`reservation_object_add_excl_fence.description`:

Description
-----------

Add a fence to the exclusive slot.  The obj->lock must be held.

.. _`reservation_object_copy_fences`:

reservation_object_copy_fences
==============================

.. c:function:: int reservation_object_copy_fences(struct reservation_object *dst, struct reservation_object *src)

    Copy all fences from src to dst.

    :param dst:
        the destination reservation object
    :type dst: struct reservation_object \*

    :param src:
        the source reservation object
    :type src: struct reservation_object \*

.. _`reservation_object_copy_fences.description`:

Description
-----------

Copy all fences from src to dst. dst-lock must be held.

.. _`reservation_object_get_fences_rcu`:

reservation_object_get_fences_rcu
=================================

.. c:function:: int reservation_object_get_fences_rcu(struct reservation_object *obj, struct dma_fence **pfence_excl, unsigned *pshared_count, struct dma_fence ***pshared)

    Get an object's shared and exclusive fences without update side lock held

    :param obj:
        the reservation object
    :type obj: struct reservation_object \*

    :param pfence_excl:
        the returned exclusive fence (or NULL)
    :type pfence_excl: struct dma_fence \*\*

    :param pshared_count:
        the number of shared fences returned
    :type pshared_count: unsigned \*

    :param pshared:
        the array of shared fence ptrs returned (array is krealloc'd to
        the required size, and must be freed by caller)
    :type pshared: struct dma_fence \*\*\*

.. _`reservation_object_get_fences_rcu.description`:

Description
-----------

Retrieve all fences from the reservation object. If the pointer for the
exclusive fence is not specified the fence is put into the array of the
shared fences as well. Returns either zero or -ENOMEM.

.. _`reservation_object_wait_timeout_rcu`:

reservation_object_wait_timeout_rcu
===================================

.. c:function:: long reservation_object_wait_timeout_rcu(struct reservation_object *obj, bool wait_all, bool intr, unsigned long timeout)

    Wait on reservation's objects shared and/or exclusive fences.

    :param obj:
        the reservation object
    :type obj: struct reservation_object \*

    :param wait_all:
        if true, wait on all fences, else wait on just exclusive fence
    :type wait_all: bool

    :param intr:
        if true, do interruptible wait
    :type intr: bool

    :param timeout:
        timeout value in jiffies or zero to return immediately
    :type timeout: unsigned long

.. _`reservation_object_wait_timeout_rcu.description`:

Description
-----------

RETURNS
Returns -ERESTARTSYS if interrupted, 0 if the wait timed out, or
greater than zer on success.

.. _`reservation_object_test_signaled_rcu`:

reservation_object_test_signaled_rcu
====================================

.. c:function:: bool reservation_object_test_signaled_rcu(struct reservation_object *obj, bool test_all)

    Test if a reservation object's fences have been signaled.

    :param obj:
        the reservation object
    :type obj: struct reservation_object \*

    :param test_all:
        if true, test all fences, otherwise only test the exclusive
        fence
    :type test_all: bool

.. _`reservation_object_test_signaled_rcu.description`:

Description
-----------

RETURNS
true if all fences signaled, else false

.. This file was automatic generated / don't edit.


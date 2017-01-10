.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma-buf/reservation.c

.. _`reservation_object_reserve_shared`:

reservation_object_reserve_shared
=================================

.. c:function:: int reservation_object_reserve_shared(struct reservation_object *obj)

    Reserve space to add a shared fence to a reservation_object.

    :param struct reservation_object \*obj:
        reservation object

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

    :param struct reservation_object \*obj:
        the reservation object

    :param struct dma_fence \*fence:
        the shared fence to add

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

    :param struct reservation_object \*obj:
        the reservation object

    :param struct dma_fence \*fence:
        the shared fence to add

.. _`reservation_object_add_excl_fence.description`:

Description
-----------

Add a fence to the exclusive slot.  The obj->lock must be held.

.. _`reservation_object_get_fences_rcu`:

reservation_object_get_fences_rcu
=================================

.. c:function:: int reservation_object_get_fences_rcu(struct reservation_object *obj, struct dma_fence **pfence_excl, unsigned *pshared_count, struct dma_fence ***pshared)

    Get an object's shared and exclusive fences without update side lock held

    :param struct reservation_object \*obj:
        the reservation object

    :param struct dma_fence \*\*pfence_excl:
        the returned exclusive fence (or NULL)

    :param unsigned \*pshared_count:
        the number of shared fences returned

    :param struct dma_fence \*\*\*pshared:
        the array of shared fence ptrs returned (array is krealloc'd to
        the required size, and must be freed by caller)

.. _`reservation_object_get_fences_rcu.description`:

Description
-----------

RETURNS
Zero or -errno

.. _`reservation_object_wait_timeout_rcu`:

reservation_object_wait_timeout_rcu
===================================

.. c:function:: long reservation_object_wait_timeout_rcu(struct reservation_object *obj, bool wait_all, bool intr, unsigned long timeout)

    Wait on reservation's objects shared and/or exclusive fences.

    :param struct reservation_object \*obj:
        the reservation object

    :param bool wait_all:
        if true, wait on all fences, else wait on just exclusive fence

    :param bool intr:
        if true, do interruptible wait

    :param unsigned long timeout:
        timeout value in jiffies or zero to return immediately

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

    :param struct reservation_object \*obj:
        the reservation object

    :param bool test_all:
        if true, test all fences, otherwise only test the exclusive
        fence

.. _`reservation_object_test_signaled_rcu.description`:

Description
-----------

RETURNS
true if all fences signaled, else false

.. This file was automatic generated / don't edit.


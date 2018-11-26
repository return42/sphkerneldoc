.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/reservation.h

.. _`reservation_object_list`:

struct reservation_object_list
==============================

.. c:type:: struct reservation_object_list

    a list of shared fences

.. _`reservation_object_list.definition`:

Definition
----------

.. code-block:: c

    struct reservation_object_list {
        struct rcu_head rcu;
        u32 shared_count, shared_max;
        struct dma_fence __rcu *shared[];
    }

.. _`reservation_object_list.members`:

Members
-------

rcu
    for internal use

shared_count
    table of shared fences

shared_max
    for growing shared fence table

shared
    shared fence table

.. _`reservation_object`:

struct reservation_object
=========================

.. c:type:: struct reservation_object

    a reservation object manages fences for a buffer

.. _`reservation_object.definition`:

Definition
----------

.. code-block:: c

    struct reservation_object {
        struct ww_mutex lock;
        seqcount_t seq;
        struct dma_fence __rcu *fence_excl;
        struct reservation_object_list __rcu *fence;
        struct reservation_object_list *staged;
    }

.. _`reservation_object.members`:

Members
-------

lock
    update side lock

seq
    sequence count for managing RCU read-side synchronization

fence_excl
    the exclusive fence, if there is one currently

fence
    list of current shared fences

staged
    staged copy of shared fences for RCU updates

.. _`reservation_object_init`:

reservation_object_init
=======================

.. c:function:: void reservation_object_init(struct reservation_object *obj)

    initialize a reservation object

    :param obj:
        the reservation object
    :type obj: struct reservation_object \*

.. _`reservation_object_fini`:

reservation_object_fini
=======================

.. c:function:: void reservation_object_fini(struct reservation_object *obj)

    destroys a reservation object

    :param obj:
        the reservation object
    :type obj: struct reservation_object \*

.. _`reservation_object_get_list`:

reservation_object_get_list
===========================

.. c:function:: struct reservation_object_list *reservation_object_get_list(struct reservation_object *obj)

    get the reservation object's shared fence list, with update-side lock held

    :param obj:
        the reservation object
    :type obj: struct reservation_object \*

.. _`reservation_object_get_list.description`:

Description
-----------

Returns the shared fence list.  Does NOT take references to
the fence.  The obj->lock must be held.

.. _`reservation_object_lock`:

reservation_object_lock
=======================

.. c:function:: int reservation_object_lock(struct reservation_object *obj, struct ww_acquire_ctx *ctx)

    lock the reservation object

    :param obj:
        the reservation object
    :type obj: struct reservation_object \*

    :param ctx:
        the locking context
    :type ctx: struct ww_acquire_ctx \*

.. _`reservation_object_lock.description`:

Description
-----------

Locks the reservation object for exclusive access and modification. Note,
that the lock is only against other writers, readers will run concurrently
with a writer under RCU. The seqlock is used to notify readers if they
overlap with a writer.

As the reservation object may be locked by multiple parties in an
undefined order, a #ww_acquire_ctx is passed to unwind if a cycle
is detected. See \ :c:func:`ww_mutex_lock`\  and \ :c:func:`ww_acquire_init`\ . A reservation
object may be locked by itself by passing NULL as \ ``ctx``\ .

.. _`reservation_object_lock_interruptible`:

reservation_object_lock_interruptible
=====================================

.. c:function:: int reservation_object_lock_interruptible(struct reservation_object *obj, struct ww_acquire_ctx *ctx)

    lock the reservation object

    :param obj:
        the reservation object
    :type obj: struct reservation_object \*

    :param ctx:
        the locking context
    :type ctx: struct ww_acquire_ctx \*

.. _`reservation_object_lock_interruptible.description`:

Description
-----------

Locks the reservation object interruptible for exclusive access and
modification. Note, that the lock is only against other writers, readers
will run concurrently with a writer under RCU. The seqlock is used to
notify readers if they overlap with a writer.

As the reservation object may be locked by multiple parties in an
undefined order, a #ww_acquire_ctx is passed to unwind if a cycle
is detected. See \ :c:func:`ww_mutex_lock`\  and \ :c:func:`ww_acquire_init`\ . A reservation
object may be locked by itself by passing NULL as \ ``ctx``\ .

.. _`reservation_object_trylock`:

reservation_object_trylock
==========================

.. c:function:: bool reservation_object_trylock(struct reservation_object *obj)

    trylock the reservation object

    :param obj:
        the reservation object
    :type obj: struct reservation_object \*

.. _`reservation_object_trylock.description`:

Description
-----------

Tries to lock the reservation object for exclusive access and modification.
Note, that the lock is only against other writers, readers will run
concurrently with a writer under RCU. The seqlock is used to notify readers
if they overlap with a writer.

Also note that since no context is provided, no deadlock protection is
possible.

Returns true if the lock was acquired, false otherwise.

.. _`reservation_object_unlock`:

reservation_object_unlock
=========================

.. c:function:: void reservation_object_unlock(struct reservation_object *obj)

    unlock the reservation object

    :param obj:
        the reservation object
    :type obj: struct reservation_object \*

.. _`reservation_object_unlock.description`:

Description
-----------

Unlocks the reservation object following exclusive access.

.. _`reservation_object_get_excl`:

reservation_object_get_excl
===========================

.. c:function:: struct dma_fence *reservation_object_get_excl(struct reservation_object *obj)

    get the reservation object's exclusive fence, with update-side lock held

    :param obj:
        the reservation object
    :type obj: struct reservation_object \*

.. _`reservation_object_get_excl.description`:

Description
-----------

Returns the exclusive fence (if any).  Does NOT take a
reference.  The obj->lock must be held.

RETURNS
The exclusive fence or NULL

.. _`reservation_object_get_excl_rcu`:

reservation_object_get_excl_rcu
===============================

.. c:function:: struct dma_fence *reservation_object_get_excl_rcu(struct reservation_object *obj)

    get the reservation object's exclusive fence, without lock held.

    :param obj:
        the reservation object
    :type obj: struct reservation_object \*

.. _`reservation_object_get_excl_rcu.description`:

Description
-----------

If there is an exclusive fence, this atomically increments it's
reference count and returns it.

RETURNS
The exclusive fence or NULL if none

.. This file was automatic generated / don't edit.


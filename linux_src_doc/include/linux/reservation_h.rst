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
        u32 shared_count;
        u32 shared_max;
        struct fence __rcu  *shared[];
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
        struct fence __rcu *fence_excl;
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

    :param struct reservation_object \*obj:
        the reservation object

.. _`reservation_object_fini`:

reservation_object_fini
=======================

.. c:function:: void reservation_object_fini(struct reservation_object *obj)

    destroys a reservation object

    :param struct reservation_object \*obj:
        the reservation object

.. _`reservation_object_get_list`:

reservation_object_get_list
===========================

.. c:function:: struct reservation_object_list *reservation_object_get_list(struct reservation_object *obj)

    get the reservation object's shared fence list, with update-side lock held

    :param struct reservation_object \*obj:
        the reservation object

.. _`reservation_object_get_list.description`:

Description
-----------

Returns the shared fence list.  Does NOT take references to
the fence.  The obj->lock must be held.

.. _`reservation_object_get_excl`:

reservation_object_get_excl
===========================

.. c:function:: struct fence *reservation_object_get_excl(struct reservation_object *obj)

    get the reservation object's exclusive fence, with update-side lock held

    :param struct reservation_object \*obj:
        the reservation object

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

.. c:function:: struct fence *reservation_object_get_excl_rcu(struct reservation_object *obj)

    get the reservation object's exclusive fence, without lock held.

    :param struct reservation_object \*obj:
        the reservation object

.. _`reservation_object_get_excl_rcu.description`:

Description
-----------

If there is an exclusive fence, this atomically increments it's
reference count and returns it.

RETURNS
The exclusive fence or NULL if none

.. This file was automatic generated / don't edit.


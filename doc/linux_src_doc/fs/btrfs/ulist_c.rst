.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/btrfs/ulist.c

.. _`ulist_init`:

ulist_init
==========

.. c:function:: void ulist_init(struct ulist *ulist)

    freshly initialize a ulist

    :param struct ulist \*ulist:
        the ulist to initialize

.. _`ulist_init.note`:

Note
----

don't use this function to init an already used ulist, use
ulist_reinit instead.

.. _`ulist_fini`:

ulist_fini
==========

.. c:function:: void ulist_fini(struct ulist *ulist)

    free up additionally allocated memory for the ulist

    :param struct ulist \*ulist:
        the ulist from which to free the additional memory

.. _`ulist_fini.description`:

Description
-----------

This is useful in cases where the base 'struct ulist' has been statically
allocated.

.. _`ulist_reinit`:

ulist_reinit
============

.. c:function:: void ulist_reinit(struct ulist *ulist)

    prepare a ulist for reuse

    :param struct ulist \*ulist:
        ulist to be reused

.. _`ulist_reinit.description`:

Description
-----------

Free up all additional memory allocated for the list elements and reinit
the ulist.

.. _`ulist_alloc`:

ulist_alloc
===========

.. c:function:: struct ulist *ulist_alloc(gfp_t gfp_mask)

    dynamically allocate a ulist

    :param gfp_t gfp_mask:
        allocation flags to for base allocation

.. _`ulist_alloc.description`:

Description
-----------

The allocated ulist will be returned in an initialized state.

.. _`ulist_free`:

ulist_free
==========

.. c:function:: void ulist_free(struct ulist *ulist)

    free dynamically allocated ulist

    :param struct ulist \*ulist:
        ulist to free

.. _`ulist_free.description`:

Description
-----------

It is not necessary to call ulist_fini before.

.. _`ulist_add`:

ulist_add
=========

.. c:function:: int ulist_add(struct ulist *ulist, u64 val, u64 aux, gfp_t gfp_mask)

    add an element to the ulist

    :param struct ulist \*ulist:
        ulist to add the element to

    :param u64 val:
        value to add to ulist

    :param u64 aux:
        auxiliary value to store along with val

    :param gfp_t gfp_mask:
        flags to use for allocation

.. _`ulist_add.note`:

Note
----

locking must be provided by the caller. In case of rwlocks write
locking is needed

Add an element to a ulist. The \ ``val``\  will only be added if it doesn't
already exist. If it is added, the auxiliary value \ ``aux``\  is stored along with
it. In case \ ``val``\  already exists in the ulist, \ ``aux``\  is ignored, even if
it differs from the already stored value.

ulist_add returns 0 if \ ``val``\  already exists in ulist and 1 if \ ``val``\  has been
inserted.
In case of allocation failure -ENOMEM is returned and the ulist stays
unaltered.

.. _`ulist_next`:

ulist_next
==========

.. c:function:: struct ulist_node *ulist_next(struct ulist *ulist, struct ulist_iterator *uiter)

    iterate ulist

    :param struct ulist \*ulist:
        ulist to iterate

    :param struct ulist_iterator \*uiter:
        iterator variable, initialized with ULIST_ITER_INIT(\ :c:type:`struct iterator <iterator>`)

.. _`ulist_next.note`:

Note
----

locking must be provided by the caller. In case of rwlocks only read
locking is needed

This function is used to iterate an ulist.
It returns the next element from the ulist or \ ``NULL``\  when the
end is reached. No guarantee is made with respect to the order in which
the elements are returned. They might neither be returned in order of
addition nor in ascending order.
It is allowed to call ulist_add during an enumeration. Newly added items
are guaranteed to show up in the running enumeration.

.. This file was automatic generated / don't edit.


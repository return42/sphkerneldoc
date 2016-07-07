.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/idr.c

.. _`idr_layer_alloc`:

idr_layer_alloc
===============

.. c:function:: struct idr_layer *idr_layer_alloc(gfp_t gfp_mask, struct idr *layer_idr)

    allocate a new idr_layer

    :param gfp_t gfp_mask:
        allocation mask

    :param struct idr \*layer_idr:
        optional idr to allocate from

.. _`idr_layer_alloc.description`:

Description
-----------

If \ ``layer_idr``\  is \ ``NULL``\ , directly allocate one using \ ``gfp_mask``\  or fetch
one from the per-cpu preload buffer.  If \ ``layer_idr``\  is not \ ``NULL``\ , fetch
an idr_layer from \ ``idr``\ ->id_free.

\ ``layer_idr``\  is to maintain backward compatibility with the old alloc
interface - \ :c:func:`idr_pre_get`\  and idr_get_new\*() - and will be removed
together with per-pool preload buffer.

.. _`sub_alloc`:

sub_alloc
=========

.. c:function:: int sub_alloc(struct idr *idp, int *starting_id, struct idr_layer **pa, gfp_t gfp_mask, struct idr *layer_idr)

    try to allocate an id without growing the tree depth

    :param struct idr \*idp:
        idr handle

    :param int \*starting_id:
        id to start search at

    :param struct idr_layer \*\*pa:
        idr_layer[MAX_IDR_LEVEL] used as backtrack buffer

    :param gfp_t gfp_mask:
        allocation mask for \ :c:func:`idr_layer_alloc`\ 

    :param struct idr \*layer_idr:
        optional idr passed to \ :c:func:`idr_layer_alloc`\ 

.. _`sub_alloc.description`:

Description
-----------

Allocate an id in range [\ ``starting_id``\ , INT_MAX] from \ ``idp``\  without
growing its depth.  Returns

the allocated id >= 0 if successful,
-EAGAIN if the tree needs to grow for allocation to succeed,
-ENOSPC if the id space is exhausted,
-ENOMEM if more idr_layers need to be allocated.

.. _`idr_preload`:

idr_preload
===========

.. c:function:: void idr_preload(gfp_t gfp_mask)

    preload for \ :c:func:`idr_alloc`\ 

    :param gfp_t gfp_mask:
        allocation mask to use for preloading

.. _`idr_preload.description`:

Description
-----------

Preload per-cpu layer buffer for \ :c:func:`idr_alloc`\ .  Can only be used from
process context and each \ :c:func:`idr_preload`\  invocation should be matched with
\ :c:func:`idr_preload_end`\ .  Note that preemption is disabled while preloaded.

The first \ :c:func:`idr_alloc`\  in the preloaded section can be treated as if it
were invoked with \ ``gfp_mask``\  used for preloading.  This allows using more
permissive allocation masks for idrs protected by spinlocks.

For example, if \ :c:func:`idr_alloc`\  below fails, the failure can be treated as
if \ :c:func:`idr_alloc`\  were called with GFP_KERNEL rather than GFP_NOWAIT.

idr_preload(GFP_KERNEL);
spin_lock(lock);

id = idr_alloc(idr, ptr, start, end, GFP_NOWAIT);

spin_unlock(lock);
\ :c:func:`idr_preload_end`\ ;
if (id < 0)
error;

.. _`idr_alloc`:

idr_alloc
=========

.. c:function:: int idr_alloc(struct idr *idr, void *ptr, int start, int end, gfp_t gfp_mask)

    allocate new idr entry

    :param struct idr \*idr:
        the (initialized) idr

    :param void \*ptr:
        pointer to be associated with the new id

    :param int start:
        the minimum id (inclusive)

    :param int end:
        the maximum id (exclusive, <= 0 for max)

    :param gfp_t gfp_mask:
        memory allocation flags

.. _`idr_alloc.description`:

Description
-----------

Allocate an id in [start, end) and associate it with \ ``ptr``\ .  If no ID is
available in the specified range, returns -ENOSPC.  On memory allocation
failure, returns -ENOMEM.

Note that \ ``end``\  is treated as max when <= 0.  This is to always allow
using \ ``start``\  + N as \ ``end``\  as long as N is inside integer range.

The user is responsible for exclusively synchronizing all operations
which may modify \ ``idr``\ .  However, read-only accesses such as \ :c:func:`idr_find`\ 
or iteration can be performed under RCU read lock provided the user
destroys \ ``ptr``\  in RCU-safe way after removal from idr.

.. _`idr_alloc_cyclic`:

idr_alloc_cyclic
================

.. c:function:: int idr_alloc_cyclic(struct idr *idr, void *ptr, int start, int end, gfp_t gfp_mask)

    allocate new idr entry in a cyclical fashion

    :param struct idr \*idr:
        the (initialized) idr

    :param void \*ptr:
        pointer to be associated with the new id

    :param int start:
        the minimum id (inclusive)

    :param int end:
        the maximum id (exclusive, <= 0 for max)

    :param gfp_t gfp_mask:
        memory allocation flags

.. _`idr_alloc_cyclic.description`:

Description
-----------

Essentially the same as idr_alloc, but prefers to allocate progressively
higher ids if it can. If the "cur" counter wraps, then it will start again
at the "start" end of the range and allocate one that has already been used.

.. _`idr_remove`:

idr_remove
==========

.. c:function:: void idr_remove(struct idr *idp, int id)

    remove the given id and free its slot

    :param struct idr \*idp:
        idr handle

    :param int id:
        unique key

.. _`idr_destroy`:

idr_destroy
===========

.. c:function:: void idr_destroy(struct idr *idp)

    release all cached layers within an idr tree

    :param struct idr \*idp:
        idr handle

.. _`idr_destroy.description`:

Description
-----------

Free all id mappings and all idp_layers.  After this function, \ ``idp``\  is
completely unused and can be freed / recycled.  The caller is
responsible for ensuring that no one else accesses \ ``idp``\  during or after
\ :c:func:`idr_destroy`\ .

A typical clean-up sequence for objects stored in an idr tree will use
\ :c:func:`idr_for_each`\  to free all objects, if necessary, then \ :c:func:`idr_destroy`\  to
free up the id mappings and cached idr_layers.

.. _`idr_for_each`:

idr_for_each
============

.. c:function:: int idr_for_each(struct idr *idp, int (*) fn (int id, void *p, void *data, void *data)

    iterate through all stored pointers

    :param struct idr \*idp:
        idr handle

    :param (int (\*) fn (int id, void \*p, void \*data):
        function to be called for each pointer

    :param void \*data:
        data passed back to callback function

.. _`idr_for_each.description`:

Description
-----------

Iterate over the pointers registered with the given idr.  The
callback function will be called for each pointer currently
registered, passing the id, the pointer and the data pointer passed
to this function.  It is not safe to modify the idr tree while in
the callback, so functions such as idr_get_new and idr_remove are
not allowed.

We check the return of \ ``fn``\  each time. If it returns anything other
than \ ``0``\ , we break out and return that value.

The caller must serialize \ :c:func:`idr_for_each`\  vs \ :c:func:`idr_get_new`\  and \ :c:func:`idr_remove`\ .

.. _`idr_get_next`:

idr_get_next
============

.. c:function:: void *idr_get_next(struct idr *idp, int *nextidp)

    lookup next object of id to given id.

    :param struct idr \*idp:
        idr handle

    :param int \*nextidp:
        pointer to lookup key

.. _`idr_get_next.description`:

Description
-----------

Returns pointer to registered object with id, which is next number to
given id. After being looked up, \*\ ``nextidp``\  will be updated for the next
iteration.

This function can be called under \ :c:func:`rcu_read_lock`\ , given that the leaf
pointers lifetimes are correctly managed.

.. _`idr_replace`:

idr_replace
===========

.. c:function:: void *idr_replace(struct idr *idp, void *ptr, int id)

    replace pointer for given id

    :param struct idr \*idp:
        idr handle

    :param void \*ptr:
        pointer you want associated with the id

    :param int id:
        lookup key

.. _`idr_replace.description`:

Description
-----------

Replace the pointer registered with an id and return the old value.
A \ ``-ENOENT``\  return indicates that \ ``id``\  was not found.
A \ ``-EINVAL``\  return indicates that \ ``id``\  was not within valid constraints.

The caller must serialize with writers.

.. _`idr_init`:

idr_init
========

.. c:function:: void idr_init(struct idr *idp)

    initialize idr handle

    :param struct idr \*idp:
        idr handle

.. _`idr_init.description`:

Description
-----------

This function is use to set up the handle (\ ``idp``\ ) that you will pass
to the rest of the functions.

.. _`ida_pre_get`:

ida_pre_get
===========

.. c:function:: int ida_pre_get(struct ida *ida, gfp_t gfp_mask)

    reserve resources for ida allocation

    :param struct ida \*ida:
        ida handle

    :param gfp_t gfp_mask:
        memory allocation flag

.. _`ida_pre_get.description`:

Description
-----------

This function should be called prior to locking and calling the
following function.  It preallocates enough memory to satisfy the
worst possible allocation.

If the system is REALLY out of memory this function returns \ ``0``\ ,
otherwise \ ``1``\ .

.. _`ida_get_new_above`:

ida_get_new_above
=================

.. c:function:: int ida_get_new_above(struct ida *ida, int starting_id, int *p_id)

    allocate new ID above or equal to a start id

    :param struct ida \*ida:
        ida handle

    :param int starting_id:
        id to start search at

    :param int \*p_id:
        pointer to the allocated handle

.. _`ida_get_new_above.description`:

Description
-----------

Allocate new ID above or equal to \ ``starting_id``\ .  It should be called
with any required locks.

If memory is required, it will return \ ``-EAGAIN``\ , you should unlock
and go back to the \ :c:func:`ida_pre_get`\  call.  If the ida is full, it will
return \ ``-ENOSPC``\ .

\ ``p_id``\  returns a value in the range \ ``starting_id``\  ... \ ``0x7fffffff``\ .

.. _`ida_remove`:

ida_remove
==========

.. c:function:: void ida_remove(struct ida *ida, int id)

    remove the given ID

    :param struct ida \*ida:
        ida handle

    :param int id:
        ID to free

.. _`ida_destroy`:

ida_destroy
===========

.. c:function:: void ida_destroy(struct ida *ida)

    release all cached layers within an ida tree

    :param struct ida \*ida:
        ida handle

.. _`ida_simple_get`:

ida_simple_get
==============

.. c:function:: int ida_simple_get(struct ida *ida, unsigned int start, unsigned int end, gfp_t gfp_mask)

    get a new id.

    :param struct ida \*ida:
        the (initialized) ida.

    :param unsigned int start:
        the minimum id (inclusive, < 0x8000000)

    :param unsigned int end:
        the maximum id (exclusive, < 0x8000000 or 0)

    :param gfp_t gfp_mask:
        memory allocation flags

.. _`ida_simple_get.description`:

Description
-----------

Allocates an id in the range start <= id < end, or returns -ENOSPC.
On memory allocation failure, returns -ENOMEM.

Use \ :c:func:`ida_simple_remove`\  to get rid of an id.

.. _`ida_simple_remove`:

ida_simple_remove
=================

.. c:function:: void ida_simple_remove(struct ida *ida, unsigned int id)

    remove an allocated id.

    :param struct ida \*ida:
        the (initialized) ida.

    :param unsigned int id:
        the id returned by ida_simple_get.

.. _`ida_init`:

ida_init
========

.. c:function:: void ida_init(struct ida *ida)

    initialize ida handle

    :param struct ida \*ida:
        ida handle

.. _`ida_init.description`:

Description
-----------

This function is use to set up the handle (\ ``ida``\ ) that you will pass
to the rest of the functions.

.. This file was automatic generated / don't edit.


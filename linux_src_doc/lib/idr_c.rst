.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/idr.c

.. _`idr_alloc_u32`:

idr_alloc_u32
=============

.. c:function:: int idr_alloc_u32(struct idr *idr, void *ptr, u32 *nextid, unsigned long max, gfp_t gfp)

    Allocate an ID.

    :param struct idr \*idr:
        IDR handle.

    :param void \*ptr:
        Pointer to be associated with the new ID.

    :param u32 \*nextid:
        Pointer to an ID.

    :param unsigned long max:
        The maximum ID to allocate (inclusive).

    :param gfp_t gfp:
        Memory allocation flags.

.. _`idr_alloc_u32.description`:

Description
-----------

Allocates an unused ID in the range specified by \ ``nextid``\  and \ ``max``\ .
Note that \ ``max``\  is inclusive whereas the \ ``end``\  parameter to \ :c:func:`idr_alloc`\ 
is exclusive.  The new ID is assigned to \ ``nextid``\  before the pointer
is inserted into the IDR, so if \ ``nextid``\  points into the object pointed
to by \ ``ptr``\ , a concurrent lookup will not find an uninitialised ID.

The caller should provide their own locking to ensure that two
concurrent modifications to the IDR are not possible.  Read-only
accesses to the IDR may be done under the RCU read lock or may
exclude simultaneous writers.

.. _`idr_alloc_u32.return`:

Return
------

0 if an ID was allocated, -ENOMEM if memory allocation failed,
or -ENOSPC if no free IDs could be found.  If an error occurred,
\ ``nextid``\  is unchanged.

.. _`idr_alloc`:

idr_alloc
=========

.. c:function:: int idr_alloc(struct idr *idr, void *ptr, int start, int end, gfp_t gfp)

    Allocate an ID.

    :param struct idr \*idr:
        IDR handle.

    :param void \*ptr:
        Pointer to be associated with the new ID.

    :param int start:
        The minimum ID (inclusive).

    :param int end:
        The maximum ID (exclusive).

    :param gfp_t gfp:
        Memory allocation flags.

.. _`idr_alloc.description`:

Description
-----------

Allocates an unused ID in the range specified by \ ``start``\  and \ ``end``\ .  If
\ ``end``\  is <= 0, it is treated as one larger than \ ``INT_MAX``\ .  This allows
callers to use \ ``start``\  + N as \ ``end``\  as long as N is within integer range.

The caller should provide their own locking to ensure that two
concurrent modifications to the IDR are not possible.  Read-only
accesses to the IDR may be done under the RCU read lock or may
exclude simultaneous writers.

.. _`idr_alloc.return`:

Return
------

The newly allocated ID, -ENOMEM if memory allocation failed,
or -ENOSPC if no free IDs could be found.

.. _`idr_alloc_cyclic`:

idr_alloc_cyclic
================

.. c:function:: int idr_alloc_cyclic(struct idr *idr, void *ptr, int start, int end, gfp_t gfp)

    Allocate an ID cyclically.

    :param struct idr \*idr:
        IDR handle.

    :param void \*ptr:
        Pointer to be associated with the new ID.

    :param int start:
        The minimum ID (inclusive).

    :param int end:
        The maximum ID (exclusive).

    :param gfp_t gfp:
        Memory allocation flags.

.. _`idr_alloc_cyclic.description`:

Description
-----------

Allocates an unused ID in the range specified by \ ``nextid``\  and \ ``end``\ .  If
\ ``end``\  is <= 0, it is treated as one larger than \ ``INT_MAX``\ .  This allows
callers to use \ ``start``\  + N as \ ``end``\  as long as N is within integer range.
The search for an unused ID will start at the last ID allocated and will
wrap around to \ ``start``\  if no free IDs are found before reaching \ ``end``\ .

The caller should provide their own locking to ensure that two
concurrent modifications to the IDR are not possible.  Read-only
accesses to the IDR may be done under the RCU read lock or may
exclude simultaneous writers.

.. _`idr_alloc_cyclic.return`:

Return
------

The newly allocated ID, -ENOMEM if memory allocation failed,
or -ENOSPC if no free IDs could be found.

.. _`idr_remove`:

idr_remove
==========

.. c:function:: void *idr_remove(struct idr *idr, unsigned long id)

    Remove an ID from the IDR.

    :param struct idr \*idr:
        IDR handle.

    :param unsigned long id:
        Pointer ID.

.. _`idr_remove.description`:

Description
-----------

Removes this ID from the IDR.  If the ID was not previously in the IDR,
this function returns \ ``NULL``\ .

Since this function modifies the IDR, the caller should provide their
own locking to ensure that concurrent modification of the same IDR is
not possible.

.. _`idr_remove.return`:

Return
------

The pointer formerly associated with this ID.

.. _`idr_find`:

idr_find
========

.. c:function:: void *idr_find(const struct idr *idr, unsigned long id)

    Return pointer for given ID.

    :param const struct idr \*idr:
        IDR handle.

    :param unsigned long id:
        Pointer ID.

.. _`idr_find.description`:

Description
-----------

Looks up the pointer associated with this ID.  A \ ``NULL``\  pointer may
indicate that \ ``id``\  is not allocated or that the \ ``NULL``\  pointer was
associated with this ID.

This function can be called under \ :c:func:`rcu_read_lock`\ , given that the leaf
pointers lifetimes are correctly managed.

.. _`idr_find.return`:

Return
------

The pointer associated with this ID.

.. _`idr_for_each`:

idr_for_each
============

.. c:function:: int idr_for_each(const struct idr *idr, int (*fn)(int id, void *p, void *data), void *data)

    Iterate through all stored pointers.

    :param const struct idr \*idr:
        IDR handle.

    :param int (\*fn)(int id, void \*p, void \*data):
        Function to be called for each pointer.

    :param void \*data:
        Data passed to callback function.

.. _`idr_for_each.description`:

Description
-----------

The callback function will be called for each entry in \ ``idr``\ , passing
the ID, the entry and \ ``data``\ .

If \ ``fn``\  returns anything other than \ ``0``\ , the iteration stops and that
value is returned from this function.

\ :c:func:`idr_for_each`\  can be called concurrently with \ :c:func:`idr_alloc`\  and
\ :c:func:`idr_remove`\  if protected by RCU.  Newly added entries may not be
seen and deleted entries may be seen, but adding and removing entries
will not cause other entries to be skipped, nor spurious ones to be seen.

.. _`idr_get_next`:

idr_get_next
============

.. c:function:: void *idr_get_next(struct idr *idr, int *nextid)

    Find next populated entry.

    :param struct idr \*idr:
        IDR handle.

    :param int \*nextid:
        Pointer to an ID.

.. _`idr_get_next.description`:

Description
-----------

Returns the next populated entry in the tree with an ID greater than
or equal to the value pointed to by \ ``nextid``\ .  On exit, \ ``nextid``\  is updated
to the ID of the found value.  To use in a loop, the value pointed to by
nextid must be incremented by the user.

.. _`idr_get_next_ul`:

idr_get_next_ul
===============

.. c:function:: void *idr_get_next_ul(struct idr *idr, unsigned long *nextid)

    Find next populated entry.

    :param struct idr \*idr:
        IDR handle.

    :param unsigned long \*nextid:
        Pointer to an ID.

.. _`idr_get_next_ul.description`:

Description
-----------

Returns the next populated entry in the tree with an ID greater than
or equal to the value pointed to by \ ``nextid``\ .  On exit, \ ``nextid``\  is updated
to the ID of the found value.  To use in a loop, the value pointed to by
nextid must be incremented by the user.

.. _`idr_replace`:

idr_replace
===========

.. c:function:: void *idr_replace(struct idr *idr, void *ptr, unsigned long id)

    replace pointer for given ID.

    :param struct idr \*idr:
        IDR handle.

    :param void \*ptr:
        New pointer to associate with the ID.

    :param unsigned long id:
        ID to change.

.. _`idr_replace.description`:

Description
-----------

Replace the pointer registered with an ID and return the old value.
This function can be called under the RCU read lock concurrently with
\ :c:func:`idr_alloc`\  and \ :c:func:`idr_remove`\  (as long as the ID being removed is not
the one being replaced!).

.. _`idr_replace.return`:

Return
------

the old value on success.  \ ``-ENOENT``\  indicates that \ ``id``\  was not
found.  \ ``-EINVAL``\  indicates that \ ``ptr``\  was not valid.

.. _`ida-description`:

IDA description
===============

The IDA is an ID allocator which does not provide the ability to
associate an ID with a pointer.  As such, it only needs to store one
bit per ID, and so is more space efficient than an IDR.  To use an IDA,
define it using \ :c:func:`DEFINE_IDA`\  (or embed a \ :c:type:`struct ida <ida>`\  in a data structure,
then initialise it using \ :c:func:`ida_init`\ ).  To allocate a new ID, call
\ :c:func:`ida_simple_get`\ .  To free an ID, call \ :c:func:`ida_simple_remove`\ .

If you have more complex locking requirements, use a loop around
\ :c:func:`ida_pre_get`\  and \ :c:func:`ida_get_new`\  to allocate a new ID.  Then use
\ :c:func:`ida_remove`\  to free an ID.  You must make sure that \ :c:func:`ida_get_new`\  and
\ :c:func:`ida_remove`\  cannot be called at the same time as each other for the
same IDA.

You can also use \ :c:func:`ida_get_new_above`\  if you need an ID to be allocated
above a particular number.  \ :c:func:`ida_destroy`\  can be used to dispose of an
IDA without needing to free the individual IDs in it.  You can use
\ :c:func:`ida_is_empty`\  to find out whether the IDA has any IDs currently allocated.

IDs are currently limited to the range [0-INT_MAX].  If this is an awkward
limitation, it should be quite straightforward to raise the maximum.

.. _`ida_get_new_above`:

ida_get_new_above
=================

.. c:function:: int ida_get_new_above(struct ida *ida, int start, int *id)

    allocate new ID above or equal to a start id

    :param struct ida \*ida:
        ida handle

    :param int start:
        id to start search at

    :param int \*id:
        pointer to the allocated handle

.. _`ida_get_new_above.description`:

Description
-----------

Allocate new ID above or equal to \ ``start``\ .  It should be called
with any required locks to ensure that concurrent calls to
\ :c:func:`ida_get_new_above`\  / \ :c:func:`ida_get_new`\  / \ :c:func:`ida_remove`\  are not allowed.
Consider using \ :c:func:`ida_simple_get`\  if you do not have complex locking
requirements.

If memory is required, it will return \ ``-EAGAIN``\ , you should unlock
and go back to the \ :c:func:`ida_pre_get`\  call.  If the ida is full, it will
return \ ``-ENOSPC``\ .  On success, it will return 0.

\ ``id``\  returns a value in the range \ ``start``\  ... \ ``0x7fffffff``\ .

.. _`ida_remove`:

ida_remove
==========

.. c:function:: void ida_remove(struct ida *ida, int id)

    Free the given ID

    :param struct ida \*ida:
        ida handle

    :param int id:
        ID to free

.. _`ida_remove.description`:

Description
-----------

This function should not be called at the same time as \ :c:func:`ida_get_new_above`\ .

.. _`ida_destroy`:

ida_destroy
===========

.. c:function:: void ida_destroy(struct ida *ida)

    Free the contents of an ida

    :param struct ida \*ida:
        ida handle

.. _`ida_destroy.description`:

Description
-----------

Calling this function releases all resources associated with an IDA.  When
this call returns, the IDA is empty and can be reused or freed.  The caller
should not allow \ :c:func:`ida_remove`\  or \ :c:func:`ida_get_new_above`\  to be called at the
same time.

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

Compared to \ :c:func:`ida_get_new_above`\  this function does its own locking, and
should be used unless there are special requirements.

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

.. _`ida_simple_remove.description`:

Description
-----------

Use to release an id allocated with \ :c:func:`ida_simple_get`\ .

Compared to \ :c:func:`ida_remove`\  this function does its own locking, and should be
used unless there are special requirements.

.. This file was automatic generated / don't edit.


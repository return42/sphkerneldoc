.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/idr.c

.. _`idr_alloc_u32`:

idr_alloc_u32
=============

.. c:function:: int idr_alloc_u32(struct idr *idr, void *ptr, u32 *nextid, unsigned long max, gfp_t gfp)

    Allocate an ID.

    :param idr:
        IDR handle.
    :type idr: struct idr \*

    :param ptr:
        Pointer to be associated with the new ID.
    :type ptr: void \*

    :param nextid:
        Pointer to an ID.
    :type nextid: u32 \*

    :param max:
        The maximum ID to allocate (inclusive).
    :type max: unsigned long

    :param gfp:
        Memory allocation flags.
    :type gfp: gfp_t

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

    :param idr:
        IDR handle.
    :type idr: struct idr \*

    :param ptr:
        Pointer to be associated with the new ID.
    :type ptr: void \*

    :param start:
        The minimum ID (inclusive).
    :type start: int

    :param end:
        The maximum ID (exclusive).
    :type end: int

    :param gfp:
        Memory allocation flags.
    :type gfp: gfp_t

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

    :param idr:
        IDR handle.
    :type idr: struct idr \*

    :param ptr:
        Pointer to be associated with the new ID.
    :type ptr: void \*

    :param start:
        The minimum ID (inclusive).
    :type start: int

    :param end:
        The maximum ID (exclusive).
    :type end: int

    :param gfp:
        Memory allocation flags.
    :type gfp: gfp_t

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

    :param idr:
        IDR handle.
    :type idr: struct idr \*

    :param id:
        Pointer ID.
    :type id: unsigned long

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

    :param idr:
        IDR handle.
    :type idr: const struct idr \*

    :param id:
        Pointer ID.
    :type id: unsigned long

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

    :param idr:
        IDR handle.
    :type idr: const struct idr \*

    :param int (\*fn)(int id, void \*p, void \*data):
        Function to be called for each pointer.

    :param data:
        Data passed to callback function.
    :type data: void \*

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

    :param idr:
        IDR handle.
    :type idr: struct idr \*

    :param nextid:
        Pointer to an ID.
    :type nextid: int \*

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

    :param idr:
        IDR handle.
    :type idr: struct idr \*

    :param nextid:
        Pointer to an ID.
    :type nextid: unsigned long \*

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

    :param idr:
        IDR handle.
    :type idr: struct idr \*

    :param ptr:
        New pointer to associate with the ID.
    :type ptr: void \*

    :param id:
        ID to change.
    :type id: unsigned long

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
\ :c:func:`ida_alloc`\ , \ :c:func:`ida_alloc_min`\ , \ :c:func:`ida_alloc_max`\  or \ :c:func:`ida_alloc_range`\ .
To free an ID, call \ :c:func:`ida_free`\ .

\ :c:func:`ida_destroy`\  can be used to dispose of an IDA without needing to
free the individual IDs in it.  You can use \ :c:func:`ida_is_empty`\  to find
out whether the IDA has any IDs currently allocated.

The IDA handles its own locking.  It is safe to call any of the IDA
functions without synchronisation in your code.

IDs are currently limited to the range [0-INT_MAX].  If this is an awkward
limitation, it should be quite straightforward to raise the maximum.

.. _`ida_alloc_range`:

ida_alloc_range
===============

.. c:function:: int ida_alloc_range(struct ida *ida, unsigned int min, unsigned int max, gfp_t gfp)

    Allocate an unused ID.

    :param ida:
        IDA handle.
    :type ida: struct ida \*

    :param min:
        Lowest ID to allocate.
    :type min: unsigned int

    :param max:
        Highest ID to allocate.
    :type max: unsigned int

    :param gfp:
        Memory allocation flags.
    :type gfp: gfp_t

.. _`ida_alloc_range.description`:

Description
-----------

Allocate an ID between \ ``min``\  and \ ``max``\ , inclusive.  The allocated ID will
not exceed \ ``INT_MAX``\ , even if \ ``max``\  is larger.

.. _`ida_alloc_range.context`:

Context
-------

Any context.

.. _`ida_alloc_range.return`:

Return
------

The allocated ID, or \ ``-ENOMEM``\  if memory could not be allocated,
or \ ``-ENOSPC``\  if there are no free IDs.

.. _`ida_free`:

ida_free
========

.. c:function:: void ida_free(struct ida *ida, unsigned int id)

    Release an allocated ID.

    :param ida:
        IDA handle.
    :type ida: struct ida \*

    :param id:
        Previously allocated ID.
    :type id: unsigned int

.. _`ida_free.context`:

Context
-------

Any context.

.. _`ida_destroy`:

ida_destroy
===========

.. c:function:: void ida_destroy(struct ida *ida)

    Free all IDs.

    :param ida:
        IDA handle.
    :type ida: struct ida \*

.. _`ida_destroy.description`:

Description
-----------

Calling this function frees all IDs and releases all resources used
by an IDA.  When this call returns, the IDA is empty and can be reused
or freed.  If the IDA is already empty, there is no need to call this
function.

.. _`ida_destroy.context`:

Context
-------

Any context.

.. This file was automatic generated / don't edit.


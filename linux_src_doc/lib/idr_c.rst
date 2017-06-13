.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/idr.c

.. _`idr_alloc`:

idr_alloc
=========

.. c:function:: int idr_alloc(struct idr *idr, void *ptr, int start, int end, gfp_t gfp)

    allocate an id

    :param struct idr \*idr:
        idr handle

    :param void \*ptr:
        pointer to be associated with the new id

    :param int start:
        the minimum id (inclusive)

    :param int end:
        the maximum id (exclusive)

    :param gfp_t gfp:
        memory allocation flags

.. _`idr_alloc.description`:

Description
-----------

Allocates an unused ID in the range [start, end).  Returns -ENOSPC
if there are no unused IDs in that range.

Note that \ ``end``\  is treated as max when <= 0.  This is to always allow
using \ ``start``\  + N as \ ``end``\  as long as N is inside integer range.

Simultaneous modifications to the \ ``idr``\  are not allowed and should be
prevented by the user, usually with a lock.  \ :c:func:`idr_alloc`\  may be called
concurrently with read-only accesses to the \ ``idr``\ , such as \ :c:func:`idr_find`\  and
\ :c:func:`idr_for_each_entry`\ .

.. _`idr_alloc_cyclic`:

idr_alloc_cyclic
================

.. c:function:: int idr_alloc_cyclic(struct idr *idr, void *ptr, int start, int end, gfp_t gfp)

    allocate new idr entry in a cyclical fashion

    :param struct idr \*idr:
        idr handle

    :param void \*ptr:
        pointer to be associated with the new id

    :param int start:
        the minimum id (inclusive)

    :param int end:
        the maximum id (exclusive)

    :param gfp_t gfp:
        memory allocation flags

.. _`idr_alloc_cyclic.description`:

Description
-----------

Allocates an ID larger than the last ID allocated if one is available.
If not, it will attempt to allocate the smallest ID that is larger or
equal to \ ``start``\ .

.. _`idr_for_each`:

idr_for_each
============

.. c:function:: int idr_for_each(const struct idr *idr, int (*fn)(int id, void *p, void *data), void *data)

    iterate through all stored pointers

    :param const struct idr \*idr:
        idr handle

    :param int (\*fn)(int id, void \*p, void \*data):
        function to be called for each pointer

    :param void \*data:
        data passed to callback function

.. _`idr_for_each.description`:

Description
-----------

The callback function will be called for each entry in \ ``idr``\ , passing
the id, the pointer and the data pointer passed to this function.

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

    Find next populated entry

    :param struct idr \*idr:
        idr handle

    :param int \*nextid:
        Pointer to lowest possible ID to return

.. _`idr_get_next.description`:

Description
-----------

Returns the next populated entry in the tree with an ID greater than
or equal to the value pointed to by \ ``nextid``\ .  On exit, \ ``nextid``\  is updated
to the ID of the found value.  To use in a loop, the value pointed to by
nextid must be incremented by the user.

.. _`idr_replace`:

idr_replace
===========

.. c:function:: void *idr_replace(struct idr *idr, void *ptr, int id)

    replace pointer for given id

    :param struct idr \*idr:
        idr handle

    :param void \*ptr:
        New pointer to associate with the ID

    :param int id:
        Lookup key

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

0 on success.  \ ``-ENOENT``\  indicates that \ ``id``\  was not found.
\ ``-EINVAL``\  indicates that \ ``id``\  or \ ``ptr``\  were not valid.

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


.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/xarray.c

.. _`xas_load`:

xas_load
========

.. c:function:: void *xas_load(struct xa_state *xas)

    Load an entry from the XArray (advanced).

    :param xas:
        XArray operation state.
    :type xas: struct xa_state \*

.. _`xas_load.description`:

Description
-----------

Usually walks the \ ``xas``\  to the appropriate state to load the entry
stored at xa_index.  However, it will do nothing and return \ ``NULL``\  if
\ ``xas``\  is in an error state.  \ :c:func:`xas_load`\  will never expand the tree.

If the xa_state is set up to operate on a multi-index entry, \ :c:func:`xas_load`\ 
may return \ ``NULL``\  or an internal entry, even if there are entries
present within the range specified by \ ``xas``\ .

.. _`xas_load.context`:

Context
-------

Any context.  The caller should hold the xa_lock or the RCU lock.

.. _`xas_load.return`:

Return
------

Usually an entry in the XArray, but see description for exceptions.

.. _`xas_nomem`:

xas_nomem
=========

.. c:function:: bool xas_nomem(struct xa_state *xas, gfp_t gfp)

    Allocate memory if needed.

    :param xas:
        XArray operation state.
    :type xas: struct xa_state \*

    :param gfp:
        Memory allocation flags.
    :type gfp: gfp_t

.. _`xas_nomem.description`:

Description
-----------

If we need to add new nodes to the XArray, we try to allocate memory
with GFP_NOWAIT while holding the lock, which will usually succeed.
If it fails, \ ``xas``\  is flagged as needing memory to continue.  The caller
should drop the lock and call \ :c:func:`xas_nomem`\ .  If \ :c:func:`xas_nomem`\  succeeds,
the caller should retry the operation.

Forward progress is guaranteed as one node is allocated here and
stored in the xa_state where it will be found by \ :c:func:`xas_alloc`\ .  More
nodes will likely be found in the slab allocator, but we do not tie
them up here.

.. _`xas_nomem.return`:

Return
------

true if memory was needed, and was successfully allocated.

.. _`xas_free_nodes`:

xas_free_nodes
==============

.. c:function:: void xas_free_nodes(struct xa_state *xas, struct xa_node *top)

    Free this node and all nodes that it references

    :param xas:
        Array operation state.
    :type xas: struct xa_state \*

    :param top:
        Node to free
    :type top: struct xa_node \*

.. _`xas_free_nodes.description`:

Description
-----------

This node has been removed from the tree.  We must now free it and all
of its subnodes.  There may be RCU walkers with references into the tree,
so we must replace all entries with retry markers.

.. _`xas_create_range`:

xas_create_range
================

.. c:function:: void xas_create_range(struct xa_state *xas)

    Ensure that stores to this range will succeed

    :param xas:
        XArray operation state.
    :type xas: struct xa_state \*

.. _`xas_create_range.description`:

Description
-----------

Creates all of the slots in the range covered by \ ``xas``\ .  Sets \ ``xas``\  to
create single-index entries and positions it at the beginning of the
range.  This is for the benefit of users which have not yet been
converted to use multi-index entries.

.. _`xas_store`:

xas_store
=========

.. c:function:: void *xas_store(struct xa_state *xas, void *entry)

    Store this entry in the XArray.

    :param xas:
        XArray operation state.
    :type xas: struct xa_state \*

    :param entry:
        New entry.
    :type entry: void \*

.. _`xas_store.description`:

Description
-----------

If \ ``xas``\  is operating on a multi-index entry, the entry returned by this
function is essentially meaningless (it may be an internal entry or it
may be \ ``NULL``\ , even if there are non-NULL entries at some of the indices
covered by the range).  This is not a problem for any current users,
and can be changed if needed.

.. _`xas_store.return`:

Return
------

The old entry at this index.

.. _`xas_get_mark`:

xas_get_mark
============

.. c:function:: bool xas_get_mark(const struct xa_state *xas, xa_mark_t mark)

    Returns the state of this mark.

    :param xas:
        XArray operation state.
    :type xas: const struct xa_state \*

    :param mark:
        Mark number.
    :type mark: xa_mark_t

.. _`xas_get_mark.return`:

Return
------

true if the mark is set, false if the mark is clear or \ ``xas``\ 
is in an error state.

.. _`xas_set_mark`:

xas_set_mark
============

.. c:function:: void xas_set_mark(const struct xa_state *xas, xa_mark_t mark)

    Sets the mark on this entry and its parents.

    :param xas:
        XArray operation state.
    :type xas: const struct xa_state \*

    :param mark:
        Mark number.
    :type mark: xa_mark_t

.. _`xas_set_mark.description`:

Description
-----------

Sets the specified mark on this entry, and walks up the tree setting it
on all the ancestor entries.  Does nothing if \ ``xas``\  has not been walked to
an entry, or is in an error state.

.. _`xas_clear_mark`:

xas_clear_mark
==============

.. c:function:: void xas_clear_mark(const struct xa_state *xas, xa_mark_t mark)

    Clears the mark on this entry and its parents.

    :param xas:
        XArray operation state.
    :type xas: const struct xa_state \*

    :param mark:
        Mark number.
    :type mark: xa_mark_t

.. _`xas_clear_mark.description`:

Description
-----------

Clears the specified mark on this entry, and walks back to the head
attempting to clear it on all the ancestor entries.  Does nothing if
\ ``xas``\  has not been walked to an entry, or is in an error state.

.. _`xas_init_marks`:

xas_init_marks
==============

.. c:function:: void xas_init_marks(const struct xa_state *xas)

    Initialise all marks for the entry

    :param xas:
        Array operations state.
    :type xas: const struct xa_state \*

.. _`xas_init_marks.description`:

Description
-----------

Initialise all marks for the entry specified by \ ``xas``\ .  If we're tracking
free entries with a mark, we need to set it on all entries.  All other
marks are cleared.

This implementation is not as efficient as it could be; we may walk
up the tree multiple times.

.. _`xas_pause`:

xas_pause
=========

.. c:function:: void xas_pause(struct xa_state *xas)

    Pause a walk to drop a lock.

    :param xas:
        XArray operation state.
    :type xas: struct xa_state \*

.. _`xas_pause.description`:

Description
-----------

Some users need to pause a walk and drop the lock they're holding in
order to yield to a higher priority thread or carry out an operation
on an entry.  Those users should call this function before they drop
the lock.  It resets the \ ``xas``\  to be suitable for the next iteration
of the loop after the user has reacquired the lock.  If most entries
found during a walk require you to call \ :c:func:`xas_pause`\ , the \ :c:func:`xa_for_each`\ 
iterator may be more appropriate.

Note that \ :c:func:`xas_pause`\  only works for forward iteration.  If a user needs
to pause a reverse iteration, we will need a \ :c:func:`xas_pause_rev`\ .

.. _`xas_find`:

xas_find
========

.. c:function:: void *xas_find(struct xa_state *xas, unsigned long max)

    Find the next present entry in the XArray.

    :param xas:
        XArray operation state.
    :type xas: struct xa_state \*

    :param max:
        Highest index to return.
    :type max: unsigned long

.. _`xas_find.description`:

Description
-----------

If the \ ``xas``\  has not yet been walked to an entry, return the entry
which has an index >= xas.xa_index.  If it has been walked, the entry
currently being pointed at has been processed, and so we move to the
next entry.

If no entry is found and the array is smaller than \ ``max``\ , the iterator
is set to the smallest index not yet in the array.  This allows \ ``xas``\ 
to be immediately passed to \ :c:func:`xas_store`\ .

.. _`xas_find.return`:

Return
------

The entry, if found, otherwise \ ``NULL``\ .

.. _`xas_find_marked`:

xas_find_marked
===============

.. c:function:: void *xas_find_marked(struct xa_state *xas, unsigned long max, xa_mark_t mark)

    Find the next marked entry in the XArray.

    :param xas:
        XArray operation state.
    :type xas: struct xa_state \*

    :param max:
        Highest index to return.
    :type max: unsigned long

    :param mark:
        Mark number to search for.
    :type mark: xa_mark_t

.. _`xas_find_marked.description`:

Description
-----------

If the \ ``xas``\  has not yet been walked to an entry, return the marked entry
which has an index >= xas.xa_index.  If it has been walked, the entry
currently being pointed at has been processed, and so we return the
first marked entry with an index > xas.xa_index.

If no marked entry is found and the array is smaller than \ ``max``\ , \ ``xas``\  is
set to the bounds state and xas->xa_index is set to the smallest index
not yet in the array.  This allows \ ``xas``\  to be immediately passed to
\ :c:func:`xas_store`\ .

If no entry is found before \ ``max``\  is reached, \ ``xas``\  is set to the restart
state.

.. _`xas_find_marked.return`:

Return
------

The entry, if found, otherwise \ ``NULL``\ .

.. _`xas_find_conflict`:

xas_find_conflict
=================

.. c:function:: void *xas_find_conflict(struct xa_state *xas)

    Find the next present entry in a range.

    :param xas:
        XArray operation state.
    :type xas: struct xa_state \*

.. _`xas_find_conflict.description`:

Description
-----------

The \ ``xas``\  describes both a range and a position within that range.

.. _`xas_find_conflict.context`:

Context
-------

Any context.  Expects xa_lock to be held.

.. _`xas_find_conflict.return`:

Return
------

The next entry in the range covered by \ ``xas``\  or \ ``NULL``\ .

.. _`xa_init_flags`:

xa_init_flags
=============

.. c:function:: void xa_init_flags(struct xarray *xa, gfp_t flags)

    Initialise an empty XArray with flags.

    :param xa:
        XArray.
    :type xa: struct xarray \*

    :param flags:
        XA_FLAG values.
    :type flags: gfp_t

.. _`xa_init_flags.description`:

Description
-----------

If you need to initialise an XArray with special flags (eg you need
to take the lock from interrupt context), use this function instead
of \ :c:func:`xa_init`\ .

.. _`xa_init_flags.context`:

Context
-------

Any context.

.. _`xa_load`:

xa_load
=======

.. c:function:: void *xa_load(struct xarray *xa, unsigned long index)

    Load an entry from an XArray.

    :param xa:
        XArray.
    :type xa: struct xarray \*

    :param index:
        index into array.
    :type index: unsigned long

.. _`xa_load.context`:

Context
-------

Any context.  Takes and releases the RCU lock.

.. _`xa_load.return`:

Return
------

The entry at \ ``index``\  in \ ``xa``\ .

.. _`__xa_erase`:

__xa_erase
==========

.. c:function:: void *__xa_erase(struct xarray *xa, unsigned long index)

    Erase this entry from the XArray while locked.

    :param xa:
        XArray.
    :type xa: struct xarray \*

    :param index:
        Index into array.
    :type index: unsigned long

.. _`__xa_erase.description`:

Description
-----------

If the entry at this index is a multi-index entry then all indices will
be erased, and the entry will no longer be a multi-index entry.
This function expects the xa_lock to be held on entry.

.. _`__xa_erase.context`:

Context
-------

Any context.  Expects xa_lock to be held on entry.  May
release and reacquire xa_lock if \ ``gfp``\  flags permit.

.. _`__xa_erase.return`:

Return
------

The old entry at this index.

.. _`xa_erase`:

xa_erase
========

.. c:function:: void *xa_erase(struct xarray *xa, unsigned long index)

    Erase this entry from the XArray.

    :param xa:
        XArray.
    :type xa: struct xarray \*

    :param index:
        Index of entry.
    :type index: unsigned long

.. _`xa_erase.description`:

Description
-----------

This function is the equivalent of calling \ :c:func:`xa_store`\  with \ ``NULL``\  as
the third argument.  The XArray does not need to allocate memory, so
the user does not need to provide GFP flags.

.. _`xa_erase.context`:

Context
-------

Any context.  Takes and releases the xa_lock.

.. _`xa_erase.return`:

Return
------

The entry which used to be at this index.

.. _`__xa_store`:

__xa_store
==========

.. c:function:: void *__xa_store(struct xarray *xa, unsigned long index, void *entry, gfp_t gfp)

    Store this entry in the XArray.

    :param xa:
        XArray.
    :type xa: struct xarray \*

    :param index:
        Index into array.
    :type index: unsigned long

    :param entry:
        New entry.
    :type entry: void \*

    :param gfp:
        Memory allocation flags.
    :type gfp: gfp_t

.. _`__xa_store.description`:

Description
-----------

You must already be holding the xa_lock when calling this function.
It will drop the lock if needed to allocate memory, and then reacquire
it afterwards.

.. _`__xa_store.context`:

Context
-------

Any context.  Expects xa_lock to be held on entry.  May
release and reacquire xa_lock if \ ``gfp``\  flags permit.

.. _`__xa_store.return`:

Return
------

The old entry at this index or \ :c:func:`xa_err`\  if an error happened.

.. _`xa_store`:

xa_store
========

.. c:function:: void *xa_store(struct xarray *xa, unsigned long index, void *entry, gfp_t gfp)

    Store this entry in the XArray.

    :param xa:
        XArray.
    :type xa: struct xarray \*

    :param index:
        Index into array.
    :type index: unsigned long

    :param entry:
        New entry.
    :type entry: void \*

    :param gfp:
        Memory allocation flags.
    :type gfp: gfp_t

.. _`xa_store.description`:

Description
-----------

After this function returns, loads from this index will return \ ``entry``\ .
Storing into an existing multislot entry updates the entry of every index.
The marks associated with \ ``index``\  are unaffected unless \ ``entry``\  is \ ``NULL``\ .

.. _`xa_store.context`:

Context
-------

Any context.  Takes and releases the xa_lock.
May sleep if the \ ``gfp``\  flags permit.

.. _`xa_store.return`:

Return
------

The old entry at this index on success, xa_err(-EINVAL) if \ ``entry``\ 
cannot be stored in an XArray, or xa_err(-ENOMEM) if memory allocation
failed.

.. _`__xa_cmpxchg`:

__xa_cmpxchg
============

.. c:function:: void *__xa_cmpxchg(struct xarray *xa, unsigned long index, void *old, void *entry, gfp_t gfp)

    Store this entry in the XArray.

    :param xa:
        XArray.
    :type xa: struct xarray \*

    :param index:
        Index into array.
    :type index: unsigned long

    :param old:
        Old value to test against.
    :type old: void \*

    :param entry:
        New entry.
    :type entry: void \*

    :param gfp:
        Memory allocation flags.
    :type gfp: gfp_t

.. _`__xa_cmpxchg.description`:

Description
-----------

You must already be holding the xa_lock when calling this function.
It will drop the lock if needed to allocate memory, and then reacquire
it afterwards.

.. _`__xa_cmpxchg.context`:

Context
-------

Any context.  Expects xa_lock to be held on entry.  May
release and reacquire xa_lock if \ ``gfp``\  flags permit.

.. _`__xa_cmpxchg.return`:

Return
------

The old entry at this index or \ :c:func:`xa_err`\  if an error happened.

.. _`__xa_reserve`:

__xa_reserve
============

.. c:function:: int __xa_reserve(struct xarray *xa, unsigned long index, gfp_t gfp)

    Reserve this index in the XArray.

    :param xa:
        XArray.
    :type xa: struct xarray \*

    :param index:
        Index into array.
    :type index: unsigned long

    :param gfp:
        Memory allocation flags.
    :type gfp: gfp_t

.. _`__xa_reserve.description`:

Description
-----------

Ensures there is somewhere to store an entry at \ ``index``\  in the array.
If there is already something stored at \ ``index``\ , this function does
nothing.  If there was nothing there, the entry is marked as reserved.
Loading from a reserved entry returns a \ ``NULL``\  pointer.

If you do not use the entry that you have reserved, call \ :c:func:`xa_release`\ 
or \ :c:func:`xa_erase`\  to free any unnecessary memory.

.. _`__xa_reserve.context`:

Context
-------

Any context.  Expects the xa_lock to be held on entry.  May
release the lock, sleep and reacquire the lock if the \ ``gfp``\  flags permit.

.. _`__xa_reserve.return`:

Return
------

0 if the reservation succeeded or -ENOMEM if it failed.

.. _`xa_store_range`:

xa_store_range
==============

.. c:function:: void *xa_store_range(struct xarray *xa, unsigned long first, unsigned long last, void *entry, gfp_t gfp)

    Store this entry at a range of indices in the XArray.

    :param xa:
        XArray.
    :type xa: struct xarray \*

    :param first:
        First index to affect.
    :type first: unsigned long

    :param last:
        Last index to affect.
    :type last: unsigned long

    :param entry:
        New entry.
    :type entry: void \*

    :param gfp:
        Memory allocation flags.
    :type gfp: gfp_t

.. _`xa_store_range.description`:

Description
-----------

After this function returns, loads from any index between \ ``first``\  and \ ``last``\ ,
inclusive will return \ ``entry``\ .
Storing into an existing multislot entry updates the entry of every index.
The marks associated with \ ``index``\  are unaffected unless \ ``entry``\  is \ ``NULL``\ .

.. _`xa_store_range.context`:

Context
-------

Process context.  Takes and releases the xa_lock.  May sleep
if the \ ``gfp``\  flags permit.

.. _`xa_store_range.return`:

Return
------

\ ``NULL``\  on success, xa_err(-EINVAL) if \ ``entry``\  cannot be stored in
an XArray, or xa_err(-ENOMEM) if memory allocation failed.

.. _`__xa_alloc`:

__xa_alloc
==========

.. c:function:: int __xa_alloc(struct xarray *xa, u32 *id, u32 max, void *entry, gfp_t gfp)

    Find somewhere to store this entry in the XArray.

    :param xa:
        XArray.
    :type xa: struct xarray \*

    :param id:
        Pointer to ID.
    :type id: u32 \*

    :param max:
        Maximum ID to allocate (inclusive).
    :type max: u32

    :param entry:
        New entry.
    :type entry: void \*

    :param gfp:
        Memory allocation flags.
    :type gfp: gfp_t

.. _`__xa_alloc.description`:

Description
-----------

Allocates an unused ID in the range specified by \ ``id``\  and \ ``max``\ .
Updates the \ ``id``\  pointer with the index, then stores the entry at that
index.  A concurrent lookup will not see an uninitialised \ ``id``\ .

.. _`__xa_alloc.context`:

Context
-------

Any context.  Expects xa_lock to be held on entry.  May
release and reacquire xa_lock if \ ``gfp``\  flags permit.

.. _`__xa_alloc.return`:

Return
------

0 on success, -ENOMEM if memory allocation fails or -ENOSPC if
there is no more space in the XArray.

.. _`__xa_set_mark`:

__xa_set_mark
=============

.. c:function:: void __xa_set_mark(struct xarray *xa, unsigned long index, xa_mark_t mark)

    Set this mark on this entry while locked.

    :param xa:
        XArray.
    :type xa: struct xarray \*

    :param index:
        Index of entry.
    :type index: unsigned long

    :param mark:
        Mark number.
    :type mark: xa_mark_t

.. _`__xa_set_mark.description`:

Description
-----------

Attempting to set a mark on a \ ``NULL``\  entry does not succeed.

.. _`__xa_set_mark.context`:

Context
-------

Any context.  Expects xa_lock to be held on entry.

.. _`__xa_clear_mark`:

__xa_clear_mark
===============

.. c:function:: void __xa_clear_mark(struct xarray *xa, unsigned long index, xa_mark_t mark)

    Clear this mark on this entry while locked.

    :param xa:
        XArray.
    :type xa: struct xarray \*

    :param index:
        Index of entry.
    :type index: unsigned long

    :param mark:
        Mark number.
    :type mark: xa_mark_t

.. _`__xa_clear_mark.context`:

Context
-------

Any context.  Expects xa_lock to be held on entry.

.. _`xa_get_mark`:

xa_get_mark
===========

.. c:function:: bool xa_get_mark(struct xarray *xa, unsigned long index, xa_mark_t mark)

    Inquire whether this mark is set on this entry.

    :param xa:
        XArray.
    :type xa: struct xarray \*

    :param index:
        Index of entry.
    :type index: unsigned long

    :param mark:
        Mark number.
    :type mark: xa_mark_t

.. _`xa_get_mark.description`:

Description
-----------

This function uses the RCU read lock, so the result may be out of date
by the time it returns.  If you need the result to be stable, use a lock.

.. _`xa_get_mark.context`:

Context
-------

Any context.  Takes and releases the RCU lock.

.. _`xa_get_mark.return`:

Return
------

True if the entry at \ ``index``\  has this mark set, false if it doesn't.

.. _`xa_set_mark`:

xa_set_mark
===========

.. c:function:: void xa_set_mark(struct xarray *xa, unsigned long index, xa_mark_t mark)

    Set this mark on this entry.

    :param xa:
        XArray.
    :type xa: struct xarray \*

    :param index:
        Index of entry.
    :type index: unsigned long

    :param mark:
        Mark number.
    :type mark: xa_mark_t

.. _`xa_set_mark.description`:

Description
-----------

Attempting to set a mark on a \ ``NULL``\  entry does not succeed.

.. _`xa_set_mark.context`:

Context
-------

Process context.  Takes and releases the xa_lock.

.. _`xa_clear_mark`:

xa_clear_mark
=============

.. c:function:: void xa_clear_mark(struct xarray *xa, unsigned long index, xa_mark_t mark)

    Clear this mark on this entry.

    :param xa:
        XArray.
    :type xa: struct xarray \*

    :param index:
        Index of entry.
    :type index: unsigned long

    :param mark:
        Mark number.
    :type mark: xa_mark_t

.. _`xa_clear_mark.description`:

Description
-----------

Clearing a mark always succeeds.

.. _`xa_clear_mark.context`:

Context
-------

Process context.  Takes and releases the xa_lock.

.. _`xa_find`:

xa_find
=======

.. c:function:: void *xa_find(struct xarray *xa, unsigned long *indexp, unsigned long max, xa_mark_t filter)

    Search the XArray for an entry.

    :param xa:
        XArray.
    :type xa: struct xarray \*

    :param indexp:
        Pointer to an index.
    :type indexp: unsigned long \*

    :param max:
        Maximum index to search to.
    :type max: unsigned long

    :param filter:
        Selection criterion.
    :type filter: xa_mark_t

.. _`xa_find.description`:

Description
-----------

Finds the entry in \ ``xa``\  which matches the \ ``filter``\ , and has the lowest
index that is at least \ ``indexp``\  and no more than \ ``max``\ .
If an entry is found, \ ``indexp``\  is updated to be the index of the entry.
This function is protected by the RCU read lock, so it may not find
entries which are being simultaneously added.  It will not return an
\ ``XA_RETRY_ENTRY``\ ; if you need to see retry entries, use \ :c:func:`xas_find`\ .

.. _`xa_find.context`:

Context
-------

Any context.  Takes and releases the RCU lock.

.. _`xa_find.return`:

Return
------

The entry, if found, otherwise \ ``NULL``\ .

.. _`xa_find_after`:

xa_find_after
=============

.. c:function:: void *xa_find_after(struct xarray *xa, unsigned long *indexp, unsigned long max, xa_mark_t filter)

    Search the XArray for a present entry.

    :param xa:
        XArray.
    :type xa: struct xarray \*

    :param indexp:
        Pointer to an index.
    :type indexp: unsigned long \*

    :param max:
        Maximum index to search to.
    :type max: unsigned long

    :param filter:
        Selection criterion.
    :type filter: xa_mark_t

.. _`xa_find_after.description`:

Description
-----------

Finds the entry in \ ``xa``\  which matches the \ ``filter``\  and has the lowest
index that is above \ ``indexp``\  and no more than \ ``max``\ .
If an entry is found, \ ``indexp``\  is updated to be the index of the entry.
This function is protected by the RCU read lock, so it may miss entries
which are being simultaneously added.  It will not return an
\ ``XA_RETRY_ENTRY``\ ; if you need to see retry entries, use \ :c:func:`xas_find`\ .

.. _`xa_find_after.context`:

Context
-------

Any context.  Takes and releases the RCU lock.

.. _`xa_find_after.return`:

Return
------

The pointer, if found, otherwise \ ``NULL``\ .

.. _`xa_extract`:

xa_extract
==========

.. c:function:: unsigned int xa_extract(struct xarray *xa, void **dst, unsigned long start, unsigned long max, unsigned int n, xa_mark_t filter)

    Copy selected entries from the XArray into a normal array.

    :param xa:
        The source XArray to copy from.
    :type xa: struct xarray \*

    :param dst:
        The buffer to copy entries into.
    :type dst: void \*\*

    :param start:
        The first index in the XArray eligible to be selected.
    :type start: unsigned long

    :param max:
        The last index in the XArray eligible to be selected.
    :type max: unsigned long

    :param n:
        The maximum number of entries to copy.
    :type n: unsigned int

    :param filter:
        Selection criterion.
    :type filter: xa_mark_t

.. _`xa_extract.description`:

Description
-----------

Copies up to \ ``n``\  entries that match \ ``filter``\  from the XArray.  The
copied entries will have indices between \ ``start``\  and \ ``max``\ , inclusive.

The \ ``filter``\  may be an XArray mark value, in which case entries which are
marked with that mark will be copied.  It may also be \ ``XA_PRESENT``\ , in
which case all entries which are not \ ``NULL``\  will be copied.

The entries returned may not represent a snapshot of the XArray at a
moment in time.  For example, if another thread stores to index 5, then
index 10, calling \ :c:func:`xa_extract`\  may return the old contents of index 5
and the new contents of index 10.  Indices not modified while this
function is running will not be skipped.

If you need stronger guarantees, holding the xa_lock across calls to this
function will prevent concurrent modification.

.. _`xa_extract.context`:

Context
-------

Any context.  Takes and releases the RCU lock.

.. _`xa_extract.return`:

Return
------

The number of entries copied.

.. _`xa_destroy`:

xa_destroy
==========

.. c:function:: void xa_destroy(struct xarray *xa)

    Free all internal data structures.

    :param xa:
        XArray.
    :type xa: struct xarray \*

.. _`xa_destroy.description`:

Description
-----------

After calling this function, the XArray is empty and has freed all memory
allocated for its internal data structures.  You are responsible for
freeing the objects referenced by the XArray.

.. _`xa_destroy.context`:

Context
-------

Any context.  Takes and releases the xa_lock, interrupt-safe.

.. This file was automatic generated / don't edit.


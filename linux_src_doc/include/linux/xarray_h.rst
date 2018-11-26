.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/xarray.h

.. _`xa_mk_value`:

xa_mk_value
===========

.. c:function:: void *xa_mk_value(unsigned long v)

    Create an XArray entry from an integer.

    :param v:
        Value to store in XArray.
    :type v: unsigned long

.. _`xa_mk_value.context`:

Context
-------

Any context.

.. _`xa_mk_value.return`:

Return
------

An entry suitable for storing in the XArray.

.. _`xa_to_value`:

xa_to_value
===========

.. c:function:: unsigned long xa_to_value(const void *entry)

    Get value stored in an XArray entry.

    :param entry:
        XArray entry.
    :type entry: const void \*

.. _`xa_to_value.context`:

Context
-------

Any context.

.. _`xa_to_value.return`:

Return
------

The value stored in the XArray entry.

.. _`xa_is_value`:

xa_is_value
===========

.. c:function:: bool xa_is_value(const void *entry)

    Determine if an entry is a value.

    :param entry:
        XArray entry.
    :type entry: const void \*

.. _`xa_is_value.context`:

Context
-------

Any context.

.. _`xa_is_value.return`:

Return
------

True if the entry is a value, false if it is a pointer.

.. _`xa_tag_pointer`:

xa_tag_pointer
==============

.. c:function:: void *xa_tag_pointer(void *p, unsigned long tag)

    Create an XArray entry for a tagged pointer.

    :param p:
        Plain pointer.
    :type p: void \*

    :param tag:
        Tag value (0, 1 or 3).
    :type tag: unsigned long

.. _`xa_tag_pointer.description`:

Description
-----------

If the user of the XArray prefers, they can tag their pointers instead
of storing value entries.  Three tags are available (0, 1 and 3).
These are distinct from the xa_mark_t as they are not replicated up
through the array and cannot be searched for.

.. _`xa_tag_pointer.context`:

Context
-------

Any context.

.. _`xa_tag_pointer.return`:

Return
------

An XArray entry.

.. _`xa_untag_pointer`:

xa_untag_pointer
================

.. c:function:: void *xa_untag_pointer(void *entry)

    Turn an XArray entry into a plain pointer.

    :param entry:
        XArray entry.
    :type entry: void \*

.. _`xa_untag_pointer.description`:

Description
-----------

If you have stored a tagged pointer in the XArray, call this function
to get the untagged version of the pointer.

.. _`xa_untag_pointer.context`:

Context
-------

Any context.

.. _`xa_untag_pointer.return`:

Return
------

A pointer.

.. _`xa_pointer_tag`:

xa_pointer_tag
==============

.. c:function:: unsigned int xa_pointer_tag(void *entry)

    Get the tag stored in an XArray entry.

    :param entry:
        XArray entry.
    :type entry: void \*

.. _`xa_pointer_tag.description`:

Description
-----------

If you have stored a tagged pointer in the XArray, call this function
to get the tag of that pointer.

.. _`xa_pointer_tag.context`:

Context
-------

Any context.

.. _`xa_pointer_tag.return`:

Return
------

A tag.

.. _`xa_is_err`:

xa_is_err
=========

.. c:function:: bool xa_is_err(const void *entry)

    Report whether an XArray operation returned an error

    :param entry:
        Result from calling an XArray function
    :type entry: const void \*

.. _`xa_is_err.description`:

Description
-----------

If an XArray operation cannot complete an operation, it will return
a special value indicating an error.  This function tells you
whether an error occurred; \ :c:func:`xa_err`\  tells you which error occurred.

.. _`xa_is_err.context`:

Context
-------

Any context.

.. _`xa_is_err.return`:

Return
------

\ ``true``\  if the entry indicates an error.

.. _`xa_err`:

xa_err
======

.. c:function:: int xa_err(void *entry)

    Turn an XArray result into an errno.

    :param entry:
        Result from calling an XArray function.
    :type entry: void \*

.. _`xa_err.description`:

Description
-----------

If an XArray operation cannot complete an operation, it will return
a special pointer value which encodes an errno.  This function extracts
the errno from the pointer value, or returns 0 if the pointer does not
represent an errno.

.. _`xa_err.context`:

Context
-------

Any context.

.. _`xa_err.return`:

Return
------

A negative errno or 0.

.. _`define_xarray_flags`:

DEFINE_XARRAY_FLAGS
===================

.. c:function::  DEFINE_XARRAY_FLAGS( name,  flags)

    Define an XArray with custom flags.

    :param name:
        A string that names your XArray.
    :type name: 

    :param flags:
        XA_FLAG values.
    :type flags: 

.. _`define_xarray_flags.description`:

Description
-----------

This is intended for file scope definitions of XArrays.  It declares
and initialises an empty XArray with the chosen name and flags.  It is
equivalent to calling \ :c:func:`xa_init_flags`\  on the array, but it does the
initialisation at compiletime instead of runtime.

.. _`define_xarray`:

DEFINE_XARRAY
=============

.. c:function::  DEFINE_XARRAY( name)

    Define an XArray.

    :param name:
        A string that names your XArray.
    :type name: 

.. _`define_xarray.description`:

Description
-----------

This is intended for file scope definitions of XArrays.  It declares
and initialises an empty XArray with the chosen name.  It is equivalent
to calling \ :c:func:`xa_init`\  on the array, but it does the initialisation at
compiletime instead of runtime.

.. _`define_xarray_alloc`:

DEFINE_XARRAY_ALLOC
===================

.. c:function::  DEFINE_XARRAY_ALLOC( name)

    Define an XArray which can allocate IDs.

    :param name:
        A string that names your XArray.
    :type name: 

.. _`define_xarray_alloc.description`:

Description
-----------

This is intended for file scope definitions of allocating XArrays.
See also \ :c:func:`DEFINE_XARRAY`\ .

.. _`xa_init`:

xa_init
=======

.. c:function:: void xa_init(struct xarray *xa)

    Initialise an empty XArray.

    :param xa:
        XArray.
    :type xa: struct xarray \*

.. _`xa_init.description`:

Description
-----------

An empty XArray is full of NULL entries.

.. _`xa_init.context`:

Context
-------

Any context.

.. _`xa_empty`:

xa_empty
========

.. c:function:: bool xa_empty(const struct xarray *xa)

    Determine if an array has any present entries.

    :param xa:
        XArray.
    :type xa: const struct xarray \*

.. _`xa_empty.context`:

Context
-------

Any context.

.. _`xa_empty.return`:

Return
------

\ ``true``\  if the array contains only NULL pointers.

.. _`xa_marked`:

xa_marked
=========

.. c:function:: bool xa_marked(const struct xarray *xa, xa_mark_t mark)

    Inquire whether any entry in this array has a mark set

    :param xa:
        Array
    :type xa: const struct xarray \*

    :param mark:
        Mark value
    :type mark: xa_mark_t

.. _`xa_marked.context`:

Context
-------

Any context.

.. _`xa_marked.return`:

Return
------

\ ``true``\  if any entry has this mark set.

.. _`xa_for_each`:

xa_for_each
===========

.. c:function::  xa_for_each( xa,  entry,  index,  max,  filter)

    Iterate over a portion of an XArray.

    :param xa:
        XArray.
    :type xa: 

    :param entry:
        Entry retrieved from array.
    :type entry: 

    :param index:
        Index of \ ``entry``\ .
    :type index: 

    :param max:
        Maximum index to retrieve from array.
    :type max: 

    :param filter:
        Selection criterion.
    :type filter: 

.. _`xa_for_each.description`:

Description
-----------

Initialise \ ``index``\  to the lowest index you want to retrieve from the
array.  During the iteration, \ ``entry``\  will have the value of the entry
stored in \ ``xa``\  at \ ``index``\ .  The iteration will skip all entries in the
array which do not match \ ``filter``\ .  You may modify \ ``index``\  during the
iteration if you want to skip or reprocess indices.  It is safe to modify
the array during the iteration.  At the end of the iteration, \ ``entry``\  will
be set to NULL and \ ``index``\  will have a value less than or equal to max.

\ :c:func:`xa_for_each`\  is O(n.log(n)) while \ :c:func:`xas_for_each`\  is O(n).  You have
to handle your own locking with \ :c:func:`xas_for_each`\ , and if you have to unlock
after each iteration, it will also end up being O(n.log(n)).  \ :c:func:`xa_for_each`\ 
will spin if it hits a retry entry; if you intend to see retry entries,
you should use the \ :c:func:`xas_for_each`\  iterator instead.  The \ :c:func:`xas_for_each`\ 
iterator will expand into more inline code than \ :c:func:`xa_for_each`\ .

.. _`xa_for_each.context`:

Context
-------

Any context.  Takes and releases the RCU lock.

.. _`__xa_insert`:

__xa_insert
===========

.. c:function:: int __xa_insert(struct xarray *xa, unsigned long index, void *entry, gfp_t gfp)

    Store this entry in the XArray unless another entry is already present.

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

.. _`__xa_insert.description`:

Description
-----------

If you would rather see the existing entry in the array, use \ :c:func:`__xa_cmpxchg`\ .
This function is for users who don't care what the entry is, only that
one is present.

.. _`__xa_insert.context`:

Context
-------

Any context.  Expects xa_lock to be held on entry.  May
         release and reacquire xa_lock if the \ ``gfp``\  flags permit.

.. _`__xa_insert.return`:

Return
------

0 if the store succeeded.  -EEXIST if another entry was present.
-ENOMEM if memory could not be allocated.

.. _`xa_store_bh`:

xa_store_bh
===========

.. c:function:: void *xa_store_bh(struct xarray *xa, unsigned long index, void *entry, gfp_t gfp)

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

.. _`xa_store_bh.description`:

Description
-----------

This function is like calling \ :c:func:`xa_store`\  except it disables softirqs
while holding the array lock.

.. _`xa_store_bh.context`:

Context
-------

Any context.  Takes and releases the xa_lock while
disabling softirqs.

.. _`xa_store_bh.return`:

Return
------

The entry which used to be at this index.

.. _`xa_store_irq`:

xa_store_irq
============

.. c:function:: void *xa_store_irq(struct xarray *xa, unsigned long index, void *entry, gfp_t gfp)

    Erase this entry from the XArray.

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

.. _`xa_store_irq.description`:

Description
-----------

This function is like calling \ :c:func:`xa_store`\  except it disables interrupts
while holding the array lock.

.. _`xa_store_irq.context`:

Context
-------

Process context.  Takes and releases the xa_lock while
disabling interrupts.

.. _`xa_store_irq.return`:

Return
------

The entry which used to be at this index.

.. _`xa_erase_bh`:

xa_erase_bh
===========

.. c:function:: void *xa_erase_bh(struct xarray *xa, unsigned long index)

    Erase this entry from the XArray.

    :param xa:
        XArray.
    :type xa: struct xarray \*

    :param index:
        Index of entry.
    :type index: unsigned long

.. _`xa_erase_bh.description`:

Description
-----------

This function is the equivalent of calling \ :c:func:`xa_store`\  with \ ``NULL``\  as
the third argument.  The XArray does not need to allocate memory, so
the user does not need to provide GFP flags.

.. _`xa_erase_bh.context`:

Context
-------

Any context.  Takes and releases the xa_lock while
disabling softirqs.

.. _`xa_erase_bh.return`:

Return
------

The entry which used to be at this index.

.. _`xa_erase_irq`:

xa_erase_irq
============

.. c:function:: void *xa_erase_irq(struct xarray *xa, unsigned long index)

    Erase this entry from the XArray.

    :param xa:
        XArray.
    :type xa: struct xarray \*

    :param index:
        Index of entry.
    :type index: unsigned long

.. _`xa_erase_irq.description`:

Description
-----------

This function is the equivalent of calling \ :c:func:`xa_store`\  with \ ``NULL``\  as
the third argument.  The XArray does not need to allocate memory, so
the user does not need to provide GFP flags.

.. _`xa_erase_irq.context`:

Context
-------

Process context.  Takes and releases the xa_lock while
disabling interrupts.

.. _`xa_erase_irq.return`:

Return
------

The entry which used to be at this index.

.. _`xa_cmpxchg`:

xa_cmpxchg
==========

.. c:function:: void *xa_cmpxchg(struct xarray *xa, unsigned long index, void *old, void *entry, gfp_t gfp)

    Conditionally replace an entry in the XArray.

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
        New value to place in array.
    :type entry: void \*

    :param gfp:
        Memory allocation flags.
    :type gfp: gfp_t

.. _`xa_cmpxchg.description`:

Description
-----------

If the entry at \ ``index``\  is the same as \ ``old``\ , replace it with \ ``entry``\ .
If the return value is equal to \ ``old``\ , then the exchange was successful.

.. _`xa_cmpxchg.context`:

Context
-------

Any context.  Takes and releases the xa_lock.  May sleep
if the \ ``gfp``\  flags permit.

.. _`xa_cmpxchg.return`:

Return
------

The old value at this index or \ :c:func:`xa_err`\  if an error happened.

.. _`xa_insert`:

xa_insert
=========

.. c:function:: int xa_insert(struct xarray *xa, unsigned long index, void *entry, gfp_t gfp)

    Store this entry in the XArray unless another entry is already present.

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

.. _`xa_insert.description`:

Description
-----------

If you would rather see the existing entry in the array, use \ :c:func:`xa_cmpxchg`\ .
This function is for users who don't care what the entry is, only that
one is present.

.. _`xa_insert.context`:

Context
-------

Process context.  Takes and releases the xa_lock.
         May sleep if the \ ``gfp``\  flags permit.

.. _`xa_insert.return`:

Return
------

0 if the store succeeded.  -EEXIST if another entry was present.
-ENOMEM if memory could not be allocated.

.. _`xa_alloc`:

xa_alloc
========

.. c:function:: int xa_alloc(struct xarray *xa, u32 *id, u32 max, void *entry, gfp_t gfp)

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

.. _`xa_alloc.description`:

Description
-----------

Allocates an unused ID in the range specified by \ ``id``\  and \ ``max``\ .
Updates the \ ``id``\  pointer with the index, then stores the entry at that
index.  A concurrent lookup will not see an uninitialised \ ``id``\ .

.. _`xa_alloc.context`:

Context
-------

Process context.  Takes and releases the xa_lock.  May sleep if
the \ ``gfp``\  flags permit.

.. _`xa_alloc.return`:

Return
------

0 on success, -ENOMEM if memory allocation fails or -ENOSPC if
there is no more space in the XArray.

.. _`xa_alloc_bh`:

xa_alloc_bh
===========

.. c:function:: int xa_alloc_bh(struct xarray *xa, u32 *id, u32 max, void *entry, gfp_t gfp)

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

.. _`xa_alloc_bh.description`:

Description
-----------

Allocates an unused ID in the range specified by \ ``id``\  and \ ``max``\ .
Updates the \ ``id``\  pointer with the index, then stores the entry at that
index.  A concurrent lookup will not see an uninitialised \ ``id``\ .

.. _`xa_alloc_bh.context`:

Context
-------

Any context.  Takes and releases the xa_lock while
disabling softirqs.  May sleep if the \ ``gfp``\  flags permit.

.. _`xa_alloc_bh.return`:

Return
------

0 on success, -ENOMEM if memory allocation fails or -ENOSPC if
there is no more space in the XArray.

.. _`xa_alloc_irq`:

xa_alloc_irq
============

.. c:function:: int xa_alloc_irq(struct xarray *xa, u32 *id, u32 max, void *entry, gfp_t gfp)

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

.. _`xa_alloc_irq.description`:

Description
-----------

Allocates an unused ID in the range specified by \ ``id``\  and \ ``max``\ .
Updates the \ ``id``\  pointer with the index, then stores the entry at that
index.  A concurrent lookup will not see an uninitialised \ ``id``\ .

.. _`xa_alloc_irq.context`:

Context
-------

Process context.  Takes and releases the xa_lock while
disabling interrupts.  May sleep if the \ ``gfp``\  flags permit.

.. _`xa_alloc_irq.return`:

Return
------

0 on success, -ENOMEM if memory allocation fails or -ENOSPC if
there is no more space in the XArray.

.. _`xa_reserve`:

xa_reserve
==========

.. c:function:: int xa_reserve(struct xarray *xa, unsigned long index, gfp_t gfp)

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

.. _`xa_reserve.description`:

Description
-----------

Ensures there is somewhere to store an entry at \ ``index``\  in the array.
If there is already something stored at \ ``index``\ , this function does
nothing.  If there was nothing there, the entry is marked as reserved.
Loading from a reserved entry returns a \ ``NULL``\  pointer.

If you do not use the entry that you have reserved, call \ :c:func:`xa_release`\ 
or \ :c:func:`xa_erase`\  to free any unnecessary memory.

.. _`xa_reserve.context`:

Context
-------

Any context.  Takes and releases the xa_lock.
May sleep if the \ ``gfp``\  flags permit.

.. _`xa_reserve.return`:

Return
------

0 if the reservation succeeded or -ENOMEM if it failed.

.. _`xa_reserve_bh`:

xa_reserve_bh
=============

.. c:function:: int xa_reserve_bh(struct xarray *xa, unsigned long index, gfp_t gfp)

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

.. _`xa_reserve_bh.description`:

Description
-----------

A softirq-disabling version of \ :c:func:`xa_reserve`\ .

.. _`xa_reserve_bh.context`:

Context
-------

Any context.  Takes and releases the xa_lock while
disabling softirqs.

.. _`xa_reserve_bh.return`:

Return
------

0 if the reservation succeeded or -ENOMEM if it failed.

.. _`xa_reserve_irq`:

xa_reserve_irq
==============

.. c:function:: int xa_reserve_irq(struct xarray *xa, unsigned long index, gfp_t gfp)

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

.. _`xa_reserve_irq.description`:

Description
-----------

An interrupt-disabling version of \ :c:func:`xa_reserve`\ .

.. _`xa_reserve_irq.context`:

Context
-------

Process context.  Takes and releases the xa_lock while
disabling interrupts.

.. _`xa_reserve_irq.return`:

Return
------

0 if the reservation succeeded or -ENOMEM if it failed.

.. _`xa_release`:

xa_release
==========

.. c:function:: void xa_release(struct xarray *xa, unsigned long index)

    Release a reserved entry.

    :param xa:
        XArray.
    :type xa: struct xarray \*

    :param index:
        Index of entry.
    :type index: unsigned long

.. _`xa_release.description`:

Description
-----------

After calling \ :c:func:`xa_reserve`\ , you can call this function to release the
reservation.  If the entry at \ ``index``\  has been stored to, this function
will do nothing.

.. _`xa_is_sibling`:

xa_is_sibling
=============

.. c:function:: bool xa_is_sibling(const void *entry)

    Is the entry a sibling entry?

    :param entry:
        Entry retrieved from the XArray
    :type entry: const void \*

.. _`xa_is_sibling.return`:

Return
------

\ ``true``\  if the entry is a sibling entry.

.. _`xa_is_zero`:

xa_is_zero
==========

.. c:function:: bool xa_is_zero(const void *entry)

    Is the entry a zero entry?

    :param entry:
        Entry retrieved from the XArray
    :type entry: const void \*

.. _`xa_is_zero.return`:

Return
------

\ ``true``\  if the entry is a zero entry.

.. _`xa_is_retry`:

xa_is_retry
===========

.. c:function:: bool xa_is_retry(const void *entry)

    Is the entry a retry entry?

    :param entry:
        Entry retrieved from the XArray
    :type entry: const void \*

.. _`xa_is_retry.return`:

Return
------

\ ``true``\  if the entry is a retry entry.

.. _`xa_update_node_t`:

xa_update_node_t
================

.. c:function:: void xa_update_node_t(struct xa_node *node)

    A callback function from the XArray.

    :param node:
        The node which is being processed
    :type node: struct xa_node \*

.. _`xa_update_node_t.description`:

Description
-----------

This function is called every time the XArray updates the count of
present and value entries in a node.  It allows advanced users to
maintain the private_list in the node.

.. _`xa_update_node_t.context`:

Context
-------

The xa_lock is held and interrupts may be disabled.
         Implementations should not drop the xa_lock, nor re-enable
         interrupts.

.. _`xa_state`:

XA_STATE
========

.. c:function::  XA_STATE( name,  array,  index)

    Declare an XArray operation state.

    :param name:
        Name of this operation state (usually xas).
    :type name: 

    :param array:
        Array to operate on.
    :type array: 

    :param index:
        Initial index of interest.
    :type index: 

.. _`xa_state.description`:

Description
-----------

Declare and initialise an xa_state on the stack.

.. _`xa_state_order`:

XA_STATE_ORDER
==============

.. c:function::  XA_STATE_ORDER( name,  array,  index,  order)

    Declare an XArray operation state.

    :param name:
        Name of this operation state (usually xas).
    :type name: 

    :param array:
        Array to operate on.
    :type array: 

    :param index:
        Initial index of interest.
    :type index: 

    :param order:
        Order of entry.
    :type order: 

.. _`xa_state_order.description`:

Description
-----------

Declare and initialise an xa_state on the stack.  This variant of
\ :c:func:`XA_STATE`\  allows you to specify the 'order' of the element you
want to operate on.`

.. _`xas_error`:

xas_error
=========

.. c:function:: int xas_error(const struct xa_state *xas)

    Return an errno stored in the xa_state.

    :param xas:
        XArray operation state.
    :type xas: const struct xa_state \*

.. _`xas_error.return`:

Return
------

0 if no error has been noted.  A negative errno if one has.

.. _`xas_set_err`:

xas_set_err
===========

.. c:function:: void xas_set_err(struct xa_state *xas, long err)

    Note an error in the xa_state.

    :param xas:
        XArray operation state.
    :type xas: struct xa_state \*

    :param err:
        Negative error number.
    :type err: long

.. _`xas_set_err.description`:

Description
-----------

Only call this function with a negative \ ``err``\ ; zero or positive errors
will probably not behave the way you think they should.  If you want
to clear the error from an xa_state, use \ :c:func:`xas_reset`\ .

.. _`xas_invalid`:

xas_invalid
===========

.. c:function:: bool xas_invalid(const struct xa_state *xas)

    Is the xas in a retry or error state?

    :param xas:
        XArray operation state.
    :type xas: const struct xa_state \*

.. _`xas_invalid.return`:

Return
------

\ ``true``\  if the xas cannot be used for operations.

.. _`xas_valid`:

xas_valid
=========

.. c:function:: bool xas_valid(const struct xa_state *xas)

    Is the xas a valid cursor into the array?

    :param xas:
        XArray operation state.
    :type xas: const struct xa_state \*

.. _`xas_valid.return`:

Return
------

\ ``true``\  if the xas can be used for operations.

.. _`xas_is_node`:

xas_is_node
===========

.. c:function:: bool xas_is_node(const struct xa_state *xas)

    Does the xas point to a node?

    :param xas:
        XArray operation state.
    :type xas: const struct xa_state \*

.. _`xas_is_node.return`:

Return
------

\ ``true``\  if the xas currently references a node.

.. _`xas_reset`:

xas_reset
=========

.. c:function:: void xas_reset(struct xa_state *xas)

    Reset an XArray operation state.

    :param xas:
        XArray operation state.
    :type xas: struct xa_state \*

.. _`xas_reset.description`:

Description
-----------

Resets the error or walk state of the \ ``xas``\  so future walks of the
array will start from the root.  Use this if you have dropped the
xarray lock and want to reuse the xa_state.

.. _`xas_reset.context`:

Context
-------

Any context.

.. _`xas_retry`:

xas_retry
=========

.. c:function:: bool xas_retry(struct xa_state *xas, const void *entry)

    Retry the operation if appropriate.

    :param xas:
        XArray operation state.
    :type xas: struct xa_state \*

    :param entry:
        Entry from xarray.
    :type entry: const void \*

.. _`xas_retry.description`:

Description
-----------

The advanced functions may sometimes return an internal entry, such as
a retry entry or a zero entry.  This function sets up the \ ``xas``\  to restart
the walk from the head of the array if needed.

.. _`xas_retry.context`:

Context
-------

Any context.

.. _`xas_retry.return`:

Return
------

true if the operation needs to be retried.

.. _`xas_reload`:

xas_reload
==========

.. c:function:: void *xas_reload(struct xa_state *xas)

    Refetch an entry from the xarray.

    :param xas:
        XArray operation state.
    :type xas: struct xa_state \*

.. _`xas_reload.description`:

Description
-----------

Use this function to check that a previously loaded entry still has
the same value.  This is useful for the lockless pagecache lookup where
we walk the array with only the RCU lock to protect us, lock the page,
then check that the page hasn't moved since we looked it up.

The caller guarantees that \ ``xas``\  is still valid.  If it may be in an
error or restart state, call \ :c:func:`xas_load`\  instead.

.. _`xas_reload.return`:

Return
------

The entry at this location in the xarray.

.. _`xas_set`:

xas_set
=======

.. c:function:: void xas_set(struct xa_state *xas, unsigned long index)

    Set up XArray operation state for a different index.

    :param xas:
        XArray operation state.
    :type xas: struct xa_state \*

    :param index:
        New index into the XArray.
    :type index: unsigned long

.. _`xas_set.description`:

Description
-----------

Move the operation state to refer to a different index.  This will
have the effect of starting a walk from the top; see \ :c:func:`xas_next`\ 
to move to an adjacent index.

.. _`xas_set_order`:

xas_set_order
=============

.. c:function:: void xas_set_order(struct xa_state *xas, unsigned long index, unsigned int order)

    Set up XArray operation state for a multislot entry.

    :param xas:
        XArray operation state.
    :type xas: struct xa_state \*

    :param index:
        Target of the operation.
    :type index: unsigned long

    :param order:
        Entry occupies 2^@order indices.
    :type order: unsigned int

.. _`xas_set_update`:

xas_set_update
==============

.. c:function:: void xas_set_update(struct xa_state *xas, xa_update_node_t update)

    Set up XArray operation state for a callback.

    :param xas:
        XArray operation state.
    :type xas: struct xa_state \*

    :param update:
        Function to call when updating a node.
    :type update: xa_update_node_t

.. _`xas_set_update.description`:

Description
-----------

The XArray can notify a caller after it has updated an xa_node.
This is advanced functionality and is only needed by the page cache.

.. _`xas_next_entry`:

xas_next_entry
==============

.. c:function:: void *xas_next_entry(struct xa_state *xas, unsigned long max)

    Advance iterator to next present entry.

    :param xas:
        XArray operation state.
    :type xas: struct xa_state \*

    :param max:
        Highest index to return.
    :type max: unsigned long

.. _`xas_next_entry.description`:

Description
-----------

\ :c:func:`xas_next_entry`\  is an inline function to optimise xarray traversal for
speed.  It is equivalent to calling \ :c:func:`xas_find`\ , and will call \ :c:func:`xas_find`\ 
for all the hard cases.

.. _`xas_next_entry.return`:

Return
------

The next present entry after the one currently referred to by \ ``xas``\ .

.. _`xas_next_marked`:

xas_next_marked
===============

.. c:function:: void *xas_next_marked(struct xa_state *xas, unsigned long max, xa_mark_t mark)

    Advance iterator to next marked entry.

    :param xas:
        XArray operation state.
    :type xas: struct xa_state \*

    :param max:
        Highest index to return.
    :type max: unsigned long

    :param mark:
        Mark to search for.
    :type mark: xa_mark_t

.. _`xas_next_marked.description`:

Description
-----------

\ :c:func:`xas_next_marked`\  is an inline function to optimise xarray traversal for
speed.  It is equivalent to calling \ :c:func:`xas_find_marked`\ , and will call
\ :c:func:`xas_find_marked`\  for all the hard cases.

.. _`xas_next_marked.return`:

Return
------

The next marked entry after the one currently referred to by \ ``xas``\ .

.. _`xas_for_each`:

xas_for_each
============

.. c:function::  xas_for_each( xas,  entry,  max)

    Iterate over a range of an XArray.

    :param xas:
        XArray operation state.
    :type xas: 

    :param entry:
        Entry retrieved from the array.
    :type entry: 

    :param max:
        Maximum index to retrieve from array.
    :type max: 

.. _`xas_for_each.description`:

Description
-----------

The loop body will be executed for each entry present in the xarray
between the current xas position and \ ``max``\ .  \ ``entry``\  will be set to
the entry retrieved from the xarray.  It is safe to delete entries
from the array in the loop body.  You should hold either the RCU lock
or the xa_lock while iterating.  If you need to drop the lock, call
\ :c:func:`xas_pause`\  first.

.. _`xas_for_each_marked`:

xas_for_each_marked
===================

.. c:function::  xas_for_each_marked( xas,  entry,  max,  mark)

    Iterate over a range of an XArray.

    :param xas:
        XArray operation state.
    :type xas: 

    :param entry:
        Entry retrieved from the array.
    :type entry: 

    :param max:
        Maximum index to retrieve from array.
    :type max: 

    :param mark:
        Mark to search for.
    :type mark: 

.. _`xas_for_each_marked.description`:

Description
-----------

The loop body will be executed for each marked entry in the xarray
between the current xas position and \ ``max``\ .  \ ``entry``\  will be set to
the entry retrieved from the xarray.  It is safe to delete entries
from the array in the loop body.  You should hold either the RCU lock
or the xa_lock while iterating.  If you need to drop the lock, call
\ :c:func:`xas_pause`\  first.

.. _`xas_for_each_conflict`:

xas_for_each_conflict
=====================

.. c:function::  xas_for_each_conflict( xas,  entry)

    Iterate over a range of an XArray.

    :param xas:
        XArray operation state.
    :type xas: 

    :param entry:
        Entry retrieved from the array.
    :type entry: 

.. _`xas_for_each_conflict.description`:

Description
-----------

The loop body will be executed for each entry in the XArray that lies
within the range specified by \ ``xas``\ .  If the loop completes successfully,
any entries that lie in this range will be replaced by \ ``entry``\ .  The caller
may break out of the loop; if they do so, the contents of the XArray will
be unchanged.  The operation may fail due to an out of memory condition.
The caller may also call \ :c:func:`xa_set_err`\  to exit the loop while setting an
error to record the reason.

.. _`xas_prev`:

xas_prev
========

.. c:function:: void *xas_prev(struct xa_state *xas)

    Move iterator to previous index.

    :param xas:
        XArray operation state.
    :type xas: struct xa_state \*

.. _`xas_prev.description`:

Description
-----------

If the \ ``xas``\  was in an error state, it will remain in an error state
and this function will return \ ``NULL``\ .  If the \ ``xas``\  has never been walked,
it will have the effect of calling \ :c:func:`xas_load`\ .  Otherwise one will be
subtracted from the index and the state will be walked to the correct
location in the array for the next operation.

If the iterator was referencing index 0, this function wraps
around to \ ``ULONG_MAX``\ .

.. _`xas_prev.return`:

Return
------

The entry at the new index.  This may be \ ``NULL``\  or an internal
entry.

.. _`xas_next`:

xas_next
========

.. c:function:: void *xas_next(struct xa_state *xas)

    Move state to next index.

    :param xas:
        XArray operation state.
    :type xas: struct xa_state \*

.. _`xas_next.description`:

Description
-----------

If the \ ``xas``\  was in an error state, it will remain in an error state
and this function will return \ ``NULL``\ .  If the \ ``xas``\  has never been walked,
it will have the effect of calling \ :c:func:`xas_load`\ .  Otherwise one will be
added to the index and the state will be walked to the correct
location in the array for the next operation.

If the iterator was referencing index \ ``ULONG_MAX``\ , this function wraps
around to 0.

.. _`xas_next.return`:

Return
------

The entry at the new index.  This may be \ ``NULL``\  or an internal
entry.

.. This file was automatic generated / don't edit.


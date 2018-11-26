.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/idr.h

.. _`idr_init`:

IDR_INIT
========

.. c:function::  IDR_INIT( name)

    Initialise an IDR.

    :param name:
        Name of IDR.
    :type name: 

.. _`idr_init.description`:

Description
-----------

A freshly-initialised IDR contains no IDs.

.. _`define_idr`:

DEFINE_IDR
==========

.. c:function::  DEFINE_IDR( name)

    Define a statically-allocated IDR.

    :param name:
        Name of IDR.
    :type name: 

.. _`define_idr.description`:

Description
-----------

An IDR defined using this macro is ready for use with no additional
initialisation required.  It contains no IDs.

.. _`idr_get_cursor`:

idr_get_cursor
==============

.. c:function:: unsigned int idr_get_cursor(const struct idr *idr)

    Return the current position of the cyclic allocator

    :param idr:
        idr handle
    :type idr: const struct idr \*

.. _`idr_get_cursor.description`:

Description
-----------

The value returned is the value that will be next returned from
\ :c:func:`idr_alloc_cyclic`\  if it is free (otherwise the search will start from
this position).

.. _`idr_set_cursor`:

idr_set_cursor
==============

.. c:function:: void idr_set_cursor(struct idr *idr, unsigned int val)

    Set the current position of the cyclic allocator

    :param idr:
        idr handle
    :type idr: struct idr \*

    :param val:
        new position
    :type val: unsigned int

.. _`idr_set_cursor.description`:

Description
-----------

The next call to \ :c:func:`idr_alloc_cyclic`\  will return \ ``val``\  if it is free
(otherwise the search will start from this position).

.. _`idr-sync`:

idr sync
========

idr synchronization (stolen from radix-tree.h)

\ :c:func:`idr_find`\  is able to be called locklessly, using RCU. The caller must
ensure calls to this function are made within \ :c:func:`rcu_read_lock`\  regions.
Other readers (lock-free or otherwise) and modifications may be running
concurrently.

It is still required that the caller manage the synchronization and
lifetimes of the items. So if RCU lock-free lookups are used, typically
this would mean that the items have their own locks, or are amenable to
lock-free access; and that the items are freed by RCU (or only freed after
having been deleted from the idr tree *and* a \ :c:func:`synchronize_rcu`\  grace
period).

.. _`idr_init_base`:

idr_init_base
=============

.. c:function:: void idr_init_base(struct idr *idr, int base)

    Initialise an IDR.

    :param idr:
        IDR handle.
    :type idr: struct idr \*

    :param base:
        The base value for the IDR.
    :type base: int

.. _`idr_init_base.description`:

Description
-----------

This variation of \ :c:func:`idr_init`\  creates an IDR which will allocate IDs
starting at \ ``base``\ .

.. _`idr_init`:

idr_init
========

.. c:function:: void idr_init(struct idr *idr)

    Initialise an IDR.

    :param idr:
        IDR handle.
    :type idr: struct idr \*

.. _`idr_init.description`:

Description
-----------

Initialise a dynamically allocated IDR.  To initialise a
statically allocated IDR, use \ :c:func:`DEFINE_IDR`\ .

.. _`idr_is_empty`:

idr_is_empty
============

.. c:function:: bool idr_is_empty(const struct idr *idr)

    Are there any IDs allocated?

    :param idr:
        IDR handle.
    :type idr: const struct idr \*

.. _`idr_is_empty.return`:

Return
------

\ ``true``\  if any IDs have been allocated from this IDR.

.. _`idr_preload_end`:

idr_preload_end
===============

.. c:function:: void idr_preload_end( void)

    end preload section started with \ :c:func:`idr_preload`\ 

    :param void:
        no arguments
    :type void: 

.. _`idr_preload_end.description`:

Description
-----------

Each \ :c:func:`idr_preload`\  should be matched with an invocation of this
function.  See \ :c:func:`idr_preload`\  for details.

.. _`idr_for_each_entry`:

idr_for_each_entry
==================

.. c:function::  idr_for_each_entry( idr,  entry,  id)

    Iterate over an IDR's elements of a given type.

    :param idr:
        IDR handle.
    :type idr: 

    :param entry:
        The type * to use as cursor
    :type entry: 

    :param id:
        Entry ID.
    :type id: 

.. _`idr_for_each_entry.description`:

Description
-----------

\ ``entry``\  and \ ``id``\  do not need to be initialized before the loop, and
after normal termination \ ``entry``\  is left with the value NULL.  This
is convenient for a "not found" value.

.. _`idr_for_each_entry_ul`:

idr_for_each_entry_ul
=====================

.. c:function::  idr_for_each_entry_ul( idr,  entry,  id)

    Iterate over an IDR's elements of a given type.

    :param idr:
        IDR handle.
    :type idr: 

    :param entry:
        The type * to use as cursor.
    :type entry: 

    :param id:
        Entry ID.
    :type id: 

.. _`idr_for_each_entry_ul.description`:

Description
-----------

\ ``entry``\  and \ ``id``\  do not need to be initialized before the loop, and
after normal termination \ ``entry``\  is left with the value NULL.  This
is convenient for a "not found" value.

.. _`idr_for_each_entry_continue`:

idr_for_each_entry_continue
===========================

.. c:function::  idr_for_each_entry_continue( idr,  entry,  id)

    Continue iteration over an IDR's elements of a given type

    :param idr:
        IDR handle.
    :type idr: 

    :param entry:
        The type * to use as a cursor.
    :type entry: 

    :param id:
        Entry ID.
    :type id: 

.. _`idr_for_each_entry_continue.description`:

Description
-----------

Continue to iterate over entries, continuing after the current position.

.. _`ida_alloc`:

ida_alloc
=========

.. c:function:: int ida_alloc(struct ida *ida, gfp_t gfp)

    Allocate an unused ID.

    :param ida:
        IDA handle.
    :type ida: struct ida \*

    :param gfp:
        Memory allocation flags.
    :type gfp: gfp_t

.. _`ida_alloc.description`:

Description
-----------

Allocate an ID between 0 and \ ``INT_MAX``\ , inclusive.

.. _`ida_alloc.context`:

Context
-------

Any context.

.. _`ida_alloc.return`:

Return
------

The allocated ID, or \ ``-ENOMEM``\  if memory could not be allocated,
or \ ``-ENOSPC``\  if there are no free IDs.

.. _`ida_alloc_min`:

ida_alloc_min
=============

.. c:function:: int ida_alloc_min(struct ida *ida, unsigned int min, gfp_t gfp)

    Allocate an unused ID.

    :param ida:
        IDA handle.
    :type ida: struct ida \*

    :param min:
        Lowest ID to allocate.
    :type min: unsigned int

    :param gfp:
        Memory allocation flags.
    :type gfp: gfp_t

.. _`ida_alloc_min.description`:

Description
-----------

Allocate an ID between \ ``min``\  and \ ``INT_MAX``\ , inclusive.

.. _`ida_alloc_min.context`:

Context
-------

Any context.

.. _`ida_alloc_min.return`:

Return
------

The allocated ID, or \ ``-ENOMEM``\  if memory could not be allocated,
or \ ``-ENOSPC``\  if there are no free IDs.

.. _`ida_alloc_max`:

ida_alloc_max
=============

.. c:function:: int ida_alloc_max(struct ida *ida, unsigned int max, gfp_t gfp)

    Allocate an unused ID.

    :param ida:
        IDA handle.
    :type ida: struct ida \*

    :param max:
        Highest ID to allocate.
    :type max: unsigned int

    :param gfp:
        Memory allocation flags.
    :type gfp: gfp_t

.. _`ida_alloc_max.description`:

Description
-----------

Allocate an ID between 0 and \ ``max``\ , inclusive.

.. _`ida_alloc_max.context`:

Context
-------

Any context.

.. _`ida_alloc_max.return`:

Return
------

The allocated ID, or \ ``-ENOMEM``\  if memory could not be allocated,
or \ ``-ENOSPC``\  if there are no free IDs.

.. This file was automatic generated / don't edit.


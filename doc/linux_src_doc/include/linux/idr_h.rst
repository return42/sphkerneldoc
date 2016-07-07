.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/idr.h

.. _`idr_preload_end`:

idr_preload_end
===============

.. c:function:: void idr_preload_end( void)

    end preload section started with \ :c:func:`idr_preload`\ 

    :param  void:
        no arguments

.. _`idr_preload_end.description`:

Description
-----------

Each \ :c:func:`idr_preload`\  should be matched with an invocation of this
function.  See \ :c:func:`idr_preload`\  for details.

.. _`idr_find`:

idr_find
========

.. c:function:: void *idr_find(struct idr *idr, int id)

    return pointer for given id

    :param struct idr \*idr:
        idr handle

    :param int id:
        lookup key

.. _`idr_find.description`:

Description
-----------

Return the pointer given the id it has been registered with.  A \ ``NULL``\ 
return indicates that \ ``id``\  is not valid or you passed \ ``NULL``\  in
\ :c:func:`idr_get_new`\ .

This function can be called under \ :c:func:`rcu_read_lock`\ , given that the leaf
pointers lifetimes are correctly managed.

.. _`idr_for_each_entry`:

idr_for_each_entry
==================

.. c:function::  idr_for_each_entry( idp,  entry,  id)

    iterate over an idr's elements of a given type

    :param  idp:
        idr handle

    :param  entry:
        the type \* to use as cursor

    :param  id:
        id entry's key

.. _`idr_for_each_entry.description`:

Description
-----------

\ ``entry``\  and \ ``id``\  do not need to be initialized before the loop, and
after normal terminatinon \ ``entry``\  is left with the value NULL.  This
is convenient for a "not found" value.

.. _`idr_for_each_entry_continue`:

idr_for_each_entry_continue
===========================

.. c:function::  idr_for_each_entry_continue( idp,  entry,  id)

    continue iteration over an idr's elements of a given type

    :param  idp:
        idr handle

    :param  entry:
        the type \* to use as cursor

    :param  id:
        id entry's key

.. _`idr_for_each_entry_continue.description`:

Description
-----------

Continue to iterate over list of given type, continuing after
the current position.

.. _`ida_get_new`:

ida_get_new
===========

.. c:function:: int ida_get_new(struct ida *ida, int *p_id)

    allocate new ID

    :param struct ida \*ida:
        idr handle

    :param int \*p_id:
        pointer to the allocated handle

.. _`ida_get_new.description`:

Description
-----------

Simple wrapper around \ :c:func:`ida_get_new_above`\  w/ \ ``starting_id``\  of zero.

.. This file was automatic generated / don't edit.


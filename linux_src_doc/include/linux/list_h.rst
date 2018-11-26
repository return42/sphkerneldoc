.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/list.h

.. _`list_add`:

list_add
========

.. c:function:: void list_add(struct list_head *new, struct list_head *head)

    add a new entry

    :param new:
        new entry to be added
    :type new: struct list_head \*

    :param head:
        list head to add it after
    :type head: struct list_head \*

.. _`list_add.description`:

Description
-----------

Insert a new entry after the specified head.
This is good for implementing stacks.

.. _`list_add_tail`:

list_add_tail
=============

.. c:function:: void list_add_tail(struct list_head *new, struct list_head *head)

    add a new entry

    :param new:
        new entry to be added
    :type new: struct list_head \*

    :param head:
        list head to add it before
    :type head: struct list_head \*

.. _`list_add_tail.description`:

Description
-----------

Insert a new entry before the specified head.
This is useful for implementing queues.

.. _`__list_del_entry`:

__list_del_entry
================

.. c:function:: void __list_del_entry(struct list_head *entry)

    deletes entry from list.

    :param entry:
        the element to delete from the list.
        Note: \ :c:func:`list_empty`\  on entry does not return true after this, the entry is
        in an undefined state.
    :type entry: struct list_head \*

.. _`list_replace`:

list_replace
============

.. c:function:: void list_replace(struct list_head *old, struct list_head *new)

    replace old entry by new one

    :param old:
        the element to be replaced
    :type old: struct list_head \*

    :param new:
        the new element to insert
    :type new: struct list_head \*

.. _`list_replace.description`:

Description
-----------

If \ ``old``\  was empty, it will be overwritten.

.. _`list_del_init`:

list_del_init
=============

.. c:function:: void list_del_init(struct list_head *entry)

    deletes entry from list and reinitialize it.

    :param entry:
        the element to delete from the list.
    :type entry: struct list_head \*

.. _`list_move`:

list_move
=========

.. c:function:: void list_move(struct list_head *list, struct list_head *head)

    delete from one list and add as another's head

    :param list:
        the entry to move
    :type list: struct list_head \*

    :param head:
        the head that will precede our entry
    :type head: struct list_head \*

.. _`list_move_tail`:

list_move_tail
==============

.. c:function:: void list_move_tail(struct list_head *list, struct list_head *head)

    delete from one list and add as another's tail

    :param list:
        the entry to move
    :type list: struct list_head \*

    :param head:
        the head that will follow our entry
    :type head: struct list_head \*

.. _`list_bulk_move_tail`:

list_bulk_move_tail
===================

.. c:function:: void list_bulk_move_tail(struct list_head *head, struct list_head *first, struct list_head *last)

    move a subsection of a list to its tail

    :param head:
        the head that will follow our entry
    :type head: struct list_head \*

    :param first:
        first entry to move
    :type first: struct list_head \*

    :param last:
        last entry to move, can be the same as first
    :type last: struct list_head \*

.. _`list_bulk_move_tail.description`:

Description
-----------

Move all entries between \ ``first``\  and including \ ``last``\  before \ ``head``\ .
All three entries must belong to the same linked list.

.. _`list_is_last`:

list_is_last
============

.. c:function:: int list_is_last(const struct list_head *list, const struct list_head *head)

    tests whether \ ``list``\  is the last entry in list \ ``head``\ 

    :param list:
        the entry to test
    :type list: const struct list_head \*

    :param head:
        the head of the list
    :type head: const struct list_head \*

.. _`list_empty`:

list_empty
==========

.. c:function:: int list_empty(const struct list_head *head)

    tests whether a list is empty

    :param head:
        the list to test.
    :type head: const struct list_head \*

.. _`list_empty_careful`:

list_empty_careful
==================

.. c:function:: int list_empty_careful(const struct list_head *head)

    tests whether a list is empty and not being modified

    :param head:
        the list to test
    :type head: const struct list_head \*

.. _`list_empty_careful.description`:

Description
-----------

tests whether a list is empty _and_ checks that no other CPU might be
in the process of modifying either member (next or prev)

.. _`list_empty_careful.note`:

NOTE
----

using \ :c:func:`list_empty_careful`\  without synchronization
can only be safe if the only activity that can happen
to the list entry is \ :c:func:`list_del_init`\ . Eg. it cannot be used
if another CPU could re-list_add() it.

.. _`list_rotate_left`:

list_rotate_left
================

.. c:function:: void list_rotate_left(struct list_head *head)

    rotate the list to the left

    :param head:
        the head of the list
    :type head: struct list_head \*

.. _`list_is_singular`:

list_is_singular
================

.. c:function:: int list_is_singular(const struct list_head *head)

    tests whether a list has just one entry.

    :param head:
        the list to test.
    :type head: const struct list_head \*

.. _`list_cut_position`:

list_cut_position
=================

.. c:function:: void list_cut_position(struct list_head *list, struct list_head *head, struct list_head *entry)

    cut a list into two

    :param list:
        a new list to add all removed entries
    :type list: struct list_head \*

    :param head:
        a list with entries
    :type head: struct list_head \*

    :param entry:
        an entry within head, could be the head itself
        and if so we won't cut the list
    :type entry: struct list_head \*

.. _`list_cut_position.description`:

Description
-----------

This helper moves the initial part of \ ``head``\ , up to and
including \ ``entry``\ , from \ ``head``\  to \ ``list``\ . You should
pass on \ ``entry``\  an element you know is on \ ``head``\ . \ ``list``\ 
should be an empty list or a list you do not care about
losing its data.

.. _`list_cut_before`:

list_cut_before
===============

.. c:function:: void list_cut_before(struct list_head *list, struct list_head *head, struct list_head *entry)

    cut a list into two, before given entry

    :param list:
        a new list to add all removed entries
    :type list: struct list_head \*

    :param head:
        a list with entries
    :type head: struct list_head \*

    :param entry:
        an entry within head, could be the head itself
    :type entry: struct list_head \*

.. _`list_cut_before.description`:

Description
-----------

This helper moves the initial part of \ ``head``\ , up to but
excluding \ ``entry``\ , from \ ``head``\  to \ ``list``\ .  You should pass
in \ ``entry``\  an element you know is on \ ``head``\ .  \ ``list``\  should
be an empty list or a list you do not care about losing
its data.
If \ ``entry``\  == \ ``head``\ , all entries on \ ``head``\  are moved to
\ ``list``\ .

.. _`list_splice`:

list_splice
===========

.. c:function:: void list_splice(const struct list_head *list, struct list_head *head)

    join two lists, this is designed for stacks

    :param list:
        the new list to add.
    :type list: const struct list_head \*

    :param head:
        the place to add it in the first list.
    :type head: struct list_head \*

.. _`list_splice_tail`:

list_splice_tail
================

.. c:function:: void list_splice_tail(struct list_head *list, struct list_head *head)

    join two lists, each list being a queue

    :param list:
        the new list to add.
    :type list: struct list_head \*

    :param head:
        the place to add it in the first list.
    :type head: struct list_head \*

.. _`list_splice_init`:

list_splice_init
================

.. c:function:: void list_splice_init(struct list_head *list, struct list_head *head)

    join two lists and reinitialise the emptied list.

    :param list:
        the new list to add.
    :type list: struct list_head \*

    :param head:
        the place to add it in the first list.
    :type head: struct list_head \*

.. _`list_splice_init.description`:

Description
-----------

The list at \ ``list``\  is reinitialised

.. _`list_splice_tail_init`:

list_splice_tail_init
=====================

.. c:function:: void list_splice_tail_init(struct list_head *list, struct list_head *head)

    join two lists and reinitialise the emptied list

    :param list:
        the new list to add.
    :type list: struct list_head \*

    :param head:
        the place to add it in the first list.
    :type head: struct list_head \*

.. _`list_splice_tail_init.description`:

Description
-----------

Each of the lists is a queue.
The list at \ ``list``\  is reinitialised

.. _`list_entry`:

list_entry
==========

.. c:function::  list_entry( ptr,  type,  member)

    get the struct for this entry

    :param ptr:
        the \ :c:type:`struct list_head <list_head>`\  pointer.
    :type ptr: 

    :param type:
        the type of the struct this is embedded in.
    :type type: 

    :param member:
        the name of the list_head within the struct.
    :type member: 

.. _`list_first_entry`:

list_first_entry
================

.. c:function::  list_first_entry( ptr,  type,  member)

    get the first element from a list

    :param ptr:
        the list head to take the element from.
    :type ptr: 

    :param type:
        the type of the struct this is embedded in.
    :type type: 

    :param member:
        the name of the list_head within the struct.
    :type member: 

.. _`list_first_entry.description`:

Description
-----------

Note, that list is expected to be not empty.

.. _`list_last_entry`:

list_last_entry
===============

.. c:function::  list_last_entry( ptr,  type,  member)

    get the last element from a list

    :param ptr:
        the list head to take the element from.
    :type ptr: 

    :param type:
        the type of the struct this is embedded in.
    :type type: 

    :param member:
        the name of the list_head within the struct.
    :type member: 

.. _`list_last_entry.description`:

Description
-----------

Note, that list is expected to be not empty.

.. _`list_first_entry_or_null`:

list_first_entry_or_null
========================

.. c:function::  list_first_entry_or_null( ptr,  type,  member)

    get the first element from a list

    :param ptr:
        the list head to take the element from.
    :type ptr: 

    :param type:
        the type of the struct this is embedded in.
    :type type: 

    :param member:
        the name of the list_head within the struct.
    :type member: 

.. _`list_first_entry_or_null.description`:

Description
-----------

Note that if the list is empty, it returns NULL.

.. _`list_next_entry`:

list_next_entry
===============

.. c:function::  list_next_entry( pos,  member)

    get the next element in list

    :param pos:
        the type * to cursor
    :type pos: 

    :param member:
        the name of the list_head within the struct.
    :type member: 

.. _`list_prev_entry`:

list_prev_entry
===============

.. c:function::  list_prev_entry( pos,  member)

    get the prev element in list

    :param pos:
        the type * to cursor
    :type pos: 

    :param member:
        the name of the list_head within the struct.
    :type member: 

.. _`list_for_each`:

list_for_each
=============

.. c:function::  list_for_each( pos,  head)

    iterate over a list

    :param pos:
        the \ :c:type:`struct list_head <list_head>`\  to use as a loop cursor.
    :type pos: 

    :param head:
        the head for your list.
    :type head: 

.. _`list_for_each_prev`:

list_for_each_prev
==================

.. c:function::  list_for_each_prev( pos,  head)

    iterate over a list backwards

    :param pos:
        the \ :c:type:`struct list_head <list_head>`\  to use as a loop cursor.
    :type pos: 

    :param head:
        the head for your list.
    :type head: 

.. _`list_for_each_safe`:

list_for_each_safe
==================

.. c:function::  list_for_each_safe( pos,  n,  head)

    iterate over a list safe against removal of list entry

    :param pos:
        the \ :c:type:`struct list_head <list_head>`\  to use as a loop cursor.
    :type pos: 

    :param n:
        another \ :c:type:`struct list_head <list_head>`\  to use as temporary storage
    :type n: 

    :param head:
        the head for your list.
    :type head: 

.. _`list_for_each_prev_safe`:

list_for_each_prev_safe
=======================

.. c:function::  list_for_each_prev_safe( pos,  n,  head)

    iterate over a list backwards safe against removal of list entry

    :param pos:
        the \ :c:type:`struct list_head <list_head>`\  to use as a loop cursor.
    :type pos: 

    :param n:
        another \ :c:type:`struct list_head <list_head>`\  to use as temporary storage
    :type n: 

    :param head:
        the head for your list.
    :type head: 

.. _`list_for_each_entry`:

list_for_each_entry
===================

.. c:function::  list_for_each_entry( pos,  head,  member)

    iterate over list of given type

    :param pos:
        the type * to use as a loop cursor.
    :type pos: 

    :param head:
        the head for your list.
    :type head: 

    :param member:
        the name of the list_head within the struct.
    :type member: 

.. _`list_for_each_entry_reverse`:

list_for_each_entry_reverse
===========================

.. c:function::  list_for_each_entry_reverse( pos,  head,  member)

    iterate backwards over list of given type.

    :param pos:
        the type * to use as a loop cursor.
    :type pos: 

    :param head:
        the head for your list.
    :type head: 

    :param member:
        the name of the list_head within the struct.
    :type member: 

.. _`list_prepare_entry`:

list_prepare_entry
==================

.. c:function::  list_prepare_entry( pos,  head,  member)

    prepare a pos entry for use in \ :c:func:`list_for_each_entry_continue`\ 

    :param pos:
        the type * to use as a start point
    :type pos: 

    :param head:
        the head of the list
    :type head: 

    :param member:
        the name of the list_head within the struct.
    :type member: 

.. _`list_prepare_entry.description`:

Description
-----------

Prepares a pos entry for use as a start point in \ :c:func:`list_for_each_entry_continue`\ .

.. _`list_for_each_entry_continue`:

list_for_each_entry_continue
============================

.. c:function::  list_for_each_entry_continue( pos,  head,  member)

    continue iteration over list of given type

    :param pos:
        the type * to use as a loop cursor.
    :type pos: 

    :param head:
        the head for your list.
    :type head: 

    :param member:
        the name of the list_head within the struct.
    :type member: 

.. _`list_for_each_entry_continue.description`:

Description
-----------

Continue to iterate over list of given type, continuing after
the current position.

.. _`list_for_each_entry_continue_reverse`:

list_for_each_entry_continue_reverse
====================================

.. c:function::  list_for_each_entry_continue_reverse( pos,  head,  member)

    iterate backwards from the given point

    :param pos:
        the type * to use as a loop cursor.
    :type pos: 

    :param head:
        the head for your list.
    :type head: 

    :param member:
        the name of the list_head within the struct.
    :type member: 

.. _`list_for_each_entry_continue_reverse.description`:

Description
-----------

Start to iterate over list of given type backwards, continuing after
the current position.

.. _`list_for_each_entry_from`:

list_for_each_entry_from
========================

.. c:function::  list_for_each_entry_from( pos,  head,  member)

    iterate over list of given type from the current point

    :param pos:
        the type * to use as a loop cursor.
    :type pos: 

    :param head:
        the head for your list.
    :type head: 

    :param member:
        the name of the list_head within the struct.
    :type member: 

.. _`list_for_each_entry_from.description`:

Description
-----------

Iterate over list of given type, continuing from current position.

.. _`list_for_each_entry_from_reverse`:

list_for_each_entry_from_reverse
================================

.. c:function::  list_for_each_entry_from_reverse( pos,  head,  member)

    iterate backwards over list of given type from the current point

    :param pos:
        the type * to use as a loop cursor.
    :type pos: 

    :param head:
        the head for your list.
    :type head: 

    :param member:
        the name of the list_head within the struct.
    :type member: 

.. _`list_for_each_entry_from_reverse.description`:

Description
-----------

Iterate backwards over list of given type, continuing from current position.

.. _`list_for_each_entry_safe`:

list_for_each_entry_safe
========================

.. c:function::  list_for_each_entry_safe( pos,  n,  head,  member)

    iterate over list of given type safe against removal of list entry

    :param pos:
        the type * to use as a loop cursor.
    :type pos: 

    :param n:
        another type * to use as temporary storage
    :type n: 

    :param head:
        the head for your list.
    :type head: 

    :param member:
        the name of the list_head within the struct.
    :type member: 

.. _`list_for_each_entry_safe_continue`:

list_for_each_entry_safe_continue
=================================

.. c:function::  list_for_each_entry_safe_continue( pos,  n,  head,  member)

    continue list iteration safe against removal

    :param pos:
        the type * to use as a loop cursor.
    :type pos: 

    :param n:
        another type * to use as temporary storage
    :type n: 

    :param head:
        the head for your list.
    :type head: 

    :param member:
        the name of the list_head within the struct.
    :type member: 

.. _`list_for_each_entry_safe_continue.description`:

Description
-----------

Iterate over list of given type, continuing after current point,
safe against removal of list entry.

.. _`list_for_each_entry_safe_from`:

list_for_each_entry_safe_from
=============================

.. c:function::  list_for_each_entry_safe_from( pos,  n,  head,  member)

    iterate over list from current point safe against removal

    :param pos:
        the type * to use as a loop cursor.
    :type pos: 

    :param n:
        another type * to use as temporary storage
    :type n: 

    :param head:
        the head for your list.
    :type head: 

    :param member:
        the name of the list_head within the struct.
    :type member: 

.. _`list_for_each_entry_safe_from.description`:

Description
-----------

Iterate over list of given type from current point, safe against
removal of list entry.

.. _`list_for_each_entry_safe_reverse`:

list_for_each_entry_safe_reverse
================================

.. c:function::  list_for_each_entry_safe_reverse( pos,  n,  head,  member)

    iterate backwards over list safe against removal

    :param pos:
        the type * to use as a loop cursor.
    :type pos: 

    :param n:
        another type * to use as temporary storage
    :type n: 

    :param head:
        the head for your list.
    :type head: 

    :param member:
        the name of the list_head within the struct.
    :type member: 

.. _`list_for_each_entry_safe_reverse.description`:

Description
-----------

Iterate backwards over list of given type, safe against removal
of list entry.

.. _`list_safe_reset_next`:

list_safe_reset_next
====================

.. c:function::  list_safe_reset_next( pos,  n,  member)

    reset a stale list_for_each_entry_safe loop

    :param pos:
        the loop cursor used in the list_for_each_entry_safe loop
    :type pos: 

    :param n:
        temporary storage used in list_for_each_entry_safe
    :type n: 

    :param member:
        the name of the list_head within the struct.
    :type member: 

.. _`list_safe_reset_next.description`:

Description
-----------

list_safe_reset_next is not safe to use in general if the list may be
modified concurrently (eg. the lock is dropped in the loop body). An
exception to this is if the cursor element (pos) is pinned in the list,
and list_safe_reset_next is called after re-taking the lock and before
completing the current iteration of the loop body.

.. _`hlist_for_each_entry`:

hlist_for_each_entry
====================

.. c:function::  hlist_for_each_entry( pos,  head,  member)

    iterate over list of given type

    :param pos:
        the type * to use as a loop cursor.
    :type pos: 

    :param head:
        the head for your list.
    :type head: 

    :param member:
        the name of the hlist_node within the struct.
    :type member: 

.. _`hlist_for_each_entry_continue`:

hlist_for_each_entry_continue
=============================

.. c:function::  hlist_for_each_entry_continue( pos,  member)

    iterate over a hlist continuing after current point

    :param pos:
        the type * to use as a loop cursor.
    :type pos: 

    :param member:
        the name of the hlist_node within the struct.
    :type member: 

.. _`hlist_for_each_entry_from`:

hlist_for_each_entry_from
=========================

.. c:function::  hlist_for_each_entry_from( pos,  member)

    iterate over a hlist continuing from current point

    :param pos:
        the type * to use as a loop cursor.
    :type pos: 

    :param member:
        the name of the hlist_node within the struct.
    :type member: 

.. _`hlist_for_each_entry_safe`:

hlist_for_each_entry_safe
=========================

.. c:function::  hlist_for_each_entry_safe( pos,  n,  head,  member)

    iterate over list of given type safe against removal of list entry

    :param pos:
        the type * to use as a loop cursor.
    :type pos: 

    :param n:
        another \ :c:type:`struct hlist_node <hlist_node>`\  to use as temporary storage
    :type n: 

    :param head:
        the head for your list.
    :type head: 

    :param member:
        the name of the hlist_node within the struct.
    :type member: 

.. This file was automatic generated / don't edit.


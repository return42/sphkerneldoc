.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/mkregtable.c

.. _`container_of`:

container_of
============

.. c:function::  container_of( ptr,  type,  member)

    cast a member of a structure out to the containing structure

    :param  ptr:
        the pointer to the member.

    :param  type:
        the type of the container struct this is embedded in.

    :param  member:
        the name of the member within the struct.

.. _`list_add`:

list_add
========

.. c:function:: void list_add(struct list_head *new, struct list_head *head)

    add a new entry

    :param struct list_head \*new:
        new entry to be added

    :param struct list_head \*head:
        list head to add it after

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

    :param struct list_head \*new:
        new entry to be added

    :param struct list_head \*head:
        list head to add it before

.. _`list_add_tail.description`:

Description
-----------

Insert a new entry before the specified head.
This is useful for implementing queues.

.. _`list_del`:

list_del
========

.. c:function:: void list_del(struct list_head *entry)

    deletes entry from list.

    :param struct list_head \*entry:
        the element to delete from the list.

.. _`list_del.note`:

Note
----

\ :c:func:`list_empty`\  on entry does not return true after this, the entry is
in an undefined state.

.. _`list_replace`:

list_replace
============

.. c:function:: void list_replace(struct list_head *old, struct list_head *new)

    replace old entry by new one

    :param struct list_head \*old:
        the element to be replaced

    :param struct list_head \*new:
        the new element to insert

.. _`list_replace.description`:

Description
-----------

If \ ``old``\  was empty, it will be overwritten.

.. _`list_del_init`:

list_del_init
=============

.. c:function:: void list_del_init(struct list_head *entry)

    deletes entry from list and reinitialize it.

    :param struct list_head \*entry:
        the element to delete from the list.

.. _`list_move`:

list_move
=========

.. c:function:: void list_move(struct list_head *list, struct list_head *head)

    delete from one list and add as another's head

    :param struct list_head \*list:
        the entry to move

    :param struct list_head \*head:
        the head that will precede our entry

.. _`list_move_tail`:

list_move_tail
==============

.. c:function:: void list_move_tail(struct list_head *list, struct list_head *head)

    delete from one list and add as another's tail

    :param struct list_head \*list:
        the entry to move

    :param struct list_head \*head:
        the head that will follow our entry

.. _`list_is_last`:

list_is_last
============

.. c:function:: int list_is_last(const struct list_head *list, const struct list_head *head)

    tests whether \ ``list``\  is the last entry in list \ ``head``\ 

    :param const struct list_head \*list:
        the entry to test

    :param const struct list_head \*head:
        the head of the list

.. _`list_empty`:

list_empty
==========

.. c:function:: int list_empty(const struct list_head *head)

    tests whether a list is empty

    :param const struct list_head \*head:
        the list to test.

.. _`list_empty_careful`:

list_empty_careful
==================

.. c:function:: int list_empty_careful(const struct list_head *head)

    tests whether a list is empty and not being modified

    :param const struct list_head \*head:
        the list to test

.. _`list_empty_careful.description`:

Description
-----------

tests whether a list is empty \_and\_ checks that no other CPU might be
in the process of modifying either member (next or prev)

.. _`list_empty_careful.note`:

NOTE
----

using \ :c:func:`list_empty_careful`\  without synchronization
can only be safe if the only activity that can happen
to the list entry is \ :c:func:`list_del_init`\ . Eg. it cannot be used
if another CPU could re-\ :c:func:`list_add`\  it.

.. _`list_is_singular`:

list_is_singular
================

.. c:function:: int list_is_singular(const struct list_head *head)

    tests whether a list has just one entry.

    :param const struct list_head \*head:
        the list to test.

.. _`list_cut_position`:

list_cut_position
=================

.. c:function:: void list_cut_position(struct list_head *list, struct list_head *head, struct list_head *entry)

    cut a list into two

    :param struct list_head \*list:
        a new list to add all removed entries

    :param struct list_head \*head:
        a list with entries

    :param struct list_head \*entry:
        an entry within head, could be the head itself
        and if so we won't cut the list

.. _`list_cut_position.description`:

Description
-----------

This helper moves the initial part of \ ``head``\ , up to and
including \ ``entry``\ , from \ ``head``\  to \ ``list``\ . You should
pass on \ ``entry``\  an element you know is on \ ``head``\ . \ ``list``\ 
should be an empty list or a list you do not care about
losing its data.

.. _`list_splice`:

list_splice
===========

.. c:function:: void list_splice(const struct list_head *list, struct list_head *head)

    join two lists, this is designed for stacks

    :param const struct list_head \*list:
        the new list to add.

    :param struct list_head \*head:
        the place to add it in the first list.

.. _`list_splice_tail`:

list_splice_tail
================

.. c:function:: void list_splice_tail(struct list_head *list, struct list_head *head)

    join two lists, each list being a queue

    :param struct list_head \*list:
        the new list to add.

    :param struct list_head \*head:
        the place to add it in the first list.

.. _`list_splice_init`:

list_splice_init
================

.. c:function:: void list_splice_init(struct list_head *list, struct list_head *head)

    join two lists and reinitialise the emptied list.

    :param struct list_head \*list:
        the new list to add.

    :param struct list_head \*head:
        the place to add it in the first list.

.. _`list_splice_init.description`:

Description
-----------

The list at \ ``list``\  is reinitialised

.. _`list_splice_tail_init`:

list_splice_tail_init
=====================

.. c:function:: void list_splice_tail_init(struct list_head *list, struct list_head *head)

    join two lists and reinitialise the emptied list

    :param struct list_head \*list:
        the new list to add.

    :param struct list_head \*head:
        the place to add it in the first list.

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

    :param  ptr:
        the \ :c:type:`struct list_head <list_head>`\  pointer.

    :param  type:
        the type of the struct this is embedded in.

    :param  member:
        the name of the list_head within the struct.

.. _`list_first_entry`:

list_first_entry
================

.. c:function::  list_first_entry( ptr,  type,  member)

    get the first element from a list

    :param  ptr:
        the list head to take the element from.

    :param  type:
        the type of the struct this is embedded in.

    :param  member:
        the name of the list_head within the struct.

.. _`list_first_entry.description`:

Description
-----------

Note, that list is expected to be not empty.

.. _`list_for_each`:

list_for_each
=============

.. c:function::  list_for_each( pos,  head)

    iterate over a list

    :param  pos:
        the \ :c:type:`struct list_head <list_head>`\  to use as a loop cursor.

    :param  head:
        the head for your list.

.. _`list_for_each_prev`:

list_for_each_prev
==================

.. c:function::  list_for_each_prev( pos,  head)

    iterate over a list backwards

    :param  pos:
        the \ :c:type:`struct list_head <list_head>`\  to use as a loop cursor.

    :param  head:
        the head for your list.

.. _`list_for_each_safe`:

list_for_each_safe
==================

.. c:function::  list_for_each_safe( pos,  n,  head)

    iterate over a list safe against removal of list entry

    :param  pos:
        the \ :c:type:`struct list_head <list_head>`\  to use as a loop cursor.

    :param  n:
        another \ :c:type:`struct list_head <list_head>`\  to use as temporary storage

    :param  head:
        the head for your list.

.. _`list_for_each_prev_safe`:

list_for_each_prev_safe
=======================

.. c:function::  list_for_each_prev_safe( pos,  n,  head)

    iterate over a list backwards safe against removal of list entry

    :param  pos:
        the \ :c:type:`struct list_head <list_head>`\  to use as a loop cursor.

    :param  n:
        another \ :c:type:`struct list_head <list_head>`\  to use as temporary storage

    :param  head:
        the head for your list.

.. _`list_for_each_entry`:

list_for_each_entry
===================

.. c:function::  list_for_each_entry( pos,  head,  member)

    iterate over list of given type

    :param  pos:
        the type \* to use as a loop cursor.

    :param  head:
        the head for your list.

    :param  member:
        the name of the list_head within the struct.

.. _`list_for_each_entry_reverse`:

list_for_each_entry_reverse
===========================

.. c:function::  list_for_each_entry_reverse( pos,  head,  member)

    iterate backwards over list of given type.

    :param  pos:
        the type \* to use as a loop cursor.

    :param  head:
        the head for your list.

    :param  member:
        the name of the list_head within the struct.

.. _`list_prepare_entry`:

list_prepare_entry
==================

.. c:function::  list_prepare_entry( pos,  head,  member)

    prepare a pos entry for use in \ :c:func:`list_for_each_entry_continue`\ 

    :param  pos:
        the type \* to use as a start point

    :param  head:
        the head of the list

    :param  member:
        the name of the list_head within the struct.

.. _`list_prepare_entry.description`:

Description
-----------

Prepares a pos entry for use as a start point in \ :c:func:`list_for_each_entry_continue`\ .

.. _`list_for_each_entry_continue`:

list_for_each_entry_continue
============================

.. c:function::  list_for_each_entry_continue( pos,  head,  member)

    continue iteration over list of given type

    :param  pos:
        the type \* to use as a loop cursor.

    :param  head:
        the head for your list.

    :param  member:
        the name of the list_head within the struct.

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

    :param  pos:
        the type \* to use as a loop cursor.

    :param  head:
        the head for your list.

    :param  member:
        the name of the list_head within the struct.

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

    :param  pos:
        the type \* to use as a loop cursor.

    :param  head:
        the head for your list.

    :param  member:
        the name of the list_head within the struct.

.. _`list_for_each_entry_from.description`:

Description
-----------

Iterate over list of given type, continuing from current position.

.. _`list_for_each_entry_safe`:

list_for_each_entry_safe
========================

.. c:function::  list_for_each_entry_safe( pos,  n,  head,  member)

    iterate over list of given type safe against removal of list entry

    :param  pos:
        the type \* to use as a loop cursor.

    :param  n:
        another type \* to use as temporary storage

    :param  head:
        the head for your list.

    :param  member:
        the name of the list_head within the struct.

.. _`list_for_each_entry_safe_continue`:

list_for_each_entry_safe_continue
=================================

.. c:function::  list_for_each_entry_safe_continue( pos,  n,  head,  member)

    :param  pos:
        the type \* to use as a loop cursor.

    :param  n:
        another type \* to use as temporary storage

    :param  head:
        the head for your list.

    :param  member:
        the name of the list_head within the struct.

.. _`list_for_each_entry_safe_continue.description`:

Description
-----------

Iterate over list of given type, continuing after current point,
safe against removal of list entry.

.. _`list_for_each_entry_safe_from`:

list_for_each_entry_safe_from
=============================

.. c:function::  list_for_each_entry_safe_from( pos,  n,  head,  member)

    :param  pos:
        the type \* to use as a loop cursor.

    :param  n:
        another type \* to use as temporary storage

    :param  head:
        the head for your list.

    :param  member:
        the name of the list_head within the struct.

.. _`list_for_each_entry_safe_from.description`:

Description
-----------

Iterate over list of given type from current point, safe against
removal of list entry.

.. _`list_for_each_entry_safe_reverse`:

list_for_each_entry_safe_reverse
================================

.. c:function::  list_for_each_entry_safe_reverse( pos,  n,  head,  member)

    :param  pos:
        the type \* to use as a loop cursor.

    :param  n:
        another type \* to use as temporary storage

    :param  head:
        the head for your list.

    :param  member:
        the name of the list_head within the struct.

.. _`list_for_each_entry_safe_reverse.description`:

Description
-----------

Iterate backwards over list of given type, safe against removal
of list entry.

.. This file was automatic generated / don't edit.

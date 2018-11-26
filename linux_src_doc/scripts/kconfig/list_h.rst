.. -*- coding: utf-8; mode: rst -*-
.. src-file: scripts/kconfig/list.h

.. _`container_of`:

container_of
============

.. c:function::  container_of( ptr,  type,  member)

    cast a member of a structure out to the containing structure

    :param ptr:
        the pointer to the member.
    :type ptr: 

    :param type:
        the type of the container struct this is embedded in.
    :type type: 

    :param member:
        the name of the member within the struct.
    :type member: 

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

.. _`list_for_each_entry`:

list_for_each_entry
===================

.. c:function::  list_for_each_entry( pos,  head,  member)

    iterate over list of given type

    :param pos:
        the type \* to use as a loop cursor.
    :type pos: 

    :param head:
        the head for your list.
    :type head: 

    :param member:
        the name of the list_head within the struct.
    :type member: 

.. _`list_for_each_entry_safe`:

list_for_each_entry_safe
========================

.. c:function::  list_for_each_entry_safe( pos,  n,  head,  member)

    iterate over list of given type safe against removal of list entry

    :param pos:
        the type \* to use as a loop cursor.
    :type pos: 

    :param n:
        another type \* to use as temporary storage
    :type n: 

    :param head:
        the head for your list.
    :type head: 

    :param member:
        the name of the list_head within the struct.
    :type member: 

.. _`list_empty`:

list_empty
==========

.. c:function:: int list_empty(const struct list_head *head)

    tests whether a list is empty

    :param head:
        the list to test.
    :type head: const struct list_head \*

.. _`list_add_tail`:

list_add_tail
=============

.. c:function:: void list_add_tail(struct list_head *_new, struct list_head *head)

    add a new entry

    :param _new:
        *undescribed*
    :type _new: struct list_head \*

    :param head:
        list head to add it before
    :type head: struct list_head \*

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

    :param entry:
        the element to delete from the list.
    :type entry: struct list_head \*

.. _`list_del.note`:

Note
----

\ :c:func:`list_empty`\  on entry does not return true after this, the entry is
in an undefined state.

.. This file was automatic generated / don't edit.


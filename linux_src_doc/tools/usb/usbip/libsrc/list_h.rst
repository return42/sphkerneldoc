.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/usb/usbip/libsrc/list.h

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

.. _`__list_del_entry`:

\__list_del_entry
=================

.. c:function:: void __list_del_entry(struct list_head *entry)

    deletes entry from list.

    :param entry:
        the element to delete from the list.
    :type entry: struct list_head \*

.. _`__list_del_entry.note`:

Note
----

\ :c:func:`list_empty`\  on entry does not return true after this, the entry is
in an undefined state.

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

.. This file was automatic generated / don't edit.


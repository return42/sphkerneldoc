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

.. This file was automatic generated / don't edit.


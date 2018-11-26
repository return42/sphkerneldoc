.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/nouveau/include/nvif/list.h

.. _`list_head_init`:

LIST_HEAD_INIT
==============

.. c:function::  LIST_HEAD_INIT( name)

    :param name:
        *undescribed*
    :type name: 

.. _`list_head_init.example`:

Example
-------

.. code-block:: c

    INIT_LIST_HEAD(&bar->list_of_foos);

    @param The list to initialized.


.. _`list_add`:

list_add
========

.. c:function:: void list_add(struct list_head *entry, struct list_head *head)

    need to be initialised as empty list.

    :param entry:
        *undescribed*
    :type entry: struct list_head \*

    :param head:
        *undescribed*
    :type head: struct list_head \*

.. _`list_add.the-list-changes-from`:

The list changes from
---------------------

head → some element → ...
to
head → new element → older element → ...

.. _`list_add.example`:

Example
-------

.. code-block:: c

    struct foo *newfoo = malloc(...);
    list_add(&newfoo->entry, &bar->list_of_foos);

    @param entry The new element to prepend to the list.
    @param head The existing list.


.. _`list_add_tail`:

list_add_tail
=============

.. c:function:: void list_add_tail(struct list_head *entry, struct list_head *head)

    :param entry:
        *undescribed*
    :type entry: struct list_head \*

    :param head:
        *undescribed*
    :type head: struct list_head \*

.. _`list_add_tail.the-list-changes-from`:

The list changes from
---------------------

head → some element → ... → lastelement
to
head → some element → ... → lastelement → new element

.. _`list_add_tail.example`:

Example
-------

.. code-block:: c

    struct foo *newfoo = malloc(...);
    list_add_tail(&newfoo->entry, &bar->list_of_foos);

    @param entry The new element to prepend to the list.
    @param head The existing list.


.. _`list_del`:

list_del
========

.. c:function:: void list_del(struct list_head *entry)

    the pointers to/from this element so it is removed from the list. It does NOT free the element itself or manipulate it otherwise.

    :param entry:
        *undescribed*
    :type entry: struct list_head \*

.. _`list_del.description`:

Description
-----------

Using list_del on a pure list head (like in the example at the top of
this file) will NOT remove the first element from
the list but rather reset the list as empty list.

.. _`list_del.example`:

Example
-------

.. code-block:: c

    list_del(&foo->entry);

    @param entry The element to remove.


.. _`list_empty`:

list_empty
==========

.. c:function:: bool list_empty(struct list_head *head)

    :param head:
        *undescribed*
    :type head: struct list_head \*

.. _`list_empty.example`:

Example
-------

.. code-block:: c

    list_empty(&bar->list_of_foos);

    @return True if the list contains one or more elements or False otherwise.


.. _`container_of`:

container_of
============

.. c:function::  container_of( ptr,  type,  member)

    :param ptr:
        *undescribed*
    :type ptr: 

    :param type:
        *undescribed*
    :type type: 

    :param member:
        *undescribed*
    :type member: 

.. _`container_of.example`:

Example
-------

.. code-block:: c

    struct foo* f;
    f = container_of(&foo->entry, struct foo, entry);
    assert(f == foo);

    @param ptr Pointer to the struct list_head.
    @param type Data type of the list element.
    @param member Member name of the struct list_head field in the list element.
    @return A pointer to the data struct containing the list head.


.. _`list_entry`:

list_entry
==========

.. c:function::  list_entry( ptr,  type,  member)

    :param ptr:
        *undescribed*
    :type ptr: 

    :param type:
        *undescribed*
    :type type: 

    :param member:
        *undescribed*
    :type member: 

.. _`list_first_entry`:

list_first_entry
================

.. c:function::  list_first_entry( ptr,  type,  member)

    :param ptr:
        *undescribed*
    :type ptr: 

    :param type:
        *undescribed*
    :type type: 

    :param member:
        *undescribed*
    :type member: 

.. _`list_first_entry.example`:

Example
-------

.. code-block:: c

    struct foo *first;
    first = list_first_entry(&bar->list_of_foos, struct foo, list_of_foos);

    @param ptr The list head
    @param type Data type of the list element to retrieve
    @param member Member name of the struct list_head field in the list element.
    @return A pointer to the first list element.


.. _`list_last_entry`:

list_last_entry
===============

.. c:function::  list_last_entry( ptr,  type,  member)

    :param ptr:
        *undescribed*
    :type ptr: 

    :param type:
        *undescribed*
    :type type: 

    :param member:
        *undescribed*
    :type member: 

.. _`list_last_entry.example`:

Example
-------

.. code-block:: c

    struct foo *first;
    first = list_last_entry(&bar->list_of_foos, struct foo, list_of_foos);

    @param ptr The list head
    @param type Data type of the list element to retrieve
    @param member Member name of the struct list_head field in the list element.
    @return A pointer to the last list element.


.. _`list_for_each_entry`:

list_for_each_entry
===================

.. c:function::  list_for_each_entry( pos,  head,  member)

    :param pos:
        *undescribed*
    :type pos: 

    :param head:
        *undescribed*
    :type head: 

    :param member:
        *undescribed*
    :type member: 

.. _`list_for_each_entry.example`:

Example
-------

.. code-block:: c

    struct foo *iterator;
    list_for_each_entry(iterator, &bar->list_of_foos, entry) {
         [modify iterator]
    }

    This macro is not safe for node deletion. Use list_for_each_entry_safe
    instead.

    @param pos Iterator variable of the type of the list elements.
    @param head List head
    @param member Member name of the struct list_head in the list elements.


.. _`list_for_each_entry_safe`:

list_for_each_entry_safe
========================

.. c:function::  list_for_each_entry_safe( pos,  tmp,  head,  member)

    macro allows for the deletion of a list element while looping through the list.

    :param pos:
        *undescribed*
    :type pos: 

    :param tmp:
        *undescribed*
    :type tmp: 

    :param head:
        *undescribed*
    :type head: 

    :param member:
        *undescribed*
    :type member: 

.. _`list_for_each_entry_safe.description`:

Description
-----------

See list_for_each_entry for more details.

.. This file was automatic generated / don't edit.


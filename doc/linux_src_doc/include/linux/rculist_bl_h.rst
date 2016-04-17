.. -*- coding: utf-8; mode: rst -*-

============
rculist_bl.h
============


.. _`hlist_bl_del_init_rcu`:

hlist_bl_del_init_rcu
=====================

.. c:function:: void hlist_bl_del_init_rcu (struct hlist_bl_node *n)

    deletes entry from hash list with re-initialization

    :param struct hlist_bl_node \*n:
        the element to delete from the hash list.



.. _`hlist_bl_del_init_rcu.note`:

Note
----

:c:func:`hlist_bl_unhashed` on the node returns true after this. It is
useful for RCU based read lockfree traversal if the writer side
must know if the list entry is still hashed or already unhashed.

In particular, it means that we can not poison the forward pointers
that may still be used for walking the hash list and we can only
zero the pprev pointer so :c:func:`list_unhashed` will return true after
this.

The caller must take whatever precautions are necessary (such as
holding appropriate locks) to avoid racing with another
list-mutation primitive, such as :c:func:`hlist_bl_add_head_rcu` or
:c:func:`hlist_bl_del_rcu`, running on this same list.  However, it is
perfectly legal to run concurrently with the _rcu list-traversal
primitives, such as :c:func:`hlist_bl_for_each_entry_rcu`.



.. _`hlist_bl_del_rcu`:

hlist_bl_del_rcu
================

.. c:function:: void hlist_bl_del_rcu (struct hlist_bl_node *n)

    deletes entry from hash list without re-initialization

    :param struct hlist_bl_node \*n:
        the element to delete from the hash list.



.. _`hlist_bl_del_rcu.note`:

Note
----

:c:func:`hlist_bl_unhashed` on entry does not return true after this,
the entry is in an undefined state. It is useful for RCU based
lockfree traversal.

In particular, it means that we can not poison the forward
pointers that may still be used for walking the hash list.

The caller must take whatever precautions are necessary
(such as holding appropriate locks) to avoid racing
with another list-mutation primitive, such as :c:func:`hlist_bl_add_head_rcu`
or :c:func:`hlist_bl_del_rcu`, running on this same list.
However, it is perfectly legal to run concurrently with
the _rcu list-traversal primitives, such as
:c:func:`hlist_bl_for_each_entry`.



.. _`hlist_bl_add_head_rcu`:

hlist_bl_add_head_rcu
=====================

.. c:function:: void hlist_bl_add_head_rcu (struct hlist_bl_node *n, struct hlist_bl_head *h)

    :param struct hlist_bl_node \*n:
        the element to add to the hash list.

    :param struct hlist_bl_head \*h:
        the list to add to.



.. _`hlist_bl_add_head_rcu.description`:

Description
-----------

Adds the specified element to the specified hlist_bl,
while permitting racing traversals.

The caller must take whatever precautions are necessary
(such as holding appropriate locks) to avoid racing
with another list-mutation primitive, such as :c:func:`hlist_bl_add_head_rcu`
or :c:func:`hlist_bl_del_rcu`, running on this same list.
However, it is perfectly legal to run concurrently with
the _rcu list-traversal primitives, such as
:c:func:`hlist_bl_for_each_entry_rcu`, used to prevent memory-consistency
problems on Alpha CPUs.  Regardless of the type of CPU, the
list-traversal primitive must be guarded by :c:func:`rcu_read_lock`.



.. _`hlist_bl_for_each_entry_rcu`:

hlist_bl_for_each_entry_rcu
===========================

.. c:function:: hlist_bl_for_each_entry_rcu ( tpos,  pos,  head,  member)

    iterate over rcu list of given type

    :param tpos:
        the type * to use as a loop cursor.

    :param pos:
        the :c:type:`struct hlist_bl_node <hlist_bl_node>` to use as a loop cursor.

    :param head:
        the head for your list.

    :param member:
        the name of the hlist_bl_node within the struct.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/rculist_nulls.h

.. _`hlist_nulls_del_init_rcu`:

hlist_nulls_del_init_rcu
========================

.. c:function:: void hlist_nulls_del_init_rcu(struct hlist_nulls_node *n)

    deletes entry from hash list with re-initialization

    :param n:
        the element to delete from the hash list.
    :type n: struct hlist_nulls_node \*

.. _`hlist_nulls_del_init_rcu.note`:

Note
----

\ :c:func:`hlist_nulls_unhashed`\  on the node return true after this. It is
useful for RCU based read lockfree traversal if the writer side
must know if the list entry is still hashed or already unhashed.

In particular, it means that we can not poison the forward pointers
that may still be used for walking the hash list and we can only
zero the pprev pointer so \ :c:func:`list_unhashed`\  will return true after
this.

The caller must take whatever precautions are necessary (such as
holding appropriate locks) to avoid racing with another
list-mutation primitive, such as \ :c:func:`hlist_nulls_add_head_rcu`\  or
\ :c:func:`hlist_nulls_del_rcu`\ , running on this same list.  However, it is
perfectly legal to run concurrently with the _rcu list-traversal
primitives, such as \ :c:func:`hlist_nulls_for_each_entry_rcu`\ .

.. _`hlist_nulls_del_rcu`:

hlist_nulls_del_rcu
===================

.. c:function:: void hlist_nulls_del_rcu(struct hlist_nulls_node *n)

    deletes entry from hash list without re-initialization

    :param n:
        the element to delete from the hash list.
    :type n: struct hlist_nulls_node \*

.. _`hlist_nulls_del_rcu.note`:

Note
----

\ :c:func:`hlist_nulls_unhashed`\  on entry does not return true after this,
the entry is in an undefined state. It is useful for RCU based
lockfree traversal.

In particular, it means that we can not poison the forward
pointers that may still be used for walking the hash list.

The caller must take whatever precautions are necessary
(such as holding appropriate locks) to avoid racing
with another list-mutation primitive, such as \ :c:func:`hlist_nulls_add_head_rcu`\ 
or \ :c:func:`hlist_nulls_del_rcu`\ , running on this same list.
However, it is perfectly legal to run concurrently with
the _rcu list-traversal primitives, such as
\ :c:func:`hlist_nulls_for_each_entry`\ .

.. _`hlist_nulls_add_head_rcu`:

hlist_nulls_add_head_rcu
========================

.. c:function:: void hlist_nulls_add_head_rcu(struct hlist_nulls_node *n, struct hlist_nulls_head *h)

    :param n:
        the element to add to the hash list.
    :type n: struct hlist_nulls_node \*

    :param h:
        the list to add to.
    :type h: struct hlist_nulls_head \*

.. _`hlist_nulls_add_head_rcu.description`:

Description
-----------

Adds the specified element to the specified hlist_nulls,
while permitting racing traversals.

The caller must take whatever precautions are necessary
(such as holding appropriate locks) to avoid racing
with another list-mutation primitive, such as \ :c:func:`hlist_nulls_add_head_rcu`\ 
or \ :c:func:`hlist_nulls_del_rcu`\ , running on this same list.
However, it is perfectly legal to run concurrently with
the _rcu list-traversal primitives, such as
\ :c:func:`hlist_nulls_for_each_entry_rcu`\ , used to prevent memory-consistency
problems on Alpha CPUs.  Regardless of the type of CPU, the
list-traversal primitive must be guarded by \ :c:func:`rcu_read_lock`\ .

.. _`hlist_nulls_for_each_entry_rcu`:

hlist_nulls_for_each_entry_rcu
==============================

.. c:function::  hlist_nulls_for_each_entry_rcu( tpos,  pos,  head,  member)

    iterate over rcu list of given type

    :param tpos:
        the type * to use as a loop cursor.
    :type tpos: 

    :param pos:
        the \ :c:type:`struct hlist_nulls_node <hlist_nulls_node>`\  to use as a loop cursor.
    :type pos: 

    :param head:
        the head for your list.
    :type head: 

    :param member:
        the name of the hlist_nulls_node within the struct.
    :type member: 

.. _`hlist_nulls_for_each_entry_rcu.description`:

Description
-----------

The \ :c:func:`barrier`\  is needed to make sure compiler doesn't cache first element [1],
as this loop can be restarted [2]
[1] Documentation/core-api/atomic_ops.rst around line 114
[2] Documentation/RCU/rculist_nulls.txt around line 146

.. _`hlist_nulls_for_each_entry_safe`:

hlist_nulls_for_each_entry_safe
===============================

.. c:function::  hlist_nulls_for_each_entry_safe( tpos,  pos,  head,  member)

    iterate over list of given type safe against removal of list entry

    :param tpos:
        the type * to use as a loop cursor.
    :type tpos: 

    :param pos:
        the \ :c:type:`struct hlist_nulls_node <hlist_nulls_node>`\  to use as a loop cursor.
    :type pos: 

    :param head:
        the head for your list.
    :type head: 

    :param member:
        the name of the hlist_nulls_node within the struct.
    :type member: 

.. This file was automatic generated / don't edit.


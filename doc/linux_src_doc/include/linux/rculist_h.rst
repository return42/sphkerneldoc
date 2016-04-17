.. -*- coding: utf-8; mode: rst -*-

=========
rculist.h
=========


.. _`list_add_rcu`:

list_add_rcu
============

.. c:function:: void list_add_rcu (struct list_head *new, struct list_head *head)

    add a new entry to rcu-protected list

    :param struct list_head \*new:
        new entry to be added

    :param struct list_head \*head:
        list head to add it after



.. _`list_add_rcu.description`:

Description
-----------

Insert a new entry after the specified head.
This is good for implementing stacks.

The caller must take whatever precautions are necessary
(such as holding appropriate locks) to avoid racing
with another list-mutation primitive, such as :c:func:`list_add_rcu`
or :c:func:`list_del_rcu`, running on this same list.
However, it is perfectly legal to run concurrently with
the _rcu list-traversal primitives, such as
:c:func:`list_for_each_entry_rcu`.



.. _`list_add_tail_rcu`:

list_add_tail_rcu
=================

.. c:function:: void list_add_tail_rcu (struct list_head *new, struct list_head *head)

    add a new entry to rcu-protected list

    :param struct list_head \*new:
        new entry to be added

    :param struct list_head \*head:
        list head to add it before



.. _`list_add_tail_rcu.description`:

Description
-----------

Insert a new entry before the specified head.
This is useful for implementing queues.

The caller must take whatever precautions are necessary
(such as holding appropriate locks) to avoid racing
with another list-mutation primitive, such as :c:func:`list_add_tail_rcu`
or :c:func:`list_del_rcu`, running on this same list.
However, it is perfectly legal to run concurrently with
the _rcu list-traversal primitives, such as
:c:func:`list_for_each_entry_rcu`.



.. _`list_del_rcu`:

list_del_rcu
============

.. c:function:: void list_del_rcu (struct list_head *entry)

    deletes entry from list without re-initialization

    :param struct list_head \*entry:
        the element to delete from the list.



.. _`list_del_rcu.note`:

Note
----

:c:func:`list_empty` on entry does not return true after this,
the entry is in an undefined state. It is useful for RCU based
lockfree traversal.

In particular, it means that we can not poison the forward
pointers that may still be used for walking the list.

The caller must take whatever precautions are necessary
(such as holding appropriate locks) to avoid racing
with another list-mutation primitive, such as :c:func:`list_del_rcu`
or :c:func:`list_add_rcu`, running on this same list.
However, it is perfectly legal to run concurrently with
the _rcu list-traversal primitives, such as
:c:func:`list_for_each_entry_rcu`.

Note that the caller is not permitted to immediately free
the newly deleted entry.  Instead, either :c:func:`synchronize_rcu`
or :c:func:`call_rcu` must be used to defer freeing until an RCU
grace period has elapsed.



.. _`hlist_del_init_rcu`:

hlist_del_init_rcu
==================

.. c:function:: void hlist_del_init_rcu (struct hlist_node *n)

    deletes entry from hash list with re-initialization

    :param struct hlist_node \*n:
        the element to delete from the hash list.



.. _`hlist_del_init_rcu.note`:

Note
----

:c:func:`list_unhashed` on the node return true after this. It is
useful for RCU based read lockfree traversal if the writer side
must know if the list entry is still hashed or already unhashed.

In particular, it means that we can not poison the forward pointers
that may still be used for walking the hash list and we can only
zero the pprev pointer so :c:func:`list_unhashed` will return true after
this.

The caller must take whatever precautions are necessary (such as
holding appropriate locks) to avoid racing with another
list-mutation primitive, such as :c:func:`hlist_add_head_rcu` or
:c:func:`hlist_del_rcu`, running on this same list.  However, it is
perfectly legal to run concurrently with the _rcu list-traversal
primitives, such as :c:func:`hlist_for_each_entry_rcu`.



.. _`list_replace_rcu`:

list_replace_rcu
================

.. c:function:: void list_replace_rcu (struct list_head *old, struct list_head *new)

    replace old entry by new one

    :param struct list_head \*old:
        the element to be replaced

    :param struct list_head \*new:
        the new element to insert



.. _`list_replace_rcu.description`:

Description
-----------

The ``old`` entry will be replaced with the ``new`` entry atomically.



.. _`list_replace_rcu.note`:

Note
----

``old`` should not be empty.



.. _`__list_splice_init_rcu`:

__list_splice_init_rcu
======================

.. c:function:: void __list_splice_init_rcu (struct list_head *list, struct list_head *prev, struct list_head *next, void (*sync) (void)

    join an RCU-protected list into an existing list.

    :param struct list_head \*list:
        the RCU-protected list to splice

    :param struct list_head \*prev:
        points to the last element of the existing list

    :param struct list_head \*next:
        points to the first element of the existing list

    :param void (\*sync) (void):
        function to sync: :c:func:`synchronize_rcu`, :c:func:`synchronize_sched`, ...



.. _`__list_splice_init_rcu.description`:

Description
-----------

The list pointed to by ``prev`` and ``next`` can be RCU-read traversed
concurrently with this function.

Note that this function blocks.



.. _`__list_splice_init_rcu.important-note`:

Important note
--------------

the caller must take whatever action is necessary to prevent
any other updates to the existing list.  In principle, it is possible to
modify the list as soon as :c:func:`sync` begins execution. If this sort of thing
becomes necessary, an alternative version based on :c:func:`call_rcu` could be
created.  But only if -really- needed -- there is no shortage of RCU API
members.



.. _`list_splice_init_rcu`:

list_splice_init_rcu
====================

.. c:function:: void list_splice_init_rcu (struct list_head *list, struct list_head *head, void (*sync) (void)

    splice an RCU-protected list into an existing list, designed for stacks.

    :param struct list_head \*list:
        the RCU-protected list to splice

    :param struct list_head \*head:
        the place in the existing list to splice the first list into

    :param void (\*sync) (void):
        function to sync: :c:func:`synchronize_rcu`, :c:func:`synchronize_sched`, ...



.. _`list_splice_tail_init_rcu`:

list_splice_tail_init_rcu
=========================

.. c:function:: void list_splice_tail_init_rcu (struct list_head *list, struct list_head *head, void (*sync) (void)

    splice an RCU-protected list into an existing list, designed for queues.

    :param struct list_head \*list:
        the RCU-protected list to splice

    :param struct list_head \*head:
        the place in the existing list to splice the first list into

    :param void (\*sync) (void):
        function to sync: :c:func:`synchronize_rcu`, :c:func:`synchronize_sched`, ...



.. _`list_entry_rcu`:

list_entry_rcu
==============

.. c:function:: list_entry_rcu ( ptr,  type,  member)

    get the struct for this entry

    :param ptr:
        the :c:type:`struct list_head <list_head>` pointer.

    :param type:
        the type of the struct this is embedded in.

    :param member:
        the name of the list_head within the struct.



.. _`list_entry_rcu.description`:

Description
-----------

This primitive may safely run concurrently with the _rcu list-mutation
primitives such as :c:func:`list_add_rcu` as long as it's guarded by :c:func:`rcu_read_lock`.



.. _`list_first_or_null_rcu`:

list_first_or_null_rcu
======================

.. c:function:: list_first_or_null_rcu ( ptr,  type,  member)

    :param ptr:

        *undescribed*

    :param type:

        *undescribed*

    :param member:

        *undescribed*



.. _`list_first_or_null_rcu.description`:

Description
-----------


Implementing those functions following their counterparts :c:func:`list_empty` and
:c:func:`list_first_entry` is not advisable because they lead to subtle race



.. _`list_first_or_null_rcu.conditions-as-the-following-snippet-shows`:

conditions as the following snippet shows
-----------------------------------------


if (!list_empty_rcu(mylist)) {
struct foo \*bar = list_first_entry_rcu(mylist, struct foo, list_member);
do_something(bar);

}

The list may not be empty when list_empty_rcu checks it, but it may be when
list_first_entry_rcu rereads the ->next pointer.

Rereading the ->next pointer is not a problem for :c:func:`list_empty` and
:c:func:`list_first_entry` because they would be protected by a lock that blocks
writers.

See list_first_or_null_rcu for an alternative.



.. _`list_next_or_null_rcu`:

list_next_or_null_rcu
=====================

.. c:function:: list_next_or_null_rcu ( head,  ptr,  type,  member)

    get the first element from a list

    :param head:
        the head for the list.

    :param ptr:
        the list head to take the next element from.

    :param type:
        the type of the struct this is embedded in.

    :param member:
        the name of the list_head within the struct.



.. _`list_next_or_null_rcu.description`:

Description
-----------

Note that if the ptr is at the end of the list, NULL is returned.

This primitive may safely run concurrently with the _rcu list-mutation
primitives such as :c:func:`list_add_rcu` as long as it's guarded by :c:func:`rcu_read_lock`.



.. _`list_for_each_entry_rcu`:

list_for_each_entry_rcu
=======================

.. c:function:: list_for_each_entry_rcu ( pos,  head,  member)

    iterate over rcu list of given type

    :param pos:
        the type * to use as a loop cursor.

    :param head:
        the head for your list.

    :param member:
        the name of the list_head within the struct.



.. _`list_for_each_entry_rcu.description`:

Description
-----------

This list-traversal primitive may safely run concurrently with
the _rcu list-mutation primitives such as :c:func:`list_add_rcu`
as long as the traversal is guarded by :c:func:`rcu_read_lock`.



.. _`list_entry_lockless`:

list_entry_lockless
===================

.. c:function:: list_entry_lockless ( ptr,  type,  member)

    get the struct for this entry

    :param ptr:
        the :c:type:`struct list_head <list_head>` pointer.

    :param type:
        the type of the struct this is embedded in.

    :param member:
        the name of the list_head within the struct.



.. _`list_entry_lockless.description`:

Description
-----------

This primitive may safely run concurrently with the _rcu list-mutation
primitives such as :c:func:`list_add_rcu`, but requires some implicit RCU
read-side guarding.  One example is running within a special
exception-time environment where preemption is disabled and where
lockdep cannot be invoked (in which case updaters must use RCU-sched,
as in :c:func:`synchronize_sched`, :c:func:`call_rcu_sched`, and friends).  Another
example is when items are added to the list, but never deleted.



.. _`list_for_each_entry_lockless`:

list_for_each_entry_lockless
============================

.. c:function:: list_for_each_entry_lockless ( pos,  head,  member)

    iterate over rcu list of given type

    :param pos:
        the type * to use as a loop cursor.

    :param head:
        the head for your list.

    :param member:
        the name of the list_struct within the struct.



.. _`list_for_each_entry_lockless.description`:

Description
-----------

This primitive may safely run concurrently with the _rcu list-mutation
primitives such as :c:func:`list_add_rcu`, but requires some implicit RCU
read-side guarding.  One example is running within a special
exception-time environment where preemption is disabled and where
lockdep cannot be invoked (in which case updaters must use RCU-sched,
as in :c:func:`synchronize_sched`, :c:func:`call_rcu_sched`, and friends).  Another
example is when items are added to the list, but never deleted.



.. _`list_for_each_entry_continue_rcu`:

list_for_each_entry_continue_rcu
================================

.. c:function:: list_for_each_entry_continue_rcu ( pos,  head,  member)

    continue iteration over list of given type

    :param pos:
        the type * to use as a loop cursor.

    :param head:
        the head for your list.

    :param member:
        the name of the list_head within the struct.



.. _`list_for_each_entry_continue_rcu.description`:

Description
-----------

Continue to iterate over list of given type, continuing after
the current position.



.. _`hlist_del_rcu`:

hlist_del_rcu
=============

.. c:function:: void hlist_del_rcu (struct hlist_node *n)

    deletes entry from hash list without re-initialization

    :param struct hlist_node \*n:
        the element to delete from the hash list.



.. _`hlist_del_rcu.note`:

Note
----

:c:func:`list_unhashed` on entry does not return true after this,
the entry is in an undefined state. It is useful for RCU based
lockfree traversal.

In particular, it means that we can not poison the forward
pointers that may still be used for walking the hash list.

The caller must take whatever precautions are necessary
(such as holding appropriate locks) to avoid racing
with another list-mutation primitive, such as :c:func:`hlist_add_head_rcu`
or :c:func:`hlist_del_rcu`, running on this same list.
However, it is perfectly legal to run concurrently with
the _rcu list-traversal primitives, such as
:c:func:`hlist_for_each_entry`.



.. _`hlist_replace_rcu`:

hlist_replace_rcu
=================

.. c:function:: void hlist_replace_rcu (struct hlist_node *old, struct hlist_node *new)

    replace old entry by new one

    :param struct hlist_node \*old:
        the element to be replaced

    :param struct hlist_node \*new:
        the new element to insert



.. _`hlist_replace_rcu.description`:

Description
-----------

The ``old`` entry will be replaced with the ``new`` entry atomically.



.. _`hlist_add_head_rcu`:

hlist_add_head_rcu
==================

.. c:function:: void hlist_add_head_rcu (struct hlist_node *n, struct hlist_head *h)

    :param struct hlist_node \*n:
        the element to add to the hash list.

    :param struct hlist_head \*h:
        the list to add to.



.. _`hlist_add_head_rcu.description`:

Description
-----------

Adds the specified element to the specified hlist,
while permitting racing traversals.

The caller must take whatever precautions are necessary
(such as holding appropriate locks) to avoid racing
with another list-mutation primitive, such as :c:func:`hlist_add_head_rcu`
or :c:func:`hlist_del_rcu`, running on this same list.
However, it is perfectly legal to run concurrently with
the _rcu list-traversal primitives, such as
:c:func:`hlist_for_each_entry_rcu`, used to prevent memory-consistency
problems on Alpha CPUs.  Regardless of the type of CPU, the
list-traversal primitive must be guarded by :c:func:`rcu_read_lock`.



.. _`hlist_add_before_rcu`:

hlist_add_before_rcu
====================

.. c:function:: void hlist_add_before_rcu (struct hlist_node *n, struct hlist_node *next)

    :param struct hlist_node \*n:
        the new element to add to the hash list.

    :param struct hlist_node \*next:
        the existing element to add the new element before.



.. _`hlist_add_before_rcu.description`:

Description
-----------

Adds the specified element to the specified hlist
before the specified node while permitting racing traversals.

The caller must take whatever precautions are necessary
(such as holding appropriate locks) to avoid racing
with another list-mutation primitive, such as :c:func:`hlist_add_head_rcu`
or :c:func:`hlist_del_rcu`, running on this same list.
However, it is perfectly legal to run concurrently with
the _rcu list-traversal primitives, such as
:c:func:`hlist_for_each_entry_rcu`, used to prevent memory-consistency
problems on Alpha CPUs.



.. _`hlist_add_behind_rcu`:

hlist_add_behind_rcu
====================

.. c:function:: void hlist_add_behind_rcu (struct hlist_node *n, struct hlist_node *prev)

    :param struct hlist_node \*n:
        the new element to add to the hash list.

    :param struct hlist_node \*prev:
        the existing element to add the new element after.



.. _`hlist_add_behind_rcu.description`:

Description
-----------

Adds the specified element to the specified hlist
after the specified node while permitting racing traversals.

The caller must take whatever precautions are necessary
(such as holding appropriate locks) to avoid racing
with another list-mutation primitive, such as :c:func:`hlist_add_head_rcu`
or :c:func:`hlist_del_rcu`, running on this same list.
However, it is perfectly legal to run concurrently with
the _rcu list-traversal primitives, such as
:c:func:`hlist_for_each_entry_rcu`, used to prevent memory-consistency
problems on Alpha CPUs.



.. _`hlist_for_each_entry_rcu`:

hlist_for_each_entry_rcu
========================

.. c:function:: hlist_for_each_entry_rcu ( pos,  head,  member)

    iterate over rcu list of given type

    :param pos:
        the type * to use as a loop cursor.

    :param head:
        the head for your list.

    :param member:
        the name of the hlist_node within the struct.



.. _`hlist_for_each_entry_rcu.description`:

Description
-----------

This list-traversal primitive may safely run concurrently with
the _rcu list-mutation primitives such as :c:func:`hlist_add_head_rcu`
as long as the traversal is guarded by :c:func:`rcu_read_lock`.



.. _`hlist_for_each_entry_rcu_notrace`:

hlist_for_each_entry_rcu_notrace
================================

.. c:function:: hlist_for_each_entry_rcu_notrace ( pos,  head,  member)

    iterate over rcu list of given type (for tracing)

    :param pos:
        the type * to use as a loop cursor.

    :param head:
        the head for your list.

    :param member:
        the name of the hlist_node within the struct.



.. _`hlist_for_each_entry_rcu_notrace.description`:

Description
-----------

This list-traversal primitive may safely run concurrently with
the _rcu list-mutation primitives such as :c:func:`hlist_add_head_rcu`
as long as the traversal is guarded by :c:func:`rcu_read_lock`.

This is the same as :c:func:`hlist_for_each_entry_rcu` except that it does
not do any RCU debugging or tracing.



.. _`hlist_for_each_entry_rcu_bh`:

hlist_for_each_entry_rcu_bh
===========================

.. c:function:: hlist_for_each_entry_rcu_bh ( pos,  head,  member)

    iterate over rcu list of given type

    :param pos:
        the type * to use as a loop cursor.

    :param head:
        the head for your list.

    :param member:
        the name of the hlist_node within the struct.



.. _`hlist_for_each_entry_rcu_bh.description`:

Description
-----------

This list-traversal primitive may safely run concurrently with
the _rcu list-mutation primitives such as :c:func:`hlist_add_head_rcu`
as long as the traversal is guarded by :c:func:`rcu_read_lock`.



.. _`hlist_for_each_entry_continue_rcu`:

hlist_for_each_entry_continue_rcu
=================================

.. c:function:: hlist_for_each_entry_continue_rcu ( pos,  member)

    iterate over a hlist continuing after current point

    :param pos:
        the type * to use as a loop cursor.

    :param member:
        the name of the hlist_node within the struct.



.. _`hlist_for_each_entry_continue_rcu_bh`:

hlist_for_each_entry_continue_rcu_bh
====================================

.. c:function:: hlist_for_each_entry_continue_rcu_bh ( pos,  member)

    iterate over a hlist continuing after current point

    :param pos:
        the type * to use as a loop cursor.

    :param member:
        the name of the hlist_node within the struct.



.. _`hlist_for_each_entry_from_rcu`:

hlist_for_each_entry_from_rcu
=============================

.. c:function:: hlist_for_each_entry_from_rcu ( pos,  member)

    iterate over a hlist continuing from current point

    :param pos:
        the type * to use as a loop cursor.

    :param member:
        the name of the hlist_node within the struct.


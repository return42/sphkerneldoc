.. -*- coding: utf-8; mode: rst -*-

=======
llist.h
=======


.. _`init_llist_head`:

init_llist_head
===============

.. c:function:: void init_llist_head (struct llist_head *list)

    initialize lock-less list head

    :param struct llist_head \*list:

        *undescribed*



.. _`llist_entry`:

llist_entry
===========

.. c:function:: llist_entry ( ptr,  type,  member)

    get the struct of this entry

    :param ptr:
        the :c:type:`struct llist_node <llist_node>` pointer.

    :param type:
        the type of the struct this is embedded in.

    :param member:
        the name of the llist_node within the struct.



.. _`llist_for_each`:

llist_for_each
==============

.. c:function:: llist_for_each ( pos,  node)

    iterate over some deleted entries of a lock-less list

    :param pos:
        the :c:type:`struct llist_node <llist_node>` to use as a loop cursor

    :param node:
        the first entry of deleted list entries



.. _`llist_for_each.description`:

Description
-----------

In general, some entries of the lock-less list can be traversed
safely only after being deleted from list, so start with an entry
instead of list head.

If being used on entries deleted from lock-less list directly, the
traverse order is from the newest to the oldest added entry.  If
you want to traverse from the oldest to the newest, you must
reverse the order by yourself before traversing.



.. _`llist_for_each_entry`:

llist_for_each_entry
====================

.. c:function:: llist_for_each_entry ( pos,  node,  member)

    iterate over some deleted entries of lock-less list of given type

    :param pos:
        the type * to use as a loop cursor.

    :param node:
        the fist entry of deleted list entries.

    :param member:
        the name of the llist_node with the struct.



.. _`llist_for_each_entry.description`:

Description
-----------

In general, some entries of the lock-less list can be traversed
safely only after being removed from list, so start with an entry
instead of list head.

If being used on entries deleted from lock-less list directly, the
traverse order is from the newest to the oldest added entry.  If
you want to traverse from the oldest to the newest, you must
reverse the order by yourself before traversing.



.. _`llist_for_each_entry_safe`:

llist_for_each_entry_safe
=========================

.. c:function:: llist_for_each_entry_safe ( pos,  n,  node,  member)

    iterate over some deleted entries of lock-less list of given type safe against removal of list entry

    :param pos:
        the type * to use as a loop cursor.

    :param n:
        another type * to use as temporary storage

    :param node:
        the first entry of deleted list entries.

    :param member:
        the name of the llist_node with the struct.



.. _`llist_for_each_entry_safe.description`:

Description
-----------

In general, some entries of the lock-less list can be traversed
safely only after being removed from list, so start with an entry
instead of list head.

If being used on entries deleted from lock-less list directly, the
traverse order is from the newest to the oldest added entry.  If
you want to traverse from the oldest to the newest, you must
reverse the order by yourself before traversing.



.. _`llist_empty`:

llist_empty
===========

.. c:function:: bool llist_empty (const struct llist_head *head)

    tests whether a lock-less list is empty

    :param const struct llist_head \*head:
        the list to test



.. _`llist_empty.description`:

Description
-----------

Not guaranteed to be accurate or up to date.  Just a quick way to
test whether the list is empty without deleting something from the
list.



.. _`llist_add`:

llist_add
=========

.. c:function:: bool llist_add (struct llist_node *new, struct llist_head *head)

    add a new entry

    :param struct llist_node \*new:
        new entry to be added

    :param struct llist_head \*head:
        the head for your lock-less list



.. _`llist_add.description`:

Description
-----------

Returns true if the list was empty prior to adding this entry.



.. _`llist_del_all`:

llist_del_all
=============

.. c:function:: struct llist_node *llist_del_all (struct llist_head *head)

    delete all entries from lock-less list

    :param struct llist_head \*head:
        the head of lock-less list to delete all entries



.. _`llist_del_all.description`:

Description
-----------

If list is empty, return NULL, otherwise, delete all entries and
return the pointer to the first entry.  The order of entries
deleted is from the newest to the oldest added one.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/llist.h

.. _`init_llist_head`:

init_llist_head
===============

.. c:function:: void init_llist_head(struct llist_head *list)

    initialize lock-less list head

    :param list:
        *undescribed*
    :type list: struct llist_head \*

.. _`llist_entry`:

llist_entry
===========

.. c:function::  llist_entry( ptr,  type,  member)

    get the struct of this entry

    :param ptr:
        the \ :c:type:`struct llist_node <llist_node>`\  pointer.
    :type ptr: 

    :param type:
        the type of the struct this is embedded in.
    :type type: 

    :param member:
        the name of the llist_node within the struct.
    :type member: 

.. _`member_address_is_nonnull`:

member_address_is_nonnull
=========================

.. c:function::  member_address_is_nonnull( ptr,  member)

    check whether the member address is not NULL

    :param ptr:
        the object pointer (struct type \* that contains the llist_node)
    :type ptr: 

    :param member:
        the name of the llist_node within the struct.
    :type member: 

.. _`member_address_is_nonnull.description`:

Description
-----------

This macro is conceptually the same as
\ :c:type:`ptr->member <ptr>`\  != NULL
but it works around the fact that compilers can decide that taking a member
address is never a NULL pointer.

Real objects that start at a high address and have a member at NULL are
unlikely to exist, but such pointers may be returned e.g. by the
\ :c:func:`container_of`\  macro.

.. _`llist_for_each`:

llist_for_each
==============

.. c:function::  llist_for_each( pos,  node)

    iterate over some deleted entries of a lock-less list

    :param pos:
        the \ :c:type:`struct llist_node <llist_node>`\  to use as a loop cursor
    :type pos: 

    :param node:
        the first entry of deleted list entries
    :type node: 

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

.. _`llist_for_each_safe`:

llist_for_each_safe
===================

.. c:function::  llist_for_each_safe( pos,  n,  node)

    iterate over some deleted entries of a lock-less list safe against removal of list entry

    :param pos:
        the \ :c:type:`struct llist_node <llist_node>`\  to use as a loop cursor
    :type pos: 

    :param n:
        another \ :c:type:`struct llist_node <llist_node>`\  to use as temporary storage
    :type n: 

    :param node:
        the first entry of deleted list entries
    :type node: 

.. _`llist_for_each_safe.description`:

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

.. c:function::  llist_for_each_entry( pos,  node,  member)

    iterate over some deleted entries of lock-less list of given type

    :param pos:
        the type \* to use as a loop cursor.
    :type pos: 

    :param node:
        the fist entry of deleted list entries.
    :type node: 

    :param member:
        the name of the llist_node with the struct.
    :type member: 

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

.. c:function::  llist_for_each_entry_safe( pos,  n,  node,  member)

    iterate over some deleted entries of lock-less list of given type safe against removal of list entry

    :param pos:
        the type \* to use as a loop cursor.
    :type pos: 

    :param n:
        another type \* to use as temporary storage
    :type n: 

    :param node:
        the first entry of deleted list entries.
    :type node: 

    :param member:
        the name of the llist_node with the struct.
    :type member: 

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

.. c:function:: bool llist_empty(const struct llist_head *head)

    tests whether a lock-less list is empty

    :param head:
        the list to test
    :type head: const struct llist_head \*

.. _`llist_empty.description`:

Description
-----------

Not guaranteed to be accurate or up to date.  Just a quick way to
test whether the list is empty without deleting something from the
list.

.. _`llist_add`:

llist_add
=========

.. c:function:: bool llist_add(struct llist_node *new, struct llist_head *head)

    add a new entry

    :param new:
        new entry to be added
    :type new: struct llist_node \*

    :param head:
        the head for your lock-less list
    :type head: struct llist_head \*

.. _`llist_add.description`:

Description
-----------

Returns true if the list was empty prior to adding this entry.

.. _`llist_del_all`:

llist_del_all
=============

.. c:function:: struct llist_node *llist_del_all(struct llist_head *head)

    delete all entries from lock-less list

    :param head:
        the head of lock-less list to delete all entries
    :type head: struct llist_head \*

.. _`llist_del_all.description`:

Description
-----------

If list is empty, return NULL, otherwise, delete all entries and
return the pointer to the first entry.  The order of entries
deleted is from the newest to the oldest added one.

.. This file was automatic generated / don't edit.


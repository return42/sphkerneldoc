.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/llist.c

.. _`llist_add_batch`:

llist_add_batch
===============

.. c:function:: bool llist_add_batch(struct llist_node *new_first, struct llist_node *new_last, struct llist_head *head)

    add several linked entries in batch

    :param struct llist_node \*new_first:
        first entry in batch to be added

    :param struct llist_node \*new_last:
        last entry in batch to be added

    :param struct llist_head \*head:
        the head for your lock-less list

.. _`llist_add_batch.description`:

Description
-----------

Return whether list is empty before adding.

.. _`llist_del_first`:

llist_del_first
===============

.. c:function:: struct llist_node *llist_del_first(struct llist_head *head)

    delete the first entry of lock-less list

    :param struct llist_head \*head:
        the head for your lock-less list

.. _`llist_del_first.description`:

Description
-----------

If list is empty, return NULL, otherwise, return the first entry
deleted, this is the newest added one.

Only one llist_del_first user can be used simultaneously with
multiple llist_add users without lock.  Because otherwise
llist_del_first, llist_add, llist_add (or llist_del_all, llist_add,
llist_add) sequence in another user may change \ ``head``\ ->first->next,
but keep \ ``head``\ ->first.  If multiple consumers are needed, please
use llist_del_all or use lock between consumers.

.. _`llist_reverse_order`:

llist_reverse_order
===================

.. c:function:: struct llist_node *llist_reverse_order(struct llist_node *head)

    reverse order of a llist chain

    :param struct llist_node \*head:
        first item of the list to be reversed

.. _`llist_reverse_order.description`:

Description
-----------

Reverse the order of a chain of llist entries and return the
new first entry.

.. This file was automatic generated / don't edit.


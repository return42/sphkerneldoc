.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/plist.c

.. _`plist_add`:

plist_add
=========

.. c:function:: void plist_add(struct plist_node *node, struct plist_head *head)

    add \ ``node``\  to \ ``head``\ 

    :param node:
        \ :c:type:`struct plist_node <plist_node>`\  pointer
    :type node: struct plist_node \*

    :param head:
        \ :c:type:`struct plist_head <plist_head>`\  pointer
    :type head: struct plist_head \*

.. _`plist_del`:

plist_del
=========

.. c:function:: void plist_del(struct plist_node *node, struct plist_head *head)

    Remove a \ ``node``\  from plist.

    :param node:
        \ :c:type:`struct plist_node <plist_node>`\  pointer - entry to be removed
    :type node: struct plist_node \*

    :param head:
        \ :c:type:`struct plist_head <plist_head>`\  pointer - list head
    :type head: struct plist_head \*

.. _`plist_requeue`:

plist_requeue
=============

.. c:function:: void plist_requeue(struct plist_node *node, struct plist_head *head)

    Requeue \ ``node``\  at end of same-prio entries.

    :param node:
        \ :c:type:`struct plist_node <plist_node>`\  pointer - entry to be moved
    :type node: struct plist_node \*

    :param head:
        \ :c:type:`struct plist_head <plist_head>`\  pointer - list head
    :type head: struct plist_head \*

.. _`plist_requeue.description`:

Description
-----------

This is essentially an optimized \ :c:func:`plist_del`\  followed by
\ :c:func:`plist_add`\ .  It moves an entry already in the plist to
after any other same-priority entries.

.. This file was automatic generated / don't edit.


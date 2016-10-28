.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/tipc/name_distr.c

.. _`publ_to_item`:

publ_to_item
============

.. c:function:: void publ_to_item(struct distr_item *i, struct publication *p)

    add publication info to a publication message

    :param struct distr_item \*i:
        *undescribed*

    :param struct publication \*p:
        *undescribed*

.. _`named_prepare_buf`:

named_prepare_buf
=================

.. c:function:: struct sk_buff *named_prepare_buf(struct net *net, u32 type, u32 size, u32 dest)

    allocate & initialize a publication message

    :param struct net \*net:
        *undescribed*

    :param u32 type:
        *undescribed*

    :param u32 size:
        *undescribed*

    :param u32 dest:
        *undescribed*

.. _`tipc_named_publish`:

tipc_named_publish
==================

.. c:function:: struct sk_buff *tipc_named_publish(struct net *net, struct publication *publ)

    tell other nodes about a new publication by this node

    :param struct net \*net:
        *undescribed*

    :param struct publication \*publ:
        *undescribed*

.. _`tipc_named_withdraw`:

tipc_named_withdraw
===================

.. c:function:: struct sk_buff *tipc_named_withdraw(struct net *net, struct publication *publ)

    tell other nodes about a withdrawn publication by this node

    :param struct net \*net:
        *undescribed*

    :param struct publication \*publ:
        *undescribed*

.. _`named_distribute`:

named_distribute
================

.. c:function:: void named_distribute(struct net *net, struct sk_buff_head *list, u32 dnode, struct list_head *pls)

    prepare name info for bulk distribution to another node

    :param struct net \*net:
        *undescribed*

    :param struct sk_buff_head \*list:
        list of messages (buffers) to be returned from this function

    :param u32 dnode:
        node to be updated

    :param struct list_head \*pls:
        linked list of publication items to be packed into buffer chain

.. _`tipc_named_node_up`:

tipc_named_node_up
==================

.. c:function:: void tipc_named_node_up(struct net *net, u32 dnode)

    tell specified node about all publications by this node

    :param struct net \*net:
        *undescribed*

    :param u32 dnode:
        *undescribed*

.. _`tipc_publ_purge`:

tipc_publ_purge
===============

.. c:function:: void tipc_publ_purge(struct net *net, struct publication *publ, u32 addr)

    remove publication associated with a failed node

    :param struct net \*net:
        *undescribed*

    :param struct publication \*publ:
        *undescribed*

    :param u32 addr:
        *undescribed*

.. _`tipc_publ_purge.description`:

Description
-----------

Invoked for each publication issued by a newly failed node.
Removes publication structure from name table & deletes it.

.. _`tipc_dist_queue_purge`:

tipc_dist_queue_purge
=====================

.. c:function:: void tipc_dist_queue_purge(struct net *net, u32 addr)

    remove deferred updates from a node that went down

    :param struct net \*net:
        *undescribed*

    :param u32 addr:
        *undescribed*

.. _`tipc_update_nametbl`:

tipc_update_nametbl
===================

.. c:function:: bool tipc_update_nametbl(struct net *net, struct distr_item *i, u32 node, u32 dtype)

    try to process a nametable update and notify subscribers

    :param struct net \*net:
        *undescribed*

    :param struct distr_item \*i:
        *undescribed*

    :param u32 node:
        *undescribed*

    :param u32 dtype:
        *undescribed*

.. _`tipc_update_nametbl.description`:

Description
-----------

tipc_nametbl_lock must be held.
Returns the publication item if successful, otherwise NULL.

.. _`tipc_named_add_backlog`:

tipc_named_add_backlog
======================

.. c:function:: void tipc_named_add_backlog(struct net *net, struct distr_item *i, u32 type, u32 node)

    add a failed name table update to the backlog

    :param struct net \*net:
        *undescribed*

    :param struct distr_item \*i:
        *undescribed*

    :param u32 type:
        *undescribed*

    :param u32 node:
        *undescribed*

.. _`tipc_named_process_backlog`:

tipc_named_process_backlog
==========================

.. c:function:: void tipc_named_process_backlog(struct net *net)

    try to process any pending name table updates from the network.

    :param struct net \*net:
        *undescribed*

.. _`tipc_named_rcv`:

tipc_named_rcv
==============

.. c:function:: void tipc_named_rcv(struct net *net, struct sk_buff_head *inputq)

    process name table update messages sent by another node

    :param struct net \*net:
        *undescribed*

    :param struct sk_buff_head \*inputq:
        *undescribed*

.. _`tipc_named_reinit`:

tipc_named_reinit
=================

.. c:function:: void tipc_named_reinit(struct net *net)

    re-initialize local publications

    :param struct net \*net:
        *undescribed*

.. _`tipc_named_reinit.description`:

Description
-----------

This routine is called whenever TIPC networking is enabled.
All name table entries published by this node are updated to reflect
the node's new network address.

.. This file was automatic generated / don't edit.


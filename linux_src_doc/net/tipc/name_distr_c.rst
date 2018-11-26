.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/tipc/name_distr.c

.. _`publ_to_item`:

publ_to_item
============

.. c:function:: void publ_to_item(struct distr_item *i, struct publication *p)

    add publication info to a publication message

    :param i:
        *undescribed*
    :type i: struct distr_item \*

    :param p:
        *undescribed*
    :type p: struct publication \*

.. _`named_prepare_buf`:

named_prepare_buf
=================

.. c:function:: struct sk_buff *named_prepare_buf(struct net *net, u32 type, u32 size, u32 dest)

    allocate & initialize a publication message

    :param net:
        *undescribed*
    :type net: struct net \*

    :param type:
        *undescribed*
    :type type: u32

    :param size:
        *undescribed*
    :type size: u32

    :param dest:
        *undescribed*
    :type dest: u32

.. _`named_prepare_buf.description`:

Description
-----------

The buffer returned is of size INT_H_SIZE + payload size

.. _`tipc_named_publish`:

tipc_named_publish
==================

.. c:function:: struct sk_buff *tipc_named_publish(struct net *net, struct publication *publ)

    tell other nodes about a new publication by this node

    :param net:
        *undescribed*
    :type net: struct net \*

    :param publ:
        *undescribed*
    :type publ: struct publication \*

.. _`tipc_named_withdraw`:

tipc_named_withdraw
===================

.. c:function:: struct sk_buff *tipc_named_withdraw(struct net *net, struct publication *publ)

    tell other nodes about a withdrawn publication by this node

    :param net:
        *undescribed*
    :type net: struct net \*

    :param publ:
        *undescribed*
    :type publ: struct publication \*

.. _`named_distribute`:

named_distribute
================

.. c:function:: void named_distribute(struct net *net, struct sk_buff_head *list, u32 dnode, struct list_head *pls)

    prepare name info for bulk distribution to another node

    :param net:
        *undescribed*
    :type net: struct net \*

    :param list:
        list of messages (buffers) to be returned from this function
    :type list: struct sk_buff_head \*

    :param dnode:
        node to be updated
    :type dnode: u32

    :param pls:
        linked list of publication items to be packed into buffer chain
    :type pls: struct list_head \*

.. _`tipc_named_node_up`:

tipc_named_node_up
==================

.. c:function:: void tipc_named_node_up(struct net *net, u32 dnode)

    tell specified node about all publications by this node

    :param net:
        *undescribed*
    :type net: struct net \*

    :param dnode:
        *undescribed*
    :type dnode: u32

.. _`tipc_publ_purge`:

tipc_publ_purge
===============

.. c:function:: void tipc_publ_purge(struct net *net, struct publication *publ, u32 addr)

    remove publication associated with a failed node

    :param net:
        *undescribed*
    :type net: struct net \*

    :param publ:
        *undescribed*
    :type publ: struct publication \*

    :param addr:
        *undescribed*
    :type addr: u32

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

    :param net:
        *undescribed*
    :type net: struct net \*

    :param addr:
        *undescribed*
    :type addr: u32

.. _`tipc_update_nametbl`:

tipc_update_nametbl
===================

.. c:function:: bool tipc_update_nametbl(struct net *net, struct distr_item *i, u32 node, u32 dtype)

    try to process a nametable update and notify subscribers

    :param net:
        *undescribed*
    :type net: struct net \*

    :param i:
        *undescribed*
    :type i: struct distr_item \*

    :param node:
        *undescribed*
    :type node: u32

    :param dtype:
        *undescribed*
    :type dtype: u32

.. _`tipc_update_nametbl.description`:

Description
-----------

tipc_nametbl_lock must be held.
Returns the publication item if successful, otherwise NULL.

.. _`tipc_named_rcv`:

tipc_named_rcv
==============

.. c:function:: void tipc_named_rcv(struct net *net, struct sk_buff_head *inputq)

    process name table update messages sent by another node

    :param net:
        *undescribed*
    :type net: struct net \*

    :param inputq:
        *undescribed*
    :type inputq: struct sk_buff_head \*

.. _`tipc_named_reinit`:

tipc_named_reinit
=================

.. c:function:: void tipc_named_reinit(struct net *net)

    re-initialize local publications

    :param net:
        *undescribed*
    :type net: struct net \*

.. _`tipc_named_reinit.description`:

Description
-----------

This routine is called whenever TIPC networking is enabled.
All name table entries published by this node are updated to reflect
the node's new network address.

.. This file was automatic generated / don't edit.


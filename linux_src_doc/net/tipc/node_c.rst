.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/tipc/node.c

.. _`tipc_node`:

struct tipc_node
================

.. c:type:: struct tipc_node

    TIPC node structure

.. _`tipc_node.definition`:

Definition
----------

.. code-block:: c

    struct tipc_node {
        u32 addr;
        struct kref kref;
        rwlock_t lock;
        struct net *net;
        struct hlist_node hash;
        int active_links[2];
        struct tipc_link_entry links[MAX_BEARERS];
        struct tipc_bclink_entry bc_entry;
        int action_flags;
        struct list_head list;
        int state;
        u16 sync_point;
        int link_cnt;
        u16 working_links;
        u16 capabilities;
        u32 signature;
        u32 link_id;
        struct list_head publ_list;
        struct list_head conn_sks;
        unsigned long keepalive_intv;
        struct timer_list timer;
        struct rcu_head rcu;
    }

.. _`tipc_node.members`:

Members
-------

addr
    network address of node

kref
    *undescribed*

lock
    rwlock governing access to structure

net
    the applicable net namespace

hash
    links to adjacent nodes in unsorted hash chain

active_links
    bearer ids of active links, used as index into links[] array

links
    array containing references to all links to node

bc_entry
    *undescribed*

action_flags
    bit mask of different types of node actions

list
    links to adjacent nodes in sorted list of cluster's nodes

state
    connectivity state vs peer node

sync_point
    sequence number where synch/failover is finished

link_cnt
    number of links to node

working_links
    number of working links to node (both active and standby)

capabilities
    bitmap, indicating peer node's functional capabilities

signature
    node instance identifier

link_id
    local and remote bearer ids of changing link, if any

publ_list
    list of publications

conn_sks
    *undescribed*

keepalive_intv
    *undescribed*

timer
    *undescribed*

rcu
    rcu struct for tipc_node

.. _`__tipc_node_link_up`:

__tipc_node_link_up
===================

.. c:function:: void __tipc_node_link_up(struct tipc_node *n, int bearer_id, struct sk_buff_head *xmitq)

    handle addition of link Node lock must be held by caller Link becomes active (alone or shared) or standby, depending on its priority.

    :param struct tipc_node \*n:
        *undescribed*

    :param int bearer_id:
        *undescribed*

    :param struct sk_buff_head \*xmitq:
        *undescribed*

.. _`tipc_node_link_up`:

tipc_node_link_up
=================

.. c:function:: void tipc_node_link_up(struct tipc_node *n, int bearer_id, struct sk_buff_head *xmitq)

    handle addition of link

    :param struct tipc_node \*n:
        *undescribed*

    :param int bearer_id:
        *undescribed*

    :param struct sk_buff_head \*xmitq:
        *undescribed*

.. _`tipc_node_link_up.description`:

Description
-----------

Link becomes active (alone or shared) or standby, depending on its priority.

.. _`__tipc_node_link_down`:

__tipc_node_link_down
=====================

.. c:function:: void __tipc_node_link_down(struct tipc_node *n, int *bearer_id, struct sk_buff_head *xmitq, struct tipc_media_addr **maddr)

    handle loss of link

    :param struct tipc_node \*n:
        *undescribed*

    :param int \*bearer_id:
        *undescribed*

    :param struct sk_buff_head \*xmitq:
        *undescribed*

    :param struct tipc_media_addr \*\*maddr:
        *undescribed*

.. _`tipc_node_get_linkname`:

tipc_node_get_linkname
======================

.. c:function:: int tipc_node_get_linkname(struct net *net, u32 bearer_id, u32 addr, char *linkname, size_t len)

    get the name of a link

    :param struct net \*net:
        *undescribed*

    :param u32 bearer_id:
        id of the bearer

    :param u32 addr:
        *undescribed*

    :param char \*linkname:
        link name output buffer

    :param size_t len:
        *undescribed*

.. _`tipc_node_get_linkname.description`:

Description
-----------

Returns 0 on success

.. _`tipc_node_xmit`:

tipc_node_xmit
==============

.. c:function:: int tipc_node_xmit(struct net *net, struct sk_buff_head *list, u32 dnode, int selector)

    :param struct net \*net:
        the applicable net namespace

    :param struct sk_buff_head \*list:
        chain of buffers containing message

    :param u32 dnode:
        address of destination node

    :param int selector:
        a number used for deterministic link selection
        Consumes the buffer chain.
        Returns 0 if success, otherwise: -ELINKCONG,-EHOSTUNREACH,-EMSGSIZE,-ENOBUF

.. _`tipc_node_bc_rcv`:

tipc_node_bc_rcv
================

.. c:function:: void tipc_node_bc_rcv(struct net *net, struct sk_buff *skb, int bearer_id)

    process TIPC broadcast packet arriving from off-node

    :param struct net \*net:
        the applicable net namespace

    :param struct sk_buff \*skb:
        TIPC packet

    :param int bearer_id:
        id of bearer message arrived on

.. _`tipc_node_bc_rcv.description`:

Description
-----------

Invoked with no locks held.

.. _`tipc_node_check_state`:

tipc_node_check_state
=====================

.. c:function:: bool tipc_node_check_state(struct tipc_node *n, struct sk_buff *skb, int bearer_id, struct sk_buff_head *xmitq)

    check and if necessary update node state

    :param struct tipc_node \*n:
        *undescribed*

    :param struct sk_buff \*skb:
        TIPC packet

    :param int bearer_id:
        identity of bearer delivering the packet
        Returns true if state is ok, otherwise consumes buffer and returns false

    :param struct sk_buff_head \*xmitq:
        *undescribed*

.. _`tipc_rcv`:

tipc_rcv
========

.. c:function:: void tipc_rcv(struct net *net, struct sk_buff *skb, struct tipc_bearer *b)

    process TIPC packets/messages arriving from off-node

    :param struct net \*net:
        the applicable net namespace

    :param struct sk_buff \*skb:
        TIPC packet

    :param struct tipc_bearer \*b:
        *undescribed*

.. _`tipc_rcv.description`:

Description
-----------

Invoked with no locks held. Bearer pointer must point to a valid bearer
structure (i.e. cannot be NULL), but bearer can be inactive.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/tipc/discover.c

.. _`tipc_discoverer`:

struct tipc_discoverer
======================

.. c:type:: struct tipc_discoverer

    information about an ongoing link setup request

.. _`tipc_discoverer.definition`:

Definition
----------

.. code-block:: c

    struct tipc_discoverer {
        u32 bearer_id;
        struct tipc_media_addr dest;
        struct net *net;
        u32 domain;
        int num_nodes;
        spinlock_t lock;
        struct sk_buff *skb;
        struct timer_list timer;
        unsigned long timer_intv;
    }

.. _`tipc_discoverer.members`:

Members
-------

bearer_id
    identity of bearer issuing requests

dest
    destination address for request messages

net
    network namespace instance

domain
    network domain to which links can be established

num_nodes
    number of nodes currently discovered (i.e. with an active link)

lock
    spinlock for controlling access to requests

skb
    request message to be (repeatedly) sent

timer
    timer governing period between requests

timer_intv
    current interval between requests (in ms)

.. _`tipc_disc_init_msg`:

tipc_disc_init_msg
==================

.. c:function:: void tipc_disc_init_msg(struct net *net, struct sk_buff *skb, u32 mtyp, struct tipc_bearer *b)

    initialize a link setup message

    :param struct net \*net:
        the applicable net namespace

    :param struct sk_buff \*skb:
        *undescribed*

    :param u32 mtyp:
        *undescribed*

    :param struct tipc_bearer \*b:
        ptr to bearer issuing message

.. _`disc_dupl_alert`:

disc_dupl_alert
===============

.. c:function:: void disc_dupl_alert(struct tipc_bearer *b, u32 node_addr, struct tipc_media_addr *media_addr)

    issue node address duplication alert

    :param struct tipc_bearer \*b:
        pointer to bearer detecting duplication

    :param u32 node_addr:
        duplicated node address

    :param struct tipc_media_addr \*media_addr:
        media address advertised by duplicated node

.. _`tipc_disc_rcv`:

tipc_disc_rcv
=============

.. c:function:: void tipc_disc_rcv(struct net *net, struct sk_buff *skb, struct tipc_bearer *b)

    handle incoming discovery message (request or response)

    :param struct net \*net:
        applicable net namespace

    :param struct sk_buff \*skb:
        buffer containing message

    :param struct tipc_bearer \*b:
        bearer that message arrived on

.. _`tipc_disc_create`:

tipc_disc_create
================

.. c:function:: int tipc_disc_create(struct net *net, struct tipc_bearer *b, struct tipc_media_addr *dest, struct sk_buff **skb)

    create object to send periodic link setup requests

    :param struct net \*net:
        the applicable net namespace

    :param struct tipc_bearer \*b:
        ptr to bearer issuing requests

    :param struct tipc_media_addr \*dest:
        destination address for request messages

    :param struct sk_buff \*\*skb:
        *undescribed*

.. _`tipc_disc_create.description`:

Description
-----------

Returns 0 if successful, otherwise -errno.

.. _`tipc_disc_delete`:

tipc_disc_delete
================

.. c:function:: void tipc_disc_delete(struct tipc_discoverer *d)

    destroy object sending periodic link setup requests

    :param struct tipc_discoverer \*d:
        ptr to link duest structure

.. _`tipc_disc_reset`:

tipc_disc_reset
===============

.. c:function:: void tipc_disc_reset(struct net *net, struct tipc_bearer *b)

    reset object to send periodic link setup requests

    :param struct net \*net:
        the applicable net namespace

    :param struct tipc_bearer \*b:
        ptr to bearer issuing requests

.. This file was automatic generated / don't edit.


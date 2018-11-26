.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/tipc/name_table.c

.. _`service_range`:

struct service_range
====================

.. c:type:: struct service_range

    container for all bindings of a service range

.. _`service_range.definition`:

Definition
----------

.. code-block:: c

    struct service_range {
        u32 lower;
        u32 upper;
        struct rb_node tree_node;
        struct list_head local_publ;
        struct list_head all_publ;
    }

.. _`service_range.members`:

Members
-------

lower
    service range lower bound

upper
    service range upper bound

tree_node
    member of service range RB tree

local_publ
    list of identical publications made from this node
    Used by closest_first lookup and multicast lookup algorithm

all_publ
    all publications identical to this one, whatever node and scope
    Used by round-robin lookup algorithm

.. _`tipc_service`:

struct tipc_service
===================

.. c:type:: struct tipc_service

    container for all published instances of a service type

.. _`tipc_service.definition`:

Definition
----------

.. code-block:: c

    struct tipc_service {
        u32 type;
        struct rb_root ranges;
        struct hlist_node service_list;
        struct list_head subscriptions;
        spinlock_t lock;
        struct rcu_head rcu;
    }

.. _`tipc_service.members`:

Members
-------

type
    32 bit 'type' value for service

ranges
    rb tree containing all service ranges for this service

service_list
    links to adjacent name ranges in hash chain

subscriptions
    list of subscriptions for this service type

lock
    spinlock controlling access to pertaining service ranges/publications

rcu
    RCU callback head used for deferred freeing

.. _`tipc_publ_create`:

tipc_publ_create
================

.. c:function:: struct publication *tipc_publ_create(u32 type, u32 lower, u32 upper, u32 scope, u32 node, u32 port, u32 key)

    create a publication structure

    :param type:
        *undescribed*
    :type type: u32

    :param lower:
        *undescribed*
    :type lower: u32

    :param upper:
        *undescribed*
    :type upper: u32

    :param scope:
        *undescribed*
    :type scope: u32

    :param node:
        *undescribed*
    :type node: u32

    :param port:
        *undescribed*
    :type port: u32

    :param key:
        *undescribed*
    :type key: u32

.. _`tipc_service_create`:

tipc_service_create
===================

.. c:function:: struct tipc_service *tipc_service_create(u32 type, struct hlist_head *hd)

    create a service structure for the specified 'type'

    :param type:
        *undescribed*
    :type type: u32

    :param hd:
        *undescribed*
    :type hd: struct hlist_head \*

.. _`tipc_service_create.description`:

Description
-----------

Allocates a single range structure and sets it to all 0's.

.. _`tipc_service_first_range`:

tipc_service_first_range
========================

.. c:function:: struct service_range *tipc_service_first_range(struct tipc_service *sc, u32 instance)

    find first service range in tree matching instance

    :param sc:
        *undescribed*
    :type sc: struct tipc_service \*

    :param instance:
        *undescribed*
    :type instance: u32

.. _`tipc_service_first_range.description`:

Description
-----------

Very time-critical, so binary search through range rb tree

.. _`tipc_service_remove_publ`:

tipc_service_remove_publ
========================

.. c:function:: struct publication *tipc_service_remove_publ(struct service_range *sr, u32 node, u32 key)

    remove a publication from a service

    :param sr:
        *undescribed*
    :type sr: struct service_range \*

    :param node:
        *undescribed*
    :type node: u32

    :param key:
        *undescribed*
    :type key: u32

.. _`tipc_service_subscribe`:

tipc_service_subscribe
======================

.. c:function:: void tipc_service_subscribe(struct tipc_service *service, struct tipc_subscription *sub)

    attach a subscription, and optionally issue the prescribed number of events if there is any service range overlapping with the requested range

    :param service:
        *undescribed*
    :type service: struct tipc_service \*

    :param sub:
        *undescribed*
    :type sub: struct tipc_subscription \*

.. _`tipc_nametbl_translate`:

tipc_nametbl_translate
======================

.. c:function:: u32 tipc_nametbl_translate(struct net *net, u32 type, u32 instance, u32 *dnode)

    perform service instance to socket translation

    :param net:
        *undescribed*
    :type net: struct net \*

    :param type:
        *undescribed*
    :type type: u32

    :param instance:
        *undescribed*
    :type instance: u32

    :param dnode:
        *undescribed*
    :type dnode: u32 \*

.. _`tipc_nametbl_translate.description`:

Description
-----------

On entry, 'dnode' is the search domain used during translation.

.. _`tipc_nametbl_translate.on-exit`:

On exit
-------

- if translation is deferred to another node, leave 'dnode' unchanged and
return 0
- if translation is attempted and succeeds, set 'dnode' to the publishing
node and return the published (non-zero) port number
- if translation is attempted and fails, set 'dnode' to 0 and return 0

Note that for legacy users (node configured with Z.C.N address format) the
'closest-first' lookup algorithm must be maintained, i.e., if dnode is 0
we must look in the local binding list first

.. _`tipc_nametbl_withdraw`:

tipc_nametbl_withdraw
=====================

.. c:function:: int tipc_nametbl_withdraw(struct net *net, u32 type, u32 lower, u32 upper, u32 key)

    withdraw a service binding

    :param net:
        *undescribed*
    :type net: struct net \*

    :param type:
        *undescribed*
    :type type: u32

    :param lower:
        *undescribed*
    :type lower: u32

    :param upper:
        *undescribed*
    :type upper: u32

    :param key:
        *undescribed*
    :type key: u32

.. _`tipc_nametbl_subscribe`:

tipc_nametbl_subscribe
======================

.. c:function:: bool tipc_nametbl_subscribe(struct tipc_subscription *sub)

    add a subscription object to the name table

    :param sub:
        *undescribed*
    :type sub: struct tipc_subscription \*

.. _`tipc_nametbl_unsubscribe`:

tipc_nametbl_unsubscribe
========================

.. c:function:: void tipc_nametbl_unsubscribe(struct tipc_subscription *sub)

    remove a subscription object from name table

    :param sub:
        *undescribed*
    :type sub: struct tipc_subscription \*

.. _`tipc_service_delete`:

tipc_service_delete
===================

.. c:function:: void tipc_service_delete(struct net *net, struct tipc_service *sc)

    purge all publications for a service and delete it

    :param net:
        *undescribed*
    :type net: struct net \*

    :param sc:
        *undescribed*
    :type sc: struct tipc_service \*

.. This file was automatic generated / don't edit.


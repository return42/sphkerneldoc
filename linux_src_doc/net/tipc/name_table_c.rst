.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/tipc/name_table.c

.. _`name_info`:

struct name_info
================

.. c:type:: struct name_info

    name sequence publication info

.. _`name_info.definition`:

Definition
----------

.. code-block:: c

    struct name_info {
        struct list_head node_list;
        struct list_head cluster_list;
        struct list_head zone_list;
        u32 node_list_size;
        u32 cluster_list_size;
        u32 zone_list_size;
    }

.. _`name_info.members`:

Members
-------

node_list
    circular list of publications made by own node

cluster_list
    circular list of publications made by own cluster

zone_list
    circular list of publications made by own zone

node_list_size
    number of entries in "node_list"

cluster_list_size
    number of entries in "cluster_list"

zone_list_size
    number of entries in "zone_list"

.. _`name_info.note`:

Note
----

The zone list always contains at least one entry, since all
publications of the associated name sequence belong to it.
(The cluster and node lists may be empty.)

.. _`sub_seq`:

struct sub_seq
==============

.. c:type:: struct sub_seq

    container for all published instances of a name sequence

.. _`sub_seq.definition`:

Definition
----------

.. code-block:: c

    struct sub_seq {
        u32 lower;
        u32 upper;
        struct name_info *info;
    }

.. _`sub_seq.members`:

Members
-------

lower
    name sequence lower bound

upper
    name sequence upper bound

info
    pointer to name sequence publication info

.. _`name_seq`:

struct name_seq
===============

.. c:type:: struct name_seq

    container for all published instances of a name type

.. _`name_seq.definition`:

Definition
----------

.. code-block:: c

    struct name_seq {
        u32 type;
        struct sub_seq *sseqs;
        u32 alloc;
        u32 first_free;
        struct hlist_node ns_list;
        struct list_head subscriptions;
        spinlock_t lock;
        struct rcu_head rcu;
    }

.. _`name_seq.members`:

Members
-------

type
    32 bit 'type' value for name sequence

sseqs
    *undescribed*

alloc
    number of sub-sequences currently in array

first_free
    array index of first unused sub-sequence entry

ns_list
    links to adjacent name sequences in hash chain

subscriptions
    list of subscriptions for this 'type'

lock
    spinlock controlling access to publication lists of all sub-sequences

rcu
    RCU callback head used for deferred freeing

.. _`publ_create`:

publ_create
===========

.. c:function:: struct publication *publ_create(u32 type, u32 lower, u32 upper, u32 scope, u32 node, u32 port_ref, u32 key)

    create a publication structure

    :param u32 type:
        *undescribed*

    :param u32 lower:
        *undescribed*

    :param u32 upper:
        *undescribed*

    :param u32 scope:
        *undescribed*

    :param u32 node:
        *undescribed*

    :param u32 port_ref:
        *undescribed*

    :param u32 key:
        *undescribed*

.. _`tipc_subseq_alloc`:

tipc_subseq_alloc
=================

.. c:function:: struct sub_seq *tipc_subseq_alloc(u32 cnt)

    allocate a specified number of sub-sequence structures

    :param u32 cnt:
        *undescribed*

.. _`tipc_nameseq_create`:

tipc_nameseq_create
===================

.. c:function:: struct name_seq *tipc_nameseq_create(u32 type, struct hlist_head *seq_head)

    create a name sequence structure for the specified 'type'

    :param u32 type:
        *undescribed*

    :param struct hlist_head \*seq_head:
        *undescribed*

.. _`tipc_nameseq_create.description`:

Description
-----------

Allocates a single sub-sequence structure and sets it to all 0's.

.. _`nameseq_find_subseq`:

nameseq_find_subseq
===================

.. c:function:: struct sub_seq *nameseq_find_subseq(struct name_seq *nseq, u32 instance)

    find sub-sequence (if any) matching a name instance

    :param struct name_seq \*nseq:
        *undescribed*

    :param u32 instance:
        *undescribed*

.. _`nameseq_find_subseq.description`:

Description
-----------

Very time-critical, so binary searches through sub-sequence array.

.. _`nameseq_locate_subseq`:

nameseq_locate_subseq
=====================

.. c:function:: u32 nameseq_locate_subseq(struct name_seq *nseq, u32 instance)

    determine position of name instance in sub-sequence

    :param struct name_seq \*nseq:
        *undescribed*

    :param u32 instance:
        *undescribed*

.. _`nameseq_locate_subseq.description`:

Description
-----------

Returns index in sub-sequence array of the entry that contains the specified
instance value; if no entry contains that value, returns the position
where a new entry for it would be inserted in the array.

.. _`nameseq_locate_subseq.note`:

Note
----

Similar to binary search code for locating a sub-sequence.

.. _`tipc_nameseq_insert_publ`:

tipc_nameseq_insert_publ
========================

.. c:function:: struct publication *tipc_nameseq_insert_publ(struct net *net, struct name_seq *nseq, u32 type, u32 lower, u32 upper, u32 scope, u32 node, u32 port, u32 key)

    :param struct net \*net:
        *undescribed*

    :param struct name_seq \*nseq:
        *undescribed*

    :param u32 type:
        *undescribed*

    :param u32 lower:
        *undescribed*

    :param u32 upper:
        *undescribed*

    :param u32 scope:
        *undescribed*

    :param u32 node:
        *undescribed*

    :param u32 port:
        *undescribed*

    :param u32 key:
        *undescribed*

.. _`tipc_nameseq_remove_publ`:

tipc_nameseq_remove_publ
========================

.. c:function:: struct publication *tipc_nameseq_remove_publ(struct net *net, struct name_seq *nseq, u32 inst, u32 node, u32 ref, u32 key)

    :param struct net \*net:
        *undescribed*

    :param struct name_seq \*nseq:
        *undescribed*

    :param u32 inst:
        *undescribed*

    :param u32 node:
        *undescribed*

    :param u32 ref:
        *undescribed*

    :param u32 key:
        *undescribed*

.. _`tipc_nameseq_remove_publ.note`:

NOTE
----

There may be cases where TIPC is asked to remove a publication
that is not in the name table.  For example, if another node issues a
publication for a name sequence that overlaps an existing name sequence
the publication will not be recorded, which means the publication won't
be found when the name sequence is later withdrawn by that node.
A failed withdraw request simply returns a failure indication and lets the
caller issue any error or warning messages associated with such a problem.

.. _`tipc_nameseq_subscribe`:

tipc_nameseq_subscribe
======================

.. c:function:: void tipc_nameseq_subscribe(struct name_seq *nseq, struct tipc_subscription *s, bool status)

    attach a subscription, and optionally issue the prescribed number of events if there is any sub- sequence overlapping with the requested sequence

    :param struct name_seq \*nseq:
        *undescribed*

    :param struct tipc_subscription \*s:
        *undescribed*

    :param bool status:
        *undescribed*

.. _`tipc_nametbl_translate`:

tipc_nametbl_translate
======================

.. c:function:: u32 tipc_nametbl_translate(struct net *net, u32 type, u32 instance, u32 *destnode)

    perform name translation

    :param struct net \*net:
        *undescribed*

    :param u32 type:
        *undescribed*

    :param u32 instance:
        *undescribed*

    :param u32 \*destnode:
        *undescribed*

.. _`tipc_nametbl_translate.description`:

Description
-----------

On entry, 'destnode' is the search domain used during translation.

.. _`tipc_nametbl_translate.on-exit`:

On exit
-------

- if name translation is deferred to another node/cluster/zone,
leaves 'destnode' unchanged (will be non-zero) and returns 0
- if name translation is attempted and succeeds, sets 'destnode'
to publishing node and returns port reference (will be non-zero)
- if name translation is attempted and fails, sets 'destnode' to 0
and returns 0

.. _`tipc_nametbl_withdraw`:

tipc_nametbl_withdraw
=====================

.. c:function:: int tipc_nametbl_withdraw(struct net *net, u32 type, u32 lower, u32 ref, u32 key)

    withdraw name publication from network name tables

    :param struct net \*net:
        *undescribed*

    :param u32 type:
        *undescribed*

    :param u32 lower:
        *undescribed*

    :param u32 ref:
        *undescribed*

    :param u32 key:
        *undescribed*

.. _`tipc_nametbl_subscribe`:

tipc_nametbl_subscribe
======================

.. c:function:: void tipc_nametbl_subscribe(struct tipc_subscription *s, bool status)

    add a subscription object to the name table

    :param struct tipc_subscription \*s:
        *undescribed*

    :param bool status:
        *undescribed*

.. _`tipc_nametbl_unsubscribe`:

tipc_nametbl_unsubscribe
========================

.. c:function:: void tipc_nametbl_unsubscribe(struct tipc_subscription *s)

    remove a subscription object from name table

    :param struct tipc_subscription \*s:
        *undescribed*

.. _`tipc_purge_publications`:

tipc_purge_publications
=======================

.. c:function:: void tipc_purge_publications(struct net *net, struct name_seq *seq)

    remove all publications for a given type

    :param struct net \*net:
        *undescribed*

    :param struct name_seq \*seq:
        *undescribed*

.. _`tipc_purge_publications.description`:

Description
-----------

tipc_nametbl_lock must be held when calling this function

.. This file was automatic generated / don't edit.


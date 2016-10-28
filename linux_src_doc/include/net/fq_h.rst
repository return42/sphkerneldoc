.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/fq.h

.. _`fq_flow`:

struct fq_flow
==============

.. c:type:: struct fq_flow

    per traffic flow queue

.. _`fq_flow.definition`:

Definition
----------

.. code-block:: c

    struct fq_flow {
        struct fq_tin *tin;
        struct list_head flowchain;
        struct list_head backlogchain;
        struct sk_buff_head queue;
        u32 backlog;
        int deficit;
    }

.. _`fq_flow.members`:

Members
-------

tin
    owner of this flow. Used to manage collisions, i.e. when a packet
    hashes to an index which points to a flow that is already owned by a
    different tin the packet is destined to. In such case the implementer
    must provide a fallback flow

flowchain
    can be linked to fq_tin's new_flows or old_flows. Used for DRR++
    (deficit round robin) based round robin queuing similar to the one
    found in net/sched/sch_fq_codel.c

backlogchain
    can be linked to other fq_flow and fq. Used to keep track of
    fat flows and efficient head-dropping if packet limit is reached

queue
    sk_buff queue to hold packets

backlog
    number of bytes pending in the queue. The number of packets can be
    found in \ ``queue``\ .qlen

deficit
    used for DRR++

.. _`fq_tin`:

struct fq_tin
=============

.. c:type:: struct fq_tin

    a logical container of fq_flows

.. _`fq_tin.definition`:

Definition
----------

.. code-block:: c

    struct fq_tin {
        struct list_head new_flows;
        struct list_head old_flows;
        u32 backlog_bytes;
        u32 backlog_packets;
        u32 overlimit;
        u32 collisions;
        u32 flows;
        u32 tx_bytes;
        u32 tx_packets;
    }

.. _`fq_tin.members`:

Members
-------

new_flows
    linked list of fq_flow

old_flows
    linked list of fq_flow

backlog_bytes
    *undescribed*

backlog_packets
    *undescribed*

overlimit
    *undescribed*

collisions
    *undescribed*

flows
    *undescribed*

tx_bytes
    *undescribed*

tx_packets
    *undescribed*

.. _`fq_tin.description`:

Description
-----------

Used to group fq_flows into a logical aggregate. DRR++ scheme is used to
pull interleaved packets out of the associated flows.

.. _`fq`:

struct fq
=========

.. c:type:: struct fq

    main container for fair queuing purposes

.. _`fq.definition`:

Definition
----------

.. code-block:: c

    struct fq {
        struct fq_flow *flows;
        struct list_head backlogs;
        spinlock_t lock;
        u32 flows_cnt;
        u32 perturbation;
        u32 limit;
        u32 quantum;
        u32 backlog;
        u32 overlimit;
        u32 collisions;
    }

.. _`fq.members`:

Members
-------

flows
    *undescribed*

backlogs
    linked to fq_flows. Used to maintain fat flows for efficient
    head-dropping when \ ``backlog``\  reaches \ ``limit``\ 

lock
    *undescribed*

flows_cnt
    *undescribed*

perturbation
    *undescribed*

limit
    max number of packets that can be queued across all flows

quantum
    *undescribed*

backlog
    number of packets queued across all flows

overlimit
    *undescribed*

collisions
    *undescribed*

.. This file was automatic generated / don't edit.


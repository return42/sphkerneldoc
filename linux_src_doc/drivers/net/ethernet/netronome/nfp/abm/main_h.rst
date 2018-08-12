.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/abm/main.h

.. _`nfp_abm`:

struct nfp_abm
==============

.. c:type:: struct nfp_abm

    ABM NIC app structure

.. _`nfp_abm.definition`:

Definition
----------

.. code-block:: c

    struct nfp_abm {
        struct nfp_app *app;
        unsigned int pf_id;
        enum devlink_eswitch_mode eswitch_mode;
        const struct nfp_rtsym *q_lvls;
        const struct nfp_rtsym *qm_stats;
    }

.. _`nfp_abm.members`:

Members
-------

app
    back pointer to nfp_app

pf_id
    ID of our PF link

eswitch_mode
    devlink eswitch mode, advanced functions only visible
    in switchdev mode

q_lvls
    queue level control area

qm_stats
    queue statistics symbol

.. _`nfp_alink_stats`:

struct nfp_alink_stats
======================

.. c:type:: struct nfp_alink_stats

    ABM NIC statistics

.. _`nfp_alink_stats.definition`:

Definition
----------

.. code-block:: c

    struct nfp_alink_stats {
        u64 tx_pkts;
        u64 tx_bytes;
        u64 backlog_pkts;
        u64 backlog_bytes;
        u64 overlimits;
        u64 drops;
    }

.. _`nfp_alink_stats.members`:

Members
-------

tx_pkts
    number of TXed packets

tx_bytes
    number of TXed bytes

backlog_pkts
    momentary backlog length (packets)

backlog_bytes
    momentary backlog length (bytes)

overlimits
    number of ECN marked TXed packets (accumulative)

drops
    number of tail-dropped packets (accumulative)

.. _`nfp_alink_xstats`:

struct nfp_alink_xstats
=======================

.. c:type:: struct nfp_alink_xstats

    extended ABM NIC statistics

.. _`nfp_alink_xstats.definition`:

Definition
----------

.. code-block:: c

    struct nfp_alink_xstats {
        u64 ecn_marked;
        u64 pdrop;
    }

.. _`nfp_alink_xstats.members`:

Members
-------

ecn_marked
    number of ECN marked TXed packets

pdrop
    number of hard drops due to queue limit

.. _`nfp_red_qdisc`:

struct nfp_red_qdisc
====================

.. c:type:: struct nfp_red_qdisc

    representation of single RED Qdisc

.. _`nfp_red_qdisc.definition`:

Definition
----------

.. code-block:: c

    struct nfp_red_qdisc {
        u32 handle;
        struct nfp_alink_stats stats;
        struct nfp_alink_xstats xstats;
    }

.. _`nfp_red_qdisc.members`:

Members
-------

handle
    handle of currently offloaded RED Qdisc

stats
    statistics from last refresh

xstats
    base of extended statistics

.. _`nfp_abm_link`:

struct nfp_abm_link
===================

.. c:type:: struct nfp_abm_link

    port tuple of a ABM NIC

.. _`nfp_abm_link.definition`:

Definition
----------

.. code-block:: c

    struct nfp_abm_link {
        struct nfp_abm *abm;
        struct nfp_net *vnic;
        unsigned int id;
        unsigned int queue_base;
        unsigned int total_queues;
        u32 parent;
        unsigned int num_qdiscs;
        struct nfp_red_qdisc *qdiscs;
    }

.. _`nfp_abm_link.members`:

Members
-------

abm
    back pointer to nfp_abm

vnic
    data vNIC

id
    id of the data vNIC

queue_base
    id of base to host queue within PCIe (not QC idx)

total_queues
    number of PF queues

parent
    handle of expected parent, i.e. handle of MQ, or TC_H_ROOT

num_qdiscs
    number of currently used qdiscs

qdiscs
    array of qdiscs

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfp_net_repr.h

.. _`nfp_reprs`:

struct nfp_reprs
================

.. c:type:: struct nfp_reprs

    container for representor netdevs

.. _`nfp_reprs.definition`:

Definition
----------

.. code-block:: c

    struct nfp_reprs {
        unsigned int num_reprs;
        struct net_device *reprs[0];
    }

.. _`nfp_reprs.members`:

Members
-------

num_reprs
    Number of elements in reprs array

reprs
    Array of representor netdevs

.. _`nfp_repr_pcpu_stats`:

struct nfp_repr_pcpu_stats
==========================

.. c:type:: struct nfp_repr_pcpu_stats


.. _`nfp_repr_pcpu_stats.definition`:

Definition
----------

.. code-block:: c

    struct nfp_repr_pcpu_stats {
        u64 rx_packets;
        u64 rx_bytes;
        u64 tx_packets;
        u64 tx_bytes;
        u64 tx_drops;
        struct u64_stats_sync syncp;
    }

.. _`nfp_repr_pcpu_stats.members`:

Members
-------

rx_packets
    Received packets

rx_bytes
    Received bytes

tx_packets
    Transmitted packets

tx_bytes
    Transmitted dropped

tx_drops
    Packets dropped on transmit

syncp
    Reference count

.. _`nfp_repr`:

struct nfp_repr
===============

.. c:type:: struct nfp_repr

    priv data for representor netdevs

.. _`nfp_repr.definition`:

Definition
----------

.. code-block:: c

    struct nfp_repr {
        struct net_device *netdev;
        struct metadata_dst *dst;
        struct nfp_port *port;
        struct nfp_app *app;
        struct nfp_repr_pcpu_stats __percpu *stats;
    }

.. _`nfp_repr.members`:

Members
-------

netdev
    Back pointer to netdev

dst
    Destination for packet TX

port
    Port of representor

app
    APP handle

stats
    Statistic of packets hitting CPU

.. _`nfp_repr_type`:

enum nfp_repr_type
==================

.. c:type:: enum nfp_repr_type

    type of representor

.. _`nfp_repr_type.definition`:

Definition
----------

.. code-block:: c

    enum nfp_repr_type {
        NFP_REPR_TYPE_PHYS_PORT,
        NFP_REPR_TYPE_PF,
        NFP_REPR_TYPE_VF,
        __NFP_REPR_TYPE_MAX
    };

.. _`nfp_repr_type.constants`:

Constants
---------

NFP_REPR_TYPE_PHYS_PORT
    external NIC port

NFP_REPR_TYPE_PF
    physical function

NFP_REPR_TYPE_VF
    virtual function

__NFP_REPR_TYPE_MAX
    *undescribed*

.. This file was automatic generated / don't edit.


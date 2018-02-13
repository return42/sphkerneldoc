.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfp_port.h

.. _`nfp_port_type`:

enum nfp_port_type
==================

.. c:type:: enum nfp_port_type

    type of port NFP can switch traffic to

.. _`nfp_port_type.definition`:

Definition
----------

.. code-block:: c

    enum nfp_port_type {
        NFP_PORT_INVALID,
        NFP_PORT_PHYS_PORT,
        NFP_PORT_PF_PORT,
        NFP_PORT_VF_PORT
    };

.. _`nfp_port_type.constants`:

Constants
---------

NFP_PORT_INVALID
    port is invalid, \ ``NFP_PORT_PHYS_PORT``\  transitions to this
    state when port disappears because of FW fault or config
    change

NFP_PORT_PHYS_PORT
    external NIC port

NFP_PORT_PF_PORT
    logical port of PCI PF

NFP_PORT_VF_PORT
    logical port of PCI VF

.. _`nfp_port_flags`:

enum nfp_port_flags
===================

.. c:type:: enum nfp_port_flags

    port flags (can be type-specific)

.. _`nfp_port_flags.definition`:

Definition
----------

.. code-block:: c

    enum nfp_port_flags {
        NFP_PORT_CHANGED
    };

.. _`nfp_port_flags.constants`:

Constants
---------

NFP_PORT_CHANGED
    port state has changed since last eth table refresh;
    for NFP_PORT_PHYS_PORT, never set otherwise; must hold
    rtnl_lock to clear

.. _`nfp_port`:

struct nfp_port
===============

.. c:type:: struct nfp_port

    structure representing NFP port

.. _`nfp_port.definition`:

Definition
----------

.. code-block:: c

    struct nfp_port {
        struct net_device *netdev;
        enum nfp_port_type type;
        unsigned long flags;
        unsigned long tc_offload_cnt;
        struct nfp_app *app;
        struct devlink_port dl_port;
        union {
            struct {
                unsigned int eth_id;
                struct nfp_eth_table_port *eth_port;
                u8 __iomem *eth_stats;
            } ;
            struct {
                unsigned int pf_id;
                unsigned int vf_id;
                u8 __iomem *vnic;
            } ;
        } ;
        struct list_head port_list;
    }

.. _`nfp_port.members`:

Members
-------

netdev
    backpointer to associated netdev

type
    what port type does the entity represent

flags
    port flags

tc_offload_cnt
    number of active TC offloads, how offloads are counted
    is not defined, use as a boolean

app
    backpointer to the app structure

dl_port
    devlink port structure

{unnamed_union}
    anonymous

{unnamed_struct}
    anonymous

eth_id
    for \ ``NFP_PORT_PHYS_PORT``\  port ID in NFP enumeration scheme

eth_port
    for \ ``NFP_PORT_PHYS_PORT``\  translated ETH Table port entry

eth_stats
    for \ ``NFP_PORT_PHYS_PORT``\  MAC stats if available

{unnamed_struct}
    anonymous

pf_id
    for \ ``NFP_PORT_PF_PORT``\ , \ ``NFP_PORT_VF_PORT``\  ID of the PCI PF (0-3)

vf_id
    for \ ``NFP_PORT_VF_PORT``\  ID of the PCI VF within \ ``pf_id``\ 

vnic
    for \ ``NFP_PORT_PF_PORT``\ , \ ``NFP_PORT_VF_PORT``\  vNIC ctrl memory

port_list
    entry on pf's list of ports

.. _`nfp_mac_stats_base`:

NFP_MAC_STATS_BASE
==================

.. c:function::  NFP_MAC_STATS_BASE()

    0x0200) all counters are 64bit.

.. This file was automatic generated / don't edit.


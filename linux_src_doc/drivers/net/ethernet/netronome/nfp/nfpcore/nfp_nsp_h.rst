.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfpcore/nfp_nsp.h

.. _`nfp_eth_table`:

struct nfp_eth_table
====================

.. c:type:: struct nfp_eth_table

    ETH table information

.. _`nfp_eth_table.definition`:

Definition
----------

.. code-block:: c

    struct nfp_eth_table {
        unsigned int count;
        unsigned int max_index;
        struct nfp_eth_table_port {
            unsigned int eth_index;
            unsigned int index;
            unsigned int nbi;
            unsigned int base;
            unsigned int lanes;
            unsigned int speed;
            unsigned int interface;
            enum nfp_eth_media media;
            enum nfp_eth_fec fec;
            enum nfp_eth_aneg aneg;
            u8 mac_addr[ETH_ALEN];
            u8 label_port;
            u8 label_subport;
            bool enabled;
            bool tx_enabled;
            bool rx_enabled;
            bool override_changed;
            u8 port_type;
            unsigned int port_lanes;
            bool is_split;
            unsigned int fec_modes_supported;
        } ports[0];
    }

.. _`nfp_eth_table.members`:

Members
-------

count
    number of table entries

max_index
    max of \ ``index``\  fields of all \ ``ports``\ 

ports
    table of ports

ports.eth_index
    port index according to legacy ethX numbering

ports.index
    chip-wide first channel index

ports.nbi
    NBI index

ports.base
    first channel index (within NBI)

ports.lanes
    number of channels

ports.speed
    interface speed (in Mbps)

ports.interface
    interface (module) plugged in

ports.media
    media type of the \ ``interface``\ 

ports.fec
    forward error correction mode

ports.aneg
    auto negotiation mode

ports.mac_addr
    interface MAC address

ports.label_port
    port id

ports.label_subport
    id of interface within port (for split ports)

ports.enabled
    is enabled?

ports.tx_enabled
    is TX enabled?

ports.rx_enabled
    is RX enabled?

ports.override_changed
    is media reconfig pending?

ports.port_type
    one of \ ``PORT``\ \_\* defines for ethtool

ports.port_lanes
    total number of lanes on the port (sum of lanes of all
    subports)

ports.is_split
    is interface part of a split port

ports.fec_modes_supported
    bitmap of FEC modes supported

.. _`nfp_nsp_identify`:

struct nfp_nsp_identify
=======================

.. c:type:: struct nfp_nsp_identify

    NSP static information

.. _`nfp_nsp_identify.definition`:

Definition
----------

.. code-block:: c

    struct nfp_nsp_identify {
        char version[40];
        u8 flags;
        u8 br_primary;
        u8 br_secondary;
        u8 br_nsp;
        u16 primary;
        u16 secondary;
        u16 nsp;
        u64 sensor_mask;
    }

.. _`nfp_nsp_identify.members`:

Members
-------

version
    opaque version string

flags
    version flags

br_primary
    branch id of primary bootloader

br_secondary
    branch id of secondary bootloader

br_nsp
    branch id of NSP

primary
    version of primarary bootloader

secondary
    version id of secondary bootloader

nsp
    version id of NSP

sensor_mask
    mask of present sensors available on NIC

.. This file was automatic generated / don't edit.


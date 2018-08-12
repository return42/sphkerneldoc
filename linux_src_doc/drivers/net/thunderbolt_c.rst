.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/thunderbolt.c

.. _`thunderbolt_ip_frame_header`:

struct thunderbolt_ip_frame_header
==================================

.. c:type:: struct thunderbolt_ip_frame_header

    Header for each Thunderbolt frame

.. _`thunderbolt_ip_frame_header.definition`:

Definition
----------

.. code-block:: c

    struct thunderbolt_ip_frame_header {
        u32 frame_size;
        u16 frame_index;
        u16 frame_id;
        u32 frame_count;
    }

.. _`thunderbolt_ip_frame_header.members`:

Members
-------

frame_size
    size of the data with the frame

frame_index
    running index on the frames

frame_id
    ID of the frame to match frames to specific packet

frame_count
    how many frames assembles a full packet

.. _`thunderbolt_ip_frame_header.description`:

Description
-----------

Each data frame passed to the high-speed DMA ring has this header. If
the XDomain network directory announces that \ ``TBNET_MATCH_FRAGS_ID``\  is
supported then \ ``frame_id``\  is filled, otherwise it stays \ ``0``\ .

.. _`tbnet`:

struct tbnet
============

.. c:type:: struct tbnet

    ThunderboltIP network driver private data

.. _`tbnet.definition`:

Definition
----------

.. code-block:: c

    struct tbnet {
        const struct tb_service *svc;
        struct tb_xdomain *xd;
        struct tb_protocol_handler handler;
        struct net_device *dev;
        struct napi_struct napi;
        struct tbnet_stats stats;
        struct sk_buff *skb;
        atomic_t command_id;
        bool login_sent;
        bool login_received;
        u32 transmit_path;
        struct mutex connection_lock;
        int login_retries;
        struct delayed_work login_work;
        struct work_struct connected_work;
        struct work_struct disconnect_work;
        struct thunderbolt_ip_frame_header rx_hdr;
        struct tbnet_ring rx_ring;
        atomic_t frame_id;
        struct tbnet_ring tx_ring;
    }

.. _`tbnet.members`:

Members
-------

svc
    XDomain service the driver is bound to

xd
    XDomain the service blongs to

handler
    ThunderboltIP configuration protocol handler

dev
    Networking device

napi
    NAPI structure for Rx polling

stats
    Network statistics

skb
    Network packet that is currently processed on Rx path

command_id
    ID used for next configuration protocol packet

login_sent
    ThunderboltIP login message successfully sent

login_received
    ThunderboltIP login message received from the remote
    host

transmit_path
    HopID the other end needs to use building the
    opposite side path.

connection_lock
    Lock serializing access to \ ``login_sent``\ ,
    \ ``login_received``\  and \ ``transmit_path``\ .

login_retries
    Number of login retries currently done

login_work
    Worker to send ThunderboltIP login packets

connected_work
    Worker that finalizes the ThunderboltIP connection
    setup and enables DMA paths for high speed data
    transfers

disconnect_work
    Worker that handles tearing down the ThunderboltIP
    connection

rx_hdr
    Copy of the currently processed Rx frame. Used when a
    network packet consists of multiple Thunderbolt frames.
    In host byte order.

rx_ring
    Software ring holding Rx frames

frame_id
    Frame ID use for next Tx packet
    (if \ ``TBNET_MATCH_FRAGS_ID``\  is supported in both ends)

tx_ring
    Software ring holding Tx frames

.. This file was automatic generated / don't edit.


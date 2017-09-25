.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/scsi/libfcoe.h

.. _`fip_state`:

enum fip_state
==============

.. c:type:: enum fip_state

    internal state of FCoE controller.

.. _`fip_state.definition`:

Definition
----------

.. code-block:: c

    enum fip_state {
        FIP_ST_DISABLED,
        FIP_ST_LINK_WAIT,
        FIP_ST_AUTO,
        FIP_ST_NON_FIP,
        FIP_ST_ENABLED,
        FIP_ST_VNMP_START,
        FIP_ST_VNMP_PROBE1,
        FIP_ST_VNMP_PROBE2,
        FIP_ST_VNMP_CLAIM,
        FIP_ST_VNMP_UP
    };

.. _`fip_state.constants`:

Constants
---------

FIP_ST_DISABLED
    controller has been disabled or not yet enabled.

FIP_ST_LINK_WAIT
    the physical link is down or unusable.

FIP_ST_AUTO
    determining whether to use FIP or non-FIP mode.

FIP_ST_NON_FIP
    non-FIP mode selected.

FIP_ST_ENABLED
    FIP mode selected.

FIP_ST_VNMP_START
    VN2VN multipath mode start, wait

FIP_ST_VNMP_PROBE1
    VN2VN sent first probe, listening

FIP_ST_VNMP_PROBE2
    VN2VN sent second probe, listening

FIP_ST_VNMP_CLAIM
    VN2VN sent claim, waiting for responses

FIP_ST_VNMP_UP
    VN2VN multipath mode operation

.. _`fcoe_ctlr`:

struct fcoe_ctlr
================

.. c:type:: struct fcoe_ctlr

    FCoE Controller and FIP state

.. _`fcoe_ctlr.definition`:

Definition
----------

.. code-block:: c

    struct fcoe_ctlr {
        enum fip_state state;
        enum fip_mode mode;
        struct fc_lport *lp;
        struct fcoe_fcf *sel_fcf;
        struct list_head fcfs;
        struct fcoe_ctlr_device *cdev;
        u16 fcf_count;
        unsigned long sol_time;
        unsigned long sel_time;
        unsigned long port_ka_time;
        unsigned long ctlr_ka_time;
        struct timer_list timer;
        struct work_struct timer_work;
        struct work_struct recv_work;
        struct sk_buff_head fip_recv_list;
        struct sk_buff *flogi_req;
        struct rnd_state rnd_state;
        u32 port_id;
        u16 user_mfs;
        u16 flogi_oxid;
        u8 flogi_req_send;
        u8 flogi_count;
        bool map_dest;
        bool fip_resp;
        u8 spma;
        u8 probe_tries;
        u8 priority;
        u8 dest_addr[ETH_ALEN];
        u8 ctl_src_addr[ETH_ALEN];
        void (*send)(struct fcoe_ctlr *, struct sk_buff *);
        void (*update_mac)(struct fc_lport *, u8 *addr);
        u8 * (*get_src_addr)(struct fc_lport *);
        struct mutex ctlr_mutex;
        spinlock_t ctlr_lock;
    }

.. _`fcoe_ctlr.members`:

Members
-------

state
    internal FIP state for network link and FIP or non-FIP mode.

mode
    LLD-selected mode.

lp
    &fc_lport: libfc local port.

sel_fcf
    currently selected FCF, or NULL.

fcfs
    list of discovered FCFs.

cdev
    (Optional) pointer to sysfs fcoe_ctlr_device.

fcf_count
    number of discovered FCF entries.

sol_time
    time when a multicast solicitation was last sent.

sel_time
    time after which to select an FCF.

port_ka_time
    time of next port keep-alive.

ctlr_ka_time
    time of next controller keep-alive.

timer
    timer struct used for all delayed events.

timer_work
    &work_struct for doing keep-alives and resets.

recv_work
    &work_struct for receiving FIP frames.

fip_recv_list
    list of received FIP frames.

flogi_req
    clone of FLOGI request sent

rnd_state
    state for pseudo-random number generator.

port_id
    proposed or selected local-port ID.

user_mfs
    configured maximum FC frame size, including FC header.

flogi_oxid
    exchange ID of most recent fabric login.

flogi_req_send
    send of FLOGI requested

flogi_count
    number of FLOGI attempts in AUTO mode.

map_dest
    use the FC_MAP mode for destination MAC addresses.

fip_resp
    start FIP VLAN discovery responder

spma
    supports SPMA server-provided MACs mode

probe_tries
    number of FC_IDs probed

priority
    DCBx FCoE APP priority

dest_addr
    MAC address of the selected FC forwarder.

ctl_src_addr
    the native MAC address of our local port.

send
    LLD-supplied function to handle sending FIP Ethernet frames

update_mac
    LLD-supplied function to handle changes to MAC addresses.

get_src_addr
    LLD-supplied function to supply a source MAC address.

ctlr_mutex
    lock protecting this structure.

ctlr_lock
    spinlock covering flogi_req

.. _`fcoe_ctlr.description`:

Description
-----------

This structure is used by all FCoE drivers.  It contains information
needed by all FCoE low-level drivers (LLDs) as well as internal state
for FIP, and fields shared with the LLDS.

.. _`fcoe_ctlr_priv`:

fcoe_ctlr_priv
==============

.. c:function:: void *fcoe_ctlr_priv(const struct fcoe_ctlr *ctlr)

    Return the private data from a fcoe_ctlr

    :param const struct fcoe_ctlr \*ctlr:
        *undescribed*

.. _`fcoe_fcf`:

struct fcoe_fcf
===============

.. c:type:: struct fcoe_fcf

    Fibre-Channel Forwarder

.. _`fcoe_fcf.definition`:

Definition
----------

.. code-block:: c

    struct fcoe_fcf {
        struct list_head list;
        struct work_struct event_work;
        struct fcoe_ctlr *fip;
        struct fcoe_fcf_device *fcf_dev;
        unsigned long time;
        u64 switch_name;
        u64 fabric_name;
        u32 fc_map;
        u16 vfid;
        u8 fcf_mac[ETH_ALEN];
        u8 fcoe_mac[ETH_ALEN];
        u8 pri;
        u8 flogi_sent;
        u16 flags;
        u32 fka_period;
        u8 fd_flags:1;
    }

.. _`fcoe_fcf.members`:

Members
-------

list
    list linkage

event_work
    Work for FC Transport actions queue

fip
    The controller that the FCF was discovered on

fcf_dev
    The associated fcoe_fcf_device instance

time
    system time (jiffies) when an advertisement was last received

switch_name
    WWN of switch from advertisement

fabric_name
    WWN of fabric from advertisement

fc_map
    FC_MAP value from advertisement

vfid
    virtual fabric ID

fcf_mac
    Ethernet address of the FCF for FIP traffic

fcoe_mac
    Ethernet address of the FCF for FCoE traffic

pri
    selection priority, smaller values are better

flogi_sent
    current FLOGI sent to this FCF

flags
    flags received from advertisement

fka_period
    keep-alive period, in jiffies

fd_flags
    *undescribed*

.. _`fcoe_fcf.description`:

Description
-----------

A Fibre-Channel Forwarder (FCF) is the entity on the Ethernet that
passes FCoE frames on to an FC fabric.  This structure represents
one FCF from which advertisements have been received.

When looking up an FCF, \ ``switch_name``\ , \ ``fabric_name``\ , \ ``fc_map``\ , \ ``vfid``\ , and
\ ``fcf_mac``\  together form the lookup key.

.. _`fcoe_rport`:

struct fcoe_rport
=================

.. c:type:: struct fcoe_rport

    VN2VN remote port

.. _`fcoe_rport.definition`:

Definition
----------

.. code-block:: c

    struct fcoe_rport {
        unsigned long time;
        u16 fcoe_len;
        u16 flags;
        u8 login_count;
        u8 enode_mac[ETH_ALEN];
        u8 vn_mac[ETH_ALEN];
    }

.. _`fcoe_rport.members`:

Members
-------

time
    time of create or last beacon packet received from node

fcoe_len
    max FCoE frame size, not including VLAN or Ethernet headers

flags
    flags from probe or claim

login_count
    number of unsuccessful rport logins to this port

enode_mac
    E_Node control MAC address

vn_mac
    VN_Node assigned MAC address for data

.. _`is_fip_mode`:

is_fip_mode
===========

.. c:function:: bool is_fip_mode(struct fcoe_ctlr *fip)

    returns true if FIP mode selected.

    :param struct fcoe_ctlr \*fip:
        FCoE controller.

.. _`fcoe_percpu_s`:

struct fcoe_percpu_s
====================

.. c:type:: struct fcoe_percpu_s

    The context for FCoE receive thread(s)

.. _`fcoe_percpu_s.definition`:

Definition
----------

.. code-block:: c

    struct fcoe_percpu_s {
        struct task_struct *kthread;
        struct work_struct work;
        struct sk_buff_head fcoe_rx_list;
        struct page *crc_eof_page;
        int crc_eof_offset;
    }

.. _`fcoe_percpu_s.members`:

Members
-------

kthread
    The thread context (used by bnx2fc)

work
    The work item (used by fcoe)

fcoe_rx_list
    The queue of pending packets to process

crc_eof_page
    *undescribed*

crc_eof_offset
    The offset into the CRC page pointing to available
    memory for a new trailer

.. _`fcoe_port`:

struct fcoe_port
================

.. c:type:: struct fcoe_port

    The FCoE private structure

.. _`fcoe_port.definition`:

Definition
----------

.. code-block:: c

    struct fcoe_port {
        void *priv;
        struct fc_lport *lport;
        struct sk_buff_head fcoe_pending_queue;
        u8 fcoe_pending_queue_active;
        u32 max_queue_depth;
        u32 min_queue_depth;
        struct timer_list timer;
        struct work_struct destroy_work;
        u8 data_src_addr[ETH_ALEN];
        struct net_device * (*get_netdev)(const struct fc_lport *lport);
    }

.. _`fcoe_port.members`:

Members
-------

priv
    The associated fcoe interface. The structure is
    defined by the low level driver

lport
    The associated local port

fcoe_pending_queue
    The pending Rx queue of skbs

fcoe_pending_queue_active
    Indicates if the pending queue is active

max_queue_depth
    Max queue depth of pending queue

min_queue_depth
    Min queue depth of pending queue

timer
    The queue timer

destroy_work
    Handle for work context
    (to prevent RTNL deadlocks)

data_src_addr
    *undescribed*

get_netdev
    *undescribed*

.. _`fcoe_port.description`:

Description
-----------

An instance of this structure is to be allocated along with the
Scsi_Host and libfc fc_lport structures.

.. _`fcoe_get_netdev`:

fcoe_get_netdev
===============

.. c:function:: struct net_device *fcoe_get_netdev(const struct fc_lport *lport)

    Return the net device associated with a local port

    :param const struct fc_lport \*lport:
        The local port to get the net device from

.. _`fcoe_netdev_mapping`:

struct fcoe_netdev_mapping
==========================

.. c:type:: struct fcoe_netdev_mapping

    A mapping from netdevice to fcoe_transport

.. _`fcoe_netdev_mapping.definition`:

Definition
----------

.. code-block:: c

    struct fcoe_netdev_mapping {
        struct list_head list;
        struct net_device *netdev;
        struct fcoe_transport *ft;
    }

.. _`fcoe_netdev_mapping.members`:

Members
-------

list
    *undescribed*

netdev
    *undescribed*

ft
    *undescribed*

.. This file was automatic generated / don't edit.


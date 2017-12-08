.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/netdevice.h

.. _`napi_schedule`:

napi_schedule
=============

.. c:function:: void napi_schedule(struct napi_struct *n)

    schedule NAPI poll

    :param struct napi_struct \*n:
        NAPI context

.. _`napi_schedule.description`:

Description
-----------

Schedule NAPI poll routine to be called if it is not already
running.

.. _`napi_schedule_irqoff`:

napi_schedule_irqoff
====================

.. c:function:: void napi_schedule_irqoff(struct napi_struct *n)

    schedule NAPI poll

    :param struct napi_struct \*n:
        NAPI context

.. _`napi_schedule_irqoff.description`:

Description
-----------

Variant of \ :c:func:`napi_schedule`\ , assuming hard irqs are masked.

.. _`napi_complete`:

napi_complete
=============

.. c:function:: bool napi_complete(struct napi_struct *n)

    NAPI processing complete

    :param struct napi_struct \*n:
        NAPI context

.. _`napi_complete.description`:

Description
-----------

Mark NAPI processing as complete.
Consider using \ :c:func:`napi_complete_done`\  instead.
Return false if device should avoid rearming interrupts.

.. _`napi_hash_del`:

napi_hash_del
=============

.. c:function:: bool napi_hash_del(struct napi_struct *napi)

    remove a NAPI from global table

    :param struct napi_struct \*napi:
        NAPI context

.. _`napi_hash_del.description`:

Description
-----------

Warning: caller must observe RCU grace period
before freeing memory containing \ ``napi``\ , if
this function returns true.

.. _`napi_hash_del.note`:

Note
----

core networking stack automatically calls it
from \ :c:func:`netif_napi_del`\ .
Drivers might want to call this helper to combine all
the needed RCU grace periods into a single one.

.. _`napi_disable`:

napi_disable
============

.. c:function:: void napi_disable(struct napi_struct *n)

    prevent NAPI from scheduling

    :param struct napi_struct \*n:
        NAPI context

.. _`napi_disable.description`:

Description
-----------

Stop NAPI from being scheduled on this context.
Waits till any outstanding processing completes.

.. _`napi_enable`:

napi_enable
===========

.. c:function:: void napi_enable(struct napi_struct *n)

    enable NAPI scheduling

    :param struct napi_struct \*n:
        NAPI context

.. _`napi_enable.description`:

Description
-----------

Resume NAPI from being scheduled on this context.
Must be paired with napi_disable.

.. _`napi_synchronize`:

napi_synchronize
================

.. c:function:: void napi_synchronize(const struct napi_struct *n)

    wait until NAPI is not running

    :param const struct napi_struct \*n:
        NAPI context

.. _`napi_synchronize.description`:

Description
-----------

Wait until NAPI is done being scheduled on this context.
Waits till any outstanding processing completes but
does not disable future activations.

.. _`netdev_priv_flags`:

enum netdev_priv_flags
======================

.. c:type:: enum netdev_priv_flags

    &struct net_device priv_flags

.. _`netdev_priv_flags.definition`:

Definition
----------

.. code-block:: c

    enum netdev_priv_flags {
        IFF_802_1Q_VLAN,
        IFF_EBRIDGE,
        IFF_BONDING,
        IFF_ISATAP,
        IFF_WAN_HDLC,
        IFF_XMIT_DST_RELEASE,
        IFF_DONT_BRIDGE,
        IFF_DISABLE_NETPOLL,
        IFF_MACVLAN_PORT,
        IFF_BRIDGE_PORT,
        IFF_OVS_DATAPATH,
        IFF_TX_SKB_SHARING,
        IFF_UNICAST_FLT,
        IFF_TEAM_PORT,
        IFF_SUPP_NOFCS,
        IFF_LIVE_ADDR_CHANGE,
        IFF_MACVLAN,
        IFF_XMIT_DST_RELEASE_PERM,
        IFF_IPVLAN_MASTER,
        IFF_IPVLAN_SLAVE,
        IFF_L3MDEV_MASTER,
        IFF_NO_QUEUE,
        IFF_OPENVSWITCH,
        IFF_L3MDEV_SLAVE,
        IFF_TEAM,
        IFF_RXFH_CONFIGURED,
        IFF_PHONY_HEADROOM,
        IFF_MACSEC
    };

.. _`netdev_priv_flags.constants`:

Constants
---------

IFF_802_1Q_VLAN
    802.1Q VLAN device

IFF_EBRIDGE
    Ethernet bridging device

IFF_BONDING
    bonding master or slave

IFF_ISATAP
    ISATAP interface (RFC4214)

IFF_WAN_HDLC
    WAN HDLC device

IFF_XMIT_DST_RELEASE
    dev_hard_start_xmit() is allowed to
    release skb->dst

IFF_DONT_BRIDGE
    disallow bridging this ether dev

IFF_DISABLE_NETPOLL
    disable netpoll at run-time

IFF_MACVLAN_PORT
    device used as macvlan port

IFF_BRIDGE_PORT
    device used as bridge port

IFF_OVS_DATAPATH
    device used as Open vSwitch datapath port

IFF_TX_SKB_SHARING
    The interface supports sharing skbs on transmit

IFF_UNICAST_FLT
    Supports unicast filtering

IFF_TEAM_PORT
    device used as team port

IFF_SUPP_NOFCS
    device supports sending custom FCS

IFF_LIVE_ADDR_CHANGE
    device supports hardware address
    change when it's running

IFF_MACVLAN
    Macvlan device

IFF_XMIT_DST_RELEASE_PERM
    IFF_XMIT_DST_RELEASE not taking into account
    underlying stacked devices

IFF_IPVLAN_MASTER
    IPvlan master device

IFF_IPVLAN_SLAVE
    IPvlan slave device

IFF_L3MDEV_MASTER
    device is an L3 master device

IFF_NO_QUEUE
    device can run without qdisc attached

IFF_OPENVSWITCH
    device is a Open vSwitch master

IFF_L3MDEV_SLAVE
    device is enslaved to an L3 master device

IFF_TEAM
    device is a team device

IFF_RXFH_CONFIGURED
    device has had Rx Flow indirection table configured

IFF_PHONY_HEADROOM
    the headroom value is controlled by an external
    entity (i.e. the master device for bridged veth)

IFF_MACSEC
    device is a MACsec device

.. _`netdev_priv_flags.description`:

Description
-----------

These are the \ :c:type:`struct net_device <net_device>`\ , they are only set internally
by drivers and used in the kernel. These flags are invisible to
userspace; this means that the order of these flags can change
during any kernel release.

You should have a pretty good reason to be extending these flags.

.. _`net_device`:

struct net_device
=================

.. c:type:: struct net_device

    The DEVICE structure.

.. _`net_device.definition`:

Definition
----------

.. code-block:: c

    struct net_device {
        char name[IFNAMSIZ];
        struct hlist_node name_hlist;
        struct dev_ifalias __rcu *ifalias;
        unsigned long mem_end;
        unsigned long mem_start;
        unsigned long base_addr;
        int irq;
        atomic_t carrier_changes;
        unsigned long state;
        struct list_head dev_list;
        struct list_head napi_list;
        struct list_head unreg_list;
        struct list_head close_list;
        struct list_head ptype_all;
        struct list_head ptype_specific;
        struct {
            struct list_head upper;
            struct list_head lower;
        } adj_list;
        netdev_features_t features;
        netdev_features_t hw_features;
        netdev_features_t wanted_features;
        netdev_features_t vlan_features;
        netdev_features_t hw_enc_features;
        netdev_features_t mpls_features;
        netdev_features_t gso_partial_features;
        int ifindex;
        int group;
        struct net_device_stats stats;
        atomic_long_t rx_dropped;
        atomic_long_t tx_dropped;
        atomic_long_t rx_nohandler;
    #ifdef CONFIG_WIRELESS_EXT
        const struct iw_handler_def *wireless_handlers;
        struct iw_public_data *wireless_data;
    #endif
        const struct net_device_ops *netdev_ops;
        const struct ethtool_ops *ethtool_ops;
    #ifdef CONFIG_NET_SWITCHDEV
        const struct switchdev_ops *switchdev_ops;
    #endif
    #ifdef CONFIG_NET_L3_MASTER_DEV
        const struct l3mdev_ops *l3mdev_ops;
    #endif
    #if IS_ENABLED(CONFIG_IPV6)
        const struct ndisc_ops *ndisc_ops;
    #endif
    #ifdef CONFIG_XFRM
        const struct xfrmdev_ops *xfrmdev_ops;
    #endif
        const struct header_ops *header_ops;
        unsigned int flags;
        unsigned int priv_flags;
        unsigned short gflags;
        unsigned short padded;
        unsigned char operstate;
        unsigned char link_mode;
        unsigned char if_port;
        unsigned char dma;
        unsigned int mtu;
        unsigned int min_mtu;
        unsigned int max_mtu;
        unsigned short type;
        unsigned short hard_header_len;
        unsigned char min_header_len;
        unsigned short needed_headroom;
        unsigned short needed_tailroom;
        unsigned char perm_addr[MAX_ADDR_LEN];
        unsigned char addr_assign_type;
        unsigned char addr_len;
        unsigned short neigh_priv_len;
        unsigned short dev_id;
        unsigned short dev_port;
        spinlock_t addr_list_lock;
        unsigned char name_assign_type;
        bool uc_promisc;
        struct netdev_hw_addr_list uc;
        struct netdev_hw_addr_list mc;
        struct netdev_hw_addr_list dev_addrs;
    #ifdef CONFIG_SYSFS
        struct kset *queues_kset;
    #endif
        unsigned int promiscuity;
        unsigned int allmulti;
    #if IS_ENABLED(CONFIG_VLAN_8021Q)
        struct vlan_info __rcu *vlan_info;
    #endif
    #if IS_ENABLED(CONFIG_NET_DSA)
        struct dsa_port *dsa_ptr;
    #endif
    #if IS_ENABLED(CONFIG_TIPC)
        struct tipc_bearer __rcu *tipc_ptr;
    #endif
        void *atalk_ptr;
        struct in_device __rcu *ip_ptr;
        struct dn_dev __rcu *dn_ptr;
        struct inet6_dev __rcu *ip6_ptr;
        void *ax25_ptr;
        struct wireless_dev *ieee80211_ptr;
        struct wpan_dev *ieee802154_ptr;
    #if IS_ENABLED(CONFIG_MPLS_ROUTING)
        struct mpls_dev __rcu *mpls_ptr;
    #endif
        unsigned char *dev_addr;
    #ifdef CONFIG_SYSFS
        struct netdev_rx_queue *_rx;
        unsigned int num_rx_queues;
        unsigned int real_num_rx_queues;
    #endif
        struct bpf_prog __rcu *xdp_prog;
        unsigned long gro_flush_timeout;
        rx_handler_func_t __rcu *rx_handler;
        void __rcu *rx_handler_data;
    #ifdef CONFIG_NET_CLS_ACT
        struct mini_Qdisc __rcu *miniq_ingress;
    #endif
        struct netdev_queue __rcu *ingress_queue;
    #ifdef CONFIG_NETFILTER_INGRESS
        struct nf_hook_entries __rcu *nf_hooks_ingress;
    #endif
        unsigned char broadcast[MAX_ADDR_LEN];
    #ifdef CONFIG_RFS_ACCEL
        struct cpu_rmap *rx_cpu_rmap;
    #endif
        struct hlist_node index_hlist;
        struct netdev_queue *_tx ____cacheline_aligned_in_smp;
        unsigned int num_tx_queues;
        unsigned int real_num_tx_queues;
        struct Qdisc *qdisc;
    #ifdef CONFIG_NET_SCHED
        DECLARE_HASHTABLE (qdisc_hash, 4);
    #endif
        unsigned int tx_queue_len;
        spinlock_t tx_global_lock;
        int watchdog_timeo;
    #ifdef CONFIG_XPS
        struct xps_dev_maps __rcu *xps_maps;
    #endif
    #ifdef CONFIG_NET_CLS_ACT
        struct mini_Qdisc __rcu *miniq_egress;
    #endif
        struct timer_list watchdog_timer;
        int __percpu *pcpu_refcnt;
        struct list_head todo_list;
        struct list_head link_watch_list;
        enum {
            NETREG_UNINITIALIZED=0,
            NETREG_REGISTERED,
            NETREG_UNREGISTERING,
            NETREG_UNREGISTERED,
            NETREG_RELEASED,
            NETREG_DUMMY,
        } reg_state:8;
        bool dismantle;,
        enum {,
            RTNL_LINK_INITIALIZED,
            RTNL_LINK_INITIALIZING,
        } rtnl_link_state:16;
        bool needs_free_netdev;,
        void (*priv_destructor)(struct net_device *dev);,
    #ifdef CONFIG_NETPOLL
        struct netpoll_info __rcu *npinfo;,
    #endif
        possible_net_t nd_net;,
        union {,
            void *ml_priv;
            struct pcpu_lstats __percpu *lstats;
            struct pcpu_sw_netstats __percpu *tstats;
            struct pcpu_dstats __percpu *dstats;
            struct pcpu_vstats __percpu *vstats;
        } ;
    #if IS_ENABLED(CONFIG_GARP)
        struct garp_port __rcu *garp_port;
    #endif
    #if IS_ENABLED(CONFIG_MRP)
        struct mrp_port __rcu *mrp_port;
    #endif
        struct device dev;
        const struct attribute_group *sysfs_groups[4];
        const struct attribute_group *sysfs_rx_queue_group;
        const struct rtnl_link_ops *rtnl_link_ops;
    #define GSO_MAX_SIZE 65536
        unsigned int gso_max_size;
    #define GSO_MAX_SEGS 65535
        u16 gso_max_segs;
    #ifdef CONFIG_DCB
        const struct dcbnl_rtnl_ops *dcbnl_ops;
    #endif
        u8 num_tc;
        struct netdev_tc_txq tc_to_txq[TC_MAX_QUEUE];
        u8 prio_tc_map[TC_BITMASK + 1];
    #if IS_ENABLED(CONFIG_FCOE)
        unsigned int fcoe_ddp_xid;
    #endif
    #if IS_ENABLED(CONFIG_CGROUP_NET_PRIO)
        struct netprio_map __rcu *priomap;
    #endif
        struct phy_device *phydev;
        struct lock_class_key *qdisc_tx_busylock;
        struct lock_class_key *qdisc_running_key;
        bool proto_down;
    }

.. _`net_device.members`:

Members
-------

name
    This is the first field of the "visible" part of this structure
    (i.e. as seen by users in the "Space.c" file).  It is the name
    of the interface.

name_hlist
    Device name hash chain, please keep it close to name[]

ifalias
    SNMP alias

mem_end
    Shared memory end

mem_start
    Shared memory start

base_addr
    Device I/O address

irq
    Device IRQ number

carrier_changes
    Stats to monitor carrier on<->off transitions

state
    Generic network queuing layer state, see netdev_state_t

dev_list
    The global list of network devices

napi_list
    List entry used for polling NAPI devices

unreg_list
    List entry  when we are unregistering the
    device; see the function unregister_netdev

close_list
    List entry used when we are closing the device

ptype_all
    Device-specific packet handlers for all protocols

ptype_specific
    Device-specific, protocol-specific packet handlers

adj_list
    Directly linked devices, like slaves for bonding

features
    Currently active device features

hw_features
    User-changeable features

wanted_features
    User-requested features

vlan_features
    Mask of features inheritable by VLAN devices

hw_enc_features
    Mask of features inherited by encapsulating devices
    This field indicates what encapsulation
    offloads the hardware is capable of doing,
    and drivers will need to set them appropriately.

mpls_features
    Mask of features inheritable by MPLS

gso_partial_features
    *undescribed*

ifindex
    interface index

group
    The group the device belongs to

stats
    Statistics struct, which was left as a legacy, use
    rtnl_link_stats64 instead

rx_dropped
    Dropped packets by core network,
    do not use this in drivers

tx_dropped
    Dropped packets by core network,
    do not use this in drivers

rx_nohandler
    nohandler dropped packets by core network on
    inactive devices, do not use this in drivers

wireless_handlers
    List of functions to handle Wireless Extensions,
    instead of ioctl,
    see <net/iw_handler.h> for details.

wireless_data
    Instance data managed by the core of wireless extensions

netdev_ops
    Includes several pointers to callbacks,
    if one wants to override the ndo_*() functions

ethtool_ops
    Management operations

switchdev_ops
    *undescribed*

l3mdev_ops
    *undescribed*

ndisc_ops
    Includes callbacks for different IPv6 neighbour
    discovery handling. Necessary for e.g. 6LoWPAN.

xfrmdev_ops
    *undescribed*

header_ops
    Includes callbacks for creating,parsing,caching,etc
    of Layer 2 headers.

flags
    Interface flags (a la BSD)

priv_flags
    Like 'flags' but invisible to userspace,
    see if.h for the definitions

gflags
    Global flags ( kept as legacy )

padded
    How much padding added by \ :c:func:`alloc_netdev`\ 

operstate
    RFC2863 operstate

link_mode
    Mapping policy to operstate

if_port
    Selectable AUI, TP, ...

dma
    DMA channel

mtu
    Interface MTU value

min_mtu
    Interface Minimum MTU value

max_mtu
    Interface Maximum MTU value

type
    Interface hardware type

hard_header_len
    Maximum hardware header length.

min_header_len
    Minimum hardware header length

needed_headroom
    Extra headroom the hardware may need, but not in all
    cases can this be guaranteed

needed_tailroom
    Extra tailroom the hardware may need, but not in all
    cases can this be guaranteed. Some cases also use
    LL_MAX_HEADER instead to allocate the skb

perm_addr
    Permanent hw address

addr_assign_type
    Hw address assignment type

addr_len
    Hardware address length

neigh_priv_len
    Used in \ :c:func:`neigh_alloc`\ 

dev_id
    Used to differentiate devices that share
    the same link layer address

dev_port
    Used to differentiate devices that share
    the same function

addr_list_lock
    XXX: need comments on this one

name_assign_type
    *undescribed*

uc_promisc
    Counter that indicates promiscuous mode
    has been enabled due to the need to listen to
    additional unicast addresses in a device that
    does not implement \ :c:func:`ndo_set_rx_mode`\ 

uc
    unicast mac addresses

mc
    multicast mac addresses

dev_addrs
    list of device hw addresses

queues_kset
    Group of all Kobjects in the Tx and RX queues

promiscuity
    Number of times the NIC is told to work in
    promiscuous mode; if it becomes 0 the NIC will
    exit promiscuous mode

allmulti
    Counter, enables or disables allmulticast mode

vlan_info
    VLAN info

dsa_ptr
    dsa specific data

tipc_ptr
    TIPC specific data

atalk_ptr
    AppleTalk link

ip_ptr
    IPv4 specific data

dn_ptr
    DECnet specific data

ip6_ptr
    IPv6 specific data

ax25_ptr
    AX.25 specific data

ieee80211_ptr
    IEEE 802.11 specific data, assign before registering

ieee802154_ptr
    *undescribed*

mpls_ptr
    *undescribed*

dev_addr
    Hw address (before bcast,
    because most packets are unicast)

_rx
    Array of RX queues

num_rx_queues
    Number of RX queues
    allocated at \ :c:func:`register_netdev`\  time

real_num_rx_queues
    Number of RX queues currently active in device

xdp_prog
    *undescribed*

gro_flush_timeout
    *undescribed*

rx_handler
    handler for received packets

rx_handler_data
    XXX: need comments on this one

miniq_ingress
    ingress/clsact qdisc specific data for
    ingress processing

ingress_queue
    XXX: need comments on this one

nf_hooks_ingress
    *undescribed*

broadcast
    hw bcast address

rx_cpu_rmap
    CPU reverse-mapping for RX completion interrupts,
    indexed by RX queue number. Assigned by driver.
    This must only be set if the ndo_rx_flow_steer
    operation is defined

index_hlist
    Device index hash chain

____cacheline_aligned_in_smp
    *undescribed*

num_tx_queues
    Number of TX queues allocated at \ :c:func:`alloc_netdev_mq`\  time

real_num_tx_queues
    Number of TX queues currently active in device

qdisc
    Root qdisc from userspace point of view

qdisc_hash
    *undescribed*

tx_queue_len
    Max frames per queue allowed

tx_global_lock
    XXX: need comments on this one

watchdog_timeo
    Represents the timeout that is used by
    the watchdog (see \ :c:func:`dev_watchdog`\ )

xps_maps
    XXX: need comments on this one

miniq_egress
    clsact qdisc specific data for
    egress processing

watchdog_timer
    List of timers

pcpu_refcnt
    Number of references to this device

todo_list
    Delayed register/unregister

link_watch_list
    XXX: need comments on this one

reg_state
    Register/unregister state machine

dismantle
    Device is going to be freed

rtnl_link_state
    This enum represents the phases of creating
    a new link

needs_free_netdev
    Should unregister perform free_netdev?

priv_destructor
    Called from unregister

npinfo
    XXX: need comments on this one

nd_net
    Network namespace this network device is inside

{unnamed_union}
    anonymous

ml_priv
    Mid-layer private

lstats
    Loopback statistics

tstats
    Tunnel statistics

dstats
    Dummy statistics

vstats
    Virtual ethernet statistics

garp_port
    GARP

mrp_port
    MRP

dev
    Class/net/name entry

sysfs_groups
    Space for optional device, statistics and wireless
    sysfs groups

sysfs_rx_queue_group
    Space for optional per-rx queue attributes

rtnl_link_ops
    Rtnl_link_ops

gso_max_size
    Maximum size of generic segmentation offload

gso_max_segs
    Maximum number of segments that can be passed to the
    NIC for GSO

dcbnl_ops
    Data Center Bridging netlink ops

num_tc
    Number of traffic classes in the net device

tc_to_txq
    XXX: need comments on this one

prio_tc_map
    XXX: need comments on this one

fcoe_ddp_xid
    Max exchange id for FCoE LRO by ddp

priomap
    XXX: need comments on this one

phydev
    Physical device may attach itself
    for hardware timestamping

qdisc_tx_busylock
    lockdep class annotating Qdisc->busylock spinlock

qdisc_running_key
    lockdep class annotating Qdisc->running seqcount

proto_down
    protocol port state information can be sent to the
    switch driver and used to set the phys state of the
    switch port.

.. _`net_device.description`:

Description
-----------

     Actually, this whole structure is a big mistake.  It mixes I/O
     data with strictly "high-level" data, and it has to know about
     almost every data structure used in the INET module.

     FIXME: cleanup struct net_device such that network protocol info
     moves out.

.. _`netdev_priv`:

netdev_priv
===========

.. c:function:: void *netdev_priv(const struct net_device *dev)

    access network device private data

    :param const struct net_device \*dev:
        network device

.. _`netdev_priv.description`:

Description
-----------

Get network device private data

.. _`netif_napi_add`:

netif_napi_add
==============

.. c:function:: void netif_napi_add(struct net_device *dev, struct napi_struct *napi, int (*poll)(struct napi_struct *, int), int weight)

    initialize a NAPI context

    :param struct net_device \*dev:
        network device

    :param struct napi_struct \*napi:
        NAPI context

    :param int (\*poll)(struct napi_struct \*, int):
        polling function

    :param int weight:
        default weight

.. _`netif_napi_add.description`:

Description
-----------

netif_napi_add() must be used to initialize a NAPI context prior to calling
*any* of the other NAPI-related functions.

.. _`netif_tx_napi_add`:

netif_tx_napi_add
=================

.. c:function:: void netif_tx_napi_add(struct net_device *dev, struct napi_struct *napi, int (*poll)(struct napi_struct *, int), int weight)

    initialize a NAPI context

    :param struct net_device \*dev:
        network device

    :param struct napi_struct \*napi:
        NAPI context

    :param int (\*poll)(struct napi_struct \*, int):
        polling function

    :param int weight:
        default weight

.. _`netif_tx_napi_add.description`:

Description
-----------

This variant of \ :c:func:`netif_napi_add`\  should be used from drivers using NAPI
to exclusively poll a TX queue.
This will avoid we add it into napi_hash[], thus polluting this hash table.

.. _`netif_napi_del`:

netif_napi_del
==============

.. c:function:: void netif_napi_del(struct napi_struct *napi)

    remove a NAPI context

    :param struct napi_struct \*napi:
        NAPI context

.. _`netif_napi_del.description`:

Description
-----------

 \ :c:func:`netif_napi_del`\  removes a NAPI context from the network device NAPI list

.. _`netif_start_queue`:

netif_start_queue
=================

.. c:function:: void netif_start_queue(struct net_device *dev)

    allow transmit

    :param struct net_device \*dev:
        network device

.. _`netif_start_queue.description`:

Description
-----------

     Allow upper layers to call the device hard_start_xmit routine.

.. _`netif_wake_queue`:

netif_wake_queue
================

.. c:function:: void netif_wake_queue(struct net_device *dev)

    restart transmit

    :param struct net_device \*dev:
        network device

.. _`netif_wake_queue.description`:

Description
-----------

     Allow upper layers to call the device hard_start_xmit routine.
     Used for flow control when transmit resources are available.

.. _`netif_stop_queue`:

netif_stop_queue
================

.. c:function:: void netif_stop_queue(struct net_device *dev)

    stop transmitted packets

    :param struct net_device \*dev:
        network device

.. _`netif_stop_queue.description`:

Description
-----------

     Stop upper layers calling the device hard_start_xmit routine.
     Used for flow control when transmit resources are unavailable.

.. _`netif_queue_stopped`:

netif_queue_stopped
===================

.. c:function:: bool netif_queue_stopped(const struct net_device *dev)

    test if transmit queue is flowblocked

    :param const struct net_device \*dev:
        network device

.. _`netif_queue_stopped.description`:

Description
-----------

     Test if transmit queue on device is currently unable to send.

.. _`netdev_txq_bql_enqueue_prefetchw`:

netdev_txq_bql_enqueue_prefetchw
================================

.. c:function:: void netdev_txq_bql_enqueue_prefetchw(struct netdev_queue *dev_queue)

    prefetch bql data for write

    :param struct netdev_queue \*dev_queue:
        pointer to transmit queue

.. _`netdev_txq_bql_enqueue_prefetchw.description`:

Description
-----------

BQL enabled drivers might use this helper in their \ :c:func:`ndo_start_xmit`\ ,
to give appropriate hint to the CPU.

.. _`netdev_txq_bql_complete_prefetchw`:

netdev_txq_bql_complete_prefetchw
=================================

.. c:function:: void netdev_txq_bql_complete_prefetchw(struct netdev_queue *dev_queue)

    prefetch bql data for write

    :param struct netdev_queue \*dev_queue:
        pointer to transmit queue

.. _`netdev_txq_bql_complete_prefetchw.description`:

Description
-----------

BQL enabled drivers might use this helper in their TX completion path,
to give appropriate hint to the CPU.

.. _`netdev_sent_queue`:

netdev_sent_queue
=================

.. c:function:: void netdev_sent_queue(struct net_device *dev, unsigned int bytes)

    report the number of bytes queued to hardware

    :param struct net_device \*dev:
        network device

    :param unsigned int bytes:
        number of bytes queued to the hardware device queue

.. _`netdev_sent_queue.description`:

Description
-----------

     Report the number of bytes queued for sending/completion to the network
     device hardware queue. \ ``bytes``\  should be a good approximation and should
     exactly match \ :c:func:`netdev_completed_queue`\  \ ``bytes``\ 

.. _`netdev_completed_queue`:

netdev_completed_queue
======================

.. c:function:: void netdev_completed_queue(struct net_device *dev, unsigned int pkts, unsigned int bytes)

    report bytes and packets completed by device

    :param struct net_device \*dev:
        network device

    :param unsigned int pkts:
        actual number of packets sent over the medium

    :param unsigned int bytes:
        actual number of bytes sent over the medium

.. _`netdev_completed_queue.description`:

Description
-----------

     Report the number of bytes and packets transmitted by the network device
     hardware queue over the physical medium, \ ``bytes``\  must exactly match the
     \ ``bytes``\  amount passed to \ :c:func:`netdev_sent_queue`\ 

.. _`netdev_reset_queue`:

netdev_reset_queue
==================

.. c:function:: void netdev_reset_queue(struct net_device *dev_queue)

    reset the packets and bytes count of a network device

    :param struct net_device \*dev_queue:
        network device

.. _`netdev_reset_queue.description`:

Description
-----------

     Reset the bytes and packet count of a network device and clear the
     software flow control OFF bit for this network device

.. _`netdev_cap_txqueue`:

netdev_cap_txqueue
==================

.. c:function:: u16 netdev_cap_txqueue(struct net_device *dev, u16 queue_index)

    check if selected tx queue exceeds device queues

    :param struct net_device \*dev:
        network device

    :param u16 queue_index:
        given tx queue index

.. _`netdev_cap_txqueue.description`:

Description
-----------

     Returns 0 if given tx queue index >= number of device tx queues,
     otherwise returns the originally passed tx queue index.

.. _`netif_running`:

netif_running
=============

.. c:function:: bool netif_running(const struct net_device *dev)

    test if up

    :param const struct net_device \*dev:
        network device

.. _`netif_running.description`:

Description
-----------

     Test if the device has been brought up.

.. _`netif_start_subqueue`:

netif_start_subqueue
====================

.. c:function:: void netif_start_subqueue(struct net_device *dev, u16 queue_index)

    allow sending packets on subqueue

    :param struct net_device \*dev:
        network device

    :param u16 queue_index:
        sub queue index

.. _`netif_start_subqueue.description`:

Description
-----------

Start individual transmit queue of a device with multiple transmit queues.

.. _`netif_stop_subqueue`:

netif_stop_subqueue
===================

.. c:function:: void netif_stop_subqueue(struct net_device *dev, u16 queue_index)

    stop sending packets on subqueue

    :param struct net_device \*dev:
        network device

    :param u16 queue_index:
        sub queue index

.. _`netif_stop_subqueue.description`:

Description
-----------

Stop individual transmit queue of a device with multiple transmit queues.

.. _`__netif_subqueue_stopped`:

__netif_subqueue_stopped
========================

.. c:function:: bool __netif_subqueue_stopped(const struct net_device *dev, u16 queue_index)

    test status of subqueue

    :param const struct net_device \*dev:
        network device

    :param u16 queue_index:
        sub queue index

.. _`__netif_subqueue_stopped.description`:

Description
-----------

Check individual transmit queue of a device with multiple transmit queues.

.. _`netif_wake_subqueue`:

netif_wake_subqueue
===================

.. c:function:: void netif_wake_subqueue(struct net_device *dev, u16 queue_index)

    allow sending packets on subqueue

    :param struct net_device \*dev:
        network device

    :param u16 queue_index:
        sub queue index

.. _`netif_wake_subqueue.description`:

Description
-----------

Resume individual transmit queue of a device with multiple transmit queues.

.. _`netif_is_multiqueue`:

netif_is_multiqueue
===================

.. c:function:: bool netif_is_multiqueue(const struct net_device *dev)

    test if device has multiple transmit queues

    :param const struct net_device \*dev:
        network device

.. _`netif_is_multiqueue.description`:

Description
-----------

Check if device has multiple transmit queues

.. _`dev_put`:

dev_put
=======

.. c:function:: void dev_put(struct net_device *dev)

    release reference to device

    :param struct net_device \*dev:
        network device

.. _`dev_put.description`:

Description
-----------

Release reference to device to allow it to be freed.

.. _`dev_hold`:

dev_hold
========

.. c:function:: void dev_hold(struct net_device *dev)

    get reference to device

    :param struct net_device \*dev:
        network device

.. _`dev_hold.description`:

Description
-----------

Hold reference to device to keep it from being freed.

.. _`netif_carrier_ok`:

netif_carrier_ok
================

.. c:function:: bool netif_carrier_ok(const struct net_device *dev)

    test if carrier present

    :param const struct net_device \*dev:
        network device

.. _`netif_carrier_ok.description`:

Description
-----------

Check if carrier is present on device

.. _`netif_dormant_on`:

netif_dormant_on
================

.. c:function:: void netif_dormant_on(struct net_device *dev)

    mark device as dormant.

    :param struct net_device \*dev:
        network device

.. _`netif_dormant_on.description`:

Description
-----------

Mark device as dormant (as per RFC2863).

The dormant state indicates that the relevant interface is not
actually in a condition to pass packets (i.e., it is not 'up') but is
in a "pending" state, waiting for some external event.  For "on-
demand" interfaces, this new state identifies the situation where the
interface is waiting for events to place it in the up state.

.. _`netif_dormant_off`:

netif_dormant_off
=================

.. c:function:: void netif_dormant_off(struct net_device *dev)

    set device as not dormant.

    :param struct net_device \*dev:
        network device

.. _`netif_dormant_off.description`:

Description
-----------

Device is not in dormant state.

.. _`netif_dormant`:

netif_dormant
=============

.. c:function:: bool netif_dormant(const struct net_device *dev)

    test if device is dormant

    :param const struct net_device \*dev:
        network device

.. _`netif_dormant.description`:

Description
-----------

Check if device is dormant.

.. _`netif_oper_up`:

netif_oper_up
=============

.. c:function:: bool netif_oper_up(const struct net_device *dev)

    test if device is operational

    :param const struct net_device \*dev:
        network device

.. _`netif_oper_up.description`:

Description
-----------

Check if carrier is operational

.. _`netif_device_present`:

netif_device_present
====================

.. c:function:: bool netif_device_present(struct net_device *dev)

    is device available or removed

    :param struct net_device \*dev:
        network device

.. _`netif_device_present.description`:

Description
-----------

Check if device has not been removed from system.

.. _`netif_tx_lock`:

netif_tx_lock
=============

.. c:function:: void netif_tx_lock(struct net_device *dev)

    grab network device transmit lock

    :param struct net_device \*dev:
        network device

.. _`netif_tx_lock.description`:

Description
-----------

Get network device transmit lock

.. _`__dev_uc_sync`:

__dev_uc_sync
=============

.. c:function:: int __dev_uc_sync(struct net_device *dev, int (*sync)(struct net_device *, const unsigned char *), int (*unsync)(struct net_device *, const unsigned char *))

    Synchonize device's unicast list

    :param struct net_device \*dev:
        device to sync

    :param int (\*sync)(struct net_device \*, const unsigned char \*):
        function to call if address should be added

    :param int (\*unsync)(struct net_device \*, const unsigned char \*):
        function to call if address should be removed

.. _`__dev_uc_sync.description`:

Description
-----------

 Add newly added addresses to the interface, and release
 addresses that have been deleted.

.. _`__dev_uc_unsync`:

__dev_uc_unsync
===============

.. c:function:: void __dev_uc_unsync(struct net_device *dev, int (*unsync)(struct net_device *, const unsigned char *))

    Remove synchronized addresses from device

    :param struct net_device \*dev:
        device to sync

    :param int (\*unsync)(struct net_device \*, const unsigned char \*):
        function to call if address should be removed

.. _`__dev_uc_unsync.description`:

Description
-----------

 Remove all addresses that were added to the device by \ :c:func:`dev_uc_sync`\ .

.. _`__dev_mc_sync`:

__dev_mc_sync
=============

.. c:function:: int __dev_mc_sync(struct net_device *dev, int (*sync)(struct net_device *, const unsigned char *), int (*unsync)(struct net_device *, const unsigned char *))

    Synchonize device's multicast list

    :param struct net_device \*dev:
        device to sync

    :param int (\*sync)(struct net_device \*, const unsigned char \*):
        function to call if address should be added

    :param int (\*unsync)(struct net_device \*, const unsigned char \*):
        function to call if address should be removed

.. _`__dev_mc_sync.description`:

Description
-----------

 Add newly added addresses to the interface, and release
 addresses that have been deleted.

.. _`__dev_mc_unsync`:

__dev_mc_unsync
===============

.. c:function:: void __dev_mc_unsync(struct net_device *dev, int (*unsync)(struct net_device *, const unsigned char *))

    Remove synchronized addresses from device

    :param struct net_device \*dev:
        device to sync

    :param int (\*unsync)(struct net_device \*, const unsigned char \*):
        function to call if address should be removed

.. _`__dev_mc_unsync.description`:

Description
-----------

 Remove all addresses that were added to the device by \ :c:func:`dev_mc_sync`\ .

.. This file was automatic generated / don't edit.


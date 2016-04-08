
.. _API-struct-net-device:

=================
struct net_device
=================

*man struct net_device(9)*

*4.6.0-rc1*

The DEVICE structure. Actually, this whole structure is a big mistake. It mixes I/O data with strictly “high-level” data, and it has to know about almost every data structure used
in the INET module.


Synopsis
========

.. code-block:: c

    struct net_device {
      char name[IFNAMSIZ];
      struct hlist_node name_hlist;
      char * ifalias;
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
      struct {unnamed_struct};
      struct garp_port __rcu * garp_port;
      struct mrp_port __rcu * mrp_port;
      struct device dev;
      const struct attribute_group * sysfs_groups[4];
      const struct attribute_group * sysfs_rx_queue_group;
      const struct rtnl_link_ops * rtnl_link_ops;
    #define GSO_MAX_SIZE        65536
      unsigned int gso_max_size;
    #define GSO_MAX_SEGS        65535
      u16 gso_max_segs;
      u16 gso_min_segs;
    #ifdef CONFIG_DCB
      const struct dcbnl_rtnl_ops * dcbnl_ops;
    #endif
      u8 num_tc;
      struct netdev_tc_txq tc_to_txq[TC_MAX_QUEUE];
      u8 prio_tc_map[TC_BITMASK + 1];
    #if IS_ENABLED(CONFIG_FCOE)
      unsigned int fcoe_ddp_xid;
    #endif
    #if IS_ENABLED(CONFIG_CGROUP_NET_PRIO)
      struct netprio_map __rcu * priomap;
    #endif
      struct phy_device * phydev;
      struct lock_class_key * qdisc_tx_busylock;
      bool proto_down;
    };


Members
=======

name[IFNAMSIZ]
    This is the first field of the “visible” part of this structure (i.e. as seen by users in the “Space.c” file). It is the name of the interface.

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
    List entry when we are unregistering the device; see the function unregister_netdev

close_list
    List entry used when we are closing the device

ptype_all
    Device-specific packet handlers for all protocols

ptype_specific
    Device-specific, protocol-specific packet handlers

{unnamed_struct}
    anonymous

garp_port
    GARP

mrp_port
    MRP

dev
    Class/net/name entry

sysfs_groups[4]
    Space for optional device, statistics and wireless sysfs groups

sysfs_rx_queue_group
    Space for optional per-rx queue attributes

rtnl_link_ops
    Rtnl_link_ops

gso_max_size
    Maximum size of generic segmentation offload

gso_max_segs
    Maximum number of segments that can be passed to the NIC for GSO

gso_min_segs
    Minimum number of segments that can be passed to the NIC for GSO

dcbnl_ops
    Data Center Bridging netlink ops

num_tc
    Number of traffic classes in the net device

tc_to_txq[TC_MAX_QUEUE]
    XXX: need comments on this one

prio_tc_map[TC_BITMASK + 1]
    need comments on this one

fcoe_ddp_xid
    Max exchange id for FCoE LRO by ddp

priomap
    XXX: need comments on this one

phydev
    Physical device may attach itself for hardware timestamping

qdisc_tx_busylock
    XXX: need comments on this one

proto_down
    protocol port state information can be sent to the switch driver and used to set the phys state of the switch port.


FIXME
=====

cleanup struct net_device such that network protocol info moves out.

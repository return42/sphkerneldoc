.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/ulp/opa_vnic/opa_vnic_internal.h

.. _`__opa_vesw_info`:

struct \__opa_vesw_info
=======================

.. c:type:: struct __opa_vesw_info

    OPA vnic virtual switch info

.. _`__opa_vesw_info.definition`:

Definition
----------

.. code-block:: c

    struct __opa_vesw_info {
        u16 fabric_id;
        u16 vesw_id;
        u8 rsvd0[6];
        u16 def_port_mask;
        u8 rsvd1[2];
        u16 pkey;
        u8 rsvd2[4];
        u32 u_mcast_dlid;
        u32 u_ucast_dlid[OPA_VESW_MAX_NUM_DEF_PORT];
        u32 rc;
        u8 rsvd3[56];
        u16 eth_mtu;
        u8 rsvd4[2];
    }

.. _`__opa_vesw_info.members`:

Members
-------

fabric_id
    *undescribed*

vesw_id
    *undescribed*

rsvd0
    *undescribed*

def_port_mask
    *undescribed*

rsvd1
    *undescribed*

pkey
    *undescribed*

rsvd2
    *undescribed*

u_mcast_dlid
    *undescribed*

u_ucast_dlid
    *undescribed*

rc
    *undescribed*

rsvd3
    *undescribed*

eth_mtu
    *undescribed*

rsvd4
    *undescribed*

.. _`__opa_vesw_info.description`:

Description
-----------

Same as opa_vesw_info without bitwise attribute.

.. _`__opa_per_veswport_info`:

struct \__opa_per_veswport_info
===============================

.. c:type:: struct __opa_per_veswport_info

    OPA vnic per port info

.. _`__opa_per_veswport_info.definition`:

Definition
----------

.. code-block:: c

    struct __opa_per_veswport_info {
        u32 port_num;
        u8 eth_link_status;
        u8 rsvd0[3];
        u8 base_mac_addr[ETH_ALEN];
        u8 config_state;
        u8 oper_state;
        u16 max_mac_tbl_ent;
        u16 max_smac_ent;
        u32 mac_tbl_digest;
        u8 rsvd1[4];
        u32 encap_slid;
        u8 pcp_to_sc_uc[OPA_VNIC_MAX_NUM_PCP];
        u8 pcp_to_vl_uc[OPA_VNIC_MAX_NUM_PCP];
        u8 pcp_to_sc_mc[OPA_VNIC_MAX_NUM_PCP];
        u8 pcp_to_vl_mc[OPA_VNIC_MAX_NUM_PCP];
        u8 non_vlan_sc_uc;
        u8 non_vlan_vl_uc;
        u8 non_vlan_sc_mc;
        u8 non_vlan_vl_mc;
        u8 rsvd2[48];
        u16 uc_macs_gen_count;
        u16 mc_macs_gen_count;
        u8 rsvd3[8];
    }

.. _`__opa_per_veswport_info.members`:

Members
-------

port_num
    *undescribed*

eth_link_status
    *undescribed*

rsvd0
    *undescribed*

base_mac_addr
    *undescribed*

config_state
    *undescribed*

oper_state
    *undescribed*

max_mac_tbl_ent
    *undescribed*

max_smac_ent
    *undescribed*

mac_tbl_digest
    *undescribed*

rsvd1
    *undescribed*

encap_slid
    *undescribed*

pcp_to_sc_uc
    *undescribed*

pcp_to_vl_uc
    *undescribed*

pcp_to_sc_mc
    *undescribed*

pcp_to_vl_mc
    *undescribed*

non_vlan_sc_uc
    *undescribed*

non_vlan_vl_uc
    *undescribed*

non_vlan_sc_mc
    *undescribed*

non_vlan_vl_mc
    *undescribed*

rsvd2
    *undescribed*

uc_macs_gen_count
    *undescribed*

mc_macs_gen_count
    *undescribed*

rsvd3
    *undescribed*

.. _`__opa_per_veswport_info.description`:

Description
-----------

Same as opa_per_veswport_info without bitwise attribute.

.. _`__opa_veswport_info`:

struct \__opa_veswport_info
===========================

.. c:type:: struct __opa_veswport_info

    OPA vnic port info

.. _`__opa_veswport_info.definition`:

Definition
----------

.. code-block:: c

    struct __opa_veswport_info {
        struct __opa_vesw_info vesw;
        struct __opa_per_veswport_info vport;
    }

.. _`__opa_veswport_info.members`:

Members
-------

vesw
    *undescribed*

vport
    *undescribed*

.. _`__opa_veswport_info.description`:

Description
-----------

Same as opa_veswport_info without bitwise attribute.

.. _`__opa_veswport_trap`:

struct \__opa_veswport_trap
===========================

.. c:type:: struct __opa_veswport_trap

    OPA vnic trap info

.. _`__opa_veswport_trap.definition`:

Definition
----------

.. code-block:: c

    struct __opa_veswport_trap {
        u16 fabric_id;
        u16 veswid;
        u32 veswportnum;
        u16 opaportnum;
        u8 veswportindex;
        u8 opcode;
        u32 reserved;
    }

.. _`__opa_veswport_trap.members`:

Members
-------

fabric_id
    *undescribed*

veswid
    *undescribed*

veswportnum
    *undescribed*

opaportnum
    *undescribed*

veswportindex
    *undescribed*

opcode
    *undescribed*

reserved
    *undescribed*

.. _`__opa_veswport_trap.description`:

Description
-----------

Same as opa_veswport_trap without bitwise attribute.

.. _`opa_vnic_ctrl_port`:

struct opa_vnic_ctrl_port
=========================

.. c:type:: struct opa_vnic_ctrl_port

    OPA virtual NIC control port

.. _`opa_vnic_ctrl_port.definition`:

Definition
----------

.. code-block:: c

    struct opa_vnic_ctrl_port {
        struct ib_device *ibdev;
        struct opa_vnic_ctrl_ops *ops;
        u8 num_ports;
    }

.. _`opa_vnic_ctrl_port.members`:

Members
-------

ibdev
    pointer to ib device

ops
    opa vnic control operations

num_ports
    number of opa ports

.. _`opa_vnic_adapter`:

struct opa_vnic_adapter
=======================

.. c:type:: struct opa_vnic_adapter

    OPA VNIC netdev private data structure

.. _`opa_vnic_adapter.definition`:

Definition
----------

.. code-block:: c

    struct opa_vnic_adapter {
        struct net_device *netdev;
        struct ib_device *ibdev;
        struct opa_vnic_ctrl_port *cport;
        const struct net_device_ops *rn_ops;
        u8 port_num;
        u8 vport_num;
        struct mutex lock;
        struct __opa_veswport_info info;
        u8 vema_mac_addr[ETH_ALEN];
        u32 umac_hash;
        u32 mmac_hash;
        struct hlist_head __rcu *mactbl;
        struct mutex mactbl_lock;
        spinlock_t stats_lock;
        u8 flow_tbl[OPA_VNIC_FLOW_TBL_SIZE];
        unsigned long trap_timeout;
        u8 trap_count;
    }

.. _`opa_vnic_adapter.members`:

Members
-------

netdev
    pointer to associated netdev

ibdev
    ib device

cport
    pointer to opa vnic control port

rn_ops
    rdma netdev's net_device_ops

port_num
    OPA port number

vport_num
    vesw port number

lock
    adapter lock

info
    virtual ethernet switch port information

vema_mac_addr
    mac address configured by vema

umac_hash
    unicast maclist hash

mmac_hash
    multicast maclist hash

mactbl
    hash table of MAC entries

mactbl_lock
    mac table lock

stats_lock
    statistics lock

flow_tbl
    flow to default port redirection table

trap_timeout
    trap timeout

trap_count
    no. of traps allowed within timeout period

.. _`opa_vnic_mac_tbl_node`:

struct opa_vnic_mac_tbl_node
============================

.. c:type:: struct opa_vnic_mac_tbl_node

    OPA VNIC mac table node

.. _`opa_vnic_mac_tbl_node.definition`:

Definition
----------

.. code-block:: c

    struct opa_vnic_mac_tbl_node {
        struct hlist_node hlist;
        u16 index;
        struct __opa_vnic_mactable_entry entry;
    }

.. _`opa_vnic_mac_tbl_node.members`:

Members
-------

hlist
    hash list handle

index
    index of entry in the mac table

entry
    entry in the table

.. This file was automatic generated / don't edit.


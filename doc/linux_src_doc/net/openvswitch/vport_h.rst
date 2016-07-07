.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/openvswitch/vport.h

.. _`vport_portids`:

struct vport_portids
====================

.. c:type:: struct vport_portids

    array of netlink portids of a vport. must be protected by rcu.

.. _`vport_portids.definition`:

Definition
----------

.. code-block:: c

    struct vport_portids {
        struct reciprocal_value rn_ids;
        struct rcu_head rcu;
        u32 n_ids;
        u32 ids[];
    }

.. _`vport_portids.members`:

Members
-------

rn_ids
    The reciprocal value of \ ``n_ids``\ .

rcu
    RCU callback head for deferred destruction.

n_ids
    Size of \ ``ids``\  array.

ids
    Array storing the Netlink socket pids to be used for packets received
    on this port that miss the flow table.

.. _`vport`:

struct vport
============

.. c:type:: struct vport

    one port within a datapath

.. _`vport.definition`:

Definition
----------

.. code-block:: c

    struct vport {
        struct net_device *dev;
        struct datapath *dp;
        struct vport_portids __rcu *upcall_portids;
        u16 port_no;
        struct hlist_node hash_node;
        struct hlist_node dp_hash_node;
        const struct vport_ops *ops;
        struct list_head detach_list;
        struct rcu_head rcu;
    }

.. _`vport.members`:

Members
-------

dev
    Pointer to net_device.

dp
    Datapath to which this port belongs.

upcall_portids
    RCU protected 'struct vport_portids'.

port_no
    Index into \ ``dp``\ 's \ ``ports``\  array.

hash_node
    Element in \ ``dev_table``\  hash table in vport.c.

dp_hash_node
    Element in \ ``datapath``\ ->ports hash table in datapath.c.

ops
    Class structure.

detach_list
    list used for detaching vport in net-exit call.

rcu
    RCU callback head for deferred destruction.

.. _`vport_parms`:

struct vport_parms
==================

.. c:type:: struct vport_parms

    parameters for creating a new vport

.. _`vport_parms.definition`:

Definition
----------

.. code-block:: c

    struct vport_parms {
        const char *name;
        enum ovs_vport_type type;
        struct nlattr *options;
        struct datapath *dp;
        u16 port_no;
        struct nlattr *upcall_portids;
    }

.. _`vport_parms.members`:

Members
-------

name
    New vport's name.

type
    New vport's type.

options
    \ ``OVS_VPORT_ATTR_OPTIONS``\  attribute from Netlink message, \ ``NULL``\  if
    none was supplied.

dp
    New vport's datapath.

port_no
    New vport's port number.

upcall_portids
    *undescribed*

.. _`vport_ops`:

struct vport_ops
================

.. c:type:: struct vport_ops

    definition of a type of virtual port

.. _`vport_ops.definition`:

Definition
----------

.. code-block:: c

    struct vport_ops {
        enum ovs_vport_type type;
        struct vport *(* create) (const struct vport_parms *);
        void (* destroy) (struct vport *);
        int (* set_options) (struct vport *, struct nlattr *);
        int (* get_options) (const struct vport *, struct sk_buff *);
        netdev_tx_t (* send) (struct sk_buff *skb);
        struct module *owner;
        struct list_head list;
    }

.. _`vport_ops.members`:

Members
-------

type
    \ ``OVS_VPORT_TYPE``\ \_\* value for this type of virtual port.

create
    Create a new vport configured as specified.  On success returns
    a new vport allocated with \ :c:func:`ovs_vport_alloc`\ , otherwise an \ :c:func:`ERR_PTR`\  value.

destroy
    Destroys a vport.  Must call \ :c:func:`vport_free`\  on the vport but not
    before an RCU grace period has elapsed.

set_options
    Modify the configuration of an existing vport.  May be \ ``NULL``\ 
    if modification is not supported.

get_options
    Appends vport-specific attributes for the configuration of an
    existing vport to a \ :c:type:`struct sk_buff <sk_buff>`\ .  May be \ ``NULL``\  for a vport that does not
    have any configuration.

send
    Send a packet on the device.
    zero for dropped packets or negative for error.

owner
    *undescribed*

list
    *undescribed*

.. _`vport_priv`:

vport_priv
==========

.. c:function:: void *vport_priv(const struct vport *vport)

    access private data area of vport

    :param const struct vport \*vport:
        vport to access

.. _`vport_priv.description`:

Description
-----------

If a nonzero size was passed in priv_size of \ :c:func:`vport_alloc`\  a private data
area was allocated on creation.  This allows that area to be accessed and
used for any purpose needed by the vport implementer.

.. _`vport_from_priv`:

vport_from_priv
===============

.. c:function:: struct vport *vport_from_priv(void *priv)

    lookup vport from private data pointer

    :param void \*priv:
        Start of private data area.

.. _`vport_from_priv.description`:

Description
-----------

It is sometimes useful to translate from a pointer to the private data
area to the vport, such as in the case where the private data pointer is
the result of a hash table lookup.  \ ``priv``\  must point to the start of the
private data area.

.. This file was automatic generated / don't edit.


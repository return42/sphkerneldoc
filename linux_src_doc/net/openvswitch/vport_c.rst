.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/openvswitch/vport.c

.. _`ovs_vport_init`:

ovs_vport_init
==============

.. c:function:: int ovs_vport_init( void)

    initialize vport subsystem

    :param void:
        no arguments
    :type void: 

.. _`ovs_vport_init.description`:

Description
-----------

Called at module load time to initialize the vport subsystem.

.. _`ovs_vport_exit`:

ovs_vport_exit
==============

.. c:function:: void ovs_vport_exit( void)

    shutdown vport subsystem

    :param void:
        no arguments
    :type void: 

.. _`ovs_vport_exit.description`:

Description
-----------

Called at module exit time to shutdown the vport subsystem.

.. _`ovs_vport_locate`:

ovs_vport_locate
================

.. c:function:: struct vport *ovs_vport_locate(const struct net *net, const char *name)

    find a port that has already been created

    :param net:
        *undescribed*
    :type net: const struct net \*

    :param name:
        name of port to find
    :type name: const char \*

.. _`ovs_vport_locate.description`:

Description
-----------

Must be called with ovs or RCU read lock.

.. _`ovs_vport_alloc`:

ovs_vport_alloc
===============

.. c:function:: struct vport *ovs_vport_alloc(int priv_size, const struct vport_ops *ops, const struct vport_parms *parms)

    allocate and initialize new vport

    :param priv_size:
        Size of private data area to allocate.
    :type priv_size: int

    :param ops:
        vport device ops
    :type ops: const struct vport_ops \*

    :param parms:
        *undescribed*
    :type parms: const struct vport_parms \*

.. _`ovs_vport_alloc.description`:

Description
-----------

Allocate and initialize a new vport defined by \ ``ops``\ .  The vport will contain
a private data area of size \ ``priv_size``\  that can be accessed using
\ :c:func:`vport_priv`\ .  vports that are no longer needed should be released with
\ :c:func:`vport_free`\ .

.. _`ovs_vport_free`:

ovs_vport_free
==============

.. c:function:: void ovs_vport_free(struct vport *vport)

    uninitialize and free vport

    :param vport:
        vport to free
    :type vport: struct vport \*

.. _`ovs_vport_free.description`:

Description
-----------

Frees a vport allocated with \ :c:func:`vport_alloc`\  when it is no longer needed.

The caller must ensure that an RCU grace period has passed since the last
time \ ``vport``\  was in a datapath.

.. _`ovs_vport_add`:

ovs_vport_add
=============

.. c:function:: struct vport *ovs_vport_add(const struct vport_parms *parms)

    add vport device (for kernel callers)

    :param parms:
        Information about new vport.
    :type parms: const struct vport_parms \*

.. _`ovs_vport_add.description`:

Description
-----------

Creates a new vport with the specified configuration (which is dependent on
device type).  ovs_mutex must be held.

.. _`ovs_vport_set_options`:

ovs_vport_set_options
=====================

.. c:function:: int ovs_vport_set_options(struct vport *vport, struct nlattr *options)

    modify existing vport device (for kernel callers)

    :param vport:
        vport to modify.
    :type vport: struct vport \*

    :param options:
        New configuration.
    :type options: struct nlattr \*

.. _`ovs_vport_set_options.description`:

Description
-----------

Modifies an existing device with the specified configuration (which is
dependent on device type).  ovs_mutex must be held.

.. _`ovs_vport_del`:

ovs_vport_del
=============

.. c:function:: void ovs_vport_del(struct vport *vport)

    delete existing vport device

    :param vport:
        vport to delete.
    :type vport: struct vport \*

.. _`ovs_vport_del.description`:

Description
-----------

Detaches \ ``vport``\  from its datapath and destroys it.  ovs_mutex must
be held.

.. _`ovs_vport_get_stats`:

ovs_vport_get_stats
===================

.. c:function:: void ovs_vport_get_stats(struct vport *vport, struct ovs_vport_stats *stats)

    retrieve device stats

    :param vport:
        vport from which to retrieve the stats
    :type vport: struct vport \*

    :param stats:
        location to store stats
    :type stats: struct ovs_vport_stats \*

.. _`ovs_vport_get_stats.description`:

Description
-----------

Retrieves transmit, receive, and error stats for the given device.

Must be called with ovs_mutex or rcu_read_lock.

.. _`ovs_vport_get_options`:

ovs_vport_get_options
=====================

.. c:function:: int ovs_vport_get_options(const struct vport *vport, struct sk_buff *skb)

    retrieve device options

    :param vport:
        vport from which to retrieve the options.
    :type vport: const struct vport \*

    :param skb:
        sk_buff where options should be appended.
    :type skb: struct sk_buff \*

.. _`ovs_vport_get_options.description`:

Description
-----------

Retrieves the configuration of the given device, appending an
\ ``OVS_VPORT_ATTR_OPTIONS``\  attribute that in turn contains nested
vport-specific attributes to \ ``skb``\ .

Returns 0 if successful, -EMSGSIZE if \ ``skb``\  has insufficient room, or another
negative error code if a real error occurred.  If an error occurs, \ ``skb``\  is
left unmodified.

Must be called with ovs_mutex or rcu_read_lock.

.. _`ovs_vport_set_upcall_portids`:

ovs_vport_set_upcall_portids
============================

.. c:function:: int ovs_vport_set_upcall_portids(struct vport *vport, const struct nlattr *ids)

    set upcall portids of \ ``vport``\ .

    :param vport:
        vport to modify.
    :type vport: struct vport \*

    :param ids:
        new configuration, an array of port ids.
    :type ids: const struct nlattr \*

.. _`ovs_vport_set_upcall_portids.description`:

Description
-----------

Sets the vport's upcall_portids to \ ``ids``\ .

Returns 0 if successful, -EINVAL if \ ``ids``\  is zero length or cannot be parsed
as an array of U32.

Must be called with ovs_mutex.

.. _`ovs_vport_get_upcall_portids`:

ovs_vport_get_upcall_portids
============================

.. c:function:: int ovs_vport_get_upcall_portids(const struct vport *vport, struct sk_buff *skb)

    get the upcall_portids of \ ``vport``\ .

    :param vport:
        vport from which to retrieve the portids.
    :type vport: const struct vport \*

    :param skb:
        sk_buff where portids should be appended.
    :type skb: struct sk_buff \*

.. _`ovs_vport_get_upcall_portids.description`:

Description
-----------

Retrieves the configuration of the given vport, appending the
\ ``OVS_VPORT_ATTR_UPCALL_PID``\  attribute which is the array of upcall
portids to \ ``skb``\ .

Returns 0 if successful, -EMSGSIZE if \ ``skb``\  has insufficient room.
If an error occurs, \ ``skb``\  is left unmodified.  Must be called with
ovs_mutex or rcu_read_lock.

.. _`ovs_vport_find_upcall_portid`:

ovs_vport_find_upcall_portid
============================

.. c:function:: u32 ovs_vport_find_upcall_portid(const struct vport *vport, struct sk_buff *skb)

    find the upcall portid to send upcall.

    :param vport:
        vport from which the missed packet is received.
    :type vport: const struct vport \*

    :param skb:
        skb that the missed packet was received.
    :type skb: struct sk_buff \*

.. _`ovs_vport_find_upcall_portid.description`:

Description
-----------

Uses the \ :c:func:`skb_get_hash`\  to select the upcall portid to send the
upcall.

Returns the portid of the target socket.  Must be called with rcu_read_lock.

.. _`ovs_vport_receive`:

ovs_vport_receive
=================

.. c:function:: int ovs_vport_receive(struct vport *vport, struct sk_buff *skb, const struct ip_tunnel_info *tun_info)

    pass up received packet to the datapath for processing

    :param vport:
        vport that received the packet
    :type vport: struct vport \*

    :param skb:
        skb that was received
    :type skb: struct sk_buff \*

    :param tun_info:
        *undescribed*
    :type tun_info: const struct ip_tunnel_info \*

.. _`ovs_vport_receive.description`:

Description
-----------

Must be called with rcu_read_lock.  The packet cannot be shared and
skb->data should point to the Ethernet header.

.. This file was automatic generated / don't edit.


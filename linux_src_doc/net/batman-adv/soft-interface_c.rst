.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/soft-interface.c

.. _`batadv_skb_head_push`:

batadv_skb_head_push
====================

.. c:function:: int batadv_skb_head_push(struct sk_buff *skb, unsigned int len)

    Increase header size and move (push) head pointer

    :param skb:
        packet buffer which should be modified
    :type skb: struct sk_buff \*

    :param len:
        number of bytes to add
    :type len: unsigned int

.. _`batadv_skb_head_push.return`:

Return
------

0 on success or negative error number in case of failure

.. _`batadv_sum_counter`:

batadv_sum_counter
==================

.. c:function:: u64 batadv_sum_counter(struct batadv_priv *bat_priv, size_t idx)

    Sum the cpu-local counters for index 'idx'

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param idx:
        index of counter to sum up
    :type idx: size_t

.. _`batadv_sum_counter.return`:

Return
------

sum of all cpu-local counters

.. _`batadv_interface_set_rx_mode`:

batadv_interface_set_rx_mode
============================

.. c:function:: void batadv_interface_set_rx_mode(struct net_device *dev)

    set the rx mode of a device

    :param dev:
        registered network device to modify
    :type dev: struct net_device \*

.. _`batadv_interface_set_rx_mode.description`:

Description
-----------

We do not actually need to set any rx filters for the virtual batman
soft interface. However a dummy handler enables a user to set static
multicast listeners for instance.

.. _`batadv_interface_rx`:

batadv_interface_rx
===================

.. c:function:: void batadv_interface_rx(struct net_device *soft_iface, struct sk_buff *skb, int hdr_size, struct batadv_orig_node *orig_node)

    receive ethernet frame on local batman-adv interface

    :param soft_iface:
        local interface which will receive the ethernet frame
    :type soft_iface: struct net_device \*

    :param skb:
        ethernet frame for \ ``soft_iface``\ 
    :type skb: struct sk_buff \*

    :param hdr_size:
        size of already parsed batman-adv header
    :type hdr_size: int

    :param orig_node:
        originator from which the batman-adv packet was sent
    :type orig_node: struct batadv_orig_node \*

.. _`batadv_interface_rx.description`:

Description
-----------

Sends a ethernet frame to the receive path of the local \ ``soft_iface``\ .
skb->data has still point to the batman-adv header with the size \ ``hdr_size``\ .
The caller has to have parsed this header already and made sure that at least
\ ``hdr_size``\  bytes are still available for pull in \ ``skb``\ .

The packet may still get dropped. This can happen when the encapsulated
ethernet frame is invalid or contains again an batman-adv packet. Also
unicast packets will be dropped directly when it was sent between two
isolated clients.

.. _`batadv_softif_vlan_release`:

batadv_softif_vlan_release
==========================

.. c:function:: void batadv_softif_vlan_release(struct kref *ref)

    release vlan from lists and queue for free after rcu grace period

    :param ref:
        kref pointer of the vlan object
    :type ref: struct kref \*

.. _`batadv_softif_vlan_put`:

batadv_softif_vlan_put
======================

.. c:function:: void batadv_softif_vlan_put(struct batadv_softif_vlan *vlan)

    decrease the vlan object refcounter and possibly release it

    :param vlan:
        the vlan object to release
    :type vlan: struct batadv_softif_vlan \*

.. _`batadv_softif_vlan_get`:

batadv_softif_vlan_get
======================

.. c:function:: struct batadv_softif_vlan *batadv_softif_vlan_get(struct batadv_priv *bat_priv, unsigned short vid)

    get the vlan object for a specific vid

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param vid:
        the identifier of the vlan object to retrieve
    :type vid: unsigned short

.. _`batadv_softif_vlan_get.return`:

Return
------

the private data of the vlan matching the vid passed as argument or
NULL otherwise. The refcounter of the returned object is incremented by 1.

.. _`batadv_softif_create_vlan`:

batadv_softif_create_vlan
=========================

.. c:function:: int batadv_softif_create_vlan(struct batadv_priv *bat_priv, unsigned short vid)

    allocate the needed resources for a new vlan

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param vid:
        the VLAN identifier
    :type vid: unsigned short

.. _`batadv_softif_create_vlan.return`:

Return
------

0 on success, a negative error otherwise.

.. _`batadv_softif_destroy_vlan`:

batadv_softif_destroy_vlan
==========================

.. c:function:: void batadv_softif_destroy_vlan(struct batadv_priv *bat_priv, struct batadv_softif_vlan *vlan)

    remove and destroy a softif_vlan object

    :param bat_priv:
        the bat priv with all the soft interface information
    :type bat_priv: struct batadv_priv \*

    :param vlan:
        the object to remove
    :type vlan: struct batadv_softif_vlan \*

.. _`batadv_interface_add_vid`:

batadv_interface_add_vid
========================

.. c:function:: int batadv_interface_add_vid(struct net_device *dev, __be16 proto, unsigned short vid)

    ndo_add_vid API implementation

    :param dev:
        the netdev of the mesh interface
    :type dev: struct net_device \*

    :param proto:
        protocol of the the vlan id
    :type proto: __be16

    :param vid:
        identifier of the new vlan
    :type vid: unsigned short

.. _`batadv_interface_add_vid.description`:

Description
-----------

Set up all the internal structures for handling the new vlan on top of the
mesh interface

.. _`batadv_interface_add_vid.return`:

Return
------

0 on success or a negative error code in case of failure.

.. _`batadv_interface_kill_vid`:

batadv_interface_kill_vid
=========================

.. c:function:: int batadv_interface_kill_vid(struct net_device *dev, __be16 proto, unsigned short vid)

    ndo_kill_vid API implementation

    :param dev:
        the netdev of the mesh interface
    :type dev: struct net_device \*

    :param proto:
        protocol of the the vlan id
    :type proto: __be16

    :param vid:
        identifier of the deleted vlan
    :type vid: unsigned short

.. _`batadv_interface_kill_vid.description`:

Description
-----------

Destroy all the internal structures used to handle the vlan identified by vid
on top of the mesh interface

.. _`batadv_interface_kill_vid.return`:

Return
------

0 on success, -EINVAL if the specified prototype is not ETH_P_8021Q
or -ENOENT if the specified vlan id wasn't registered.

.. _`batadv_set_lockdep_class_one`:

batadv_set_lockdep_class_one
============================

.. c:function:: void batadv_set_lockdep_class_one(struct net_device *dev, struct netdev_queue *txq, void *_unused)

    Set lockdep class for a single tx queue

    :param dev:
        device which owns the tx queue
    :type dev: struct net_device \*

    :param txq:
        tx queue to modify
    :type txq: struct netdev_queue \*

    :param _unused:
        always NULL
    :type _unused: void \*

.. _`batadv_set_lockdep_class`:

batadv_set_lockdep_class
========================

.. c:function:: void batadv_set_lockdep_class(struct net_device *dev)

    Set txq and addr_list lockdep class

    :param dev:
        network device to modify
    :type dev: struct net_device \*

.. _`batadv_softif_init_late`:

batadv_softif_init_late
=======================

.. c:function:: int batadv_softif_init_late(struct net_device *dev)

    late stage initialization of soft interface

    :param dev:
        registered network device to modify
    :type dev: struct net_device \*

.. _`batadv_softif_init_late.return`:

Return
------

error code on failures

.. _`batadv_softif_slave_add`:

batadv_softif_slave_add
=======================

.. c:function:: int batadv_softif_slave_add(struct net_device *dev, struct net_device *slave_dev, struct netlink_ext_ack *extack)

    Add a slave interface to a batadv_soft_interface

    :param dev:
        batadv_soft_interface used as master interface
    :type dev: struct net_device \*

    :param slave_dev:
        net_device which should become the slave interface
    :type slave_dev: struct net_device \*

    :param extack:
        extended ACK report struct
    :type extack: struct netlink_ext_ack \*

.. _`batadv_softif_slave_add.return`:

Return
------

0 if successful or error otherwise.

.. _`batadv_softif_slave_del`:

batadv_softif_slave_del
=======================

.. c:function:: int batadv_softif_slave_del(struct net_device *dev, struct net_device *slave_dev)

    Delete a slave iface from a batadv_soft_interface

    :param dev:
        batadv_soft_interface used as master interface
    :type dev: struct net_device \*

    :param slave_dev:
        net_device which should be removed from the master interface
    :type slave_dev: struct net_device \*

.. _`batadv_softif_slave_del.return`:

Return
------

0 if successful or error otherwise.

.. _`batadv_softif_free`:

batadv_softif_free
==================

.. c:function:: void batadv_softif_free(struct net_device *dev)

    Deconstructor of batadv_soft_interface

    :param dev:
        Device to cleanup and remove
    :type dev: struct net_device \*

.. _`batadv_softif_init_early`:

batadv_softif_init_early
========================

.. c:function:: void batadv_softif_init_early(struct net_device *dev)

    early stage initialization of soft interface

    :param dev:
        registered network device to modify
    :type dev: struct net_device \*

.. _`batadv_softif_create`:

batadv_softif_create
====================

.. c:function:: struct net_device *batadv_softif_create(struct net *net, const char *name)

    Create and register soft interface

    :param net:
        the applicable net namespace
    :type net: struct net \*

    :param name:
        name of the new soft interface
    :type name: const char \*

.. _`batadv_softif_create.return`:

Return
------

newly allocated soft_interface, NULL on errors

.. _`batadv_softif_destroy_sysfs`:

batadv_softif_destroy_sysfs
===========================

.. c:function:: void batadv_softif_destroy_sysfs(struct net_device *soft_iface)

    deletion of batadv_soft_interface via sysfs

    :param soft_iface:
        the to-be-removed batman-adv interface
    :type soft_iface: struct net_device \*

.. _`batadv_softif_destroy_netlink`:

batadv_softif_destroy_netlink
=============================

.. c:function:: void batadv_softif_destroy_netlink(struct net_device *soft_iface, struct list_head *head)

    deletion of batadv_soft_interface via netlink

    :param soft_iface:
        the to-be-removed batman-adv interface
    :type soft_iface: struct net_device \*

    :param head:
        list pointer
    :type head: struct list_head \*

.. _`batadv_softif_is_valid`:

batadv_softif_is_valid
======================

.. c:function:: bool batadv_softif_is_valid(const struct net_device *net_dev)

    Check whether device is a batadv soft interface

    :param net_dev:
        device which should be checked
    :type net_dev: const struct net_device \*

.. _`batadv_softif_is_valid.return`:

Return
------

true when net_dev is a batman-adv interface, false otherwise

.. This file was automatic generated / don't edit.


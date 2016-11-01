.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/soft-interface.c

.. _`batadv_interface_set_rx_mode`:

batadv_interface_set_rx_mode
============================

.. c:function:: void batadv_interface_set_rx_mode(struct net_device *dev)

    set the rx mode of a device

    :param struct net_device \*dev:
        registered network device to modify

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

    :param struct net_device \*soft_iface:
        local interface which will receive the ethernet frame

    :param struct sk_buff \*skb:
        ethernet frame for \ ``soft_iface``\ 

    :param int hdr_size:
        size of already parsed batman-adv header

    :param struct batadv_orig_node \*orig_node:
        originator from which the batman-adv packet was sent

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

    :param struct kref \*ref:
        kref pointer of the vlan object

.. _`batadv_softif_vlan_put`:

batadv_softif_vlan_put
======================

.. c:function:: void batadv_softif_vlan_put(struct batadv_softif_vlan *vlan)

    decrease the vlan object refcounter and possibly release it

    :param struct batadv_softif_vlan \*vlan:
        the vlan object to release

.. _`batadv_softif_vlan_get`:

batadv_softif_vlan_get
======================

.. c:function:: struct batadv_softif_vlan *batadv_softif_vlan_get(struct batadv_priv *bat_priv, unsigned short vid)

    get the vlan object for a specific vid

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param unsigned short vid:
        the identifier of the vlan object to retrieve

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

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param unsigned short vid:
        the VLAN identifier

.. _`batadv_softif_create_vlan.return`:

Return
------

0 on success, a negative error otherwise.

.. _`batadv_softif_destroy_vlan`:

batadv_softif_destroy_vlan
==========================

.. c:function:: void batadv_softif_destroy_vlan(struct batadv_priv *bat_priv, struct batadv_softif_vlan *vlan)

    remove and destroy a softif_vlan object

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_softif_vlan \*vlan:
        the object to remove

.. _`batadv_interface_add_vid`:

batadv_interface_add_vid
========================

.. c:function:: int batadv_interface_add_vid(struct net_device *dev, __be16 proto, unsigned short vid)

    ndo_add_vid API implementation

    :param struct net_device \*dev:
        the netdev of the mesh interface

    :param __be16 proto:
        protocol of the the vlan id

    :param unsigned short vid:
        identifier of the new vlan

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

    :param struct net_device \*dev:
        the netdev of the mesh interface

    :param __be16 proto:
        protocol of the the vlan id

    :param unsigned short vid:
        identifier of the deleted vlan

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

    :param struct net_device \*dev:
        device which owns the tx queue

    :param struct netdev_queue \*txq:
        tx queue to modify

    :param void \*_unused:
        always NULL

.. _`batadv_set_lockdep_class`:

batadv_set_lockdep_class
========================

.. c:function:: void batadv_set_lockdep_class(struct net_device *dev)

    Set txq and addr_list lockdep class

    :param struct net_device \*dev:
        network device to modify

.. _`batadv_softif_init_late`:

batadv_softif_init_late
=======================

.. c:function:: int batadv_softif_init_late(struct net_device *dev)

    late stage initialization of soft interface

    :param struct net_device \*dev:
        registered network device to modify

.. _`batadv_softif_init_late.return`:

Return
------

error code on failures

.. _`batadv_softif_slave_add`:

batadv_softif_slave_add
=======================

.. c:function:: int batadv_softif_slave_add(struct net_device *dev, struct net_device *slave_dev)

    Add a slave interface to a batadv_soft_interface

    :param struct net_device \*dev:
        batadv_soft_interface used as master interface

    :param struct net_device \*slave_dev:
        net_device which should become the slave interface

.. _`batadv_softif_slave_add.return`:

Return
------

0 if successful or error otherwise.

.. _`batadv_softif_slave_del`:

batadv_softif_slave_del
=======================

.. c:function:: int batadv_softif_slave_del(struct net_device *dev, struct net_device *slave_dev)

    Delete a slave iface from a batadv_soft_interface

    :param struct net_device \*dev:
        batadv_soft_interface used as master interface

    :param struct net_device \*slave_dev:
        net_device which should be removed from the master interface

.. _`batadv_softif_slave_del.return`:

Return
------

0 if successful or error otherwise.

.. _`batadv_softif_free`:

batadv_softif_free
==================

.. c:function:: void batadv_softif_free(struct net_device *dev)

    Deconstructor of batadv_soft_interface

    :param struct net_device \*dev:
        Device to cleanup and remove

.. _`batadv_softif_init_early`:

batadv_softif_init_early
========================

.. c:function:: void batadv_softif_init_early(struct net_device *dev)

    early stage initialization of soft interface

    :param struct net_device \*dev:
        registered network device to modify

.. _`batadv_softif_destroy_sysfs`:

batadv_softif_destroy_sysfs
===========================

.. c:function:: void batadv_softif_destroy_sysfs(struct net_device *soft_iface)

    deletion of batadv_soft_interface via sysfs

    :param struct net_device \*soft_iface:
        the to-be-removed batman-adv interface

.. _`batadv_softif_destroy_netlink`:

batadv_softif_destroy_netlink
=============================

.. c:function:: void batadv_softif_destroy_netlink(struct net_device *soft_iface, struct list_head *head)

    deletion of batadv_soft_interface via netlink

    :param struct net_device \*soft_iface:
        the to-be-removed batman-adv interface

    :param struct list_head \*head:
        list pointer

.. This file was automatic generated / don't edit.


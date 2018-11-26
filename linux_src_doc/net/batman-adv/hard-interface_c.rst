.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/hard-interface.c

.. _`batadv_hardif_release`:

batadv_hardif_release
=====================

.. c:function:: void batadv_hardif_release(struct kref *ref)

    release hard interface from lists and queue for free after rcu grace period

    :param ref:
        kref pointer of the hard interface
    :type ref: struct kref \*

.. _`batadv_hardif_get_by_netdev`:

batadv_hardif_get_by_netdev
===========================

.. c:function:: struct batadv_hard_iface *batadv_hardif_get_by_netdev(const struct net_device *net_dev)

    Get hard interface object of a net_device

    :param net_dev:
        net_device to search for
    :type net_dev: const struct net_device \*

.. _`batadv_hardif_get_by_netdev.return`:

Return
------

batadv_hard_iface of net_dev (with increased refcnt), NULL on errors

.. _`batadv_getlink_net`:

batadv_getlink_net
==================

.. c:function:: struct net *batadv_getlink_net(const struct net_device *netdev, struct net *fallback_net)

    return link net namespace (of use fallback)

    :param netdev:
        net_device to check
    :type netdev: const struct net_device \*

    :param fallback_net:
        return in case get_link_net is not available for \ ``netdev``\ 
    :type fallback_net: struct net \*

.. _`batadv_getlink_net.return`:

Return
------

result of rtnl_link_ops->get_link_net or \ ``fallback_net``\ 

.. _`batadv_mutual_parents`:

batadv_mutual_parents
=====================

.. c:function:: bool batadv_mutual_parents(const struct net_device *dev1, struct net *net1, const struct net_device *dev2, struct net *net2)

    check if two devices are each others parent

    :param dev1:
        1st net dev
    :type dev1: const struct net_device \*

    :param net1:
        1st devices netns
    :type net1: struct net \*

    :param dev2:
        2nd net dev
    :type dev2: const struct net_device \*

    :param net2:
        2nd devices netns
    :type net2: struct net \*

.. _`batadv_mutual_parents.description`:

Description
-----------

veth devices come in pairs and each is the parent of the other!

.. _`batadv_mutual_parents.return`:

Return
------

true if the devices are each others parent, otherwise false

.. _`batadv_is_on_batman_iface`:

batadv_is_on_batman_iface
=========================

.. c:function:: bool batadv_is_on_batman_iface(const struct net_device *net_dev)

    check if a device is a batman iface descendant

    :param net_dev:
        the device to check
    :type net_dev: const struct net_device \*

.. _`batadv_is_on_batman_iface.description`:

Description
-----------

If the user creates any virtual device on top of a batman-adv interface, it
is important to prevent this new interface to be used to create a new mesh
network (this behaviour would lead to a batman-over-batman configuration).
This function recursively checks all the fathers of the device passed as
argument looking for a batman-adv soft interface.

.. _`batadv_is_on_batman_iface.return`:

Return
------

true if the device is descendant of a batman-adv mesh interface (or
if it is a batman-adv interface itself), false otherwise

.. _`batadv_get_real_netdevice`:

batadv_get_real_netdevice
=========================

.. c:function:: struct net_device *batadv_get_real_netdevice(struct net_device *netdev)

    check if the given netdev struct is a virtual interface on top of another 'real' interface

    :param netdev:
        the device to check
    :type netdev: struct net_device \*

.. _`batadv_get_real_netdevice.description`:

Description
-----------

Callers must hold the rtnl semaphore. You may want \ :c:func:`batadv_get_real_netdev`\ 
instead of this.

.. _`batadv_get_real_netdevice.return`:

Return
------

the 'real' net device or the original net device and NULL in case
of an error.

.. _`batadv_get_real_netdev`:

batadv_get_real_netdev
======================

.. c:function:: struct net_device *batadv_get_real_netdev(struct net_device *net_device)

    check if the given net_device struct is a virtual interface on top of another 'real' interface

    :param net_device:
        the device to check
    :type net_device: struct net_device \*

.. _`batadv_get_real_netdev.return`:

Return
------

the 'real' net device or the original net device and NULL in case
of an error.

.. _`batadv_is_wext_netdev`:

batadv_is_wext_netdev
=====================

.. c:function:: bool batadv_is_wext_netdev(struct net_device *net_device)

    check if the given net_device struct is a wext wifi interface

    :param net_device:
        the device to check
    :type net_device: struct net_device \*

.. _`batadv_is_wext_netdev.return`:

Return
------

true if the net device is a wext wireless device, false
otherwise.

.. _`batadv_is_cfg80211_netdev`:

batadv_is_cfg80211_netdev
=========================

.. c:function:: bool batadv_is_cfg80211_netdev(struct net_device *net_device)

    check if the given net_device struct is a cfg80211 wifi interface

    :param net_device:
        the device to check
    :type net_device: struct net_device \*

.. _`batadv_is_cfg80211_netdev.return`:

Return
------

true if the net device is a cfg80211 wireless device, false
otherwise.

.. _`batadv_wifi_flags_evaluate`:

batadv_wifi_flags_evaluate
==========================

.. c:function:: u32 batadv_wifi_flags_evaluate(struct net_device *net_device)

    calculate wifi flags for net_device

    :param net_device:
        the device to check
    :type net_device: struct net_device \*

.. _`batadv_wifi_flags_evaluate.return`:

Return
------

batadv_hard_iface_wifi_flags flags of the device

.. _`batadv_is_cfg80211_hardif`:

batadv_is_cfg80211_hardif
=========================

.. c:function:: bool batadv_is_cfg80211_hardif(struct batadv_hard_iface *hard_iface)

    check if the given hardif is a cfg80211 wifi interface

    :param hard_iface:
        the device to check
    :type hard_iface: struct batadv_hard_iface \*

.. _`batadv_is_cfg80211_hardif.return`:

Return
------

true if the net device is a cfg80211 wireless device, false
otherwise.

.. _`batadv_is_wifi_hardif`:

batadv_is_wifi_hardif
=====================

.. c:function:: bool batadv_is_wifi_hardif(struct batadv_hard_iface *hard_iface)

    check if the given hardif is a wifi interface

    :param hard_iface:
        the device to check
    :type hard_iface: struct batadv_hard_iface \*

.. _`batadv_is_wifi_hardif.return`:

Return
------

true if the net device is a 802.11 wireless device, false otherwise.

.. _`batadv_hardif_no_broadcast`:

batadv_hardif_no_broadcast
==========================

.. c:function:: int batadv_hardif_no_broadcast(struct batadv_hard_iface *if_outgoing, u8 *orig_addr, u8 *orig_neigh)

    check whether (re)broadcast is necessary

    :param if_outgoing:
        the outgoing interface checked and considered for (re)broadcast
    :type if_outgoing: struct batadv_hard_iface \*

    :param orig_addr:
        the originator of this packet
    :type orig_addr: u8 \*

    :param orig_neigh:
        originator address of the forwarder we just got the packet from
        (NULL if we originated)
    :type orig_neigh: u8 \*

.. _`batadv_hardif_no_broadcast.description`:

Description
-----------

Checks whether a packet needs to be (re)broadcasted on the given interface.

.. _`batadv_hardif_no_broadcast.batadv_hardif_bcast_norecipient`:

BATADV_HARDIF_BCAST_NORECIPIENT
-------------------------------

No neighbor on interface

.. _`batadv_hardif_no_broadcast.batadv_hardif_bcast_dupfwd`:

BATADV_HARDIF_BCAST_DUPFWD
--------------------------

Just one neighbor, but it is the forwarder

.. _`batadv_hardif_no_broadcast.batadv_hardif_bcast_duporig`:

BATADV_HARDIF_BCAST_DUPORIG
---------------------------

Just one neighbor, but it is the originator

.. _`batadv_hardif_no_broadcast.batadv_hardif_bcast_ok`:

BATADV_HARDIF_BCAST_OK
----------------------

Several neighbors, must broadcast

.. _`batadv_hardif_recalc_extra_skbroom`:

batadv_hardif_recalc_extra_skbroom
==================================

.. c:function:: void batadv_hardif_recalc_extra_skbroom(struct net_device *soft_iface)

    Recalculate skbuff extra head/tailroom

    :param soft_iface:
        netdev struct of the mesh interface
    :type soft_iface: struct net_device \*

.. _`batadv_hardif_min_mtu`:

batadv_hardif_min_mtu
=====================

.. c:function:: int batadv_hardif_min_mtu(struct net_device *soft_iface)

    Calculate maximum MTU for soft interface

    :param soft_iface:
        netdev struct of the soft interface
    :type soft_iface: struct net_device \*

.. _`batadv_hardif_min_mtu.return`:

Return
------

MTU for the soft-interface (limited by the minimal MTU of all active
slave interfaces)

.. _`batadv_update_min_mtu`:

batadv_update_min_mtu
=====================

.. c:function:: void batadv_update_min_mtu(struct net_device *soft_iface)

    Adjusts the MTU if a new interface with a smaller MTU appeared

    :param soft_iface:
        netdev struct of the soft interface
    :type soft_iface: struct net_device \*

.. _`batadv_master_del_slave`:

batadv_master_del_slave
=======================

.. c:function:: int batadv_master_del_slave(struct batadv_hard_iface *slave, struct net_device *master)

    remove hard_iface from the current master iface

    :param slave:
        the interface enslaved in another master
    :type slave: struct batadv_hard_iface \*

    :param master:
        the master from which slave has to be removed
    :type master: struct net_device \*

.. _`batadv_master_del_slave.description`:

Description
-----------

Invoke ndo_del_slave on master passing slave as argument. In this way slave
is free'd and master can correctly change its internal state.

.. _`batadv_master_del_slave.return`:

Return
------

0 on success, a negative value representing the error otherwise

.. _`batadv_hardif_enable_interface`:

batadv_hardif_enable_interface
==============================

.. c:function:: int batadv_hardif_enable_interface(struct batadv_hard_iface *hard_iface, struct net *net, const char *iface_name)

    Enslave hard interface to soft interface

    :param hard_iface:
        hard interface to add to soft interface
    :type hard_iface: struct batadv_hard_iface \*

    :param net:
        the applicable net namespace
    :type net: struct net \*

    :param iface_name:
        name of the soft interface
    :type iface_name: const char \*

.. _`batadv_hardif_enable_interface.return`:

Return
------

0 on success or negative error number in case of failure

.. _`batadv_hardif_cnt`:

batadv_hardif_cnt
=================

.. c:function:: size_t batadv_hardif_cnt(const struct net_device *soft_iface)

    get number of interfaces enslaved to soft interface

    :param soft_iface:
        soft interface to check
    :type soft_iface: const struct net_device \*

.. _`batadv_hardif_cnt.description`:

Description
-----------

This function is only using RCU for locking - the result can therefore be
off when another functions is modifying the list at the same time. The
caller can use the rtnl_lock to make sure that the count is accurate.

.. _`batadv_hardif_cnt.return`:

Return
------

number of connected/enslaved hard interfaces

.. _`batadv_hardif_disable_interface`:

batadv_hardif_disable_interface
===============================

.. c:function:: void batadv_hardif_disable_interface(struct batadv_hard_iface *hard_iface, enum batadv_hard_if_cleanup autodel)

    Remove hard interface from soft interface

    :param hard_iface:
        hard interface to be removed
    :type hard_iface: struct batadv_hard_iface \*

    :param autodel:
        whether to delete soft interface when it doesn't contain any other
        slave interfaces
    :type autodel: enum batadv_hard_if_cleanup

.. _`batadv_hardif_remove_interfaces`:

batadv_hardif_remove_interfaces
===============================

.. c:function:: void batadv_hardif_remove_interfaces( void)

    Remove all hard interfaces

    :param void:
        no arguments
    :type void: 

.. _`batadv_hard_if_event_softif`:

batadv_hard_if_event_softif
===========================

.. c:function:: int batadv_hard_if_event_softif(unsigned long event, struct net_device *net_dev)

    Handle events for soft interfaces

    :param event:
        NETDEV\_\* event to handle
    :type event: unsigned long

    :param net_dev:
        net_device which generated an event
    :type net_dev: struct net_device \*

.. _`batadv_hard_if_event_softif.return`:

Return
------

NOTIFY\_\* result

.. This file was automatic generated / don't edit.


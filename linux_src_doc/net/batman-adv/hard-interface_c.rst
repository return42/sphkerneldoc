.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/hard-interface.c

.. _`batadv_hardif_release`:

batadv_hardif_release
=====================

.. c:function:: void batadv_hardif_release(struct kref *ref)

    release hard interface from lists and queue for free after rcu grace period

    :param struct kref \*ref:
        kref pointer of the hard interface

.. _`batadv_getlink_net`:

batadv_getlink_net
==================

.. c:function:: struct net *batadv_getlink_net(const struct net_device *netdev, struct net *fallback_net)

    return link net namespace (of use fallback)

    :param const struct net_device \*netdev:
        net_device to check

    :param struct net \*fallback_net:
        return in case get_link_net is not available for \ ``netdev``\ 

.. _`batadv_getlink_net.return`:

Return
------

result of rtnl_link_ops->get_link_net or \ ``fallback_net``\ 

.. _`batadv_mutual_parents`:

batadv_mutual_parents
=====================

.. c:function:: bool batadv_mutual_parents(const struct net_device *dev1, struct net *net1, const struct net_device *dev2, struct net *net2)

    check if two devices are each others parent

    :param const struct net_device \*dev1:
        1st net dev

    :param struct net \*net1:
        1st devices netns

    :param const struct net_device \*dev2:
        2nd net dev

    :param struct net \*net2:
        2nd devices netns

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

    :param const struct net_device \*net_dev:
        the device to check

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

    :param struct net_device \*netdev:
        the device to check

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

    :param struct net_device \*net_device:
        the device to check

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

    :param struct net_device \*net_device:
        the device to check

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

    :param struct net_device \*net_device:
        the device to check

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

    :param struct net_device \*net_device:
        the device to check

.. _`batadv_wifi_flags_evaluate.return`:

Return
------

batadv_hard_iface_wifi_flags flags of the device

.. _`batadv_is_cfg80211_hardif`:

batadv_is_cfg80211_hardif
=========================

.. c:function:: bool batadv_is_cfg80211_hardif(struct batadv_hard_iface *hard_iface)

    check if the given hardif is a cfg80211 wifi interface

    :param struct batadv_hard_iface \*hard_iface:
        the device to check

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

    :param struct batadv_hard_iface \*hard_iface:
        the device to check

.. _`batadv_is_wifi_hardif.return`:

Return
------

true if the net device is a 802.11 wireless device, false otherwise.

.. _`batadv_hardif_no_broadcast`:

batadv_hardif_no_broadcast
==========================

.. c:function:: int batadv_hardif_no_broadcast(struct batadv_hard_iface *if_outgoing, u8 *orig_addr, u8 *orig_neigh)

    check whether (re)broadcast is necessary

    :param struct batadv_hard_iface \*if_outgoing:
        the outgoing interface checked and considered for (re)broadcast

    :param u8 \*orig_addr:
        the originator of this packet

    :param u8 \*orig_neigh:
        originator address of the forwarder we just got the packet from
        (NULL if we originated)

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

    :param struct net_device \*soft_iface:
        netdev struct of the mesh interface

.. _`batadv_master_del_slave`:

batadv_master_del_slave
=======================

.. c:function:: int batadv_master_del_slave(struct batadv_hard_iface *slave, struct net_device *master)

    remove hard_iface from the current master interface

    :param struct batadv_hard_iface \*slave:
        the interface enslaved in another master

    :param struct net_device \*master:
        the master from which slave has to be removed

.. _`batadv_master_del_slave.description`:

Description
-----------

Invoke ndo_del_slave on master passing slave as argument. In this way slave
is free'd and master can correctly change its internal state.

.. _`batadv_master_del_slave.return`:

Return
------

0 on success, a negative value representing the error otherwise

.. This file was automatic generated / don't edit.


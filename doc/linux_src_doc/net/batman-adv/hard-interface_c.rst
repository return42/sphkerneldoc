.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/hard-interface.c

.. _`batadv_hardif_release`:

batadv_hardif_release
=====================

.. c:function:: void batadv_hardif_release(struct kref *ref)

    release hard interface from lists and queue for free after rcu grace period

    :param struct kref \*ref:
        kref pointer of the hard interface

.. _`batadv_mutual_parents`:

batadv_mutual_parents
=====================

.. c:function:: bool batadv_mutual_parents(const struct net_device *dev1, const struct net_device *dev2)

    check if two devices are each others parent

    :param const struct net_device \*dev1:
        1st net_device

    :param const struct net_device \*dev2:
        2nd net_device

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

.. _`batadv_is_wifi_netdev`:

batadv_is_wifi_netdev
=====================

.. c:function:: bool batadv_is_wifi_netdev(struct net_device *net_device)

    check if the given net_device struct is a wifi interface

    :param struct net_device \*net_device:
        the device to check

.. _`batadv_is_wifi_netdev.return`:

Return
------

true if the net device is a 802.11 wireless device, false otherwise.

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

.. _`batadv_hardif_remove_interface_finish`:

batadv_hardif_remove_interface_finish
=====================================

.. c:function:: void batadv_hardif_remove_interface_finish(struct work_struct *work)

    cleans up the remains of a hardif

    :param struct work_struct \*work:
        work queue item

.. _`batadv_hardif_remove_interface_finish.description`:

Description
-----------

Free the parts of the hard interface which can not be removed under
rtnl lock (to prevent deadlock situations).

.. This file was automatic generated / don't edit.


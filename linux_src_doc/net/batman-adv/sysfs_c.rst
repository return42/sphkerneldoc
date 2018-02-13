.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/sysfs.c

.. _`batadv_vlan_kobj_to_batpriv`:

batadv_vlan_kobj_to_batpriv
===========================

.. c:function:: struct batadv_priv *batadv_vlan_kobj_to_batpriv(struct kobject *obj)

    convert a vlan kobj in the associated batpriv

    :param struct kobject \*obj:
        kobject to covert

.. _`batadv_vlan_kobj_to_batpriv.return`:

Return
------

the associated batadv_priv struct.

.. _`batadv_kobj_to_vlan`:

batadv_kobj_to_vlan
===================

.. c:function:: struct batadv_softif_vlan *batadv_kobj_to_vlan(struct batadv_priv *bat_priv, struct kobject *obj)

    convert a kobj in the associated softif_vlan struct

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct kobject \*obj:
        kobject to covert

.. _`batadv_kobj_to_vlan.return`:

Return
------

the associated softif_vlan struct if found, NULL otherwise.

.. _`batadv_show_isolation_mark`:

batadv_show_isolation_mark
==========================

.. c:function:: ssize_t batadv_show_isolation_mark(struct kobject *kobj, struct attribute *attr, char *buff)

    print the current isolation mark/mask

    :param struct kobject \*kobj:
        kobject representing the private mesh sysfs directory

    :param struct attribute \*attr:
        the batman-adv attribute the user is interacting with

    :param char \*buff:
        the buffer that will contain the data to send back to the user

.. _`batadv_show_isolation_mark.return`:

Return
------

the number of bytes written into 'buff' on success or a negative
error code in case of failure

.. _`batadv_store_isolation_mark`:

batadv_store_isolation_mark
===========================

.. c:function:: ssize_t batadv_store_isolation_mark(struct kobject *kobj, struct attribute *attr, char *buff, size_t count)

    parse and store the isolation mark/mask entered by the user

    :param struct kobject \*kobj:
        kobject representing the private mesh sysfs directory

    :param struct attribute \*attr:
        the batman-adv attribute the user is interacting with

    :param char \*buff:
        the buffer containing the user data

    :param size_t count:
        number of bytes in the buffer

.. _`batadv_store_isolation_mark.return`:

Return
------

'count' on success or a negative error code in case of failure

.. _`batadv_sysfs_add_meshif`:

batadv_sysfs_add_meshif
=======================

.. c:function:: int batadv_sysfs_add_meshif(struct net_device *dev)

    Add soft interface specific sysfs entries

    :param struct net_device \*dev:
        netdev struct of the soft interface

.. _`batadv_sysfs_add_meshif.return`:

Return
------

0 on success or negative error number in case of failure

.. _`batadv_sysfs_del_meshif`:

batadv_sysfs_del_meshif
=======================

.. c:function:: void batadv_sysfs_del_meshif(struct net_device *dev)

    Remove soft interface specific sysfs entries

    :param struct net_device \*dev:
        netdev struct of the soft interface

.. _`batadv_sysfs_add_vlan`:

batadv_sysfs_add_vlan
=====================

.. c:function:: int batadv_sysfs_add_vlan(struct net_device *dev, struct batadv_softif_vlan *vlan)

    add all the needed sysfs objects for the new vlan

    :param struct net_device \*dev:
        netdev of the mesh interface

    :param struct batadv_softif_vlan \*vlan:
        private data of the newly added VLAN interface

.. _`batadv_sysfs_add_vlan.return`:

Return
------

0 on success and -ENOMEM if any of the structure allocations fails.

.. _`batadv_sysfs_del_vlan`:

batadv_sysfs_del_vlan
=====================

.. c:function:: void batadv_sysfs_del_vlan(struct batadv_priv *bat_priv, struct batadv_softif_vlan *vlan)

    remove all the sysfs objects for a given VLAN

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param struct batadv_softif_vlan \*vlan:
        the private data of the VLAN to destroy

.. _`batadv_store_mesh_iface_finish`:

batadv_store_mesh_iface_finish
==============================

.. c:function:: int batadv_store_mesh_iface_finish(struct net_device *net_dev, char ifname)

    store new hardif mesh_iface state

    :param struct net_device \*net_dev:
        netdevice to add/remove to/from batman-adv soft-interface

    :param char ifname:
        name of soft-interface to modify

.. _`batadv_store_mesh_iface_finish.description`:

Description
-----------

Changes the parts of the hard+soft interface which can not be modified under
sysfs lock (to prevent deadlock situations).

.. _`batadv_store_mesh_iface_finish.return`:

Return
------

0 on success, 0 < on failure

.. _`batadv_store_mesh_iface_work`:

batadv_store_mesh_iface_work
============================

.. c:function:: void batadv_store_mesh_iface_work(struct work_struct *work)

    store new hardif mesh_iface state

    :param struct work_struct \*work:
        work queue item

.. _`batadv_store_mesh_iface_work.description`:

Description
-----------

Changes the parts of the hard+soft interface which can not be modified under
sysfs lock (to prevent deadlock situations).

.. _`batadv_store_throughput_override`:

batadv_store_throughput_override
================================

.. c:function:: ssize_t batadv_store_throughput_override(struct kobject *kobj, struct attribute *attr, char *buff, size_t count)

    parse and store throughput override entered by the user

    :param struct kobject \*kobj:
        kobject representing the private mesh sysfs directory

    :param struct attribute \*attr:
        the batman-adv attribute the user is interacting with

    :param char \*buff:
        the buffer containing the user data

    :param size_t count:
        number of bytes in the buffer

.. _`batadv_store_throughput_override.return`:

Return
------

'count' on success or a negative error code in case of failure

.. _`batadv_sysfs_add_hardif`:

batadv_sysfs_add_hardif
=======================

.. c:function:: int batadv_sysfs_add_hardif(struct kobject **hardif_obj, struct net_device *dev)

    Add hard interface specific sysfs entries

    :param struct kobject \*\*hardif_obj:
        address where to store the pointer to new sysfs folder

    :param struct net_device \*dev:
        netdev struct of the hard interface

.. _`batadv_sysfs_add_hardif.return`:

Return
------

0 on success or negative error number in case of failure

.. _`batadv_sysfs_del_hardif`:

batadv_sysfs_del_hardif
=======================

.. c:function:: void batadv_sysfs_del_hardif(struct kobject **hardif_obj)

    Remove hard interface specific sysfs entries

    :param struct kobject \*\*hardif_obj:
        address to the pointer to which stores batman-adv sysfs folder
        of the hard interface

.. _`batadv_throw_uevent`:

batadv_throw_uevent
===================

.. c:function:: int batadv_throw_uevent(struct batadv_priv *bat_priv, enum batadv_uev_type type, enum batadv_uev_action action, const char *data)

    Send an uevent with batman-adv specific env data

    :param struct batadv_priv \*bat_priv:
        the bat priv with all the soft interface information

    :param enum batadv_uev_type type:
        subsystem type of event. Stored in uevent's BATTYPE

    :param enum batadv_uev_action action:
        action type of event. Stored in uevent's BATACTION

    :param const char \*data:
        string with additional information to the event (ignored for
        BATADV_UEV_DEL). Stored in uevent's BATDATA

.. _`batadv_throw_uevent.return`:

Return
------

0 on success or negative error number in case of failure

.. This file was automatic generated / don't edit.


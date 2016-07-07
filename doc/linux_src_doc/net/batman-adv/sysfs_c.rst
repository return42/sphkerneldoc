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

.. This file was automatic generated / don't edit.


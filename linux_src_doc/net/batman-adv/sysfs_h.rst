.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/batman-adv/sysfs.h

.. _`batadv_sysfs_vlan_subdir_prefix`:

BATADV_SYSFS_VLAN_SUBDIR_PREFIX
===============================

.. c:function::  BATADV_SYSFS_VLAN_SUBDIR_PREFIX()

    prefix of the subfolder that will be created in the sysfs hierarchy for each VLAN interface. The subfolder will be named "BATADV_SYSFS_VLAN_SUBDIR_PREFIX%vid".

.. _`batadv_attribute`:

struct batadv_attribute
=======================

.. c:type:: struct batadv_attribute

    sysfs export helper for batman-adv attributes

.. _`batadv_attribute.definition`:

Definition
----------

.. code-block:: c

    struct batadv_attribute {
        struct attribute attr;
        ssize_t (*show)(struct kobject *kobj, struct attribute *attr, char *buf);
        ssize_t (*store)(struct kobject *kobj, struct attribute *attr, char *buf, size_t count);
    }

.. _`batadv_attribute.members`:

Members
-------

attr
    sysfs attribute file

show
    function to export the current attribute's content to sysfs

store
    function to load new value from character buffer and save itin batman-adv attribute

.. This file was automatic generated / don't edit.


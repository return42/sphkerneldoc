.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/iscsi_boot_sysfs.c

.. _`iscsi_boot_create_target`:

iscsi_boot_create_target
========================

.. c:function:: struct iscsi_boot_kobj *iscsi_boot_create_target(struct iscsi_boot_kset *boot_kset, int index, void *data, ssize_t (*show)(void *data, int type, char *buf), umode_t (*is_visible)(void *data, int type), void (*release)(void *data))

    create boot target sysfs dir

    :param boot_kset:
        boot kset
    :type boot_kset: struct iscsi_boot_kset \*

    :param index:
        the target id
    :type index: int

    :param data:
        driver specific data for target
    :type data: void \*

    :param ssize_t (\*show)(void \*data, int type, char \*buf):
        attr show function

    :param umode_t (\*is_visible)(void \*data, int type):
        attr visibility function

    :param void (\*release)(void \*data):
        release function

.. _`iscsi_boot_create_target.note`:

Note
----

The boot sysfs lib will free the data passed in for the caller
when all refs to the target kobject have been released.

.. _`iscsi_boot_create_initiator`:

iscsi_boot_create_initiator
===========================

.. c:function:: struct iscsi_boot_kobj *iscsi_boot_create_initiator(struct iscsi_boot_kset *boot_kset, int index, void *data, ssize_t (*show)(void *data, int type, char *buf), umode_t (*is_visible)(void *data, int type), void (*release)(void *data))

    create boot initiator sysfs dir

    :param boot_kset:
        boot kset
    :type boot_kset: struct iscsi_boot_kset \*

    :param index:
        the initiator id
    :type index: int

    :param data:
        driver specific data
    :type data: void \*

    :param ssize_t (\*show)(void \*data, int type, char \*buf):
        attr show function

    :param umode_t (\*is_visible)(void \*data, int type):
        attr visibility function

    :param void (\*release)(void \*data):
        release function

.. _`iscsi_boot_create_initiator.note`:

Note
----

The boot sysfs lib will free the data passed in for the caller
when all refs to the initiator kobject have been released.

.. _`iscsi_boot_create_ethernet`:

iscsi_boot_create_ethernet
==========================

.. c:function:: struct iscsi_boot_kobj *iscsi_boot_create_ethernet(struct iscsi_boot_kset *boot_kset, int index, void *data, ssize_t (*show)(void *data, int type, char *buf), umode_t (*is_visible)(void *data, int type), void (*release)(void *data))

    create boot ethernet sysfs dir

    :param boot_kset:
        boot kset
    :type boot_kset: struct iscsi_boot_kset \*

    :param index:
        the ethernet device id
    :type index: int

    :param data:
        driver specific data
    :type data: void \*

    :param ssize_t (\*show)(void \*data, int type, char \*buf):
        attr show function

    :param umode_t (\*is_visible)(void \*data, int type):
        attr visibility function

    :param void (\*release)(void \*data):
        release function

.. _`iscsi_boot_create_ethernet.note`:

Note
----

The boot sysfs lib will free the data passed in for the caller
when all refs to the ethernet kobject have been released.

.. _`iscsi_boot_create_acpitbl`:

iscsi_boot_create_acpitbl
=========================

.. c:function:: struct iscsi_boot_kobj *iscsi_boot_create_acpitbl(struct iscsi_boot_kset *boot_kset, int index, void *data, ssize_t (*show)(void *data, int type, char *buf), umode_t (*is_visible)(void *data, int type), void (*release)(void *data))

    create boot acpi table sysfs dir

    :param boot_kset:
        boot kset
    :type boot_kset: struct iscsi_boot_kset \*

    :param index:
        not used
    :type index: int

    :param data:
        driver specific data
    :type data: void \*

    :param ssize_t (\*show)(void \*data, int type, char \*buf):
        attr show function

    :param umode_t (\*is_visible)(void \*data, int type):
        attr visibility function

    :param void (\*release)(void \*data):
        release function

.. _`iscsi_boot_create_acpitbl.note`:

Note
----

The boot sysfs lib will free the data passed in for the caller
when all refs to the acpitbl kobject have been released.

.. _`iscsi_boot_create_kset`:

iscsi_boot_create_kset
======================

.. c:function:: struct iscsi_boot_kset *iscsi_boot_create_kset(const char *set_name)

    creates root sysfs tree

    :param set_name:
        name of root dir
    :type set_name: const char \*

.. _`iscsi_boot_create_host_kset`:

iscsi_boot_create_host_kset
===========================

.. c:function:: struct iscsi_boot_kset *iscsi_boot_create_host_kset(unsigned int hostno)

    creates root sysfs tree for a scsi host

    :param hostno:
        host number of scsi host
    :type hostno: unsigned int

.. _`iscsi_boot_destroy_kset`:

iscsi_boot_destroy_kset
=======================

.. c:function:: void iscsi_boot_destroy_kset(struct iscsi_boot_kset *boot_kset)

    destroy kset and kobjects under it

    :param boot_kset:
        boot kset
    :type boot_kset: struct iscsi_boot_kset \*

.. _`iscsi_boot_destroy_kset.description`:

Description
-----------

This will remove the kset and kobjects and attrs under it.

.. This file was automatic generated / don't edit.


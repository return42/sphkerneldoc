.. -*- coding: utf-8; mode: rst -*-

============
scsi_sysfs.c
============

.. _`scsi_sysfs_add_sdev`:

scsi_sysfs_add_sdev
===================

.. c:function:: int scsi_sysfs_add_sdev (struct scsi_device *sdev)

    add scsi device to sysfs

    :param struct scsi_device \*sdev:
        scsi_device to add


.. _`scsi_sysfs_add_sdev.description`:

Description
-----------

Return value::

        0 on Success / non-zero on Failure


.. _`scsi_remove_device`:

scsi_remove_device
==================

.. c:function:: void scsi_remove_device (struct scsi_device *sdev)

    unregister a device from the scsi bus

    :param struct scsi_device \*sdev:
        scsi_device to unregister


.. _`scsi_remove_target`:

scsi_remove_target
==================

.. c:function:: void scsi_remove_target (struct device *dev)

    try to remove a target and all its devices

    :param struct device \*dev:
        generic starget or parent of generic stargets to be removed


.. _`scsi_remove_target.description`:

Description
-----------

Note: This is slightly racy.  It is possible that if the user
requests the addition of another device then the target won't be
removed.


.. _`scsi_sysfs_add_host`:

scsi_sysfs_add_host
===================

.. c:function:: int scsi_sysfs_add_host (struct Scsi_Host *shost)

    add scsi host to subsystem

    :param struct Scsi_Host \*shost:
        scsi host struct to add to subsystem


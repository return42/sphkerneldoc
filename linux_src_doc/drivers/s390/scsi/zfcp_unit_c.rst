.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/scsi/zfcp_unit.c

.. _`zfcp_unit_scsi_scan`:

zfcp_unit_scsi_scan
===================

.. c:function:: void zfcp_unit_scsi_scan(struct zfcp_unit *unit)

    Register LUN with SCSI midlayer

    :param unit:
        The zfcp LUN/unit to register
    :type unit: struct zfcp_unit \*

.. _`zfcp_unit_scsi_scan.description`:

Description
-----------

When the SCSI midlayer is not allowed to automatically scan and
attach SCSI devices, zfcp has to register the single devices with
the SCSI midlayer.

.. _`zfcp_unit_queue_scsi_scan`:

zfcp_unit_queue_scsi_scan
=========================

.. c:function:: void zfcp_unit_queue_scsi_scan(struct zfcp_port *port)

    Register configured units on port

    :param port:
        The zfcp_port where to register units
    :type port: struct zfcp_port \*

.. _`zfcp_unit_queue_scsi_scan.description`:

Description
-----------

After opening a port, all units configured on this port have to be
registered with the SCSI midlayer. This function should be called
after calling fc_remote_port_add, so that the fc_rport is already
ONLINE and the call to scsi_scan_target runs the same way as the
call in the FC transport class.

.. _`zfcp_unit_find`:

zfcp_unit_find
==============

.. c:function:: struct zfcp_unit *zfcp_unit_find(struct zfcp_port *port, u64 fcp_lun)

    Find and return zfcp_unit with specified FCP LUN

    :param port:
        zfcp_port where to look for the unit
    :type port: struct zfcp_port \*

    :param fcp_lun:
        64 Bit FCP LUN used to identify the zfcp_unit
    :type fcp_lun: u64

.. _`zfcp_unit_find.description`:

Description
-----------

If zfcp_unit is found, a reference is acquired that has to be
released later.

.. _`zfcp_unit_find.return`:

Return
------

Pointer to the zfcp_unit, or NULL if there is no zfcp_unit
with the specified FCP LUN.

.. _`zfcp_unit_release`:

zfcp_unit_release
=================

.. c:function:: void zfcp_unit_release(struct device *dev)

    Drop reference to zfcp_port and free memory of zfcp_unit.

    :param dev:
        pointer to device in zfcp_unit
    :type dev: struct device \*

.. _`zfcp_unit_add`:

zfcp_unit_add
=============

.. c:function:: int zfcp_unit_add(struct zfcp_port *port, u64 fcp_lun)

    enqueue unit to unit list of a port.

    :param port:
        pointer to port where unit is added
    :type port: struct zfcp_port \*

    :param fcp_lun:
        FCP LUN of unit to be enqueued
    :type fcp_lun: u64

.. _`zfcp_unit_add.return`:

Return
------

0 success

Sets up some unit internal structures and creates sysfs entry.

.. _`zfcp_unit_sdev`:

zfcp_unit_sdev
==============

.. c:function:: struct scsi_device *zfcp_unit_sdev(struct zfcp_unit *unit)

    Return SCSI device for zfcp_unit

    :param unit:
        The zfcp_unit where to get the SCSI device for
    :type unit: struct zfcp_unit \*

.. _`zfcp_unit_sdev.return`:

Return
------

scsi_device pointer on success, NULL if there is no SCSI
device for this zfcp_unit

On success, the caller also holds a reference to the SCSI device
that must be released with scsi_device_put.

.. _`zfcp_unit_sdev_status`:

zfcp_unit_sdev_status
=====================

.. c:function:: unsigned int zfcp_unit_sdev_status(struct zfcp_unit *unit)

    Return zfcp LUN status for SCSI device

    :param unit:
        The unit to lookup the SCSI device for
    :type unit: struct zfcp_unit \*

.. _`zfcp_unit_sdev_status.description`:

Description
-----------

Returns the zfcp LUN status field of the SCSI device if the SCSI device
for the zfcp_unit exists, 0 otherwise.

.. _`zfcp_unit_remove`:

zfcp_unit_remove
================

.. c:function:: int zfcp_unit_remove(struct zfcp_port *port, u64 fcp_lun)

    Remove entry from list of configured units

    :param port:
        The port where to remove the unit from the configuration
    :type port: struct zfcp_port \*

    :param fcp_lun:
        The 64 bit LUN of the unit to remove
    :type fcp_lun: u64

.. _`zfcp_unit_remove.return`:

Return
------

-EINVAL if a unit with the specified LUN does not exist,
0 on success.

.. This file was automatic generated / don't edit.


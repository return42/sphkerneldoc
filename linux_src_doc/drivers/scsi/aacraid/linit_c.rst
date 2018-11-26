.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/aacraid/linit.c

.. _`aac_queuecommand`:

aac_queuecommand
================

.. c:function:: int aac_queuecommand(struct Scsi_Host *shost, struct scsi_cmnd *cmd)

    queue a SCSI command

    :param shost:
        *undescribed*
    :type shost: struct Scsi_Host \*

    :param cmd:
        SCSI command to queue
    :type cmd: struct scsi_cmnd \*

.. _`aac_queuecommand.description`:

Description
-----------

Queues a command for execution by the associated Host Adapter.

.. _`aac_queuecommand.todo`:

TODO
----

unify with \ :c:func:`aac_scsi_cmd`\ .

.. _`aac_info`:

aac_info
========

.. c:function:: const char *aac_info(struct Scsi_Host *shost)

    Returns the host adapter name

    :param shost:
        Scsi host to report on
    :type shost: struct Scsi_Host \*

.. _`aac_info.description`:

Description
-----------

Returns a static string describing the device in question

.. _`aac_get_driver_ident`:

aac_get_driver_ident
====================

.. c:function:: struct aac_driver_ident* aac_get_driver_ident(int devtype)

    :param devtype:
        index into lookup table
    :type devtype: int

.. _`aac_get_driver_ident.description`:

Description
-----------

Returns a pointer to the entry in the driver lookup table.

.. _`aac_biosparm`:

aac_biosparm
============

.. c:function:: int aac_biosparm(struct scsi_device *sdev, struct block_device *bdev, sector_t capacity, int *geom)

    return BIOS parameters for disk

    :param sdev:
        The scsi device corresponding to the disk
    :type sdev: struct scsi_device \*

    :param bdev:
        the block device corresponding to the disk
    :type bdev: struct block_device \*

    :param capacity:
        the sector capacity of the disk
    :type capacity: sector_t

    :param geom:
        geometry block to fill in
    :type geom: int \*

.. _`aac_biosparm.description`:

Description
-----------

Return the Heads/Sectors/Cylinders BIOS Disk Parameters for Disk.
The default disk geometry is 64 heads, 32 sectors, and the appropriate
number of cylinders so as not to exceed drive capacity.  In order for
disks equal to or larger than 1 GB to be addressable by the BIOS
without exceeding the BIOS limitation of 1024 cylinders, Extended
Translation should be enabled.   With Extended Translation enabled,
drives between 1 GB inclusive and 2 GB exclusive are given a disk
geometry of 128 heads and 32 sectors, and drives above 2 GB inclusive
are given a disk geometry of 255 heads and 63 sectors.  However, if
the BIOS detects that the Extended Translation setting does not match
the geometry in the partition table, then the translation inferred
from the partition table will be used by the BIOS, and a warning may
be displayed.

.. _`aac_slave_configure`:

aac_slave_configure
===================

.. c:function:: int aac_slave_configure(struct scsi_device *sdev)

    compute queue depths

    :param sdev:
        SCSI device we are considering
    :type sdev: struct scsi_device \*

.. _`aac_slave_configure.description`:

Description
-----------

Selects queue depths for each target device based on the host adapter's
total capacity and the queue depth supported by the target device.
A queue depth of one automatically disables tagged queueing.

.. _`aac_change_queue_depth`:

aac_change_queue_depth
======================

.. c:function:: int aac_change_queue_depth(struct scsi_device *sdev, int depth)

    alter queue depths

    :param sdev:
        SCSI device we are considering
    :type sdev: struct scsi_device \*

    :param depth:
        desired queue depth
    :type depth: int

.. _`aac_change_queue_depth.description`:

Description
-----------

Alters queue depths for target device based on the host adapter's
total capacity and the queue depth supported by the target device.

.. _`aac_cfg_open`:

aac_cfg_open
============

.. c:function:: int aac_cfg_open(struct inode *inode, struct file *file)

    open a configuration file

    :param inode:
        inode being opened
    :type inode: struct inode \*

    :param file:
        file handle attached
    :type file: struct file \*

.. _`aac_cfg_open.description`:

Description
-----------

Called when the configuration device is opened. Does the needed
set up on the handle and then returns

.. _`aac_cfg_open.bugs`:

Bugs
----

This needs extending to check a given adapter is present
so we can support hot plugging, and to ref count adapters.

.. _`aac_cfg_ioctl`:

aac_cfg_ioctl
=============

.. c:function:: long aac_cfg_ioctl(struct file *file, unsigned int cmd, unsigned long arg)

    AAC configuration request

    :param file:
        file handle
    :type file: struct file \*

    :param cmd:
        ioctl command code
    :type cmd: unsigned int

    :param arg:
        argument
    :type arg: unsigned long

.. _`aac_cfg_ioctl.description`:

Description
-----------

Handles a configuration ioctl. Currently this involves wrapping it
up and feeding it into the nasty windowsalike glue layer.

.. _`aac_cfg_ioctl.bugs`:

Bugs
----

Needs locking against parallel ioctls lower down

Needs to handle hot plugging

.. This file was automatic generated / don't edit.


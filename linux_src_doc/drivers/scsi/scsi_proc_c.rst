.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/scsi_proc.c

.. _`scsi_proc_hostdir_add`:

scsi_proc_hostdir_add
=====================

.. c:function:: void scsi_proc_hostdir_add(struct scsi_host_template *sht)

    Create directory in /proc for a scsi host

    :param sht:
        owner of this directory
    :type sht: struct scsi_host_template \*

.. _`scsi_proc_hostdir_add.description`:

Description
-----------

Sets sht->proc_dir to the new directory.

.. _`scsi_proc_hostdir_rm`:

scsi_proc_hostdir_rm
====================

.. c:function:: void scsi_proc_hostdir_rm(struct scsi_host_template *sht)

    remove directory in /proc for a scsi host

    :param sht:
        owner of directory
    :type sht: struct scsi_host_template \*

.. _`scsi_proc_host_add`:

scsi_proc_host_add
==================

.. c:function:: void scsi_proc_host_add(struct Scsi_Host *shost)

    Add entry for this host to appropriate /proc dir

    :param shost:
        host to add
    :type shost: struct Scsi_Host \*

.. _`scsi_proc_host_rm`:

scsi_proc_host_rm
=================

.. c:function:: void scsi_proc_host_rm(struct Scsi_Host *shost)

    remove this host's entry from /proc

    :param shost:
        which host
    :type shost: struct Scsi_Host \*

.. _`proc_print_scsidevice`:

proc_print_scsidevice
=====================

.. c:function:: int proc_print_scsidevice(struct device *dev, void *data)

    return data about this host

    :param dev:
        A scsi device
    :type dev: struct device \*

    :param data:
        \ :c:type:`struct seq_file <seq_file>`\  to output to.
    :type data: void \*

.. _`proc_print_scsidevice.description`:

Description
-----------

prints Host, Channel, Id, Lun, Vendor, Model, Rev, Type,
and revision.

.. _`scsi_add_single_device`:

scsi_add_single_device
======================

.. c:function:: int scsi_add_single_device(uint host, uint channel, uint id, uint lun)

    Respond to user request to probe for/add device

    :param host:
        user-supplied decimal integer
    :type host: uint

    :param channel:
        user-supplied decimal integer
    :type channel: uint

    :param id:
        user-supplied decimal integer
    :type id: uint

    :param lun:
        user-supplied decimal integer
    :type lun: uint

.. _`scsi_add_single_device.description`:

Description
-----------

called by writing "scsi add-single-device" to /proc/scsi/scsi.

does \ :c:func:`scsi_host_lookup`\  and either \ :c:func:`user_scan`\  if that transport
type supports it, or else \ :c:func:`scsi_scan_host_selected`\ 

.. _`scsi_add_single_device.note`:

Note
----

this seems to be aimed exclusively at SCSI parallel busses.

.. _`scsi_remove_single_device`:

scsi_remove_single_device
=========================

.. c:function:: int scsi_remove_single_device(uint host, uint channel, uint id, uint lun)

    Respond to user request to remove a device

    :param host:
        user-supplied decimal integer
    :type host: uint

    :param channel:
        user-supplied decimal integer
    :type channel: uint

    :param id:
        user-supplied decimal integer
    :type id: uint

    :param lun:
        user-supplied decimal integer
    :type lun: uint

.. _`scsi_remove_single_device.description`:

Description
-----------

called by writing "scsi remove-single-device" to
/proc/scsi/scsi.  Does a \ :c:func:`scsi_device_lookup`\  and \ :c:func:`scsi_remove_device`\ 

.. _`proc_scsi_write`:

proc_scsi_write
===============

.. c:function:: ssize_t proc_scsi_write(struct file *file, const char __user *buf, size_t length, loff_t *ppos)

    handle writes to /proc/scsi/scsi

    :param file:
        not used
    :type file: struct file \*

    :param buf:
        buffer to write
    :type buf: const char __user \*

    :param length:
        length of buf, at most PAGE_SIZE
    :type length: size_t

    :param ppos:
        not used
    :type ppos: loff_t \*

.. _`proc_scsi_write.description`:

Description
-----------

this provides a legacy mechanism to add or remove devices by
Host, Channel, ID, and Lun.  To use,
"echo 'scsi add-single-device 0 1 2 3' > /proc/scsi/scsi" or
"echo 'scsi remove-single-device 0 1 2 3' > /proc/scsi/scsi" with
"0 1 2 3" replaced by the Host, Channel, Id, and Lun.

.. _`proc_scsi_write.note`:

Note
----

this seems to be aimed at parallel SCSI. Most modern busses (USB,
SATA, Firewire, Fibre Channel, etc) dynamically assign these values to
provide a unique identifier and nothing more.

.. _`proc_scsi_open`:

proc_scsi_open
==============

.. c:function:: int proc_scsi_open(struct inode *inode, struct file *file)

    glue function

    :param inode:
        not used
    :type inode: struct inode \*

    :param file:
        passed to \ :c:func:`single_open`\ 
    :type file: struct file \*

.. _`proc_scsi_open.description`:

Description
-----------

Associates proc_scsi_show with this file

.. _`scsi_init_procfs`:

scsi_init_procfs
================

.. c:function:: int scsi_init_procfs( void)

    create scsi and scsi/scsi in procfs

    :param void:
        no arguments
    :type void: 

.. _`scsi_exit_procfs`:

scsi_exit_procfs
================

.. c:function:: void scsi_exit_procfs( void)

    Remove scsi/scsi and scsi from procfs

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.


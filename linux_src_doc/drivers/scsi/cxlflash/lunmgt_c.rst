.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/cxlflash/lunmgt.c

.. _`create_local`:

create_local
============

.. c:function:: struct llun_info *create_local(struct scsi_device *sdev, u8 *wwid)

    allocate and initialize a local LUN information structure

    :param sdev:
        SCSI device associated with LUN.
    :type sdev: struct scsi_device \*

    :param wwid:
        World Wide Node Name for LUN.
    :type wwid: u8 \*

.. _`create_local.return`:

Return
------

Allocated local llun_info structure on success, NULL on failure

.. _`create_global`:

create_global
=============

.. c:function:: struct glun_info *create_global(struct scsi_device *sdev, u8 *wwid)

    allocate and initialize a global LUN information structure

    :param sdev:
        SCSI device associated with LUN.
    :type sdev: struct scsi_device \*

    :param wwid:
        World Wide Node Name for LUN.
    :type wwid: u8 \*

.. _`create_global.return`:

Return
------

Allocated global glun_info structure on success, NULL on failure

.. _`lookup_local`:

lookup_local
============

.. c:function:: struct llun_info *lookup_local(struct cxlflash_cfg *cfg, u8 *wwid)

    find a local LUN information structure by WWID

    :param cfg:
        Internal structure associated with the host.
    :type cfg: struct cxlflash_cfg \*

    :param wwid:
        WWID associated with LUN.
    :type wwid: u8 \*

.. _`lookup_local.return`:

Return
------

Found local lun_info structure on success, NULL on failure

.. _`lookup_global`:

lookup_global
=============

.. c:function:: struct glun_info *lookup_global(u8 *wwid)

    find a global LUN information structure by WWID

    :param wwid:
        WWID associated with LUN.
    :type wwid: u8 \*

.. _`lookup_global.return`:

Return
------

Found global lun_info structure on success, NULL on failure

.. _`find_and_create_lun`:

find_and_create_lun
===================

.. c:function:: struct llun_info *find_and_create_lun(struct scsi_device *sdev, u8 *wwid)

    find or create a local LUN information structure

    :param sdev:
        SCSI device associated with LUN.
    :type sdev: struct scsi_device \*

    :param wwid:
        WWID associated with LUN.
    :type wwid: u8 \*

.. _`find_and_create_lun.description`:

Description
-----------

The LUN is kept both in a local list (per adapter) and in a global list
(across all adapters). Certain attributes of the LUN are local to the
adapter (such as index, port selection mask, etc.).

The block allocation map is shared across all adapters (i.e. associated
wih the global list). Since different attributes are associated with
the per adapter and global entries, allocate two separate structures for each
LUN (one local, one global).

Keep a pointer back from the local to the global entry.

This routine assumes the caller holds the global mutex.

.. _`find_and_create_lun.return`:

Return
------

Found/Allocated local lun_info structure on success, NULL on failure

.. _`cxlflash_term_local_luns`:

cxlflash_term_local_luns
========================

.. c:function:: void cxlflash_term_local_luns(struct cxlflash_cfg *cfg)

    Delete all entries from local LUN list, free.

    :param cfg:
        Internal structure associated with the host.
    :type cfg: struct cxlflash_cfg \*

.. _`cxlflash_list_init`:

cxlflash_list_init
==================

.. c:function:: void cxlflash_list_init( void)

    initializes the global LUN list

    :param void:
        no arguments
    :type void: 

.. _`cxlflash_term_global_luns`:

cxlflash_term_global_luns
=========================

.. c:function:: void cxlflash_term_global_luns( void)

    frees resources associated with global LUN list

    :param void:
        no arguments
    :type void: 

.. _`cxlflash_manage_lun`:

cxlflash_manage_lun
===================

.. c:function:: int cxlflash_manage_lun(struct scsi_device *sdev, struct dk_cxlflash_manage_lun *manage)

    handles LUN management activities

    :param sdev:
        SCSI device associated with LUN.
    :type sdev: struct scsi_device \*

    :param manage:
        Manage ioctl data structure.
    :type manage: struct dk_cxlflash_manage_lun \*

.. _`cxlflash_manage_lun.description`:

Description
-----------

This routine is used to notify the driver about a LUN's WWID and associate
SCSI devices (sdev) with a global LUN instance. Additionally it serves to
change a LUN's operating mode: legacy or superpipe.

.. _`cxlflash_manage_lun.return`:

Return
------

0 on success, -errno on failure

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/ufs/ufs_bsg.c

.. _`ufs_bsg_remove`:

ufs_bsg_remove
==============

.. c:function:: void ufs_bsg_remove(struct ufs_hba *hba)

    detach and remove the added ufs-bsg node

    :param hba:
        *undescribed*
    :type hba: struct ufs_hba \*

.. _`ufs_bsg_remove.description`:

Description
-----------

Should be called when unloading the driver.

.. _`ufs_bsg_probe`:

ufs_bsg_probe
=============

.. c:function:: int ufs_bsg_probe(struct ufs_hba *hba)

    Add ufs bsg device node

    :param hba:
        per adapter object
    :type hba: struct ufs_hba \*

.. _`ufs_bsg_probe.description`:

Description
-----------

Called during initial loading of the driver, and before scsi_scan_host.

.. This file was automatic generated / don't edit.


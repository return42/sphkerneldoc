.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/qedf/qedf_debugfs.c

.. _`qedf_dbg_host_init`:

qedf_dbg_host_init
==================

.. c:function:: void qedf_dbg_host_init(struct qedf_dbg_ctx *qedf, const struct qedf_debugfs_ops *dops, const struct file_operations *fops)

    setup the debugfs file for the pf

    :param qedf:
        *undescribed*
    :type qedf: struct qedf_dbg_ctx \*

    :param dops:
        *undescribed*
    :type dops: const struct qedf_debugfs_ops \*

    :param fops:
        *undescribed*
    :type fops: const struct file_operations \*

.. _`qedf_dbg_host_exit`:

qedf_dbg_host_exit
==================

.. c:function:: void qedf_dbg_host_exit(struct qedf_dbg_ctx *qedf)

    clear out the pf's debugfs entries

    :param qedf:
        *undescribed*
    :type qedf: struct qedf_dbg_ctx \*

.. _`qedf_dbg_init`:

qedf_dbg_init
=============

.. c:function:: void qedf_dbg_init(char *drv_name)

    start up debugfs for the driver

    :param drv_name:
        *undescribed*
    :type drv_name: char \*

.. _`qedf_dbg_exit`:

qedf_dbg_exit
=============

.. c:function:: void qedf_dbg_exit( void)

    clean out the driver's debugfs entries

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.


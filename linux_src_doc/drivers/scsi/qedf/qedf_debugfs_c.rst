.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/qedf/qedf_debugfs.c

.. _`qedf_dbg_host_init`:

qedf_dbg_host_init
==================

.. c:function:: void qedf_dbg_host_init(struct qedf_dbg_ctx *qedf, const struct qedf_debugfs_ops *dops, const struct file_operations *fops)

    setup the debugfs file for the pf

    :param struct qedf_dbg_ctx \*qedf:
        *undescribed*

    :param const struct qedf_debugfs_ops \*dops:
        *undescribed*

    :param const struct file_operations \*fops:
        *undescribed*

.. _`qedf_dbg_host_exit`:

qedf_dbg_host_exit
==================

.. c:function:: void qedf_dbg_host_exit(struct qedf_dbg_ctx *qedf)

    clear out the pf's debugfs entries

    :param struct qedf_dbg_ctx \*qedf:
        *undescribed*

.. _`qedf_dbg_init`:

qedf_dbg_init
=============

.. c:function:: void qedf_dbg_init(char *drv_name)

    start up debugfs for the driver

    :param char \*drv_name:
        *undescribed*

.. _`qedf_dbg_exit`:

qedf_dbg_exit
=============

.. c:function:: void qedf_dbg_exit( void)

    clean out the driver's debugfs entries

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.


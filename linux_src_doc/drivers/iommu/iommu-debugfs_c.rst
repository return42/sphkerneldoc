.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iommu/iommu-debugfs.c

.. _`iommu_debugfs_setup`:

iommu_debugfs_setup
===================

.. c:function:: void iommu_debugfs_setup( void)

    create the top-level iommu directory in debugfs

    :param void:
        no arguments
    :type void: 

.. _`iommu_debugfs_setup.description`:

Description
-----------

Provide base enablement for using debugfs to expose internal data of an
IOMMU driver. When called, this function creates the
/sys/kernel/debug/iommu directory.

Emit a strong warning at boot time to indicate that this feature is
enabled.

This function is called from iommu_init; drivers may then call
\ :c:func:`iommu_debugfs_new_driver_dir`\  to instantiate a vendor-specific
directory to be used to expose internal data.

.. _`iommu_debugfs_new_driver_dir`:

iommu_debugfs_new_driver_dir
============================

.. c:function:: struct dentry *iommu_debugfs_new_driver_dir(const char *vendor)

    create a vendor directory under debugfs/iommu

    :param vendor:
        name of the vendor-specific subdirectory to create
    :type vendor: const char \*

.. _`iommu_debugfs_new_driver_dir.description`:

Description
-----------

This function is called by an IOMMU driver to create the top-level debugfs
directory for that driver.

.. _`iommu_debugfs_new_driver_dir.return`:

Return
------

upon success, a pointer to the dentry for the new directory.
NULL in case of failure.

.. This file was automatic generated / don't edit.


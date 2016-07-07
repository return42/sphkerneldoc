.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/rapidio/rio-sysfs.c

.. _`rio_create_sysfs_dev_files`:

rio_create_sysfs_dev_files
==========================

.. c:function:: int rio_create_sysfs_dev_files(struct rio_dev *rdev)

    create RIO specific sysfs files

    :param struct rio_dev \*rdev:
        device whose entries should be created

.. _`rio_create_sysfs_dev_files.description`:

Description
-----------

Create files when \ ``rdev``\  is added to sysfs.

.. _`rio_remove_sysfs_dev_files`:

rio_remove_sysfs_dev_files
==========================

.. c:function:: void rio_remove_sysfs_dev_files(struct rio_dev *rdev)

    cleanup RIO specific sysfs files

    :param struct rio_dev \*rdev:
        device whose entries we should free

.. _`rio_remove_sysfs_dev_files.description`:

Description
-----------

Cleanup when \ ``rdev``\  is removed from sysfs.

.. This file was automatic generated / don't edit.


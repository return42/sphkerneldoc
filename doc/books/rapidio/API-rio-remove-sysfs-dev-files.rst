
.. _API-rio-remove-sysfs-dev-files:

==========================
rio_remove_sysfs_dev_files
==========================

*man rio_remove_sysfs_dev_files(9)*

*4.6.0-rc1*

cleanup RIO specific sysfs files


Synopsis
========

.. c:function:: void rio_remove_sysfs_dev_files( struct rio_dev * rdev )

Arguments
=========

``rdev``
    device whose entries we should free


Description
===========

Cleanup when ``rdev`` is removed from sysfs.

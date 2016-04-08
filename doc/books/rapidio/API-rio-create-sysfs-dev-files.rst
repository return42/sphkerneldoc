
.. _API-rio-create-sysfs-dev-files:

==========================
rio_create_sysfs_dev_files
==========================

*man rio_create_sysfs_dev_files(9)*

*4.6.0-rc1*

create RIO specific sysfs files


Synopsis
========

.. c:function:: int rio_create_sysfs_dev_files( struct rio_dev * rdev )

Arguments
=========

``rdev``
    device whose entries should be created


Description
===========

Create files when ``rdev`` is added to sysfs.

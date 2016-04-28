.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-remove-sysfs-dev-files:

==========================
rio_remove_sysfs_dev_files
==========================

*man rio_remove_sysfs_dev_files(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-create-sysfs-dev-files:

==========================
rio_create_sysfs_dev_files
==========================

*man rio_create_sysfs_dev_files(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

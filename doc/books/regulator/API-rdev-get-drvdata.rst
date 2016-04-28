.. -*- coding: utf-8; mode: rst -*-

.. _API-rdev-get-drvdata:

================
rdev_get_drvdata
================

*man rdev_get_drvdata(9)*

*4.6.0-rc5*

get rdev regulator driver data


Synopsis
========

.. c:function:: void * rdev_get_drvdata( struct regulator_dev * rdev )

Arguments
=========

``rdev``
    regulator


Description
===========

Get rdev regulator driver private data. This call can be used in the
regulator driver context.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

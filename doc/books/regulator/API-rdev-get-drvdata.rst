
.. _API-rdev-get-drvdata:

================
rdev_get_drvdata
================

*man rdev_get_drvdata(9)*

*4.6.0-rc1*

get rdev regulator driver data


Synopsis
========

.. c:function:: void ⋆ rdev_get_drvdata( struct regulator_dev * rdev )

Arguments
=========

``rdev``
    regulator


Description
===========

Get rdev regulator driver private data. This call can be used in the regulator driver context.

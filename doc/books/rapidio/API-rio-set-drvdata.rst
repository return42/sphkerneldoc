
.. _API-rio-set-drvdata:

===============
rio_set_drvdata
===============

*man rio_set_drvdata(9)*

*4.6.0-rc1*

Set RIO driver specific data


Synopsis
========

.. c:function:: void rio_set_drvdata( struct rio_dev * rdev, void * data )

Arguments
=========

``rdev``
    RIO device

``data``
    Pointer to driver specific data


Description
===========

Set RIO driver specific data. device struct driver data pointer is set to the ``data`` argument.


.. _API-rio-get-drvdata:

===============
rio_get_drvdata
===============

*man rio_get_drvdata(9)*

*4.6.0-rc1*

Get RIO driver specific data


Synopsis
========

.. c:function:: void ⋆ rio_get_drvdata( struct rio_dev * rdev )

Arguments
=========

``rdev``
    RIO device


Description
===========

Get RIO driver specific data. Returns a pointer to the driver specific data.

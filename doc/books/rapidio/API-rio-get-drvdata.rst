.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-get-drvdata:

===============
rio_get_drvdata
===============

*man rio_get_drvdata(9)*

*4.6.0-rc5*

Get RIO driver specific data


Synopsis
========

.. c:function:: void * rio_get_drvdata( struct rio_dev * rdev )

Arguments
=========

``rdev``
    RIO device


Description
===========

Get RIO driver specific data. Returns a pointer to the driver specific
data.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

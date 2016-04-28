.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-set-drvdata:

===============
rio_set_drvdata
===============

*man rio_set_drvdata(9)*

*4.6.0-rc5*

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

Set RIO driver specific data. device struct driver data pointer is set
to the ``data`` argument.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

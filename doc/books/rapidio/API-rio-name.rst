.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-name:

========
rio_name
========

*man rio_name(9)*

*4.6.0-rc5*

Get the unique RIO device identifier


Synopsis
========

.. c:function:: const char * rio_name( struct rio_dev * rdev )

Arguments
=========

``rdev``
    RIO device


Description
===========

Get the unique RIO device identifier. Returns the device identifier
string.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

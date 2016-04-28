.. -*- coding: utf-8; mode: rst -*-

.. _API-disable-cmf:

===========
disable_cmf
===========

*man disable_cmf(9)*

*4.6.0-rc5*

switch off the channel measurement for a specific device


Synopsis
========

.. c:function:: int disable_cmf( struct ccw_device * cdev )

Arguments
=========

``cdev``
    The ccw device to be disabled


Description
===========

Returns ``0`` for success or a negative error value.


Context
=======

non-atomic


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

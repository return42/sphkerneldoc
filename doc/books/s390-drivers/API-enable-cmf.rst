.. -*- coding: utf-8; mode: rst -*-

.. _API-enable-cmf:

==========
enable_cmf
==========

*man enable_cmf(9)*

*4.6.0-rc5*

switch on the channel measurement for a specific device


Synopsis
========

.. c:function:: int enable_cmf( struct ccw_device * cdev )

Arguments
=========

``cdev``
    The ccw device to be enabled


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

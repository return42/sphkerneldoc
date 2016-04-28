.. -*- coding: utf-8; mode: rst -*-

.. _API-ccw-device-tm-intrg:

===================
ccw_device_tm_intrg
===================

*man ccw_device_tm_intrg(9)*

*4.6.0-rc5*

perform interrogate function


Synopsis
========

.. c:function:: int ccw_device_tm_intrg( struct ccw_device * cdev )

Arguments
=========

``cdev``
    ccw device on which to perform the interrogate function


Description
===========

Perform an interrogate function on the given ccw device. Return zero on
success, non-zero otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

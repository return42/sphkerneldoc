.. -*- coding: utf-8; mode: rst -*-

.. _API-ccw-device-is-pathgroup:

=======================
ccw_device_is_pathgroup
=======================

*man ccw_device_is_pathgroup(9)*

*4.6.0-rc5*

determine if paths to this device are grouped


Synopsis
========

.. c:function:: int ccw_device_is_pathgroup( struct ccw_device * cdev )

Arguments
=========

``cdev``
    ccw device


Description
===========

Return non-zero if there is a path group, zero otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

.. -*- coding: utf-8; mode: rst -*-

.. _API-ccw-device-get-schid:

====================
ccw_device_get_schid
====================

*man ccw_device_get_schid(9)*

*4.6.0-rc5*

obtain a subchannel id


Synopsis
========

.. c:function:: void ccw_device_get_schid( struct ccw_device * cdev, struct subchannel_id * schid )

Arguments
=========

``cdev``
    device to obtain the id for

``schid``
    where to fill in the values


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

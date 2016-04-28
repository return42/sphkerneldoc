.. -*- coding: utf-8; mode: rst -*-

.. _API-ccwgroup-probe-ccwdev:

=====================
ccwgroup_probe_ccwdev
=====================

*man ccwgroup_probe_ccwdev(9)*

*4.6.0-rc5*

probe function for slave devices


Synopsis
========

.. c:function:: int ccwgroup_probe_ccwdev( struct ccw_device * cdev )

Arguments
=========

``cdev``
    ccw device to be probed


Description
===========

This is a dummy probe function for ccw devices that are slave devices in
a ccw group device.


Returns
=======

always ``0``


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

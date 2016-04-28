.. -*- coding: utf-8; mode: rst -*-

.. _API-ccwgroup-driver-unregister:

==========================
ccwgroup_driver_unregister
==========================

*man ccwgroup_driver_unregister(9)*

*4.6.0-rc5*

deregister a ccw group driver


Synopsis
========

.. c:function:: void ccwgroup_driver_unregister( struct ccwgroup_driver * cdriver )

Arguments
=========

``cdriver``
    driver to be deregistered


Description
===========

This function is mainly a wrapper around ``driver_unregister``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

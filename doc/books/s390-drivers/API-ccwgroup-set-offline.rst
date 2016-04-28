.. -*- coding: utf-8; mode: rst -*-

.. _API-ccwgroup-set-offline:

====================
ccwgroup_set_offline
====================

*man ccwgroup_set_offline(9)*

*4.6.0-rc5*

disable a ccwgroup device


Synopsis
========

.. c:function:: int ccwgroup_set_offline( struct ccwgroup_device * gdev )

Arguments
=========

``gdev``
    target ccwgroup device


Description
===========

This function attempts to put the ccwgroup device into the offline
state.


Returns
=======

``0`` on success and a negative error value on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

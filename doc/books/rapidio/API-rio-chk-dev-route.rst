.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-chk-dev-route:

=================
rio_chk_dev_route
=================

*man rio_chk_dev_route(9)*

*4.6.0-rc5*

Validate route to the specified device.


Synopsis
========

.. c:function:: int rio_chk_dev_route( struct rio_dev * rdev, struct rio_dev ** nrdev, int * npnum )

Arguments
=========

``rdev``
    RIO device failed to respond

``nrdev``
    Last active device on the route to rdev

``npnum``
    nrdev's port number on the route to rdev


Description
===========

Follows a route to the specified RIO device to determine the last
available device (and corresponding RIO port) on the route.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------


.. _API-rio-chk-dev-route:

=================
rio_chk_dev_route
=================

*man rio_chk_dev_route(9)*

*4.6.0-rc1*

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

Follows a route to the specified RIO device to determine the last available device (and corresponding RIO port) on the route.

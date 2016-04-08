
.. _API-rio-is-switch:

=============
rio_is_switch
=============

*man rio_is_switch(9)*

*4.6.0-rc1*

Tests if a RIO device has switch capabilities


Synopsis
========

.. c:function:: int rio_is_switch( struct rio_dev * rdev )

Arguments
=========

``rdev``
    RIO device


Description
===========

Gets the RIO device Processing Element Features register contents and tests for switch capabilities. Returns 1 if the device is a switch or 0 if it is not a switch. The RIO device
struct is freed.

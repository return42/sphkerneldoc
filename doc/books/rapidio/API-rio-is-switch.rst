.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-is-switch:

=============
rio_is_switch
=============

*man rio_is_switch(9)*

*4.6.0-rc5*

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

Gets the RIO device Processing Element Features register contents and
tests for switch capabilities. Returns 1 if the device is a switch or 0
if it is not a switch. The RIO device struct is freed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

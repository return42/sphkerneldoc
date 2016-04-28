.. -*- coding: utf-8; mode: rst -*-

.. _API-parport-release:

===============
parport_release
===============

*man parport_release(9)*

*4.6.0-rc5*

give up access to a parallel port device


Synopsis
========

.. c:function:: void parport_release( struct pardevice * dev )

Arguments
=========

``dev``
    pointer to structure representing parallel port device


Description
===========

This function cannot fail, but it should not be called without the port
claimed. Similarly, if the port is already claimed you should not try
claiming it again.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

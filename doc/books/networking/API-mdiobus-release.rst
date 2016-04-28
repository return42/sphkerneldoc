.. -*- coding: utf-8; mode: rst -*-

.. _API-mdiobus-release:

===============
mdiobus_release
===============

*man mdiobus_release(9)*

*4.6.0-rc5*

mii_bus device release callback


Synopsis
========

.. c:function:: void mdiobus_release( struct device * d )

Arguments
=========

``d``
    the target struct device that contains the mii_bus


Description
===========

called when the last reference to an mii_bus is dropped, to free the
underlying memory.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

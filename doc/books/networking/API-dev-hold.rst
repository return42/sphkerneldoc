.. -*- coding: utf-8; mode: rst -*-

.. _API-dev-hold:

========
dev_hold
========

*man dev_hold(9)*

*4.6.0-rc5*

get reference to device


Synopsis
========

.. c:function:: void dev_hold( struct net_device * dev )

Arguments
=========

``dev``
    network device


Description
===========

Hold reference to device to keep it from being freed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

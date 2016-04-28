.. -*- coding: utf-8; mode: rst -*-

.. _API-dev-put:

=======
dev_put
=======

*man dev_put(9)*

*4.6.0-rc5*

release reference to device


Synopsis
========

.. c:function:: void dev_put( struct net_device * dev )

Arguments
=========

``dev``
    network device


Description
===========

Release reference to device to allow it to be freed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

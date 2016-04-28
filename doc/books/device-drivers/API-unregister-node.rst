.. -*- coding: utf-8; mode: rst -*-

.. _API-unregister-node:

===============
unregister_node
===============

*man unregister_node(9)*

*4.6.0-rc5*

unregister a node device


Synopsis
========

.. c:function:: void unregister_node( struct node * node )

Arguments
=========

``node``
    node going away


Description
===========

Unregisters a node device ``node``. All the devices on the node must be
unregistered before calling this function.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

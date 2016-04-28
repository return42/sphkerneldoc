.. -*- coding: utf-8; mode: rst -*-

.. _API-devres-add:

==========
devres_add
==========

*man devres_add(9)*

*4.6.0-rc5*

Register device resource


Synopsis
========

.. c:function:: void devres_add( struct device * dev, void * res )

Arguments
=========

``dev``
    Device to add resource to

``res``
    Resource to register


Description
===========

Register devres ``res`` to ``dev``. ``res`` should have been allocated
using ``devres_alloc``. On driver detach, the associated release
function will be invoked and devres will be freed automatically.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

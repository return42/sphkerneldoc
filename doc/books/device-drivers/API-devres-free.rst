.. -*- coding: utf-8; mode: rst -*-

.. _API-devres-free:

===========
devres_free
===========

*man devres_free(9)*

*4.6.0-rc5*

Free device resource data


Synopsis
========

.. c:function:: void devres_free( void * res )

Arguments
=========

``res``
    Pointer to devres data to free


Description
===========

Free devres created with ``devres_alloc``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

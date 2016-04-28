.. -*- coding: utf-8; mode: rst -*-

.. _API-devres-alloc-node:

=================
devres_alloc_node
=================

*man devres_alloc_node(9)*

*4.6.0-rc5*

Allocate device resource data


Synopsis
========

.. c:function:: void * devres_alloc_node( dr_release_t release, size_t size, gfp_t gfp, int nid )

Arguments
=========

``release``
    Release function devres will be associated with

``size``
    Allocation size

``gfp``
    Allocation flags

``nid``
    NUMA node


Description
===========

Allocate devres of ``size`` bytes. The allocated area is zeroed, then
associated with ``release``. The returned pointer can be passed to other
devres_*() functions.


RETURNS
=======

Pointer to allocated devres on success, NULL on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

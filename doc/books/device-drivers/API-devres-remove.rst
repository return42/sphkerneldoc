.. -*- coding: utf-8; mode: rst -*-

.. _API-devres-remove:

=============
devres_remove
=============

*man devres_remove(9)*

*4.6.0-rc5*

Find a device resource and remove it


Synopsis
========

.. c:function:: void * devres_remove( struct device * dev, dr_release_t release, dr_match_t match, void * match_data )

Arguments
=========

``dev``
    Device to find resource from

``release``
    Look for resources associated with this release function

``match``
    Match function (optional)

``match_data``
    Data for the match function


Description
===========

Find the latest devres of ``dev`` associated with ``release`` and for
which ``match`` returns 1. If ``match`` is NULL, it's considered to
match all. If found, the resource is removed atomically and returned.


RETURNS
=======

Pointer to removed devres on success, NULL if not found.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

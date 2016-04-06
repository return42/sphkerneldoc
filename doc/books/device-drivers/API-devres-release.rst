
.. _API-devres-release:

==============
devres_release
==============

*man devres_release(9)*

*4.6.0-rc1*

Find a device resource and destroy it, calling release


Synopsis
========

.. c:function:: int devres_release( struct device * dev, dr_release_t release, dr_match_t match, void * match_data )

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

Find the latest devres of ``dev`` associated with ``release`` and for which ``match`` returns 1. If ``match`` is NULL, it's considered to match all. If found, the resource is
removed atomically, the release function called and the resource freed.


RETURNS
=======

0 if devres is found and freed, -ENOENT if not found.

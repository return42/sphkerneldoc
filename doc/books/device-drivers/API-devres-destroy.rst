
.. _API-devres-destroy:

==============
devres_destroy
==============

*man devres_destroy(9)*

*4.6.0-rc1*

Find a device resource and destroy it


Synopsis
========

.. c:function:: int devres_destroy( struct device * dev, dr_release_t release, dr_match_t match, void * match_data )

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
removed atomically and freed.

Note that the release function for the resource will not be called, only the devres-allocated data will be freed. The caller becomes responsible for freeing any other data.


RETURNS
=======

0 if devres is found and freed, -ENOENT if not found.

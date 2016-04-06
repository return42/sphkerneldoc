
.. _API-devres-find:

===========
devres_find
===========

*man devres_find(9)*

*4.6.0-rc1*

Find device resource


Synopsis
========

.. c:function:: void ⋆ devres_find( struct device * dev, dr_release_t release, dr_match_t match, void * match_data )

Arguments
=========

``dev``
    Device to lookup resource from

``release``
    Look for resources associated with this release function

``match``
    Match function (optional)

``match_data``
    Data for the match function


Description
===========

Find the latest devres of ``dev`` which is associated with ``release`` and for which ``match`` returns 1. If ``match`` is NULL, it's considered to match all.


RETURNS
=======

Pointer to found devres, NULL if not found.

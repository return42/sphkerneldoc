
.. _API-devres-get:

==========
devres_get
==========

*man devres_get(9)*

*4.6.0-rc1*

Find devres, if non-existent, add one atomically


Synopsis
========

.. c:function:: void ⋆ devres_get( struct device * dev, void * new_res, dr_match_t match, void * match_data )

Arguments
=========

``dev``
    Device to lookup or add devres for

``new_res``
    Pointer to new initialized devres to add if not found

``match``
    Match function (optional)

``match_data``
    Data for the match function


Description
===========

Find the latest devres of ``dev`` which has the same release function as ``new_res`` and for which ``match`` return 1. If found, ``new_res`` is freed; otherwise, ``new_res`` is
added atomically.


RETURNS
=======

Pointer to found or added devres.

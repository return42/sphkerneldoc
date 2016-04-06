
.. _API-devres-for-each-res:

===================
devres_for_each_res
===================

*man devres_for_each_res(9)*

*4.6.0-rc1*

Resource iterator


Synopsis
========

.. c:function:: void devres_for_each_res( struct device * dev, dr_release_t release, dr_match_t match, void * match_data, void (*fn) struct device *, void *, void *, void * data )

Arguments
=========

``dev``
    Device to iterate resource from

``release``
    Look for resources associated with this release function

``match``
    Match function (optional)

``match_data``
    Data for the match function

``fn``
    Function to be called for each matched resource.

``data``
    Data for ``fn``, the 3rd parameter of ``fn``


Description
===========

Call ``fn`` for each devres of ``dev`` which is associated with ``release`` and for which ``match`` returns 1.


RETURNS
=======

void

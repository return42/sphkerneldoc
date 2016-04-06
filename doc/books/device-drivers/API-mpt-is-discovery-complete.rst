
.. _API-mpt-is-discovery-complete:

=========================
mpt_is_discovery_complete
=========================

*man mpt_is_discovery_complete(9)*

*4.6.0-rc1*

determine if discovery has completed


Synopsis
========

.. c:function:: int mpt_is_discovery_complete( MPT_ADAPTER * ioc )

Arguments
=========

``ioc``
    per adatper instance


Description
===========

Returns 1 when discovery completed, else zero.

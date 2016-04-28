.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-is-discovery-complete:

=========================
mpt_is_discovery_complete
=========================

*man mpt_is_discovery_complete(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

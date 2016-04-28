.. -*- coding: utf-8; mode: rst -*-

.. _API-napi-synchronize:

================
napi_synchronize
================

*man napi_synchronize(9)*

*4.6.0-rc5*

wait until NAPI is not running


Synopsis
========

.. c:function:: void napi_synchronize( const struct napi_struct * n )

Arguments
=========

``n``
    NAPI context


Description
===========

Wait until NAPI is done being scheduled on this context. Waits till any
outstanding processing completes but does not disable future
activations.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

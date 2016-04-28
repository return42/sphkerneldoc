.. -*- coding: utf-8; mode: rst -*-

.. _API-napi-enable:

===========
napi_enable
===========

*man napi_enable(9)*

*4.6.0-rc5*

enable NAPI scheduling


Synopsis
========

.. c:function:: void napi_enable( struct napi_struct * n )

Arguments
=========

``n``
    NAPI context


Description
===========

Resume NAPI from being scheduled on this context. Must be paired with
napi_disable.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

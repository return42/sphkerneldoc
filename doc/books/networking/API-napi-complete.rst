.. -*- coding: utf-8; mode: rst -*-

.. _API-napi-complete:

=============
napi_complete
=============

*man napi_complete(9)*

*4.6.0-rc5*

NAPI processing complete


Synopsis
========

.. c:function:: void napi_complete( struct napi_struct * n )

Arguments
=========

``n``
    NAPI context


Description
===========

Mark NAPI processing as complete. Consider using ``napi_complete_done``
instead.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

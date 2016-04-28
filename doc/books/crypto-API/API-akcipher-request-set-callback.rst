.. -*- coding: utf-8; mode: rst -*-

.. _API-akcipher-request-set-callback:

=============================
akcipher_request_set_callback
=============================

*man akcipher_request_set_callback(9)*

*4.6.0-rc5*

Sets an asynchronous callback.


Synopsis
========

.. c:function:: void akcipher_request_set_callback( struct akcipher_request * req, u32 flgs, crypto_completion_t cmpl, void * data )

Arguments
=========

``req``
    request that the callback will be set for

``flgs``
    specify for instance if the operation may backlog

``cmpl``
    callback which will be called

``data``
    private data used by the caller


Description
===========

Callback will be called when an asynchronous operation on a given
request is finished.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

.. -*- coding: utf-8; mode: rst -*-

.. _API-skcipher-request-set-tfm:

========================
skcipher_request_set_tfm
========================

*man skcipher_request_set_tfm(9)*

*4.6.0-rc5*

update cipher handle reference in request


Synopsis
========

.. c:function:: void skcipher_request_set_tfm( struct skcipher_request * req, struct crypto_skcipher * tfm )

Arguments
=========

``req``
    request handle to be modified

``tfm``
    cipher handle that shall be added to the request handle


Description
===========

Allow the caller to replace the existing skcipher handle in the request
data structure with a different one.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

.. -*- coding: utf-8; mode: rst -*-

.. _API-aead-request-set-ad:

===================
aead_request_set_ad
===================

*man aead_request_set_ad(9)*

*4.6.0-rc5*

set associated data information


Synopsis
========

.. c:function:: void aead_request_set_ad( struct aead_request * req, unsigned int assoclen )

Arguments
=========

``req``
    request handle

``assoclen``
    number of bytes in associated data


Description
===========

Setting the AD information. This function sets the length of the
associated data.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

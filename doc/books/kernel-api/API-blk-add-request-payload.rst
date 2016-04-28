.. -*- coding: utf-8; mode: rst -*-

.. _API-blk-add-request-payload:

=======================
blk_add_request_payload
=======================

*man blk_add_request_payload(9)*

*4.6.0-rc5*

add a payload to a request


Synopsis
========

.. c:function:: void blk_add_request_payload( struct request * rq, struct page * page, unsigned int len )

Arguments
=========

``rq``
    request to update

``page``
    page backing the payload

``len``
    length of the payload.


Description
===========

This allows to later add a payload to an already submitted request by a
block driver. The driver needs to take care of freeing the payload
itself.

Note that this is a quite horrible hack and nothing but handling of
discard requests should ever use it.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------


.. _API-blk-add-request-payload:

=======================
blk_add_request_payload
=======================

*man blk_add_request_payload(9)*

*4.6.0-rc1*

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

This allows to later add a payload to an already submitted request by a block driver. The driver needs to take care of freeing the payload itself.

Note that this is a quite horrible hack and nothing but handling of discard requests should ever use it.

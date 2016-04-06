
.. _API-blk-end-request-all:

===================
blk_end_request_all
===================

*man blk_end_request_all(9)*

*4.6.0-rc1*

Helper function for drives to finish the request.


Synopsis
========

.. c:function:: void blk_end_request_all( struct request * rq, int error )

Arguments
=========

``rq``
    the request to finish

``error``
    ``0`` for success, < ``0`` for error


Description
===========

Completely finish ``rq``.

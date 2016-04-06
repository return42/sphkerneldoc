
.. _API-blk-end-request:

===============
blk_end_request
===============

*man blk_end_request(9)*

*4.6.0-rc1*

Helper function for drivers to complete the request.


Synopsis
========

.. c:function:: bool blk_end_request( struct request * rq, int error, unsigned int nr_bytes )

Arguments
=========

``rq``
    the request being processed

``error``
    ``0`` for success, < ``0`` for error

``nr_bytes``
    number of bytes to complete


Description
===========

Ends I/O on a number of bytes attached to ``rq``. If ``rq`` has leftover, sets it up for the next range of segments.


Return
======

``false`` - we are done with this request ``true`` - still buffers pending for this request

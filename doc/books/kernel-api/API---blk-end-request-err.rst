
.. _API---blk-end-request-err:

=====================
__blk_end_request_err
=====================

*man __blk_end_request_err(9)*

*4.6.0-rc1*

Finish a request till the next failure boundary.


Synopsis
========

.. c:function:: bool __blk_end_request_err( struct request * rq, int error )

Arguments
=========

``rq``
    the request to finish till the next failure boundary for

``error``
    must be negative errno


Description
===========

Complete ``rq`` till the next failure boundary. Must be called with queue lock held.


Return
======

``false`` - we are done with this request ``true`` - still buffers pending for this request

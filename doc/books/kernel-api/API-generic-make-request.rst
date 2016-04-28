.. -*- coding: utf-8; mode: rst -*-

.. _API-generic-make-request:

====================
generic_make_request
====================

*man generic_make_request(9)*

*4.6.0-rc5*

hand a buffer to its device driver for I/O


Synopsis
========

.. c:function:: blk_qc_t generic_make_request( struct bio * bio )

Arguments
=========

``bio``
    The bio describing the location in memory and on the device.


Description
===========

``generic_make_request`` is used to make I/O requests of block devices.
It is passed a ``struct bio``, which describes the I/O that needs to be
done.

``generic_make_request`` does not return any status. The success/failure
status of the request, along with notification of completion, is
delivered asynchronously through the bio->bi_end_io function described
(one day) else where.

The caller of generic_make_request must make sure that bi_io_vec are
set to describe the memory buffer, and that bi_dev and bi_sector are
set to describe the device address, and the bi_end_io and optionally
bi_private are set to describe how completion notification should be
signaled.

generic_make_request and the drivers it calls may use bi_next if this
bio happens to be merged with someone else, and may resubmit the bio to
a lower device by calling into generic_make_request recursively, which
means the bio should NOT be touched after the call to
->make_request_fn.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

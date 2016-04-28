.. -*- coding: utf-8; mode: rst -*-

.. _API-submit-bio-wait:

===============
submit_bio_wait
===============

*man submit_bio_wait(9)*

*4.6.0-rc5*

submit a bio, and wait until it completes


Synopsis
========

.. c:function:: int submit_bio_wait( int rw, struct bio * bio )

Arguments
=========

``rw``
    whether to ``READ`` or ``WRITE``, or maybe to ``READA`` (read ahead)

``bio``
    The ``struct bio`` which describes the I/O


Description
===========

Simple wrapper around ``submit_bio``. Returns 0 on success, or the error
from ``bio_endio`` on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------


.. _API-submit-bio:

==========
submit_bio
==========

*man submit_bio(9)*

*4.6.0-rc1*

submit a bio to the block device layer for I/O


Synopsis
========

.. c:function:: blk_qc_t submit_bio( int rw, struct bio * bio )

Arguments
=========

``rw``
    whether to ``READ`` or ``WRITE``, or maybe to ``READA`` (read ahead)

``bio``
    The ``struct bio`` which describes the I/O


Description
===========

``submit_bio`` is very similar in purpose to ``generic_make_request``, and uses that function to do most of the work. Both are fairly rough interfaces; ``bio`` must be presetup and
ready for I/O.


.. _API-bio-chain:

=========
bio_chain
=========

*man bio_chain(9)*

*4.6.0-rc1*

chain bio completions


Synopsis
========

.. c:function:: void bio_chain( struct bio * bio, struct bio * parent )

Arguments
=========

``bio``
    the target bio

``parent``
    the ``bio``'s parent bio


Description
===========

The caller won't have a bi_end_io called when ``bio`` completes - instead, ``parent``'s bi_end_io won't be called until both ``parent`` and ``bio`` have completed; the chained
bio will also be freed when it completes.

The caller must not set bi_private or bi_end_io in ``bio``.

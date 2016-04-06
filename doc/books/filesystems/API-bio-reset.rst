
.. _API-bio-reset:

=========
bio_reset
=========

*man bio_reset(9)*

*4.6.0-rc1*

reinitialize a bio


Synopsis
========

.. c:function:: void bio_reset( struct bio * bio )

Arguments
=========

``bio``
    bio to reset


Description
===========

After calling ``bio_reset``, ``bio`` will be in the same state as a freshly allocated bio returned bio ``bio_alloc_bioset`` - the only fields that are preserved are the ones that
are initialized by ``bio_alloc_bioset``. See comment in struct bio.

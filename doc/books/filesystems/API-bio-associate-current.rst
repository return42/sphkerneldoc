
.. _API-bio-associate-current:

=====================
bio_associate_current
=====================

*man bio_associate_current(9)*

*4.6.0-rc1*

associate a bio with ``current``


Synopsis
========

.. c:function:: int bio_associate_current( struct bio * bio )

Arguments
=========

``bio``
    target bio


Description
===========

Associate ``bio`` with ``current`` if it hasn't been associated yet. Block layer will treat ``bio`` as if it were issued by ``current`` no matter which task actually issues it.

This function takes an extra reference of ``task``'s io_context and blkcg which will be put when ``bio`` is released. The caller must own ``bio``, ensure ``current-``>io_context
exists, and is responsible for synchronizing calls to this function.

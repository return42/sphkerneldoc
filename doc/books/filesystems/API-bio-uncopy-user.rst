
.. _API-bio-uncopy-user:

===============
bio_uncopy_user
===============

*man bio_uncopy_user(9)*

*4.6.0-rc1*

finish previously mapped bio


Synopsis
========

.. c:function:: int bio_uncopy_user( struct bio * bio )

Arguments
=========

``bio``
    bio being terminated


Description
===========

Free pages allocated from ``bio_copy_user_iov`` and write back data to user space in case of a read.

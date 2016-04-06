
.. _API-bio-trim:

========
bio_trim
========

*man bio_trim(9)*

*4.6.0-rc1*

trim a bio


Synopsis
========

.. c:function:: void bio_trim( struct bio * bio, int offset, int size )

Arguments
=========

``bio``
    bio to trim

``offset``
    number of sectors to trim from the front of ``bio``

``size``
    size we want to trim ``bio`` to, in sectors

.. -*- coding: utf-8; mode: rst -*-

.. _API-bio-trim:

========
bio_trim
========

*man bio_trim(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

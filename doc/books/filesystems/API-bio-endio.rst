.. -*- coding: utf-8; mode: rst -*-

.. _API-bio-endio:

=========
bio_endio
=========

*man bio_endio(9)*

*4.6.0-rc5*

end I/O on a bio


Synopsis
========

.. c:function:: void bio_endio( struct bio * bio )

Arguments
=========

``bio``
    bio


Description
===========

``bio_endio`` will end I/O on the whole bio. ``bio_endio`` is the
preferred way to end I/O on a bio. No one should call ``bi_end_io``
directly on a bio unless they own it and thus know that it has an
end_io function.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

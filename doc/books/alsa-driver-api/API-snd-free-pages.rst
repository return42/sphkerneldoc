.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-free-pages:

==============
snd_free_pages
==============

*man snd_free_pages(9)*

*4.6.0-rc5*

release the pages


Synopsis
========

.. c:function:: void snd_free_pages( void * ptr, size_t size )

Arguments
=========

``ptr``
    the buffer pointer to release

``size``
    the allocated buffer size


Description
===========

Releases the buffer allocated via ``snd_malloc_pages``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------


.. _API-snd-free-pages:

==============
snd_free_pages
==============

*man snd_free_pages(9)*

*4.6.0-rc1*

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


.. _API-vunmap:

======
vunmap
======

*man vunmap(9)*

*4.6.0-rc1*

release virtual mapping obtained by ``vmap``


Synopsis
========

.. c:function:: void vunmap( const void * addr )

Arguments
=========

``addr``
    memory base address


Description
===========

Free the virtually contiguous memory area starting at ``addr``, which was created from the page array passed to ``vmap``.

Must not be called in interrupt context.


.. _API-kstrdup:

=======
kstrdup
=======

*man kstrdup(9)*

*4.6.0-rc1*

allocate space for and copy an existing string


Synopsis
========

.. c:function:: char ⋆ kstrdup( const char * s, gfp_t gfp )

Arguments
=========

``s``
    the string to duplicate

``gfp``
    the GFP mask used in the ``kmalloc`` call when allocating memory

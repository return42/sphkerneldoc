
.. _API-kstrndup:

========
kstrndup
========

*man kstrndup(9)*

*4.6.0-rc1*

allocate space for and copy an existing string


Synopsis
========

.. c:function:: char ⋆ kstrndup( const char * s, size_t max, gfp_t gfp )

Arguments
=========

``s``
    the string to duplicate

``max``
    read at most ``max`` chars from ``s``

``gfp``
    the GFP mask used in the ``kmalloc`` call when allocating memory

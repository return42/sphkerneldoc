
.. _API-kstrdup-const:

=============
kstrdup_const
=============

*man kstrdup_const(9)*

*4.6.0-rc1*

conditionally duplicate an existing const string


Synopsis
========

.. c:function:: const char ⋆ kstrdup_const( const char * s, gfp_t gfp )

Arguments
=========

``s``
    the string to duplicate

``gfp``
    the GFP mask used in the ``kmalloc`` call when allocating memory


Description
===========

Function returns source string if it is in .rodata section otherwise it fallbacks to kstrdup. Strings allocated by kstrdup_const should be freed by kfree_const.

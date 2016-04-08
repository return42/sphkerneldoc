
.. _API-priv-to-wiphy:

=============
priv_to_wiphy
=============

*man priv_to_wiphy(9)*

*4.6.0-rc1*

return the wiphy containing the priv


Synopsis
========

.. c:function:: struct wiphy ⋆ priv_to_wiphy( void * priv )

Arguments
=========

``priv``
    a pointer previously returned by wiphy_priv


Return
======

The wiphy of ``priv``.

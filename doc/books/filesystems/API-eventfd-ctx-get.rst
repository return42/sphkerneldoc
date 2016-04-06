
.. _API-eventfd-ctx-get:

===============
eventfd_ctx_get
===============

*man eventfd_ctx_get(9)*

*4.6.0-rc1*

Acquires a reference to the internal eventfd context.


Synopsis
========

.. c:function:: struct eventfd_ctx ⋆ eventfd_ctx_get( struct eventfd_ctx * ctx )

Arguments
=========

``ctx``
    [in] Pointer to the eventfd context.


Returns
=======

In case of success, returns a pointer to the eventfd context.

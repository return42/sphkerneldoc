
.. _API-pnp-add-id:

==========
pnp_add_id
==========

*man pnp_add_id(9)*

*4.6.0-rc1*

adds an EISA id to the specified device


Synopsis
========

.. c:function:: struct pnp_id ⋆ pnp_add_id( struct pnp_dev * dev, const char * id )

Arguments
=========

``dev``
    pointer to the desired device

``id``
    pointer to an EISA id string

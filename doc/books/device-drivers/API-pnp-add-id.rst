.. -*- coding: utf-8; mode: rst -*-

.. _API-pnp-add-id:

==========
pnp_add_id
==========

*man pnp_add_id(9)*

*4.6.0-rc5*

adds an EISA id to the specified device


Synopsis
========

.. c:function:: struct pnp_id * pnp_add_id( struct pnp_dev * dev, const char * id )

Arguments
=========

``dev``
    pointer to the desired device

``id``
    pointer to an EISA id string


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

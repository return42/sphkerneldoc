.. -*- coding: utf-8; mode: rst -*-

.. _API-pnp-register-protocol:

=====================
pnp_register_protocol
=====================

*man pnp_register_protocol(9)*

*4.6.0-rc5*

adds a pnp protocol to the pnp layer


Synopsis
========

.. c:function:: int pnp_register_protocol( struct pnp_protocol * protocol )

Arguments
=========

``protocol``
    pointer to the corresponding pnp_protocol structure


Ex protocols
============

ISAPNP, PNPBIOS, etc


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

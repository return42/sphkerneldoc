
.. _API-pnp-register-protocol:

=====================
pnp_register_protocol
=====================

*man pnp_register_protocol(9)*

*4.6.0-rc1*

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

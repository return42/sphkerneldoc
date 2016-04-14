.. -*- coding: utf-8; mode: rst -*-

======
core.c
======

.. _`pnp_register_protocol`:

pnp_register_protocol
=====================

.. c:function:: int pnp_register_protocol (struct pnp_protocol *protocol)

    adds a pnp protocol to the pnp layer

    :param struct pnp_protocol \*protocol:
        pointer to the corresponding pnp_protocol structure


.. _`pnp_register_protocol.description`:

Description
-----------

Ex protocols: ISAPNP, PNPBIOS, etc


.. _`pnp_unregister_protocol`:

pnp_unregister_protocol
=======================

.. c:function:: void pnp_unregister_protocol (struct pnp_protocol *protocol)

    removes a pnp protocol from the pnp layer

    :param struct pnp_protocol \*protocol:
        pointer to the corresponding pnp_protocol structure


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pnp/core.c

.. _`pnp_register_protocol`:

pnp_register_protocol
=====================

.. c:function:: int pnp_register_protocol(struct pnp_protocol *protocol)

    adds a pnp protocol to the pnp layer

    :param protocol:
        pointer to the corresponding pnp_protocol structure
    :type protocol: struct pnp_protocol \*

.. _`pnp_register_protocol.description`:

Description
-----------

 Ex protocols: ISAPNP, PNPBIOS, etc

.. _`pnp_unregister_protocol`:

pnp_unregister_protocol
=======================

.. c:function:: void pnp_unregister_protocol(struct pnp_protocol *protocol)

    removes a pnp protocol from the pnp layer

    :param protocol:
        pointer to the corresponding pnp_protocol structure
    :type protocol: struct pnp_protocol \*

.. This file was automatic generated / don't edit.


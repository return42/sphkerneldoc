.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fsl-mc/bus/dpmcp.h

.. _`dpmcp_cfg`:

struct dpmcp_cfg
================

.. c:type:: struct dpmcp_cfg

    Structure representing DPMCP configuration

.. _`dpmcp_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpmcp_cfg {
        int portal_id;
    }

.. _`dpmcp_cfg.members`:

Members
-------

portal_id
    Portal ID; 'DPMCP_GET_PORTAL_ID_FROM_POOL' to get the portal ID
    from pool

.. _`dpmcp_irq_cfg`:

struct dpmcp_irq_cfg
====================

.. c:type:: struct dpmcp_irq_cfg

    IRQ configuration

.. _`dpmcp_irq_cfg.definition`:

Definition
----------

.. code-block:: c

    struct dpmcp_irq_cfg {
        u64 paddr;
        u32 val;
        int irq_num;
    }

.. _`dpmcp_irq_cfg.members`:

Members
-------

paddr
    Address that must be written to signal a message-based interrupt

val
    Value to write into irq_addr address

irq_num
    A user defined number associated with this IRQ

.. _`dpmcp_attr`:

struct dpmcp_attr
=================

.. c:type:: struct dpmcp_attr

    Structure representing DPMCP attributes

.. _`dpmcp_attr.definition`:

Definition
----------

.. code-block:: c

    struct dpmcp_attr {
        int id;
    }

.. _`dpmcp_attr.members`:

Members
-------

id
    DPMCP object ID

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/smc/smc_pnet.c

.. _`smc_pnetentry`:

struct smc_pnetentry
====================

.. c:type:: struct smc_pnetentry

    pnet identifier name entry

.. _`smc_pnetentry.definition`:

Definition
----------

.. code-block:: c

    struct smc_pnetentry {
        struct list_head list;
        char pnet_name;
        struct net_device *ndev;
        struct smc_ib_device *smcibdev;
        u8 ib_port;
    }

.. _`smc_pnetentry.members`:

Members
-------

list
    List node.

pnet_name
    Pnet identifier name

ndev
    pointer to network device.

smcibdev
    Pointer to IB device.

ib_port
    *undescribed*

.. This file was automatic generated / don't edit.


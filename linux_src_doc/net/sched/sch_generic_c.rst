.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/sched/sch_generic.c

.. _`netif_carrier_on`:

netif_carrier_on
================

.. c:function:: void netif_carrier_on(struct net_device *dev)

    set carrier

    :param struct net_device \*dev:
        network device

.. _`netif_carrier_on.description`:

Description
-----------

Device has detected that carrier.

.. _`netif_carrier_off`:

netif_carrier_off
=================

.. c:function:: void netif_carrier_off(struct net_device *dev)

    clear carrier

    :param struct net_device \*dev:
        network device

.. _`netif_carrier_off.description`:

Description
-----------

Device has detected loss of carrier.

.. _`dev_deactivate_many`:

dev_deactivate_many
===================

.. c:function:: void dev_deactivate_many(struct list_head *head)

    deactivate transmissions on several devices

    :param struct list_head \*head:
        list of devices to deactivate

.. _`dev_deactivate_many.description`:

Description
-----------

     This function returns only when all outstanding transmissions
     have completed, unless all devices are in dismantle phase.

.. This file was automatic generated / don't edit.


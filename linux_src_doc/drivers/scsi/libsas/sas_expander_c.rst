.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/libsas/sas_expander.c

.. _`sas_ex_discover_devices`:

sas_ex_discover_devices
=======================

.. c:function:: int sas_ex_discover_devices(struct domain_device *dev, int single)

    discover devices attached to this expander

    :param struct domain_device \*dev:
        pointer to the expander domain device

    :param int single:
        if you want to do a single phy, else set to -1;

.. _`sas_ex_discover_devices.description`:

Description
-----------

Configure this expander for use with its devices and register the
devices of this expander.

.. _`sas_configure_parent`:

sas_configure_parent
====================

.. c:function:: int sas_configure_parent(struct domain_device *parent, struct domain_device *child, u8 *sas_addr, int include)

    configure routing table of parent

    :param struct domain_device \*parent:
        parent expander

    :param struct domain_device \*child:
        child expander

    :param u8 \*sas_addr:
        SAS port identifier of device directly attached to child

    :param int include:
        whether or not to include \ ``child``\  in the expander routing table

.. _`sas_configure_routing`:

sas_configure_routing
=====================

.. c:function:: int sas_configure_routing(struct domain_device *dev, u8 *sas_addr)

    configure routing

    :param struct domain_device \*dev:
        expander device

    :param u8 \*sas_addr:
        port identifier of device directly attached to the expander device

.. _`sas_discover_expander`:

sas_discover_expander
=====================

.. c:function:: int sas_discover_expander(struct domain_device *dev)

    expander discovery

    :param struct domain_device \*dev:
        pointer to expander domain device

.. _`sas_discover_expander.description`:

Description
-----------

See comment in \ :c:func:`sas_discover_sata`\ .

.. _`sas_find_bcast_dev`:

sas_find_bcast_dev
==================

.. c:function:: int sas_find_bcast_dev(struct domain_device *dev, struct domain_device **src_dev)

    find the device issue BROADCAST(CHANGE).

    :param struct domain_device \*dev:
        domain device to be detect.

    :param struct domain_device \*\*src_dev:
        the device which originated BROADCAST(CHANGE).

.. _`sas_find_bcast_dev.description`:

Description
-----------

Add self-configuration expander support. Suppose two expander cascading,
when the first level expander is self-configuring, hotplug the disks in
second level expander, BROADCAST(CHANGE) will not only be originated
in the second level expander, but also be originated in the first level
expander (see SAS protocol SAS 2r-14, 7.11 for detail), it is to say,
expander changed count in two level expanders will all increment at least
once, but the phy which chang count has changed is the source device which
we concerned.

.. _`sas_rediscover`:

sas_rediscover
==============

.. c:function:: int sas_rediscover(struct domain_device *dev, const int phy_id)

    revalidate the domain.

    :param struct domain_device \*dev:
        domain device to be detect.

    :param const int phy_id:
        the phy id will be detected.

.. _`sas_rediscover.note`:

NOTE
----

this process \_must\_ quit (return) as soon as any connection
errors are encountered.  Connection recovery is done elsewhere.
Discover process only interrogates devices in order to discover the
domain.For plugging out, we un-register the device only when it is
the last phy in the port, for other phys in this port, we just delete it
from the port.For inserting, we do discovery when it is the
first phy,for other phys in this port, we add it to the port to
forming the wide-port.

.. _`sas_ex_revalidate_domain`:

sas_ex_revalidate_domain
========================

.. c:function:: int sas_ex_revalidate_domain(struct domain_device *port_dev)

    revalidate the domain

    :param struct domain_device \*port_dev:
        port domain device.

.. _`sas_ex_revalidate_domain.note`:

NOTE
----

this process \_must\_ quit (return) as soon as any connection
errors are encountered.  Connection recovery is done elsewhere.
Discover process only interrogates devices in order to discover the
domain.

.. This file was automatic generated / don't edit.


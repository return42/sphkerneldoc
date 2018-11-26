.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/libsas/sas_discover.c

.. _`sas_get_port_device`:

sas_get_port_device
===================

.. c:function:: int sas_get_port_device(struct asd_sas_port *port)

    Discover devices which caused port creation

    :param port:
        pointer to struct sas_port of interest
    :type port: struct asd_sas_port \*

.. _`sas_get_port_device.description`:

Description
-----------

Devices directly attached to a HA port, have no parent.  This is
how we know they are (domain) "root" devices.  All other devices
do, and should have their "parent" pointer set appropriately as
soon as a child device is discovered.

.. _`sas_discover_end_dev`:

sas_discover_end_dev
====================

.. c:function:: int sas_discover_end_dev(struct domain_device *dev)

    discover an end device (SSP, etc)

    :param dev:
        pointer to domain device of interest
    :type dev: struct domain_device \*

.. _`sas_discover_end_dev.description`:

Description
-----------

See comment in \ :c:func:`sas_discover_sata`\ .

.. _`sas_discover_domain`:

sas_discover_domain
===================

.. c:function:: void sas_discover_domain(struct work_struct *work)

    discover the domain

    :param work:
        work structure embedded in port domain device.
    :type work: struct work_struct \*

.. _`sas_discover_domain.note`:

NOTE
----

this process \_must\_ quit (return) as soon as any connection
errors are encountered.  Connection recovery is done elsewhere.
Discover process only interrogates devices in order to discover the
domain.

.. _`sas_init_disc`:

sas_init_disc
=============

.. c:function:: void sas_init_disc(struct sas_discovery *disc, struct asd_sas_port *port)

    initialize the discovery struct in the port

    :param disc:
        port discovery structure
    :type disc: struct sas_discovery \*

    :param port:
        pointer to struct port
    :type port: struct asd_sas_port \*

.. _`sas_init_disc.description`:

Description
-----------

Called when the ports are being initialized.

.. This file was automatic generated / don't edit.


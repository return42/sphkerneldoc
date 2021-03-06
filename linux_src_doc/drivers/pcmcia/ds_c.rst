.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pcmcia/ds.c

.. _`new_id_store`:

new_id_store
============

.. c:function:: ssize_t new_id_store(struct device_driver *driver, const char *buf, size_t count)

    add a new PCMCIA device ID to this driver and re-probe devices

    :param driver:
        target device driver
    :type driver: struct device_driver \*

    :param buf:
        buffer for scanning device ID data
    :type buf: const char \*

    :param count:
        input size
    :type count: size_t

.. _`new_id_store.description`:

Description
-----------

Adds a new dynamic PCMCIA device ID to this driver,
and causes the driver to probe for all devices again.

.. _`pcmcia_register_driver`:

pcmcia_register_driver
======================

.. c:function:: int pcmcia_register_driver(struct pcmcia_driver *driver)

    register a PCMCIA driver with the bus core

    :param driver:
        the \ :c:type:`struct driver <driver>`\  being registered
    :type driver: struct pcmcia_driver \*

.. _`pcmcia_register_driver.description`:

Description
-----------

Registers a PCMCIA driver with the PCMCIA bus core.

.. _`pcmcia_unregister_driver`:

pcmcia_unregister_driver
========================

.. c:function:: void pcmcia_unregister_driver(struct pcmcia_driver *driver)

    unregister a PCMCIA driver with the bus core

    :param driver:
        the \ :c:type:`struct driver <driver>`\  being unregistered
    :type driver: struct pcmcia_driver \*

.. _`pcmcia_load_firmware`:

pcmcia_load_firmware
====================

.. c:function:: int pcmcia_load_firmware(struct pcmcia_device *dev, char *filename)

    load CIS from userspace if device-provided is broken

    :param dev:
        the pcmcia device which needs a CIS override
    :type dev: struct pcmcia_device \*

    :param filename:
        requested filename in /lib/firmware/
    :type filename: char \*

.. _`pcmcia_load_firmware.description`:

Description
-----------

This uses the in-kernel firmware loading mechanism to use a "fake CIS" if
the one provided by the card is broken. The firmware files reside in
/lib/firmware/ in userspace.

.. This file was automatic generated / don't edit.


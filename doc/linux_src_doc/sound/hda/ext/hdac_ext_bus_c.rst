.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/hda/ext/hdac_ext_bus.c

.. _`snd_hdac_ext_bus_init`:

snd_hdac_ext_bus_init
=====================

.. c:function:: int snd_hdac_ext_bus_init(struct hdac_ext_bus *ebus, struct device *dev, const struct hdac_bus_ops *ops, const struct hdac_io_ops *io_ops)

    initialize a HD-audio extended bus

    :param struct hdac_ext_bus \*ebus:
        the pointer to extended bus object

    :param struct device \*dev:
        device pointer

    :param const struct hdac_bus_ops \*ops:
        bus verb operators

    :param const struct hdac_io_ops \*io_ops:
        lowlevel I/O operators, can be NULL. If NULL core will use
        default ops

.. _`snd_hdac_ext_bus_init.description`:

Description
-----------

Returns 0 if successful, or a negative error code.

.. _`snd_hdac_ext_bus_exit`:

snd_hdac_ext_bus_exit
=====================

.. c:function:: void snd_hdac_ext_bus_exit(struct hdac_ext_bus *ebus)

    clean up a HD-audio extended bus

    :param struct hdac_ext_bus \*ebus:
        the pointer to extended bus object

.. _`snd_hdac_ext_bus_device_init`:

snd_hdac_ext_bus_device_init
============================

.. c:function:: int snd_hdac_ext_bus_device_init(struct hdac_ext_bus *ebus, int addr)

    initialize the HDA extended codec base device

    :param struct hdac_ext_bus \*ebus:
        hdac extended bus to attach to

    :param int addr:
        codec address

.. _`snd_hdac_ext_bus_device_init.description`:

Description
-----------

Returns zero for success or a negative error code.

.. _`snd_hdac_ext_bus_device_exit`:

snd_hdac_ext_bus_device_exit
============================

.. c:function:: void snd_hdac_ext_bus_device_exit(struct hdac_device *hdev)

    clean up a HD-audio extended codec base device

    :param struct hdac_device \*hdev:
        hdac device to clean up

.. _`snd_hdac_ext_bus_device_remove`:

snd_hdac_ext_bus_device_remove
==============================

.. c:function:: void snd_hdac_ext_bus_device_remove(struct hdac_ext_bus *ebus)

    remove HD-audio extended codec base devices

    :param struct hdac_ext_bus \*ebus:
        HD-audio extended bus

.. _`snd_hda_ext_driver_register`:

snd_hda_ext_driver_register
===========================

.. c:function:: int snd_hda_ext_driver_register(struct hdac_ext_driver *drv)

    register a driver for ext hda devices

    :param struct hdac_ext_driver \*drv:
        ext hda driver structure

.. _`snd_hda_ext_driver_unregister`:

snd_hda_ext_driver_unregister
=============================

.. c:function:: void snd_hda_ext_driver_unregister(struct hdac_ext_driver *drv)

    unregister a driver for ext hda devices

    :param struct hdac_ext_driver \*drv:
        ext hda driver structure

.. This file was automatic generated / don't edit.


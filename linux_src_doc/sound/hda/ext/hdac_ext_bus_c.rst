.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/hda/ext/hdac_ext_bus.c

.. _`snd_hdac_ext_bus_init`:

snd_hdac_ext_bus_init
=====================

.. c:function:: int snd_hdac_ext_bus_init(struct hdac_bus *bus, struct device *dev, const struct hdac_bus_ops *ops, const struct hdac_io_ops *io_ops, const struct hdac_ext_bus_ops *ext_ops)

    initialize a HD-audio extended bus

    :param bus:
        *undescribed*
    :type bus: struct hdac_bus \*

    :param dev:
        device pointer
    :type dev: struct device \*

    :param ops:
        bus verb operators
    :type ops: const struct hdac_bus_ops \*

    :param io_ops:
        lowlevel I/O operators, can be NULL. If NULL core will use
        default ops
    :type io_ops: const struct hdac_io_ops \*

    :param ext_ops:
        *undescribed*
    :type ext_ops: const struct hdac_ext_bus_ops \*

.. _`snd_hdac_ext_bus_init.description`:

Description
-----------

Returns 0 if successful, or a negative error code.

.. _`snd_hdac_ext_bus_exit`:

snd_hdac_ext_bus_exit
=====================

.. c:function:: void snd_hdac_ext_bus_exit(struct hdac_bus *bus)

    clean up a HD-audio extended bus

    :param bus:
        *undescribed*
    :type bus: struct hdac_bus \*

.. _`snd_hdac_ext_bus_device_init`:

snd_hdac_ext_bus_device_init
============================

.. c:function:: int snd_hdac_ext_bus_device_init(struct hdac_bus *bus, int addr, struct hdac_device *hdev)

    initialize the HDA extended codec base device

    :param bus:
        *undescribed*
    :type bus: struct hdac_bus \*

    :param addr:
        codec address
    :type addr: int

    :param hdev:
        *undescribed*
    :type hdev: struct hdac_device \*

.. _`snd_hdac_ext_bus_device_init.description`:

Description
-----------

Returns zero for success or a negative error code.

.. _`snd_hdac_ext_bus_device_exit`:

snd_hdac_ext_bus_device_exit
============================

.. c:function:: void snd_hdac_ext_bus_device_exit(struct hdac_device *hdev)

    clean up a HD-audio extended codec base device

    :param hdev:
        hdac device to clean up
    :type hdev: struct hdac_device \*

.. _`snd_hdac_ext_bus_device_remove`:

snd_hdac_ext_bus_device_remove
==============================

.. c:function:: void snd_hdac_ext_bus_device_remove(struct hdac_bus *bus)

    remove HD-audio extended codec base devices

    :param bus:
        *undescribed*
    :type bus: struct hdac_bus \*

.. _`snd_hda_ext_driver_register`:

snd_hda_ext_driver_register
===========================

.. c:function:: int snd_hda_ext_driver_register(struct hdac_driver *drv)

    register a driver for ext hda devices

    :param drv:
        ext hda driver structure
    :type drv: struct hdac_driver \*

.. _`snd_hda_ext_driver_unregister`:

snd_hda_ext_driver_unregister
=============================

.. c:function:: void snd_hda_ext_driver_unregister(struct hdac_driver *drv)

    unregister a driver for ext hda devices

    :param drv:
        ext hda driver structure
    :type drv: struct hdac_driver \*

.. This file was automatic generated / don't edit.


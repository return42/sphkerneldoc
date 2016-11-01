.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/comedi/comedi_pcmcia.c

.. _`comedi_to_pcmcia_dev`:

comedi_to_pcmcia_dev
====================

.. c:function:: struct pcmcia_device *comedi_to_pcmcia_dev(struct comedi_device *dev)

    Return PCMCIA device attached to COMEDI device

    :param struct comedi_device \*dev:
        COMEDI device.

.. _`comedi_to_pcmcia_dev.description`:

Description
-----------

Assuming \ ``dev``\ ->hw_dev is non-%NULL, it is assumed to be pointing to a
a \ :c:type:`struct device <device>`\  embedded in a \ :c:type:`struct pcmcia_device <pcmcia_device>`\ .

.. _`comedi_to_pcmcia_dev.return`:

Return
------

Attached PCMCIA device if \ ``dev``\ ->hw_dev is non-%NULL.
Return \ ``NULL``\  if \ ``dev``\ ->hw_dev is \ ``NULL``\ .

.. _`comedi_pcmcia_enable`:

comedi_pcmcia_enable
====================

.. c:function:: int comedi_pcmcia_enable(struct comedi_device *dev, int (*conf_check)(struct pcmcia_device *, void *))

    Request the regions and enable the PCMCIA device

    :param struct comedi_device \*dev:
        COMEDI device.

    :param int (\*conf_check)(struct pcmcia_device \*, void \*):
        Optional callback to check each configuration option of the
        PCMCIA device and request I/O regions.

.. _`comedi_pcmcia_enable.description`:

Description
-----------

Assuming \ ``dev``\ ->hw_dev is non-%NULL, it is assumed to be pointing to a a
\ :c:type:`struct device <device>`\  embedded in a \ :c:type:`struct pcmcia_device <pcmcia_device>`\ .  The comedi PCMCIA
driver needs to set the 'config_flags' member in the \ :c:type:`struct pcmcia_device <pcmcia_device>`\ ,
as appropriate for that driver, before calling this function in order to
allow \ :c:func:`pcmcia_loop_config`\  to do its internal autoconfiguration.

If \ ``conf_check``\  is \ ``NULL``\  it is set to a default function.  If is
passed to \ :c:func:`pcmcia_loop_config`\  and should return \ ``0``\  if the configuration
is valid and I/O regions requested successfully, otherwise it should return
a negative error value.  The default function returns -%EINVAL if the
'config_index' member is \ ``0``\ , otherwise it calls \ :c:func:`pcmcia_request_io`\  and
returns the result.

If the above configuration check passes, \ :c:func:`pcmcia_enable_device`\  is called
to set up and activate the PCMCIA device.

If this function returns an error, \ :c:func:`comedi_pcmcia_disable`\  should be called
to release requested resources.

.. _`comedi_pcmcia_enable.return`:

Return
------

0 on success,
-%ENODEV id \ ``dev``\ ->hw_dev is \ ``NULL``\ ,
a negative error number from \ :c:func:`pcmcia_loop_config`\  if it fails,
or a negative error number from \ :c:func:`pcmcia_enable_device`\  if it fails.

.. _`comedi_pcmcia_disable`:

comedi_pcmcia_disable
=====================

.. c:function:: void comedi_pcmcia_disable(struct comedi_device *dev)

    Disable the PCMCIA device and release the regions

    :param struct comedi_device \*dev:
        COMEDI device.

.. _`comedi_pcmcia_disable.description`:

Description
-----------

Assuming \ ``dev``\ ->hw_dev is non-%NULL, it is assumed to be pointing to a
a \ :c:type:`struct device <device>`\  embedded in a \ :c:type:`struct pcmcia_device <pcmcia_device>`\ .  Call
\ :c:func:`pcmcia_disable_device`\  to disable and clean up the PCMCIA device.

.. _`comedi_pcmcia_auto_config`:

comedi_pcmcia_auto_config
=========================

.. c:function:: int comedi_pcmcia_auto_config(struct pcmcia_device *link, struct comedi_driver *driver)

    Configure/probe a PCMCIA COMEDI device

    :param struct pcmcia_device \*link:
        PCMCIA device.

    :param struct comedi_driver \*driver:
        Registered COMEDI driver.

.. _`comedi_pcmcia_auto_config.description`:

Description
-----------

Typically called from the pcmcia_driver (\*probe) function.  Auto-configure
a COMEDI device, using a pointer to the \ :c:type:`struct device <device>`\  embedded in \*@link
as the hardware device.  The \ ``driver``\ 's "auto_attach" handler may call
\ :c:func:`comedi_to_pcmcia_dev`\  on the passed in COMEDI device to recover \ ``link``\ .

.. _`comedi_pcmcia_auto_config.return`:

Return
------

The result of calling \ :c:func:`comedi_auto_config`\  (0 on success, or a
negative error number on failure).

.. _`comedi_pcmcia_auto_unconfig`:

comedi_pcmcia_auto_unconfig
===========================

.. c:function:: void comedi_pcmcia_auto_unconfig(struct pcmcia_device *link)

    Unconfigure/remove a PCMCIA COMEDI device

    :param struct pcmcia_device \*link:
        PCMCIA device.

.. _`comedi_pcmcia_auto_unconfig.description`:

Description
-----------

Typically called from the pcmcia_driver (\*remove) function.
Auto-unconfigure a COMEDI device attached to this PCMCIA device, using a
pointer to the \ :c:type:`struct device <device>`\  embedded in \*@link as the hardware device.
The COMEDI driver's "detach" handler will be called during unconfiguration
of the COMEDI device.

Note that the COMEDI device may have already been unconfigured using the
\ ``COMEDI_DEVCONFIG``\  ioctl, in which case this attempt to unconfigure it
again should be ignored.

.. _`comedi_pcmcia_driver_register`:

comedi_pcmcia_driver_register
=============================

.. c:function:: int comedi_pcmcia_driver_register(struct comedi_driver *comedi_driver, struct pcmcia_driver *pcmcia_driver)

    Register a PCMCIA COMEDI driver

    :param struct comedi_driver \*comedi_driver:
        COMEDI driver to be registered.

    :param struct pcmcia_driver \*pcmcia_driver:
        PCMCIA driver to be registered.

.. _`comedi_pcmcia_driver_register.description`:

Description
-----------

This function is used for the \ :c:func:`module_init`\  of PCMCIA COMEDI driver modules
to register the COMEDI driver and the PCMCIA driver.  Do not call it
directly, use the \ :c:func:`module_comedi_pcmcia_driver`\  helper macro instead.

.. _`comedi_pcmcia_driver_register.return`:

Return
------

0 on success, or a negative error number on failure.

.. _`comedi_pcmcia_driver_unregister`:

comedi_pcmcia_driver_unregister
===============================

.. c:function:: void comedi_pcmcia_driver_unregister(struct comedi_driver *comedi_driver, struct pcmcia_driver *pcmcia_driver)

    Unregister a PCMCIA COMEDI driver

    :param struct comedi_driver \*comedi_driver:
        COMEDI driver to be registered.

    :param struct pcmcia_driver \*pcmcia_driver:
        PCMCIA driver to be registered.

.. _`comedi_pcmcia_driver_unregister.description`:

Description
-----------

This function is called from the \ :c:func:`module_exit`\  of PCMCIA COMEDI driver
modules to unregister the PCMCIA driver and the COMEDI driver.  Do not call
it directly, use the \ :c:func:`module_comedi_pcmcia_driver`\  helper macro instead.

.. This file was automatic generated / don't edit.


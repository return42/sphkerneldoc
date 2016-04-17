.. -*- coding: utf-8; mode: rst -*-

============
comedi_pci.c
============


.. _`comedi_to_pci_dev`:

comedi_to_pci_dev
=================

.. c:function:: struct pci_dev *comedi_to_pci_dev (struct comedi_device *dev)

    Return PCI device attached to COMEDI device

    :param struct comedi_device \*dev:
        COMEDI device.



.. _`comedi_to_pci_dev.description`:

Description
-----------

Assuming ``dev``\ ->hw_dev is non-\ ``NULL``\ , it is assumed to be pointing to a
a :c:type:`struct device <device>` embedded in a :c:type:`struct pci_dev <pci_dev>`.



.. _`comedi_to_pci_dev.return`:

Return
------

Attached PCI device if ``dev``\ ->hw_dev is non-\ ``NULL``\ .
Return ``NULL`` if ``dev``\ ->hw_dev is ``NULL``\ .



.. _`comedi_pci_enable`:

comedi_pci_enable
=================

.. c:function:: int comedi_pci_enable (struct comedi_device *dev)

    Enable the PCI device and request the regions

    :param struct comedi_device \*dev:
        COMEDI device.



.. _`comedi_pci_enable.description`:

Description
-----------

Assuming ``dev``\ ->hw_dev is non-\ ``NULL``\ , it is assumed to be pointing to a
a :c:type:`struct device <device>` embedded in a :c:type:`struct pci_dev <pci_dev>`.  Enable the PCI device
and request its regions.  Set ``dev``\ ->ioenabled to ``true`` if successful,
otherwise undo what was done.

Calls to :c:func:`comedi_pci_enable` and :c:func:`comedi_pci_disable` cannot be nested.



.. _`comedi_pci_enable.return`:

Return
------

0 on success,
-\ ``ENODEV`` if ``dev``\ ->hw_dev is ``NULL``\ ,
-\ ``EBUSY`` if regions busy,
or some negative error number if failed to enable PCI device.



.. _`comedi_pci_disable`:

comedi_pci_disable
==================

.. c:function:: void comedi_pci_disable (struct comedi_device *dev)

    Release the regions and disable the PCI device

    :param struct comedi_device \*dev:
        COMEDI device.



.. _`comedi_pci_disable.description`:

Description
-----------

Assuming ``dev``\ ->hw_dev is non-\ ``NULL``\ , it is assumed to be pointing to a
a :c:type:`struct device <device>` embedded in a :c:type:`struct pci_dev <pci_dev>`.  If the earlier call
to :c:func:`comedi_pci_enable` was successful, release the PCI device's regions
and disable it.  Reset ``dev``\ ->ioenabled back to ``false``\ .



.. _`comedi_pci_detach`:

comedi_pci_detach
=================

.. c:function:: void comedi_pci_detach (struct comedi_device *dev)

    A generic "detach" handler for PCI COMEDI drivers

    :param struct comedi_device \*dev:
        COMEDI device.



.. _`comedi_pci_detach.description`:

Description
-----------

COMEDI drivers for PCI devices that need no special clean-up of private data
and have no ioremapped regions other than that pointed to by ``dev``\ ->mmio may
use this function as its "detach" handler called by the COMEDI core when a
COMEDI device is being detached from the low-level driver.  It may be also
called from a more specific "detach" handler that does additional clean-up.

Free the IRQ if ``dev``\ ->irq is non-zero, iounmap ``dev``\ ->mmio if it is
non-\ ``NULL``\ , and call :c:func:`comedi_pci_disable` to release the PCI device's regions
and disable it.



.. _`comedi_pci_auto_config`:

comedi_pci_auto_config
======================

.. c:function:: int comedi_pci_auto_config (struct pci_dev *pcidev, struct comedi_driver *driver, unsigned long context)

    Configure/probe a PCI COMEDI device

    :param struct pci_dev \*pcidev:
        PCI device.

    :param struct comedi_driver \*driver:
        Registered COMEDI driver.

    :param unsigned long context:
        Driver specific data, passed to :c:func:`comedi_auto_config`.



.. _`comedi_pci_auto_config.description`:

Description
-----------

Typically called from the pci_driver (\*probe) function.  Auto-configure
a COMEDI device, using the :c:type:`struct device <device>` embedded in \*\ ``pcidev`` as the
hardware device.  The ``context`` value gets passed through to ``driver``\ 's
"auto_attach" handler.  The "auto_attach" handler may call
:c:func:`comedi_to_pci_dev` on the passed in COMEDI device to recover ``pcidev``\ .



.. _`comedi_pci_auto_config.return`:

Return
------

The result of calling :c:func:`comedi_auto_config` (0 on success, or
a negative error number on failure).



.. _`comedi_pci_auto_unconfig`:

comedi_pci_auto_unconfig
========================

.. c:function:: void comedi_pci_auto_unconfig (struct pci_dev *pcidev)

    Unconfigure/remove a PCI COMEDI device

    :param struct pci_dev \*pcidev:
        PCI device.



.. _`comedi_pci_auto_unconfig.description`:

Description
-----------

Typically called from the pci_driver (\*remove) function.  Auto-unconfigure
a COMEDI device attached to this PCI device, using a pointer to the
:c:type:`struct device <device>` embedded in \*\ ``pcidev`` as the hardware device.  The COMEDI
driver's "detach" handler will be called during unconfiguration of the
COMEDI device.

Note that the COMEDI device may have already been unconfigured using the
``COMEDI_DEVCONFIG`` ioctl, in which case this attempt to unconfigure it
again should be ignored.



.. _`comedi_pci_driver_register`:

comedi_pci_driver_register
==========================

.. c:function:: int comedi_pci_driver_register (struct comedi_driver *comedi_driver, struct pci_driver *pci_driver)

    Register a PCI COMEDI driver

    :param struct comedi_driver \*comedi_driver:
        COMEDI driver to be registered.

    :param struct pci_driver \*pci_driver:
        PCI driver to be registered.



.. _`comedi_pci_driver_register.description`:

Description
-----------

This function is called from the :c:func:`module_init` of PCI COMEDI driver modules
to register the COMEDI driver and the PCI driver.  Do not call it directly,
use the :c:func:`module_comedi_pci_driver` helper macro instead.



.. _`comedi_pci_driver_register.return`:

Return
------

0 on success, or a negative error number on failure.



.. _`comedi_pci_driver_unregister`:

comedi_pci_driver_unregister
============================

.. c:function:: void comedi_pci_driver_unregister (struct comedi_driver *comedi_driver, struct pci_driver *pci_driver)

    Unregister a PCI COMEDI driver

    :param struct comedi_driver \*comedi_driver:
        COMEDI driver to be unregistered.

    :param struct pci_driver \*pci_driver:
        PCI driver to be unregistered.



.. _`comedi_pci_driver_unregister.description`:

Description
-----------

This function is called from the :c:func:`module_exit` of PCI COMEDI driver modules
to unregister the PCI driver and the COMEDI driver.  Do not call it
directly, use the :c:func:`module_comedi_pci_driver` helper macro instead.


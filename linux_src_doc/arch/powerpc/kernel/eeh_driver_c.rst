.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/kernel/eeh_driver.c

.. _`eeh_pcid_name`:

eeh_pcid_name
=============

.. c:function:: const char *eeh_pcid_name(struct pci_dev *pdev)

    Retrieve name of PCI device driver

    :param struct pci_dev \*pdev:
        PCI device

.. _`eeh_pcid_name.description`:

Description
-----------

This routine is used to retrieve the name of PCI device driver
if that's valid.

.. _`eeh_pcid_get`:

eeh_pcid_get
============

.. c:function:: struct pci_driver *eeh_pcid_get(struct pci_dev *pdev)

    Get the PCI device driver

    :param struct pci_dev \*pdev:
        PCI device

.. _`eeh_pcid_get.description`:

Description
-----------

The function is used to retrieve the PCI device driver for
the indicated PCI device. Besides, we will increase the reference
of the PCI device driver to prevent that being unloaded on
the fly. Otherwise, kernel crash would be seen.

.. _`eeh_pcid_put`:

eeh_pcid_put
============

.. c:function:: void eeh_pcid_put(struct pci_dev *pdev)

    Dereference on the PCI device driver

    :param struct pci_dev \*pdev:
        PCI device

.. _`eeh_pcid_put.description`:

Description
-----------

The function is called to do dereference on the PCI device
driver of the indicated PCI device.

.. _`eeh_disable_irq`:

eeh_disable_irq
===============

.. c:function:: void eeh_disable_irq(struct pci_dev *dev)

    Disable interrupt for the recovering device

    :param struct pci_dev \*dev:
        PCI device

.. _`eeh_disable_irq.description`:

Description
-----------

This routine must be called when reporting temporary or permanent
error to the particular PCI device to disable interrupt of that
device. If the device has enabled MSI or MSI-X interrupt, we needn't
do real work because EEH should freeze DMA transfers for those PCI
devices encountering EEH errors, which includes MSI or MSI-X.

.. _`eeh_enable_irq`:

eeh_enable_irq
==============

.. c:function:: void eeh_enable_irq(struct pci_dev *dev)

    Enable interrupt for the recovering device

    :param struct pci_dev \*dev:
        PCI device

.. _`eeh_enable_irq.description`:

Description
-----------

This routine must be called to enable interrupt while failed
device could be resumed.

.. _`eeh_report_error`:

eeh_report_error
================

.. c:function:: void *eeh_report_error(void *data, void *userdata)

    Report pci error to each device driver

    :param void \*data:
        eeh device

    :param void \*userdata:
        return value

.. _`eeh_report_error.description`:

Description
-----------

Report an EEH error to each device driver, collect up and
merge the device driver responses. Cumulative response
passed back in "userdata".

.. _`eeh_report_mmio_enabled`:

eeh_report_mmio_enabled
=======================

.. c:function:: void *eeh_report_mmio_enabled(void *data, void *userdata)

    Tell drivers that MMIO has been enabled

    :param void \*data:
        eeh device

    :param void \*userdata:
        return value

.. _`eeh_report_mmio_enabled.description`:

Description
-----------

Tells each device driver that IO ports, MMIO and config space I/O
are now enabled. Collects up and merges the device driver responses.
Cumulative response passed back in "userdata".

.. _`eeh_report_reset`:

eeh_report_reset
================

.. c:function:: void *eeh_report_reset(void *data, void *userdata)

    Tell device that slot has been reset

    :param void \*data:
        eeh device

    :param void \*userdata:
        return value

.. _`eeh_report_reset.description`:

Description
-----------

This routine must be called while EEH tries to reset particular
PCI device so that the associated PCI device driver could take
some actions, usually to save data the driver needs so that the
driver can work again while the device is recovered.

.. _`eeh_report_resume`:

eeh_report_resume
=================

.. c:function:: void *eeh_report_resume(void *data, void *userdata)

    Tell device to resume normal operations

    :param void \*data:
        eeh device

    :param void \*userdata:
        return value

.. _`eeh_report_resume.description`:

Description
-----------

This routine must be called to notify the device driver that it
could resume so that the device driver can do some initialization
to make the recovered device work again.

.. _`eeh_report_failure`:

eeh_report_failure
==================

.. c:function:: void *eeh_report_failure(void *data, void *userdata)

    Tell device driver that device is dead.

    :param void \*data:
        eeh device

    :param void \*userdata:
        return value

.. _`eeh_report_failure.description`:

Description
-----------

This informs the device driver that the device is permanently
dead, and that no further recovery attempts will be made on it.

.. _`eeh_reset_device`:

eeh_reset_device
================

.. c:function:: int eeh_reset_device(struct eeh_pe *pe, struct pci_bus *bus, struct eeh_rmv_data *rmv_data)

    Perform actual reset of a pci slot

    :param struct eeh_pe \*pe:
        EEH PE

    :param struct pci_bus \*bus:
        PCI bus corresponding to the isolcated slot

    :param struct eeh_rmv_data \*rmv_data:
        *undescribed*

.. _`eeh_reset_device.description`:

Description
-----------

This routine must be called to do reset on the indicated PE.
During the reset, udev might be invoked because those affected
PCI devices will be removed and then added.

.. _`eeh_handle_normal_event`:

eeh_handle_normal_event
=======================

.. c:function:: bool eeh_handle_normal_event(struct eeh_pe *pe)

    Handle EEH events on a specific PE

    :param struct eeh_pe \*pe:
        EEH PE

.. _`eeh_handle_normal_event.description`:

Description
-----------

Attempts to recover the given PE.  If recovery fails or the PE has failed
too many times, remove the PE.

Returns true if \ ``pe``\  should no longer be used, else false.

.. _`eeh_handle_special_event`:

eeh_handle_special_event
========================

.. c:function:: void eeh_handle_special_event( void)

    Handle EEH events without a specific failing PE

    :param  void:
        no arguments

.. _`eeh_handle_special_event.description`:

Description
-----------

Called when an EEH event is detected but can't be narrowed down to a
specific PE.  Iterates through possible failures and handles them as
necessary.

.. _`eeh_handle_event`:

eeh_handle_event
================

.. c:function:: void eeh_handle_event(struct eeh_pe *pe)

    Reset a PCI device after hard lockup.

    :param struct eeh_pe \*pe:
        EEH PE

.. _`eeh_handle_event.description`:

Description
-----------

While PHB detects address or data parity errors on particular PCI
slot, the associated PE will be frozen. Besides, DMA's occurring
to wild addresses (which usually happen due to bugs in device
drivers or in PCI adapter firmware) can cause EEH error. #SERR,
#PERR or other misc PCI-related errors also can trigger EEH errors.

Recovery process consists of unplugging the device driver (which
generated hotplug events to userspace), then issuing a PCI #RST to
the device, then reconfiguring the PCI config space for all bridges
& devices under this slot, and then finally restarting the device
drivers (which cause a second set of hotplug events to go out to
userspace).

.. This file was automatic generated / don't edit.


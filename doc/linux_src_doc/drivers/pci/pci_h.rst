.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/pci.h

.. _`pci_platform_pm_ops`:

struct pci_platform_pm_ops
==========================

.. c:type:: struct pci_platform_pm_ops

    Firmware PM callbacks

.. _`pci_platform_pm_ops.definition`:

Definition
----------

.. code-block:: c

    struct pci_platform_pm_ops {
        bool (* is_manageable) (struct pci_dev *dev);
        int (* set_state) (struct pci_dev *dev, pci_power_t state);
        pci_power_t (* choose_state) (struct pci_dev *dev);
        int (* sleep_wake) (struct pci_dev *dev, bool enable);
        int (* run_wake) (struct pci_dev *dev, bool enable);
        bool (* need_resume) (struct pci_dev *dev);
    }

.. _`pci_platform_pm_ops.members`:

Members
-------

is_manageable
    returns 'true' if given device is power manageable by the
    platform firmware

set_state
    invokes the platform firmware to set the device's power state

choose_state
    returns PCI power state of given device preferred by the
    platform; to be used during system-wide transitions from a
    sleeping state to the working state and vice versa

sleep_wake
    enables/disables the system wake up capability of given device

run_wake
    enables/disables the platform to generate run-time wake-up events
    for given device (the device's wake-up capability has to be
    enabled by \ ``sleep_wake``\  for this feature to work)

need_resume
    returns 'true' if the given device (which is currently
    suspended) needs to be resumed to be configured for system
    wakeup.

.. _`pci_platform_pm_ops.description`:

Description
-----------

If given platform is generally capable of power managing PCI devices, all of
these callbacks are mandatory.

.. _`pci_match_one_device`:

pci_match_one_device
====================

.. c:function:: const struct pci_device_id *pci_match_one_device(const struct pci_device_id *id, const struct pci_dev *dev)

    Tell if a PCI device structure has a matching PCI device id structure

    :param const struct pci_device_id \*id:
        single PCI device id structure to match

    :param const struct pci_dev \*dev:
        the PCI device structure to match against

.. _`pci_match_one_device.description`:

Description
-----------

Returns the matching pci_device_id structure or \ ``NULL``\  if there is no match.

.. This file was automatic generated / don't edit.


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
        bool (*bridge_d3)(struct pci_dev *dev);
        bool (*is_manageable)(struct pci_dev *dev);
        int (*set_state)(struct pci_dev *dev, pci_power_t state);
        pci_power_t (*get_state)(struct pci_dev *dev);
        pci_power_t (*choose_state)(struct pci_dev *dev);
        int (*set_wakeup)(struct pci_dev *dev, bool enable);
        bool (*need_resume)(struct pci_dev *dev);
    }

.. _`pci_platform_pm_ops.members`:

Members
-------

bridge_d3
    Does the bridge allow entering into D3

is_manageable
    returns 'true' if given device is power manageable by the
    platform firmware

set_state
    invokes the platform firmware to set the device's power state

get_state
    queries the platform firmware for a device's current power state

choose_state
    returns PCI power state of given device preferred by the
    platform; to be used during system-wide transitions from a
    sleeping state to the working state and vice versa

set_wakeup
    enables/disables wakeup capability for the device

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

    :param id:
        single PCI device id structure to match
    :type id: const struct pci_device_id \*

    :param dev:
        the PCI device structure to match against
    :type dev: const struct pci_dev \*

.. _`pci_match_one_device.description`:

Description
-----------

Returns the matching pci_device_id structure or \ ``NULL``\  if there is no match.

.. _`pci_dev_set_io_state`:

pci_dev_set_io_state
====================

.. c:function:: bool pci_dev_set_io_state(struct pci_dev *dev, pci_channel_state_t new)

    Set the new error state if possible.

    :param dev:
        *undescribed*
    :type dev: struct pci_dev \*

    :param new:
        *undescribed*
    :type new: pci_channel_state_t

.. _`pci_dev_set_io_state.description`:

Description
-----------

\ ``dev``\  - pci device to set new error_state
\ ``new``\  - the state we want dev to be in

Must be called with device_lock held.

Returns true if state has been changed to the requested state.

.. This file was automatic generated / don't edit.


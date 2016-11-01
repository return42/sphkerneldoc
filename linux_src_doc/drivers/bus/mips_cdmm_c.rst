.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/bus/mips_cdmm.c

.. _`mips_cdmm_work_dev`:

struct mips_cdmm_work_dev
=========================

.. c:type:: struct mips_cdmm_work_dev

    Data for per-device call work.

.. _`mips_cdmm_work_dev.definition`:

Definition
----------

.. code-block:: c

    struct mips_cdmm_work_dev {
        void *fn;
        struct mips_cdmm_device *dev;
    }

.. _`mips_cdmm_work_dev.members`:

Members
-------

fn
    CDMM driver callback function to call for the device.

dev
    CDMM device to pass to \ ``fn``\ .

.. _`mips_cdmm_void_work`:

mips_cdmm_void_work
===================

.. c:function:: long mips_cdmm_void_work(void *data)

    Call a void returning CDMM driver callback.

    :param void \*data:
        struct mips_cdmm_work_dev pointer.

.. _`mips_cdmm_void_work.description`:

Description
-----------

A \ :c:func:`work_on_cpu`\  callback function to call an arbitrary CDMM driver callback
function which doesn't return a value.

.. _`mips_cdmm_int_work`:

mips_cdmm_int_work
==================

.. c:function:: long mips_cdmm_int_work(void *data)

    Call an int returning CDMM driver callback.

    :param void \*data:
        struct mips_cdmm_work_dev pointer.

.. _`mips_cdmm_int_work.description`:

Description
-----------

A \ :c:func:`work_on_cpu`\  callback function to call an arbitrary CDMM driver callback
function which returns an int.

.. _`build_percpu_helper`:

BUILD_PERCPU_HELPER
===================

.. c:function::  BUILD_PERCPU_HELPER( _ret,  _name)

    Helper to call a CDMM driver callback on right CPU.

    :param  _ret:
        Return type (void or int).

    :param  _name:
        Name of CDMM driver callback function.

.. _`build_percpu_helper.description`:

Description
-----------

Generates a specific device callback function to call a CDMM driver callback
function on the appropriate CPU for the device, and if applicable return the
result.

.. _`mips_cdmm_driver_register`:

mips_cdmm_driver_register
=========================

.. c:function:: int mips_cdmm_driver_register(struct mips_cdmm_driver *drv)

    Register a CDMM driver.

    :param struct mips_cdmm_driver \*drv:
        CDMM driver information.

.. _`mips_cdmm_driver_register.description`:

Description
-----------

Register a CDMM driver with the CDMM subsystem. The driver will be informed
of matching devices which are discovered.

.. _`mips_cdmm_driver_register.return`:

Return
------

0 on success.

.. _`mips_cdmm_driver_unregister`:

mips_cdmm_driver_unregister
===========================

.. c:function:: void mips_cdmm_driver_unregister(struct mips_cdmm_driver *drv)

    Unregister a CDMM driver.

    :param struct mips_cdmm_driver \*drv:
        CDMM driver information.

.. _`mips_cdmm_driver_unregister.description`:

Description
-----------

Unregister a CDMM driver from the CDMM subsystem.

.. _`mips_cdmm_bus`:

struct mips_cdmm_bus
====================

.. c:type:: struct mips_cdmm_bus

    Info about CDMM bus.

.. _`mips_cdmm_bus.definition`:

Definition
----------

.. code-block:: c

    struct mips_cdmm_bus {
        phys_addr_t phys;
        void __iomem *regs;
        unsigned int drbs;
        unsigned int drbs_reserved;
        bool discovered;
        bool offline;
    }

.. _`mips_cdmm_bus.members`:

Members
-------

phys
    Physical address at which it is mapped.

regs
    Virtual address where registers can be accessed.

drbs
    Total number of DRBs.

drbs_reserved
    Number of DRBs reserved.

discovered
    Whether the devices on the bus have been discovered yet.

offline
    Whether the CDMM bus is going offline (or very early
    coming back online), in which case it should be
    reconfigured each time.

.. _`mips_cdmm_get_bus`:

mips_cdmm_get_bus
=================

.. c:function:: struct mips_cdmm_bus *mips_cdmm_get_bus( void)

    Get the per-CPU CDMM bus information.

    :param  void:
        no arguments

.. _`mips_cdmm_get_bus.description`:

Description
-----------

Get information about the per-CPU CDMM bus, if the bus is present.

The caller must prevent migration to another CPU, either by disabling
pre-emption or by running from a pinned kernel thread.

.. _`mips_cdmm_get_bus.return`:

Return
------

Pointer to CDMM bus information for the current CPU.
May return ERR_PTR(-errno) in case of error, so check with
\ :c:func:`IS_ERR`\ .

.. _`mips_cdmm_cur_base`:

mips_cdmm_cur_base
==================

.. c:function:: phys_addr_t mips_cdmm_cur_base( void)

    Find current physical base address of CDMM region.

    :param  void:
        no arguments

.. _`mips_cdmm_cur_base.return`:

Return
------

Physical base address of CDMM region according to cdmmbase CP0
register, or 0 if the CDMM region is disabled.

.. _`mips_cdmm_phys_base`:

mips_cdmm_phys_base
===================

.. c:function:: phys_addr_t mips_cdmm_phys_base( void)

    Choose a physical base address for CDMM region.

    :param  void:
        no arguments

.. _`mips_cdmm_phys_base.description`:

Description
-----------

Picking a suitable physical address at which to map the CDMM region is
platform specific, so this weak function can be overridden by platform
code to pick a suitable value if none is configured by the bootloader.

.. _`mips_cdmm_setup`:

mips_cdmm_setup
===============

.. c:function:: int mips_cdmm_setup(struct mips_cdmm_bus *bus)

    Ensure the CDMM bus is initialised and usable.

    :param struct mips_cdmm_bus \*bus:
        Pointer to bus information for current CPU.
        IS_ERR(bus) is checked, so no need for caller to check.

.. _`mips_cdmm_setup.description`:

Description
-----------

The caller must prevent migration to another CPU, either by disabling
pre-emption or by running from a pinned kernel thread.

Returns      0 on success, -errno on failure.

.. _`mips_cdmm_early_probe`:

mips_cdmm_early_probe
=====================

.. c:function:: void __iomem *mips_cdmm_early_probe(unsigned int dev_type)

    Minimally probe for a specific device on CDMM.

    :param unsigned int dev_type:
        CDMM type code to look for.

.. _`mips_cdmm_early_probe.description`:

Description
-----------

Minimally configure the in-CPU Common Device Memory Map (CDMM) and look for a
specific device. This can be used to find a device very early in boot for
example to configure an early FDC console device.

The caller must prevent migration to another CPU, either by disabling
pre-emption or by running from a pinned kernel thread.

.. _`mips_cdmm_early_probe.return`:

Return
------

MMIO pointer to device memory. The caller can read the ACSR
register to find more information about the device (such as the
version number or the number of blocks).
May return IOMEM_ERR_PTR(-errno) in case of error, so check with
\ :c:func:`IS_ERR`\ .

.. _`mips_cdmm_release`:

mips_cdmm_release
=================

.. c:function:: void mips_cdmm_release(struct device *dev)

    Release a removed CDMM device.

    :param struct device \*dev:
        Device object

.. _`mips_cdmm_release.description`:

Description
-----------

Clean up the struct mips_cdmm_device for an unused CDMM device. This is
called automatically by the driver core when a device is removed.

.. _`mips_cdmm_bus_discover`:

mips_cdmm_bus_discover
======================

.. c:function:: void mips_cdmm_bus_discover(struct mips_cdmm_bus *bus)

    Discover the devices on the CDMM bus.

    :param struct mips_cdmm_bus \*bus:
        CDMM bus information, must already be set up.

.. _`build_perdev_helper`:

BUILD_PERDEV_HELPER
===================

.. c:function::  BUILD_PERDEV_HELPER( _name)

    Helper to call a CDMM driver callback if CPU matches.

    :param  _name:
        Name of CDMM driver callback function.

.. _`build_perdev_helper.description`:

Description
-----------

Generates a bus_for_each_dev callback function to call a specific CDMM driver
callback function for the device if the device's CPU matches that pointed to
by the data argument.

This is used for informing drivers for all devices on a given CPU of some
event (such as the CPU going online/offline).

It is expected to already be called from the appropriate CPU.

.. _`mips_cdmm_cpu_down_prep`:

mips_cdmm_cpu_down_prep
=======================

.. c:function:: int mips_cdmm_cpu_down_prep(unsigned int cpu)

    Callback for CPUHP DOWN_PREP: Tear down the CDMM bus.

    :param unsigned int cpu:
        unsigned int CPU number.

.. _`mips_cdmm_cpu_down_prep.description`:

Description
-----------

This function is executed on the hotplugged CPU and calls the CDMM
driver cpu_down callback for all devices on that CPU.

.. _`mips_cdmm_cpu_online`:

mips_cdmm_cpu_online
====================

.. c:function:: int mips_cdmm_cpu_online(unsigned int cpu)

    Callback for CPUHP ONLINE: Bring up the CDMM bus.

    :param unsigned int cpu:
        unsigned int CPU number.

.. _`mips_cdmm_cpu_online.description`:

Description
-----------

This work_on_cpu callback function is executed on a given CPU to discover
CDMM devices on that CPU, or to call the CDMM driver cpu_up callback for all
devices already discovered on that CPU.

It is used as work_on_cpu callback function during
initialisation. When CPUs are brought online the function is
invoked directly on the hotplugged CPU.

.. _`mips_cdmm_init`:

mips_cdmm_init
==============

.. c:function:: int mips_cdmm_init( void)

    Initialise CDMM bus.

    :param  void:
        no arguments

.. _`mips_cdmm_init.description`:

Description
-----------

Initialise CDMM bus, discover CDMM devices for online CPUs, and arrange for
hotplug notifications so the CDMM drivers can be kept up to date.

.. This file was automatic generated / don't edit.


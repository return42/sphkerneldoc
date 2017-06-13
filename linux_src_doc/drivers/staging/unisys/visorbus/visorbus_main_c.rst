.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/unisys/visorbus/visorbus_main.c

.. _`visorbus_unregister_visor_driver`:

visorbus_unregister_visor_driver
================================

.. c:function:: void visorbus_unregister_visor_driver(struct visor_driver *drv)

    unregisters the provided driver

    :param struct visor_driver \*drv:
        the driver to unregister

.. _`visorbus_unregister_visor_driver.description`:

Description
-----------

A visor function driver calls this function to unregister the driver,
i.e., within its module_exit function.

.. _`visorbus_read_channel`:

visorbus_read_channel
=====================

.. c:function:: int visorbus_read_channel(struct visor_device *dev, unsigned long offset, void *dest, unsigned long nbytes)

    reads from the designated channel into the provided buffer

    :param struct visor_device \*dev:
        the device whose channel is read from

    :param unsigned long offset:
        the offset into the channel at which reading starts

    :param void \*dest:
        the destination buffer that is written into from the channel

    :param unsigned long nbytes:
        the number of bytes to read from the channel

.. _`visorbus_read_channel.description`:

Description
-----------

If receiving a message, use the \ :c:func:`visorchannel_signalremove`\ 
function instead.

.. _`visorbus_read_channel.return`:

Return
------

integer indicating success (zero) or failure (non-zero)

.. _`visorbus_write_channel`:

visorbus_write_channel
======================

.. c:function:: int visorbus_write_channel(struct visor_device *dev, unsigned long offset, void *src, unsigned long nbytes)

    writes the provided buffer into the designated channel

    :param struct visor_device \*dev:
        the device whose channel is written to

    :param unsigned long offset:
        the offset into the channel at which writing starts

    :param void \*src:
        the source buffer that is written into the channel

    :param unsigned long nbytes:
        the number of bytes to write into the channel

.. _`visorbus_write_channel.description`:

Description
-----------

If sending a message, use the \ :c:func:`visorchannel_signalinsert`\ 
function instead.

.. _`visorbus_write_channel.return`:

Return
------

integer indicating success (zero) or failure (non-zero)

.. _`visorbus_enable_channel_interrupts`:

visorbus_enable_channel_interrupts
==================================

.. c:function:: int visorbus_enable_channel_interrupts(struct visor_device *dev)

    enables interrupts on the designated device

    :param struct visor_device \*dev:
        the device on which to enable interrupts

.. _`visorbus_enable_channel_interrupts.description`:

Description
-----------

Currently we don't yet have a real interrupt, so for now we just call the
interrupt function periodically via a timer.

.. _`visorbus_disable_channel_interrupts`:

visorbus_disable_channel_interrupts
===================================

.. c:function:: void visorbus_disable_channel_interrupts(struct visor_device *dev)

    disables interrupts on the designated device

    :param struct visor_device \*dev:
        the device on which to disable interrupts

.. _`visorbus_register_visor_driver`:

visorbus_register_visor_driver
==============================

.. c:function:: int visorbus_register_visor_driver(struct visor_driver *drv)

    registers the provided visor driver for handling one or more visor device types (channel_types)

    :param struct visor_driver \*drv:
        the driver to register

.. _`visorbus_register_visor_driver.description`:

Description
-----------

A visor function driver calls this function to register
the driver.  The caller MUST fill in the following fields within the
#drv structure:
name, version, owner, channel_types, probe, remove

Here's how the whole Linux bus / driver / device model works.

At system start-up, the visorbus kernel module is loaded, which registers
visorbus_type as a bus type, using \ :c:func:`bus_register`\ .

All kernel modules that support particular device types on a
visorbus bus are loaded.  Each of these kernel modules calls
\ :c:func:`visorbus_register_visor_driver`\  in their init functions, passing a
visor_driver struct.  \ :c:func:`visorbus_register_visor_driver`\  in turn calls
register_driver(&visor_driver.driver).  This .driver member is
initialized with generic methods (like probe), whose sole responsibility
is to act as a broker for the real methods, which are within the
visor_driver struct.  (This is the way the subclass behavior is
implemented, since visor_driver is essentially a subclass of the
generic driver.)  Whenever a \ :c:func:`driver_register`\  happens, core bus code in
the kernel does (see \ :c:func:`device_attach`\  in drivers/base/dd.c):

for each dev associated with the bus (the bus that driver is on) that
does not yet have a driver
if bus.match(dev,newdriver) == yes_matched  \*\* .match specified
\*\* during \ :c:func:`bus_register`\ .
newdriver.probe(dev)  \*\* for visor drivers, this will call
\*\* the generic driver.probe implemented in visorbus.c,
\*\* which in turn calls the probe specified within the
\*\* struct visor_driver (which was specified by the
\*\* actual device driver as part of
\*\* \ :c:func:`visorbus_register_visor_driver`\ ).

The above dance also happens when a new device appears.
So the question is, how are devices created within the system?
Basically, just call device_add(dev).  See \ :c:func:`pci_bus_add_devices`\ .
\ :c:func:`pci_scan_device`\  shows an example of how to build a device struct.  It
returns the newly-created struct to \ :c:func:`pci_scan_single_device`\ , who adds it
to the list of devices at PCIBUS.devices.  That list of devices is what
is traversed by \ :c:func:`pci_bus_add_devices`\ .

.. _`visorbus_register_visor_driver.return`:

Return
------

integer indicating success (zero) or failure (non-zero)

.. _`chipset_device_pause`:

chipset_device_pause
====================

.. c:function:: int chipset_device_pause(struct visor_device *dev_info)

    start a pause operation for a visor device

    :param struct visor_device \*dev_info:
        struct visor_device identifying the device being paused

.. _`chipset_device_pause.description`:

Description
-----------

Tell the subordinate function driver for a specific device to pause
that device.  Success/failure result is returned asynchronously
via a callback function; see \ :c:func:`pause_state_change_complete`\ .

.. _`chipset_device_resume`:

chipset_device_resume
=====================

.. c:function:: int chipset_device_resume(struct visor_device *dev_info)

    start a resume operation for a visor device

    :param struct visor_device \*dev_info:
        struct visor_device identifying the device being resumed

.. _`chipset_device_resume.description`:

Description
-----------

Tell the subordinate function driver for a specific device to resume
that device.  Success/failure result is returned asynchronously
via a callback function; see \ :c:func:`resume_state_change_complete`\ .

.. This file was automatic generated / don't edit.


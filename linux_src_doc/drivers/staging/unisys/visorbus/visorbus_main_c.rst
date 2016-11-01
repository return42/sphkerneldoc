.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/unisys/visorbus/visorbus_main.c

.. _`visorbus_match`:

visorbus_match
==============

.. c:function:: int visorbus_match(struct device *xdev, struct device_driver *xdrv)

    called automatically upon adding a visor_device (device_add), or adding a visor_driver (visorbus_register_visor_driver)

    :param struct device \*xdev:
        struct device for the device being matched

    :param struct device_driver \*xdrv:
        struct device_driver for driver to match device against

.. _`visorbus_match.return`:

Return
------

1 iff the provided driver can control the specified device

.. _`visorbus_release_busdevice`:

visorbus_release_busdevice
==========================

.. c:function:: void visorbus_release_busdevice(struct device *xdev)

    called when \ :c:func:`device_unregister`\  is called for the bus device instance, after all other tasks involved with destroying the dev are complete

    :param struct device \*xdev:
        struct device for the bus being released

.. _`visorbus_release_device`:

visorbus_release_device
=======================

.. c:function:: void visorbus_release_device(struct device *xdev)

    called when \ :c:func:`device_unregister`\  is called for each child device instance

    :param struct device \*xdev:
        struct device for the visor device being released

.. _`visordriver_remove_device`:

visordriver_remove_device
=========================

.. c:function:: int visordriver_remove_device(struct device *xdev)

    handle visor device going away

    :param struct device \*xdev:
        struct device for the visor device being removed

.. _`visordriver_remove_device.description`:

Description
-----------

This is called when \ :c:func:`device_unregister`\  is called for each child device
instance, to notify the appropriate visorbus function driver that the device
is going away, and to decrease the reference count of the device.

.. _`visordriver_remove_device.return`:

Return
------

0 iff successful

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

.. c:function:: void visorbus_enable_channel_interrupts(struct visor_device *dev)

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

.. _`create_visor_device`:

create_visor_device
===================

.. c:function:: int create_visor_device(struct visor_device *dev)

    create visor device as a result of receiving the controlvm device_create message for a new device

    :param struct visor_device \*dev:
        a freshly-zeroed struct visor_device, containing only filled-in values
        for chipset_bus_no and chipset_dev_no, that will be initialized

.. _`create_visor_device.description`:

Description
-----------

This is how everything starts from the device end.
This function is called when a channel first appears via a ControlVM
message.  In response, this function allocates a visor_device to
correspond to the new channel, and attempts to connect it the appropriate
driver.  If the appropriate driver is found, the visor_driver.probe()
function for that driver will be called, and will be passed the new
visor_device that we just created.

It's ok if the appropriate driver is not yet loaded, because in that case
the new device struct will just stick around in the bus' list of devices.
When the appropriate driver calls \ :c:func:`visorbus_register_visor_driver`\ , the
visor_driver.probe() for the new driver will be called with the new
device.

.. _`create_visor_device.return`:

Return
------

0 if successful, otherwise the negative value returned by
\ :c:func:`device_add`\  indicating the reason for failure

.. _`write_vbus_chp_info`:

write_vbus_chp_info
===================

.. c:function:: void write_vbus_chp_info(struct visorchannel *chan, struct spar_vbus_headerinfo *hdr_info, struct ultra_vbus_deviceinfo *info)

    write the contents of <info> to the struct spar_vbus_channel_protocol.chp_info

    :param struct visorchannel \*chan:
        indentifies the s-Par channel that will be updated

    :param struct spar_vbus_headerinfo \*hdr_info:
        used to find appropriate channel offset to write data

    :param struct ultra_vbus_deviceinfo \*info:
        contains the information to write

.. _`write_vbus_chp_info.description`:

Description
-----------

Writes chipset info into the channel memory to be used for diagnostic
purposes.

Returns no value since this is debug information and not needed for
device functionality.

.. _`write_vbus_bus_info`:

write_vbus_bus_info
===================

.. c:function:: void write_vbus_bus_info(struct visorchannel *chan, struct spar_vbus_headerinfo *hdr_info, struct ultra_vbus_deviceinfo *info)

    write the contents of <info> to the struct spar_vbus_channel_protocol.bus_info

    :param struct visorchannel \*chan:
        indentifies the s-Par channel that will be updated

    :param struct spar_vbus_headerinfo \*hdr_info:
        used to find appropriate channel offset to write data

    :param struct ultra_vbus_deviceinfo \*info:
        contains the information to write

.. _`write_vbus_bus_info.description`:

Description
-----------

Writes bus info into the channel memory to be used for diagnostic
purposes.

Returns no value since this is debug information and not needed for
device functionality.

.. _`write_vbus_dev_info`:

write_vbus_dev_info
===================

.. c:function:: void write_vbus_dev_info(struct visorchannel *chan, struct spar_vbus_headerinfo *hdr_info, struct ultra_vbus_deviceinfo *info, unsigned int devix)

    write the contents of <info> to the struct spar_vbus_channel_protocol.dev_info[<devix>]

    :param struct visorchannel \*chan:
        indentifies the s-Par channel that will be updated

    :param struct spar_vbus_headerinfo \*hdr_info:
        used to find appropriate channel offset to write data

    :param struct ultra_vbus_deviceinfo \*info:
        contains the information to write

    :param unsigned int devix:
        the relative device number (0..n-1) of the device on the bus

.. _`write_vbus_dev_info.description`:

Description
-----------

Writes device info into the channel memory to be used for diagnostic
purposes.

Returns no value since this is debug information and not needed for
device functionality.

.. _`fix_vbus_dev_info`:

fix_vbus_dev_info
=================

.. c:function:: void fix_vbus_dev_info(struct visor_device *visordev)

    for a child device just created on a client bus, fill in information about the driver that is controlling this device into the the appropriate slot within the vbus channel of the bus instance

    :param struct visor_device \*visordev:
        struct visor_device for the desired device

.. _`visordriver_probe_device`:

visordriver_probe_device
========================

.. c:function:: int visordriver_probe_device(struct device *xdev)

    handle new visor device coming online

    :param struct device \*xdev:
        struct device for the visor device being probed

.. _`visordriver_probe_device.description`:

Description
-----------

This is called automatically upon adding a visor_device (device_add), or
adding a visor_driver (visorbus_register_visor_driver), but only after
\ :c:func:`visorbus_match`\  has returned 1 to indicate a successful match between
driver and device.

If successful, a reference to the device will be held onto via \ :c:func:`get_device`\ .

.. _`visordriver_probe_device.return`:

Return
------

0 if successful, meaning the function driver's \ :c:func:`probe`\  function
was successful with this device, otherwise a negative errno
value indicating failure reason

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

.. _`create_bus_instance`:

create_bus_instance
===================

.. c:function:: int create_bus_instance(struct visor_device *dev)

    create a device instance for the visor bus itself

    :param struct visor_device \*dev:
        struct visor_device indicating the bus instance

.. _`create_bus_instance.return`:

Return
------

0 for success, otherwise negative errno value indicating reason for
failure

.. _`remove_bus_instance`:

remove_bus_instance
===================

.. c:function:: void remove_bus_instance(struct visor_device *dev)

    remove a device instance for the visor bus itself

    :param struct visor_device \*dev:
        struct visor_device indentifying the bus to remove

.. _`create_bus_type`:

create_bus_type
===============

.. c:function:: int create_bus_type( void)

    create and register the one-and-only one instance of the visor bus type (visorbus_type)

    :param  void:
        no arguments

.. _`create_bus_type.return`:

Return
------

0 for success, otherwise negative errno value returned by
\ :c:func:`bus_register`\  indicating the reason for failure

.. _`remove_bus_type`:

remove_bus_type
===============

.. c:function:: void remove_bus_type( void)

    remove the one-and-only one instance of the visor bus type (visorbus_type)

    :param  void:
        no arguments

.. _`remove_all_visor_devices`:

remove_all_visor_devices
========================

.. c:function:: void remove_all_visor_devices( void)

    remove all child visor bus device instances

    :param  void:
        no arguments

.. _`pause_state_change_complete`:

pause_state_change_complete
===========================

.. c:function:: void pause_state_change_complete(struct visor_device *dev, int status)

    the callback function to be called by a visorbus function driver when a pending "pause device" operation has completed

    :param struct visor_device \*dev:
        struct visor_device identifying the paused device

    :param int status:
        0 iff the pause state change completed successfully, otherwise
        a negative errno value indicating the reason for failure

.. _`resume_state_change_complete`:

resume_state_change_complete
============================

.. c:function:: void resume_state_change_complete(struct visor_device *dev, int status)

    the callback function to be called by a visorbus function driver when a pending "resume device" operation has completed

    :param struct visor_device \*dev:
        struct visor_device identifying the resumed device

    :param int status:
        0 iff the resume state change completed successfully, otherwise
        a negative errno value indicating the reason for failure

.. _`initiate_chipset_device_pause_resume`:

initiate_chipset_device_pause_resume
====================================

.. c:function:: void initiate_chipset_device_pause_resume(struct visor_device *dev, bool is_pause)

    start a pause or resume operation for a visor device

    :param struct visor_device \*dev:
        struct visor_device identifying the device being paused or resumed

    :param bool is_pause:
        true to indicate pause operation, false to indicate resume

.. _`initiate_chipset_device_pause_resume.description`:

Description
-----------

Tell the subordinate function driver for a specific device to pause
or resume that device.  Success/failure result is returned asynchronously
via a callback function; see \ :c:func:`pause_state_change_complete`\  and
\ :c:func:`resume_state_change_complete`\ .

.. _`chipset_device_pause`:

chipset_device_pause
====================

.. c:function:: void chipset_device_pause(struct visor_device *dev_info)

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

.. c:function:: void chipset_device_resume(struct visor_device *dev_info)

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


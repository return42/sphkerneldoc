.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/dc395x.c

.. _`set_safe_settings`:

set_safe_settings
=================

.. c:function:: void set_safe_settings( void)

    if the use_safe_settings option is set then set all values to the safe and slow values.

    :param  void:
        no arguments

.. _`fix_settings`:

fix_settings
============

.. c:function:: void fix_settings( void)

    reset any boot parameters which are out of range back to the default values.

    :param  void:
        no arguments

.. _`eeprom_index_to_delay`:

eeprom_index_to_delay
=====================

.. c:function:: void eeprom_index_to_delay(struct NvRamType *eeprom)

    Take the eeprom delay setting and convert it into a number of seconds.

    :param struct NvRamType \*eeprom:
        The eeprom structure in which we find the delay index to map.

.. _`delay_to_eeprom_index`:

delay_to_eeprom_index
=====================

.. c:function:: int delay_to_eeprom_index(int delay)

    Take a delay in seconds and return the closest eeprom index which will delay for at least that amount of seconds.

    :param int delay:
        The delay, in seconds, to find the eeprom index for.

.. _`eeprom_override`:

eeprom_override
===============

.. c:function:: void eeprom_override(struct NvRamType *eeprom)

    Override the eeprom settings, in the provided eeprom structure, with values that have been set on the command line.

    :param struct NvRamType \*eeprom:
        The eeprom data to override with command line options.

.. _`dc395x_queue_command_lck`:

dc395x_queue_command_lck
========================

.. c:function:: int dc395x_queue_command_lck(struct scsi_cmnd *cmd, void (*) done (struct scsi_cmnd *)

    queue scsi command passed from the mid layer, invoke 'done' on completion

    :param struct scsi_cmnd \*cmd:
        pointer to scsi command object

    :param (void (\*) done (struct scsi_cmnd \*):
        function pointer to be invoked on completion

.. _`dc395x_queue_command_lck.description`:

Description
-----------

Returns 1 if the adapter (host) is busy, else returns 0. One
reason for an adapter to be busy is that the number
of outstanding queued commands is already equal to
struct Scsi_Host::can_queue .

Required: if struct Scsi_Host::can_queue is ever non-zero
then this function is required.

Locks: struct Scsi_Host::host_lock held on entry (with "irqsave")
and is expected to be held on return.

.. _`dc395x_handle_interrupt`:

dc395x_handle_interrupt
=======================

.. c:function:: void dc395x_handle_interrupt(struct AdapterCtlBlk *acb, u16 scsi_status)

    Handle an interrupt that has been confirmed to have been triggered for this card.

    :param struct AdapterCtlBlk \*acb:
        a pointer to the adpter control block

    :param u16 scsi_status:
        the status return when we checked the card

.. _`device_alloc`:

device_alloc
============

.. c:function:: struct DeviceCtlBlk *device_alloc(struct AdapterCtlBlk *acb, u8 target, u8 lun)

    Allocate a new device instance. This create the devices instance and sets up all the data items. The adapter instance is required to obtain confiuration information for this device. This does \*not\* add this device to the adapters device list.

    :param struct AdapterCtlBlk \*acb:
        The adapter to obtain configuration information from.

    :param u8 target:
        The target for the new device.

    :param u8 lun:
        The lun for the new device.

.. _`device_alloc.description`:

Description
-----------

Return the new device if successful or NULL on failure.

.. _`adapter_add_device`:

adapter_add_device
==================

.. c:function:: void adapter_add_device(struct AdapterCtlBlk *acb, struct DeviceCtlBlk *dcb)

    Adds the device instance to the adaptor instance.

    :param struct AdapterCtlBlk \*acb:
        The adapter device to be updated

    :param struct DeviceCtlBlk \*dcb:
        A newly created and initialised device instance to add.

.. _`adapter_remove_device`:

adapter_remove_device
=====================

.. c:function:: void adapter_remove_device(struct AdapterCtlBlk *acb, struct DeviceCtlBlk *dcb)

    Removes the device instance from the adaptor instance. The device instance is not check in any way or freed by this. The caller is expected to take care of that. This will simply remove the device from the adapters data strcutures.

    :param struct AdapterCtlBlk \*acb:
        The adapter device to be updated

    :param struct DeviceCtlBlk \*dcb:
        A device that has previously been added to the adapter.

.. _`adapter_remove_and_free_device`:

adapter_remove_and_free_device
==============================

.. c:function:: void adapter_remove_and_free_device(struct AdapterCtlBlk *acb, struct DeviceCtlBlk *dcb)

    Removes a single device from the adapter and then frees the device information.

    :param struct AdapterCtlBlk \*acb:
        The adapter device to be updated

    :param struct DeviceCtlBlk \*dcb:
        A device that has previously been added to the adapter.

.. _`adapter_remove_and_free_all_devices`:

adapter_remove_and_free_all_devices
===================================

.. c:function:: void adapter_remove_and_free_all_devices(struct AdapterCtlBlk*acb)

    Removes and frees all of the devices associated with the specified adapter.

    :param struct AdapterCtlBlk\*acb:
        The adapter from which all devices should be removed.

.. _`dc395x_slave_alloc`:

dc395x_slave_alloc
==================

.. c:function:: int dc395x_slave_alloc(struct scsi_device *scsi_device)

    Called by the scsi mid layer to tell us about a new scsi device that we need to deal with. We allocate a new device and then insert that device into the adapters device list.

    :param struct scsi_device \*scsi_device:
        The new scsi device that we need to handle.

.. _`dc395x_slave_destroy`:

dc395x_slave_destroy
====================

.. c:function:: void dc395x_slave_destroy(struct scsi_device *scsi_device)

    Called by the scsi mid layer to tell us about a device that is going away.

    :param struct scsi_device \*scsi_device:
        The new scsi device that we need to handle.

.. _`trms1040_wait_30us`:

trms1040_wait_30us
==================

.. c:function:: void trms1040_wait_30us(unsigned long io_port)

    wait for 30 us

    :param unsigned long io_port:
        base I/O address

.. _`trms1040_wait_30us.description`:

Description
-----------

Waits for 30us (using the chip by the looks of it..)

.. _`trms1040_write_cmd`:

trms1040_write_cmd
==================

.. c:function:: void trms1040_write_cmd(unsigned long io_port, u8 cmd, u8 addr)

    write the secified command and address to chip

    :param unsigned long io_port:
        base I/O address

    :param u8 cmd:
        SB + op code (command) to send

    :param u8 addr:
        address to send

.. _`trms1040_set_data`:

trms1040_set_data
=================

.. c:function:: void trms1040_set_data(unsigned long io_port, u8 addr, u8 byte)

    store a single byte in the eeprom

    :param unsigned long io_port:
        base I/O address

    :param u8 addr:
        offset into EEPROM

    :param u8 byte:
        bytes to write

.. _`trms1040_set_data.description`:

Description
-----------

Called from write all to write a single byte into the SSEEPROM
Which is done one bit at a time.

.. _`trms1040_write_all`:

trms1040_write_all
==================

.. c:function:: void trms1040_write_all(struct NvRamType *eeprom, unsigned long io_port)

    write 128 bytes to the eeprom

    :param struct NvRamType \*eeprom:
        the data to write

    :param unsigned long io_port:
        the base io port

.. _`trms1040_write_all.description`:

Description
-----------

Write the supplied 128 bytes to the chips SEEPROM

.. _`trms1040_get_data`:

trms1040_get_data
=================

.. c:function:: u8 trms1040_get_data(unsigned long io_port, u8 addr)

    get a single byte from the eeprom

    :param unsigned long io_port:
        base I/O address

    :param u8 addr:
        offset into SEEPROM

.. _`trms1040_get_data.description`:

Description
-----------

Called from read all to read a single byte into the SSEEPROM
Which is done one bit at a time.

Returns the byte read.

.. _`trms1040_read_all`:

trms1040_read_all
=================

.. c:function:: void trms1040_read_all(struct NvRamType *eeprom, unsigned long io_port)

    read all bytes from the eeprom

    :param struct NvRamType \*eeprom:
        where to store the data

    :param unsigned long io_port:
        the base io port

.. _`trms1040_read_all.description`:

Description
-----------

Read the 128 bytes from the SEEPROM.

.. _`check_eeprom`:

check_eeprom
============

.. c:function:: void check_eeprom(struct NvRamType *eeprom, unsigned long io_port)

    get and check contents of the eeprom

    :param struct NvRamType \*eeprom:
        caller allocated strcuture to read the eeprom data into

    :param unsigned long io_port:
        io port to read from

.. _`check_eeprom.description`:

Description
-----------

Read seeprom 128 bytes into the memory provider in eeprom.
Checks the checksum and if it's not correct it uses a set of default
values.

.. _`print_eeprom_settings`:

print_eeprom_settings
=====================

.. c:function:: void print_eeprom_settings(struct NvRamType *eeprom)

    output the eeprom settings to the kernel log so people can see what they were.

    :param struct NvRamType \*eeprom:
        The eeprom data strucutre to show details for.

.. _`adapter_print_config`:

adapter_print_config
====================

.. c:function:: void adapter_print_config(struct AdapterCtlBlk *acb)

    print adapter connection and termination config

    :param struct AdapterCtlBlk \*acb:
        The adapter to print the information for.

.. _`adapter_print_config.description`:

Description
-----------

The io port in the adapter needs to have been set before calling
this function.

.. _`adapter_init_params`:

adapter_init_params
===================

.. c:function:: void adapter_init_params(struct AdapterCtlBlk *acb)

    Initialize the various parameters in the adapter structure. Note that the pointer to the scsi_host is set early (when this instance is created) and the io_port and irq values are set later after they have been reserved. This just gets everything set to a good starting position.

    :param struct AdapterCtlBlk \*acb:
        The adapter to initialize.

.. _`adapter_init_params.description`:

Description
-----------

The eeprom structure in the adapter needs to have been set before
calling this function.

.. _`adapter_init_scsi_host`:

adapter_init_scsi_host
======================

.. c:function:: void adapter_init_scsi_host(struct Scsi_Host *host)

    Initialize the scsi host instance based on values that we have already stored in the adapter instance. There's some mention that a lot of these are deprecated, so we won't use them (we'll use the ones in the adapter instance) but we'll fill them in in case something else needs them.

    :param struct Scsi_Host \*host:
        The scsi host instance to fill in the values for.

.. _`adapter_init_scsi_host.description`:

Description
-----------

The eeprom structure, irq and io ports in the adapter need to have
been set before calling this function.

.. _`adapter_init_chip`:

adapter_init_chip
=================

.. c:function:: void adapter_init_chip(struct AdapterCtlBlk *acb)

    Get the chip into a know state and figure out some of the settings that apply to this adapter.

    :param struct AdapterCtlBlk \*acb:
        The adapter which we are to init.

.. _`adapter_init_chip.description`:

Description
-----------

The io port in the adapter needs to have been set before calling
this function. The config will be configured correctly on return.

.. _`adapter_init`:

adapter_init
============

.. c:function:: int adapter_init(struct AdapterCtlBlk *acb, unsigned long io_port, u32 io_port_len, unsigned int irq)

    Grab the resource for the card, setup the adapter information, set the card into a known state, create the various tables etc etc. This basically gets all adapter information all up to date, initialised and gets the chip in sync with it.

    :param struct AdapterCtlBlk \*acb:
        *undescribed*

    :param unsigned long io_port:
        The base I/O port

    :param u32 io_port_len:
        *undescribed*

    :param unsigned int irq:
        IRQ

.. _`adapter_init.description`:

Description
-----------

Returns 0 if the initialization succeeds, any other value on
failure.

.. _`adapter_uninit_chip`:

adapter_uninit_chip
===================

.. c:function:: void adapter_uninit_chip(struct AdapterCtlBlk *acb)

    cleanly shut down the scsi controller chip, stopping all operations and disabling interrupt generation on the card.

    :param struct AdapterCtlBlk \*acb:
        The adapter which we are to shutdown.

.. _`adapter_uninit`:

adapter_uninit
==============

.. c:function:: void adapter_uninit(struct AdapterCtlBlk *acb)

    Shut down the chip and release any resources that we had allocated. Once this returns the adapter should not be used anymore.

    :param struct AdapterCtlBlk \*acb:
        The adapter which we are to un-initialize.

.. _`banner_display`:

banner_display
==============

.. c:function:: void banner_display( void)

    Display banner on first instance of driver initialized.

    :param  void:
        no arguments

.. _`dc395x_init_one`:

dc395x_init_one
===============

.. c:function:: int dc395x_init_one(struct pci_dev *dev, const struct pci_device_id *id)

    Initialise a single instance of the adapter.

    :param struct pci_dev \*dev:
        The PCI device to initialize.

    :param const struct pci_device_id \*id:
        Looks like a pointer to the entry in our pci device table
        that was actually matched by the PCI subsystem.

.. _`dc395x_init_one.description`:

Description
-----------

The PCI layer will call this once for each instance of the adapter
that it finds in the system. The pci_dev strcuture indicates which
instance we are being called from.

Returns 0 on success, or an error code (-ve) on failure.

.. _`dc395x_remove_one`:

dc395x_remove_one
=================

.. c:function:: void dc395x_remove_one(struct pci_dev *dev)

    Called to remove a single instance of the adapter.

    :param struct pci_dev \*dev:
        The PCI device to initialize.

.. _`dc395x_module_init`:

dc395x_module_init
==================

.. c:function:: int dc395x_module_init( void)

    Module initialization function

    :param  void:
        no arguments

.. _`dc395x_module_init.description`:

Description
-----------

Used by both module and built-in driver to initialise this driver.

.. _`dc395x_module_exit`:

dc395x_module_exit
==================

.. c:function:: void __exit dc395x_module_exit( void)

    Module cleanup function.

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-

=========
drivers.c
=========


.. _`comedi_set_hw_dev`:

comedi_set_hw_dev
=================

.. c:function:: int comedi_set_hw_dev (struct comedi_device *dev, struct device *hw_dev)

    Set hardware device associated with COMEDI device

    :param struct comedi_device \*dev:
        COMEDI device.

    :param struct device \*hw_dev:
        Hardware device.



.. _`comedi_set_hw_dev.description`:

Description
-----------

For automatically configured COMEDI devices (resulting from a call to
:c:func:`comedi_auto_config` or one of its wrappers from the low-level COMEDI
driver), :c:func:`comedi_set_hw_dev` is called automatically by the COMEDI core
to associate the COMEDI device with the hardware device.  It can also be
called directly by "legacy" low-level COMEDI drivers that rely on the
``COMEDI_DEVCONFIG`` ioctl to configure the hardware as long as the hardware
has a :c:type:`struct device <device>`.

If ``dev``\ ->hw_dev is NULL, it gets a reference to ``hw_dev`` and sets
``dev``\ ->hw_dev, otherwise, it does nothing.  Calling it multiple times
with the same hardware device is not considered an error.  If it gets
a reference to the hardware device, it will be automatically 'put' when
the device is detached from COMEDI.

Returns 0 if ``dev``\ ->hw_dev was NULL or the same as ``hw_dev``\ , otherwise
returns -EEXIST.



.. _`comedi_alloc_devpriv`:

comedi_alloc_devpriv
====================

.. c:function:: void *comedi_alloc_devpriv (struct comedi_device *dev, size_t size)

    Allocate memory for the device private data

    :param struct comedi_device \*dev:
        COMEDI device.

    :param size_t size:
        Size of the memory to allocate.



.. _`comedi_alloc_devpriv.description`:

Description
-----------

The allocated memory is zero-filled.  ``dev``\ ->private points to it on
return.  The memory will be automatically freed when the COMEDI device is
"detached".

Returns a pointer to the allocated memory, or NULL on failure.



.. _`comedi_alloc_subdevices`:

comedi_alloc_subdevices
=======================

.. c:function:: int comedi_alloc_subdevices (struct comedi_device *dev, int num_subdevices)

    Allocate subdevices for COMEDI device

    :param struct comedi_device \*dev:
        COMEDI device.

    :param int num_subdevices:
        Number of subdevices to allocate.



.. _`comedi_alloc_subdevices.description`:

Description
-----------

Allocates and initializes an array of :c:type:`struct comedi_subdevice <comedi_subdevice>` for the
COMEDI device.  If successful, sets ``dev``\ ->subdevices to point to the
first one and ``dev``\ ->n_subdevices to the number.

Returns 0 on success, -EINVAL if ``num_subdevices`` is < 1, or -ENOMEM if
failed to allocate the memory.



.. _`comedi_alloc_subdev_readback`:

comedi_alloc_subdev_readback
============================

.. c:function:: int comedi_alloc_subdev_readback (struct comedi_subdevice *s)

    Allocate memory for the subdevice readback

    :param struct comedi_subdevice \*s:
        COMEDI subdevice.



.. _`comedi_alloc_subdev_readback.description`:

Description
-----------

This is called by low-level COMEDI drivers to allocate an array to record
the last values written to a subdevice's analog output channels (at least
by the ``INSN_WRITE`` instruction), to allow them to be read back by an
``INSN_READ`` instruction.  It also provides a default handler for the
``INSN_READ`` instruction unless one has already been set.

On success, ``s``\ ->readback points to the first element of the array, which
is zero-filled.  The low-level driver is responsible for updating its
contents.  ``s``\ ->insn_read will be set to :c:func:`comedi_readback_insn_read`
unless it is already non-NULL.

Returns 0 on success, -EINVAL if the subdevice has no channels, or
-ENOMEM on allocation failure.



.. _`comedi_readback_insn_read`:

comedi_readback_insn_read
=========================

.. c:function:: int comedi_readback_insn_read (struct comedi_device *dev, struct comedi_subdevice *s, struct comedi_insn *insn, unsigned int *data)

    A generic (\*insn_read) for subdevice readback.

    :param struct comedi_device \*dev:
        COMEDI device.

    :param struct comedi_subdevice \*s:
        COMEDI subdevice.

    :param struct comedi_insn \*insn:
        COMEDI instruction.

    :param unsigned int \*data:
        Pointer to return the readback data.



.. _`comedi_readback_insn_read.description`:

Description
-----------

Handles the ``INSN_READ`` instruction for subdevices that use the readback
array allocated by :c:func:`comedi_alloc_subdev_readback`.  It may be used
directly as the subdevice's handler (\ ``s``\ ->insn_read) or called via a
wrapper.

``insn``\ ->n is normally 1, which will read a single value.  If higher, the
same element of the readback array will be read multiple times.

Returns ``insn``\ ->n on success, or -EINVAL if ``s``\ ->readback is NULL.



.. _`comedi_timeout`:

comedi_timeout
==============

.. c:function:: int comedi_timeout (struct comedi_device *dev, struct comedi_subdevice *s, struct comedi_insn *insn, int (*cb) (struct comedi_device *dev, struct comedi_subdevice *s, struct comedi_insn *insn, unsigned long context, unsigned long context)

    Busy-wait for a driver condition to occur

    :param struct comedi_device \*dev:
        COMEDI device.

    :param struct comedi_subdevice \*s:
        COMEDI subdevice.

    :param struct comedi_insn \*insn:
        COMEDI instruction.

    :param int (\*cb) (struct comedi_device \*dev, struct comedi_subdevice \*s, struct comedi_insn \*insn, unsigned long context):
        Callback to check for the condition.

    :param unsigned long context:
        Private context from the driver.



.. _`comedi_timeout.description`:

Description
-----------

Busy-waits for up to a second (\ ``COMEDI_TIMEOUT_MS``\ ) for the condition or
some error (other than -EBUSY) to occur.  The parameters ``dev``\ , ``s``\ , ``insn``\ ,
and ``context`` are passed to the callback function, which returns -EBUSY to
continue waiting or some other value to stop waiting (generally 0 if the
condition occurred, or some error value).

Returns -ETIMEDOUT if timed out, otherwise the return value from the
callback function.



.. _`comedi_dio_insn_config`:

comedi_dio_insn_config
======================

.. c:function:: int comedi_dio_insn_config (struct comedi_device *dev, struct comedi_subdevice *s, struct comedi_insn *insn, unsigned int *data, unsigned int mask)

    Boilerplate (\*insn_config) for DIO subdevices

    :param struct comedi_device \*dev:
        COMEDI device.

    :param struct comedi_subdevice \*s:
        COMEDI subdevice.

    :param struct comedi_insn \*insn:
        COMEDI instruction.

    :param unsigned int \*data:
        Instruction parameters and return data.

    :param unsigned int mask:
        io_bits mask for grouped channels, or 0 for single channel.



.. _`comedi_dio_insn_config.description`:

Description
-----------

If ``mask`` is 0, it is replaced with a single-bit mask corresponding to the
channel number specified by ``insn``\ ->chanspec.  Otherwise, ``mask``
corresponds to a group of channels (which should include the specified
channel) that are always configured together as inputs or outputs.

Partially handles the ``INSN_CONFIG_DIO_INPUT``\ , ``INSN_CONFIG_DIO_OUTPUTS``\ ,
and ``INSN_CONFIG_DIO_QUERY`` instructions.  The first two update
``s``\ ->io_bits to record the directions of the masked channels.  The last
one sets ``data``\ [1] to the current direction of the group of channels
(\ ``COMEDI_INPUT``\ ) or ``COMEDI_OUTPUT``\ ) as recorded in ``s``\ ->io_bits.

The caller is responsible for updating the DIO direction in the hardware
registers if this function returns 0.

Returns 0 for a ``INSN_CONFIG_DIO_INPUT`` or ``INSN_CONFIG_DIO_OUTPUT``
instruction, ``insn``\ ->n (> 0) for a ``INSN_CONFIG_DIO_QUERY`` instruction, or
-EINVAL for some other instruction.



.. _`comedi_dio_update_state`:

comedi_dio_update_state
=======================

.. c:function:: unsigned int comedi_dio_update_state (struct comedi_subdevice *s, unsigned int *data)

    Update the internal state of DIO subdevices

    :param struct comedi_subdevice \*s:
        COMEDI subdevice.

    :param unsigned int \*data:
        The channel mask and bits to update.



.. _`comedi_dio_update_state.description`:

Description
-----------

Updates ``s``\ ->state which holds the internal state of the outputs for DIO
or DO subdevices (up to 32 channels).  ``data``\ [0] contains a bit-mask of
the channels to be updated.  ``data``\ [1] contains a bit-mask of those
channels to be set to '1'.  The caller is responsible for updating the
outputs in hardware according to ``s``\ ->state.  As a minimum, the channels
in the returned bit-mask need to be updated.

Returns ``mask`` with non-existent channels removed.



.. _`comedi_bytes_per_scan`:

comedi_bytes_per_scan
=====================

.. c:function:: unsigned int comedi_bytes_per_scan (struct comedi_subdevice *s)

    Get length of asynchronous command "scan" in bytes

    :param struct comedi_subdevice \*s:
        COMEDI subdevice.



.. _`comedi_bytes_per_scan.description`:

Description
-----------

Determines the overall scan length according to the subdevice type and the
number of channels in the scan.

For digital input, output or input/output subdevices, samples for
multiple channels are assumed to be packed into one or more unsigned
short or unsigned int values according to the subdevice's ``SDF_LSAMPL``
flag.  For other types of subdevice, samples are assumed to occupy a
whole unsigned short or unsigned int according to the ``SDF_LSAMPL`` flag.

Returns the overall scan length in bytes.



.. _`comedi_nscans_left`:

comedi_nscans_left
==================

.. c:function:: unsigned int comedi_nscans_left (struct comedi_subdevice *s, unsigned int nscans)

    Return the number of scans left in the command

    :param struct comedi_subdevice \*s:
        COMEDI subdevice.

    :param unsigned int nscans:
        The expected number of scans or 0 for all available scans.



.. _`comedi_nscans_left.description`:

Description
-----------

If ``nscans`` is 0, it is set to the number of scans available in the
async buffer.

If the async command has a stop_src of ``TRIG_COUNT``\ , the ``nscans`` will be
checked against the number of scans remaining to complete the command.

The return value will then be either the expected number of scans or the
number of scans remaining to complete the command, whichever is fewer.



.. _`comedi_nsamples_left`:

comedi_nsamples_left
====================

.. c:function:: unsigned int comedi_nsamples_left (struct comedi_subdevice *s, unsigned int nsamples)

    Return the number of samples left in the command

    :param struct comedi_subdevice \*s:
        COMEDI subdevice.

    :param unsigned int nsamples:
        The expected number of samples.



.. _`comedi_nsamples_left.description`:

Description
-----------

Returns the number of samples remaining to complete the command, or the
specified expected number of samples (\ ``nsamples``\ ), whichever is fewer.



.. _`comedi_inc_scan_progress`:

comedi_inc_scan_progress
========================

.. c:function:: void comedi_inc_scan_progress (struct comedi_subdevice *s, unsigned int num_bytes)

    Update scan progress in asynchronous command

    :param struct comedi_subdevice \*s:
        COMEDI subdevice.

    :param unsigned int num_bytes:
        Amount of data in bytes to increment scan progress.



.. _`comedi_inc_scan_progress.description`:

Description
-----------

Increments the scan progress by the number of bytes specified by ``num_bytes``\ .
If the scan progress reaches or exceeds the scan length in bytes, reduce
it modulo the scan length in bytes and set the "end of scan" asynchronous
event flag (\ ``COMEDI_CB_EOS``\ ) to be processed later.



.. _`comedi_handle_events`:

comedi_handle_events
====================

.. c:function:: unsigned int comedi_handle_events (struct comedi_device *dev, struct comedi_subdevice *s)

    Handle events and possibly stop acquisition

    :param struct comedi_device \*dev:
        COMEDI device.

    :param struct comedi_subdevice \*s:
        COMEDI subdevice.



.. _`comedi_handle_events.description`:

Description
-----------

Handles outstanding asynchronous acquisition event flags associated
with the subdevice.  Call the subdevice's ``s``\ ->:c:func:`cancel` handler if the
"end of acquisition", "error" or "overflow" event flags are set in order
to stop the acquisition at the driver level.

Calls :c:func:`comedi_event` to further process the event flags, which may mark
the asynchronous command as no longer running, possibly terminated with
an error, and may wake up tasks.

Return a bit-mask of the handled events.



.. _`comedi_load_firmware`:

comedi_load_firmware
====================

.. c:function:: int comedi_load_firmware (struct comedi_device *dev, struct device *device, const char *name, int (*cb) (struct comedi_device *dev, const u8 *data, size_t size, unsigned long context, unsigned long context)

    Request and load firmware for a device

    :param struct comedi_device \*dev:
        COMEDI device.

    :param struct device \*device:
        Hardware device.

    :param const char \*name:
        The name of the firmware image.

    :param int (\*cb) (struct comedi_device \*dev, const u8 \*data, size_t size, unsigned long context):
        Callback to the upload the firmware image.

    :param unsigned long context:
        Private context from the driver.



.. _`comedi_load_firmware.description`:

Description
-----------

Sends a firmware request for the hardware device and waits for it.  Calls
the callback function to upload the firmware to the device, them releases
the firmware.

Returns 0 on success, -EINVAL if ``cb`` is NULL, or a negative error number
from the firmware request or the callback function.



.. _`__comedi_request_region`:

__comedi_request_region
=======================

.. c:function:: int __comedi_request_region (struct comedi_device *dev, unsigned long start, unsigned long len)

    Request an I/O region for a legacy driver

    :param struct comedi_device \*dev:
        COMEDI device.

    :param unsigned long start:
        Base address of the I/O region.

    :param unsigned long len:
        Length of the I/O region.



.. _`__comedi_request_region.description`:

Description
-----------

Requests the specified I/O port region which must start at a non-zero
address.

Returns 0 on success, -EINVAL if ``start`` is 0, or -EIO if the request
fails.



.. _`comedi_request_region`:

comedi_request_region
=====================

.. c:function:: int comedi_request_region (struct comedi_device *dev, unsigned long start, unsigned long len)

    Request an I/O region for a legacy driver

    :param struct comedi_device \*dev:
        COMEDI device.

    :param unsigned long start:
        Base address of the I/O region.

    :param unsigned long len:
        Length of the I/O region.



.. _`comedi_request_region.description`:

Description
-----------

Requests the specified I/O port region which must start at a non-zero
address.

On success, ``dev``\ ->iobase is set to the base address of the region and
``dev``\ ->iolen is set to its length.

Returns 0 on success, -EINVAL if ``start`` is 0, or -EIO if the request
fails.



.. _`comedi_legacy_detach`:

comedi_legacy_detach
====================

.. c:function:: void comedi_legacy_detach (struct comedi_device *dev)

    A generic (\*detach) function for legacy drivers

    :param struct comedi_device \*dev:
        COMEDI device.



.. _`comedi_legacy_detach.description`:

Description
-----------

This is a simple, generic 'detach' handler for legacy COMEDI devices that
just use a single I/O port region and possibly an IRQ and that don't need
any special clean-up for their private device or subdevice storage.  It
can also be called by a driver-specific 'detach' handler.

If ``dev``\ ->irq is non-zero, the IRQ will be freed.  If ``dev``\ ->iobase and
``dev``\ ->iolen are both non-zero, the I/O port region will be released.



.. _`comedi_auto_config`:

comedi_auto_config
==================

.. c:function:: int comedi_auto_config (struct device *hardware_device, struct comedi_driver *driver, unsigned long context)

    Create a COMEDI device for a hardware device

    :param struct device \*hardware_device:
        Hardware device.

    :param struct comedi_driver \*driver:
        COMEDI low-level driver for the hardware device.

    :param unsigned long context:
        Driver context for the auto_attach handler.



.. _`comedi_auto_config.description`:

Description
-----------

Allocates a new COMEDI device for the hardware device and calls the
low-level driver's 'auto_attach' handler to set-up the hardware and
allocate the COMEDI subdevices.  Additional "post-configuration" setting
up is performed on successful return from the 'auto_attach' handler.
If the 'auto_attach' handler fails, the low-level driver's 'detach'
handler will be called as part of the clean-up.

This is usually called from a wrapper function in a bus-specific COMEDI
module, which in turn is usually called from a bus device 'probe'
function in the low-level driver.

Returns 0 on success, -EINVAL if the parameters are invalid or the
post-configuration determines the driver has set the COMEDI device up
incorrectly, -ENOMEM if failed to allocate memory, -EBUSY if run out of
COMEDI minor device numbers, or some negative error number returned by
the driver's 'auto_attach' handler.



.. _`comedi_auto_unconfig`:

comedi_auto_unconfig
====================

.. c:function:: void comedi_auto_unconfig (struct device *hardware_device)

    Unconfigure auto-allocated COMEDI device

    :param struct device \*hardware_device:
        Hardware device previously passed to
        :c:func:`comedi_auto_config`.



.. _`comedi_auto_unconfig.description`:

Description
-----------

Cleans up and eventually destroys the COMEDI device allocated by
:c:func:`comedi_auto_config` for the same hardware device.  As part of this
clean-up, the low-level COMEDI driver's 'detach' handler will be called.
(The COMEDI device itself will persist in an unattached state if it is
still open, until it is released, and any mmapped buffers will persist
until they are munmapped.)

This is usually called from a wrapper module in a bus-specific COMEDI
module, which in turn is usually set as the bus device 'remove' function
in the low-level COMEDI driver.



.. _`comedi_driver_register`:

comedi_driver_register
======================

.. c:function:: int comedi_driver_register (struct comedi_driver *driver)

    Register a low-level COMEDI driver

    :param struct comedi_driver \*driver:
        Low-level COMEDI driver.



.. _`comedi_driver_register.description`:

Description
-----------

The low-level COMEDI driver is added to the list of registered COMEDI
drivers.  This is used by the handler for the "/proc/comedi" file and is
also used by the handler for the ``COMEDI_DEVCONFIG`` ioctl to configure
"legacy" COMEDI devices (for those low-level drivers that support it).

Returns 0.



.. _`comedi_driver_unregister`:

comedi_driver_unregister
========================

.. c:function:: void comedi_driver_unregister (struct comedi_driver *driver)

    Unregister a low-level COMEDI driver

    :param struct comedi_driver \*driver:
        Low-level COMEDI driver.



.. _`comedi_driver_unregister.description`:

Description
-----------

The low-level COMEDI driver is removed from the list of registered COMEDI
drivers.  Detaches any COMEDI devices attached to the driver, which will
result in the low-level driver's 'detach' handler being called for those
devices before this function returns.


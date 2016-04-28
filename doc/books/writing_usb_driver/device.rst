.. -*- coding: utf-8; mode: rst -*-

.. _device:

================
Device operation
================

When a device is plugged into the USB bus that matches the device ID
pattern that your driver registered with the USB core, the probe
function is called. The usb_device structure, interface number and the
interface ID are passed to the function:


.. code-block:: c

    static int skel_probe(struct usb_interface *interface,
        const struct usb_device_id *id)

The driver now needs to verify that this device is actually one that it
can accept. If so, it returns 0. If not, or if any error occurs during
initialization, an errorcode (such as ``-ENOMEM`` or ``-ENODEV``) is
returned from the probe function.

In the skeleton driver, we determine what end points are marked as
bulk-in and bulk-out. We create buffers to hold the data that will be
sent and received from the device, and a USB urb to write data to the
device is initialized.

Conversely, when the device is removed from the USB bus, the disconnect
function is called with the device pointer. The driver needs to clean
any private data that has been allocated at this time and to shut down
any pending urbs that are in the USB system.

Now that the device is plugged into the system and the driver is bound
to the device, any of the functions in the file_operations structure
that were passed to the USB subsystem will be called from a user program
trying to talk to the device. The first function called will be open, as
the program tries to open the device for I/O. We increment our private
usage count and save a pointer to our internal structure in the file
structure. This is done so that future calls to file operations will
enable the driver to determine which device the user is addressing. All
of this is done with the following code:


.. code-block:: c

    /* increment our usage count for the module */
    ++skel->open_count;

    /* save our object in the file's private structure */
    file->private_data = dev;

After the open function is called, the read and write functions are
called to receive and send data to the device. In the skel_write
function, we receive a pointer to some data that the user wants to send
to the device and the size of the data. The function determines how much
data it can send to the device based on the size of the write urb it has
created (this size depends on the size of the bulk out end point that
the device has). Then it copies the data from user space to kernel
space, points the urb to the data and submits the urb to the USB
subsystem. This can be seen in the following code:


.. code-block:: c

    /* we can only write as much as 1 urb will hold */
    bytes_written = (count > skel->bulk_out_size) ? skel->bulk_out_size : count;

    /* copy the data from user space into our urb */
    copy_from_user(skel->write_urb->transfer_buffer, buffer, bytes_written);

    /* set up our urb */
    usb_fill_bulk_urb(skel->write_urb,
                      skel->dev,
                      usb_sndbulkpipe(skel->dev, skel->bulk_out_endpointAddr),
                      skel->write_urb->transfer_buffer,
                      bytes_written,
                      skel_write_bulk_callback,
                      skel);

    /* send the data out the bulk port */
    result = usb_submit_urb(skel->write_urb);
    if (result) {
            err("Failed submitting write urb, error %d", result);
    }

When the write urb is filled up with the proper information using the
usb_fill_bulk_urb function, we point the urb's completion callback to
call our own skel_write_bulk_callback function. This function is
called when the urb is finished by the USB subsystem. The callback
function is called in interrupt context, so caution must be taken not to
do very much processing at that time. Our implementation of
skel_write_bulk_callback merely reports if the urb was completed
successfully or not and then returns.

The read function works a bit differently from the write function in
that we do not use an urb to transfer data from the device to the
driver. Instead we call the usb_bulk_msg function, which can be used
to send or receive data from a device without having to create urbs and
handle urb completion callback functions. We call the usb_bulk_msg
function, giving it a buffer into which to place any data received from
the device and a timeout value. If the timeout period expires without
receiving any data from the device, the function will fail and return an
error message. This can be shown with the following code:


.. code-block:: c

    /* do an immediate bulk read to get data from the device */
    retval = usb_bulk_msg (skel->dev,
                           usb_rcvbulkpipe (skel->dev,
                           skel->bulk_in_endpointAddr),
                           skel->bulk_in_buffer,
                           skel->bulk_in_size,
                           &count, HZ*10);
    /* if the read was successful, copy the data to user space */
    if (!retval) {
            if (copy_to_user (buffer, skel->bulk_in_buffer, count))
                    retval = -EFAULT;
            else
                    retval = count;
    }

The usb_bulk_msg function can be very useful for doing single reads or
writes to a device; however, if you need to read or write constantly to
a device, it is recommended to set up your own urbs and submit them to
the USB subsystem.

When the user program releases the file handle that it has been using to
talk to the device, the release function in the driver is called. In
this function we decrement our private usage count and wait for possible
pending writes:


.. code-block:: c

    /* decrement our usage count for the device */
    --skel->open_count;

One of the more difficult problems that USB drivers must be able to
handle smoothly is the fact that the USB device may be removed from the
system at any point in time, even if a program is currently talking to
it. It needs to be able to shut down any current reads and writes and
notify the user-space programs that the device is no longer there. The
following code (function ``skel_delete``) is an example of how to do
this:


.. code-block:: c

    static inline void skel_delete (struct usb_skel *dev)
    {
        kfree (dev->bulk_in_buffer);
        if (dev->bulk_out_buffer != NULL)
            usb_free_coherent (dev->udev, dev->bulk_out_size,
                dev->bulk_out_buffer,
                dev->write_urb->transfer_dma);
        usb_free_urb (dev->write_urb);
        kfree (dev);
    }

If a program currently has an open handle to the device, we reset the
flag ``device_present``. For every read, write, release and other
functions that expect a device to be present, the driver first checks
this flag to see if the device is still present. If not, it releases
that the device has disappeared, and a -ENODEV error is returned to the
user-space program. When the release function is eventually called, it
determines if there is no device and if not, it does the cleanup that
the skel_disconnect function normally does if there are no open files
on the device (see Listing 5).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------

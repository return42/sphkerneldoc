.. -*- coding: utf-8; mode: rst -*-

.. _uio_hv_generic:

**************************
Generic Hyper-V UIO driver
**************************

The generic driver is a kernel module named uio_hv_generic. It
supports devices on the Hyper-V VMBus similar to uio_pci_generic on
PCI bus.


.. _uio_hv_generic_binding:

Making the driver recognize the device
======================================

Since the driver does not declare any device GUID's, it will not get
loaded automatically and will not automatically bind to any devices, you
must load it and allocate id to the driver yourself. For example, to use
the network device GUID:


.. code-block:: c

     modprobe uio_hv_generic
     echo "f8615163-df3e-46c5-913f-f2d2f965ed0e" > /sys/bus/vmbus/drivers/uio_hv_generic/new_id

If there already is a hardware specific kernel driver for the device,
the generic driver still won't bind to it, in this case if you want to
use the generic driver (why would you?) you'll have to manually unbind
the hardware specific driver and bind the generic driver, like this:


.. code-block:: c

          echo -n vmbus-ed963694-e847-4b2a-85af-bc9cfc11d6f3 > /sys/bus/vmbus/drivers/hv_netvsc/unbind
          echo -n vmbus-ed963694-e847-4b2a-85af-bc9cfc11d6f3 > /sys/bus/vmbus/drivers/uio_hv_generic/bind

You can verify that the device has been bound to the driver by looking
for it in sysfs, for example like the following:


.. code-block:: c

        ls -l /sys/bus/vmbus/devices/vmbus-ed963694-e847-4b2a-85af-bc9cfc11d6f3/driver

Which if successful should print


.. code-block:: c

      .../vmbus-ed963694-e847-4b2a-85af-bc9cfc11d6f3/driver -> ../../../bus/vmbus/drivers/uio_hv_generic


.. _uio_hv_generic_internals:

Things to know about uio_hv_generic
===================================

On each interrupt, uio_hv_generic sets the Interrupt Disable bit. This
prevents the device from generating further interrupts until the bit is
cleared. The userspace driver should clear this bit before blocking and
waiting for more interrupts.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------

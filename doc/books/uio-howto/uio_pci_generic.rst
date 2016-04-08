
.. _uio_pci_generic:

======================
Generic PCI UIO driver
======================

The generic driver is a kernel module named uio_pci_generic. It can work with any device compliant to PCI 2.3 (circa 2002) and any compliant PCI Express device. Using this, you
only need to write the userspace driver, removing the need to write a hardware-specific kernel module.


.. _uio_pci_generic_binding:

Making the driver recognize the device
======================================

Since the driver does not declare any device ids, it will not get loaded automatically and will not automatically bind to any devices, you must load it and allocate id to the
driver yourself. For example:


.. code-block:: c

     modprobe uio_pci_generic
     echo "8086 10f5" > /sys/bus/pci/drivers/uio_pci_generic/new_id

If there already is a hardware specific kernel driver for your device, the generic driver still won't bind to it, in this case if you want to use the generic driver (why would
you?) you'll have to manually unbind the hardware specific driver and bind the generic driver, like this:


.. code-block:: c

        echo -n 0000:00:19.0 > /sys/bus/pci/drivers/e1000e/unbind
        echo -n 0000:00:19.0 > /sys/bus/pci/drivers/uio_pci_generic/bind

You can verify that the device has been bound to the driver by looking for it in sysfs, for example like the following:


.. code-block:: c

        ls -l /sys/bus/pci/devices/0000:00:19.0/driver

Which if successful should print


.. code-block:: c

      .../0000:00:19.0/driver -> ../../../bus/pci/drivers/uio_pci_generic

Note that the generic driver will not bind to old PCI 2.2 devices. If binding the device failed, run the following command:


.. code-block:: c

      dmesg

and look in the output for failure reasons


.. _uio_pci_generic_internals:

Things to know about uio_pci_generic
====================================

Interrupts are handled using the Interrupt Disable bit in the PCI command register and Interrupt Status bit in the PCI status register. All devices compliant to PCI 2.3 (circa
2002) and all compliant PCI Express devices should support these bits. uio_pci_generic detects this support, and won't bind to devices which do not support the Interrupt Disable
Bit in the command register.

On each interrupt, uio_pci_generic sets the Interrupt Disable bit. This prevents the device from generating further interrupts until the bit is cleared. The userspace driver
should clear this bit before blocking and waiting for more interrupts.


.. _uio_pci_generic_userspace:

Writing userspace driver using uio_pci_generic
==============================================

Userspace driver can use pci sysfs interface, or the libpci libray that wraps it, to talk to the device and to re-enable interrupts by writing to the command register.


.. _uio_pci_generic_example:

Example code using uio_pci_generic
==================================

Here is some sample userspace driver code using uio_pci_generic:


.. code-block:: c

    #include <stdlib.h>
    #include <stdio.h>
    #include <unistd.h>
    #include <sys/types.h>
    #include <sys/stat.h>
    #include <fcntl.h>
    #include <errno.h>

    int main()
    {
        int uiofd;
        int configfd;
        int err;
        int i;
        unsigned icount;
        unsigned char command_high;

        uiofd = open("/dev/uio0", O_RDONLY);
        if (uiofd < 0) {
            perror("uio open:");
            return errno;
        }
        configfd = open("/sys/class/uio/uio0/device/config", O_RDWR);
        if (configfd < 0) {
            perror("config open:");
            return errno;
        }

        /* Read and cache command value */
        err = pread(configfd, &command_high, 1, 5);
        if (err != 1) {
            perror("command config read:");
            return errno;
        }
        command_high &= ~0x4;

        for(i = 0;; ++i) {
            /* Print out a message, for debugging. */
            if (i == 0)
                fprintf(stderr, "Started uio test driver.\\n");
            else
                fprintf(stderr, "Interrupts: %d\\n", icount);

            /****************************************/
            /* Here we got an interrupt from the
               device. Do something to it. */
            /****************************************/

            /* Re-enable interrupts. */
            err = pwrite(configfd, &command_high, 1, 5);
            if (err != 1) {
                perror("config write:");
                break;
            }

            /* Wait for next interrupt. */
            err = read(uiofd, &icount, 4);
            if (err != 4) {
                perror("uio read:");
                break;
            }

        }
        return errno;
    }



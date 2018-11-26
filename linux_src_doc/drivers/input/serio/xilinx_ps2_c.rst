.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/serio/xilinx_ps2.c

.. _`xps2_recv`:

xps2_recv
=========

.. c:function:: int xps2_recv(struct xps2data *drvdata, u8 *byte)

    attempts to receive a byte from the PS/2 port.

    :param drvdata:
        pointer to ps2 device private data structure
    :type drvdata: struct xps2data \*

    :param byte:
        address where the read data will be copied
    :type byte: u8 \*

.. _`xps2_recv.description`:

Description
-----------

If there is any data available in the PS/2 receiver, this functions reads
the data, otherwise it returns error.

.. _`sxps2_write`:

sxps2_write
===========

.. c:function:: int sxps2_write(struct serio *pserio, unsigned char c)

    sends a byte out through the PS/2 port.

    :param pserio:
        pointer to the serio structure of the PS/2 port
    :type pserio: struct serio \*

    :param c:
        data that needs to be written to the PS/2 port
    :type c: unsigned char

.. _`sxps2_write.description`:

Description
-----------

This function checks if the PS/2 transmitter is empty and sends a byte.
Otherwise it returns error. Transmission fails only when nothing is connected
to the PS/2 port. Thats why, we do not try to resend the data in case of a
failure.

.. _`sxps2_open`:

sxps2_open
==========

.. c:function:: int sxps2_open(struct serio *pserio)

    called when a port is opened by the higher layer.

    :param pserio:
        pointer to the serio structure of the PS/2 device
    :type pserio: struct serio \*

.. _`sxps2_open.description`:

Description
-----------

This function requests irq and enables interrupts for the PS/2 device.

.. _`sxps2_close`:

sxps2_close
===========

.. c:function:: void sxps2_close(struct serio *pserio)

    frees the interrupt.

    :param pserio:
        pointer to the serio structure of the PS/2 device
    :type pserio: struct serio \*

.. _`sxps2_close.description`:

Description
-----------

This function frees the irq and disables interrupts for the PS/2 device.

.. _`xps2_of_probe`:

xps2_of_probe
=============

.. c:function:: int xps2_of_probe(struct platform_device *ofdev)

    probe method for the PS/2 device.

    :param ofdev:
        *undescribed*
    :type ofdev: struct platform_device \*

.. _`xps2_of_probe.description`:

Description
-----------

This function probes the PS/2 device in the device tree.
It initializes the driver data structure and the hardware.
It returns 0, if the driver is bound to the PS/2 device, or a negative
value if there is an error.

.. _`xps2_of_remove`:

xps2_of_remove
==============

.. c:function:: int xps2_of_remove(struct platform_device *of_dev)

    unbinds the driver from the PS/2 device.

    :param of_dev:
        pointer to OF device structure
    :type of_dev: struct platform_device \*

.. _`xps2_of_remove.description`:

Description
-----------

This function is called if a device is physically removed from the system or
if the driver module is being unloaded. It frees any resources allocated to
the device.

.. This file was automatic generated / don't edit.


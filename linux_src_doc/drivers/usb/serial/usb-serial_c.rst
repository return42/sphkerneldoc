.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/serial/usb-serial.c

.. _`serial_install`:

serial_install
==============

.. c:function:: int serial_install(struct tty_driver *driver, struct tty_struct *tty)

    install tty

    :param driver:
        the driver (USB in our case)
    :type driver: struct tty_driver \*

    :param tty:
        the tty being created
    :type tty: struct tty_struct \*

.. _`serial_install.description`:

Description
-----------

Create the termios objects for this tty.  We use the default
USB serial settings but permit them to be overridden by
serial->type->init_termios.

This is the first place a new tty gets used.  Hence this is where we
acquire references to the usb_serial structure and the driver module,
where we store a pointer to the port, and where we do an autoresume.
All these actions are reversed in \ :c:func:`serial_cleanup`\ .

.. _`serial_port_shutdown`:

serial_port_shutdown
====================

.. c:function:: void serial_port_shutdown(struct tty_port *tport)

    shut down hardware

    :param tport:
        tty port to shut down
    :type tport: struct tty_port \*

.. _`serial_port_shutdown.description`:

Description
-----------

Shut down a USB serial port. Serialized against activate by the
tport mutex and kept to matching open/close pairs
of calls by the initialized flag.

Not called if tty is console.

.. _`serial_cleanup`:

serial_cleanup
==============

.. c:function:: void serial_cleanup(struct tty_struct *tty)

    free resources post close/hangup

    :param tty:
        *undescribed*
    :type tty: struct tty_struct \*

.. _`serial_cleanup.description`:

Description
-----------

Do the resource freeing and refcount dropping for the port.
Avoid freeing the console.

Called asynchronously after the last tty kref is dropped.

.. _`usb_serial_register_drivers`:

usb_serial_register_drivers
===========================

.. c:function:: int usb_serial_register_drivers(struct usb_serial_driver *const serial_drivers, const char *name, const struct usb_device_id *id_table)

    register drivers for a usb-serial module

    :param serial_drivers:
        NULL-terminated array of pointers to drivers to be registered
    :type serial_drivers: struct usb_serial_driver \*const

    :param name:
        name of the usb_driver for this set of \ ``serial_drivers``\ 
    :type name: const char \*

    :param id_table:
        list of all devices this \ ``serial_drivers``\  set binds to
    :type id_table: const struct usb_device_id \*

.. _`usb_serial_register_drivers.description`:

Description
-----------

Registers all the drivers in the \ ``serial_drivers``\  array, and dynamically
creates a struct usb_driver with the name \ ``name``\  and id_table of \ ``id_table``\ .

.. _`usb_serial_deregister_drivers`:

usb_serial_deregister_drivers
=============================

.. c:function:: void usb_serial_deregister_drivers(struct usb_serial_driver *const serial_drivers)

    deregister drivers for a usb-serial module

    :param serial_drivers:
        NULL-terminated array of pointers to drivers to be deregistered
    :type serial_drivers: struct usb_serial_driver \*const

.. _`usb_serial_deregister_drivers.description`:

Description
-----------

Deregisters all the drivers in the \ ``serial_drivers``\  array and deregisters and
frees the struct usb_driver that was created by the call to
\ :c:func:`usb_serial_register_drivers`\ .

.. This file was automatic generated / don't edit.


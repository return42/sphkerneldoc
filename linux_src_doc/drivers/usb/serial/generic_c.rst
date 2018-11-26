.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/serial/generic.c

.. _`usb_serial_generic_write_start`:

usb_serial_generic_write_start
==============================

.. c:function:: int usb_serial_generic_write_start(struct usb_serial_port *port, gfp_t mem_flags)

    start writing buffered data

    :param port:
        usb-serial port
    :type port: struct usb_serial_port \*

    :param mem_flags:
        flags to use for memory allocations
    :type mem_flags: gfp_t

.. _`usb_serial_generic_write_start.description`:

Description
-----------

Serialised using USB_SERIAL_WRITE_BUSY flag.

.. _`usb_serial_generic_write_start.return`:

Return
------

Zero on success or if busy, otherwise a negative errno value.

.. _`usb_serial_generic_write`:

usb_serial_generic_write
========================

.. c:function:: int usb_serial_generic_write(struct tty_struct *tty, struct usb_serial_port *port, const unsigned char *buf, int count)

    generic write function

    :param tty:
        tty for the port
    :type tty: struct tty_struct \*

    :param port:
        usb-serial port
    :type port: struct usb_serial_port \*

    :param buf:
        data to write
    :type buf: const unsigned char \*

    :param count:
        number of bytes to write
    :type count: int

.. _`usb_serial_generic_write.return`:

Return
------

The number of characters buffered, which may be anything from
zero to \ ``count``\ , or a negative errno value.

.. _`usb_serial_handle_dcd_change`:

usb_serial_handle_dcd_change
============================

.. c:function:: void usb_serial_handle_dcd_change(struct usb_serial_port *usb_port, struct tty_struct *tty, unsigned int status)

    handle a change of carrier detect state

    :param usb_port:
        *undescribed*
    :type usb_port: struct usb_serial_port \*

    :param tty:
        tty for the port
    :type tty: struct tty_struct \*

    :param status:
        new carrier detect status, nonzero if active
    :type status: unsigned int

.. This file was automatic generated / don't edit.


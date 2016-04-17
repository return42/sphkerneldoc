.. -*- coding: utf-8; mode: rst -*-

=======
daisy.c
=======


.. _`parport_open`:

parport_open
============

.. c:function:: struct pardevice *parport_open (int devnum, const char *name)

    find a device by canonical device number

    :param int devnum:
        canonical device number

    :param const char \*name:
        name to associate with the device



.. _`parport_open.description`:

Description
-----------

This function is similar to :c:func:`parport_register_device`, except
that it locates a device by its number rather than by the port
it is attached to.

All parameters except for ``devnum`` are the same as for
:c:func:`parport_register_device`.  The return value is the same as
for :c:func:`parport_register_device`.



.. _`parport_close`:

parport_close
=============

.. c:function:: void parport_close (struct pardevice *dev)

    close a device opened with parport_open()

    :param struct pardevice \*dev:
        device to close



.. _`parport_close.description`:

Description
-----------

This is to :c:func:`parport_open` as :c:func:`parport_unregister_device` is to
:c:func:`parport_register_device`.


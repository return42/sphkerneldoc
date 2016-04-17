.. -*- coding: utf-8; mode: rst -*-

=====
ide.c
=====


.. _`ide_device_get`:

ide_device_get
==============

.. c:function:: int ide_device_get (ide_drive_t *drive)

    get an additional reference to a ide_drive_t

    :param ide_drive_t \*drive:
        device to get a reference to



.. _`ide_device_get.description`:

Description
-----------

Gets a reference to the ide_drive_t and increments the use count of the
underlying LLDD module.



.. _`ide_device_put`:

ide_device_put
==============

.. c:function:: void ide_device_put (ide_drive_t *drive)

    release a reference to a ide_drive_t

    :param ide_drive_t \*drive:
        device to release a reference on



.. _`ide_device_put.description`:

Description
-----------

Release a reference to the ide_drive_t and decrements the use count of
the underlying LLDD module.


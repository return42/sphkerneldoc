.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ide/ide.c

.. _`ide_device_get`:

ide_device_get
==============

.. c:function:: int ide_device_get(ide_drive_t *drive)

    get an additional reference to a ide_drive_t

    :param drive:
        device to get a reference to
    :type drive: ide_drive_t \*

.. _`ide_device_get.description`:

Description
-----------

Gets a reference to the ide_drive_t and increments the use count of the
underlying LLDD module.

.. _`ide_device_put`:

ide_device_put
==============

.. c:function:: void ide_device_put(ide_drive_t *drive)

    release a reference to a ide_drive_t

    :param drive:
        device to release a reference on
    :type drive: ide_drive_t \*

.. _`ide_device_put.description`:

Description
-----------

Release a reference to the ide_drive_t and decrements the use count of
the underlying LLDD module.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-

==============
device_sysfs.c
==============


.. _`create_pnp_modalias`:

create_pnp_modalias
===================

.. c:function:: int create_pnp_modalias (struct acpi_device *acpi_dev, char *modalias, int size)

    Create hid/cid(s) string for modalias and uevent

    :param struct acpi_device \*acpi_dev:
        ACPI device object.

    :param char \*modalias:
        Buffer to print into.

    :param int size:
        Size of the buffer.



.. _`create_pnp_modalias.description`:

Description
-----------

Creates hid/cid(s) string needed for modalias and uevent
e.g. on a device with hid:IBM0001 and cid:ACPI0001 you get:



.. _`create_pnp_modalias.modalias`:

modalias
--------

"acpi:IBM0001:ACPI0001"



.. _`create_pnp_modalias.return`:

Return
------

0: no _HID and no _CID
-EINVAL: output error
-ENOMEM: output is truncated



.. _`create_of_modalias`:

create_of_modalias
==================

.. c:function:: int create_of_modalias (struct acpi_device *acpi_dev, char *modalias, int size)

    Creates DT compatible string for modalias and uevent

    :param struct acpi_device \*acpi_dev:
        ACPI device object.

    :param char \*modalias:
        Buffer to print into.

    :param int size:
        Size of the buffer.



.. _`create_of_modalias.expose-dt-compatible-modalias-as-of`:

Expose DT compatible modalias as of
-----------------------------------

NnameTCcompatible.  This function should
only be called for devices having ACPI_DT_NAMESPACE_HID in their list of
ACPI/PNP IDs.



.. _`acpi_device_uevent_modalias`:

acpi_device_uevent_modalias
===========================

.. c:function:: int acpi_device_uevent_modalias (struct device *dev, struct kobj_uevent_env *env)

    uevent modalias for ACPI-enumerated devices.

    :param struct device \*dev:

        *undescribed*

    :param struct kobj_uevent_env \*env:

        *undescribed*



.. _`acpi_device_uevent_modalias.description`:

Description
-----------


Create the uevent modalias field for ACPI-enumerated devices.

Because other buses do not support ACPI HIDs & CIDs, e.g. for a device with



.. _`acpi_device_uevent_modalias.hid`:

hid
---

IBM0001 and cid:ACPI0001 you get: "acpi:IBM0001:ACPI0001".



.. _`acpi_device_modalias`:

acpi_device_modalias
====================

.. c:function:: int acpi_device_modalias (struct device *dev, char *buf, int size)

    modalias sysfs attribute for ACPI-enumerated devices.

    :param struct device \*dev:

        *undescribed*

    :param char \*buf:

        *undescribed*

    :param int size:

        *undescribed*



.. _`acpi_device_modalias.description`:

Description
-----------


Create the modalias sysfs attribute for ACPI-enumerated devices.

Because other buses do not support ACPI HIDs & CIDs, e.g. for a device with



.. _`acpi_device_modalias.hid`:

hid
---

IBM0001 and cid:ACPI0001 you get: "acpi:IBM0001:ACPI0001".



.. _`acpi_device_setup_files`:

acpi_device_setup_files
=======================

.. c:function:: int acpi_device_setup_files (struct acpi_device *dev)

    Create sysfs attributes of an ACPI device.

    :param struct acpi_device \*dev:
        ACPI device object.



.. _`acpi_device_remove_files`:

acpi_device_remove_files
========================

.. c:function:: void acpi_device_remove_files (struct acpi_device *dev)

    Remove sysfs attributes of an ACPI device.

    :param struct acpi_device \*dev:
        ACPI device object.


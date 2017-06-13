.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/bus.c

.. _`acpi_bus_notify`:

acpi_bus_notify
===============

.. c:function:: void acpi_bus_notify(acpi_handle handle, u32 type, void *data)

    --------------- Callback for all 'system-level' device notifications (values 0x00-0x7F).

    :param acpi_handle handle:
        *undescribed*

    :param u32 type:
        *undescribed*

    :param void \*data:
        *undescribed*

.. _`acpi_get_first_physical_node`:

acpi_get_first_physical_node
============================

.. c:function:: struct device *acpi_get_first_physical_node(struct acpi_device *adev)

    Get first physical node of an ACPI device

    :param struct acpi_device \*adev:
        ACPI device in question

.. _`acpi_get_first_physical_node.return`:

Return
------

First physical node of ACPI device \ ``adev``\ 

.. _`acpi_device_is_first_physical_node`:

acpi_device_is_first_physical_node
==================================

.. c:function:: bool acpi_device_is_first_physical_node(struct acpi_device *adev, const struct device *dev)

    Is given dev first physical node

    :param struct acpi_device \*adev:
        ACPI companion device

    :param const struct device \*dev:
        Physical device to check

.. _`acpi_device_is_first_physical_node.description`:

Description
-----------

Function checks if given \ ``dev``\  is the first physical devices attached to
the ACPI companion device. This distinction is needed in some cases
where the same companion device is shared between many physical devices.

Note that the caller have to provide valid \ ``adev``\  pointer.

.. _`acpi_of_match_device`:

acpi_of_match_device
====================

.. c:function:: bool acpi_of_match_device(struct acpi_device *adev, const struct of_device_id *of_match_table)

    Match device object using the "compatible" property.

    :param struct acpi_device \*adev:
        ACPI device object to match.

    :param const struct of_device_id \*of_match_table:
        List of device IDs to match against.

.. _`acpi_of_match_device.description`:

Description
-----------

If \ ``dev``\  has an ACPI companion which has ACPI_DT_NAMESPACE_HID in its list of
identifiers and a \_DSD object with the "compatible" property, use that
property to match against the given list of identifiers.

.. _`acpi_set_modalias`:

acpi_set_modalias
=================

.. c:function:: void acpi_set_modalias(struct acpi_device *adev, const char *default_id, char *modalias, size_t len)

    Set modalias using "compatible" property or supplied ID

    :param struct acpi_device \*adev:
        ACPI device object to match

    :param const char \*default_id:
        ID string to use as default if no compatible string found

    :param char \*modalias:
        Pointer to buffer that modalias value will be copied into

    :param size_t len:
        Length of modalias buffer

.. _`acpi_set_modalias.description`:

Description
-----------

This is a counterpart of \ :c:func:`of_modalias_node`\  for struct acpi_device objects.
If there is a compatible string for \ ``adev``\ , it will be copied to \ ``modalias``\ 
with the vendor prefix stripped; otherwise, \ ``default_id``\  will be used.

.. _`acpi_match_device`:

acpi_match_device
=================

.. c:function:: const struct acpi_device_id *acpi_match_device(const struct acpi_device_id *ids, const struct device *dev)

    Match a struct device against a given list of ACPI IDs

    :param const struct acpi_device_id \*ids:
        Array of struct acpi_device_id object to match against.

    :param const struct device \*dev:
        The device structure to match.

.. _`acpi_match_device.description`:

Description
-----------

Check if \ ``dev``\  has a valid ACPI handle and if there is a struct acpi_device
object for that handle and use that object to match against a given list of
device IDs.

Return a pointer to the first matching ID on success or \ ``NULL``\  on failure.

.. _`acpi_bus_register_driver`:

acpi_bus_register_driver
========================

.. c:function:: int acpi_bus_register_driver(struct acpi_driver *driver)

    register a driver with the ACPI bus

    :param struct acpi_driver \*driver:
        driver being registered

.. _`acpi_bus_register_driver.description`:

Description
-----------

Registers a driver with the ACPI bus.  Searches the namespace for all
devices that match the driver's criteria and binds.  Returns zero for
success or a negative error status for failure.

.. _`acpi_bus_unregister_driver`:

acpi_bus_unregister_driver
==========================

.. c:function:: void acpi_bus_unregister_driver(struct acpi_driver *driver)

    unregisters a driver with the ACPI bus

    :param struct acpi_driver \*driver:
        driver to unregister

.. _`acpi_bus_unregister_driver.description`:

Description
-----------

Unregisters a driver with the ACPI bus.  Searches the namespace for all
devices that match the driver's criteria and unbinds.

.. _`acpi_early_init`:

acpi_early_init
===============

.. c:function:: void acpi_early_init( void)

    Initialize ACPICA and populate the ACPI namespace.

    :param  void:
        no arguments

.. _`acpi_early_init.description`:

Description
-----------

The ACPI tables are accessible after this, but the handling of events has not
been initialized and the global lock is not available yet, so AML should not
be executed at this point.

Doing this before switching the EFI runtime services to virtual mode allows
the EfiBootServices memory to be freed slightly earlier on boot.

.. _`acpi_subsystem_init`:

acpi_subsystem_init
===================

.. c:function:: void acpi_subsystem_init( void)

    Finalize the early initialization of ACPI.

    :param  void:
        no arguments

.. _`acpi_subsystem_init.description`:

Description
-----------

Switch over the platform to the ACPI mode (if possible).

Doing this too early is generally unsafe, but at the same time it needs to be
done before all things that really depend on ACPI.  The right spot appears to
be before finalizing the EFI initialization.

.. This file was automatic generated / don't edit.


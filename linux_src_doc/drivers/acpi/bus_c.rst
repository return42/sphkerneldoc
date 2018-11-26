.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/bus.c

.. _`acpi_bus_notify`:

acpi_bus_notify
===============

.. c:function:: void acpi_bus_notify(acpi_handle handle, u32 type, void *data)

    --------------- Callback for all 'system-level' device notifications (values 0x00-0x7F).

    :param handle:
        *undescribed*
    :type handle: acpi_handle

    :param type:
        *undescribed*
    :type type: u32

    :param data:
        *undescribed*
    :type data: void \*

.. _`acpi_get_first_physical_node`:

acpi_get_first_physical_node
============================

.. c:function:: struct device *acpi_get_first_physical_node(struct acpi_device *adev)

    Get first physical node of an ACPI device

    :param adev:
        ACPI device in question
    :type adev: struct acpi_device \*

.. _`acpi_get_first_physical_node.return`:

Return
------

First physical node of ACPI device \ ``adev``\ 

.. _`acpi_device_is_first_physical_node`:

acpi_device_is_first_physical_node
==================================

.. c:function:: bool acpi_device_is_first_physical_node(struct acpi_device *adev, const struct device *dev)

    Is given dev first physical node

    :param adev:
        ACPI companion device
    :type adev: struct acpi_device \*

    :param dev:
        Physical device to check
    :type dev: const struct device \*

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

.. c:function:: bool acpi_of_match_device(struct acpi_device *adev, const struct of_device_id *of_match_table, const struct of_device_id **of_id)

    Match device object using the "compatible" property.

    :param adev:
        ACPI device object to match.
    :type adev: struct acpi_device \*

    :param of_match_table:
        List of device IDs to match against.
    :type of_match_table: const struct of_device_id \*

    :param of_id:
        OF ID if matched
    :type of_id: const struct of_device_id \*\*

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

    :param adev:
        ACPI device object to match
    :type adev: struct acpi_device \*

    :param default_id:
        ID string to use as default if no compatible string found
    :type default_id: const char \*

    :param modalias:
        Pointer to buffer that modalias value will be copied into
    :type modalias: char \*

    :param len:
        Length of modalias buffer
    :type len: size_t

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

    :param ids:
        Array of struct acpi_device_id object to match against.
    :type ids: const struct acpi_device_id \*

    :param dev:
        The device structure to match.
    :type dev: const struct device \*

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

    :param driver:
        driver being registered
    :type driver: struct acpi_driver \*

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

    :param driver:
        driver to unregister
    :type driver: struct acpi_driver \*

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

    :param void:
        no arguments
    :type void: 

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

    :param void:
        no arguments
    :type void: 

.. _`acpi_subsystem_init.description`:

Description
-----------

Switch over the platform to the ACPI mode (if possible).

Doing this too early is generally unsafe, but at the same time it needs to be
done before all things that really depend on ACPI.  The right spot appears to
be before finalizing the EFI initialization.

.. This file was automatic generated / don't edit.


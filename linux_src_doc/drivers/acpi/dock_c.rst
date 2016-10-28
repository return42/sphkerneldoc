.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/dock.c

.. _`add_dock_dependent_device`:

add_dock_dependent_device
=========================

.. c:function:: int add_dock_dependent_device(struct dock_station *ds, struct acpi_device *adev)

    associate a device with the dock station

    :param struct dock_station \*ds:
        Dock station.

    :param struct acpi_device \*adev:
        Dependent ACPI device object.

.. _`add_dock_dependent_device.description`:

Description
-----------

Add the dependent device to the dock's dependent device list.

.. _`find_dock_dependent_device`:

find_dock_dependent_device
==========================

.. c:function:: struct dock_dependent_device *find_dock_dependent_device(struct dock_station *ds, struct acpi_device *adev)

    get a device dependent on this dock

    :param struct dock_station \*ds:
        the dock station

    :param struct acpi_device \*adev:
        ACPI device object to find.

.. _`find_dock_dependent_device.description`:

Description
-----------

iterate over the dependent device list for this dock.  If the
dependent device matches the handle, return.

.. _`is_dock_device`:

is_dock_device
==============

.. c:function:: int is_dock_device(struct acpi_device *adev)

    see if a device is on a dock station

    :param struct acpi_device \*adev:
        ACPI device object to check.

.. _`is_dock_device.description`:

Description
-----------

If this device is either the dock station itself,
or is a device dependent on the dock station, then it
is a dock device

.. _`dock_present`:

dock_present
============

.. c:function:: int dock_present(struct dock_station *ds)

    see if the dock station is present.

    :param struct dock_station \*ds:
        the dock station

.. _`dock_present.description`:

Description
-----------

execute the \_STA method.  note that present does not
imply that we are docked.

.. _`hot_remove_dock_devices`:

hot_remove_dock_devices
=======================

.. c:function:: void hot_remove_dock_devices(struct dock_station *ds)

    Remove dock station devices.

    :param struct dock_station \*ds:
        Dock station.

.. _`hotplug_dock_devices`:

hotplug_dock_devices
====================

.. c:function:: void hotplug_dock_devices(struct dock_station *ds, u32 event)

    Insert devices on a dock station.

    :param struct dock_station \*ds:
        the dock station

    :param u32 event:
        either bus check or device check request

.. _`hotplug_dock_devices.description`:

Description
-----------

Some devices on the dock station need to have drivers called
to perform hotplug operations after a dock event has occurred.
Traverse the list of dock devices that have registered a
hotplug handler, and call the handler.

.. _`handle_dock`:

handle_dock
===========

.. c:function:: void handle_dock(struct dock_station *ds, int dock)

    handle a dock event

    :param struct dock_station \*ds:
        the dock station

    :param int dock:
        to dock, or undock - that is the question

.. _`handle_dock.description`:

Description
-----------

Execute the \_DCK method in response to an acpi event

.. _`dock_in_progress`:

dock_in_progress
================

.. c:function:: int dock_in_progress(struct dock_station *ds)

    see if we are in the middle of handling a dock event

    :param struct dock_station \*ds:
        the dock station

.. _`dock_in_progress.description`:

Description
-----------

Sometimes while docking, false dock events can be sent to the driver
because good connections aren't made or some other reason.  Ignore these
if we are in the middle of doing something.

.. _`handle_eject_request`:

handle_eject_request
====================

.. c:function:: int handle_eject_request(struct dock_station *ds, u32 event)

    handle an undock request checking for error conditions

    :param struct dock_station \*ds:
        *undescribed*

    :param u32 event:
        *undescribed*

.. _`handle_eject_request.description`:

Description
-----------

Check to make sure the dock device is still present, then undock and
hotremove all the devices that may need removing.

.. _`dock_notify`:

dock_notify
===========

.. c:function:: int dock_notify(struct acpi_device *adev, u32 event)

    Handle ACPI dock notification.

    :param struct acpi_device \*adev:
        Dock station's ACPI device object.

    :param u32 event:
        Event code.

.. _`dock_notify.description`:

Description
-----------

If we are notified to dock, then check to see if the dock is
present and then dock.  Notify all drivers of the dock event,
and then hotplug and devices that may need hotplugging.

.. _`acpi_dock_add`:

acpi_dock_add
=============

.. c:function:: void acpi_dock_add(struct acpi_device *adev)

    Add a new dock station

    :param struct acpi_device \*adev:
        Dock station ACPI device object.

.. _`acpi_dock_add.description`:

Description
-----------

allocated and initialize a new dock station device.

.. This file was automatic generated / don't edit.


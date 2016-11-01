.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/property.c

.. _`acpi_data_get_property`:

acpi_data_get_property
======================

.. c:function:: int acpi_data_get_property(struct acpi_device_data *data, const char *name, acpi_object_type type, const union acpi_object **obj)

    return an ACPI property with given name

    :param struct acpi_device_data \*data:
        ACPI device deta object to get the property from

    :param const char \*name:
        Name of the property

    :param acpi_object_type type:
        Expected property type

    :param const union acpi_object \*\*obj:
        Location to store the property value (if not \ ``NULL``\ )

.. _`acpi_data_get_property.description`:

Description
-----------

Look up a property with \ ``name``\  and store a pointer to the resulting ACPI
object at the location pointed to by \ ``obj``\  if found.

Callers must not attempt to free the returned objects.  These objects will be
freed by the ACPI core automatically during the removal of \ ``data``\ .

.. _`acpi_data_get_property.return`:

Return
------

%0 if property with \ ``name``\  has been found (success),
\ ``-EINVAL``\  if the arguments are invalid,
\ ``-EINVAL``\  if the property doesn't exist,
\ ``-EPROTO``\  if the property value type doesn't match \ ``type``\ .

.. _`acpi_dev_get_property`:

acpi_dev_get_property
=====================

.. c:function:: int acpi_dev_get_property(struct acpi_device *adev, const char *name, acpi_object_type type, const union acpi_object **obj)

    return an ACPI property with given name.

    :param struct acpi_device \*adev:
        ACPI device to get the property from.

    :param const char \*name:
        Name of the property.

    :param acpi_object_type type:
        Expected property type.

    :param const union acpi_object \*\*obj:
        Location to store the property value (if not \ ``NULL``\ ).

.. _`acpi_node_prop_get`:

acpi_node_prop_get
==================

.. c:function:: int acpi_node_prop_get(struct fwnode_handle *fwnode, const char *propname, void **valptr)

    return an ACPI property with given name.

    :param struct fwnode_handle \*fwnode:
        Firmware node to get the property from.

    :param const char \*propname:
        Name of the property.

    :param void \*\*valptr:
        Location to store a pointer to the property value (if not \ ``NULL``\ ).

.. _`acpi_data_get_property_array`:

acpi_data_get_property_array
============================

.. c:function:: int acpi_data_get_property_array(struct acpi_device_data *data, const char *name, acpi_object_type type, const union acpi_object **obj)

    return an ACPI array property with given name

    :param struct acpi_device_data \*data:
        *undescribed*

    :param const char \*name:
        Name of the property

    :param acpi_object_type type:
        Expected type of array elements

    :param const union acpi_object \*\*obj:
        Location to store a pointer to the property value (if not NULL)

.. _`acpi_data_get_property_array.description`:

Description
-----------

Look up an array property with \ ``name``\  and store a pointer to the resulting
ACPI object at the location pointed to by \ ``obj``\  if found.

Callers must not attempt to free the returned objects.  Those objects will be
freed by the ACPI core automatically during the removal of \ ``data``\ .

.. _`acpi_data_get_property_array.return`:

Return
------

%0 if array property (package) with \ ``name``\  has been found (success),
\ ``-EINVAL``\  if the arguments are invalid,
\ ``-EINVAL``\  if the property doesn't exist,
\ ``-EPROTO``\  if the property is not a package or the type of its elements
doesn't match \ ``type``\ .

.. _`__acpi_node_get_property_reference`:

__acpi_node_get_property_reference
==================================

.. c:function:: int __acpi_node_get_property_reference(struct fwnode_handle *fwnode, const char *propname, size_t index, size_t num_args, struct acpi_reference_args *args)

    returns handle to the referenced object

    :param struct fwnode_handle \*fwnode:
        Firmware node to get the property from

    :param const char \*propname:
        Name of the property

    :param size_t index:
        Index of the reference to return

    :param size_t num_args:
        Maximum number of arguments after each reference

    :param struct acpi_reference_args \*args:
        Location to store the returned reference with optional arguments

.. _`__acpi_node_get_property_reference.description`:

Description
-----------

Find property with \ ``name``\ , verifify that it is a package containing at least
one object reference and if so, store the ACPI device object pointer to the
target object in \ ``args``\ ->adev.  If the reference includes arguments, store
them in the \ ``args``\ ->args[] array.

If there's more than one reference in the property value package, \ ``index``\  is
used to select the one to return.

It is possible to leave holes in the property value set like in the

.. _`__acpi_node_get_property_reference.example-below`:

example below
-------------


Package () {
"cs-gpios",
Package () {
^GPIO, 19, 0, 0,
^GPIO, 20, 0, 0,
0,
^GPIO, 21, 0, 0,
}
}

Calling this function with index \ ``2``\  return \ ``-ENOENT``\  and with index \ ``3``\ 
returns the last entry. If the property does not contain any more values
\ ``-ENODATA``\  is returned. The NULL entry must be single integer and
preferably contain value \ ``0``\ .

.. _`__acpi_node_get_property_reference.return`:

Return
------

%0 on success, negative error code on failure.

.. _`acpi_node_prop_read`:

acpi_node_prop_read
===================

.. c:function:: int acpi_node_prop_read(struct fwnode_handle *fwnode, const char *propname, enum dev_prop_type proptype, void *val, size_t nval)

    retrieve the value of an ACPI property with given name.

    :param struct fwnode_handle \*fwnode:
        Firmware node to get the property from.

    :param const char \*propname:
        Name of the property.

    :param enum dev_prop_type proptype:
        Expected property type.

    :param void \*val:
        Location to store the property value (if not \ ``NULL``\ ).

    :param size_t nval:
        Size of the array pointed to by \ ``val``\ .

.. _`acpi_node_prop_read.description`:

Description
-----------

If \ ``val``\  is \ ``NULL``\ , return the number of array elements comprising the value
of the property.  Otherwise, read at most \ ``nval``\  values to the array at the
location pointed to by \ ``val``\ .

.. _`acpi_get_next_subnode`:

acpi_get_next_subnode
=====================

.. c:function:: struct fwnode_handle *acpi_get_next_subnode(struct device *dev, struct fwnode_handle *child)

    Return the next child node handle for a device.

    :param struct device \*dev:
        Device to find the next child node for.

    :param struct fwnode_handle \*child:
        Handle to one of the device's child nodes or a null handle.

.. This file was automatic generated / don't edit.


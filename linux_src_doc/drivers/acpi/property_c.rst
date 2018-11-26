.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/property.c

.. _`acpi_data_get_property`:

acpi_data_get_property
======================

.. c:function:: int acpi_data_get_property(const struct acpi_device_data *data, const char *name, acpi_object_type type, const union acpi_object **obj)

    return an ACPI property with given name

    :param data:
        ACPI device deta object to get the property from
    :type data: const struct acpi_device_data \*

    :param name:
        Name of the property
    :type name: const char \*

    :param type:
        Expected property type
    :type type: acpi_object_type

    :param obj:
        Location to store the property value (if not \ ``NULL``\ )
    :type obj: const union acpi_object \*\*

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

\ ``0``\  if property with \ ``name``\  has been found (success),
\ ``-EINVAL``\  if the arguments are invalid,
\ ``-EINVAL``\  if the property doesn't exist,
\ ``-EPROTO``\  if the property value type doesn't match \ ``type``\ .

.. _`acpi_dev_get_property`:

acpi_dev_get_property
=====================

.. c:function:: int acpi_dev_get_property(const struct acpi_device *adev, const char *name, acpi_object_type type, const union acpi_object **obj)

    return an ACPI property with given name.

    :param adev:
        ACPI device to get the property from.
    :type adev: const struct acpi_device \*

    :param name:
        Name of the property.
    :type name: const char \*

    :param type:
        Expected property type.
    :type type: acpi_object_type

    :param obj:
        Location to store the property value (if not \ ``NULL``\ ).
    :type obj: const union acpi_object \*\*

.. _`acpi_node_prop_get`:

acpi_node_prop_get
==================

.. c:function:: int acpi_node_prop_get(const struct fwnode_handle *fwnode, const char *propname, void **valptr)

    return an ACPI property with given name.

    :param fwnode:
        Firmware node to get the property from.
    :type fwnode: const struct fwnode_handle \*

    :param propname:
        Name of the property.
    :type propname: const char \*

    :param valptr:
        Location to store a pointer to the property value (if not \ ``NULL``\ ).
    :type valptr: void \*\*

.. _`acpi_data_get_property_array`:

acpi_data_get_property_array
============================

.. c:function:: int acpi_data_get_property_array(const struct acpi_device_data *data, const char *name, acpi_object_type type, const union acpi_object **obj)

    return an ACPI array property with given name

    :param data:
        *undescribed*
    :type data: const struct acpi_device_data \*

    :param name:
        Name of the property
    :type name: const char \*

    :param type:
        Expected type of array elements
    :type type: acpi_object_type

    :param obj:
        Location to store a pointer to the property value (if not NULL)
    :type obj: const union acpi_object \*\*

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

\ ``0``\  if array property (package) with \ ``name``\  has been found (success),
\ ``-EINVAL``\  if the arguments are invalid,
\ ``-EINVAL``\  if the property doesn't exist,
\ ``-EPROTO``\  if the property is not a package or the type of its elements
doesn't match \ ``type``\ .

.. _`__acpi_node_get_property_reference`:

\__acpi_node_get_property_reference
===================================

.. c:function:: int __acpi_node_get_property_reference(const struct fwnode_handle *fwnode, const char *propname, size_t index, size_t num_args, struct fwnode_reference_args *args)

    returns handle to the referenced object

    :param fwnode:
        Firmware node to get the property from
    :type fwnode: const struct fwnode_handle \*

    :param propname:
        Name of the property
    :type propname: const char \*

    :param index:
        Index of the reference to return
    :type index: size_t

    :param num_args:
        Maximum number of arguments after each reference
    :type num_args: size_t

    :param args:
        Location to store the returned reference with optional arguments
    :type args: struct fwnode_reference_args \*

.. _`__acpi_node_get_property_reference.description`:

Description
-----------

Find property with \ ``name``\ , verifify that it is a package containing at least
one object reference and if so, store the ACPI device object pointer to the
target object in \ ``args->adev``\ .  If the reference includes arguments, store
them in the \ ``args->args``\ [] array.

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

Calling this function with index \ ``2``\  or index \ ``3``\  return \ ``-ENOENT``\ . If the
property does not contain any more values \ ``-ENOENT``\  is returned. The NULL
entry must be single integer and preferably contain value \ ``0``\ .

.. _`__acpi_node_get_property_reference.return`:

Return
------

\ ``0``\  on success, negative error code on failure.

.. _`acpi_node_prop_read`:

acpi_node_prop_read
===================

.. c:function:: int acpi_node_prop_read(const struct fwnode_handle *fwnode, const char *propname, enum dev_prop_type proptype, void *val, size_t nval)

    retrieve the value of an ACPI property with given name.

    :param fwnode:
        Firmware node to get the property from.
    :type fwnode: const struct fwnode_handle \*

    :param propname:
        Name of the property.
    :type propname: const char \*

    :param proptype:
        Expected property type.
    :type proptype: enum dev_prop_type

    :param val:
        Location to store the property value (if not \ ``NULL``\ ).
    :type val: void \*

    :param nval:
        Size of the array pointed to by \ ``val``\ .
    :type nval: size_t

.. _`acpi_node_prop_read.description`:

Description
-----------

If \ ``val``\  is \ ``NULL``\ , return the number of array elements comprising the value
of the property.  Otherwise, read at most \ ``nval``\  values to the array at the
location pointed to by \ ``val``\ .

.. _`acpi_get_next_subnode`:

acpi_get_next_subnode
=====================

.. c:function:: struct fwnode_handle *acpi_get_next_subnode(const struct fwnode_handle *fwnode, struct fwnode_handle *child)

    Return the next child node handle for a fwnode

    :param fwnode:
        Firmware node to find the next child node for.
    :type fwnode: const struct fwnode_handle \*

    :param child:
        Handle to one of the device's child nodes or a null handle.
    :type child: struct fwnode_handle \*

.. _`acpi_node_get_parent`:

acpi_node_get_parent
====================

.. c:function:: struct fwnode_handle *acpi_node_get_parent(const struct fwnode_handle *fwnode)

    Return parent fwnode of this fwnode

    :param fwnode:
        Firmware node whose parent to get
    :type fwnode: const struct fwnode_handle \*

.. _`acpi_node_get_parent.description`:

Description
-----------

Returns parent node of an ACPI device or data firmware node or \ ``NULL``\  if
not available.

.. _`acpi_graph_get_next_endpoint`:

acpi_graph_get_next_endpoint
============================

.. c:function:: struct fwnode_handle *acpi_graph_get_next_endpoint(const struct fwnode_handle *fwnode, struct fwnode_handle *prev)

    Get next endpoint ACPI firmware node

    :param fwnode:
        Pointer to the parent firmware node
    :type fwnode: const struct fwnode_handle \*

    :param prev:
        Previous endpoint node or \ ``NULL``\  to get the first
    :type prev: struct fwnode_handle \*

.. _`acpi_graph_get_next_endpoint.description`:

Description
-----------

Looks up next endpoint ACPI firmware node below a given \ ``fwnode``\ . Returns
\ ``NULL``\  if there is no next endpoint or in case of error. In case of success
the next endpoint is returned.

.. _`acpi_graph_get_child_prop_value`:

acpi_graph_get_child_prop_value
===============================

.. c:function:: struct fwnode_handle *acpi_graph_get_child_prop_value(const struct fwnode_handle *fwnode, const char *prop_name, unsigned int val)

    Return a child with a given property value

    :param fwnode:
        device fwnode
    :type fwnode: const struct fwnode_handle \*

    :param prop_name:
        The name of the property to look for
    :type prop_name: const char \*

    :param val:
        the desired property value
    :type val: unsigned int

.. _`acpi_graph_get_child_prop_value.description`:

Description
-----------

Return the port node corresponding to a given port number. Returns
the child node on success, NULL otherwise.

.. _`acpi_graph_get_remote_endpoint`:

acpi_graph_get_remote_endpoint
==============================

.. c:function:: struct fwnode_handle *acpi_graph_get_remote_endpoint(const struct fwnode_handle *__fwnode)

    Parses and returns remote end of an endpoint

    :param __fwnode:
        *undescribed*
    :type __fwnode: const struct fwnode_handle \*

.. _`acpi_graph_get_remote_endpoint.description`:

Description
-----------

Returns the remote endpoint corresponding to \ ``__fwnode``\ . NULL on error.

.. This file was automatic generated / don't edit.


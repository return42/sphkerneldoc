.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/property.c

.. _`device_property_present`:

device_property_present
=======================

.. c:function:: bool device_property_present(struct device *dev, const char *propname)

    check if a property of a device is present

    :param dev:
        Device whose property is being checked
    :type dev: struct device \*

    :param propname:
        Name of the property
    :type propname: const char \*

.. _`device_property_present.description`:

Description
-----------

Check if property \ ``propname``\  is present in the device firmware description.

.. _`fwnode_property_present`:

fwnode_property_present
=======================

.. c:function:: bool fwnode_property_present(const struct fwnode_handle *fwnode, const char *propname)

    check if a property of a firmware node is present

    :param fwnode:
        Firmware node whose property to check
    :type fwnode: const struct fwnode_handle \*

    :param propname:
        Name of the property
    :type propname: const char \*

.. _`device_property_read_u8_array`:

device_property_read_u8_array
=============================

.. c:function:: int device_property_read_u8_array(struct device *dev, const char *propname, u8 *val, size_t nval)

    return a u8 array property of a device

    :param dev:
        Device to get the property of
    :type dev: struct device \*

    :param propname:
        Name of the property
    :type propname: const char \*

    :param val:
        The values are stored here or \ ``NULL``\  to return the number of values
    :type val: u8 \*

    :param nval:
        Size of the \ ``val``\  array
    :type nval: size_t

.. _`device_property_read_u8_array.description`:

Description
-----------

Function reads an array of u8 properties with \ ``propname``\  from the device
firmware description and stores them to \ ``val``\  if found.

.. _`device_property_read_u8_array.return`:

Return
------

number of values if \ ``val``\  was \ ``NULL``\ ,
\ ``0``\  if the property was found (success),
\ ``-EINVAL``\  if given arguments are not valid,
\ ``-ENODATA``\  if the property does not have a value,
\ ``-EPROTO``\  if the property is not an array of numbers,
\ ``-EOVERFLOW``\  if the size of the property is not as expected.
\ ``-ENXIO``\  if no suitable firmware interface is present.

.. _`device_property_read_u16_array`:

device_property_read_u16_array
==============================

.. c:function:: int device_property_read_u16_array(struct device *dev, const char *propname, u16 *val, size_t nval)

    return a u16 array property of a device

    :param dev:
        Device to get the property of
    :type dev: struct device \*

    :param propname:
        Name of the property
    :type propname: const char \*

    :param val:
        The values are stored here or \ ``NULL``\  to return the number of values
    :type val: u16 \*

    :param nval:
        Size of the \ ``val``\  array
    :type nval: size_t

.. _`device_property_read_u16_array.description`:

Description
-----------

Function reads an array of u16 properties with \ ``propname``\  from the device
firmware description and stores them to \ ``val``\  if found.

.. _`device_property_read_u16_array.return`:

Return
------

number of values if \ ``val``\  was \ ``NULL``\ ,
\ ``0``\  if the property was found (success),
\ ``-EINVAL``\  if given arguments are not valid,
\ ``-ENODATA``\  if the property does not have a value,
\ ``-EPROTO``\  if the property is not an array of numbers,
\ ``-EOVERFLOW``\  if the size of the property is not as expected.
\ ``-ENXIO``\  if no suitable firmware interface is present.

.. _`device_property_read_u32_array`:

device_property_read_u32_array
==============================

.. c:function:: int device_property_read_u32_array(struct device *dev, const char *propname, u32 *val, size_t nval)

    return a u32 array property of a device

    :param dev:
        Device to get the property of
    :type dev: struct device \*

    :param propname:
        Name of the property
    :type propname: const char \*

    :param val:
        The values are stored here or \ ``NULL``\  to return the number of values
    :type val: u32 \*

    :param nval:
        Size of the \ ``val``\  array
    :type nval: size_t

.. _`device_property_read_u32_array.description`:

Description
-----------

Function reads an array of u32 properties with \ ``propname``\  from the device
firmware description and stores them to \ ``val``\  if found.

.. _`device_property_read_u32_array.return`:

Return
------

number of values if \ ``val``\  was \ ``NULL``\ ,
\ ``0``\  if the property was found (success),
\ ``-EINVAL``\  if given arguments are not valid,
\ ``-ENODATA``\  if the property does not have a value,
\ ``-EPROTO``\  if the property is not an array of numbers,
\ ``-EOVERFLOW``\  if the size of the property is not as expected.
\ ``-ENXIO``\  if no suitable firmware interface is present.

.. _`device_property_read_u64_array`:

device_property_read_u64_array
==============================

.. c:function:: int device_property_read_u64_array(struct device *dev, const char *propname, u64 *val, size_t nval)

    return a u64 array property of a device

    :param dev:
        Device to get the property of
    :type dev: struct device \*

    :param propname:
        Name of the property
    :type propname: const char \*

    :param val:
        The values are stored here or \ ``NULL``\  to return the number of values
    :type val: u64 \*

    :param nval:
        Size of the \ ``val``\  array
    :type nval: size_t

.. _`device_property_read_u64_array.description`:

Description
-----------

Function reads an array of u64 properties with \ ``propname``\  from the device
firmware description and stores them to \ ``val``\  if found.

.. _`device_property_read_u64_array.return`:

Return
------

number of values if \ ``val``\  was \ ``NULL``\ ,
\ ``0``\  if the property was found (success),
\ ``-EINVAL``\  if given arguments are not valid,
\ ``-ENODATA``\  if the property does not have a value,
\ ``-EPROTO``\  if the property is not an array of numbers,
\ ``-EOVERFLOW``\  if the size of the property is not as expected.
\ ``-ENXIO``\  if no suitable firmware interface is present.

.. _`device_property_read_string_array`:

device_property_read_string_array
=================================

.. c:function:: int device_property_read_string_array(struct device *dev, const char *propname, const char **val, size_t nval)

    return a string array property of device

    :param dev:
        Device to get the property of
    :type dev: struct device \*

    :param propname:
        Name of the property
    :type propname: const char \*

    :param val:
        The values are stored here or \ ``NULL``\  to return the number of values
    :type val: const char \*\*

    :param nval:
        Size of the \ ``val``\  array
    :type nval: size_t

.. _`device_property_read_string_array.description`:

Description
-----------

Function reads an array of string properties with \ ``propname``\  from the device
firmware description and stores them to \ ``val``\  if found.

.. _`device_property_read_string_array.return`:

Return
------

number of values read on success if \ ``val``\  is non-NULL,
number of values available on success if \ ``val``\  is NULL,
\ ``-EINVAL``\  if given arguments are not valid,
\ ``-ENODATA``\  if the property does not have a value,
\ ``-EPROTO``\  or \ ``-EILSEQ``\  if the property is not an array of strings,
\ ``-EOVERFLOW``\  if the size of the property is not as expected.
\ ``-ENXIO``\  if no suitable firmware interface is present.

.. _`device_property_read_string`:

device_property_read_string
===========================

.. c:function:: int device_property_read_string(struct device *dev, const char *propname, const char **val)

    return a string property of a device

    :param dev:
        Device to get the property of
    :type dev: struct device \*

    :param propname:
        Name of the property
    :type propname: const char \*

    :param val:
        The value is stored here
    :type val: const char \*\*

.. _`device_property_read_string.description`:

Description
-----------

Function reads property \ ``propname``\  from the device firmware description and
stores the value into \ ``val``\  if found. The value is checked to be a string.

.. _`device_property_read_string.return`:

Return
------

\ ``0``\  if the property was found (success),
\ ``-EINVAL``\  if given arguments are not valid,
\ ``-ENODATA``\  if the property does not have a value,
\ ``-EPROTO``\  or \ ``-EILSEQ``\  if the property type is not a string.
\ ``-ENXIO``\  if no suitable firmware interface is present.

.. _`device_property_match_string`:

device_property_match_string
============================

.. c:function:: int device_property_match_string(struct device *dev, const char *propname, const char *string)

    find a string in an array and return index

    :param dev:
        Device to get the property of
    :type dev: struct device \*

    :param propname:
        Name of the property holding the array
    :type propname: const char \*

    :param string:
        String to look for
    :type string: const char \*

.. _`device_property_match_string.description`:

Description
-----------

Find a given string in a string array and if it is found return the
index back.

.. _`device_property_match_string.return`:

Return
------

\ ``0``\  if the property was found (success),
\ ``-EINVAL``\  if given arguments are not valid,
\ ``-ENODATA``\  if the property does not have a value,
\ ``-EPROTO``\  if the property is not an array of strings,
\ ``-ENXIO``\  if no suitable firmware interface is present.

.. _`fwnode_property_read_u8_array`:

fwnode_property_read_u8_array
=============================

.. c:function:: int fwnode_property_read_u8_array(const struct fwnode_handle *fwnode, const char *propname, u8 *val, size_t nval)

    return a u8 array property of firmware node

    :param fwnode:
        Firmware node to get the property of
    :type fwnode: const struct fwnode_handle \*

    :param propname:
        Name of the property
    :type propname: const char \*

    :param val:
        The values are stored here or \ ``NULL``\  to return the number of values
    :type val: u8 \*

    :param nval:
        Size of the \ ``val``\  array
    :type nval: size_t

.. _`fwnode_property_read_u8_array.description`:

Description
-----------

Read an array of u8 properties with \ ``propname``\  from \ ``fwnode``\  and stores them to
\ ``val``\  if found.

.. _`fwnode_property_read_u8_array.return`:

Return
------

number of values if \ ``val``\  was \ ``NULL``\ ,
\ ``0``\  if the property was found (success),
\ ``-EINVAL``\  if given arguments are not valid,
\ ``-ENODATA``\  if the property does not have a value,
\ ``-EPROTO``\  if the property is not an array of numbers,
\ ``-EOVERFLOW``\  if the size of the property is not as expected,
\ ``-ENXIO``\  if no suitable firmware interface is present.

.. _`fwnode_property_read_u16_array`:

fwnode_property_read_u16_array
==============================

.. c:function:: int fwnode_property_read_u16_array(const struct fwnode_handle *fwnode, const char *propname, u16 *val, size_t nval)

    return a u16 array property of firmware node

    :param fwnode:
        Firmware node to get the property of
    :type fwnode: const struct fwnode_handle \*

    :param propname:
        Name of the property
    :type propname: const char \*

    :param val:
        The values are stored here or \ ``NULL``\  to return the number of values
    :type val: u16 \*

    :param nval:
        Size of the \ ``val``\  array
    :type nval: size_t

.. _`fwnode_property_read_u16_array.description`:

Description
-----------

Read an array of u16 properties with \ ``propname``\  from \ ``fwnode``\  and store them to
\ ``val``\  if found.

.. _`fwnode_property_read_u16_array.return`:

Return
------

number of values if \ ``val``\  was \ ``NULL``\ ,
\ ``0``\  if the property was found (success),
\ ``-EINVAL``\  if given arguments are not valid,
\ ``-ENODATA``\  if the property does not have a value,
\ ``-EPROTO``\  if the property is not an array of numbers,
\ ``-EOVERFLOW``\  if the size of the property is not as expected,
\ ``-ENXIO``\  if no suitable firmware interface is present.

.. _`fwnode_property_read_u32_array`:

fwnode_property_read_u32_array
==============================

.. c:function:: int fwnode_property_read_u32_array(const struct fwnode_handle *fwnode, const char *propname, u32 *val, size_t nval)

    return a u32 array property of firmware node

    :param fwnode:
        Firmware node to get the property of
    :type fwnode: const struct fwnode_handle \*

    :param propname:
        Name of the property
    :type propname: const char \*

    :param val:
        The values are stored here or \ ``NULL``\  to return the number of values
    :type val: u32 \*

    :param nval:
        Size of the \ ``val``\  array
    :type nval: size_t

.. _`fwnode_property_read_u32_array.description`:

Description
-----------

Read an array of u32 properties with \ ``propname``\  from \ ``fwnode``\  store them to
\ ``val``\  if found.

.. _`fwnode_property_read_u32_array.return`:

Return
------

number of values if \ ``val``\  was \ ``NULL``\ ,
\ ``0``\  if the property was found (success),
\ ``-EINVAL``\  if given arguments are not valid,
\ ``-ENODATA``\  if the property does not have a value,
\ ``-EPROTO``\  if the property is not an array of numbers,
\ ``-EOVERFLOW``\  if the size of the property is not as expected,
\ ``-ENXIO``\  if no suitable firmware interface is present.

.. _`fwnode_property_read_u64_array`:

fwnode_property_read_u64_array
==============================

.. c:function:: int fwnode_property_read_u64_array(const struct fwnode_handle *fwnode, const char *propname, u64 *val, size_t nval)

    return a u64 array property firmware node

    :param fwnode:
        Firmware node to get the property of
    :type fwnode: const struct fwnode_handle \*

    :param propname:
        Name of the property
    :type propname: const char \*

    :param val:
        The values are stored here or \ ``NULL``\  to return the number of values
    :type val: u64 \*

    :param nval:
        Size of the \ ``val``\  array
    :type nval: size_t

.. _`fwnode_property_read_u64_array.description`:

Description
-----------

Read an array of u64 properties with \ ``propname``\  from \ ``fwnode``\  and store them to
\ ``val``\  if found.

.. _`fwnode_property_read_u64_array.return`:

Return
------

number of values if \ ``val``\  was \ ``NULL``\ ,
\ ``0``\  if the property was found (success),
\ ``-EINVAL``\  if given arguments are not valid,
\ ``-ENODATA``\  if the property does not have a value,
\ ``-EPROTO``\  if the property is not an array of numbers,
\ ``-EOVERFLOW``\  if the size of the property is not as expected,
\ ``-ENXIO``\  if no suitable firmware interface is present.

.. _`fwnode_property_read_string_array`:

fwnode_property_read_string_array
=================================

.. c:function:: int fwnode_property_read_string_array(const struct fwnode_handle *fwnode, const char *propname, const char **val, size_t nval)

    return string array property of a node

    :param fwnode:
        Firmware node to get the property of
    :type fwnode: const struct fwnode_handle \*

    :param propname:
        Name of the property
    :type propname: const char \*

    :param val:
        The values are stored here or \ ``NULL``\  to return the number of values
    :type val: const char \*\*

    :param nval:
        Size of the \ ``val``\  array
    :type nval: size_t

.. _`fwnode_property_read_string_array.description`:

Description
-----------

Read an string list property \ ``propname``\  from the given firmware node and store
them to \ ``val``\  if found.

.. _`fwnode_property_read_string_array.return`:

Return
------

number of values read on success if \ ``val``\  is non-NULL,
number of values available on success if \ ``val``\  is NULL,
\ ``-EINVAL``\  if given arguments are not valid,
\ ``-ENODATA``\  if the property does not have a value,
\ ``-EPROTO``\  or \ ``-EILSEQ``\  if the property is not an array of strings,
\ ``-EOVERFLOW``\  if the size of the property is not as expected,
\ ``-ENXIO``\  if no suitable firmware interface is present.

.. _`fwnode_property_read_string`:

fwnode_property_read_string
===========================

.. c:function:: int fwnode_property_read_string(const struct fwnode_handle *fwnode, const char *propname, const char **val)

    return a string property of a firmware node

    :param fwnode:
        Firmware node to get the property of
    :type fwnode: const struct fwnode_handle \*

    :param propname:
        Name of the property
    :type propname: const char \*

    :param val:
        The value is stored here
    :type val: const char \*\*

.. _`fwnode_property_read_string.description`:

Description
-----------

Read property \ ``propname``\  from the given firmware node and store the value into
\ ``val``\  if found.  The value is checked to be a string.

.. _`fwnode_property_read_string.return`:

Return
------

\ ``0``\  if the property was found (success),
\ ``-EINVAL``\  if given arguments are not valid,
\ ``-ENODATA``\  if the property does not have a value,
\ ``-EPROTO``\  or \ ``-EILSEQ``\  if the property is not a string,
\ ``-ENXIO``\  if no suitable firmware interface is present.

.. _`fwnode_property_match_string`:

fwnode_property_match_string
============================

.. c:function:: int fwnode_property_match_string(const struct fwnode_handle *fwnode, const char *propname, const char *string)

    find a string in an array and return index

    :param fwnode:
        Firmware node to get the property of
    :type fwnode: const struct fwnode_handle \*

    :param propname:
        Name of the property holding the array
    :type propname: const char \*

    :param string:
        String to look for
    :type string: const char \*

.. _`fwnode_property_match_string.description`:

Description
-----------

Find a given string in a string array and if it is found return the
index back.

.. _`fwnode_property_match_string.return`:

Return
------

\ ``0``\  if the property was found (success),
\ ``-EINVAL``\  if given arguments are not valid,
\ ``-ENODATA``\  if the property does not have a value,
\ ``-EPROTO``\  if the property is not an array of strings,
\ ``-ENXIO``\  if no suitable firmware interface is present.

.. _`fwnode_property_get_reference_args`:

fwnode_property_get_reference_args
==================================

.. c:function:: int fwnode_property_get_reference_args(const struct fwnode_handle *fwnode, const char *prop, const char *nargs_prop, unsigned int nargs, unsigned int index, struct fwnode_reference_args *args)

    Find a reference with arguments

    :param fwnode:
        Firmware node where to look for the reference
    :type fwnode: const struct fwnode_handle \*

    :param prop:
        The name of the property
    :type prop: const char \*

    :param nargs_prop:
        The name of the property telling the number of
        arguments in the referred node. NULL if \ ``nargs``\  is known,
        otherwise \ ``nargs``\  is ignored. Only relevant on OF.
    :type nargs_prop: const char \*

    :param nargs:
        Number of arguments. Ignored if \ ``nargs_prop``\  is non-NULL.
    :type nargs: unsigned int

    :param index:
        Index of the reference, from zero onwards.
    :type index: unsigned int

    :param args:
        Result structure with reference and integer arguments.
    :type args: struct fwnode_reference_args \*

.. _`fwnode_property_get_reference_args.description`:

Description
-----------

Obtain a reference based on a named property in an fwnode, with
integer arguments.

Caller is responsible to call \ :c:func:`fwnode_handle_put`\  on the returned
args->fwnode pointer.

.. _`fwnode_property_get_reference_args.return`:

Return
------

\ ``0``\  on success
\ ``-ENOENT``\  when the index is out of bounds, the index has an empty
reference or the property was not found
\ ``-EINVAL``\  on parse error

.. _`property_entries_dup`:

property_entries_dup
====================

.. c:function:: struct property_entry *property_entries_dup(const struct property_entry *properties)

    duplicate array of properties

    :param properties:
        array of properties to copy
    :type properties: const struct property_entry \*

.. _`property_entries_dup.description`:

Description
-----------

This function creates a deep copy of the given NULL-terminated array
of property entries.

.. _`property_entries_free`:

property_entries_free
=====================

.. c:function:: void property_entries_free(const struct property_entry *properties)

    free previously allocated array of properties

    :param properties:
        array of properties to destroy
    :type properties: const struct property_entry \*

.. _`property_entries_free.description`:

Description
-----------

This function frees given NULL-terminated array of property entries,
along with their data.

.. _`pset_free_set`:

pset_free_set
=============

.. c:function:: void pset_free_set(struct property_set *pset)

    releases memory allocated for copied property set

    :param pset:
        Property set to release
    :type pset: struct property_set \*

.. _`pset_free_set.description`:

Description
-----------

Function takes previously copied property set and releases all the
memory allocated to it.

.. _`pset_copy_set`:

pset_copy_set
=============

.. c:function:: struct property_set *pset_copy_set(const struct property_set *pset)

    copies property set

    :param pset:
        Property set to copy
    :type pset: const struct property_set \*

.. _`pset_copy_set.description`:

Description
-----------

This function takes a deep copy of the given property set and returns
pointer to the copy. Call \ :c:func:`device_free_property_set`\  to free resources
allocated in this function.

.. _`pset_copy_set.return`:

Return
------

Pointer to the new property set or error pointer.

.. _`device_remove_properties`:

device_remove_properties
========================

.. c:function:: void device_remove_properties(struct device *dev)

    Remove properties from a device object.

    :param dev:
        Device whose properties to remove.
    :type dev: struct device \*

.. _`device_remove_properties.description`:

Description
-----------

The function removes properties previously associated to the device
secondary firmware node with \ :c:func:`device_add_properties`\ . Memory allocated
to the properties will also be released.

.. _`device_add_properties`:

device_add_properties
=====================

.. c:function:: int device_add_properties(struct device *dev, const struct property_entry *properties)

    Add a collection of properties to a device object.

    :param dev:
        Device to add properties to.
    :type dev: struct device \*

    :param properties:
        Collection of properties to add.
    :type properties: const struct property_entry \*

.. _`device_add_properties.description`:

Description
-----------

Associate a collection of device properties represented by \ ``properties``\  with
\ ``dev``\  as its secondary firmware node. The function takes a copy of
\ ``properties``\ .

.. _`fwnode_get_next_parent`:

fwnode_get_next_parent
======================

.. c:function:: struct fwnode_handle *fwnode_get_next_parent(struct fwnode_handle *fwnode)

    Iterate to the node's parent

    :param fwnode:
        Firmware whose parent is retrieved
    :type fwnode: struct fwnode_handle \*

.. _`fwnode_get_next_parent.description`:

Description
-----------

This is like \ :c:func:`fwnode_get_parent`\  except that it drops the refcount
on the passed node, making it suitable for iterating through a
node's parents.

Returns a node pointer with refcount incremented, use
\ :c:func:`fwnode_handle_node`\  on it when done.

.. _`fwnode_get_parent`:

fwnode_get_parent
=================

.. c:function:: struct fwnode_handle *fwnode_get_parent(const struct fwnode_handle *fwnode)

    Return parent firwmare node

    :param fwnode:
        Firmware whose parent is retrieved
    :type fwnode: const struct fwnode_handle \*

.. _`fwnode_get_parent.description`:

Description
-----------

Return parent firmware node of the given node if possible or \ ``NULL``\  if no
parent was available.

.. _`fwnode_get_next_child_node`:

fwnode_get_next_child_node
==========================

.. c:function:: struct fwnode_handle *fwnode_get_next_child_node(const struct fwnode_handle *fwnode, struct fwnode_handle *child)

    Return the next child node handle for a node

    :param fwnode:
        Firmware node to find the next child node for.
    :type fwnode: const struct fwnode_handle \*

    :param child:
        Handle to one of the node's child nodes or a \ ``NULL``\  handle.
    :type child: struct fwnode_handle \*

.. _`fwnode_get_next_available_child_node`:

fwnode_get_next_available_child_node
====================================

.. c:function:: struct fwnode_handle *fwnode_get_next_available_child_node(const struct fwnode_handle *fwnode, struct fwnode_handle *child)

    Return the next available child node handle for a node

    :param fwnode:
        Firmware node to find the next child node for.
    :type fwnode: const struct fwnode_handle \*

    :param child:
        Handle to one of the node's child nodes or a \ ``NULL``\  handle.
    :type child: struct fwnode_handle \*

.. _`device_get_next_child_node`:

device_get_next_child_node
==========================

.. c:function:: struct fwnode_handle *device_get_next_child_node(struct device *dev, struct fwnode_handle *child)

    Return the next child node handle for a device

    :param dev:
        Device to find the next child node for.
    :type dev: struct device \*

    :param child:
        Handle to one of the device's child nodes or a null handle.
    :type child: struct fwnode_handle \*

.. _`fwnode_get_named_child_node`:

fwnode_get_named_child_node
===========================

.. c:function:: struct fwnode_handle *fwnode_get_named_child_node(const struct fwnode_handle *fwnode, const char *childname)

    Return first matching named child node handle

    :param fwnode:
        Firmware node to find the named child node for.
    :type fwnode: const struct fwnode_handle \*

    :param childname:
        String to match child node name against.
    :type childname: const char \*

.. _`device_get_named_child_node`:

device_get_named_child_node
===========================

.. c:function:: struct fwnode_handle *device_get_named_child_node(struct device *dev, const char *childname)

    Return first matching named child node handle

    :param dev:
        Device to find the named child node for.
    :type dev: struct device \*

    :param childname:
        String to match child node name against.
    :type childname: const char \*

.. _`fwnode_handle_get`:

fwnode_handle_get
=================

.. c:function:: struct fwnode_handle *fwnode_handle_get(struct fwnode_handle *fwnode)

    Obtain a reference to a device node

    :param fwnode:
        Pointer to the device node to obtain the reference to.
    :type fwnode: struct fwnode_handle \*

.. _`fwnode_handle_get.description`:

Description
-----------

Returns the fwnode handle.

.. _`fwnode_handle_put`:

fwnode_handle_put
=================

.. c:function:: void fwnode_handle_put(struct fwnode_handle *fwnode)

    Drop reference to a device node

    :param fwnode:
        Pointer to the device node to drop the reference to.
    :type fwnode: struct fwnode_handle \*

.. _`fwnode_handle_put.description`:

Description
-----------

This has to be used when terminating \ :c:func:`device_for_each_child_node`\  iteration
with break or return to prevent stale device node references from being left
behind.

.. _`fwnode_device_is_available`:

fwnode_device_is_available
==========================

.. c:function:: bool fwnode_device_is_available(const struct fwnode_handle *fwnode)

    check if a device is available for use

    :param fwnode:
        Pointer to the fwnode of the device.
    :type fwnode: const struct fwnode_handle \*

.. _`device_get_child_node_count`:

device_get_child_node_count
===========================

.. c:function:: unsigned int device_get_child_node_count(struct device *dev)

    return the number of child nodes for device

    :param dev:
        Device to cound the child nodes for
    :type dev: struct device \*

.. _`fwnode_get_phy_mode`:

fwnode_get_phy_mode
===================

.. c:function:: int fwnode_get_phy_mode(struct fwnode_handle *fwnode)

    Get phy mode for given firmware node

    :param fwnode:
        Pointer to the given node
    :type fwnode: struct fwnode_handle \*

.. _`fwnode_get_phy_mode.description`:

Description
-----------

The function gets phy interface string from property 'phy-mode' or
'phy-connection-type', and return its index in phy_modes table, or errno in
error case.

.. _`device_get_phy_mode`:

device_get_phy_mode
===================

.. c:function:: int device_get_phy_mode(struct device *dev)

    Get phy mode for given device

    :param dev:
        Pointer to the given device
    :type dev: struct device \*

.. _`device_get_phy_mode.description`:

Description
-----------

The function gets phy interface string from property 'phy-mode' or
'phy-connection-type', and return its index in phy_modes table, or errno in
error case.

.. _`fwnode_get_mac_address`:

fwnode_get_mac_address
======================

.. c:function:: void *fwnode_get_mac_address(struct fwnode_handle *fwnode, char *addr, int alen)

    Get the MAC from the firmware node

    :param fwnode:
        Pointer to the firmware node
    :type fwnode: struct fwnode_handle \*

    :param addr:
        Address of buffer to store the MAC in
    :type addr: char \*

    :param alen:
        Length of the buffer pointed to by addr, should be ETH_ALEN
    :type alen: int

.. _`fwnode_get_mac_address.description`:

Description
-----------

Search the firmware node for the best MAC address to use.  'mac-address' is
checked first, because that is supposed to contain to "most recent" MAC
address. If that isn't set, then 'local-mac-address' is checked next,
because that is the default address.  If that isn't set, then the obsolete
'address' is checked, just in case we're using an old device tree.

Note that the 'address' property is supposed to contain a virtual address of
the register set, but some DTS files have redefined that property to be the
MAC address.

All-zero MAC addresses are rejected, because those could be properties that
exist in the firmware tables, but were not updated by the firmware.  For
example, the DTS could define 'mac-address' and 'local-mac-address', with
zero MAC addresses.  Some older U-Boots only initialized 'local-mac-address'.
In this case, the real MAC is in 'local-mac-address', and 'mac-address'
exists but is all zeros.

.. _`device_get_mac_address`:

device_get_mac_address
======================

.. c:function:: void *device_get_mac_address(struct device *dev, char *addr, int alen)

    Get the MAC for a given device

    :param dev:
        Pointer to the device
    :type dev: struct device \*

    :param addr:
        Address of buffer to store the MAC in
    :type addr: char \*

    :param alen:
        Length of the buffer pointed to by addr, should be ETH_ALEN
    :type alen: int

.. _`fwnode_irq_get`:

fwnode_irq_get
==============

.. c:function:: int fwnode_irq_get(struct fwnode_handle *fwnode, unsigned int index)

    Get IRQ directly from a fwnode

    :param fwnode:
        Pointer to the firmware node
    :type fwnode: struct fwnode_handle \*

    :param index:
        Zero-based index of the IRQ
    :type index: unsigned int

.. _`fwnode_irq_get.description`:

Description
-----------

Returns Linux IRQ number on success. Other values are determined
accordingly to acpi_/of\_ \ :c:func:`irq_get`\  operation.

.. _`fwnode_graph_get_next_endpoint`:

fwnode_graph_get_next_endpoint
==============================

.. c:function:: struct fwnode_handle *fwnode_graph_get_next_endpoint(const struct fwnode_handle *fwnode, struct fwnode_handle *prev)

    Get next endpoint firmware node

    :param fwnode:
        Pointer to the parent firmware node
    :type fwnode: const struct fwnode_handle \*

    :param prev:
        Previous endpoint node or \ ``NULL``\  to get the first
    :type prev: struct fwnode_handle \*

.. _`fwnode_graph_get_next_endpoint.description`:

Description
-----------

Returns an endpoint firmware node pointer or \ ``NULL``\  if no more endpoints
are available.

.. _`fwnode_graph_get_port_parent`:

fwnode_graph_get_port_parent
============================

.. c:function:: struct fwnode_handle *fwnode_graph_get_port_parent(const struct fwnode_handle *endpoint)

    Return the device fwnode of a port endpoint

    :param endpoint:
        Endpoint firmware node of the port
    :type endpoint: const struct fwnode_handle \*

.. _`fwnode_graph_get_port_parent.return`:

Return
------

the firmware node of the device the \ ``endpoint``\  belongs to.

.. _`fwnode_graph_get_remote_port_parent`:

fwnode_graph_get_remote_port_parent
===================================

.. c:function:: struct fwnode_handle *fwnode_graph_get_remote_port_parent(const struct fwnode_handle *fwnode)

    Return fwnode of a remote device

    :param fwnode:
        Endpoint firmware node pointing to the remote endpoint
    :type fwnode: const struct fwnode_handle \*

.. _`fwnode_graph_get_remote_port_parent.description`:

Description
-----------

Extracts firmware node of a remote device the \ ``fwnode``\  points to.

.. _`fwnode_graph_get_remote_port`:

fwnode_graph_get_remote_port
============================

.. c:function:: struct fwnode_handle *fwnode_graph_get_remote_port(const struct fwnode_handle *fwnode)

    Return fwnode of a remote port

    :param fwnode:
        Endpoint firmware node pointing to the remote endpoint
    :type fwnode: const struct fwnode_handle \*

.. _`fwnode_graph_get_remote_port.description`:

Description
-----------

Extracts firmware node of a remote port the \ ``fwnode``\  points to.

.. _`fwnode_graph_get_remote_endpoint`:

fwnode_graph_get_remote_endpoint
================================

.. c:function:: struct fwnode_handle *fwnode_graph_get_remote_endpoint(const struct fwnode_handle *fwnode)

    Return fwnode of a remote endpoint

    :param fwnode:
        Endpoint firmware node pointing to the remote endpoint
    :type fwnode: const struct fwnode_handle \*

.. _`fwnode_graph_get_remote_endpoint.description`:

Description
-----------

Extracts firmware node of a remote endpoint the \ ``fwnode``\  points to.

.. _`fwnode_graph_get_remote_node`:

fwnode_graph_get_remote_node
============================

.. c:function:: struct fwnode_handle *fwnode_graph_get_remote_node(const struct fwnode_handle *fwnode, u32 port_id, u32 endpoint_id)

    get remote parent node for given port/endpoint

    :param fwnode:
        pointer to parent fwnode_handle containing graph port/endpoint
    :type fwnode: const struct fwnode_handle \*

    :param port_id:
        identifier of the parent port node
    :type port_id: u32

    :param endpoint_id:
        identifier of the endpoint node
    :type endpoint_id: u32

.. _`fwnode_graph_get_remote_node.return`:

Return
------

Remote fwnode handle associated with remote endpoint node linked
to \ ``node``\ . Use \ :c:func:`fwnode_node_put`\  on it when done.

.. _`fwnode_graph_parse_endpoint`:

fwnode_graph_parse_endpoint
===========================

.. c:function:: int fwnode_graph_parse_endpoint(const struct fwnode_handle *fwnode, struct fwnode_endpoint *endpoint)

    parse common endpoint node properties

    :param fwnode:
        pointer to endpoint fwnode_handle
    :type fwnode: const struct fwnode_handle \*

    :param endpoint:
        pointer to the fwnode endpoint data structure
    :type endpoint: struct fwnode_endpoint \*

.. _`fwnode_graph_parse_endpoint.description`:

Description
-----------

Parse \ ``fwnode``\  representing a graph endpoint node and store the
information in \ ``endpoint``\ . The caller must hold a reference to
\ ``fwnode``\ .

.. This file was automatic generated / don't edit.


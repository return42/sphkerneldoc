.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/of/base.c

.. _`of_find_all_nodes`:

of_find_all_nodes
=================

.. c:function:: struct device_node *of_find_all_nodes(struct device_node *prev)

    Get next node in global list

    :param struct device_node \*prev:
        Previous node or NULL to start iteration
        \ :c:func:`of_node_put`\  will be called on it

.. _`of_find_all_nodes.description`:

Description
-----------

Returns a node pointer with refcount incremented, use
\ :c:func:`of_node_put`\  on it when done.

.. _`__of_find_n_match_cpu_property`:

__of_find_n_match_cpu_property
==============================

.. c:function:: bool __of_find_n_match_cpu_property(struct device_node *cpun, const char *prop_name, int cpu, unsigned int *thread)

    core/thread corresponding to the logical cpu 'cpu'. If 'thread' is not NULL, local thread number within the core is returned in it.

    :param struct device_node \*cpun:
        *undescribed*

    :param const char \*prop_name:
        *undescribed*

    :param int cpu:
        *undescribed*

    :param unsigned int \*thread:
        *undescribed*

.. _`of_get_cpu_node`:

of_get_cpu_node
===============

.. c:function:: struct device_node *of_get_cpu_node(int cpu, unsigned int *thread)

    Get device node associated with the given logical CPU

    :param int cpu:
        CPU number(logical index) for which device node is required

    :param unsigned int \*thread:
        if not NULL, local thread number within the physical core is
        returned

.. _`of_get_cpu_node.description`:

Description
-----------

The main purpose of this function is to retrieve the device node for the
given logical CPU index. It should be used to initialize the of_node in
cpu device. Once of_node in cpu device is populated, all the further
references can use that instead.

CPU logical to physical index mapping is architecture specific and is built
before booting secondary cores. This function uses arch_match_cpu_phys_id
which can be overridden by architecture specific implementation.

Returns a node pointer for the logical cpu with refcount incremented, use
\ :c:func:`of_node_put`\  on it when done. Returns NULL if not found.

.. _`__of_device_is_compatible`:

__of_device_is_compatible
=========================

.. c:function:: int __of_device_is_compatible(const struct device_node *device, const char *compat, const char *type, const char *name)

    Check if the node matches given constraints

    :param const struct device_node \*device:
        pointer to node

    :param const char \*compat:
        required compatible string, NULL or "" for any match

    :param const char \*type:
        required device_type value, NULL or "" for any match

    :param const char \*name:
        required node name, NULL or "" for any match

.. _`__of_device_is_compatible.description`:

Description
-----------

Checks if the given \ ``compat``\ , \ ``type``\  and \ ``name``\  strings match the
properties of the given \ ``device``\ . A constraints can be skipped by
passing NULL or an empty string as the constraint.

Returns 0 for no match, and a positive integer on match. The return
value is a relative score with larger values indicating better
matches. The score is weighted for the most specific compatible value
to get the highest score. Matching type is next, followed by matching
name. Practically speaking, this results in the following priority

.. _`__of_device_is_compatible.order-for-matches`:

order for matches
-----------------


1. specific compatible && type && name
2. specific compatible && type
3. specific compatible && name
4. specific compatible
5. general compatible && type && name
6. general compatible && type
7. general compatible && name
8. general compatible
9. type && name
10. type
11. name

.. _`of_machine_is_compatible`:

of_machine_is_compatible
========================

.. c:function:: int of_machine_is_compatible(const char *compat)

    Test root of device tree for a given compatible value

    :param const char \*compat:
        compatible string to look for in root node's compatible property.

.. _`of_machine_is_compatible.description`:

Description
-----------

Returns a positive integer if the root node has the given value in its
compatible property.

.. _`__of_device_is_available`:

__of_device_is_available
========================

.. c:function:: bool __of_device_is_available(const struct device_node *device)

    check if a device is available for use

    :param const struct device_node \*device:
        Node to check for availability, with locks already held

.. _`__of_device_is_available.description`:

Description
-----------

Returns true if the status property is absent or set to "okay" or "ok",
false otherwise

.. _`of_device_is_available`:

of_device_is_available
======================

.. c:function:: bool of_device_is_available(const struct device_node *device)

    check if a device is available for use

    :param const struct device_node \*device:
        Node to check for availability

.. _`of_device_is_available.description`:

Description
-----------

Returns true if the status property is absent or set to "okay" or "ok",
false otherwise

.. _`of_device_is_big_endian`:

of_device_is_big_endian
=======================

.. c:function:: bool of_device_is_big_endian(const struct device_node *device)

    check if a device has BE registers

    :param const struct device_node \*device:
        Node to check for endianness

.. _`of_device_is_big_endian.description`:

Description
-----------

Returns true if the device has a "big-endian" property, or if the kernel
was compiled for BE \*and\* the device has a "native-endian" property.
Returns false otherwise.

Callers would nominally use ioread32be/iowrite32be if
\ :c:func:`of_device_is_big_endian`\  == true, or readl/writel otherwise.

.. _`of_get_parent`:

of_get_parent
=============

.. c:function:: struct device_node *of_get_parent(const struct device_node *node)

    Get a node's parent if any

    :param const struct device_node \*node:
        Node to get parent

.. _`of_get_parent.description`:

Description
-----------

Returns a node pointer with refcount incremented, use
\ :c:func:`of_node_put`\  on it when done.

.. _`of_get_next_parent`:

of_get_next_parent
==================

.. c:function:: struct device_node *of_get_next_parent(struct device_node *node)

    Iterate to a node's parent

    :param struct device_node \*node:
        Node to get parent of

.. _`of_get_next_parent.description`:

Description
-----------

This is like \ :c:func:`of_get_parent`\  except that it drops the
refcount on the passed node, making it suitable for iterating
through a node's parents.

Returns a node pointer with refcount incremented, use
\ :c:func:`of_node_put`\  on it when done.

.. _`of_get_next_child`:

of_get_next_child
=================

.. c:function:: struct device_node *of_get_next_child(const struct device_node *node, struct device_node *prev)

    Iterate a node childs

    :param const struct device_node \*node:
        parent node

    :param struct device_node \*prev:
        previous child of the parent node, or NULL to get first

.. _`of_get_next_child.description`:

Description
-----------

Returns a node pointer with refcount incremented, use \ :c:func:`of_node_put`\  on
it when done. Returns NULL when prev is the last child. Decrements the
refcount of prev.

.. _`of_get_next_available_child`:

of_get_next_available_child
===========================

.. c:function:: struct device_node *of_get_next_available_child(const struct device_node *node, struct device_node *prev)

    Find the next available child node

    :param const struct device_node \*node:
        parent node

    :param struct device_node \*prev:
        previous child of the parent node, or NULL to get first

.. _`of_get_next_available_child.description`:

Description
-----------

This function is like \ :c:func:`of_get_next_child`\ , except that it
automatically skips any disabled nodes (i.e. status = "disabled").

.. _`of_get_child_by_name`:

of_get_child_by_name
====================

.. c:function:: struct device_node *of_get_child_by_name(const struct device_node *node, const char *name)

    Find the child node by name for a given parent

    :param const struct device_node \*node:
        parent node

    :param const char \*name:
        child name to look for.

.. _`of_get_child_by_name.description`:

Description
-----------

This function looks for child node for given matching name

Returns a node pointer if found, with refcount incremented, use
\ :c:func:`of_node_put`\  on it when done.
Returns NULL if node is not found.

.. _`of_find_node_opts_by_path`:

of_find_node_opts_by_path
=========================

.. c:function:: struct device_node *of_find_node_opts_by_path(const char *path, const char **opts)

    Find a node matching a full OF path

    :param const char \*path:
        Either the full path to match, or if the path does not
        start with '/', the name of a property of the /aliases
        node (an alias).  In the case of an alias, the node
        matching the alias' value will be returned.

    :param const char \*\*opts:
        Address of a pointer into which to store the start of
        an options string appended to the end of the path with
        a ':' separator.

.. _`of_find_node_opts_by_path.valid-paths`:

Valid paths
-----------

/foo/bar        Full path
foo             Valid alias
foo/bar         Valid alias + relative path

Returns a node pointer with refcount incremented, use
\ :c:func:`of_node_put`\  on it when done.

.. _`of_find_node_by_name`:

of_find_node_by_name
====================

.. c:function:: struct device_node *of_find_node_by_name(struct device_node *from, const char *name)

    Find a node by its "name" property

    :param struct device_node \*from:
        The node to start searching from or NULL, the node
        you pass will not be searched, only the next one
        will; typically, you pass what the previous call
        returned. \ :c:func:`of_node_put`\  will be called on it

    :param const char \*name:
        The name string to match against

.. _`of_find_node_by_name.description`:

Description
-----------

Returns a node pointer with refcount incremented, use
\ :c:func:`of_node_put`\  on it when done.

.. _`of_find_node_by_type`:

of_find_node_by_type
====================

.. c:function:: struct device_node *of_find_node_by_type(struct device_node *from, const char *type)

    Find a node by its "device_type" property

    :param struct device_node \*from:
        The node to start searching from, or NULL to start searching
        the entire device tree. The node you pass will not be
        searched, only the next one will; typically, you pass
        what the previous call returned. \ :c:func:`of_node_put`\  will be
        called on from for you.

    :param const char \*type:
        The type string to match against

.. _`of_find_node_by_type.description`:

Description
-----------

Returns a node pointer with refcount incremented, use
\ :c:func:`of_node_put`\  on it when done.

.. _`of_find_compatible_node`:

of_find_compatible_node
=======================

.. c:function:: struct device_node *of_find_compatible_node(struct device_node *from, const char *type, const char *compatible)

    Find a node based on type and one of the tokens in its "compatible" property

    :param struct device_node \*from:
        The node to start searching from or NULL, the node
        you pass will not be searched, only the next one
        will; typically, you pass what the previous call
        returned. \ :c:func:`of_node_put`\  will be called on it

    :param const char \*type:
        The type string to match "device_type" or NULL to ignore

    :param const char \*compatible:
        The string to match to one of the tokens in the device
        "compatible" list.

.. _`of_find_compatible_node.description`:

Description
-----------

Returns a node pointer with refcount incremented, use
\ :c:func:`of_node_put`\  on it when done.

.. _`of_find_node_with_property`:

of_find_node_with_property
==========================

.. c:function:: struct device_node *of_find_node_with_property(struct device_node *from, const char *prop_name)

    Find a node which has a property with the given name.

    :param struct device_node \*from:
        The node to start searching from or NULL, the node
        you pass will not be searched, only the next one
        will; typically, you pass what the previous call
        returned. \ :c:func:`of_node_put`\  will be called on it

    :param const char \*prop_name:
        The name of the property to look for.

.. _`of_find_node_with_property.description`:

Description
-----------

Returns a node pointer with refcount incremented, use
\ :c:func:`of_node_put`\  on it when done.

.. _`of_match_node`:

of_match_node
=============

.. c:function:: const struct of_device_id *of_match_node(const struct of_device_id *matches, const struct device_node *node)

    Tell if a device_node has a matching of_match structure

    :param const struct of_device_id \*matches:
        array of of device match structures to search in

    :param const struct device_node \*node:
        the of device structure to match against

.. _`of_match_node.description`:

Description
-----------

Low level utility function used by device matching.

.. _`of_find_matching_node_and_match`:

of_find_matching_node_and_match
===============================

.. c:function:: struct device_node *of_find_matching_node_and_match(struct device_node *from, const struct of_device_id *matches, const struct of_device_id **match)

    Find a node based on an of_device_id match table.

    :param struct device_node \*from:
        The node to start searching from or NULL, the node
        you pass will not be searched, only the next one
        will; typically, you pass what the previous call
        returned. \ :c:func:`of_node_put`\  will be called on it

    :param const struct of_device_id \*matches:
        array of of device match structures to search in
        \ ``match``\           Updated to point at the matches entry which matched

    :param const struct of_device_id \*\*match:
        *undescribed*

.. _`of_find_matching_node_and_match.description`:

Description
-----------

Returns a node pointer with refcount incremented, use
\ :c:func:`of_node_put`\  on it when done.

.. _`of_modalias_node`:

of_modalias_node
================

.. c:function:: int of_modalias_node(struct device_node *node, char *modalias, int len)

    Lookup appropriate modalias for a device node

    :param struct device_node \*node:
        pointer to a device tree node

    :param char \*modalias:
        Pointer to buffer that modalias value will be copied into

    :param int len:
        Length of modalias value

.. _`of_modalias_node.description`:

Description
-----------

Based on the value of the compatible property, this routine will attempt
to choose an appropriate modalias value for a particular device tree node.
It does this by stripping the manufacturer prefix (as delimited by a ',')
from the first entry in the compatible list property.

This routine returns 0 on success, <0 on failure.

.. _`of_find_node_by_phandle`:

of_find_node_by_phandle
=======================

.. c:function:: struct device_node *of_find_node_by_phandle(phandle handle)

    Find a node given a phandle

    :param phandle handle:
        phandle of the node to find

.. _`of_find_node_by_phandle.description`:

Description
-----------

Returns a node pointer with refcount incremented, use
\ :c:func:`of_node_put`\  on it when done.

.. _`of_property_count_elems_of_size`:

of_property_count_elems_of_size
===============================

.. c:function:: int of_property_count_elems_of_size(const struct device_node *np, const char *propname, int elem_size)

    Count the number of elements in a property

    :param const struct device_node \*np:
        device node from which the property value is to be read.

    :param const char \*propname:
        name of the property to be searched.

    :param int elem_size:
        size of the individual element

.. _`of_property_count_elems_of_size.description`:

Description
-----------

Search for a property in a device node and count the number of elements of
size elem_size in it. Returns number of elements on sucess, -EINVAL if the
property does not exist or its length does not match a multiple of elem_size
and -ENODATA if the property does not have a value.

.. _`of_find_property_value_of_size`:

of_find_property_value_of_size
==============================

.. c:function:: void *of_find_property_value_of_size(const struct device_node *np, const char *propname, u32 min, u32 max, size_t *len)

    :param const struct device_node \*np:
        device node from which the property value is to be read.

    :param const char \*propname:
        name of the property to be searched.

    :param u32 min:
        minimum allowed length of property value

    :param u32 max:
        maximum allowed length of property value (0 means unlimited)

    :param size_t \*len:
        if !=NULL, actual length is written to here

.. _`of_find_property_value_of_size.description`:

Description
-----------

Search for a property in a device node and valid the requested size.
Returns the property value on success, -EINVAL if the property does not
exist, -ENODATA if property does not have a value, and -EOVERFLOW if the
property data is too small or too large.

.. _`of_property_read_u32_index`:

of_property_read_u32_index
==========================

.. c:function:: int of_property_read_u32_index(const struct device_node *np, const char *propname, u32 index, u32 *out_value)

    Find and read a u32 from a multi-value property.

    :param const struct device_node \*np:
        device node from which the property value is to be read.

    :param const char \*propname:
        name of the property to be searched.

    :param u32 index:
        index of the u32 in the list of values

    :param u32 \*out_value:
        pointer to return value, modified only if no error.

.. _`of_property_read_u32_index.description`:

Description
-----------

Search for a property in a device node and read nth 32-bit value from
it. Returns 0 on success, -EINVAL if the property does not exist,
-ENODATA if property does not have a value, and -EOVERFLOW if the
property data isn't large enough.

The out_value is modified only if a valid u32 value can be decoded.

.. _`of_property_read_variable_u8_array`:

of_property_read_variable_u8_array
==================================

.. c:function:: int of_property_read_variable_u8_array(const struct device_node *np, const char *propname, u8 *out_values, size_t sz_min, size_t sz_max)

    Find and read an array of u8 from a property, with bounds on the minimum and maximum array size.

    :param const struct device_node \*np:
        device node from which the property value is to be read.

    :param const char \*propname:
        name of the property to be searched.

    :param u8 \*out_values:
        pointer to return value, modified only if return value is 0.

    :param size_t sz_min:
        minimum number of array elements to read

    :param size_t sz_max:
        maximum number of array elements to read, if zero there is no
        upper limit on the number of elements in the dts entry but only
        sz_min will be read.

.. _`of_property_read_variable_u8_array.description`:

Description
-----------

Search for a property in a device node and read 8-bit value(s) from
it. Returns number of elements read on success, -EINVAL if the property
does not exist, -ENODATA if property does not have a value, and -EOVERFLOW
if the property data is smaller than sz_min or longer than sz_max.

.. _`of_property_read_variable_u8_array.dts-entry-of-array-should-be-like`:

dts entry of array should be like
---------------------------------

property = /bits/ 8 <0x50 0x60 0x70>;

The out_values is modified only if a valid u8 value can be decoded.

.. _`of_property_read_variable_u16_array`:

of_property_read_variable_u16_array
===================================

.. c:function:: int of_property_read_variable_u16_array(const struct device_node *np, const char *propname, u16 *out_values, size_t sz_min, size_t sz_max)

    Find and read an array of u16 from a property, with bounds on the minimum and maximum array size.

    :param const struct device_node \*np:
        device node from which the property value is to be read.

    :param const char \*propname:
        name of the property to be searched.

    :param u16 \*out_values:
        pointer to return value, modified only if return value is 0.

    :param size_t sz_min:
        minimum number of array elements to read

    :param size_t sz_max:
        maximum number of array elements to read, if zero there is no
        upper limit on the number of elements in the dts entry but only
        sz_min will be read.

.. _`of_property_read_variable_u16_array.description`:

Description
-----------

Search for a property in a device node and read 16-bit value(s) from
it. Returns number of elements read on success, -EINVAL if the property
does not exist, -ENODATA if property does not have a value, and -EOVERFLOW
if the property data is smaller than sz_min or longer than sz_max.

.. _`of_property_read_variable_u16_array.dts-entry-of-array-should-be-like`:

dts entry of array should be like
---------------------------------

property = /bits/ 16 <0x5000 0x6000 0x7000>;

The out_values is modified only if a valid u16 value can be decoded.

.. _`of_property_read_variable_u32_array`:

of_property_read_variable_u32_array
===================================

.. c:function:: int of_property_read_variable_u32_array(const struct device_node *np, const char *propname, u32 *out_values, size_t sz_min, size_t sz_max)

    Find and read an array of 32 bit integers from a property, with bounds on the minimum and maximum array size.

    :param const struct device_node \*np:
        device node from which the property value is to be read.

    :param const char \*propname:
        name of the property to be searched.

    :param u32 \*out_values:
        pointer to return value, modified only if return value is 0.

    :param size_t sz_min:
        minimum number of array elements to read

    :param size_t sz_max:
        maximum number of array elements to read, if zero there is no
        upper limit on the number of elements in the dts entry but only
        sz_min will be read.

.. _`of_property_read_variable_u32_array.description`:

Description
-----------

Search for a property in a device node and read 32-bit value(s) from
it. Returns number of elements read on success, -EINVAL if the property
does not exist, -ENODATA if property does not have a value, and -EOVERFLOW
if the property data is smaller than sz_min or longer than sz_max.

The out_values is modified only if a valid u32 value can be decoded.

.. _`of_property_read_u64`:

of_property_read_u64
====================

.. c:function:: int of_property_read_u64(const struct device_node *np, const char *propname, u64 *out_value)

    Find and read a 64 bit integer from a property

    :param const struct device_node \*np:
        device node from which the property value is to be read.

    :param const char \*propname:
        name of the property to be searched.

    :param u64 \*out_value:
        pointer to return value, modified only if return value is 0.

.. _`of_property_read_u64.description`:

Description
-----------

Search for a property in a device node and read a 64-bit value from
it. Returns 0 on success, -EINVAL if the property does not exist,
-ENODATA if property does not have a value, and -EOVERFLOW if the
property data isn't large enough.

The out_value is modified only if a valid u64 value can be decoded.

.. _`of_property_read_variable_u64_array`:

of_property_read_variable_u64_array
===================================

.. c:function:: int of_property_read_variable_u64_array(const struct device_node *np, const char *propname, u64 *out_values, size_t sz_min, size_t sz_max)

    Find and read an array of 64 bit integers from a property, with bounds on the minimum and maximum array size.

    :param const struct device_node \*np:
        device node from which the property value is to be read.

    :param const char \*propname:
        name of the property to be searched.

    :param u64 \*out_values:
        pointer to return value, modified only if return value is 0.

    :param size_t sz_min:
        minimum number of array elements to read

    :param size_t sz_max:
        maximum number of array elements to read, if zero there is no
        upper limit on the number of elements in the dts entry but only
        sz_min will be read.

.. _`of_property_read_variable_u64_array.description`:

Description
-----------

Search for a property in a device node and read 64-bit value(s) from
it. Returns number of elements read on success, -EINVAL if the property
does not exist, -ENODATA if property does not have a value, and -EOVERFLOW
if the property data is smaller than sz_min or longer than sz_max.

The out_values is modified only if a valid u64 value can be decoded.

.. _`of_property_read_string`:

of_property_read_string
=======================

.. c:function:: int of_property_read_string(const struct device_node *np, const char *propname, const char **out_string)

    Find and read a string from a property

    :param const struct device_node \*np:
        device node from which the property value is to be read.

    :param const char \*propname:
        name of the property to be searched.

    :param const char \*\*out_string:
        pointer to null terminated return string, modified only if
        return value is 0.

.. _`of_property_read_string.description`:

Description
-----------

Search for a property in a device tree node and retrieve a null
terminated string value (pointer to data, not a copy). Returns 0 on
success, -EINVAL if the property does not exist, -ENODATA if property
does not have a value, and -EILSEQ if the string is not null-terminated
within the length of the property data.

The out_string pointer is modified only if a valid string can be decoded.

.. _`of_property_match_string`:

of_property_match_string
========================

.. c:function:: int of_property_match_string(const struct device_node *np, const char *propname, const char *string)

    Find string in a list and return index

    :param const struct device_node \*np:
        pointer to node containing string list property

    :param const char \*propname:
        string list property name

    :param const char \*string:
        pointer to string to search for in string list

.. _`of_property_match_string.description`:

Description
-----------

This function searches a string list property and returns the index
of a specific string value.

.. _`of_property_read_string_helper`:

of_property_read_string_helper
==============================

.. c:function:: int of_property_read_string_helper(const struct device_node *np, const char *propname, const char **out_strs, size_t sz, int skip)

    Utility helper for parsing string properties

    :param const struct device_node \*np:
        device node from which the property value is to be read.

    :param const char \*propname:
        name of the property to be searched.

    :param const char \*\*out_strs:
        output array of string pointers.

    :param size_t sz:
        number of array elements to read.

    :param int skip:
        Number of strings to skip over at beginning of list.

.. _`of_property_read_string_helper.description`:

Description
-----------

Don't call this function directly. It is a utility helper for the
of_property_read_string\*() family of functions.

.. _`of_parse_phandle`:

of_parse_phandle
================

.. c:function:: struct device_node *of_parse_phandle(const struct device_node *np, const char *phandle_name, int index)

    Resolve a phandle property to a device_node pointer

    :param const struct device_node \*np:
        Pointer to device node holding phandle property

    :param const char \*phandle_name:
        Name of property holding a phandle value

    :param int index:
        For properties holding a table of phandles, this is the index into
        the table

.. _`of_parse_phandle.description`:

Description
-----------

Returns the device_node pointer with refcount incremented.  Use
\ :c:func:`of_node_put`\  on it when done.

.. _`of_parse_phandle_with_args`:

of_parse_phandle_with_args
==========================

.. c:function:: int of_parse_phandle_with_args(const struct device_node *np, const char *list_name, const char *cells_name, int index, struct of_phandle_args *out_args)

    Find a node pointed by phandle in a list

    :param const struct device_node \*np:
        pointer to a device tree node containing a list

    :param const char \*list_name:
        property name that contains a list

    :param const char \*cells_name:
        property name that specifies phandles' arguments count

    :param int index:
        index of a phandle to parse out

    :param struct of_phandle_args \*out_args:
        optional pointer to output arguments structure (will be filled)

.. _`of_parse_phandle_with_args.description`:

Description
-----------

This function is useful to parse lists of phandles and their arguments.
Returns 0 on success and fills out_args, on error returns appropriate
errno value.

Caller is responsible to call \ :c:func:`of_node_put`\  on the returned out_args->np
pointer.

.. _`of_parse_phandle_with_args.phandle1`:

phandle1
--------

node1 {
#list-cells = <2>;
}

.. _`of_parse_phandle_with_args.phandle2`:

phandle2
--------

node2 {
#list-cells = <1>;
}

node3 {
list = <&phandle1 1 2 \ :c:type:`struct phandle2 <phandle2>`\  3>;
}

To get a device_node of the \`node2' node you may call this:
of_parse_phandle_with_args(node3, "list", "#list-cells", 1, \ :c:type:`struct args <args>`\ );

.. _`of_parse_phandle_with_fixed_args`:

of_parse_phandle_with_fixed_args
================================

.. c:function:: int of_parse_phandle_with_fixed_args(const struct device_node *np, const char *list_name, int cell_count, int index, struct of_phandle_args *out_args)

    Find a node pointed by phandle in a list

    :param const struct device_node \*np:
        pointer to a device tree node containing a list

    :param const char \*list_name:
        property name that contains a list

    :param int cell_count:
        number of argument cells following the phandle

    :param int index:
        index of a phandle to parse out

    :param struct of_phandle_args \*out_args:
        optional pointer to output arguments structure (will be filled)

.. _`of_parse_phandle_with_fixed_args.description`:

Description
-----------

This function is useful to parse lists of phandles and their arguments.
Returns 0 on success and fills out_args, on error returns appropriate
errno value.

Caller is responsible to call \ :c:func:`of_node_put`\  on the returned out_args->np
pointer.

.. _`of_parse_phandle_with_fixed_args.phandle1`:

phandle1
--------

node1 {
}

.. _`of_parse_phandle_with_fixed_args.phandle2`:

phandle2
--------

node2 {
}

node3 {
list = <&phandle1 0 2 \ :c:type:`struct phandle2 <phandle2>`\  2 3>;
}

To get a device_node of the \`node2' node you may call this:
of_parse_phandle_with_fixed_args(node3, "list", 2, 1, \ :c:type:`struct args <args>`\ );

.. _`of_count_phandle_with_args`:

of_count_phandle_with_args
==========================

.. c:function:: int of_count_phandle_with_args(const struct device_node *np, const char *list_name, const char *cells_name)

    Find the number of phandles references in a property

    :param const struct device_node \*np:
        pointer to a device tree node containing a list

    :param const char \*list_name:
        property name that contains a list

    :param const char \*cells_name:
        property name that specifies phandles' arguments count

.. _`of_count_phandle_with_args.description`:

Description
-----------

Returns the number of phandle + argument tuples within a property. It
is a typical pattern to encode a list of phandle and variable
arguments into a single property. The number of arguments is encoded
by a property in the phandle-target node. For example, a gpios
property would contain a list of GPIO specifies consisting of a
phandle and 1 or more arguments. The number of arguments are
determined by the #gpio-cells property in the node pointed to by the
phandle.

.. _`__of_add_property`:

__of_add_property
=================

.. c:function:: int __of_add_property(struct device_node *np, struct property *prop)

    Add a property to a node without lock operations

    :param struct device_node \*np:
        *undescribed*

    :param struct property \*prop:
        *undescribed*

.. _`of_add_property`:

of_add_property
===============

.. c:function:: int of_add_property(struct device_node *np, struct property *prop)

    Add a property to a node

    :param struct device_node \*np:
        *undescribed*

    :param struct property \*prop:
        *undescribed*

.. _`of_remove_property`:

of_remove_property
==================

.. c:function:: int of_remove_property(struct device_node *np, struct property *prop)

    Remove a property from a node.

    :param struct device_node \*np:
        *undescribed*

    :param struct property \*prop:
        *undescribed*

.. _`of_remove_property.description`:

Description
-----------

Note that we don't actually remove it, since we have given out
who-knows-how-many pointers to the data using get-property.
Instead we just move the property to the "dead properties"
list, so it won't be found any more.

.. _`of_alias_scan`:

of_alias_scan
=============

.. c:function:: void of_alias_scan(void * (*dt_alloc)(u64 size, u64 align))

    Scan all properties of the 'aliases' node

    :param void \* (\*dt_alloc)(u64 size, u64 align):
        An allocator that provides a virtual address to memory
        for storing the resulting tree

.. _`of_alias_scan.description`:

Description
-----------

The function scans all the properties of the 'aliases' node and populates
the global lookup table with the properties.  It returns the
number of alias properties found, or an error code in case of failure.

.. _`of_alias_get_id`:

of_alias_get_id
===============

.. c:function:: int of_alias_get_id(struct device_node *np, const char *stem)

    Get alias id for the given device_node

    :param struct device_node \*np:
        Pointer to the given device_node

    :param const char \*stem:
        Alias stem of the given device_node

.. _`of_alias_get_id.description`:

Description
-----------

The function travels the lookup table to get the alias id for the given
device_node and alias stem.  It returns the alias id if found.

.. _`of_alias_get_highest_id`:

of_alias_get_highest_id
=======================

.. c:function:: int of_alias_get_highest_id(const char *stem)

    Get highest alias id for the given stem

    :param const char \*stem:
        Alias stem to be examined

.. _`of_alias_get_highest_id.description`:

Description
-----------

The function travels the lookup table to get the highest alias id for the
given alias stem.  It returns the alias id if found.

.. _`of_console_check`:

of_console_check
================

.. c:function:: bool of_console_check(struct device_node *dn, char *name, int index)

    Test and setup console for DT setup \ ``dn``\  - Pointer to device node \ ``name``\  - Name to use for preferred console without index. ex. "ttyS" \ ``index``\  - Index to use for preferred console.

    :param struct device_node \*dn:
        *undescribed*

    :param char \*name:
        *undescribed*

    :param int index:
        *undescribed*

.. _`of_console_check.description`:

Description
-----------

Check if the given device node matches the stdout-path property in the
/chosen node. If it does then register it as the preferred console and return
TRUE. Otherwise return FALSE.

.. _`of_find_next_cache_node`:

of_find_next_cache_node
=======================

.. c:function:: struct device_node *of_find_next_cache_node(const struct device_node *np)

    Find a node's subsidiary cache

    :param const struct device_node \*np:
        node of type "cpu" or "cache"

.. _`of_find_next_cache_node.description`:

Description
-----------

Returns a node pointer with refcount incremented, use
\ :c:func:`of_node_put`\  on it when done.  Caller should hold a reference
to np.

.. _`of_graph_parse_endpoint`:

of_graph_parse_endpoint
=======================

.. c:function:: int of_graph_parse_endpoint(const struct device_node *node, struct of_endpoint *endpoint)

    parse common endpoint node properties

    :param const struct device_node \*node:
        pointer to endpoint device_node

    :param struct of_endpoint \*endpoint:
        pointer to the OF endpoint data structure

.. _`of_graph_parse_endpoint.description`:

Description
-----------

The caller should hold a reference to \ ``node``\ .

.. _`of_graph_get_port_by_id`:

of_graph_get_port_by_id
=======================

.. c:function:: struct device_node *of_graph_get_port_by_id(struct device_node *parent, u32 id)

    get the port matching a given id

    :param struct device_node \*parent:
        pointer to the parent device node

    :param u32 id:
        id of the port

.. _`of_graph_get_port_by_id.return`:

Return
------

A 'port' node pointer with refcount incremented. The caller
has to use \ :c:func:`of_node_put`\  on it when done.

.. _`of_graph_get_next_endpoint`:

of_graph_get_next_endpoint
==========================

.. c:function:: struct device_node *of_graph_get_next_endpoint(const struct device_node *parent, struct device_node *prev)

    get next endpoint node

    :param const struct device_node \*parent:
        pointer to the parent device node

    :param struct device_node \*prev:
        previous endpoint node, or NULL to get first

.. _`of_graph_get_next_endpoint.return`:

Return
------

An 'endpoint' node pointer with refcount incremented. Refcount
of the passed \ ``prev``\  node is decremented.

.. _`of_graph_get_endpoint_by_regs`:

of_graph_get_endpoint_by_regs
=============================

.. c:function:: struct device_node *of_graph_get_endpoint_by_regs(const struct device_node *parent, int port_reg, int reg)

    get endpoint node of specific identifiers

    :param const struct device_node \*parent:
        pointer to the parent device node

    :param int port_reg:
        identifier (value of reg property) of the parent port node

    :param int reg:
        identifier (value of reg property) of the endpoint node

.. _`of_graph_get_endpoint_by_regs.return`:

Return
------

An 'endpoint' node pointer which is identified by reg and at the same
is the child of a port node identified by port_reg. reg and port_reg are
ignored when they are -1.

.. _`of_graph_get_remote_port_parent`:

of_graph_get_remote_port_parent
===============================

.. c:function:: struct device_node *of_graph_get_remote_port_parent(const struct device_node *node)

    get remote port's parent node

    :param const struct device_node \*node:
        pointer to a local endpoint device_node

.. _`of_graph_get_remote_port_parent.return`:

Return
------

Remote device node associated with remote endpoint node linked
to \ ``node``\ . Use \ :c:func:`of_node_put`\  on it when done.

.. _`of_graph_get_remote_port`:

of_graph_get_remote_port
========================

.. c:function:: struct device_node *of_graph_get_remote_port(const struct device_node *node)

    get remote port node

    :param const struct device_node \*node:
        pointer to a local endpoint device_node

.. _`of_graph_get_remote_port.return`:

Return
------

Remote port node associated with remote endpoint node linked
to \ ``node``\ . Use \ :c:func:`of_node_put`\  on it when done.

.. This file was automatic generated / don't edit.


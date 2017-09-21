.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/of/property.c

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

.. _`of_property_read_u64_index`:

of_property_read_u64_index
==========================

.. c:function:: int of_property_read_u64_index(const struct device_node *np, const char *propname, u32 index, u64 *out_value)

    Find and read a u64 from a multi-value property.

    :param const struct device_node \*np:
        device node from which the property value is to be read.

    :param const char \*propname:
        name of the property to be searched.

    :param u32 index:
        index of the u64 in the list of values

    :param u64 \*out_value:
        pointer to return value, modified only if no error.

.. _`of_property_read_u64_index.description`:

Description
-----------

Search for a property in a device node and read nth 64-bit value from
it. Returns 0 on success, -EINVAL if the property does not exist,
-ENODATA if property does not have a value, and -EOVERFLOW if the
property data isn't large enough.

The out_value is modified only if a valid u64 value can be decoded.

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

.. _`of_graph_get_remote_endpoint`:

of_graph_get_remote_endpoint
============================

.. c:function:: struct device_node *of_graph_get_remote_endpoint(const struct device_node *node)

    get remote endpoint node

    :param const struct device_node \*node:
        pointer to a local endpoint device_node

.. _`of_graph_get_remote_endpoint.return`:

Return
------

Remote endpoint node associated with remote endpoint node linked
to \ ``node``\ . Use \ :c:func:`of_node_put`\  on it when done.

.. _`of_graph_get_port_parent`:

of_graph_get_port_parent
========================

.. c:function:: struct device_node *of_graph_get_port_parent(struct device_node *node)

    get port's parent node

    :param struct device_node \*node:
        pointer to a local endpoint device_node

.. _`of_graph_get_port_parent.return`:

Return
------

device node associated with endpoint node linked
to \ ``node``\ . Use \ :c:func:`of_node_put`\  on it when done.

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

.. _`of_graph_get_remote_node`:

of_graph_get_remote_node
========================

.. c:function:: struct device_node *of_graph_get_remote_node(const struct device_node *node, u32 port, u32 endpoint)

    get remote parent device_node for given port/endpoint

    :param const struct device_node \*node:
        pointer to parent device_node containing graph port/endpoint

    :param u32 port:
        identifier (value of reg property) of the parent port node

    :param u32 endpoint:
        identifier (value of reg property) of the endpoint node

.. _`of_graph_get_remote_node.return`:

Return
------

Remote device node associated with remote endpoint node linked
to \ ``node``\ . Use \ :c:func:`of_node_put`\  on it when done.

.. This file was automatic generated / don't edit.


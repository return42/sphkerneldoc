.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/property.c

.. _`device_property_present`:

device_property_present
=======================

.. c:function:: bool device_property_present(struct device *dev, const char *propname)

    check if a property of a device is present

    :param struct device \*dev:
        Device whose property is being checked

    :param const char \*propname:
        Name of the property

.. _`device_property_present.description`:

Description
-----------

Check if property \ ``propname``\  is present in the device firmware description.

.. _`fwnode_property_present`:

fwnode_property_present
=======================

.. c:function:: bool fwnode_property_present(struct fwnode_handle *fwnode, const char *propname)

    check if a property of a firmware node is present

    :param struct fwnode_handle \*fwnode:
        Firmware node whose property to check

    :param const char \*propname:
        Name of the property

.. _`device_property_read_u8_array`:

device_property_read_u8_array
=============================

.. c:function:: int device_property_read_u8_array(struct device *dev, const char *propname, u8 *val, size_t nval)

    return a u8 array property of a device

    :param struct device \*dev:
        Device to get the property of

    :param const char \*propname:
        Name of the property

    :param u8 \*val:
        The values are stored here or \ ``NULL``\  to return the number of values

    :param size_t nval:
        Size of the \ ``val``\  array

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

    :param struct device \*dev:
        Device to get the property of

    :param const char \*propname:
        Name of the property

    :param u16 \*val:
        The values are stored here or \ ``NULL``\  to return the number of values

    :param size_t nval:
        Size of the \ ``val``\  array

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

    :param struct device \*dev:
        Device to get the property of

    :param const char \*propname:
        Name of the property

    :param u32 \*val:
        The values are stored here or \ ``NULL``\  to return the number of values

    :param size_t nval:
        Size of the \ ``val``\  array

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

    :param struct device \*dev:
        Device to get the property of

    :param const char \*propname:
        Name of the property

    :param u64 \*val:
        The values are stored here or \ ``NULL``\  to return the number of values

    :param size_t nval:
        Size of the \ ``val``\  array

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

    :param struct device \*dev:
        Device to get the property of

    :param const char \*propname:
        Name of the property

    :param const char \*\*val:
        The values are stored here or \ ``NULL``\  to return the number of values

    :param size_t nval:
        Size of the \ ``val``\  array

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

    :param struct device \*dev:
        Device to get the property of

    :param const char \*propname:
        Name of the property

    :param const char \*\*val:
        The value is stored here

.. _`device_property_read_string.description`:

Description
-----------

Function reads property \ ``propname``\  from the device firmware description and
stores the value into \ ``val``\  if found. The value is checked to be a string.

.. _`device_property_read_string.return`:

Return
------

%0 if the property was found (success),
\ ``-EINVAL``\  if given arguments are not valid,
\ ``-ENODATA``\  if the property does not have a value,
\ ``-EPROTO``\  or \ ``-EILSEQ``\  if the property type is not a string.
\ ``-ENXIO``\  if no suitable firmware interface is present.

.. _`device_property_match_string`:

device_property_match_string
============================

.. c:function:: int device_property_match_string(struct device *dev, const char *propname, const char *string)

    find a string in an array and return index

    :param struct device \*dev:
        Device to get the property of

    :param const char \*propname:
        Name of the property holding the array

    :param const char \*string:
        String to look for

.. _`device_property_match_string.description`:

Description
-----------

Find a given string in a string array and if it is found return the
index back.

.. _`device_property_match_string.return`:

Return
------

%0 if the property was found (success),
\ ``-EINVAL``\  if given arguments are not valid,
\ ``-ENODATA``\  if the property does not have a value,
\ ``-EPROTO``\  if the property is not an array of strings,
\ ``-ENXIO``\  if no suitable firmware interface is present.

.. _`fwnode_property_read_u8_array`:

fwnode_property_read_u8_array
=============================

.. c:function:: int fwnode_property_read_u8_array(struct fwnode_handle *fwnode, const char *propname, u8 *val, size_t nval)

    return a u8 array property of firmware node

    :param struct fwnode_handle \*fwnode:
        Firmware node to get the property of

    :param const char \*propname:
        Name of the property

    :param u8 \*val:
        The values are stored here or \ ``NULL``\  to return the number of values

    :param size_t nval:
        Size of the \ ``val``\  array

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

.. c:function:: int fwnode_property_read_u16_array(struct fwnode_handle *fwnode, const char *propname, u16 *val, size_t nval)

    return a u16 array property of firmware node

    :param struct fwnode_handle \*fwnode:
        Firmware node to get the property of

    :param const char \*propname:
        Name of the property

    :param u16 \*val:
        The values are stored here or \ ``NULL``\  to return the number of values

    :param size_t nval:
        Size of the \ ``val``\  array

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

.. c:function:: int fwnode_property_read_u32_array(struct fwnode_handle *fwnode, const char *propname, u32 *val, size_t nval)

    return a u32 array property of firmware node

    :param struct fwnode_handle \*fwnode:
        Firmware node to get the property of

    :param const char \*propname:
        Name of the property

    :param u32 \*val:
        The values are stored here or \ ``NULL``\  to return the number of values

    :param size_t nval:
        Size of the \ ``val``\  array

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

.. c:function:: int fwnode_property_read_u64_array(struct fwnode_handle *fwnode, const char *propname, u64 *val, size_t nval)

    return a u64 array property firmware node

    :param struct fwnode_handle \*fwnode:
        Firmware node to get the property of

    :param const char \*propname:
        Name of the property

    :param u64 \*val:
        The values are stored here or \ ``NULL``\  to return the number of values

    :param size_t nval:
        Size of the \ ``val``\  array

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

.. c:function:: int fwnode_property_read_string_array(struct fwnode_handle *fwnode, const char *propname, const char **val, size_t nval)

    return string array property of a node

    :param struct fwnode_handle \*fwnode:
        Firmware node to get the property of

    :param const char \*propname:
        Name of the property

    :param const char \*\*val:
        The values are stored here or \ ``NULL``\  to return the number of values

    :param size_t nval:
        Size of the \ ``val``\  array

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

.. c:function:: int fwnode_property_read_string(struct fwnode_handle *fwnode, const char *propname, const char **val)

    return a string property of a firmware node

    :param struct fwnode_handle \*fwnode:
        Firmware node to get the property of

    :param const char \*propname:
        Name of the property

    :param const char \*\*val:
        The value is stored here

.. _`fwnode_property_read_string.description`:

Description
-----------

Read property \ ``propname``\  from the given firmware node and store the value into
\ ``val``\  if found.  The value is checked to be a string.

.. _`fwnode_property_read_string.return`:

Return
------

%0 if the property was found (success),
\ ``-EINVAL``\  if given arguments are not valid,
\ ``-ENODATA``\  if the property does not have a value,
\ ``-EPROTO``\  or \ ``-EILSEQ``\  if the property is not a string,
\ ``-ENXIO``\  if no suitable firmware interface is present.

.. _`fwnode_property_match_string`:

fwnode_property_match_string
============================

.. c:function:: int fwnode_property_match_string(struct fwnode_handle *fwnode, const char *propname, const char *string)

    find a string in an array and return index

    :param struct fwnode_handle \*fwnode:
        Firmware node to get the property of

    :param const char \*propname:
        Name of the property holding the array

    :param const char \*string:
        String to look for

.. _`fwnode_property_match_string.description`:

Description
-----------

Find a given string in a string array and if it is found return the
index back.

.. _`fwnode_property_match_string.return`:

Return
------

%0 if the property was found (success),
\ ``-EINVAL``\  if given arguments are not valid,
\ ``-ENODATA``\  if the property does not have a value,
\ ``-EPROTO``\  if the property is not an array of strings,
\ ``-ENXIO``\  if no suitable firmware interface is present.

.. _`property_entries_dup`:

property_entries_dup
====================

.. c:function:: struct property_entry *property_entries_dup(const struct property_entry *properties)

    duplicate array of properties

    :param const struct property_entry \*properties:
        array of properties to copy

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

    :param const struct property_entry \*properties:
        array of properties to destroy

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

    :param struct property_set \*pset:
        Property set to release

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

    :param const struct property_set \*pset:
        Property set to copy

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

    :param struct device \*dev:
        Device whose properties to remove.

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

    :param struct device \*dev:
        Device to add properties to.

    :param const struct property_entry \*properties:
        Collection of properties to add.

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

    :param struct fwnode_handle \*fwnode:
        Firmware whose parent is retrieved

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

.. c:function:: struct fwnode_handle *fwnode_get_parent(struct fwnode_handle *fwnode)

    Return parent firwmare node

    :param struct fwnode_handle \*fwnode:
        Firmware whose parent is retrieved

.. _`fwnode_get_parent.description`:

Description
-----------

Return parent firmware node of the given node if possible or \ ``NULL``\  if no
parent was available.

.. _`fwnode_get_next_child_node`:

fwnode_get_next_child_node
==========================

.. c:function:: struct fwnode_handle *fwnode_get_next_child_node(struct fwnode_handle *fwnode, struct fwnode_handle *child)

    Return the next child node handle for a node

    :param struct fwnode_handle \*fwnode:
        Firmware node to find the next child node for.

    :param struct fwnode_handle \*child:
        Handle to one of the node's child nodes or a \ ``NULL``\  handle.

.. _`device_get_next_child_node`:

device_get_next_child_node
==========================

.. c:function:: struct fwnode_handle *device_get_next_child_node(struct device *dev, struct fwnode_handle *child)

    Return the next child node handle for a device

    :param struct device \*dev:
        Device to find the next child node for.

    :param struct fwnode_handle \*child:
        Handle to one of the device's child nodes or a null handle.

.. _`fwnode_get_named_child_node`:

fwnode_get_named_child_node
===========================

.. c:function:: struct fwnode_handle *fwnode_get_named_child_node(struct fwnode_handle *fwnode, const char *childname)

    Return first matching named child node handle

    :param struct fwnode_handle \*fwnode:
        Firmware node to find the named child node for.

    :param const char \*childname:
        String to match child node name against.

.. _`device_get_named_child_node`:

device_get_named_child_node
===========================

.. c:function:: struct fwnode_handle *device_get_named_child_node(struct device *dev, const char *childname)

    Return first matching named child node handle

    :param struct device \*dev:
        Device to find the named child node for.

    :param const char \*childname:
        String to match child node name against.

.. _`fwnode_handle_get`:

fwnode_handle_get
=================

.. c:function:: void fwnode_handle_get(struct fwnode_handle *fwnode)

    Obtain a reference to a device node

    :param struct fwnode_handle \*fwnode:
        Pointer to the device node to obtain the reference to.

.. _`fwnode_handle_put`:

fwnode_handle_put
=================

.. c:function:: void fwnode_handle_put(struct fwnode_handle *fwnode)

    Drop reference to a device node

    :param struct fwnode_handle \*fwnode:
        Pointer to the device node to drop the reference to.

.. _`fwnode_handle_put.description`:

Description
-----------

This has to be used when terminating \ :c:func:`device_for_each_child_node`\  iteration
with break or return to prevent stale device node references from being left
behind.

.. _`device_get_child_node_count`:

device_get_child_node_count
===========================

.. c:function:: unsigned int device_get_child_node_count(struct device *dev)

    return the number of child nodes for device

    :param struct device \*dev:
        Device to cound the child nodes for

.. _`device_get_phy_mode`:

device_get_phy_mode
===================

.. c:function:: int device_get_phy_mode(struct device *dev)

    Get phy mode for given device

    :param struct device \*dev:
        Pointer to the given device

.. _`device_get_phy_mode.description`:

Description
-----------

The function gets phy interface string from property 'phy-mode' or
'phy-connection-type', and return its index in phy_modes table, or errno in
error case.

.. _`device_get_mac_address`:

device_get_mac_address
======================

.. c:function:: void *device_get_mac_address(struct device *dev, char *addr, int alen)

    Get the MAC for a given device

    :param struct device \*dev:
        Pointer to the device

    :param char \*addr:
        Address of buffer to store the MAC in

    :param int alen:
        Length of the buffer pointed to by addr, should be ETH_ALEN

.. _`device_get_mac_address.description`:

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

.. _`fwnode_graph_get_next_endpoint`:

fwnode_graph_get_next_endpoint
==============================

.. c:function:: struct fwnode_handle *fwnode_graph_get_next_endpoint(struct fwnode_handle *fwnode, struct fwnode_handle *prev)

    Get next endpoint firmware node

    :param struct fwnode_handle \*fwnode:
        Pointer to the parent firmware node

    :param struct fwnode_handle \*prev:
        Previous endpoint node or \ ``NULL``\  to get the first

.. _`fwnode_graph_get_next_endpoint.description`:

Description
-----------

Returns an endpoint firmware node pointer or \ ``NULL``\  if no more endpoints
are available.

.. _`fwnode_graph_get_remote_port_parent`:

fwnode_graph_get_remote_port_parent
===================================

.. c:function:: struct fwnode_handle *fwnode_graph_get_remote_port_parent(struct fwnode_handle *fwnode)

    Return fwnode of a remote device

    :param struct fwnode_handle \*fwnode:
        Endpoint firmware node pointing to the remote endpoint

.. _`fwnode_graph_get_remote_port_parent.description`:

Description
-----------

Extracts firmware node of a remote device the \ ``fwnode``\  points to.

.. _`fwnode_graph_get_remote_port`:

fwnode_graph_get_remote_port
============================

.. c:function:: struct fwnode_handle *fwnode_graph_get_remote_port(struct fwnode_handle *fwnode)

    Return fwnode of a remote port

    :param struct fwnode_handle \*fwnode:
        Endpoint firmware node pointing to the remote endpoint

.. _`fwnode_graph_get_remote_port.description`:

Description
-----------

Extracts firmware node of a remote port the \ ``fwnode``\  points to.

.. _`fwnode_graph_get_remote_endpoint`:

fwnode_graph_get_remote_endpoint
================================

.. c:function:: struct fwnode_handle *fwnode_graph_get_remote_endpoint(struct fwnode_handle *fwnode)

    Return fwnode of a remote endpoint

    :param struct fwnode_handle \*fwnode:
        Endpoint firmware node pointing to the remote endpoint

.. _`fwnode_graph_get_remote_endpoint.description`:

Description
-----------

Extracts firmware node of a remote endpoint the \ ``fwnode``\  points to.

.. _`fwnode_graph_parse_endpoint`:

fwnode_graph_parse_endpoint
===========================

.. c:function:: int fwnode_graph_parse_endpoint(struct fwnode_handle *fwnode, struct fwnode_endpoint *endpoint)

    parse common endpoint node properties

    :param struct fwnode_handle \*fwnode:
        pointer to endpoint fwnode_handle

    :param struct fwnode_endpoint \*endpoint:
        pointer to the fwnode endpoint data structure

.. _`fwnode_graph_parse_endpoint.description`:

Description
-----------

Parse \ ``fwnode``\  representing a graph endpoint node and store the
information in \ ``endpoint``\ . The caller must hold a reference to
\ ``fwnode``\ .

.. This file was automatic generated / don't edit.


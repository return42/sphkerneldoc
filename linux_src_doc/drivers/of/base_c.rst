.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/of/base.c

.. _`of_find_all_nodes`:

of_find_all_nodes
=================

.. c:function:: struct device_node *of_find_all_nodes(struct device_node *prev)

    Get next node in global list

    :param prev:
        Previous node or NULL to start iteration
        \ :c:func:`of_node_put`\  will be called on it
    :type prev: struct device_node \*

.. _`of_find_all_nodes.description`:

Description
-----------

Returns a node pointer with refcount incremented, use
\ :c:func:`of_node_put`\  on it when done.

.. _`__of_find_n_match_cpu_property`:

\__of_find_n_match_cpu_property
===============================

.. c:function:: bool __of_find_n_match_cpu_property(struct device_node *cpun, const char *prop_name, int cpu, unsigned int *thread)

    core/thread corresponding to the logical cpu 'cpu'. If 'thread' is not NULL, local thread number within the core is returned in it.

    :param cpun:
        *undescribed*
    :type cpun: struct device_node \*

    :param prop_name:
        *undescribed*
    :type prop_name: const char \*

    :param cpu:
        *undescribed*
    :type cpu: int

    :param thread:
        *undescribed*
    :type thread: unsigned int \*

.. _`of_get_cpu_node`:

of_get_cpu_node
===============

.. c:function:: struct device_node *of_get_cpu_node(int cpu, unsigned int *thread)

    Get device node associated with the given logical CPU

    :param cpu:
        CPU number(logical index) for which device node is required
    :type cpu: int

    :param thread:
        if not NULL, local thread number within the physical core is
        returned
    :type thread: unsigned int \*

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

.. _`of_cpu_node_to_id`:

of_cpu_node_to_id
=================

.. c:function:: int of_cpu_node_to_id(struct device_node *cpu_node)

    Get the logical CPU number for a given device_node

    :param cpu_node:
        Pointer to the device_node for CPU.
    :type cpu_node: struct device_node \*

.. _`of_cpu_node_to_id.description`:

Description
-----------

Returns the logical CPU number of the given CPU device_node.
Returns -ENODEV if the CPU is not found.

.. _`__of_device_is_compatible`:

\__of_device_is_compatible
==========================

.. c:function:: int __of_device_is_compatible(const struct device_node *device, const char *compat, const char *type, const char *name)

    Check if the node matches given constraints

    :param device:
        pointer to node
    :type device: const struct device_node \*

    :param compat:
        required compatible string, NULL or "" for any match
    :type compat: const char \*

    :param type:
        required device_type value, NULL or "" for any match
    :type type: const char \*

    :param name:
        required node name, NULL or "" for any match
    :type name: const char \*

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

    :param compat:
        compatible string to look for in root node's compatible property.
    :type compat: const char \*

.. _`of_machine_is_compatible.description`:

Description
-----------

Returns a positive integer if the root node has the given value in its
compatible property.

.. _`__of_device_is_available`:

\__of_device_is_available
=========================

.. c:function:: bool __of_device_is_available(const struct device_node *device)

    check if a device is available for use

    :param device:
        Node to check for availability, with locks already held
    :type device: const struct device_node \*

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

    :param device:
        Node to check for availability
    :type device: const struct device_node \*

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

    :param device:
        Node to check for endianness
    :type device: const struct device_node \*

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

    :param node:
        Node to get parent
    :type node: const struct device_node \*

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

    :param node:
        Node to get parent of
    :type node: struct device_node \*

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

    :param node:
        parent node
    :type node: const struct device_node \*

    :param prev:
        previous child of the parent node, or NULL to get first
    :type prev: struct device_node \*

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

    :param node:
        parent node
    :type node: const struct device_node \*

    :param prev:
        previous child of the parent node, or NULL to get first
    :type prev: struct device_node \*

.. _`of_get_next_available_child.description`:

Description
-----------

This function is like \ :c:func:`of_get_next_child`\ , except that it
automatically skips any disabled nodes (i.e. status = "disabled").

.. _`of_get_next_cpu_node`:

of_get_next_cpu_node
====================

.. c:function:: struct device_node *of_get_next_cpu_node(struct device_node *prev)

    Iterate on cpu nodes

    :param prev:
        previous child of the /cpus node, or NULL to get first
    :type prev: struct device_node \*

.. _`of_get_next_cpu_node.description`:

Description
-----------

Returns a cpu node pointer with refcount incremented, use \ :c:func:`of_node_put`\ 
on it when done. Returns NULL when prev is the last child. Decrements
the refcount of prev.

.. _`of_get_compatible_child`:

of_get_compatible_child
=======================

.. c:function:: struct device_node *of_get_compatible_child(const struct device_node *parent, const char *compatible)

    Find compatible child node

    :param parent:
        parent node
    :type parent: const struct device_node \*

    :param compatible:
        compatible string
    :type compatible: const char \*

.. _`of_get_compatible_child.description`:

Description
-----------

Lookup child node whose compatible property contains the given compatible
string.

Returns a node pointer with refcount incremented, use \ :c:func:`of_node_put`\  on it
when done; or NULL if not found.

.. _`of_get_child_by_name`:

of_get_child_by_name
====================

.. c:function:: struct device_node *of_get_child_by_name(const struct device_node *node, const char *name)

    Find the child node by name for a given parent

    :param node:
        parent node
    :type node: const struct device_node \*

    :param name:
        child name to look for.
    :type name: const char \*

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

    :param path:
        Either the full path to match, or if the path does not
        start with '/', the name of a property of the /aliases
        node (an alias).  In the case of an alias, the node
        matching the alias' value will be returned.
    :type path: const char \*

    :param opts:
        Address of a pointer into which to store the start of
        an options string appended to the end of the path with
        a ':' separator.
    :type opts: const char \*\*

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

    :param from:
        The node to start searching from or NULL; the node
        you pass will not be searched, only the next one
        will. Typically, you pass what the previous call
        returned. \ :c:func:`of_node_put`\  will be called on \ ``from``\ .
    :type from: struct device_node \*

    :param name:
        The name string to match against
    :type name: const char \*

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

    :param from:
        The node to start searching from, or NULL to start searching
        the entire device tree. The node you pass will not be
        searched, only the next one will; typically, you pass
        what the previous call returned. \ :c:func:`of_node_put`\  will be
        called on from for you.
    :type from: struct device_node \*

    :param type:
        The type string to match against
    :type type: const char \*

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

    :param from:
        The node to start searching from or NULL, the node
        you pass will not be searched, only the next one
        will; typically, you pass what the previous call
        returned. \ :c:func:`of_node_put`\  will be called on it
    :type from: struct device_node \*

    :param type:
        The type string to match "device_type" or NULL to ignore
    :type type: const char \*

    :param compatible:
        The string to match to one of the tokens in the device
        "compatible" list.
    :type compatible: const char \*

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

    :param from:
        The node to start searching from or NULL, the node
        you pass will not be searched, only the next one
        will; typically, you pass what the previous call
        returned. \ :c:func:`of_node_put`\  will be called on it
    :type from: struct device_node \*

    :param prop_name:
        The name of the property to look for.
    :type prop_name: const char \*

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

    :param matches:
        array of of device match structures to search in
    :type matches: const struct of_device_id \*

    :param node:
        the of device structure to match against
    :type node: const struct device_node \*

.. _`of_match_node.description`:

Description
-----------

Low level utility function used by device matching.

.. _`of_find_matching_node_and_match`:

of_find_matching_node_and_match
===============================

.. c:function:: struct device_node *of_find_matching_node_and_match(struct device_node *from, const struct of_device_id *matches, const struct of_device_id **match)

    Find a node based on an of_device_id match table.

    :param from:
        The node to start searching from or NULL, the node
        you pass will not be searched, only the next one
        will; typically, you pass what the previous call
        returned. \ :c:func:`of_node_put`\  will be called on it
    :type from: struct device_node \*

    :param matches:
        array of of device match structures to search in
        \ ``match``\           Updated to point at the matches entry which matched
    :type matches: const struct of_device_id \*

    :param match:
        *undescribed*
    :type match: const struct of_device_id \*\*

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

    :param node:
        pointer to a device tree node
    :type node: struct device_node \*

    :param modalias:
        Pointer to buffer that modalias value will be copied into
    :type modalias: char \*

    :param len:
        Length of modalias value
    :type len: int

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

    :param handle:
        phandle of the node to find
    :type handle: phandle

.. _`of_find_node_by_phandle.description`:

Description
-----------

Returns a node pointer with refcount incremented, use
\ :c:func:`of_node_put`\  on it when done.

.. _`of_parse_phandle`:

of_parse_phandle
================

.. c:function:: struct device_node *of_parse_phandle(const struct device_node *np, const char *phandle_name, int index)

    Resolve a phandle property to a device_node pointer

    :param np:
        Pointer to device node holding phandle property
    :type np: const struct device_node \*

    :param phandle_name:
        Name of property holding a phandle value
    :type phandle_name: const char \*

    :param index:
        For properties holding a table of phandles, this is the index into
        the table
    :type index: int

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

    :param np:
        pointer to a device tree node containing a list
    :type np: const struct device_node \*

    :param list_name:
        property name that contains a list
    :type list_name: const char \*

    :param cells_name:
        property name that specifies phandles' arguments count
    :type cells_name: const char \*

    :param index:
        index of a phandle to parse out
    :type index: int

    :param out_args:
        optional pointer to output arguments structure (will be filled)
    :type out_args: struct of_phandle_args \*

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

.. _`of_parse_phandle_with_args_map`:

of_parse_phandle_with_args_map
==============================

.. c:function:: int of_parse_phandle_with_args_map(const struct device_node *np, const char *list_name, const char *stem_name, int index, struct of_phandle_args *out_args)

    Find a node pointed by phandle in a list and remap it

    :param np:
        pointer to a device tree node containing a list
    :type np: const struct device_node \*

    :param list_name:
        property name that contains a list
    :type list_name: const char \*

    :param stem_name:
        stem of property names that specify phandles' arguments count
    :type stem_name: const char \*

    :param index:
        index of a phandle to parse out
    :type index: int

    :param out_args:
        optional pointer to output arguments structure (will be filled)
    :type out_args: struct of_phandle_args \*

.. _`of_parse_phandle_with_args_map.description`:

Description
-----------

This function is useful to parse lists of phandles and their arguments.
Returns 0 on success and fills out_args, on error returns appropriate errno
value. The difference between this function and \ :c:func:`of_parse_phandle_with_args`\ 
is that this API remaps a phandle if the node the phandle points to has
a <@stem_name>-map property.

Caller is responsible to call \ :c:func:`of_node_put`\  on the returned out_args->np
pointer.

.. _`of_parse_phandle_with_args_map.phandle1`:

phandle1
--------

node1 {
#list-cells = <2>;
}

.. _`of_parse_phandle_with_args_map.phandle2`:

phandle2
--------

node2 {
#list-cells = <1>;
}

.. _`of_parse_phandle_with_args_map.phandle3`:

phandle3
--------

node3 {
#list-cells = <1>;
list-map = <0 \ :c:type:`struct phandle2 <phandle2>`\  3>,
<1 \ :c:type:`struct phandle2 <phandle2>`\  2>,
<2 \ :c:type:`struct phandle1 <phandle1>`\  5 1>;
list-map-mask = <0x3>;
};

node4 {
list = <&phandle1 1 2 \ :c:type:`struct phandle3 <phandle3>`\  0>;
}

To get a device_node of the \`node2' node you may call this:
of_parse_phandle_with_args(node4, "list", "list", 1, \ :c:type:`struct args <args>`\ );

.. _`of_parse_phandle_with_fixed_args`:

of_parse_phandle_with_fixed_args
================================

.. c:function:: int of_parse_phandle_with_fixed_args(const struct device_node *np, const char *list_name, int cell_count, int index, struct of_phandle_args *out_args)

    Find a node pointed by phandle in a list

    :param np:
        pointer to a device tree node containing a list
    :type np: const struct device_node \*

    :param list_name:
        property name that contains a list
    :type list_name: const char \*

    :param cell_count:
        number of argument cells following the phandle
    :type cell_count: int

    :param index:
        index of a phandle to parse out
    :type index: int

    :param out_args:
        optional pointer to output arguments structure (will be filled)
    :type out_args: struct of_phandle_args \*

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

    :param np:
        pointer to a device tree node containing a list
    :type np: const struct device_node \*

    :param list_name:
        property name that contains a list
    :type list_name: const char \*

    :param cells_name:
        property name that specifies phandles' arguments count
    :type cells_name: const char \*

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

\__of_add_property
==================

.. c:function:: int __of_add_property(struct device_node *np, struct property *prop)

    Add a property to a node without lock operations

    :param np:
        *undescribed*
    :type np: struct device_node \*

    :param prop:
        *undescribed*
    :type prop: struct property \*

.. _`of_add_property`:

of_add_property
===============

.. c:function:: int of_add_property(struct device_node *np, struct property *prop)

    Add a property to a node

    :param np:
        *undescribed*
    :type np: struct device_node \*

    :param prop:
        *undescribed*
    :type prop: struct property \*

.. _`of_remove_property`:

of_remove_property
==================

.. c:function:: int of_remove_property(struct device_node *np, struct property *prop)

    Remove a property from a node.

    :param np:
        *undescribed*
    :type np: struct device_node \*

    :param prop:
        *undescribed*
    :type prop: struct property \*

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

    :param np:
        Pointer to the given device_node
    :type np: struct device_node \*

    :param stem:
        Alias stem of the given device_node
    :type stem: const char \*

.. _`of_alias_get_id.description`:

Description
-----------

The function travels the lookup table to get the alias id for the given
device_node and alias stem.  It returns the alias id if found.

.. _`of_alias_get_alias_list`:

of_alias_get_alias_list
=======================

.. c:function:: int of_alias_get_alias_list(const struct of_device_id *matches, const char *stem, unsigned long *bitmap, unsigned int nbits)

    Get alias list for the given device driver

    :param matches:
        Array of OF device match structures to search in
    :type matches: const struct of_device_id \*

    :param stem:
        Alias stem of the given device_node
    :type stem: const char \*

    :param bitmap:
        Bitmap field pointer
    :type bitmap: unsigned long \*

    :param nbits:
        Maximum number of alias IDs which can be recorded in bitmap
    :type nbits: unsigned int

.. _`of_alias_get_alias_list.description`:

Description
-----------

The function travels the lookup table to record alias ids for the given
device match structures and alias stem.

.. _`of_alias_get_alias_list.return`:

Return
------

0 or -ENOSYS when !CONFIG_OF or
-EOVERFLOW if alias ID is greater then allocated nbits

.. _`of_alias_get_highest_id`:

of_alias_get_highest_id
=======================

.. c:function:: int of_alias_get_highest_id(const char *stem)

    Get highest alias id for the given stem

    :param stem:
        Alias stem to be examined
    :type stem: const char \*

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

    :param dn:
        *undescribed*
    :type dn: struct device_node \*

    :param name:
        *undescribed*
    :type name: char \*

    :param index:
        *undescribed*
    :type index: int

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

    :param np:
        node of type "cpu" or "cache"
    :type np: const struct device_node \*

.. _`of_find_next_cache_node.description`:

Description
-----------

Returns a node pointer with refcount incremented, use
\ :c:func:`of_node_put`\  on it when done.  Caller should hold a reference
to np.

.. _`of_find_last_cache_level`:

of_find_last_cache_level
========================

.. c:function:: int of_find_last_cache_level(unsigned int cpu)

    Find the level at which the last cache is present for the given logical cpu

    :param cpu:
        cpu number(logical index) for which the last cache level is needed
    :type cpu: unsigned int

.. _`of_find_last_cache_level.description`:

Description
-----------

Returns the the level at which the last cache is present. It is exactly
same as  the total number of cache levels for the given logical cpu.

.. _`of_map_rid`:

of_map_rid
==========

.. c:function:: int of_map_rid(struct device_node *np, u32 rid, const char *map_name, const char *map_mask_name, struct device_node **target, u32 *id_out)

    Translate a requester ID through a downstream mapping.

    :param np:
        root complex device node.
    :type np: struct device_node \*

    :param rid:
        device requester ID to map.
    :type rid: u32

    :param map_name:
        property name of the map to use.
    :type map_name: const char \*

    :param map_mask_name:
        optional property name of the mask to use.
    :type map_mask_name: const char \*

    :param target:
        optional pointer to a target device node.
    :type target: struct device_node \*\*

    :param id_out:
        optional pointer to receive the translated ID.
    :type id_out: u32 \*

.. _`of_map_rid.description`:

Description
-----------

Given a device requester ID, look up the appropriate implementation-defined
platform ID and/or the target device which receives transactions on that
ID, as per the "iommu-map" and "msi-map" bindings. Either of \ ``target``\  or
\ ``id_out``\  may be NULL if only the other is required. If \ ``target``\  points to
a non-NULL device node pointer, only entries targeting that node will be
matched; if it points to a NULL value, it will receive the device node of
the first matching target phandle, with a reference held.

.. _`of_map_rid.return`:

Return
------

0 on success or a standard error code on failure.

.. This file was automatic generated / don't edit.


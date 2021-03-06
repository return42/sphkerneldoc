.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/of/fdt.c

.. _`of_fdt_is_compatible`:

of_fdt_is_compatible
====================

.. c:function:: int of_fdt_is_compatible(const void *blob, unsigned long node, const char *compat)

    Return true if given node from the given blob has compat in its compatible list

    :param blob:
        A device tree blob
    :type blob: const void \*

    :param node:
        node to test
    :type node: unsigned long

    :param compat:
        compatible string to compare with compatible list.
    :type compat: const char \*

.. _`of_fdt_is_compatible.description`:

Description
-----------

On match, returns a non-zero value with smaller values returned for more
specific compatible values.

.. _`of_fdt_is_big_endian`:

of_fdt_is_big_endian
====================

.. c:function:: bool of_fdt_is_big_endian(const void *blob, unsigned long node)

    Return true if given node needs BE MMIO accesses

    :param blob:
        A device tree blob
    :type blob: const void \*

    :param node:
        node to test
    :type node: unsigned long

.. _`of_fdt_is_big_endian.description`:

Description
-----------

Returns true if the node has a "big-endian" property, or if the kernel
was compiled for BE \*and\* the node has a "native-endian" property.
Returns false otherwise.

.. _`of_fdt_match`:

of_fdt_match
============

.. c:function:: int of_fdt_match(const void *blob, unsigned long node, const char *const *compat)

    Return true if node matches a list of compatible values

    :param blob:
        *undescribed*
    :type blob: const void \*

    :param node:
        *undescribed*
    :type node: unsigned long

    :param compat:
        *undescribed*
    :type compat: const char \*const \*

.. _`unflatten_dt_nodes`:

unflatten_dt_nodes
==================

.. c:function:: int unflatten_dt_nodes(const void *blob, void *mem, struct device_node *dad, struct device_node **nodepp)

    Alloc and populate a device_node from the flat tree

    :param blob:
        The parent device tree blob
    :type blob: const void \*

    :param mem:
        Memory chunk to use for allocating device nodes and properties
    :type mem: void \*

    :param dad:
        Parent struct device_node
    :type dad: struct device_node \*

    :param nodepp:
        The device_node tree created by the call
    :type nodepp: struct device_node \*\*

.. _`unflatten_dt_nodes.description`:

Description
-----------

It returns the size of unflattened device tree or error code

.. _`__unflatten_device_tree`:

\__unflatten_device_tree
========================

.. c:function:: void *__unflatten_device_tree(const void *blob, struct device_node *dad, struct device_node **mynodes, void *(*dt_alloc)(u64 size, u64 align), bool detached)

    create tree of device_nodes from flat blob

    :param blob:
        The blob to expand
    :type blob: const void \*

    :param dad:
        Parent device node
    :type dad: struct device_node \*

    :param mynodes:
        The device_node tree created by the call
    :type mynodes: struct device_node \*\*

    :param void \*(\*dt_alloc)(u64 size, u64 align):
        An allocator that provides a virtual address to memory
        for the resulting tree

    :param detached:
        if true set OF_DETACHED on \ ``mynodes``\ 
    :type detached: bool

.. _`__unflatten_device_tree.description`:

Description
-----------

unflattens a device-tree, creating the
tree of struct device_node. It also fills the "name" and "type"
pointers of the nodes so the normal device-tree walking functions
can be used.

Returns NULL on failure or the memory chunk containing the unflattened
device tree on success.

.. _`of_fdt_unflatten_tree`:

of_fdt_unflatten_tree
=====================

.. c:function:: void *of_fdt_unflatten_tree(const unsigned long *blob, struct device_node *dad, struct device_node **mynodes)

    create tree of device_nodes from flat blob

    :param blob:
        Flat device tree blob
    :type blob: const unsigned long \*

    :param dad:
        Parent device node
    :type dad: struct device_node \*

    :param mynodes:
        The device tree created by the call
    :type mynodes: struct device_node \*\*

.. _`of_fdt_unflatten_tree.description`:

Description
-----------

unflattens the device-tree passed by the firmware, creating the
tree of struct device_node. It also fills the "name" and "type"
pointers of the nodes so the normal device-tree walking functions
can be used.

Returns NULL on failure or the memory chunk containing the unflattened
device tree on success.

.. _`__reserved_mem_reserve_reg`:

\__reserved_mem_reserve_reg
===========================

.. c:function:: int __reserved_mem_reserve_reg(unsigned long node, const char *uname)

    reserve all memory described in 'reg' property

    :param node:
        *undescribed*
    :type node: unsigned long

    :param uname:
        *undescribed*
    :type uname: const char \*

.. _`__reserved_mem_check_root`:

\__reserved_mem_check_root
==========================

.. c:function:: int __reserved_mem_check_root(unsigned long node)

    check if #size-cells, #address-cells provided in /reserved-memory matches the values supported by the current implementation, also check if ranges property has been provided

    :param node:
        *undescribed*
    :type node: unsigned long

.. _`__fdt_scan_reserved_mem`:

\__fdt_scan_reserved_mem
========================

.. c:function:: int __fdt_scan_reserved_mem(unsigned long node, const char *uname, int depth, void *data)

    scan a single FDT node for reserved memory

    :param node:
        *undescribed*
    :type node: unsigned long

    :param uname:
        *undescribed*
    :type uname: const char \*

    :param depth:
        *undescribed*
    :type depth: int

    :param data:
        *undescribed*
    :type data: void \*

.. _`early_init_fdt_scan_reserved_mem`:

early_init_fdt_scan_reserved_mem
================================

.. c:function:: void early_init_fdt_scan_reserved_mem( void)

    create reserved memory regions

    :param void:
        no arguments
    :type void: 

.. _`early_init_fdt_scan_reserved_mem.description`:

Description
-----------

This function grabs memory from early allocator for device exclusive use
defined in device tree structures. It should be called by arch specific code
once the early allocator (i.e. memblock) has been fully activated.

.. _`early_init_fdt_reserve_self`:

early_init_fdt_reserve_self
===========================

.. c:function:: void early_init_fdt_reserve_self( void)

    reserve the memory used by the FDT blob

    :param void:
        no arguments
    :type void: 

.. _`of_scan_flat_dt`:

of_scan_flat_dt
===============

.. c:function:: int of_scan_flat_dt(int (*it)(unsigned long node, const char *uname, int depth, void *data), void *data)

    scan flattened tree blob and call callback on each.

    :param int (\*it)(unsigned long node, const char \*uname, int depth, void \*data):
        callback function

    :param data:
        context data pointer
    :type data: void \*

.. _`of_scan_flat_dt.description`:

Description
-----------

This function is used to scan the flattened device-tree, it is
used to extract the memory information at boot before we can
unflatten the tree

.. _`of_scan_flat_dt_subnodes`:

of_scan_flat_dt_subnodes
========================

.. c:function:: int of_scan_flat_dt_subnodes(unsigned long parent, int (*it)(unsigned long node, const char *uname, void *data), void *data)

    scan sub-nodes of a node call callback on each.

    :param parent:
        *undescribed*
    :type parent: unsigned long

    :param int (\*it)(unsigned long node, const char \*uname, void \*data):
        callback function

    :param data:
        context data pointer
    :type data: void \*

.. _`of_scan_flat_dt_subnodes.description`:

Description
-----------

This function is used to scan sub-nodes of a node.

.. _`of_get_flat_dt_subnode_by_name`:

of_get_flat_dt_subnode_by_name
==============================

.. c:function:: int of_get_flat_dt_subnode_by_name(unsigned long node, const char *uname)

    get the subnode by given name

    :param node:
        the parent node
    :type node: unsigned long

    :param uname:
        the name of subnode
        \ ``return``\  offset of the subnode, or -FDT_ERR_NOTFOUND if there is none
    :type uname: const char \*

.. _`of_get_flat_dt_root`:

of_get_flat_dt_root
===================

.. c:function:: unsigned long of_get_flat_dt_root( void)

    find the root node in the flat blob

    :param void:
        no arguments
    :type void: 

.. _`of_get_flat_dt_size`:

of_get_flat_dt_size
===================

.. c:function:: int of_get_flat_dt_size( void)

    Return the total size of the FDT

    :param void:
        no arguments
    :type void: 

.. _`of_get_flat_dt_prop`:

of_get_flat_dt_prop
===================

.. c:function:: const void *of_get_flat_dt_prop(unsigned long node, const char *name, int *size)

    Given a node in the flat blob, return the property ptr

    :param node:
        *undescribed*
    :type node: unsigned long

    :param name:
        *undescribed*
    :type name: const char \*

    :param size:
        *undescribed*
    :type size: int \*

.. _`of_get_flat_dt_prop.description`:

Description
-----------

This function can be used within scan_flattened_dt callback to get
access to properties

.. _`of_flat_dt_is_compatible`:

of_flat_dt_is_compatible
========================

.. c:function:: int of_flat_dt_is_compatible(unsigned long node, const char *compat)

    Return true if given node has compat in compatible list

    :param node:
        node to test
    :type node: unsigned long

    :param compat:
        compatible string to compare with compatible list.
    :type compat: const char \*

.. _`of_flat_dt_match`:

of_flat_dt_match
================

.. c:function:: int of_flat_dt_match(unsigned long node, const char *const *compat)

    Return true if node matches a list of compatible values

    :param node:
        *undescribed*
    :type node: unsigned long

    :param compat:
        *undescribed*
    :type compat: const char \*const \*

.. _`of_get_flat_dt_phandle`:

of_get_flat_dt_phandle
======================

.. c:function:: uint32_t of_get_flat_dt_phandle(unsigned long node)

    Given a node in the flat blob, return the phandle

    :param node:
        *undescribed*
    :type node: unsigned long

.. _`of_flat_dt_match_machine`:

of_flat_dt_match_machine
========================

.. c:function:: const void *of_flat_dt_match_machine(const void *default_match, const void * (*get_next_compat)(const char * const**))

    Iterate match tables to find matching machine.

    :param default_match:
        A machine specific ptr to return in case of no match.
    :type default_match: const void \*

    :param const void \* (\*get_next_compat)(const char \* const\*\*):
        callback function to return next compatible match table.

.. _`of_flat_dt_match_machine.description`:

Description
-----------

Iterate through machine match tables to find the best match for the machine
compatible string in the FDT.

.. _`early_init_dt_check_for_initrd`:

early_init_dt_check_for_initrd
==============================

.. c:function:: void early_init_dt_check_for_initrd(unsigned long node)

    Decode initrd location from flat tree

    :param node:
        reference to node containing initrd location ('chosen')
    :type node: unsigned long

.. _`early_init_dt_scan_root`:

early_init_dt_scan_root
=======================

.. c:function:: int early_init_dt_scan_root(unsigned long node, const char *uname, int depth, void *data)

    fetch the top level address and size cells

    :param node:
        *undescribed*
    :type node: unsigned long

    :param uname:
        *undescribed*
    :type uname: const char \*

    :param depth:
        *undescribed*
    :type depth: int

    :param data:
        *undescribed*
    :type data: void \*

.. _`early_init_dt_scan_memory`:

early_init_dt_scan_memory
=========================

.. c:function:: int early_init_dt_scan_memory(unsigned long node, const char *uname, int depth, void *data)

    Look for and parse memory nodes

    :param node:
        *undescribed*
    :type node: unsigned long

    :param uname:
        *undescribed*
    :type uname: const char \*

    :param depth:
        *undescribed*
    :type depth: int

    :param data:
        *undescribed*
    :type data: void \*

.. _`unflatten_device_tree`:

unflatten_device_tree
=====================

.. c:function:: void unflatten_device_tree( void)

    create tree of device_nodes from flat blob

    :param void:
        no arguments
    :type void: 

.. _`unflatten_device_tree.description`:

Description
-----------

unflattens the device-tree passed by the firmware, creating the
tree of struct device_node. It also fills the "name" and "type"
pointers of the nodes so the normal device-tree walking functions
can be used.

.. _`unflatten_and_copy_device_tree`:

unflatten_and_copy_device_tree
==============================

.. c:function:: void unflatten_and_copy_device_tree( void)

    copy and create tree of device_nodes from flat blob

    :param void:
        no arguments
    :type void: 

.. _`unflatten_and_copy_device_tree.description`:

Description
-----------

Copies and unflattens the device-tree passed by the firmware, creating the
tree of struct device_node. It also fills the "name" and "type"
pointers of the nodes so the normal device-tree walking functions
can be used. This should only be used when the FDT memory has not been
reserved such is the case when the FDT is built-in to the kernel init
section. If the FDT memory is reserved already then unflatten_device_tree
should be used instead.

.. This file was automatic generated / don't edit.


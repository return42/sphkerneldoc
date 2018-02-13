.. -*- coding: utf-8; mode: rst -*-
.. src-file: scripts/dtc/libfdt/libfdt.h

.. _`fdt_first_subnode`:

fdt_first_subnode
=================

.. c:function:: int fdt_first_subnode(const void *fdt, int offset)

    get offset of first direct subnode

    :param const void \*fdt:
        FDT blob

    :param int offset:
        Offset of node to check
        \ ``return``\  offset of first subnode, or -FDT_ERR_NOTFOUND if there is none

.. _`fdt_next_subnode`:

fdt_next_subnode
================

.. c:function:: int fdt_next_subnode(const void *fdt, int offset)

    get offset of next direct subnode

    :param const void \*fdt:
        FDT blob

    :param int offset:
        Offset of previous subnode
        \ ``return``\  offset of next subnode, or -FDT_ERR_NOTFOUND if there are no more
        subnodes

.. _`fdt_next_subnode.description`:

Description
-----------

After first calling \ :c:func:`fdt_first_subnode`\ , call this function repeatedly to
get direct subnodes of a parent node.

.. _`fdt_for_each_subnode`:

fdt_for_each_subnode
====================

.. c:function::  fdt_for_each_subnode( node,  fdt,  parent)

    iterate over all subnodes of a parent

    :param  node:
        child node (int, lvalue)

    :param  fdt:
        FDT blob (const void \*)

    :param  parent:
        parent node (int)

.. _`fdt_for_each_subnode.this-is-actually-a-wrapper-around-a-for-loop-and-would-be-used-like-so`:

This is actually a wrapper around a for loop and would be used like so
----------------------------------------------------------------------


fdt_for_each_subnode(node, fdt, parent) {
Use node
...
}

if ((node < 0) && (node != -FDT_ERR_NOT_FOUND)) {
Error handling
}

Note that this is implemented as a macro and \ ``node``\  is used as
iterator in the loop. The parent variable be constant or even a
literal.

.. _`fdt_check_header`:

fdt_check_header
================

.. c:function:: int fdt_check_header(const void *fdt)

    sanity check a device tree or possible device tree

    :param const void \*fdt:
        pointer to data which might be a flattened device tree

.. _`fdt_check_header.description`:

Description
-----------

\ :c:func:`fdt_check_header`\  checks that the given buffer contains what
appears to be a flattened device tree with sane information in its
header.

.. _`fdt_check_header.return`:

Return
------

0, if the buffer appears to contain a valid device tree
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE, standard meanings, as above

.. _`fdt_move`:

fdt_move
========

.. c:function:: int fdt_move(const void *fdt, void *buf, int bufsize)

    move a device tree around in memory

    :param const void \*fdt:
        pointer to the device tree to move

    :param void \*buf:
        pointer to memory where the device is to be moved

    :param int bufsize:
        size of the memory space at buf

.. _`fdt_move.description`:

Description
-----------

\ :c:func:`fdt_move`\  relocates, if possible, the device tree blob located at
fdt to the buffer at buf of size bufsize.  The buffer may overlap
with the existing device tree blob at fdt.  Therefore,
fdt_move(fdt, fdt, fdt_totalsize(fdt))
should always succeed.

.. _`fdt_move.return`:

Return
------

0, on success
-FDT_ERR_NOSPACE, bufsize is insufficient to contain the device tree
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE, standard meanings

.. _`fdt_string`:

fdt_string
==========

.. c:function:: const char *fdt_string(const void *fdt, int stroffset)

    retrieve a string from the strings block of a device tree

    :param const void \*fdt:
        pointer to the device tree blob

    :param int stroffset:
        offset of the string within the strings block (native endian)

.. _`fdt_string.description`:

Description
-----------

\ :c:func:`fdt_string`\  retrieves a pointer to a single string from the
strings block of the device tree blob at fdt.

.. _`fdt_string.return`:

Return
------

a pointer to the string, on success
NULL, if stroffset is out of bounds

.. _`fdt_get_max_phandle`:

fdt_get_max_phandle
===================

.. c:function:: uint32_t fdt_get_max_phandle(const void *fdt)

    retrieves the highest phandle in a tree

    :param const void \*fdt:
        pointer to the device tree blob

.. _`fdt_get_max_phandle.description`:

Description
-----------

fdt_get_max_phandle retrieves the highest phandle in the given
device tree. This will ignore badly formatted phandles, or phandles
with a value of 0 or -1.

.. _`fdt_get_max_phandle.return`:

Return
------

the highest phandle on success
0, if no phandle was found in the device tree
-1, if an error occurred

.. _`fdt_num_mem_rsv`:

fdt_num_mem_rsv
===============

.. c:function:: int fdt_num_mem_rsv(const void *fdt)

    retrieve the number of memory reserve map entries

    :param const void \*fdt:
        pointer to the device tree blob

.. _`fdt_num_mem_rsv.description`:

Description
-----------

Returns the number of entries in the device tree blob's memory
reservation map.  This does not include the terminating 0,0 entry
or any other (0,0) entries reserved for expansion.

.. _`fdt_num_mem_rsv.return`:

Return
------

the number of entries

.. _`fdt_get_mem_rsv`:

fdt_get_mem_rsv
===============

.. c:function:: int fdt_get_mem_rsv(const void *fdt, int n, uint64_t *address, uint64_t *size)

    retrieve one memory reserve map entry

    :param const void \*fdt:
        pointer to the device tree blob

    :param int n:
        *undescribed*

    :param uint64_t \*address:
        pointers to 64-bit variables

    :param uint64_t \*size:
        *undescribed*

.. _`fdt_get_mem_rsv.description`:

Description
-----------

On success, \*address and \*size will contain the address and size of
the n-th reserve map entry from the device tree blob, in
native-endian format.

.. _`fdt_get_mem_rsv.return`:

Return
------

0, on success
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE, standard meanings

.. _`fdt_subnode_offset_namelen`:

fdt_subnode_offset_namelen
==========================

.. c:function:: int fdt_subnode_offset_namelen(const void *fdt, int parentoffset, const char *name, int namelen)

    find a subnode based on substring

    :param const void \*fdt:
        pointer to the device tree blob

    :param int parentoffset:
        structure block offset of a node

    :param const char \*name:
        name of the subnode to locate

    :param int namelen:
        number of characters of name to consider

.. _`fdt_subnode_offset_namelen.description`:

Description
-----------

Identical to \ :c:func:`fdt_subnode_offset`\ , but only examine the first
namelen characters of name for matching the subnode name.  This is
useful for finding subnodes based on a portion of a larger string,
such as a full path.

.. _`fdt_subnode_offset`:

fdt_subnode_offset
==================

.. c:function:: int fdt_subnode_offset(const void *fdt, int parentoffset, const char *name)

    find a subnode of a given node

    :param const void \*fdt:
        pointer to the device tree blob

    :param int parentoffset:
        structure block offset of a node

    :param const char \*name:
        name of the subnode to locate

.. _`fdt_subnode_offset.description`:

Description
-----------

\ :c:func:`fdt_subnode_offset`\  finds a subnode of the node at structure block
offset parentoffset with the given name.  name may include a unit
address, in which case \ :c:func:`fdt_subnode_offset`\  will find the subnode
with that unit address, or the unit address may be omitted, in
which case \ :c:func:`fdt_subnode_offset`\  will find an arbitrary subnode
whose name excluding unit address matches the given name.

.. _`fdt_subnode_offset.return`:

Return
------

structure block offset of the requested subnode (>=0), on success
-FDT_ERR_NOTFOUND, if the requested subnode does not exist
-FDT_ERR_BADOFFSET, if parentoffset did not point to an FDT_BEGIN_NODE
tag
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_TRUNCATED, standard meanings.

.. _`fdt_path_offset_namelen`:

fdt_path_offset_namelen
=======================

.. c:function:: int fdt_path_offset_namelen(const void *fdt, const char *path, int namelen)

    find a tree node by its full path

    :param const void \*fdt:
        pointer to the device tree blob

    :param const char \*path:
        full path of the node to locate

    :param int namelen:
        number of characters of path to consider

.. _`fdt_path_offset_namelen.description`:

Description
-----------

Identical to \ :c:func:`fdt_path_offset`\ , but only consider the first namelen
characters of path as the path name.

.. _`fdt_path_offset`:

fdt_path_offset
===============

.. c:function:: int fdt_path_offset(const void *fdt, const char *path)

    find a tree node by its full path

    :param const void \*fdt:
        pointer to the device tree blob

    :param const char \*path:
        full path of the node to locate

.. _`fdt_path_offset.description`:

Description
-----------

\ :c:func:`fdt_path_offset`\  finds a node of a given path in the device tree.
Each path component may omit the unit address portion, but the
results of this are undefined if any such path component is
ambiguous (that is if there are multiple nodes at the relevant
level matching the given component, differentiated only by unit
address).

.. _`fdt_path_offset.return`:

Return
------

structure block offset of the node with the requested path (>=0), on
success
-FDT_ERR_BADPATH, given path does not begin with '/' or is invalid
-FDT_ERR_NOTFOUND, if the requested node does not exist
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_TRUNCATED, standard meanings.

.. _`fdt_get_name`:

fdt_get_name
============

.. c:function:: const char *fdt_get_name(const void *fdt, int nodeoffset, int *lenp)

    retrieve the name of a given node

    :param const void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        structure block offset of the starting node

    :param int \*lenp:
        pointer to an integer variable (will be overwritten) or NULL

.. _`fdt_get_name.description`:

Description
-----------

\ :c:func:`fdt_get_name`\  retrieves the name (including unit address) of the
device tree node at structure block offset nodeoffset.  If lenp is
non-NULL, the length of this name is also returned, in the integer
pointed to by lenp.

.. _`fdt_get_name.return`:

Return
------

pointer to the node's name, on success
If lenp is non-NULL, \*lenp contains the length of that name
(>=0)
NULL, on error
if lenp is non-NULL \*lenp contains an error code (<0):
-FDT_ERR_BADOFFSET, nodeoffset did not point to FDT_BEGIN_NODE
tag
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE, standard meanings

.. _`fdt_first_property_offset`:

fdt_first_property_offset
=========================

.. c:function:: int fdt_first_property_offset(const void *fdt, int nodeoffset)

    find the offset of a node's first property

    :param const void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        structure block offset of a node

.. _`fdt_first_property_offset.description`:

Description
-----------

\ :c:func:`fdt_first_property_offset`\  finds the first property of the node at
the given structure block offset.

.. _`fdt_first_property_offset.return`:

Return
------

structure block offset of the property (>=0), on success
-FDT_ERR_NOTFOUND, if the requested node has no properties
-FDT_ERR_BADOFFSET, if nodeoffset did not point to an FDT_BEGIN_NODE tag
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_TRUNCATED, standard meanings.

.. _`fdt_next_property_offset`:

fdt_next_property_offset
========================

.. c:function:: int fdt_next_property_offset(const void *fdt, int offset)

    step through a node's properties

    :param const void \*fdt:
        pointer to the device tree blob

    :param int offset:
        structure block offset of a property

.. _`fdt_next_property_offset.description`:

Description
-----------

\ :c:func:`fdt_next_property_offset`\  finds the property immediately after the
one at the given structure block offset.  This will be a property
of the same node as the given property.

.. _`fdt_next_property_offset.return`:

Return
------

structure block offset of the next property (>=0), on success
-FDT_ERR_NOTFOUND, if the given property is the last in its node
-FDT_ERR_BADOFFSET, if nodeoffset did not point to an FDT_PROP tag
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_TRUNCATED, standard meanings.

.. _`fdt_for_each_property_offset`:

fdt_for_each_property_offset
============================

.. c:function::  fdt_for_each_property_offset( property,  fdt,  node)

    iterate over all properties of a node

    :param  property:
        *undescribed*

    :param  fdt:
        FDT blob (const void \*)

    :param  node:
        node offset (int)

.. _`fdt_for_each_property_offset.this-is-actually-a-wrapper-around-a-for-loop-and-would-be-used-like-so`:

This is actually a wrapper around a for loop and would be used like so
----------------------------------------------------------------------


fdt_for_each_property_offset(property, fdt, node) {
Use property
...
}

if ((property < 0) && (property != -FDT_ERR_NOT_FOUND)) {
Error handling
}

Note that this is implemented as a macro and property is used as
iterator in the loop. The node variable can be constant or even a
literal.

.. _`fdt_get_property_by_offset`:

fdt_get_property_by_offset
==========================

.. c:function:: const struct fdt_property *fdt_get_property_by_offset(const void *fdt, int offset, int *lenp)

    retrieve the property at a given offset

    :param const void \*fdt:
        pointer to the device tree blob

    :param int offset:
        offset of the property to retrieve

    :param int \*lenp:
        pointer to an integer variable (will be overwritten) or NULL

.. _`fdt_get_property_by_offset.description`:

Description
-----------

\ :c:func:`fdt_get_property_by_offset`\  retrieves a pointer to the
fdt_property structure within the device tree blob at the given
offset.  If lenp is non-NULL, the length of the property value is
also returned, in the integer pointed to by lenp.

.. _`fdt_get_property_by_offset.return`:

Return
------

pointer to the structure representing the property
if lenp is non-NULL, \*lenp contains the length of the property
value (>=0)
NULL, on error
if lenp is non-NULL, \*lenp contains an error code (<0):
-FDT_ERR_BADOFFSET, nodeoffset did not point to FDT_PROP tag
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_TRUNCATED, standard meanings

.. _`fdt_get_property_namelen`:

fdt_get_property_namelen
========================

.. c:function:: const struct fdt_property *fdt_get_property_namelen(const void *fdt, int nodeoffset, const char *name, int namelen, int *lenp)

    find a property based on substring

    :param const void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        offset of the node whose property to find

    :param const char \*name:
        name of the property to find

    :param int namelen:
        number of characters of name to consider

    :param int \*lenp:
        pointer to an integer variable (will be overwritten) or NULL

.. _`fdt_get_property_namelen.description`:

Description
-----------

Identical to \ :c:func:`fdt_get_property`\ , but only examine the first namelen
characters of name for matching the property name.

.. _`fdt_get_property`:

fdt_get_property
================

.. c:function:: const struct fdt_property *fdt_get_property(const void *fdt, int nodeoffset, const char *name, int *lenp)

    find a given property in a given node

    :param const void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        offset of the node whose property to find

    :param const char \*name:
        name of the property to find

    :param int \*lenp:
        pointer to an integer variable (will be overwritten) or NULL

.. _`fdt_get_property.description`:

Description
-----------

\ :c:func:`fdt_get_property`\  retrieves a pointer to the fdt_property
structure within the device tree blob corresponding to the property
named 'name' of the node at offset nodeoffset.  If lenp is
non-NULL, the length of the property value is also returned, in the
integer pointed to by lenp.

.. _`fdt_get_property.return`:

Return
------

pointer to the structure representing the property
if lenp is non-NULL, \*lenp contains the length of the property
value (>=0)
NULL, on error
if lenp is non-NULL, \*lenp contains an error code (<0):
-FDT_ERR_NOTFOUND, node does not have named property
-FDT_ERR_BADOFFSET, nodeoffset did not point to FDT_BEGIN_NODE
tag
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_TRUNCATED, standard meanings

.. _`fdt_getprop_by_offset`:

fdt_getprop_by_offset
=====================

.. c:function:: const void *fdt_getprop_by_offset(const void *fdt, int offset, const char **namep, int *lenp)

    retrieve the value of a property at a given offset

    :param const void \*fdt:
        pointer to the device tree blob

    :param int offset:
        *undescribed*

    :param const char \*\*namep:
        pointer to a string variable (will be overwritten) or NULL

    :param int \*lenp:
        pointer to an integer variable (will be overwritten) or NULL

.. _`fdt_getprop_by_offset.description`:

Description
-----------

\ :c:func:`fdt_getprop_by_offset`\  retrieves a pointer to the value of the
property at structure block offset 'offset' (this will be a pointer
to within the device blob itself, not a copy of the value).  If
lenp is non-NULL, the length of the property value is also
returned, in the integer pointed to by lenp.  If namep is non-NULL,
the property's namne will also be returned in the char \* pointed to
by namep (this will be a pointer to within the device tree's string
block, not a new copy of the name).

.. _`fdt_getprop_by_offset.return`:

Return
------

pointer to the property's value
if lenp is non-NULL, \*lenp contains the length of the property
value (>=0)
if namep is non-NULL \*namep contiains a pointer to the property
name.
NULL, on error
if lenp is non-NULL, \*lenp contains an error code (<0):
-FDT_ERR_BADOFFSET, nodeoffset did not point to FDT_PROP tag
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_TRUNCATED, standard meanings

.. _`fdt_getprop_namelen`:

fdt_getprop_namelen
===================

.. c:function:: const void *fdt_getprop_namelen(const void *fdt, int nodeoffset, const char *name, int namelen, int *lenp)

    get property value based on substring

    :param const void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        offset of the node whose property to find

    :param const char \*name:
        name of the property to find

    :param int namelen:
        number of characters of name to consider

    :param int \*lenp:
        pointer to an integer variable (will be overwritten) or NULL

.. _`fdt_getprop_namelen.description`:

Description
-----------

Identical to \ :c:func:`fdt_getprop`\ , but only examine the first namelen
characters of name for matching the property name.

.. _`fdt_getprop`:

fdt_getprop
===========

.. c:function:: const void *fdt_getprop(const void *fdt, int nodeoffset, const char *name, int *lenp)

    retrieve the value of a given property

    :param const void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        offset of the node whose property to find

    :param const char \*name:
        name of the property to find

    :param int \*lenp:
        pointer to an integer variable (will be overwritten) or NULL

.. _`fdt_getprop.description`:

Description
-----------

\ :c:func:`fdt_getprop`\  retrieves a pointer to the value of the property
named 'name' of the node at offset nodeoffset (this will be a
pointer to within the device blob itself, not a copy of the value).
If lenp is non-NULL, the length of the property value is also
returned, in the integer pointed to by lenp.

.. _`fdt_getprop.return`:

Return
------

pointer to the property's value
if lenp is non-NULL, \*lenp contains the length of the property
value (>=0)
NULL, on error
if lenp is non-NULL, \*lenp contains an error code (<0):
-FDT_ERR_NOTFOUND, node does not have named property
-FDT_ERR_BADOFFSET, nodeoffset did not point to FDT_BEGIN_NODE
tag
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_TRUNCATED, standard meanings

.. _`fdt_get_phandle`:

fdt_get_phandle
===============

.. c:function:: uint32_t fdt_get_phandle(const void *fdt, int nodeoffset)

    retrieve the phandle of a given node

    :param const void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        structure block offset of the node

.. _`fdt_get_phandle.description`:

Description
-----------

\ :c:func:`fdt_get_phandle`\  retrieves the phandle of the device tree node at
structure block offset nodeoffset.

.. _`fdt_get_phandle.return`:

Return
------

the phandle of the node at nodeoffset, on success (!= 0, != -1)
0, if the node has no phandle, or another error occurs

.. _`fdt_get_alias_namelen`:

fdt_get_alias_namelen
=====================

.. c:function:: const char *fdt_get_alias_namelen(const void *fdt, const char *name, int namelen)

    get alias based on substring

    :param const void \*fdt:
        pointer to the device tree blob

    :param const char \*name:
        name of the alias th look up

    :param int namelen:
        number of characters of name to consider

.. _`fdt_get_alias_namelen.description`:

Description
-----------

Identical to \ :c:func:`fdt_get_alias`\ , but only examine the first namelen
characters of name for matching the alias name.

.. _`fdt_get_alias`:

fdt_get_alias
=============

.. c:function:: const char *fdt_get_alias(const void *fdt, const char *name)

    retrieve the path referenced by a given alias

    :param const void \*fdt:
        pointer to the device tree blob

    :param const char \*name:
        name of the alias th look up

.. _`fdt_get_alias.description`:

Description
-----------

\ :c:func:`fdt_get_alias`\  retrieves the value of a given alias.  That is, the
value of the property named 'name' in the node /aliases.

.. _`fdt_get_alias.return`:

Return
------

a pointer to the expansion of the alias named 'name', if it exists
NULL, if the given alias or the /aliases node does not exist

.. _`fdt_get_path`:

fdt_get_path
============

.. c:function:: int fdt_get_path(const void *fdt, int nodeoffset, char *buf, int buflen)

    determine the full path of a node

    :param const void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        offset of the node whose path to find

    :param char \*buf:
        character buffer to contain the returned path (will be overwritten)

    :param int buflen:
        size of the character buffer at buf

.. _`fdt_get_path.description`:

Description
-----------

\ :c:func:`fdt_get_path`\  computes the full path of the node at offset
nodeoffset, and records that path in the buffer at buf.

.. _`fdt_get_path.note`:

NOTE
----

This function is expensive, as it must scan the device tree
structure from the start to nodeoffset.

.. _`fdt_get_path.return`:

Return
------

0, on success
buf contains the absolute path of the node at
nodeoffset, as a NUL-terminated string.
-FDT_ERR_BADOFFSET, nodeoffset does not refer to a BEGIN_NODE tag
-FDT_ERR_NOSPACE, the path of the given node is longer than (bufsize-1)
characters and will not fit in the given buffer.
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE, standard meanings

.. _`fdt_supernode_atdepth_offset`:

fdt_supernode_atdepth_offset
============================

.. c:function:: int fdt_supernode_atdepth_offset(const void *fdt, int nodeoffset, int supernodedepth, int *nodedepth)

    find a specific ancestor of a node

    :param const void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        offset of the node whose parent to find

    :param int supernodedepth:
        depth of the ancestor to find

    :param int \*nodedepth:
        pointer to an integer variable (will be overwritten) or NULL

.. _`fdt_supernode_atdepth_offset.description`:

Description
-----------

\ :c:func:`fdt_supernode_atdepth_offset`\  finds an ancestor of the given node
at a specific depth from the root (where the root itself has depth
0, its immediate subnodes depth 1 and so forth).  So
fdt_supernode_atdepth_offset(fdt, nodeoffset, 0, NULL);
will always return 0, the offset of the root node.  If the node at
nodeoffset has depth D, then:
fdt_supernode_atdepth_offset(fdt, nodeoffset, D, NULL);
will return nodeoffset itself.

.. _`fdt_supernode_atdepth_offset.note`:

NOTE
----

This function is expensive, as it must scan the device tree
structure from the start to nodeoffset.

.. _`fdt_supernode_atdepth_offset.return`:

Return
------

structure block offset of the node at node offset's ancestor
of depth supernodedepth (>=0), on success
-FDT_ERR_BADOFFSET, nodeoffset does not refer to a BEGIN_NODE tag
-FDT_ERR_NOTFOUND, supernodedepth was greater than the depth of
nodeoffset
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE, standard meanings

.. _`fdt_node_depth`:

fdt_node_depth
==============

.. c:function:: int fdt_node_depth(const void *fdt, int nodeoffset)

    find the depth of a given node

    :param const void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        offset of the node whose parent to find

.. _`fdt_node_depth.description`:

Description
-----------

\ :c:func:`fdt_node_depth`\  finds the depth of a given node.  The root node
has depth 0, its immediate subnodes depth 1 and so forth.

.. _`fdt_node_depth.note`:

NOTE
----

This function is expensive, as it must scan the device tree
structure from the start to nodeoffset.

.. _`fdt_node_depth.return`:

Return
------

depth of the node at nodeoffset (>=0), on success
-FDT_ERR_BADOFFSET, nodeoffset does not refer to a BEGIN_NODE tag
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE, standard meanings

.. _`fdt_parent_offset`:

fdt_parent_offset
=================

.. c:function:: int fdt_parent_offset(const void *fdt, int nodeoffset)

    find the parent of a given node

    :param const void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        offset of the node whose parent to find

.. _`fdt_parent_offset.description`:

Description
-----------

\ :c:func:`fdt_parent_offset`\  locates the parent node of a given node (that
is, it finds the offset of the node which contains the node at
nodeoffset as a subnode).

.. _`fdt_parent_offset.note`:

NOTE
----

This function is expensive, as it must scan the device tree
structure from the start to nodeoffset, \*twice\*.

.. _`fdt_parent_offset.return`:

Return
------

structure block offset of the parent of the node at nodeoffset
(>=0), on success
-FDT_ERR_BADOFFSET, nodeoffset does not refer to a BEGIN_NODE tag
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE, standard meanings

.. _`fdt_node_offset_by_prop_value`:

fdt_node_offset_by_prop_value
=============================

.. c:function:: int fdt_node_offset_by_prop_value(const void *fdt, int startoffset, const char *propname, const void *propval, int proplen)

    find nodes with a given property value

    :param const void \*fdt:
        pointer to the device tree blob

    :param int startoffset:
        only find nodes after this offset

    :param const char \*propname:
        property name to check

    :param const void \*propval:
        property value to search for

    :param int proplen:
        length of the value in propval

.. _`fdt_node_offset_by_prop_value.description`:

Description
-----------

\ :c:func:`fdt_node_offset_by_prop_value`\  returns the offset of the first
node after startoffset, which has a property named propname whose
value is of length proplen and has value equal to propval; or if
startoffset is -1, the very first such node in the tree.

To iterate through all nodes matching the criterion, the following

.. _`fdt_node_offset_by_prop_value.idiom-can-be-used`:

idiom can be used
-----------------

offset = fdt_node_offset_by_prop_value(fdt, -1, propname,
propval, proplen);
while (offset != -FDT_ERR_NOTFOUND) {
// other code here
offset = fdt_node_offset_by_prop_value(fdt, offset, propname,
propval, proplen);
}

Note the -1 in the first call to the function, if 0 is used here
instead, the function will never locate the root node, even if it
matches the criterion.

.. _`fdt_node_offset_by_prop_value.return`:

Return
------

structure block offset of the located node (>= 0, >startoffset),
on success
-FDT_ERR_NOTFOUND, no node matching the criterion exists in the
tree after startoffset
-FDT_ERR_BADOFFSET, nodeoffset does not refer to a BEGIN_NODE tag
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE, standard meanings

.. _`fdt_node_offset_by_phandle`:

fdt_node_offset_by_phandle
==========================

.. c:function:: int fdt_node_offset_by_phandle(const void *fdt, uint32_t phandle)

    find the node with a given phandle

    :param const void \*fdt:
        pointer to the device tree blob

    :param uint32_t phandle:
        phandle value

.. _`fdt_node_offset_by_phandle.description`:

Description
-----------

\ :c:func:`fdt_node_offset_by_phandle`\  returns the offset of the node
which has the given phandle value.  If there is more than one node
in the tree with the given phandle (an invalid tree), results are
undefined.

.. _`fdt_node_offset_by_phandle.return`:

Return
------

structure block offset of the located node (>= 0), on success
-FDT_ERR_NOTFOUND, no node with that phandle exists
-FDT_ERR_BADPHANDLE, given phandle value was invalid (0 or -1)
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE, standard meanings

.. _`fdt_node_check_compatible`:

fdt_node_check_compatible
=========================

.. c:function:: int fdt_node_check_compatible(const void *fdt, int nodeoffset, const char *compatible)

    check a node's compatible property

    :param const void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        offset of a tree node

    :param const char \*compatible:
        string to match against

.. _`fdt_node_check_compatible.description`:

Description
-----------


\ :c:func:`fdt_node_check_compatible`\  returns 0 if the given node contains a
'compatible' property with the given string as one of its elements,
it returns non-zero otherwise, or on error.

.. _`fdt_node_check_compatible.return`:

Return
------

0, if the node has a 'compatible' property listing the given string
1, if the node has a 'compatible' property, but it does not list
the given string
-FDT_ERR_NOTFOUND, if the given node has no 'compatible' property
-FDT_ERR_BADOFFSET, if nodeoffset does not refer to a BEGIN_NODE tag
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE, standard meanings

.. _`fdt_node_offset_by_compatible`:

fdt_node_offset_by_compatible
=============================

.. c:function:: int fdt_node_offset_by_compatible(const void *fdt, int startoffset, const char *compatible)

    find nodes with a given 'compatible' value

    :param const void \*fdt:
        pointer to the device tree blob

    :param int startoffset:
        only find nodes after this offset

    :param const char \*compatible:
        'compatible' string to match against

.. _`fdt_node_offset_by_compatible.description`:

Description
-----------

\ :c:func:`fdt_node_offset_by_compatible`\  returns the offset of the first
node after startoffset, which has a 'compatible' property which
lists the given compatible string; or if startoffset is -1, the
very first such node in the tree.

To iterate through all nodes matching the criterion, the following

.. _`fdt_node_offset_by_compatible.idiom-can-be-used`:

idiom can be used
-----------------

offset = fdt_node_offset_by_compatible(fdt, -1, compatible);
while (offset != -FDT_ERR_NOTFOUND) {
// other code here
offset = fdt_node_offset_by_compatible(fdt, offset, compatible);
}

Note the -1 in the first call to the function, if 0 is used here
instead, the function will never locate the root node, even if it
matches the criterion.

.. _`fdt_node_offset_by_compatible.return`:

Return
------

structure block offset of the located node (>= 0, >startoffset),
on success
-FDT_ERR_NOTFOUND, no node matching the criterion exists in the
tree after startoffset
-FDT_ERR_BADOFFSET, nodeoffset does not refer to a BEGIN_NODE tag
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE, standard meanings

.. _`fdt_stringlist_contains`:

fdt_stringlist_contains
=======================

.. c:function:: int fdt_stringlist_contains(const char *strlist, int listlen, const char *str)

    check a string list property for a string

    :param const char \*strlist:
        Property containing a list of strings to check

    :param int listlen:
        Length of property

    :param const char \*str:
        String to search for

.. _`fdt_stringlist_contains.description`:

Description
-----------

This is a utility function provided for convenience. The list contains
one or more strings, each terminated by \0, as is found in a device tree
"compatible" property.

.. _`fdt_stringlist_count`:

fdt_stringlist_count
====================

.. c:function:: int fdt_stringlist_count(const void *fdt, int nodeoffset, const char *property)

    count the number of strings in a string list

    :param const void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        offset of a tree node

    :param const char \*property:
        name of the property containing the string list

.. _`fdt_stringlist_search`:

fdt_stringlist_search
=====================

.. c:function:: int fdt_stringlist_search(const void *fdt, int nodeoffset, const char *property, const char *string)

    find a string in a string list and return its index

    :param const void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        offset of a tree node

    :param const char \*property:
        name of the property containing the string list

    :param const char \*string:
        string to look up in the string list

.. _`fdt_stringlist_search.description`:

Description
-----------

Note that it is possible for this function to succeed on property values
that are not NUL-terminated. That's because the function will stop after
finding the first occurrence of \ ``string``\ . This can for example happen with
small-valued cell properties, such as #address-cells, when searching for
the empty string.

.. _`fdt_stringlist_get`:

fdt_stringlist_get
==================

.. c:function:: const char *fdt_stringlist_get(const void *fdt, int nodeoffset, const char *property, int index, int *lenp)

    obtain the string at a given index in a string list

    :param const void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        offset of a tree node

    :param const char \*property:
        name of the property containing the string list

    :param int index:
        index of the string to return

    :param int \*lenp:
        return location for the string length or an error code on failure

.. _`fdt_stringlist_get.description`:

Description
-----------

Note that this will successfully extract strings from properties with
non-NUL-terminated values. For example on small-valued cell properties
this function will return the empty string.

If non-NULL, the length of the string (on success) or a negative error-code
(on failure) will be stored in the integer pointer to by lenp.

.. _`fdt_max_ncells`:

FDT_MAX_NCELLS
==============

.. c:function::  FDT_MAX_NCELLS()

    maximum value for #address-cells and #size-cells

.. _`fdt_max_ncells.description`:

Description
-----------

This is the maximum value for #address-cells, #size-cells and
similar properties that will be processed by libfdt.  IEE1275
requires that OF implementations handle values up to 4.
Implementations may support larger values, but in practice higher
values aren't used.

.. _`fdt_address_cells`:

fdt_address_cells
=================

.. c:function:: int fdt_address_cells(const void *fdt, int nodeoffset)

    retrieve address size for a bus represented in the tree

    :param const void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        offset of the node to find the address size for

.. _`fdt_address_cells.description`:

Description
-----------

When the node has a valid #address-cells property, returns its value.

.. _`fdt_address_cells.return`:

Return
------

0 <= n < FDT_MAX_NCELLS, on success
2, if the node has no #address-cells property
-FDT_ERR_BADNCELLS, if the node has a badly formatted or invalid
#address-cells property
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_TRUNCATED, standard meanings

.. _`fdt_size_cells`:

fdt_size_cells
==============

.. c:function:: int fdt_size_cells(const void *fdt, int nodeoffset)

    retrieve address range size for a bus represented in the tree

    :param const void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        offset of the node to find the address range size for

.. _`fdt_size_cells.description`:

Description
-----------

When the node has a valid #size-cells property, returns its value.

.. _`fdt_size_cells.return`:

Return
------

0 <= n < FDT_MAX_NCELLS, on success
2, if the node has no #address-cells property
-FDT_ERR_BADNCELLS, if the node has a badly formatted or invalid
#size-cells property
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_TRUNCATED, standard meanings

.. _`fdt_setprop_inplace_namelen_partial`:

fdt_setprop_inplace_namelen_partial
===================================

.. c:function:: int fdt_setprop_inplace_namelen_partial(void *fdt, int nodeoffset, const char *name, int namelen, uint32_t idx, const void *val, int len)

    change a property's value, but not its size

    :param void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        offset of the node whose property to change

    :param const char \*name:
        name of the property to change

    :param int namelen:
        number of characters of name to consider

    :param uint32_t idx:
        index of the property to change in the array

    :param const void \*val:
        pointer to data to replace the property value with

    :param int len:
        length of the property value

.. _`fdt_setprop_inplace_namelen_partial.description`:

Description
-----------

Identical to \ :c:func:`fdt_setprop_inplace`\ , but modifies the given property
starting from the given index, and using only the first characters
of the name. It is useful when you want to manipulate only one value of
an array and you have a string that doesn't end with \0.

.. _`fdt_setprop_inplace`:

fdt_setprop_inplace
===================

.. c:function:: int fdt_setprop_inplace(void *fdt, int nodeoffset, const char *name, const void *val, int len)

    change a property's value, but not its size

    :param void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        offset of the node whose property to change

    :param const char \*name:
        name of the property to change

    :param const void \*val:
        pointer to data to replace the property value with

    :param int len:
        length of the property value

.. _`fdt_setprop_inplace.description`:

Description
-----------

\ :c:func:`fdt_setprop_inplace`\  replaces the value of a given property with
the data in val, of length len.  This function cannot change the
size of a property, and so will only work if len is equal to the
current length of the property.

This function will alter only the bytes in the blob which contain
the given property value, and will not alter or move any other part
of the tree.

.. _`fdt_setprop_inplace.return`:

Return
------

0, on success
-FDT_ERR_NOSPACE, if len is not equal to the property's current length
-FDT_ERR_NOTFOUND, node does not have the named property
-FDT_ERR_BADOFFSET, nodeoffset did not point to FDT_BEGIN_NODE tag
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_TRUNCATED, standard meanings

.. _`fdt_setprop_inplace_u32`:

fdt_setprop_inplace_u32
=======================

.. c:function:: int fdt_setprop_inplace_u32(void *fdt, int nodeoffset, const char *name, uint32_t val)

    change the value of a 32-bit integer property

    :param void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        offset of the node whose property to change

    :param const char \*name:
        name of the property to change

    :param uint32_t val:
        32-bit integer value to replace the property with

.. _`fdt_setprop_inplace_u32.description`:

Description
-----------

\ :c:func:`fdt_setprop_inplace_u32`\  replaces the value of a given property
with the 32-bit integer value in val, converting val to big-endian
if necessary.  This function cannot change the size of a property,
and so will only work if the property already exists and has length
4.

This function will alter only the bytes in the blob which contain
the given property value, and will not alter or move any other part
of the tree.

.. _`fdt_setprop_inplace_u32.return`:

Return
------

0, on success
-FDT_ERR_NOSPACE, if the property's length is not equal to 4
-FDT_ERR_NOTFOUND, node does not have the named property
-FDT_ERR_BADOFFSET, nodeoffset did not point to FDT_BEGIN_NODE tag
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_TRUNCATED, standard meanings

.. _`fdt_setprop_inplace_u64`:

fdt_setprop_inplace_u64
=======================

.. c:function:: int fdt_setprop_inplace_u64(void *fdt, int nodeoffset, const char *name, uint64_t val)

    change the value of a 64-bit integer property

    :param void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        offset of the node whose property to change

    :param const char \*name:
        name of the property to change

    :param uint64_t val:
        64-bit integer value to replace the property with

.. _`fdt_setprop_inplace_u64.description`:

Description
-----------

\ :c:func:`fdt_setprop_inplace_u64`\  replaces the value of a given property
with the 64-bit integer value in val, converting val to big-endian
if necessary.  This function cannot change the size of a property,
and so will only work if the property already exists and has length
8.

This function will alter only the bytes in the blob which contain
the given property value, and will not alter or move any other part
of the tree.

.. _`fdt_setprop_inplace_u64.return`:

Return
------

0, on success
-FDT_ERR_NOSPACE, if the property's length is not equal to 8
-FDT_ERR_NOTFOUND, node does not have the named property
-FDT_ERR_BADOFFSET, nodeoffset did not point to FDT_BEGIN_NODE tag
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_TRUNCATED, standard meanings

.. _`fdt_setprop_inplace_cell`:

fdt_setprop_inplace_cell
========================

.. c:function:: int fdt_setprop_inplace_cell(void *fdt, int nodeoffset, const char *name, uint32_t val)

    change the value of a single-cell property

    :param void \*fdt:
        *undescribed*

    :param int nodeoffset:
        *undescribed*

    :param const char \*name:
        *undescribed*

    :param uint32_t val:
        *undescribed*

.. _`fdt_setprop_inplace_cell.description`:

Description
-----------

This is an alternative name for \ :c:func:`fdt_setprop_inplace_u32`\ 

.. _`fdt_nop_property`:

fdt_nop_property
================

.. c:function:: int fdt_nop_property(void *fdt, int nodeoffset, const char *name)

    replace a property with nop tags

    :param void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        offset of the node whose property to nop

    :param const char \*name:
        name of the property to nop

.. _`fdt_nop_property.description`:

Description
-----------

\ :c:func:`fdt_nop_property`\  will replace a given property's representation
in the blob with FDT_NOP tags, effectively removing it from the
tree.

This function will alter only the bytes in the blob which contain
the property, and will not alter or move any other part of the
tree.

.. _`fdt_nop_property.return`:

Return
------

0, on success
-FDT_ERR_NOTFOUND, node does not have the named property
-FDT_ERR_BADOFFSET, nodeoffset did not point to FDT_BEGIN_NODE tag
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_TRUNCATED, standard meanings

.. _`fdt_nop_node`:

fdt_nop_node
============

.. c:function:: int fdt_nop_node(void *fdt, int nodeoffset)

    replace a node (subtree) with nop tags

    :param void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        offset of the node to nop

.. _`fdt_nop_node.description`:

Description
-----------

\ :c:func:`fdt_nop_node`\  will replace a given node's representation in the
blob, including all its subnodes, if any, with FDT_NOP tags,
effectively removing it from the tree.

This function will alter only the bytes in the blob which contain
the node and its properties and subnodes, and will not alter or
move any other part of the tree.

.. _`fdt_nop_node.return`:

Return
------

0, on success
-FDT_ERR_BADOFFSET, nodeoffset did not point to FDT_BEGIN_NODE tag
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_TRUNCATED, standard meanings

.. _`fdt_property_placeholder`:

fdt_property_placeholder
========================

.. c:function:: int fdt_property_placeholder(void *fdt, const char *name, int len, void **valp)

    add a new property and return a ptr to its value

    :param void \*fdt:
        pointer to the device tree blob

    :param const char \*name:
        name of property to add

    :param int len:
        length of property value in bytes

    :param void \*\*valp:
        returns a pointer to where where the value should be placed

.. _`fdt_property_placeholder.return`:

Return
------

0, on success
-FDT_ERR_BADMAGIC,
-FDT_ERR_NOSPACE, standard meanings

.. _`fdt_add_mem_rsv`:

fdt_add_mem_rsv
===============

.. c:function:: int fdt_add_mem_rsv(void *fdt, uint64_t address, uint64_t size)

    add one memory reserve map entry

    :param void \*fdt:
        pointer to the device tree blob

    :param uint64_t address:
        64-bit values (native endian)

    :param uint64_t size:
        *undescribed*

.. _`fdt_add_mem_rsv.description`:

Description
-----------

Adds a reserve map entry to the given blob reserving a region at
address address of length size.

This function will insert data into the reserve map and will
therefore change the indexes of some entries in the table.

.. _`fdt_add_mem_rsv.return`:

Return
------

0, on success
-FDT_ERR_NOSPACE, there is insufficient free space in the blob to
contain the new reservation entry
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_BADLAYOUT,
-FDT_ERR_TRUNCATED, standard meanings

.. _`fdt_del_mem_rsv`:

fdt_del_mem_rsv
===============

.. c:function:: int fdt_del_mem_rsv(void *fdt, int n)

    remove a memory reserve map entry

    :param void \*fdt:
        pointer to the device tree blob

    :param int n:
        entry to remove

.. _`fdt_del_mem_rsv.description`:

Description
-----------

\ :c:func:`fdt_del_mem_rsv`\  removes the n-th memory reserve map entry from
the blob.

This function will delete data from the reservation table and will
therefore change the indexes of some entries in the table.

.. _`fdt_del_mem_rsv.return`:

Return
------

0, on success
-FDT_ERR_NOTFOUND, there is no entry of the given index (i.e. there
are less than n+1 reserve map entries)
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_BADLAYOUT,
-FDT_ERR_TRUNCATED, standard meanings

.. _`fdt_set_name`:

fdt_set_name
============

.. c:function:: int fdt_set_name(void *fdt, int nodeoffset, const char *name)

    change the name of a given node

    :param void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        structure block offset of a node

    :param const char \*name:
        name to give the node

.. _`fdt_set_name.description`:

Description
-----------

\ :c:func:`fdt_set_name`\  replaces the name (including unit address, if any)
of the given node with the given string.  NOTE: this function can't
efficiently check if the new name is unique amongst the given
node's siblings; results are undefined if this function is invoked
with a name equal to one of the given node's siblings.

This function may insert or delete data from the blob, and will
therefore change the offsets of some existing nodes.

.. _`fdt_set_name.return`:

Return
------

0, on success
-FDT_ERR_NOSPACE, there is insufficient free space in the blob
to contain the new name
-FDT_ERR_BADOFFSET, nodeoffset did not point to FDT_BEGIN_NODE tag
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE, standard meanings

.. _`fdt_setprop`:

fdt_setprop
===========

.. c:function:: int fdt_setprop(void *fdt, int nodeoffset, const char *name, const void *val, int len)

    create or change a property

    :param void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        offset of the node whose property to change

    :param const char \*name:
        name of the property to change

    :param const void \*val:
        pointer to data to set the property value to

    :param int len:
        length of the property value

.. _`fdt_setprop.description`:

Description
-----------

\ :c:func:`fdt_setprop`\  sets the value of the named property in the given
node to the given value and length, creating the property if it
does not already exist.

This function may insert or delete data from the blob, and will
therefore change the offsets of some existing nodes.

.. _`fdt_setprop.return`:

Return
------

0, on success
-FDT_ERR_NOSPACE, there is insufficient free space in the blob to
contain the new property value
-FDT_ERR_BADOFFSET, nodeoffset did not point to FDT_BEGIN_NODE tag
-FDT_ERR_BADLAYOUT,
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_BADLAYOUT,
-FDT_ERR_TRUNCATED, standard meanings

.. _`fdt_setprop_placeholder`:

fdt_setprop_placeholder
=======================

.. c:function:: int fdt_setprop_placeholder(void *fdt, int nodeoffset, const char *name, int len, void **prop_data)

    allocate space for a property

    :param void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        offset of the node whose property to change

    :param const char \*name:
        name of the property to change

    :param int len:
        length of the property value

    :param void \*\*prop_data:
        return pointer to property data

.. _`fdt_setprop_placeholder.description`:

Description
-----------

\ :c:func:`fdt_setprop_placeholer`\  allocates the named property in the given node.
If the property exists it is resized. In either case a pointer to the
property data is returned.

This function may insert or delete data from the blob, and will
therefore change the offsets of some existing nodes.

.. _`fdt_setprop_placeholder.return`:

Return
------

0, on success
-FDT_ERR_NOSPACE, there is insufficient free space in the blob to
contain the new property value
-FDT_ERR_BADOFFSET, nodeoffset did not point to FDT_BEGIN_NODE tag
-FDT_ERR_BADLAYOUT,
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_BADLAYOUT,
-FDT_ERR_TRUNCATED, standard meanings

.. _`fdt_setprop_u32`:

fdt_setprop_u32
===============

.. c:function:: int fdt_setprop_u32(void *fdt, int nodeoffset, const char *name, uint32_t val)

    set a property to a 32-bit integer

    :param void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        offset of the node whose property to change

    :param const char \*name:
        name of the property to change

    :param uint32_t val:
        32-bit integer value for the property (native endian)

.. _`fdt_setprop_u32.description`:

Description
-----------

\ :c:func:`fdt_setprop_u32`\  sets the value of the named property in the given
node to the given 32-bit integer value (converting to big-endian if
necessary), or creates a new property with that value if it does
not already exist.

This function may insert or delete data from the blob, and will
therefore change the offsets of some existing nodes.

.. _`fdt_setprop_u32.return`:

Return
------

0, on success
-FDT_ERR_NOSPACE, there is insufficient free space in the blob to
contain the new property value
-FDT_ERR_BADOFFSET, nodeoffset did not point to FDT_BEGIN_NODE tag
-FDT_ERR_BADLAYOUT,
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_BADLAYOUT,
-FDT_ERR_TRUNCATED, standard meanings

.. _`fdt_setprop_u64`:

fdt_setprop_u64
===============

.. c:function:: int fdt_setprop_u64(void *fdt, int nodeoffset, const char *name, uint64_t val)

    set a property to a 64-bit integer

    :param void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        offset of the node whose property to change

    :param const char \*name:
        name of the property to change

    :param uint64_t val:
        64-bit integer value for the property (native endian)

.. _`fdt_setprop_u64.description`:

Description
-----------

\ :c:func:`fdt_setprop_u64`\  sets the value of the named property in the given
node to the given 64-bit integer value (converting to big-endian if
necessary), or creates a new property with that value if it does
not already exist.

This function may insert or delete data from the blob, and will
therefore change the offsets of some existing nodes.

.. _`fdt_setprop_u64.return`:

Return
------

0, on success
-FDT_ERR_NOSPACE, there is insufficient free space in the blob to
contain the new property value
-FDT_ERR_BADOFFSET, nodeoffset did not point to FDT_BEGIN_NODE tag
-FDT_ERR_BADLAYOUT,
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_BADLAYOUT,
-FDT_ERR_TRUNCATED, standard meanings

.. _`fdt_setprop_cell`:

fdt_setprop_cell
================

.. c:function:: int fdt_setprop_cell(void *fdt, int nodeoffset, const char *name, uint32_t val)

    set a property to a single cell value

    :param void \*fdt:
        *undescribed*

    :param int nodeoffset:
        *undescribed*

    :param const char \*name:
        *undescribed*

    :param uint32_t val:
        *undescribed*

.. _`fdt_setprop_cell.description`:

Description
-----------

This is an alternative name for \ :c:func:`fdt_setprop_u32`\ 

.. _`fdt_setprop_string`:

fdt_setprop_string
==================

.. c:function::  fdt_setprop_string( fdt,  nodeoffset,  name,  str)

    set a property to a string value

    :param  fdt:
        pointer to the device tree blob

    :param  nodeoffset:
        offset of the node whose property to change

    :param  name:
        name of the property to change

    :param  str:
        string value for the property

.. _`fdt_setprop_string.description`:

Description
-----------

\ :c:func:`fdt_setprop_string`\  sets the value of the named property in the
given node to the given string value (using the length of the
string to determine the new length of the property), or creates a
new property with that value if it does not already exist.

This function may insert or delete data from the blob, and will
therefore change the offsets of some existing nodes.

.. _`fdt_setprop_string.return`:

Return
------

0, on success
-FDT_ERR_NOSPACE, there is insufficient free space in the blob to
contain the new property value
-FDT_ERR_BADOFFSET, nodeoffset did not point to FDT_BEGIN_NODE tag
-FDT_ERR_BADLAYOUT,
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_BADLAYOUT,
-FDT_ERR_TRUNCATED, standard meanings

.. _`fdt_setprop_empty`:

fdt_setprop_empty
=================

.. c:function::  fdt_setprop_empty( fdt,  nodeoffset,  name)

    set a property to an empty value

    :param  fdt:
        pointer to the device tree blob

    :param  nodeoffset:
        offset of the node whose property to change

    :param  name:
        name of the property to change

.. _`fdt_setprop_empty.description`:

Description
-----------

\ :c:func:`fdt_setprop_empty`\  sets the value of the named property in the
given node to an empty (zero length) value, or creates a new empty
property if it does not already exist.

This function may insert or delete data from the blob, and will
therefore change the offsets of some existing nodes.

.. _`fdt_setprop_empty.return`:

Return
------

0, on success
-FDT_ERR_NOSPACE, there is insufficient free space in the blob to
contain the new property value
-FDT_ERR_BADOFFSET, nodeoffset did not point to FDT_BEGIN_NODE tag
-FDT_ERR_BADLAYOUT,
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_BADLAYOUT,
-FDT_ERR_TRUNCATED, standard meanings

.. _`fdt_appendprop`:

fdt_appendprop
==============

.. c:function:: int fdt_appendprop(void *fdt, int nodeoffset, const char *name, const void *val, int len)

    append to or create a property

    :param void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        offset of the node whose property to change

    :param const char \*name:
        name of the property to append to

    :param const void \*val:
        pointer to data to append to the property value

    :param int len:
        length of the data to append to the property value

.. _`fdt_appendprop.description`:

Description
-----------

\ :c:func:`fdt_appendprop`\  appends the value to the named property in the
given node, creating the property if it does not already exist.

This function may insert data into the blob, and will therefore
change the offsets of some existing nodes.

.. _`fdt_appendprop.return`:

Return
------

0, on success
-FDT_ERR_NOSPACE, there is insufficient free space in the blob to
contain the new property value
-FDT_ERR_BADOFFSET, nodeoffset did not point to FDT_BEGIN_NODE tag
-FDT_ERR_BADLAYOUT,
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_BADLAYOUT,
-FDT_ERR_TRUNCATED, standard meanings

.. _`fdt_appendprop_u32`:

fdt_appendprop_u32
==================

.. c:function:: int fdt_appendprop_u32(void *fdt, int nodeoffset, const char *name, uint32_t val)

    append a 32-bit integer value to a property

    :param void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        offset of the node whose property to change

    :param const char \*name:
        name of the property to change

    :param uint32_t val:
        32-bit integer value to append to the property (native endian)

.. _`fdt_appendprop_u32.description`:

Description
-----------

\ :c:func:`fdt_appendprop_u32`\  appends the given 32-bit integer value
(converting to big-endian if necessary) to the value of the named
property in the given node, or creates a new property with that
value if it does not already exist.

This function may insert data into the blob, and will therefore
change the offsets of some existing nodes.

.. _`fdt_appendprop_u32.return`:

Return
------

0, on success
-FDT_ERR_NOSPACE, there is insufficient free space in the blob to
contain the new property value
-FDT_ERR_BADOFFSET, nodeoffset did not point to FDT_BEGIN_NODE tag
-FDT_ERR_BADLAYOUT,
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_BADLAYOUT,
-FDT_ERR_TRUNCATED, standard meanings

.. _`fdt_appendprop_u64`:

fdt_appendprop_u64
==================

.. c:function:: int fdt_appendprop_u64(void *fdt, int nodeoffset, const char *name, uint64_t val)

    append a 64-bit integer value to a property

    :param void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        offset of the node whose property to change

    :param const char \*name:
        name of the property to change

    :param uint64_t val:
        64-bit integer value to append to the property (native endian)

.. _`fdt_appendprop_u64.description`:

Description
-----------

\ :c:func:`fdt_appendprop_u64`\  appends the given 64-bit integer value
(converting to big-endian if necessary) to the value of the named
property in the given node, or creates a new property with that
value if it does not already exist.

This function may insert data into the blob, and will therefore
change the offsets of some existing nodes.

.. _`fdt_appendprop_u64.return`:

Return
------

0, on success
-FDT_ERR_NOSPACE, there is insufficient free space in the blob to
contain the new property value
-FDT_ERR_BADOFFSET, nodeoffset did not point to FDT_BEGIN_NODE tag
-FDT_ERR_BADLAYOUT,
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_BADLAYOUT,
-FDT_ERR_TRUNCATED, standard meanings

.. _`fdt_appendprop_cell`:

fdt_appendprop_cell
===================

.. c:function:: int fdt_appendprop_cell(void *fdt, int nodeoffset, const char *name, uint32_t val)

    append a single cell value to a property

    :param void \*fdt:
        *undescribed*

    :param int nodeoffset:
        *undescribed*

    :param const char \*name:
        *undescribed*

    :param uint32_t val:
        *undescribed*

.. _`fdt_appendprop_cell.description`:

Description
-----------

This is an alternative name for \ :c:func:`fdt_appendprop_u32`\ 

.. _`fdt_appendprop_string`:

fdt_appendprop_string
=====================

.. c:function::  fdt_appendprop_string( fdt,  nodeoffset,  name,  str)

    append a string to a property

    :param  fdt:
        pointer to the device tree blob

    :param  nodeoffset:
        offset of the node whose property to change

    :param  name:
        name of the property to change

    :param  str:
        string value to append to the property

.. _`fdt_appendprop_string.description`:

Description
-----------

\ :c:func:`fdt_appendprop_string`\  appends the given string to the value of
the named property in the given node, or creates a new property
with that value if it does not already exist.

This function may insert data into the blob, and will therefore
change the offsets of some existing nodes.

.. _`fdt_appendprop_string.return`:

Return
------

0, on success
-FDT_ERR_NOSPACE, there is insufficient free space in the blob to
contain the new property value
-FDT_ERR_BADOFFSET, nodeoffset did not point to FDT_BEGIN_NODE tag
-FDT_ERR_BADLAYOUT,
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_BADLAYOUT,
-FDT_ERR_TRUNCATED, standard meanings

.. _`fdt_delprop`:

fdt_delprop
===========

.. c:function:: int fdt_delprop(void *fdt, int nodeoffset, const char *name)

    delete a property

    :param void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        offset of the node whose property to nop

    :param const char \*name:
        name of the property to nop

.. _`fdt_delprop.description`:

Description
-----------

\ :c:func:`fdt_del_property`\  will delete the given property.

This function will delete data from the blob, and will therefore
change the offsets of some existing nodes.

.. _`fdt_delprop.return`:

Return
------

0, on success
-FDT_ERR_NOTFOUND, node does not have the named property
-FDT_ERR_BADOFFSET, nodeoffset did not point to FDT_BEGIN_NODE tag
-FDT_ERR_BADLAYOUT,
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_TRUNCATED, standard meanings

.. _`fdt_add_subnode_namelen`:

fdt_add_subnode_namelen
=======================

.. c:function:: int fdt_add_subnode_namelen(void *fdt, int parentoffset, const char *name, int namelen)

    creates a new node based on substring

    :param void \*fdt:
        pointer to the device tree blob

    :param int parentoffset:
        structure block offset of a node

    :param const char \*name:
        name of the subnode to locate

    :param int namelen:
        number of characters of name to consider

.. _`fdt_add_subnode_namelen.description`:

Description
-----------

Identical to \ :c:func:`fdt_add_subnode`\ , but use only the first namelen
characters of name as the name of the new node.  This is useful for
creating subnodes based on a portion of a larger string, such as a
full path.

.. _`fdt_add_subnode`:

fdt_add_subnode
===============

.. c:function:: int fdt_add_subnode(void *fdt, int parentoffset, const char *name)

    creates a new node

    :param void \*fdt:
        pointer to the device tree blob

    :param int parentoffset:
        structure block offset of a node

    :param const char \*name:
        name of the subnode to locate

.. _`fdt_add_subnode.description`:

Description
-----------

\ :c:func:`fdt_add_subnode`\  creates a new node as a subnode of the node at
structure block offset parentoffset, with the given name (which
should include the unit address, if any).

This function will insert data into the blob, and will therefore
change the offsets of some existing nodes.

.. _`fdt_add_subnode.return`:

Return
------

structure block offset of the created nodeequested subnode (>=0), on
success
-FDT_ERR_NOTFOUND, if the requested subnode does not exist
-FDT_ERR_BADOFFSET, if parentoffset did not point to an FDT_BEGIN_NODE
tag
-FDT_ERR_EXISTS, if the node at parentoffset already has a subnode of
the given name
-FDT_ERR_NOSPACE, if there is insufficient free space in the
blob to contain the new node
-FDT_ERR_NOSPACE
-FDT_ERR_BADLAYOUT
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_TRUNCATED, standard meanings.

.. _`fdt_del_node`:

fdt_del_node
============

.. c:function:: int fdt_del_node(void *fdt, int nodeoffset)

    delete a node (subtree)

    :param void \*fdt:
        pointer to the device tree blob

    :param int nodeoffset:
        offset of the node to nop

.. _`fdt_del_node.description`:

Description
-----------

\ :c:func:`fdt_del_node`\  will remove the given node, including all its
subnodes if any, from the blob.

This function will delete data from the blob, and will therefore
change the offsets of some existing nodes.

.. _`fdt_del_node.return`:

Return
------

0, on success
-FDT_ERR_BADOFFSET, nodeoffset did not point to FDT_BEGIN_NODE tag
-FDT_ERR_BADLAYOUT,
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTATE,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_TRUNCATED, standard meanings

.. _`fdt_overlay_apply`:

fdt_overlay_apply
=================

.. c:function:: int fdt_overlay_apply(void *fdt, void *fdto)

    Applies a DT overlay on a base DT

    :param void \*fdt:
        pointer to the base device tree blob

    :param void \*fdto:
        pointer to the device tree overlay blob

.. _`fdt_overlay_apply.description`:

Description
-----------

\ :c:func:`fdt_overlay_apply`\  will apply the given device tree overlay on the
given base device tree.

Expect the base device tree to be modified, even if the function
returns an error.

.. _`fdt_overlay_apply.return`:

Return
------

0, on success
-FDT_ERR_NOSPACE, there's not enough space in the base device tree
-FDT_ERR_NOTFOUND, the overlay points to some inexistant nodes or
properties in the base DT
-FDT_ERR_BADPHANDLE,
-FDT_ERR_BADOVERLAY,
-FDT_ERR_NOPHANDLES,
-FDT_ERR_INTERNAL,
-FDT_ERR_BADLAYOUT,
-FDT_ERR_BADMAGIC,
-FDT_ERR_BADOFFSET,
-FDT_ERR_BADPATH,
-FDT_ERR_BADVERSION,
-FDT_ERR_BADSTRUCTURE,
-FDT_ERR_BADSTATE,
-FDT_ERR_TRUNCATED, standard meanings

.. This file was automatic generated / don't edit.


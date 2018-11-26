.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thunderbolt/property.c

.. _`tb_property_parse_dir`:

tb_property_parse_dir
=====================

.. c:function:: struct tb_property_dir *tb_property_parse_dir(const u32 *block, size_t block_len)

    Parses properties from given property block

    :param block:
        Property block to parse
    :type block: const u32 \*

    :param block_len:
        Number of dword elements in the property block
    :type block_len: size_t

.. _`tb_property_parse_dir.description`:

Description
-----------

This function parses the XDomain properties data block into format that
can be traversed using the helper functions provided by this module.
Upon success returns the parsed directory. In case of error returns
\ ``NULL``\ . The resulting \ :c:type:`struct tb_property_dir <tb_property_dir>`\  needs to be released by
calling \ :c:func:`tb_property_free_dir`\  when not needed anymore.

The \ ``block``\  is expected to be root directory.

.. _`tb_property_create_dir`:

tb_property_create_dir
======================

.. c:function:: struct tb_property_dir *tb_property_create_dir(const uuid_t *uuid)

    Creates new property directory

    :param uuid:
        UUID used to identify the particular directory
    :type uuid: const uuid_t \*

.. _`tb_property_create_dir.description`:

Description
-----------

Creates new, empty property directory. If \ ``uuid``\  is \ ``NULL``\  then the
directory is assumed to be root directory.

.. _`tb_property_free_dir`:

tb_property_free_dir
====================

.. c:function:: void tb_property_free_dir(struct tb_property_dir *dir)

    Release memory allocated for property directory

    :param dir:
        Directory to release
    :type dir: struct tb_property_dir \*

.. _`tb_property_free_dir.description`:

Description
-----------

This will release all the memory the directory occupies including all
descendants. It is OK to pass \ ``NULL``\  \ ``dir``\ , then the function does
nothing.

.. _`tb_property_format_dir`:

tb_property_format_dir
======================

.. c:function:: ssize_t tb_property_format_dir(const struct tb_property_dir *dir, u32 *block, size_t block_len)

    Formats directory to the packed XDomain format

    :param dir:
        Directory to format
    :type dir: const struct tb_property_dir \*

    :param block:
        Property block where the packed data is placed
    :type block: u32 \*

    :param block_len:
        Length of the property block
    :type block_len: size_t

.. _`tb_property_format_dir.description`:

Description
-----------

This function formats the directory to the packed format that can be
then send over the thunderbolt fabric to receiving host. Returns \ ``0``\  in
case of success and negative errno on faulure. Passing \ ``NULL``\  in \ ``block``\ 
returns number of entries the block takes.

.. _`tb_property_add_immediate`:

tb_property_add_immediate
=========================

.. c:function:: int tb_property_add_immediate(struct tb_property_dir *parent, const char *key, u32 value)

    Add immediate property to directory

    :param parent:
        Directory to add the property
    :type parent: struct tb_property_dir \*

    :param key:
        Key for the property
    :type key: const char \*

    :param value:
        Immediate value to store with the property
    :type value: u32

.. _`tb_property_add_data`:

tb_property_add_data
====================

.. c:function:: int tb_property_add_data(struct tb_property_dir *parent, const char *key, const void *buf, size_t buflen)

    Adds arbitrary data property to directory

    :param parent:
        Directory to add the property
    :type parent: struct tb_property_dir \*

    :param key:
        Key for the property
    :type key: const char \*

    :param buf:
        Data buffer to add
    :type buf: const void \*

    :param buflen:
        Number of bytes in the data buffer
    :type buflen: size_t

.. _`tb_property_add_data.description`:

Description
-----------

Function takes a copy of \ ``buf``\  and adds it to the directory.

.. _`tb_property_add_text`:

tb_property_add_text
====================

.. c:function:: int tb_property_add_text(struct tb_property_dir *parent, const char *key, const char *text)

    Adds string property to directory

    :param parent:
        Directory to add the property
    :type parent: struct tb_property_dir \*

    :param key:
        Key for the property
    :type key: const char \*

    :param text:
        String to add
    :type text: const char \*

.. _`tb_property_add_text.description`:

Description
-----------

Function takes a copy of \ ``text``\  and adds it to the directory.

.. _`tb_property_add_dir`:

tb_property_add_dir
===================

.. c:function:: int tb_property_add_dir(struct tb_property_dir *parent, const char *key, struct tb_property_dir *dir)

    Adds a directory to the parent directory

    :param parent:
        Directory to add the property
    :type parent: struct tb_property_dir \*

    :param key:
        Key for the property
    :type key: const char \*

    :param dir:
        Directory to add
    :type dir: struct tb_property_dir \*

.. _`tb_property_remove`:

tb_property_remove
==================

.. c:function:: void tb_property_remove(struct tb_property *property)

    Removes property from a parent directory

    :param property:
        Property to remove
    :type property: struct tb_property \*

.. _`tb_property_remove.description`:

Description
-----------

Note memory for \ ``property``\  is released as well so it is not allowed to
touch the object after call to this function.

.. _`tb_property_find`:

tb_property_find
================

.. c:function:: struct tb_property *tb_property_find(struct tb_property_dir *dir, const char *key, enum tb_property_type type)

    Find a property from a directory

    :param dir:
        Directory where the property is searched
    :type dir: struct tb_property_dir \*

    :param key:
        Key to look for
    :type key: const char \*

    :param type:
        Type of the property
    :type type: enum tb_property_type

.. _`tb_property_find.description`:

Description
-----------

Finds and returns property from the given directory. Does not recurse
into sub-directories. Returns \ ``NULL``\  if the property was not found.

.. _`tb_property_get_next`:

tb_property_get_next
====================

.. c:function:: struct tb_property *tb_property_get_next(struct tb_property_dir *dir, struct tb_property *prev)

    Get next property from directory

    :param dir:
        Directory holding properties
    :type dir: struct tb_property_dir \*

    :param prev:
        Previous property in the directory (%NULL returns the first)
    :type prev: struct tb_property \*

.. This file was automatic generated / don't edit.


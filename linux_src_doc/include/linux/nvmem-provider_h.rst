.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/nvmem-provider.h

.. _`nvmem_config`:

struct nvmem_config
===================

.. c:type:: struct nvmem_config

    NVMEM device configuration

.. _`nvmem_config.definition`:

Definition
----------

.. code-block:: c

    struct nvmem_config {
        struct device *dev;
        const char *name;
        int id;
        struct module *owner;
        const struct nvmem_cell_info *cells;
        int ncells;
        bool read_only;
        bool root_only;
        nvmem_reg_read_t reg_read;
        nvmem_reg_write_t reg_write;
        int size;
        int word_size;
        int stride;
        void *priv;
        bool compat;
        struct device *base_dev;
    }

.. _`nvmem_config.members`:

Members
-------

dev
    Parent device.

name
    Optional name.

id
    Optional device ID used in full name. Ignored if name is NULL.

owner
    Pointer to exporter module. Used for refcounting.

cells
    Optional array of pre-defined NVMEM cells.

ncells
    Number of elements in cells.

read_only
    Device is read-only.

root_only
    Device is accessibly to root only.

reg_read
    Callback to read data.

reg_write
    Callback to write data.

size
    Device size.

word_size
    Minimum read/write access granularity.

stride
    Minimum read/write access stride.

priv
    User context passed to read/write callbacks.

compat
    *undescribed*

base_dev
    *undescribed*

.. _`nvmem_config.note`:

Note
----

A default "nvmem<id>" name will be assigned to the device if
no name is specified in its configuration. In such case "<id>" is
generated with \ :c:func:`ida_simple_get`\  and provided id field is ignored.

Specifying name and setting id to -1 implies a unique device
whose name is provided as-is (kept unaltered).

.. _`nvmem_cell_table`:

struct nvmem_cell_table
=======================

.. c:type:: struct nvmem_cell_table

    NVMEM cell definitions for given provider

.. _`nvmem_cell_table.definition`:

Definition
----------

.. code-block:: c

    struct nvmem_cell_table {
        const char *nvmem_name;
        const struct nvmem_cell_info *cells;
        size_t ncells;
        struct list_head node;
    }

.. _`nvmem_cell_table.members`:

Members
-------

nvmem_name
    Provider name.

cells
    Array of cell definitions.

ncells
    Number of cell definitions in the array.

node
    List node.

.. _`nvmem_cell_table.description`:

Description
-----------

This structure together with related helper functions is provided for users
that don't can't access the nvmem provided structure but wish to register
cell definitions for it e.g. board files registering an EEPROM device.

.. This file was automatic generated / don't edit.


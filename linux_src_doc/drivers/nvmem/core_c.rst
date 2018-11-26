.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nvmem/core.c

.. _`nvmem_add_cells`:

nvmem_add_cells
===============

.. c:function:: int nvmem_add_cells(struct nvmem_device *nvmem, const struct nvmem_cell_info *info, int ncells)

    Add cell information to an nvmem device

    :param nvmem:
        nvmem device to add cells to.
    :type nvmem: struct nvmem_device \*

    :param info:
        nvmem cell info to add to the device
    :type info: const struct nvmem_cell_info \*

    :param ncells:
        number of cells in info
    :type ncells: int

.. _`nvmem_add_cells.return`:

Return
------

0 or negative error code on failure.

.. _`nvmem_register_notifier`:

nvmem_register_notifier
=======================

.. c:function:: int nvmem_register_notifier(struct notifier_block *nb)

    Register a notifier block for nvmem events.

    :param nb:
        notifier block to be called on nvmem events.
    :type nb: struct notifier_block \*

.. _`nvmem_register_notifier.return`:

Return
------

0 on success, negative error number on failure.

.. _`nvmem_unregister_notifier`:

nvmem_unregister_notifier
=========================

.. c:function:: int nvmem_unregister_notifier(struct notifier_block *nb)

    Unregister a notifier block for nvmem events.

    :param nb:
        notifier block to be unregistered.
    :type nb: struct notifier_block \*

.. _`nvmem_unregister_notifier.return`:

Return
------

0 on success, negative error number on failure.

.. _`nvmem_register`:

nvmem_register
==============

.. c:function:: struct nvmem_device *nvmem_register(const struct nvmem_config *config)

    Register a nvmem device for given nvmem_config. Also creates an binary entry in /sys/bus/nvmem/devices/dev-name/nvmem

    :param config:
        nvmem device configuration with which nvmem device is created.
    :type config: const struct nvmem_config \*

.. _`nvmem_register.return`:

Return
------

Will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer to nvmem_device
on success.

.. _`nvmem_unregister`:

nvmem_unregister
================

.. c:function:: void nvmem_unregister(struct nvmem_device *nvmem)

    Unregister previously registered nvmem device

    :param nvmem:
        Pointer to previously registered nvmem device.
    :type nvmem: struct nvmem_device \*

.. _`devm_nvmem_register`:

devm_nvmem_register
===================

.. c:function:: struct nvmem_device *devm_nvmem_register(struct device *dev, const struct nvmem_config *config)

    Register a managed nvmem device for given nvmem_config. Also creates an binary entry in /sys/bus/nvmem/devices/dev-name/nvmem

    :param dev:
        Device that uses the nvmem device.
    :type dev: struct device \*

    :param config:
        nvmem device configuration with which nvmem device is created.
    :type config: const struct nvmem_config \*

.. _`devm_nvmem_register.return`:

Return
------

Will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer to nvmem_device
on success.

.. _`devm_nvmem_unregister`:

devm_nvmem_unregister
=====================

.. c:function:: int devm_nvmem_unregister(struct device *dev, struct nvmem_device *nvmem)

    Unregister previously registered managed nvmem device.

    :param dev:
        Device that uses the nvmem device.
    :type dev: struct device \*

    :param nvmem:
        Pointer to previously registered nvmem device.
    :type nvmem: struct nvmem_device \*

.. _`devm_nvmem_unregister.return`:

Return
------

Will be an negative on error or a zero on success.

.. _`of_nvmem_device_get`:

of_nvmem_device_get
===================

.. c:function:: struct nvmem_device *of_nvmem_device_get(struct device_node *np, const char *id)

    Get nvmem device from a given id

    :param np:
        Device tree node that uses the nvmem device.
    :type np: struct device_node \*

    :param id:
        nvmem name from nvmem-names property.
    :type id: const char \*

.. _`of_nvmem_device_get.return`:

Return
------

\ :c:func:`ERR_PTR`\  on error or a valid pointer to a struct nvmem_device
on success.

.. _`nvmem_device_get`:

nvmem_device_get
================

.. c:function:: struct nvmem_device *nvmem_device_get(struct device *dev, const char *dev_name)

    Get nvmem device from a given id

    :param dev:
        Device that uses the nvmem device.
    :type dev: struct device \*

    :param dev_name:
        name of the requested nvmem device.
    :type dev_name: const char \*

.. _`nvmem_device_get.return`:

Return
------

\ :c:func:`ERR_PTR`\  on error or a valid pointer to a struct nvmem_device
on success.

.. _`devm_nvmem_device_put`:

devm_nvmem_device_put
=====================

.. c:function:: void devm_nvmem_device_put(struct device *dev, struct nvmem_device *nvmem)

    put alredy got nvmem device

    :param dev:
        Device that uses the nvmem device.
    :type dev: struct device \*

    :param nvmem:
        pointer to nvmem device allocated by \ :c:func:`devm_nvmem_cell_get`\ ,
        that needs to be released.
    :type nvmem: struct nvmem_device \*

.. _`nvmem_device_put`:

nvmem_device_put
================

.. c:function:: void nvmem_device_put(struct nvmem_device *nvmem)

    put alredy got nvmem device

    :param nvmem:
        pointer to nvmem device that needs to be released.
    :type nvmem: struct nvmem_device \*

.. _`devm_nvmem_device_get`:

devm_nvmem_device_get
=====================

.. c:function:: struct nvmem_device *devm_nvmem_device_get(struct device *dev, const char *id)

    Get nvmem cell of device form a given id

    :param dev:
        Device that requests the nvmem device.
    :type dev: struct device \*

    :param id:
        name id for the requested nvmem device.
    :type id: const char \*

.. _`devm_nvmem_device_get.return`:

Return
------

\ :c:func:`ERR_PTR`\  on error or a valid pointer to a struct nvmem_cell
on success.  The nvmem_cell will be freed by the automatically once the
device is freed.

.. _`of_nvmem_cell_get`:

of_nvmem_cell_get
=================

.. c:function:: struct nvmem_cell *of_nvmem_cell_get(struct device_node *np, const char *id)

    Get a nvmem cell from given device node and cell id

    :param np:
        Device tree node that uses the nvmem cell.
    :type np: struct device_node \*

    :param id:
        nvmem cell name from nvmem-cell-names property, or NULL
        for the cell at index 0 (the lone cell with no accompanying
        nvmem-cell-names property).
    :type id: const char \*

.. _`of_nvmem_cell_get.return`:

Return
------

Will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer
to a struct nvmem_cell.  The nvmem_cell will be freed by the
\ :c:func:`nvmem_cell_put`\ .

.. _`nvmem_cell_get`:

nvmem_cell_get
==============

.. c:function:: struct nvmem_cell *nvmem_cell_get(struct device *dev, const char *id)

    Get nvmem cell of device form a given cell name

    :param dev:
        Device that requests the nvmem cell.
    :type dev: struct device \*

    :param id:
        nvmem cell name to get (this corresponds with the name from the
        nvmem-cell-names property for DT systems and with the con_id from
        the lookup entry for non-DT systems).
    :type id: const char \*

.. _`nvmem_cell_get.return`:

Return
------

Will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer
to a struct nvmem_cell.  The nvmem_cell will be freed by the
\ :c:func:`nvmem_cell_put`\ .

.. _`devm_nvmem_cell_get`:

devm_nvmem_cell_get
===================

.. c:function:: struct nvmem_cell *devm_nvmem_cell_get(struct device *dev, const char *id)

    Get nvmem cell of device form a given id

    :param dev:
        Device that requests the nvmem cell.
    :type dev: struct device \*

    :param id:
        nvmem cell name id to get.
    :type id: const char \*

.. _`devm_nvmem_cell_get.return`:

Return
------

Will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer
to a struct nvmem_cell.  The nvmem_cell will be freed by the
automatically once the device is freed.

.. _`devm_nvmem_cell_put`:

devm_nvmem_cell_put
===================

.. c:function:: void devm_nvmem_cell_put(struct device *dev, struct nvmem_cell *cell)

    Release previously allocated nvmem cell from devm_nvmem_cell_get.

    :param dev:
        Device that requests the nvmem cell.
    :type dev: struct device \*

    :param cell:
        Previously allocated nvmem cell by \ :c:func:`devm_nvmem_cell_get`\ .
    :type cell: struct nvmem_cell \*

.. _`nvmem_cell_put`:

nvmem_cell_put
==============

.. c:function:: void nvmem_cell_put(struct nvmem_cell *cell)

    Release previously allocated nvmem cell.

    :param cell:
        Previously allocated nvmem cell by \ :c:func:`nvmem_cell_get`\ .
    :type cell: struct nvmem_cell \*

.. _`nvmem_cell_read`:

nvmem_cell_read
===============

.. c:function:: void *nvmem_cell_read(struct nvmem_cell *cell, size_t *len)

    Read a given nvmem cell

    :param cell:
        nvmem cell to be read.
    :type cell: struct nvmem_cell \*

    :param len:
        pointer to length of cell which will be populated on successful read;
        can be NULL.
    :type len: size_t \*

.. _`nvmem_cell_read.return`:

Return
------

\ :c:func:`ERR_PTR`\  on error or a valid pointer to a buffer on success. The
buffer should be freed by the consumer with a \ :c:func:`kfree`\ .

.. _`nvmem_cell_write`:

nvmem_cell_write
================

.. c:function:: int nvmem_cell_write(struct nvmem_cell *cell, void *buf, size_t len)

    Write to a given nvmem cell

    :param cell:
        nvmem cell to be written.
    :type cell: struct nvmem_cell \*

    :param buf:
        Buffer to be written.
    :type buf: void \*

    :param len:
        length of buffer to be written to nvmem cell.
    :type len: size_t

.. _`nvmem_cell_write.return`:

Return
------

length of bytes written or negative on failure.

.. _`nvmem_cell_read_u32`:

nvmem_cell_read_u32
===================

.. c:function:: int nvmem_cell_read_u32(struct device *dev, const char *cell_id, u32 *val)

    Read a cell value as an u32

    :param dev:
        Device that requests the nvmem cell.
    :type dev: struct device \*

    :param cell_id:
        Name of nvmem cell to read.
    :type cell_id: const char \*

    :param val:
        pointer to output value.
    :type val: u32 \*

.. _`nvmem_cell_read_u32.return`:

Return
------

0 on success or negative errno.

.. _`nvmem_device_cell_read`:

nvmem_device_cell_read
======================

.. c:function:: ssize_t nvmem_device_cell_read(struct nvmem_device *nvmem, struct nvmem_cell_info *info, void *buf)

    Read a given nvmem device and cell

    :param nvmem:
        nvmem device to read from.
    :type nvmem: struct nvmem_device \*

    :param info:
        nvmem cell info to be read.
    :type info: struct nvmem_cell_info \*

    :param buf:
        buffer pointer which will be populated on successful read.
    :type buf: void \*

.. _`nvmem_device_cell_read.return`:

Return
------

length of successful bytes read on success and negative
error code on error.

.. _`nvmem_device_cell_write`:

nvmem_device_cell_write
=======================

.. c:function:: int nvmem_device_cell_write(struct nvmem_device *nvmem, struct nvmem_cell_info *info, void *buf)

    Write cell to a given nvmem device

    :param nvmem:
        nvmem device to be written to.
    :type nvmem: struct nvmem_device \*

    :param info:
        nvmem cell info to be written.
    :type info: struct nvmem_cell_info \*

    :param buf:
        buffer to be written to cell.
    :type buf: void \*

.. _`nvmem_device_cell_write.return`:

Return
------

length of bytes written or negative error code on failure.

.. _`nvmem_device_read`:

nvmem_device_read
=================

.. c:function:: int nvmem_device_read(struct nvmem_device *nvmem, unsigned int offset, size_t bytes, void *buf)

    Read from a given nvmem device

    :param nvmem:
        nvmem device to read from.
    :type nvmem: struct nvmem_device \*

    :param offset:
        offset in nvmem device.
    :type offset: unsigned int

    :param bytes:
        number of bytes to read.
    :type bytes: size_t

    :param buf:
        buffer pointer which will be populated on successful read.
    :type buf: void \*

.. _`nvmem_device_read.return`:

Return
------

length of successful bytes read on success and negative
error code on error.

.. _`nvmem_device_write`:

nvmem_device_write
==================

.. c:function:: int nvmem_device_write(struct nvmem_device *nvmem, unsigned int offset, size_t bytes, void *buf)

    Write cell to a given nvmem device

    :param nvmem:
        nvmem device to be written to.
    :type nvmem: struct nvmem_device \*

    :param offset:
        offset in nvmem device.
    :type offset: unsigned int

    :param bytes:
        number of bytes to write.
    :type bytes: size_t

    :param buf:
        buffer to be written.
    :type buf: void \*

.. _`nvmem_device_write.return`:

Return
------

length of bytes written or negative error code on failure.

.. _`nvmem_add_cell_table`:

nvmem_add_cell_table
====================

.. c:function:: void nvmem_add_cell_table(struct nvmem_cell_table *table)

    register a table of cell info entries

    :param table:
        table of cell info entries
    :type table: struct nvmem_cell_table \*

.. _`nvmem_del_cell_table`:

nvmem_del_cell_table
====================

.. c:function:: void nvmem_del_cell_table(struct nvmem_cell_table *table)

    remove a previously registered cell info table

    :param table:
        table of cell info entries
    :type table: struct nvmem_cell_table \*

.. _`nvmem_add_cell_lookups`:

nvmem_add_cell_lookups
======================

.. c:function:: void nvmem_add_cell_lookups(struct nvmem_cell_lookup *entries, size_t nentries)

    register a list of cell lookup entries

    :param entries:
        array of cell lookup entries
    :type entries: struct nvmem_cell_lookup \*

    :param nentries:
        number of cell lookup entries in the array
    :type nentries: size_t

.. _`nvmem_del_cell_lookups`:

nvmem_del_cell_lookups
======================

.. c:function:: void nvmem_del_cell_lookups(struct nvmem_cell_lookup *entries, size_t nentries)

    remove a list of previously added cell lookup entries

    :param entries:
        array of cell lookup entries
    :type entries: struct nvmem_cell_lookup \*

    :param nentries:
        number of cell lookup entries in the array
    :type nentries: size_t

.. _`nvmem_dev_name`:

nvmem_dev_name
==============

.. c:function:: const char *nvmem_dev_name(struct nvmem_device *nvmem)

    Get the name of a given nvmem device.

    :param nvmem:
        nvmem device.
    :type nvmem: struct nvmem_device \*

.. _`nvmem_dev_name.return`:

Return
------

name of the nvmem device.

.. This file was automatic generated / don't edit.


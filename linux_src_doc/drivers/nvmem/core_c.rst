.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nvmem/core.c

.. _`nvmem_register`:

nvmem_register
==============

.. c:function:: struct nvmem_device *nvmem_register(const struct nvmem_config *config)

    Register a nvmem device for given nvmem_config. Also creates an binary entry in /sys/bus/nvmem/devices/dev-name/nvmem

    :param const struct nvmem_config \*config:
        nvmem device configuration with which nvmem device is created.

.. _`nvmem_register.return`:

Return
------

Will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer to nvmem_device
on success.

.. _`nvmem_unregister`:

nvmem_unregister
================

.. c:function:: int nvmem_unregister(struct nvmem_device *nvmem)

    Unregister previously registered nvmem device

    :param struct nvmem_device \*nvmem:
        Pointer to previously registered nvmem device.

.. _`nvmem_unregister.return`:

Return
------

Will be an negative on error or a zero on success.

.. _`of_nvmem_device_get`:

of_nvmem_device_get
===================

.. c:function:: struct nvmem_device *of_nvmem_device_get(struct device_node *np, const char *id)

    Get nvmem device from a given id

    :param struct device_node \*np:
        *undescribed*

    :param const char \*id:
        nvmem name from nvmem-names property.

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

    :param struct device \*dev:
        Device that uses the nvmem device

    :param const char \*dev_name:
        *undescribed*

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

    :param struct device \*dev:
        *undescribed*

    :param struct nvmem_device \*nvmem:
        pointer to nvmem device allocated by \ :c:func:`devm_nvmem_cell_get`\ ,
        that needs to be released.

.. _`nvmem_device_put`:

nvmem_device_put
================

.. c:function:: void nvmem_device_put(struct nvmem_device *nvmem)

    put alredy got nvmem device

    :param struct nvmem_device \*nvmem:
        pointer to nvmem device that needs to be released.

.. _`devm_nvmem_device_get`:

devm_nvmem_device_get
=====================

.. c:function:: struct nvmem_device *devm_nvmem_device_get(struct device *dev, const char *id)

    Get nvmem cell of device form a given id

    :param struct device \*dev:
        Device tree node that uses the nvmem cell

    :param const char \*id:
        nvmem name in nvmems property.

.. _`devm_nvmem_device_get.return`:

Return
------

\ :c:func:`ERR_PTR`\  on error or a valid pointer to a struct nvmem_cell
on success.  The nvmem_cell will be freed by the automatically once the
device is freed.

.. _`of_nvmem_cell_get`:

of_nvmem_cell_get
=================

.. c:function:: struct nvmem_cell *of_nvmem_cell_get(struct device_node *np, const char *name)

    Get a nvmem cell from given device node and cell id

    :param struct device_node \*np:
        *undescribed*

    :param const char \*name:
        *undescribed*

.. _`of_nvmem_cell_get.return`:

Return
------

Will be an \ :c:func:`ERR_PTR`\  on error or a valid pointer
to a struct nvmem_cell.  The nvmem_cell will be freed by the
\ :c:func:`nvmem_cell_put`\ .

.. _`nvmem_cell_get`:

nvmem_cell_get
==============

.. c:function:: struct nvmem_cell *nvmem_cell_get(struct device *dev, const char *cell_id)

    Get nvmem cell of device form a given cell name

    :param struct device \*dev:
        Device tree node that uses the nvmem cell

    :param const char \*cell_id:
        *undescribed*

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

    :param struct device \*dev:
        Device tree node that uses the nvmem cell

    :param const char \*id:
        nvmem id in nvmem-names property.

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

    :param struct device \*dev:
        *undescribed*

    :param struct nvmem_cell \*cell:
        Previously allocated nvmem cell by \ :c:func:`devm_nvmem_cell_get`\ 

.. _`nvmem_cell_put`:

nvmem_cell_put
==============

.. c:function:: void nvmem_cell_put(struct nvmem_cell *cell)

    Release previously allocated nvmem cell.

    :param struct nvmem_cell \*cell:
        Previously allocated nvmem cell by \ :c:func:`nvmem_cell_get`\ 

.. _`nvmem_cell_read`:

nvmem_cell_read
===============

.. c:function:: void *nvmem_cell_read(struct nvmem_cell *cell, size_t *len)

    Read a given nvmem cell

    :param struct nvmem_cell \*cell:
        nvmem cell to be read.

    :param size_t \*len:
        pointer to length of cell which will be populated on successful read.

.. _`nvmem_cell_read.return`:

Return
------

\ :c:func:`ERR_PTR`\  on error or a valid pointer to a char \* buffer on success.
The buffer should be freed by the consumer with a \ :c:func:`kfree`\ .

.. _`nvmem_cell_write`:

nvmem_cell_write
================

.. c:function:: int nvmem_cell_write(struct nvmem_cell *cell, void *buf, size_t len)

    Write to a given nvmem cell

    :param struct nvmem_cell \*cell:
        nvmem cell to be written.

    :param void \*buf:
        Buffer to be written.

    :param size_t len:
        length of buffer to be written to nvmem cell.

.. _`nvmem_cell_write.return`:

Return
------

length of bytes written or negative on failure.

.. _`nvmem_device_cell_read`:

nvmem_device_cell_read
======================

.. c:function:: ssize_t nvmem_device_cell_read(struct nvmem_device *nvmem, struct nvmem_cell_info *info, void *buf)

    Read a given nvmem device and cell

    :param struct nvmem_device \*nvmem:
        nvmem device to read from.

    :param struct nvmem_cell_info \*info:
        nvmem cell info to be read.

    :param void \*buf:
        buffer pointer which will be populated on successful read.

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

    :param struct nvmem_device \*nvmem:
        nvmem device to be written to.

    :param struct nvmem_cell_info \*info:
        nvmem cell info to be written

    :param void \*buf:
        buffer to be written to cell.

.. _`nvmem_device_cell_write.return`:

Return
------

length of bytes written or negative error code on failure.

.. _`nvmem_device_read`:

nvmem_device_read
=================

.. c:function:: int nvmem_device_read(struct nvmem_device *nvmem, unsigned int offset, size_t bytes, void *buf)

    Read from a given nvmem device

    :param struct nvmem_device \*nvmem:
        nvmem device to read from.

    :param unsigned int offset:
        offset in nvmem device.

    :param size_t bytes:
        number of bytes to read.

    :param void \*buf:
        buffer pointer which will be populated on successful read.

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

    :param struct nvmem_device \*nvmem:
        nvmem device to be written to.

    :param unsigned int offset:
        offset in nvmem device.

    :param size_t bytes:
        number of bytes to write.

    :param void \*buf:
        buffer to be written.

.. _`nvmem_device_write.return`:

Return
------

length of bytes written or negative error code on failure.

.. This file was automatic generated / don't edit.


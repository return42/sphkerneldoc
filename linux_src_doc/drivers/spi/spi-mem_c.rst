.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/spi/spi-mem.c

.. _`spi_controller_dma_map_mem_op_data`:

spi_controller_dma_map_mem_op_data
==================================

.. c:function:: int spi_controller_dma_map_mem_op_data(struct spi_controller *ctlr, const struct spi_mem_op *op, struct sg_table *sgt)

    DMA-map the buffer attached to a memory operation

    :param struct spi_controller \*ctlr:
        the SPI controller requesting this \ :c:func:`dma_map`\ 

    :param const struct spi_mem_op \*op:
        the memory operation containing the buffer to map

    :param struct sg_table \*sgt:
        a pointer to a non-initialized sg_table that will be filled by this
        function

.. _`spi_controller_dma_map_mem_op_data.description`:

Description
-----------

Some controllers might want to do DMA on the data buffer embedded in \ ``op``\ .
This helper prepares everything for you and provides a ready-to-use
sg_table. This function is not intended to be called from spi drivers.
Only SPI controller drivers should use it.
Note that the caller must ensure the memory region pointed by
op->data.buf.{in,out} is DMA-able before calling this function.

.. _`spi_controller_dma_map_mem_op_data.return`:

Return
------

0 in case of success, a negative error code otherwise.

.. _`spi_controller_dma_unmap_mem_op_data`:

spi_controller_dma_unmap_mem_op_data
====================================

.. c:function:: void spi_controller_dma_unmap_mem_op_data(struct spi_controller *ctlr, const struct spi_mem_op *op, struct sg_table *sgt)

    DMA-unmap the buffer attached to a memory operation

    :param struct spi_controller \*ctlr:
        the SPI controller requesting this \ :c:func:`dma_unmap`\ 

    :param const struct spi_mem_op \*op:
        the memory operation containing the buffer to unmap

    :param struct sg_table \*sgt:
        a pointer to an sg_table previously initialized by
        \ :c:func:`spi_controller_dma_map_mem_op_data`\ 

.. _`spi_controller_dma_unmap_mem_op_data.description`:

Description
-----------

Some controllers might want to do DMA on the data buffer embedded in \ ``op``\ .
This helper prepares things so that the CPU can access the
op->data.buf.{in,out} buffer again.

This function is not intended to be called from SPI drivers. Only SPI
controller drivers should use it.

This function should be called after the DMA operation has finished and is
only valid if the previous \ :c:func:`spi_controller_dma_map_mem_op_data`\  call
returned 0.

.. _`spi_controller_dma_unmap_mem_op_data.return`:

Return
------

0 in case of success, a negative error code otherwise.

.. _`spi_mem_supports_op`:

spi_mem_supports_op
===================

.. c:function:: bool spi_mem_supports_op(struct spi_mem *mem, const struct spi_mem_op *op)

    Check if a memory device and the controller it is connected to support a specific memory operation

    :param struct spi_mem \*mem:
        the SPI memory

    :param const struct spi_mem_op \*op:
        the memory operation to check

.. _`spi_mem_supports_op.description`:

Description
-----------

Some controllers are only supporting Single or Dual IOs, others might only
support specific opcodes, or it can even be that the controller and device
both support Quad IOs but the hardware prevents you from using it because
only 2 IO lines are connected.

This function checks whether a specific operation is supported.

.. _`spi_mem_supports_op.return`:

Return
------

true if \ ``op``\  is supported, false otherwise.

.. _`spi_mem_exec_op`:

spi_mem_exec_op
===============

.. c:function:: int spi_mem_exec_op(struct spi_mem *mem, const struct spi_mem_op *op)

    Execute a memory operation

    :param struct spi_mem \*mem:
        the SPI memory

    :param const struct spi_mem_op \*op:
        the memory operation to execute

.. _`spi_mem_exec_op.description`:

Description
-----------

Executes a memory operation.

This function first checks that \ ``op``\  is supported and then tries to execute
it.

.. _`spi_mem_exec_op.return`:

Return
------

0 in case of success, a negative error code otherwise.

.. _`spi_mem_adjust_op_size`:

spi_mem_adjust_op_size
======================

.. c:function:: int spi_mem_adjust_op_size(struct spi_mem *mem, struct spi_mem_op *op)

    Adjust the data size of a SPI mem operation to match controller limitations

    :param struct spi_mem \*mem:
        the SPI memory

    :param struct spi_mem_op \*op:
        the operation to adjust

.. _`spi_mem_adjust_op_size.description`:

Description
-----------

Some controllers have FIFO limitations and must split a data transfer
operation into multiple ones, others require a specific alignment for
optimized accesses. This function allows SPI mem drivers to split a single
operation into multiple sub-operations when required.

.. _`spi_mem_adjust_op_size.return`:

Return
------

a negative error code if the controller can't properly adjust \ ``op``\ ,
0 otherwise. Note that \ ``op``\ ->data.nbytes will be updated if \ ``op``\ 
can't be handled in a single step.

.. _`spi_mem_driver_register_with_owner`:

spi_mem_driver_register_with_owner
==================================

.. c:function:: int spi_mem_driver_register_with_owner(struct spi_mem_driver *memdrv, struct module *owner)

    Register a SPI memory driver

    :param struct spi_mem_driver \*memdrv:
        the SPI memory driver to register

    :param struct module \*owner:
        the owner of this driver

.. _`spi_mem_driver_register_with_owner.description`:

Description
-----------

Registers a SPI memory driver.

.. _`spi_mem_driver_register_with_owner.return`:

Return
------

0 in case of success, a negative error core otherwise.

.. _`spi_mem_driver_unregister`:

spi_mem_driver_unregister
=========================

.. c:function:: void spi_mem_driver_unregister(struct spi_mem_driver *memdrv)

    Unregister a SPI memory driver

    :param struct spi_mem_driver \*memdrv:
        the SPI memory driver to unregister

.. _`spi_mem_driver_unregister.description`:

Description
-----------

Unregisters a SPI memory driver.

.. This file was automatic generated / don't edit.


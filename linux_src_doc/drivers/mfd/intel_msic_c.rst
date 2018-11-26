.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mfd/intel_msic.c

.. _`intel_msic`:

struct intel_msic
=================

.. c:type:: struct intel_msic

    an MSIC MFD instance

.. _`intel_msic.definition`:

Definition
----------

.. code-block:: c

    struct intel_msic {
        struct platform_device *pdev;
        unsigned vendor;
        unsigned version;
        void __iomem *irq_base;
    }

.. _`intel_msic.members`:

Members
-------

pdev
    pointer to the platform device

vendor
    vendor ID

version
    chip version

irq_base
    base address of the mapped MSIC SRAM interrupt tree

.. _`intel_msic_reg_read`:

intel_msic_reg_read
===================

.. c:function:: int intel_msic_reg_read(unsigned short reg, u8 *val)

    read a single MSIC register

    :param reg:
        register to read
    :type reg: unsigned short

    :param val:
        register value is placed here
    :type val: u8 \*

.. _`intel_msic_reg_read.description`:

Description
-----------

Read a single register from MSIC. Returns \ ``0``\  on success and negative
errno in case of failure.

Function may sleep.

.. _`intel_msic_reg_write`:

intel_msic_reg_write
====================

.. c:function:: int intel_msic_reg_write(unsigned short reg, u8 val)

    write a single MSIC register

    :param reg:
        register to write
    :type reg: unsigned short

    :param val:
        value to write to that register
    :type val: u8

.. _`intel_msic_reg_write.description`:

Description
-----------

Write a single MSIC register. Returns 0 on success and negative
errno in case of failure.

Function may sleep.

.. _`intel_msic_reg_update`:

intel_msic_reg_update
=====================

.. c:function:: int intel_msic_reg_update(unsigned short reg, u8 val, u8 mask)

    update a single MSIC register

    :param reg:
        register to update
    :type reg: unsigned short

    :param val:
        value to write to the register
    :type val: u8

    :param mask:
        specifies which of the bits are updated (%0 = don't update,
        \ ``1``\  = update)
    :type mask: u8

.. _`intel_msic_reg_update.description`:

Description
-----------

Perform an update to a register \ ``reg``\ . \ ``mask``\  is used to specify which
bits are updated. Returns \ ``0``\  in case of success and negative errno in
case of failure.

Function may sleep.

.. _`intel_msic_bulk_read`:

intel_msic_bulk_read
====================

.. c:function:: int intel_msic_bulk_read(unsigned short *reg, u8 *buf, size_t count)

    read an array of registers

    :param reg:
        array of register addresses to read
    :type reg: unsigned short \*

    :param buf:
        array where the read values are placed
    :type buf: u8 \*

    :param count:
        number of registers to read
    :type count: size_t

.. _`intel_msic_bulk_read.description`:

Description
-----------

Function reads \ ``count``\  registers from the MSIC using addresses passed in
\ ``reg``\ . Read values are placed in \ ``buf``\ . Reads are performed atomically
wrt. MSIC.

Returns \ ``0``\  in case of success and negative errno in case of failure.

Function may sleep.

.. _`intel_msic_bulk_write`:

intel_msic_bulk_write
=====================

.. c:function:: int intel_msic_bulk_write(unsigned short *reg, u8 *buf, size_t count)

    write an array of values to the MSIC registers

    :param reg:
        array of registers to write
    :type reg: unsigned short \*

    :param buf:
        values to write to each register
    :type buf: u8 \*

    :param count:
        number of registers to write
    :type count: size_t

.. _`intel_msic_bulk_write.description`:

Description
-----------

Function writes \ ``count``\  registers in \ ``buf``\  to MSIC. Writes are performed
atomically wrt MSIC. Returns \ ``0``\  in case of success and negative errno in
case of failure.

Function may sleep.

.. _`intel_msic_irq_read`:

intel_msic_irq_read
===================

.. c:function:: int intel_msic_irq_read(struct intel_msic *msic, unsigned short reg, u8 *val)

    read a register from an MSIC interrupt tree

    :param msic:
        MSIC instance
    :type msic: struct intel_msic \*

    :param reg:
        interrupt register (between \ ``INTEL_MSIC_IRQLVL1``\  and
        \ ``INTEL_MSIC_RESETIRQ2``\ )
    :type reg: unsigned short

    :param val:
        value of the register is placed here
    :type val: u8 \*

.. _`intel_msic_irq_read.description`:

Description
-----------

This function can be used by an MSIC subdevice interrupt handler to read
a register value from the MSIC interrupt tree. In this way subdevice
drivers don't have to map in the interrupt tree themselves but can just
call this function instead.

Function doesn't sleep and is callable from interrupt context.

Returns \ ``-EINVAL``\  if \ ``reg``\  is outside of the allowed register region.

.. This file was automatic generated / don't edit.


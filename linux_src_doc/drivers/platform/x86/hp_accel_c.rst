.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/platform/x86/hp_accel.c

.. _`lis3lv02d_acpi_init`:

lis3lv02d_acpi_init
===================

.. c:function:: int lis3lv02d_acpi_init(struct lis3lv02d *lis3)

    ACPI \_INI method: initialize the device.

    :param lis3:
        pointer to the device struct
    :type lis3: struct lis3lv02d \*

.. _`lis3lv02d_acpi_init.description`:

Description
-----------

Returns 0 on success.

.. _`lis3lv02d_acpi_read`:

lis3lv02d_acpi_read
===================

.. c:function:: int lis3lv02d_acpi_read(struct lis3lv02d *lis3, int reg, u8 *ret)

    ACPI ALRD method: read a register

    :param lis3:
        pointer to the device struct
    :type lis3: struct lis3lv02d \*

    :param reg:
        the register to read
    :type reg: int

    :param ret:
        result of the operation
    :type ret: u8 \*

.. _`lis3lv02d_acpi_read.description`:

Description
-----------

Returns 0 on success.

.. _`lis3lv02d_acpi_write`:

lis3lv02d_acpi_write
====================

.. c:function:: int lis3lv02d_acpi_write(struct lis3lv02d *lis3, int reg, u8 val)

    ACPI ALWR method: write to a register

    :param lis3:
        pointer to the device struct
    :type lis3: struct lis3lv02d \*

    :param reg:
        the register to write to
    :type reg: int

    :param val:
        the value to write
    :type val: u8

.. _`lis3lv02d_acpi_write.description`:

Description
-----------

Returns 0 on success.

.. This file was automatic generated / don't edit.


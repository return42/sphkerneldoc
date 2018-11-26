.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/iio/imu/adis.h

.. _`adis_data`:

struct adis_data
================

.. c:type:: struct adis_data

    ADIS chip variant specific data

.. _`adis_data.definition`:

Definition
----------

.. code-block:: c

    struct adis_data {
        unsigned int read_delay;
        unsigned int write_delay;
        unsigned int glob_cmd_reg;
        unsigned int msc_ctrl_reg;
        unsigned int diag_stat_reg;
        unsigned int self_test_mask;
        bool self_test_no_autoclear;
        unsigned int startup_delay;
        const char * const *status_error_msgs;
        unsigned int status_error_mask;
        int (*enable_irq)(struct adis *adis, bool enable);
        bool has_paging;
    }

.. _`adis_data.members`:

Members
-------

read_delay
    SPI delay for read operations in us

write_delay
    SPI delay for write operations in us

glob_cmd_reg
    Register address of the GLOB_CMD register

msc_ctrl_reg
    Register address of the MSC_CTRL register

diag_stat_reg
    Register address of the DIAG_STAT register

self_test_mask
    *undescribed*

self_test_no_autoclear
    *undescribed*

startup_delay
    *undescribed*

status_error_msgs
    Array of error messgaes

status_error_mask
    *undescribed*

enable_irq
    *undescribed*

has_paging
    *undescribed*

.. _`adis_write_reg_8`:

adis_write_reg_8
================

.. c:function:: int adis_write_reg_8(struct adis *adis, unsigned int reg, uint8_t val)

    Write single byte to a register

    :param adis:
        The adis device
    :type adis: struct adis \*

    :param reg:
        The address of the register to be written
    :type reg: unsigned int

    :param val:
        *undescribed*
    :type val: uint8_t

.. _`adis_write_reg_16`:

adis_write_reg_16
=================

.. c:function:: int adis_write_reg_16(struct adis *adis, unsigned int reg, uint16_t val)

    Write 2 bytes to a pair of registers

    :param adis:
        The adis device
    :type adis: struct adis \*

    :param reg:
        The address of the lower of the two registers
    :type reg: unsigned int

    :param val:
        *undescribed*
    :type val: uint16_t

.. _`adis_write_reg_32`:

adis_write_reg_32
=================

.. c:function:: int adis_write_reg_32(struct adis *adis, unsigned int reg, uint32_t val)

    write 4 bytes to four registers

    :param adis:
        The adis device
    :type adis: struct adis \*

    :param reg:
        The address of the lower of the four register
    :type reg: unsigned int

    :param val:
        *undescribed*
    :type val: uint32_t

.. _`adis_read_reg_16`:

adis_read_reg_16
================

.. c:function:: int adis_read_reg_16(struct adis *adis, unsigned int reg, uint16_t *val)

    read 2 bytes from a 16-bit register

    :param adis:
        The adis device
    :type adis: struct adis \*

    :param reg:
        The address of the lower of the two registers
    :type reg: unsigned int

    :param val:
        The value read back from the device
    :type val: uint16_t \*

.. _`adis_read_reg_32`:

adis_read_reg_32
================

.. c:function:: int adis_read_reg_32(struct adis *adis, unsigned int reg, uint32_t *val)

    read 4 bytes from a 32-bit register

    :param adis:
        The adis device
    :type adis: struct adis \*

    :param reg:
        The address of the lower of the two registers
    :type reg: unsigned int

    :param val:
        The value read back from the device
    :type val: uint32_t \*

.. This file was automatic generated / don't edit.


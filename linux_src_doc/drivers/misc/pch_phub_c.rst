.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/pch_phub.c

.. _`pch_phub_reg`:

struct pch_phub_reg
===================

.. c:type:: struct pch_phub_reg

    PHUB register structure

.. _`pch_phub_reg.definition`:

Definition
----------

.. code-block:: c

    struct pch_phub_reg {
        u32 phub_id_reg;
        u32 q_pri_val_reg;
        u32 rc_q_maxsize_reg;
        u32 bri_q_maxsize_reg;
        u32 comp_resp_timeout_reg;
        u32 bus_slave_control_reg;
        u32 deadlock_avoid_type_reg;
        u32 intpin_reg_wpermit_reg0;
        u32 intpin_reg_wpermit_reg1;
        u32 intpin_reg_wpermit_reg2;
        u32 intpin_reg_wpermit_reg3;
        u32 int_reduce_control_reg[MAX_NUM_INT_REDUCE_CONTROL_REG];
        u32 clkcfg_reg;
        u32 funcsel_reg;
        void __iomem *pch_phub_base_address;
        void __iomem *pch_phub_extrom_base_address;
        u32 pch_mac_start_address;
        u32 pch_opt_rom_start_address;
        int ioh_type;
        struct pci_dev *pdev;
    }

.. _`pch_phub_reg.members`:

Members
-------

phub_id_reg
    PHUB_ID register val

q_pri_val_reg
    QUEUE_PRI_VAL register val

rc_q_maxsize_reg
    RC_QUEUE_MAXSIZE register val

bri_q_maxsize_reg
    BRI_QUEUE_MAXSIZE register val

comp_resp_timeout_reg
    COMP_RESP_TIMEOUT register val

bus_slave_control_reg
    BUS_SLAVE_CONTROL_REG register val

deadlock_avoid_type_reg
    DEADLOCK_AVOID_TYPE register val

intpin_reg_wpermit_reg0
    INTPIN_REG_WPERMIT register 0 val

intpin_reg_wpermit_reg1
    INTPIN_REG_WPERMIT register 1 val

intpin_reg_wpermit_reg2
    INTPIN_REG_WPERMIT register 2 val

intpin_reg_wpermit_reg3
    INTPIN_REG_WPERMIT register 3 val

int_reduce_control_reg
    INT_REDUCE_CONTROL registers val

clkcfg_reg
    CLK CFG register val

funcsel_reg
    Function select register value

pch_phub_base_address
    Register base address

pch_phub_extrom_base_address
    external rom base address

pch_mac_start_address
    MAC address area start address

pch_opt_rom_start_address
    Option ROM start address

ioh_type
    Save IOH type

pdev
    pointer to pci device struct

.. _`pch_phub_read_modify_write_reg`:

pch_phub_read_modify_write_reg
==============================

.. c:function:: void pch_phub_read_modify_write_reg(struct pch_phub_reg *chip, unsigned int reg_addr_offset, unsigned int data, unsigned int mask)

    Reading modifying and writing register

    :param chip:
        *undescribed*
    :type chip: struct pch_phub_reg \*

    :param reg_addr_offset:
        Register offset address value.
    :type reg_addr_offset: unsigned int

    :param data:
        Writing value.
    :type data: unsigned int

    :param mask:
        Mask value.
    :type mask: unsigned int

.. _`pch_phub_read_serial_rom`:

pch_phub_read_serial_rom
========================

.. c:function:: void pch_phub_read_serial_rom(struct pch_phub_reg *chip, unsigned int offset_address, u8 *data)

    Reading Serial ROM

    :param chip:
        *undescribed*
    :type chip: struct pch_phub_reg \*

    :param offset_address:
        Serial ROM offset address to read.
    :type offset_address: unsigned int

    :param data:
        Read buffer for specified Serial ROM value.
    :type data: u8 \*

.. _`pch_phub_write_serial_rom`:

pch_phub_write_serial_rom
=========================

.. c:function:: int pch_phub_write_serial_rom(struct pch_phub_reg *chip, unsigned int offset_address, u8 data)

    Writing Serial ROM

    :param chip:
        *undescribed*
    :type chip: struct pch_phub_reg \*

    :param offset_address:
        Serial ROM offset address.
    :type offset_address: unsigned int

    :param data:
        Serial ROM value to write.
    :type data: u8

.. _`pch_phub_read_serial_rom_val`:

pch_phub_read_serial_rom_val
============================

.. c:function:: void pch_phub_read_serial_rom_val(struct pch_phub_reg *chip, unsigned int offset_address, u8 *data)

    Read Serial ROM value

    :param chip:
        *undescribed*
    :type chip: struct pch_phub_reg \*

    :param offset_address:
        Serial ROM address offset value.
    :type offset_address: unsigned int

    :param data:
        Serial ROM value to read.
    :type data: u8 \*

.. _`pch_phub_write_serial_rom_val`:

pch_phub_write_serial_rom_val
=============================

.. c:function:: int pch_phub_write_serial_rom_val(struct pch_phub_reg *chip, unsigned int offset_address, u8 data)

    writing Serial ROM value

    :param chip:
        *undescribed*
    :type chip: struct pch_phub_reg \*

    :param offset_address:
        Serial ROM address offset value.
    :type offset_address: unsigned int

    :param data:
        Serial ROM value.
    :type data: u8

.. _`pch_phub_read_gbe_mac_addr`:

pch_phub_read_gbe_mac_addr
==========================

.. c:function:: void pch_phub_read_gbe_mac_addr(struct pch_phub_reg *chip, u8 *data)

    Read Gigabit Ethernet MAC address

    :param chip:
        *undescribed*
    :type chip: struct pch_phub_reg \*

    :param data:
        Buffer of the Gigabit Ethernet MAC address value.
    :type data: u8 \*

.. _`pch_phub_write_gbe_mac_addr`:

pch_phub_write_gbe_mac_addr
===========================

.. c:function:: int pch_phub_write_gbe_mac_addr(struct pch_phub_reg *chip, u8 *data)

    Write MAC address

    :param chip:
        *undescribed*
    :type chip: struct pch_phub_reg \*

    :param data:
        Gigabit Ethernet MAC address value.
    :type data: u8 \*

.. This file was automatic generated / don't edit.


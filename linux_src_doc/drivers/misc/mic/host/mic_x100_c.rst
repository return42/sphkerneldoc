.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mic/host/mic_x100.c

.. _`mic_x100_write_spad`:

mic_x100_write_spad
===================

.. c:function:: void mic_x100_write_spad(struct mic_device *mdev, unsigned int idx, u32 val)

    write to the scratchpad register

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

    :param idx:
        index to the scratchpad register, 0 based
    :type idx: unsigned int

    :param val:
        the data value to put into the register
    :type val: u32

.. _`mic_x100_write_spad.description`:

Description
-----------

This function allows writing of a 32bit value to the indexed scratchpad
register.

.. _`mic_x100_write_spad.return`:

Return
------

none.

.. _`mic_x100_read_spad`:

mic_x100_read_spad
==================

.. c:function:: u32 mic_x100_read_spad(struct mic_device *mdev, unsigned int idx)

    read from the scratchpad register

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

    :param idx:
        index to scratchpad register, 0 based
    :type idx: unsigned int

.. _`mic_x100_read_spad.description`:

Description
-----------

This function allows reading of the 32bit scratchpad register.

.. _`mic_x100_read_spad.return`:

Return
------

An appropriate -ERRNO error value on error, or zero for success.

.. _`mic_x100_enable_interrupts`:

mic_x100_enable_interrupts
==========================

.. c:function:: void mic_x100_enable_interrupts(struct mic_device *mdev)

    Enable interrupts.

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

.. _`mic_x100_disable_interrupts`:

mic_x100_disable_interrupts
===========================

.. c:function:: void mic_x100_disable_interrupts(struct mic_device *mdev)

    Disable interrupts.

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

.. _`mic_x100_send_sbox_intr`:

mic_x100_send_sbox_intr
=======================

.. c:function:: void mic_x100_send_sbox_intr(struct mic_device *mdev, int doorbell)

    Send an MIC_X100_SBOX interrupt to MIC.

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

    :param doorbell:
        *undescribed*
    :type doorbell: int

.. _`mic_x100_send_rdmasr_intr`:

mic_x100_send_rdmasr_intr
=========================

.. c:function:: void mic_x100_send_rdmasr_intr(struct mic_device *mdev, int doorbell)

    Send an RDMASR interrupt to MIC.

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

    :param doorbell:
        *undescribed*
    :type doorbell: int

.. _`mic_x100_send_intr`:

mic_x100_send_intr
==================

.. c:function:: void mic_x100_send_intr(struct mic_device *mdev, int doorbell)

    Send interrupt to MIC.

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

    :param doorbell:
        doorbell number.
    :type doorbell: int

.. _`mic_x100_ack_interrupt`:

mic_x100_ack_interrupt
======================

.. c:function:: u32 mic_x100_ack_interrupt(struct mic_device *mdev)

    Read the interrupt sources register and clear it. This function will be called in the MSI/INTx case.

    :param mdev:
        Pointer to mic_device instance.
    :type mdev: struct mic_device \*

.. _`mic_x100_ack_interrupt.return`:

Return
------

bitmask of interrupt sources triggered.

.. _`mic_x100_intr_workarounds`:

mic_x100_intr_workarounds
=========================

.. c:function:: void mic_x100_intr_workarounds(struct mic_device *mdev)

    These hardware specific workarounds are to be invoked everytime an interrupt is handled.

    :param mdev:
        Pointer to mic_device instance.
    :type mdev: struct mic_device \*

.. _`mic_x100_intr_workarounds.return`:

Return
------

none

.. _`mic_x100_hw_intr_init`:

mic_x100_hw_intr_init
=====================

.. c:function:: void mic_x100_hw_intr_init(struct mic_device *mdev)

    Initialize h/w specific interrupt information.

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

.. _`mic_x100_read_msi_to_src_map`:

mic_x100_read_msi_to_src_map
============================

.. c:function:: u32 mic_x100_read_msi_to_src_map(struct mic_device *mdev, int idx)

    read from the MSI mapping registers

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

    :param idx:
        index to the mapping register, 0 based
    :type idx: int

.. _`mic_x100_read_msi_to_src_map.description`:

Description
-----------

This function allows reading of the 32bit MSI mapping register.

.. _`mic_x100_read_msi_to_src_map.return`:

Return
------

The value in the register.

.. _`mic_x100_program_msi_to_src_map`:

mic_x100_program_msi_to_src_map
===============================

.. c:function:: void mic_x100_program_msi_to_src_map(struct mic_device *mdev, int idx, int offset, bool set)

    program the MSI mapping registers

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

    :param idx:
        index to the mapping register, 0 based
    :type idx: int

    :param offset:
        The bit offset in the register that needs to be updated.
    :type offset: int

    :param set:
        boolean specifying if the bit in the specified offset needs
        to be set or cleared.
    :type set: bool

.. _`mic_x100_program_msi_to_src_map.return`:

Return
------

None.

.. _`mic_x100_get_apic_id`:

mic_x100_get_apic_id
====================

.. c:function:: u32 mic_x100_get_apic_id(struct mic_device *mdev)

    Get bootstrap APIC ID.

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

.. _`mic_x100_send_firmware_intr`:

mic_x100_send_firmware_intr
===========================

.. c:function:: void mic_x100_send_firmware_intr(struct mic_device *mdev)

    Send an interrupt to the firmware on MIC.

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

.. _`mic_x100_hw_reset`:

mic_x100_hw_reset
=================

.. c:function:: void mic_x100_hw_reset(struct mic_device *mdev)

    Reset the MIC device.

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

.. _`mic_x100_load_command_line`:

mic_x100_load_command_line
==========================

.. c:function:: int mic_x100_load_command_line(struct mic_device *mdev, const struct firmware *fw)

    Load command line to MIC.

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

    :param fw:
        the firmware image
    :type fw: const struct firmware \*

.. _`mic_x100_load_command_line.return`:

Return
------

An appropriate -ERRNO error value on error, or zero for success.

.. _`mic_x100_load_ramdisk`:

mic_x100_load_ramdisk
=====================

.. c:function:: int mic_x100_load_ramdisk(struct mic_device *mdev)

    Load ramdisk to MIC.

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

.. _`mic_x100_load_ramdisk.return`:

Return
------

An appropriate -ERRNO error value on error, or zero for success.

.. _`mic_x100_get_boot_addr`:

mic_x100_get_boot_addr
======================

.. c:function:: int mic_x100_get_boot_addr(struct mic_device *mdev)

    Get MIC boot address.

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

.. _`mic_x100_get_boot_addr.description`:

Description
-----------

This function is called during firmware load to determine
the address at which the OS should be downloaded in card
memory i.e. GDDR.

.. _`mic_x100_get_boot_addr.return`:

Return
------

An appropriate -ERRNO error value on error, or zero for success.

.. _`mic_x100_load_firmware`:

mic_x100_load_firmware
======================

.. c:function:: int mic_x100_load_firmware(struct mic_device *mdev, const char *buf)

    Load firmware to MIC.

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

    :param buf:
        buffer containing boot string including firmware/ramdisk path.
    :type buf: const char \*

.. _`mic_x100_load_firmware.return`:

Return
------

An appropriate -ERRNO error value on error, or zero for success.

.. _`mic_x100_get_postcode`:

mic_x100_get_postcode
=====================

.. c:function:: u32 mic_x100_get_postcode(struct mic_device *mdev)

    Get postcode status from firmware.

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

.. _`mic_x100_get_postcode.return`:

Return
------

postcode.

.. _`mic_x100_smpt_set`:

mic_x100_smpt_set
=================

.. c:function:: void mic_x100_smpt_set(struct mic_device *mdev, dma_addr_t dma_addr, u8 index)

    Update an SMPT entry with a DMA address.

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

    :param dma_addr:
        *undescribed*
    :type dma_addr: dma_addr_t

    :param index:
        *undescribed*
    :type index: u8

.. _`mic_x100_smpt_set.return`:

Return
------

none.

.. _`mic_x100_smpt_hw_init`:

mic_x100_smpt_hw_init
=====================

.. c:function:: void mic_x100_smpt_hw_init(struct mic_device *mdev)

    Initialize SMPT X100 specific fields.

    :param mdev:
        pointer to mic_device instance
    :type mdev: struct mic_device \*

.. _`mic_x100_smpt_hw_init.return`:

Return
------

none.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/busses/i2c-ismt.c

.. _`__ismt_desc_dump`:

\__ismt_desc_dump
=================

.. c:function:: void __ismt_desc_dump(struct device *dev, const struct ismt_desc *desc)

    dump the contents of a specific descriptor

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param desc:
        *undescribed*
    :type desc: const struct ismt_desc \*

.. _`ismt_desc_dump`:

ismt_desc_dump
==============

.. c:function:: void ismt_desc_dump(struct ismt_priv *priv)

    dump the contents of a descriptor for debug purposes

    :param priv:
        iSMT private data
    :type priv: struct ismt_priv \*

.. _`ismt_gen_reg_dump`:

ismt_gen_reg_dump
=================

.. c:function:: void ismt_gen_reg_dump(struct ismt_priv *priv)

    dump the iSMT General Registers

    :param priv:
        iSMT private data
    :type priv: struct ismt_priv \*

.. _`ismt_mstr_reg_dump`:

ismt_mstr_reg_dump
==================

.. c:function:: void ismt_mstr_reg_dump(struct ismt_priv *priv)

    dump the iSMT Master Registers

    :param priv:
        iSMT private data
    :type priv: struct ismt_priv \*

.. _`ismt_submit_desc`:

ismt_submit_desc
================

.. c:function:: void ismt_submit_desc(struct ismt_priv *priv)

    add a descriptor to the ring

    :param priv:
        iSMT private data
    :type priv: struct ismt_priv \*

.. _`ismt_process_desc`:

ismt_process_desc
=================

.. c:function:: int ismt_process_desc(const struct ismt_desc *desc, union i2c_smbus_data *data, struct ismt_priv *priv, int size, char read_write)

    handle the completion of the descriptor

    :param desc:
        the iSMT hardware descriptor
    :type desc: const struct ismt_desc \*

    :param data:
        data buffer from the upper layer
    :type data: union i2c_smbus_data \*

    :param priv:
        ismt_priv struct holding our dma buffer
    :type priv: struct ismt_priv \*

    :param size:
        SMBus transaction type
    :type size: int

    :param read_write:
        flag to indicate if this is a read or write
    :type read_write: char

.. _`ismt_access`:

ismt_access
===========

.. c:function:: int ismt_access(struct i2c_adapter *adap, u16 addr, unsigned short flags, char read_write, u8 command, int size, union i2c_smbus_data *data)

    process an SMBus command

    :param adap:
        the i2c host adapter
    :type adap: struct i2c_adapter \*

    :param addr:
        address of the i2c/SMBus target
    :type addr: u16

    :param flags:
        command options
    :type flags: unsigned short

    :param read_write:
        read from or write to device
    :type read_write: char

    :param command:
        the i2c/SMBus command to issue
    :type command: u8

    :param size:
        SMBus transaction type
    :type size: int

    :param data:
        read/write data buffer
    :type data: union i2c_smbus_data \*

.. _`ismt_func`:

ismt_func
=========

.. c:function:: u32 ismt_func(struct i2c_adapter *adap)

    report which i2c commands are supported by this adapter

    :param adap:
        the i2c host adapter
    :type adap: struct i2c_adapter \*

.. _`ismt_handle_isr`:

ismt_handle_isr
===============

.. c:function:: irqreturn_t ismt_handle_isr(struct ismt_priv *priv)

    interrupt handler bottom half

    :param priv:
        iSMT private data
    :type priv: struct ismt_priv \*

.. _`ismt_do_interrupt`:

ismt_do_interrupt
=================

.. c:function:: irqreturn_t ismt_do_interrupt(int vec, void *data)

    IRQ interrupt handler

    :param vec:
        interrupt vector
    :type vec: int

    :param data:
        iSMT private data
    :type data: void \*

.. _`ismt_do_msi_interrupt`:

ismt_do_msi_interrupt
=====================

.. c:function:: irqreturn_t ismt_do_msi_interrupt(int vec, void *data)

    MSI interrupt handler

    :param vec:
        interrupt vector
    :type vec: int

    :param data:
        iSMT private data
    :type data: void \*

.. _`ismt_hw_init`:

ismt_hw_init
============

.. c:function:: void ismt_hw_init(struct ismt_priv *priv)

    initialize the iSMT hardware

    :param priv:
        iSMT private data
    :type priv: struct ismt_priv \*

.. _`ismt_dev_init`:

ismt_dev_init
=============

.. c:function:: int ismt_dev_init(struct ismt_priv *priv)

    initialize the iSMT data structures

    :param priv:
        iSMT private data
    :type priv: struct ismt_priv \*

.. _`ismt_int_init`:

ismt_int_init
=============

.. c:function:: int ismt_int_init(struct ismt_priv *priv)

    initialize interrupts

    :param priv:
        iSMT private data
    :type priv: struct ismt_priv \*

.. _`ismt_probe`:

ismt_probe
==========

.. c:function:: int ismt_probe(struct pci_dev *pdev, const struct pci_device_id *id)

    probe for iSMT devices

    :param pdev:
        PCI-Express device
    :type pdev: struct pci_dev \*

    :param id:
        PCI-Express device ID
    :type id: const struct pci_device_id \*

.. _`ismt_remove`:

ismt_remove
===========

.. c:function:: void ismt_remove(struct pci_dev *pdev)

    release driver resources

    :param pdev:
        PCI-Express device
    :type pdev: struct pci_dev \*

.. This file was automatic generated / don't edit.


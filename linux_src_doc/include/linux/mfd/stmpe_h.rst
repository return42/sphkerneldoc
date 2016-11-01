.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mfd/stmpe.h

.. _`stmpe`:

struct stmpe
============

.. c:type:: struct stmpe

    STMPE MFD structure

.. _`stmpe.definition`:

Definition
----------

.. code-block:: c

    struct stmpe {
        struct regulator *vcc;
        struct regulator *vio;
        struct mutex lock;
        struct mutex irq_lock;
        struct device *dev;
        struct irq_domain *domain;
        void *client;
        struct stmpe_client_info *ci;
        enum stmpe_partnum partnum;
        struct stmpe_variant_info *variant;
        const u8 *regs;
        int irq;
        int num_gpios;
        u8 ier[2];
        u8 oldier[2];
        struct stmpe_platform_data *pdata;
    }

.. _`stmpe.members`:

Members
-------

vcc
    optional VCC regulator

vio
    optional VIO regulator

lock
    lock protecting I/O operations

irq_lock
    IRQ bus lock

dev
    device, mostly for \ :c:func:`dev_dbg`\ 

domain
    *undescribed*

client
    client - i2c or spi

ci
    client specific information

partnum
    part number

variant
    the detected STMPE model number

regs
    list of addresses of registers which are at different addresses on
    different variants.  Indexed by one of STMPE_IDX\_\*.

irq
    irq number for stmpe

num_gpios
    number of gpios, differs for variants

ier
    cache of IER registers for bus_lock

oldier
    cache of IER registers for bus_lock

pdata
    platform data

.. This file was automatic generated / don't edit.


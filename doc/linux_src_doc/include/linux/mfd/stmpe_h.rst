.. -*- coding: utf-8; mode: rst -*-

=======
stmpe.h
=======


.. _`stmpe`:

struct stmpe
============

.. c:type:: stmpe

    STMPE MFD structure


.. _`stmpe.definition`:

Definition
----------

.. code-block:: c

  struct stmpe {
    struct regulator * vcc;
    struct regulator * vio;
    struct mutex lock;
    struct mutex irq_lock;
    struct device * dev;
    void * client;
    struct stmpe_client_info * ci;
    enum stmpe_partnum partnum;
    struct stmpe_variant_info * variant;
    const u8 * regs;
    int irq;
    int num_gpios;
    u8 ier[2];
    u8 oldier[2];
    struct stmpe_platform_data * pdata;
  };


.. _`stmpe.members`:

Members
-------

:``vcc``:
    optional VCC regulator

:``vio``:
    optional VIO regulator

:``lock``:
    lock protecting I/O operations

:``irq_lock``:
    IRQ bus lock

:``dev``:
    device, mostly for :c:func:`dev_dbg`

:``client``:
    client - i2c or spi

:``ci``:
    client specific information

:``partnum``:
    part number

:``variant``:
    the detected STMPE model number

:``regs``:
    list of addresses of registers which are at different addresses on
    different variants.  Indexed by one of STMPE_IDX\_\*.

:``irq``:
    irq number for stmpe

:``num_gpios``:
    number of gpios, differs for variants

:``ier[2]``:
    cache of IER registers for bus_lock

:``oldier[2]``:
    cache of IER registers for bus_lock

:``pdata``:
    platform data




.. _`stmpe_platform_data`:

struct stmpe_platform_data
==========================

.. c:type:: stmpe_platform_data

    STMPE platform data


.. _`stmpe_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct stmpe_platform_data {
    int id;
    unsigned int blocks;
    unsigned int irq_trigger;
    bool autosleep;
    bool irq_over_gpio;
    int irq_gpio;
    int autosleep_timeout;
  };


.. _`stmpe_platform_data.members`:

Members
-------

:``id``:
    device id to distinguish between multiple STMPEs on the same board

:``blocks``:
    bitmask of blocks to enable (use STMPE_BLOCK\_\*)

:``irq_trigger``:
    IRQ trigger to use for the interrupt to the host

:``autosleep``:
    bool to enable/disable stmpe autosleep

:``irq_over_gpio``:
    true if gpio is used to get irq

:``irq_gpio``:
    gpio number over which irq will be requested (significant only if
    irq_over_gpio is true)

:``autosleep_timeout``:
    inactivity timeout in milliseconds for autosleep



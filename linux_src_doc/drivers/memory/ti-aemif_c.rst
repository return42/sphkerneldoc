.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/memory/ti-aemif.c

.. _`aemif_cs_data`:

struct aemif_cs_data
====================

.. c:type:: struct aemif_cs_data

    structure to hold cs parameters

.. _`aemif_cs_data.definition`:

Definition
----------

.. code-block:: c

    struct aemif_cs_data {
        u8 cs;
        u16 wstrobe;
        u16 rstrobe;
        u8 wsetup;
        u8 whold;
        u8 rsetup;
        u8 rhold;
        u8 ta;
        u8 enable_ss;
        u8 enable_ew;
        u8 asize;
    }

.. _`aemif_cs_data.members`:

Members
-------

cs
    chip-select number

wstrobe
    write strobe width, ns

rstrobe
    read strobe width, ns

wsetup
    write setup width, ns

whold
    write hold width, ns

rsetup
    read setup width, ns

rhold
    read hold width, ns

ta
    minimum turn around time, ns

enable_ss
    enable/disable select strobe mode

enable_ew
    enable/disable extended wait mode

asize
    width of the asynchronous device's data bus

.. _`aemif_device`:

struct aemif_device
===================

.. c:type:: struct aemif_device

    structure to hold device data

.. _`aemif_device.definition`:

Definition
----------

.. code-block:: c

    struct aemif_device {
        void __iomem *base;
        struct clk *clk;
        unsigned long clk_rate;
        u8 num_cs;
        int cs_offset;
        struct aemif_cs_data cs_data[NUM_CS];
    }

.. _`aemif_device.members`:

Members
-------

base
    base address of AEMIF registers

clk
    source clock

clk_rate
    clock's rate in kHz

num_cs
    number of assigned chip-selects

cs_offset
    start number of cs nodes

cs_data
    array of chip-select settings

.. _`aemif_calc_rate`:

aemif_calc_rate
===============

.. c:function:: int aemif_calc_rate(struct platform_device *pdev, int wanted, unsigned long clk, int max)

    calculate timing data.

    :param struct platform_device \*pdev:
        platform device to calculate for

    :param int wanted:
        The cycle time needed in nanoseconds.

    :param unsigned long clk:
        The input clock rate in kHz.

    :param int max:
        The maximum divider value that can be programmed.

.. _`aemif_calc_rate.description`:

Description
-----------

On success, returns the calculated timing value minus 1 for easy
programming into AEMIF timing registers, else negative errno.

.. _`aemif_config_abus`:

aemif_config_abus
=================

.. c:function:: int aemif_config_abus(struct platform_device *pdev, int csnum)

    configure async bus parameters

    :param struct platform_device \*pdev:
        platform device to configure for

    :param int csnum:
        aemif chip select number

.. _`aemif_config_abus.description`:

Description
-----------

This function programs the given timing values (in real clock) into the
AEMIF registers taking the AEMIF clock into account.

This function does not use any locking while programming the AEMIF
because it is expected that there is only one user of a given
chip-select.

Returns 0 on success, else negative errno.

.. _`aemif_get_hw_params`:

aemif_get_hw_params
===================

.. c:function:: void aemif_get_hw_params(struct platform_device *pdev, int csnum)

    function to read hw register values

    :param struct platform_device \*pdev:
        platform device to read for

    :param int csnum:
        aemif chip select number

.. _`aemif_get_hw_params.description`:

Description
-----------

This function reads the defaults from the registers and update
the timing values. Required for get/set commands and also for
the case when driver needs to use defaults in hardware.

.. _`of_aemif_parse_abus_config`:

of_aemif_parse_abus_config
==========================

.. c:function:: int of_aemif_parse_abus_config(struct platform_device *pdev, struct device_node *np)

    parse CS configuration from DT

    :param struct platform_device \*pdev:
        platform device to parse for

    :param struct device_node \*np:
        device node ptr

.. _`of_aemif_parse_abus_config.description`:

Description
-----------

This function update the emif async bus configuration based on the values
configured in a cs device binding node.

.. This file was automatic generated / don't edit.


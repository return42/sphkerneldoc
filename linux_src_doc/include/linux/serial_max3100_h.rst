.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/serial_max3100.h

.. _`plat_max3100`:

struct plat_max3100
===================

.. c:type:: struct plat_max3100

    MAX3100 SPI UART platform data

.. _`plat_max3100.definition`:

Definition
----------

.. code-block:: c

    struct plat_max3100 {
        int loopback;
        int crystal;
        void (*max3100_hw_suspend)(int suspend);
        int poll_time;
    }

.. _`plat_max3100.members`:

Members
-------

loopback
    force MAX3100 in loopback

crystal
    1 for 3.6864 Mhz, 0 for 1.8432

max3100_hw_suspend
    MAX3100 has a shutdown pin. This is a hook
    called on suspend and resume to activate it.

poll_time
    poll time for CTS signal in ms, 0 disables (so no hw
    flow ctrl is possible but you have less CPU usage)

.. _`plat_max3100.description`:

Description
-----------

You should use this structure in your machine description to specify
how the MAX3100 is connected. Example:

static struct plat_max3100 max3100_plat_data = {
.loopback = 0,
.crystal = 0,
.poll_time = 100,
};

static struct spi_board_info spi_board_info[] = {
{
.modalias   = "max3100",
.platform_data      = \ :c:type:`struct max3100_plat_data <max3100_plat_data>`\ ,
.irq                = IRQ_EINT12,
.max_speed_hz       = 5\*1000\*1000,
.chip_select        = 0,
},
};

.. This file was automatic generated / don't edit.


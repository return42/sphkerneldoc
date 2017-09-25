.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/sfc/falcon/nic.h

.. _`falcon_board_type`:

struct falcon_board_type
========================

.. c:type:: struct falcon_board_type

    board operations and type information

.. _`falcon_board_type.definition`:

Definition
----------

.. code-block:: c

    struct falcon_board_type {
        u8 id;
        int (*init) (struct ef4_nic *nic);
        void (*init_phy) (struct ef4_nic *efx);
        void (*fini) (struct ef4_nic *nic);
        void (*set_id_led) (struct ef4_nic *efx, enum ef4_led_mode mode);
        int (*monitor) (struct ef4_nic *nic);
    }

.. _`falcon_board_type.members`:

Members
-------

id
    Board type id, as found in NVRAM

init
    Allocate resources and initialise peripheral hardware

init_phy
    Do board-specific PHY initialisation

fini
    Shut down hardware and free resources

set_id_led
    Set state of identifying LED or revert to automatic function

monitor
    Board-specific health check function

.. _`falcon_board`:

struct falcon_board
===================

.. c:type:: struct falcon_board

    board information

.. _`falcon_board.definition`:

Definition
----------

.. code-block:: c

    struct falcon_board {
        const struct falcon_board_type *type;
        int major;
        int minor;
        struct i2c_adapter i2c_adap;
        struct i2c_algo_bit_data i2c_data;
        struct i2c_client *hwmon_client, *ioexp_client;
    }

.. _`falcon_board.members`:

Members
-------

type
    Type of board

major
    Major rev. ('A', 'B' ...)

minor
    Minor rev. (0, 1, ...)

i2c_adap
    I2C adapter for on-board peripherals

i2c_data
    Data for bit-banging algorithm

hwmon_client
    I2C client for hardware monitor

ioexp_client
    I2C client for power/port control

.. _`falcon_spi_device`:

struct falcon_spi_device
========================

.. c:type:: struct falcon_spi_device

    a Falcon SPI (Serial Peripheral Interface) device

.. _`falcon_spi_device.definition`:

Definition
----------

.. code-block:: c

    struct falcon_spi_device {
        int device_id;
        unsigned int size;
        unsigned int addr_len;
        unsigned int munge_address:1;
        u8 erase_command;
        unsigned int erase_size;
        unsigned int block_size;
    }

.. _`falcon_spi_device.members`:

Members
-------

device_id
    Controller's id for the device

size
    Size (in bytes)

addr_len
    Number of address bytes in read/write commands

munge_address
    Flag whether addresses should be munged.
    Some devices with 9-bit addresses (e.g. AT25040A EEPROM)
    use bit 3 of the command byte as address bit A8, rather
    than having a two-byte address.  If this flag is set, then
    commands should be munged in this way.

erase_command
    Erase command (or 0 if sector erase not needed).

erase_size
    Erase sector size (in bytes)
    Erase commands affect sectors with this size and alignment.
    This must be a power of two.

block_size
    Write block size (in bytes).
    Write commands are limited to blocks with this size and alignment.

.. _`falcon_nic_data`:

struct falcon_nic_data
======================

.. c:type:: struct falcon_nic_data

    Falcon NIC state

.. _`falcon_nic_data.definition`:

Definition
----------

.. code-block:: c

    struct falcon_nic_data {
        struct pci_dev *pci_dev2;
        struct falcon_board board;
        u64 stats[FALCON_STAT_COUNT];
        unsigned int stats_disable_count;
        bool stats_pending;
        struct timer_list stats_timer;
        struct falcon_spi_device spi_flash;
        struct falcon_spi_device spi_eeprom;
        struct mutex spi_lock;
        struct mutex mdio_lock;
        bool xmac_poll_required;
    }

.. _`falcon_nic_data.members`:

Members
-------

pci_dev2
    Secondary function of Falcon A

board
    Board state and functions

stats
    Hardware statistics

stats_disable_count
    Nest count for disabling statistics fetches

stats_pending
    Is there a pending DMA of MAC statistics.

stats_timer
    A timer for regularly fetching MAC statistics.

spi_flash
    SPI flash device

spi_eeprom
    SPI EEPROM device

spi_lock
    SPI bus lock

mdio_lock
    MDIO bus lock

xmac_poll_required
    XMAC link state needs polling

.. This file was automatic generated / don't edit.


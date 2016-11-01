.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/sfc/nic.h

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
        int (*init)(struct efx_nic *nic);
        void (*init_phy)(struct efx_nic *efx);
        void (*fini)(struct efx_nic *nic);
        void (*set_id_led)(struct efx_nic *efx, enum efx_led_mode mode);
        int (*monitor)(struct efx_nic *nic);
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
        struct i2c_client *hwmon_client;
        struct i2c_client * *ioexp_client;
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

.. _`siena_nic_data`:

struct siena_nic_data
=====================

.. c:type:: struct siena_nic_data

    Siena NIC state

.. _`siena_nic_data.definition`:

Definition
----------

.. code-block:: c

    struct siena_nic_data {
        struct efx_nic *efx;
        int wol_filter_id;
        u64 stats[SIENA_STAT_COUNT];
    #ifdef CONFIG_SFC_SRIOV
        struct siena_vf *vf;
        struct efx_channel *vfdi_channel;
        unsigned vf_buftbl_base;
        struct efx_buffer vfdi_status;
        struct list_head local_addr_list;
        struct list_head local_page_list;
        struct mutex local_lock;
        struct work_struct peer_work;
    #endif
    }

.. _`siena_nic_data.members`:

Members
-------

efx
    Pointer back to main interface structure

wol_filter_id
    Wake-on-LAN packet filter id

stats
    Hardware statistics

vf
    Array of \ :c:type:`struct siena_vf <siena_vf>`\  objects

vfdi_channel
    *undescribed*

vf_buftbl_base
    The zeroth buffer table index used to back VF queues.

vfdi_status
    Common VFDI status page to be dmad to VF address space.

local_addr_list
    List of local addresses. Protected by \ ``local_lock``\ .

local_page_list
    List of DMA addressable pages used to broadcast
    \ ``local_addr_list``\ . Protected by \ ``local_lock``\ .

local_lock
    Mutex protecting \ ``local_addr_list``\  and \ ``local_page_list``\ .

peer_work
    Work item to broadcast peer addresses to VMs.

.. _`efx_ef10_nic_data`:

struct efx_ef10_nic_data
========================

.. c:type:: struct efx_ef10_nic_data

    EF10 architecture NIC state

.. _`efx_ef10_nic_data.definition`:

Definition
----------

.. code-block:: c

    struct efx_ef10_nic_data {
        struct efx_buffer mcdi_buf;
        u16 warm_boot_count;
        unsigned int vi_base;
        unsigned int n_allocated_vis;
        bool must_realloc_vis;
        bool must_restore_filters;
        unsigned int n_piobufs;
        void __iomem *wc_membase;
        void __iomem * *pio_write_base;
        unsigned int pio_write_vi_base;
        unsigned int piobuf_handle[EF10_TX_PIOBUF_COUNT];
        bool must_restore_piobufs;
        u32 rx_rss_context;
        bool rx_rss_context_exclusive;
        u64 stats[EF10_STAT_COUNT];
        bool workaround_35388;
        bool workaround_26807;
        bool workaround_61265;
        bool must_check_datapath_caps;
        u32 datapath_caps;
        u32 datapath_caps2;
        unsigned int rx_dpcpu_fw_id;
        unsigned int tx_dpcpu_fw_id;
        unsigned int vport_id;
        bool must_probe_vswitching;
        unsigned int pf_index;
        u8 port_id[ETH_ALEN];
    #ifdef CONFIG_SFC_SRIOV
        unsigned int vf_index;
        struct ef10_vf *vf;
    #endif
        u8 vport_mac[ETH_ALEN];
        struct list_head vlan_list;
        struct mutex vlan_lock;
    }

.. _`efx_ef10_nic_data.members`:

Members
-------

mcdi_buf
    DMA buffer for MCDI

warm_boot_count
    Last seen MC warm boot count

vi_base
    Absolute index of first VI in this function

n_allocated_vis
    Number of VIs allocated to this function

must_realloc_vis
    Flag: VIs have yet to be reallocated after MC reboot

must_restore_filters
    Flag: filters have yet to be restored after MC reboot

n_piobufs
    Number of PIO buffers allocated to this function

wc_membase
    Base address of write-combining mapping of the memory BAR

pio_write_base
    Base address for writing PIO buffers

pio_write_vi_base
    Relative VI number for \ ``pio_write_base``\ 

piobuf_handle
    Handle of each PIO buffer allocated

must_restore_piobufs
    Flag: PIO buffers have yet to be restored after MC
    reboot

rx_rss_context
    Firmware handle for our RSS context

rx_rss_context_exclusive
    Whether our RSS context is exclusive or shared

stats
    Hardware statistics

workaround_35388
    Flag: firmware supports workaround for bug 35388

workaround_26807
    Flag: firmware supports workaround for bug 26807

workaround_61265
    Flag: firmware supports workaround for bug 61265

must_check_datapath_caps
    Flag: \ ``datapath_caps``\  needs to be revalidated
    after MC reboot

datapath_caps
    Capabilities of datapath firmware (FLAGS1 field of
    \ ``MC_CMD_GET_CAPABILITIES``\  response)

datapath_caps2
    Further Capabilities of datapath firmware (FLAGS2 field of
    \ ``MC_CMD_GET_CAPABILITIES``\  response)

rx_dpcpu_fw_id
    Firmware ID of the RxDPCPU

tx_dpcpu_fw_id
    Firmware ID of the TxDPCPU

vport_id
    The function's vport ID, only relevant for PFs

must_probe_vswitching
    Flag: vswitching has yet to be setup after MC reboot

pf_index
    The number for this PF, or the parent PF if this is a VF

vf_index
    *undescribed*

vf
    Pointer to VF data structure

vport_mac
    The MAC address on the vport, only for PFs; VFs will be zero

vlan_list
    List of VLANs added over the interface. Serialised by vlan_lock.

vlan_lock
    Lock to serialize access to vlan_list.

.. This file was automatic generated / don't edit.


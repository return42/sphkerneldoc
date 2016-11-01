.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/neterion/vxge/vxge-config.h

.. _`vxge_assert`:

vxge_assert
===========

.. c:function::  vxge_assert( test)

    :param  test:
        C-condition to check

.. _`vxge_assert.description`:

Description
-----------

This function implements traditional assert. By default assertions
are enabled. It can be disabled by undefining VXGE_DEBUG_ASSERT macro in
compilation
time.

.. _`vxge_debug_level`:

enum vxge_debug_level
=====================

.. c:type:: enum vxge_debug_level


.. _`vxge_debug_level.definition`:

Definition
----------

.. code-block:: c

    enum vxge_debug_level {
        VXGE_NONE,
        VXGE_TRACE,
        VXGE_ERR
    };

.. _`vxge_debug_level.constants`:

Constants
---------

VXGE_NONE
    debug disabled

VXGE_TRACE
    all errors plus all kind of verbose tracing print outs
    going to be logged out. Very noisy.

VXGE_ERR
    all errors going to be logged out

.. _`vxge_debug_level.description`:

Description
-----------

This enumeration going to be used to switch between different
debug levels during runtime if DEBUG macro defined during
compilation. If DEBUG macro not defined than code will be
compiled out.

.. _`vxge_hw_device_link_state`:

enum vxge_hw_device_link_state
==============================

.. c:type:: enum vxge_hw_device_link_state

    Link state enumeration.

.. _`vxge_hw_device_link_state.definition`:

Definition
----------

.. code-block:: c

    enum vxge_hw_device_link_state {
        VXGE_HW_LINK_NONE,
        VXGE_HW_LINK_DOWN,
        VXGE_HW_LINK_UP
    };

.. _`vxge_hw_device_link_state.constants`:

Constants
---------

VXGE_HW_LINK_NONE
    Invalid link state.

VXGE_HW_LINK_DOWN
    Link is down.

VXGE_HW_LINK_UP
    Link is up.

.. _`vxge_hw_fw_upgrade_code`:

enum vxge_hw_fw_upgrade_code
============================

.. c:type:: enum vxge_hw_fw_upgrade_code

    FW upgrade return codes.

.. _`vxge_hw_fw_upgrade_code.definition`:

Definition
----------

.. code-block:: c

    enum vxge_hw_fw_upgrade_code {
        VXGE_HW_FW_UPGRADE_OK,
        VXGE_HW_FW_UPGRADE_DONE,
        VXGE_HW_FW_UPGRADE_ERR,
        VXGE_FW_UPGRADE_BYTES2SKIP
    };

.. _`vxge_hw_fw_upgrade_code.constants`:

Constants
---------

VXGE_HW_FW_UPGRADE_OK
    All OK send next 16 bytes

VXGE_HW_FW_UPGRADE_DONE
    upload completed

VXGE_HW_FW_UPGRADE_ERR
    upload error

VXGE_FW_UPGRADE_BYTES2SKIP
    skip bytes in the stream

.. _`vxge_hw_fw_upgrade_err_code`:

enum vxge_hw_fw_upgrade_err_code
================================

.. c:type:: enum vxge_hw_fw_upgrade_err_code

    FW upgrade error codes.

.. _`vxge_hw_fw_upgrade_err_code.definition`:

Definition
----------

.. code-block:: c

    enum vxge_hw_fw_upgrade_err_code {
        VXGE_HW_FW_UPGRADE_ERR_CORRUPT_DATA_1,
        VXGE_HW_FW_UPGRADE_ERR_BUFFER_OVERFLOW,
        VXGE_HW_FW_UPGRADE_ERR_INV_NCF_FILE_3,
        VXGE_HW_FW_UPGRADE_ERR_INV_NCF_FILE_4,
        VXGE_HW_FW_UPGRADE_ERR_INV_NCF_FILE_5,
        VXGE_HW_FW_UPGRADE_ERR_INV_NCF_FILE_6,
        VXGE_HW_FW_UPGRADE_ERR_CORRUPT_DATA_7,
        VXGE_HW_FW_UPGRADE_ERR_INV_NCF_FILE_8,
        VXGE_HW_FW_UPGRADE_ERR_GENERIC_ERROR_UNKNOWN,
        VXGE_HW_FW_UPGRADE_ERR_FAILED_TO_FLASH
    };

.. _`vxge_hw_fw_upgrade_err_code.constants`:

Constants
---------

VXGE_HW_FW_UPGRADE_ERR_CORRUPT_DATA_1
    corrupt data

VXGE_HW_FW_UPGRADE_ERR_BUFFER_OVERFLOW
    buffer overflow

VXGE_HW_FW_UPGRADE_ERR_INV_NCF_FILE_3
    invalid .ncf file

VXGE_HW_FW_UPGRADE_ERR_INV_NCF_FILE_4
    invalid .ncf file

VXGE_HW_FW_UPGRADE_ERR_INV_NCF_FILE_5
    invalid .ncf file

VXGE_HW_FW_UPGRADE_ERR_INV_NCF_FILE_6
    invalid .ncf file

VXGE_HW_FW_UPGRADE_ERR_CORRUPT_DATA_7
    corrupt data

VXGE_HW_FW_UPGRADE_ERR_INV_NCF_FILE_8
    invalid .ncf file

VXGE_HW_FW_UPGRADE_ERR_GENERIC_ERROR_UNKNOWN
    generic error unknown type

VXGE_HW_FW_UPGRADE_ERR_FAILED_TO_FLASH
    failed to flash image check failed

.. _`vxge_hw_fifo_config`:

struct vxge_hw_fifo_config
==========================

.. c:type:: struct vxge_hw_fifo_config

    Configuration of fifo.

.. _`vxge_hw_fifo_config.definition`:

Definition
----------

.. code-block:: c

    struct vxge_hw_fifo_config {
        u32 enable;
    #define VXGE_HW_FIFO_ENABLE 1
    #define VXGE_HW_FIFO_DISABLE 0
        u32 fifo_blocks;
    #define VXGE_HW_MIN_FIFO_BLOCKS 2
    #define VXGE_HW_MAX_FIFO_BLOCKS 128
        u32 max_frags;
    #define VXGE_HW_MIN_FIFO_FRAGS 1
    #define VXGE_HW_MAX_FIFO_FRAGS 256
        u32 memblock_size;
    #define VXGE_HW_MIN_FIFO_MEMBLOCK_SIZE VXGE_HW_BLOCK_SIZE
    #define VXGE_HW_MAX_FIFO_MEMBLOCK_SIZE 131072
    #define VXGE_HW_DEF_FIFO_MEMBLOCK_SIZE 8096
        u32 alignment_size;
    #define VXGE_HW_MIN_FIFO_ALIGNMENT_SIZE 0
    #define VXGE_HW_MAX_FIFO_ALIGNMENT_SIZE 65536
    #define VXGE_HW_DEF_FIFO_ALIGNMENT_SIZE VXGE_CACHE_LINE_SIZE
        u32 intr;
    #define VXGE_HW_FIFO_QUEUE_INTR_ENABLE 1
    #define VXGE_HW_FIFO_QUEUE_INTR_DISABLE 0
    #define VXGE_HW_FIFO_QUEUE_INTR_DEFAULT 0
        u32 no_snoop_bits;
    #define VXGE_HW_FIFO_NO_SNOOP_DISABLED 0
    #define VXGE_HW_FIFO_NO_SNOOP_TXD 1
    #define VXGE_HW_FIFO_NO_SNOOP_FRM 2
    #define VXGE_HW_FIFO_NO_SNOOP_ALL 3
    #define VXGE_HW_FIFO_NO_SNOOP_DEFAULT 0
    }

.. _`vxge_hw_fifo_config.members`:

Members
-------

enable
    Is this fifo to be commissioned

fifo_blocks
    Numbers of TxDL (that is, lists of Tx descriptors)
    blocks per queue.

max_frags
    Max number of Tx buffers per TxDL (that is, per single
    transmit operation).
    No more than 256 transmit buffers can be specified.

memblock_size
    Fifo descriptors are allocated in blocks of \ ``mem_block_size``\ 
    bytes. Setting \ ``memblock_size``\  to page size ensures
    by-page allocation of descriptors. 128K bytes is the
    maximum supported block size.

alignment_size
    per Tx fragment DMA-able memory used to align transmit data
    (e.g., to align on a cache line).

intr
    Boolean. Use 1 to generate interrupt for each completed TxDL.
    Use 0 otherwise.

no_snoop_bits
    If non-zero, specifies no-snoop PCI operation,
    which generally improves latency of the host bridge operation
    (see PCI specification). For valid values please refer
    to struct vxge_hw_fifo_config{} in the driver sources.
    Configuration of all Titan fifos.

.. _`vxge_hw_fifo_config.note`:

Note
----

Valid (min, max) range for each attribute is specified in the body of
the struct vxge_hw_fifo_config{} structure.

.. _`vxge_hw_ring_config`:

struct vxge_hw_ring_config
==========================

.. c:type:: struct vxge_hw_ring_config

    Ring configurations.

.. _`vxge_hw_ring_config.definition`:

Definition
----------

.. code-block:: c

    struct vxge_hw_ring_config {
        u32 enable;
    #define VXGE_HW_RING_ENABLE 1
    #define VXGE_HW_RING_DISABLE 0
    #define VXGE_HW_RING_DEFAULT 1
        u32 ring_blocks;
    #define VXGE_HW_MIN_RING_BLOCKS 1
    #define VXGE_HW_MAX_RING_BLOCKS 128
    #define VXGE_HW_DEF_RING_BLOCKS 2
        u32 buffer_mode;
    #define VXGE_HW_RING_RXD_BUFFER_MODE_1 1
    #define VXGE_HW_RING_RXD_BUFFER_MODE_3 3
    #define VXGE_HW_RING_RXD_BUFFER_MODE_5 5
    #define VXGE_HW_RING_RXD_BUFFER_MODE_DEFAULT 1
        u32 scatter_mode;
    #define VXGE_HW_RING_SCATTER_MODE_A 0
    #define VXGE_HW_RING_SCATTER_MODE_B 1
    #define VXGE_HW_RING_SCATTER_MODE_C 2
    #define VXGE_HW_RING_SCATTER_MODE_USE_FLASH_DEFAULT 0xffffffff
        u64 rxds_limit;
    #define VXGE_HW_DEF_RING_RXDS_LIMIT 44
    }

.. _`vxge_hw_ring_config.members`:

Members
-------

enable
    Is this ring to be commissioned

ring_blocks
    Numbers of RxD blocks in the ring

buffer_mode
    Receive buffer mode (1, 2, 3, or 5); for details please refer
    to Titan User Guide.

scatter_mode
    Titan supports two receive scatter modes: A and B.
    For details please refer to Titan User Guide.

rxds_limit
    *undescribed*

.. _`vxge_hw_vp_config`:

struct vxge_hw_vp_config
========================

.. c:type:: struct vxge_hw_vp_config

    Configuration of virtual path

.. _`vxge_hw_vp_config.definition`:

Definition
----------

.. code-block:: c

    struct vxge_hw_vp_config {
        u32 vp_id;
    #define VXGE_HW_VPATH_PRIORITY_MIN 0
    #define VXGE_HW_VPATH_PRIORITY_MAX 16
    #define VXGE_HW_VPATH_PRIORITY_DEFAULT 0
        u32 min_bandwidth;
    #define VXGE_HW_VPATH_BANDWIDTH_MIN 0
    #define VXGE_HW_VPATH_BANDWIDTH_MAX 100
    #define VXGE_HW_VPATH_BANDWIDTH_DEFAULT 0
        struct vxge_hw_ring_config ring;
        struct vxge_hw_fifo_config fifo;
        struct vxge_hw_tim_intr_config tti;
        struct vxge_hw_tim_intr_config rti;
        u32 mtu;
    #define VXGE_HW_VPATH_MIN_INITIAL_MTU VXGE_HW_MIN_MTU
    #define VXGE_HW_VPATH_MAX_INITIAL_MTU VXGE_HW_MAX_MTU
    #define VXGE_HW_VPATH_USE_FLASH_DEFAULT_INITIAL_MTU 0xffffffff
        u32 rpa_strip_vlan_tag;
    #define VXGE_HW_VPATH_RPA_STRIP_VLAN_TAG_ENABLE 1
    #define VXGE_HW_VPATH_RPA_STRIP_VLAN_TAG_DISABLE 0
    #define VXGE_HW_VPATH_RPA_STRIP_VLAN_TAG_USE_FLASH_DEFAULT 0xffffffff
    }

.. _`vxge_hw_vp_config.members`:

Members
-------

vp_id
    Virtual Path Id

min_bandwidth
    Minimum Guaranteed bandwidth

ring
    See struct vxge_hw_ring_config{}.

fifo
    See struct vxge_hw_fifo_config{}.

tti
    Configuration of interrupt associated with Transmit.
    see struct \ :c:func:`vxge_hw_tim_intr_config`\ ;

rti
    Configuration of interrupt associated with Receive.
    see struct \ :c:func:`vxge_hw_tim_intr_config`\ ;

mtu
    mtu size used on this port.

rpa_strip_vlan_tag
    Strip VLAN Tag enable/disable. Instructs the device to
    remove the VLAN tag from all received tagged frames that are not
    replicated at the internal L2 switch.
    0 - Do not strip the VLAN tag.
    1 - Strip the VLAN tag. Regardless of this setting, VLAN tags are
    always placed into the RxDMA descriptor.

.. _`vxge_hw_vp_config.description`:

Description
-----------

This structure is used by the driver to pass the configuration parameters to
configure Virtual Path.

.. _`vxge_hw_device_config`:

struct vxge_hw_device_config
============================

.. c:type:: struct vxge_hw_device_config

    Device configuration.

.. _`vxge_hw_device_config.definition`:

Definition
----------

.. code-block:: c

    struct vxge_hw_device_config {
        u32 device_poll_millis;
    #define VXGE_HW_MIN_DEVICE_POLL_MILLIS 1
    #define VXGE_HW_MAX_DEVICE_POLL_MILLIS 100000
    #define VXGE_HW_DEF_DEVICE_POLL_MILLIS 1000
        u32 dma_blockpool_initial;
        u32 dma_blockpool_max;
    #define VXGE_HW_MIN_DMA_BLOCK_POOL_SIZE 0
    #define VXGE_HW_INITIAL_DMA_BLOCK_POOL_SIZE 0
    #define VXGE_HW_INCR_DMA_BLOCK_POOL_SIZE 4
    #define VXGE_HW_MAX_DMA_BLOCK_POOL_SIZE 4096
    #define VXGE_HW_MAX_PAYLOAD_SIZE_512 2
        u32 intr_mode:2;
    #define VXGE_HW_INTR_MODE_IRQLINE 0
    #define VXGE_HW_INTR_MODE_MSIX 1
    #define VXGE_HW_INTR_MODE_MSIX_ONE_SHOT 2
    #define VXGE_HW_INTR_MODE_DEF 0
    #define VXGE_HW_RTH_DISABLE 0
    #define VXGE_HW_RTH_ENABLE 1
    #define VXGE_HW_RTH_DEFAULT 0
    #define VXGE_HW_RTH_IT_TYPE_SOLO_IT 0
    #define VXGE_HW_RTH_IT_TYPE_MULTI_IT 1
    #define VXGE_HW_RTH_IT_TYPE_DEFAULT 0
    #define VXGE_HW_RTS_MAC_DISABLE 0
    #define VXGE_HW_RTS_MAC_ENABLE 1
    #define VXGE_HW_RTS_MAC_DEFAULT 0
    #define VXGE_HW_HWTS_DISABLE 0
    #define VXGE_HW_HWTS_ENABLE 1
    #define VXGE_HW_HWTS_DEFAULT 1
        struct vxge_hw_vp_config vp_config[VXGE_HW_MAX_VIRTUAL_PATHS];
    }

.. _`vxge_hw_device_config.members`:

Members
-------

device_poll_millis
    Specify the interval (in mulliseconds)
    to wait for register reads

dma_blockpool_initial
    Initial size of DMA Pool

dma_blockpool_max
    Maximum blocks in DMA pool

intr_mode
    Line, or MSI-X interrupt.

vp_config
    Configuration for virtual paths

.. _`vxge_hw_device_config.description`:

Description
-----------

Titan configuration.
Contains per-device configuration parameters, including:
- stats sampling interval, etc.

In addition, struct vxge_hw_device_config{} includes "subordinate"
configurations, including:
- fifos and rings;
- MAC (done at firmware level).

See Titan User Guide for more details.

.. _`vxge_hw_device_config.note`:

Note
----

Valid (min, max) range for each attribute is specified in the body of
the struct vxge_hw_device_config{} structure. Please refer to the
corresponding include file.

.. _`vxge_hw_device_config.see-also`:

See also
--------

struct vxge_hw_tim_intr_config{}.

.. _`__vxge_hw_device`:

struct \__vxge_hw_device
========================

.. c:type:: struct __vxge_hw_device

    Hal device object

.. _`__vxge_hw_device.definition`:

Definition
----------

.. code-block:: c

    struct __vxge_hw_device {
        u32 magic;
    #define VXGE_HW_DEVICE_MAGIC 0x12345678
    #define VXGE_HW_DEVICE_DEAD 0xDEADDEAD
        void __iomem *bar0;
        struct pci_dev *pdev;
        struct net_device *ndev;
        struct vxge_hw_device_config config;
        enum vxge_hw_device_link_state link_state;
        const struct vxge_hw_uld_cbs *uld_callbacks;
        u32 host_type;
        u32 func_id;
        u32 access_rights;
    #define VXGE_HW_DEVICE_ACCESS_RIGHT_VPATH 0x1
    #define VXGE_HW_DEVICE_ACCESS_RIGHT_SRPCIM 0x2
    #define VXGE_HW_DEVICE_ACCESS_RIGHT_MRPCIM 0x4
        struct vxge_hw_legacy_reg __iomem *legacy_reg;
        struct vxge_hw_toc_reg __iomem *toc_reg;
        struct vxge_hw_common_reg __iomem *common_reg;
        struct vxge_hw_mrpcim_reg __iomem *mrpcim_reg;
        struct vxge_hw_srpcim_reg __iomem *srpcim_reg \[VXGE_HW_TITAN_SRPCIM_REG_SPACES];
        struct vxge_hw_vpmgmt_reg __iomem *vpmgmt_reg \[VXGE_HW_TITAN_VPMGMT_REG_SPACES];
        struct vxge_hw_vpath_reg __iomem *vpath_reg \[VXGE_HW_TITAN_VPATH_REG_SPACES];
        u8 __iomem *kdfc;
        u8 __iomem *usdc;
        struct __vxge_hw_virtualpath virtual_paths \[VXGE_HW_MAX_VIRTUAL_PATHS];
        u64 vpath_assignments;
        u64 vpaths_deployed;
        u32 first_vp_id;
        u64 tim_int_mask0[4];
        u32 tim_int_mask1[4];
        struct __vxge_hw_blockpool block_pool;
        struct vxge_hw_device_stats stats;
        u32 debug_module_mask;
        u32 debug_level;
        u32 level_err;
        u32 level_trace;
        u16 eprom_versions[VXGE_HW_MAX_ROM_IMAGES];
    }

.. _`__vxge_hw_device.members`:

Members
-------

magic
    Magic Number

bar0
    BAR0 virtual address.

pdev
    Physical device handle

ndev
    *undescribed*

config
    Confguration passed by the LL driver at initialization

link_state
    Link state

uld_callbacks
    *undescribed*

host_type
    *undescribed*

func_id
    *undescribed*

access_rights
    *undescribed*

legacy_reg
    *undescribed*

toc_reg
    *undescribed*

common_reg
    *undescribed*

mrpcim_reg
    *undescribed*

kdfc
    *undescribed*

usdc
    *undescribed*

vpath_assignments
    *undescribed*

vpaths_deployed
    *undescribed*

first_vp_id
    *undescribed*

block_pool
    *undescribed*

stats
    *undescribed*

debug_module_mask
    *undescribed*

debug_level
    *undescribed*

level_err
    *undescribed*

level_trace
    *undescribed*

.. _`__vxge_hw_device.description`:

Description
-----------

HW device object. Represents Titan adapter

.. _`vxge_hw_device_hw_info`:

struct vxge_hw_device_hw_info
=============================

.. c:type:: struct vxge_hw_device_hw_info

    Device information

.. _`vxge_hw_device_hw_info.definition`:

Definition
----------

.. code-block:: c

    struct vxge_hw_device_hw_info {
        u32 host_type;
    #define VXGE_HW_NO_MR_NO_SR_NORMAL_FUNCTION 0
    #define VXGE_HW_MR_NO_SR_VH0_BASE_FUNCTION 1
    #define VXGE_HW_NO_MR_SR_VH0_FUNCTION0 2
    #define VXGE_HW_NO_MR_SR_VH0_VIRTUAL_FUNCTION 3
    #define VXGE_HW_MR_SR_VH0_INVALID_CONFIG 4
    #define VXGE_HW_SR_VH_FUNCTION0 5
    #define VXGE_HW_SR_VH_VIRTUAL_FUNCTION 6
    #define VXGE_HW_VH_NORMAL_FUNCTION 7
        u64 function_mode;
    #define VXGE_HW_FUNCTION_MODE_SINGLE_FUNCTION 0
    #define VXGE_HW_FUNCTION_MODE_MULTI_FUNCTION 1
    #define VXGE_HW_FUNCTION_MODE_SRIOV 2
    #define VXGE_HW_FUNCTION_MODE_MRIOV 3
    #define VXGE_HW_FUNCTION_MODE_MRIOV_8 4
    #define VXGE_HW_FUNCTION_MODE_MULTI_FUNCTION_17 5
    #define VXGE_HW_FUNCTION_MODE_SRIOV_8 6
    #define VXGE_HW_FUNCTION_MODE_SRIOV_4 7
    #define VXGE_HW_FUNCTION_MODE_MULTI_FUNCTION_2 8
    #define VXGE_HW_FUNCTION_MODE_MULTI_FUNCTION_4 9
    #define VXGE_HW_FUNCTION_MODE_MRIOV_4 10
        u32 func_id;
        u64 vpath_mask;
        struct vxge_hw_device_version fw_version;
        struct vxge_hw_device_date fw_date;
        struct vxge_hw_device_version flash_version;
        struct vxge_hw_device_date flash_date;
        u8 serial_number[VXGE_HW_INFO_LEN];
        u8 part_number[VXGE_HW_INFO_LEN];
        u8 product_desc[VXGE_HW_INFO_LEN];
        u8 mac_addrs[VXGE_HW_MAX_VIRTUAL_PATHS][ETH_ALEN];
        u8 mac_addr_masks[VXGE_HW_MAX_VIRTUAL_PATHS][ETH_ALEN];
    }

.. _`vxge_hw_device_hw_info.members`:

Members
-------

host_type
    Host Type

function_mode
    *undescribed*

func_id
    Function Id

vpath_mask
    vpath bit mask

fw_version
    Firmware version

fw_date
    Firmware Date

flash_version
    Firmware version

flash_date
    Firmware Date

mac_addrs
    Mac addresses for each vpath

mac_addr_masks
    Mac address masks for each vpath

.. _`vxge_hw_device_hw_info.description`:

Description
-----------

Returns the vpath mask that has the bits set for each vpath allocated
for the driver and the first mac address for each vpath

.. _`vxge_hw_device_attr`:

struct vxge_hw_device_attr
==========================

.. c:type:: struct vxge_hw_device_attr

    Device memory spaces.

.. _`vxge_hw_device_attr.definition`:

Definition
----------

.. code-block:: c

    struct vxge_hw_device_attr {
        void __iomem *bar0;
        struct pci_dev *pdev;
        const struct vxge_hw_uld_cbs *uld_callbacks;
    }

.. _`vxge_hw_device_attr.members`:

Members
-------

bar0
    BAR0 virtual address.

pdev
    PCI device object.

uld_callbacks
    *undescribed*

.. _`vxge_hw_device_attr.description`:

Description
-----------

Device memory spaces. Includes configuration, BAR0 etc. per device
mapped memories. Also, includes a pointer to OS-specific PCI device object.

.. _`vxge_hw_txdl_state`:

enum vxge_hw_txdl_state
=======================

.. c:type:: enum vxge_hw_txdl_state

    Descriptor (TXDL) state.

.. _`vxge_hw_txdl_state.definition`:

Definition
----------

.. code-block:: c

    enum vxge_hw_txdl_state {
        VXGE_HW_TXDL_STATE_NONE,
        VXGE_HW_TXDL_STATE_AVAIL,
        VXGE_HW_TXDL_STATE_POSTED,
        VXGE_HW_TXDL_STATE_FREED
    };

.. _`vxge_hw_txdl_state.constants`:

Constants
---------

VXGE_HW_TXDL_STATE_NONE
    Invalid state.

VXGE_HW_TXDL_STATE_AVAIL
    Descriptor is available for reservation.

VXGE_HW_TXDL_STATE_POSTED
    Descriptor is posted for processing by the
    device.

VXGE_HW_TXDL_STATE_FREED
    Descriptor is free and can be reused for
    filling-in and posting later.

.. _`vxge_hw_txdl_state.description`:

Description
-----------

Titan/HW descriptor states.

.. _`vxge_hw_fifo_txd`:

struct vxge_hw_fifo_txd
=======================

.. c:type:: struct vxge_hw_fifo_txd

    Transmit Descriptor

.. _`vxge_hw_fifo_txd.definition`:

Definition
----------

.. code-block:: c

    struct vxge_hw_fifo_txd {
        u64 control_0;
    #define VXGE_HW_FIFO_TXD_LIST_OWN_ADAPTER vxge_mBIT(7)
    #define VXGE_HW_FIFO_TXD_T_CODE_GET(ctrl0) vxge_bVALn(ctrl0# 12# 4)
    #define VXGE_HW_FIFO_TXD_T_CODE(val) vxge_vBIT(val# 12# 4)
    #define VXGE_HW_FIFO_TXD_T_CODE_UNUSED VXGE_HW_FIFO_T_CODE_UNUSED
    #define VXGE_HW_FIFO_TXD_GATHER_CODE(val) vxge_vBIT(val# 22# 2)
    #define VXGE_HW_FIFO_TXD_GATHER_CODE_FIRST VXGE_HW_FIFO_GATHER_CODE_FIRST
    #define VXGE_HW_FIFO_TXD_GATHER_CODE_LAST VXGE_HW_FIFO_GATHER_CODE_LAST
    #define VXGE_HW_FIFO_TXD_LSO_EN vxge_mBIT(30)
    #define VXGE_HW_FIFO_TXD_LSO_MSS(val) vxge_vBIT(val# 34# 14)
    #define VXGE_HW_FIFO_TXD_BUFFER_SIZE(val) vxge_vBIT(val# 48# 16)
        u64 control_1;
    #define VXGE_HW_FIFO_TXD_TX_CKO_IPV4_EN vxge_mBIT(5)
    #define VXGE_HW_FIFO_TXD_TX_CKO_TCP_EN vxge_mBIT(6)
    #define VXGE_HW_FIFO_TXD_TX_CKO_UDP_EN vxge_mBIT(7)
    #define VXGE_HW_FIFO_TXD_VLAN_ENABLE vxge_mBIT(15)
    #define VXGE_HW_FIFO_TXD_VLAN_TAG(val) vxge_vBIT(val# 16# 16)
    #define VXGE_HW_FIFO_TXD_INT_NUMBER(val) vxge_vBIT(val# 34# 6)
    #define VXGE_HW_FIFO_TXD_INT_TYPE_PER_LIST vxge_mBIT(46)
    #define VXGE_HW_FIFO_TXD_INT_TYPE_UTILZ vxge_mBIT(47)
        u64 buffer_pointer;
        u64 host_control;
    }

.. _`vxge_hw_fifo_txd.members`:

Members
-------

control_0
    Bits 0 to 6 - Reserved.
    Bit 7 - List Ownership. This field should be initialized
    to '1' by the driver before the transmit list pointer is
    written to the adapter. This field will be set to '0' by the
    adapter once it has completed transmitting the frame or frames in
    the list. Note - This field is only valid in TxD0. Additionally,
    for multi-list sequences, the driver should not release any
    buffers until the ownership of the last list in the multi-list
    sequence has been returned to the host.
    Bits 8 to 11 - Reserved
    Bits 12 to 15 - Transfer_Code. This field is only valid in
    TxD0. It is used to describe the status of the transmit data
    buffer transfer. This field is always overwritten by the
    adapter, so this field may be initialized to any value.
    Bits 16 to 17 - Host steering. This field allows the host to
    override the selection of the physical transmit port.
    Attention:
    Normal sounds as if learned from the switch rather than from
    the aggregation algorythms.
    00: Normal. Use Destination/MAC Address
    lookup to determine the transmit port.
    01: Send on physical Port1.
    10: Send on physical Port0.
    11: Send on both ports.
    Bits 18 to 21 - Reserved
    Bits 22 to 23 - Gather_Code. This field is set by the host and
    is used to describe how individual buffers comprise a frame.
    10: First descriptor of a frame.
    00: Middle of a multi-descriptor frame.
    01: Last descriptor of a frame.
    11: First and last descriptor of a frame (the entire frame
    resides in a single buffer).
    For multi-descriptor frames, the only valid gather code sequence
    is {10, [00], 01}. In other words, the descriptors must be placed
    in the list in the correct order.
    Bits 24 to 27 - Reserved
    Bits 28 to 29 - LSO_Frm_Encap. LSO Frame Encapsulation
    definition. Only valid in TxD0. This field allows the host to
    indicate the Ethernet encapsulation of an outbound LSO packet.
    00 - classic mode (best guess)
    01 - LLC
    10 - SNAP
    11 - DIX
    If "classic mode" is selected, the adapter will attempt to
    decode the frame's Ethernet encapsulation by examining the L/T
    field as follows:
    <= 0x05DC LLC/SNAP encoding; must examine DSAP/SSAP to determine
    if packet is IPv4 or IPv6.
    0x8870 Jumbo-SNAP encoding.
    0x0800 IPv4 DIX encoding
    0x86DD IPv6 DIX encoding
    others illegal encapsulation
    Bits 30 - LSO\_ Flag. Large Send Offload (LSO) flag.
    Set to 1 to perform segmentation offload for TCP/UDP.
    This field is valid only in TxD0.
    Bits 31 to 33 - Reserved.
    Bits 34 to 47 - LSO_MSS. TCP/UDP LSO Maximum Segment Size
    This field is meaningful only when LSO_Control is non-zero.
    When LSO_Control is set to TCP_LSO, the single (possibly large)
    TCP segment described by this TxDL will be sent as a series of
    TCP segments each of which contains no more than LSO_MSS
    payload bytes.
    When LSO_Control is set to UDP_LSO, the single (possibly large)
    UDP datagram described by this TxDL will be sent as a series of
    UDP datagrams each of which contains no more than LSO_MSS
    payload bytes.
    All outgoing frames from this TxDL will have LSO_MSS bytes of UDP
    or TCP payload, with the exception of the last, which will have
    <= LSO_MSS bytes of payload.
    Bits 48 to 63 - Buffer_Size. Number of valid bytes in the
    buffer to be read by the adapter. This field is written by the
    host. A value of 0 is illegal.
    Bits 32 to 63 - This value is written by the adapter upon
    completion of a UDP or TCP LSO operation and indicates the number
    of UDP or TCP payload bytes that were transmitted. 0x0000 will be
    returned for any non-LSO operation.

control_1
    Bits 0 to 4 - Reserved.
    Bit 5 - Tx_CKO_IPv4 Set to a '1' to enable IPv4 header checksum
    offload. This field is only valid in the first TxD of a frame.
    Bit 6 - Tx_CKO_TCP Set to a '1' to enable TCP checksum offload.
    This field is only valid in the first TxD of a frame (the TxD's
    gather code must be 10 or 11). The driver should only set this
    bit if it can guarantee that TCP is present.
    Bit 7 - Tx_CKO_UDP Set to a '1' to enable UDP checksum offload.
    This field is only valid in the first TxD of a frame (the TxD's
    gather code must be 10 or 11). The driver should only set this
    bit if it can guarantee that UDP is present.
    Bits 8 to 14 - Reserved.
    Bit 15 - Tx_VLAN_Enable VLAN tag insertion flag. Set to a '1' to
    instruct the adapter to insert the VLAN tag specified by the
    Tx_VLAN_Tag field. This field is only valid in the first TxD of
    a frame.
    Bits 16 to 31 - Tx_VLAN_Tag. Variable portion of the VLAN tag
    to be inserted into the frame by the adapter (the first two bytes
    of a VLAN tag are always 0x8100). This field is only valid if the
    Tx_VLAN_Enable field is set to '1'.
    Bits 32 to 33 - Reserved.
    Bits 34 to 39 - Tx_Int_Number. Indicates which Tx interrupt
    number the frame associated with. This field is written by the
    host. It is only valid in the first TxD of a frame.
    Bits 40 to 42 - Reserved.
    Bit 43 - Set to 1 to exclude the frame from bandwidth metering
    functions. This field is valid only in the first TxD
    of a frame.
    Bits 44 to 45 - Reserved.
    Bit 46 - Tx_Int_Per_List Set to a '1' to instruct the adapter to
    generate an interrupt as soon as all of the frames in the list
    have been transmitted. In order to have per-frame interrupts,
    the driver should place a maximum of one frame per list. This
    field is only valid in the first TxD of a frame.
    Bit 47 - Tx_Int_Utilization Set to a '1' to instruct the adapter
    to count the frame toward the utilization interrupt specified in
    the Tx_Int_Number field. This field is only valid in the first
    TxD of a frame.
    Bits 48 to 63 - Reserved.

buffer_pointer
    Buffer start address.

host_control
    Host_Control.Opaque 64bit data stored by driver inside the
    Titan descriptor prior to posting the latter on the fifo
    via \ :c:func:`vxge_hw_fifo_txdl_post`\ .The \ ``host_control``\  is returned as is
    to the driver with each completed descriptor.

.. _`vxge_hw_fifo_txd.description`:

Description
-----------

Transmit descriptor (TxD).Fifo descriptor contains configured number
(list) of TxDs. \* For more details please refer to Titan User Guide,
Section 5.4.2 "Transmit Descriptor (TxD) Format".

.. _`vxge_hw_ring_rxd_1`:

struct vxge_hw_ring_rxd_1
=========================

.. c:type:: struct vxge_hw_ring_rxd_1

    One buffer mode RxD for ring

.. _`vxge_hw_ring_rxd_1.definition`:

Definition
----------

.. code-block:: c

    struct vxge_hw_ring_rxd_1 {
        u64 host_control;
        u64 control_0;
    #define VXGE_HW_RING_RXD_RTH_BUCKET_GET(ctrl0) vxge_bVALn(ctrl0# 0# 7)
    #define VXGE_HW_RING_RXD_LIST_OWN_ADAPTER vxge_mBIT(7)
    #define VXGE_HW_RING_RXD_FAST_PATH_ELIGIBLE_GET(ctrl0) vxge_bVALn(ctrl0# 8# 1)
    #define VXGE_HW_RING_RXD_L3_CKSUM_CORRECT_GET(ctrl0) vxge_bVALn(ctrl0# 9# 1)
    #define VXGE_HW_RING_RXD_L4_CKSUM_CORRECT_GET(ctrl0) vxge_bVALn(ctrl0# 10# 1)
    #define VXGE_HW_RING_RXD_T_CODE_GET(ctrl0) vxge_bVALn(ctrl0# 12# 4)
    #define VXGE_HW_RING_RXD_T_CODE(val) vxge_vBIT(val# 12# 4)
    #define VXGE_HW_RING_RXD_T_CODE_UNUSED VXGE_HW_RING_T_CODE_UNUSED
    #define VXGE_HW_RING_RXD_SYN_GET(ctrl0) vxge_bVALn(ctrl0# 16# 1)
    #define VXGE_HW_RING_RXD_IS_ICMP_GET(ctrl0) vxge_bVALn(ctrl0# 17# 1)
    #define VXGE_HW_RING_RXD_RTH_SPDM_HIT_GET(ctrl0) vxge_bVALn(ctrl0# 18# 1)
    #define VXGE_HW_RING_RXD_RTH_IT_HIT_GET(ctrl0) vxge_bVALn(ctrl0# 19# 1)
    #define VXGE_HW_RING_RXD_RTH_HASH_TYPE_GET(ctrl0) vxge_bVALn(ctrl0# 20# 4)
    #define VXGE_HW_RING_RXD_IS_VLAN_GET(ctrl0) vxge_bVALn(ctrl0# 24# 1)
    #define VXGE_HW_RING_RXD_ETHER_ENCAP_GET(ctrl0) vxge_bVALn(ctrl0# 25# 2)
    #define VXGE_HW_RING_RXD_FRAME_PROTO_GET(ctrl0) vxge_bVALn(ctrl0# 27# 5)
    #define VXGE_HW_RING_RXD_L3_CKSUM_GET(ctrl0) vxge_bVALn(ctrl0# 32# 16)
    #define VXGE_HW_RING_RXD_L4_CKSUM_GET(ctrl0) vxge_bVALn(ctrl0# 48# 16)
        u64 control_1;
    #define VXGE_HW_RING_RXD_1_BUFFER0_SIZE_GET(ctrl1) vxge_bVALn(ctrl1# 2# 14)
    #define VXGE_HW_RING_RXD_1_BUFFER0_SIZE(val) vxge_vBIT(val# 2# 14)
    #define VXGE_HW_RING_RXD_1_BUFFER0_SIZE_MASK vxge_vBIT(0x3FFF# 2# 14)
    #define VXGE_HW_RING_RXD_1_RTH_HASH_VAL_GET(ctrl1) vxge_bVALn(ctrl1# 16# 32)
    #define VXGE_HW_RING_RXD_VLAN_TAG_GET(ctrl1) vxge_bVALn(ctrl1# 48# 16)
        u64 buffer0_ptr;
    }

.. _`vxge_hw_ring_rxd_1.members`:

Members
-------

host_control
    This field is exclusively for host use and is "readonly"
    from the adapter's perspective.

control_0
    Bits 0 to 6 - RTH_Bucket get
    Bit 7 - Own Descriptor ownership bit. This bit is set to 1
    by the host, and is set to 0 by the adapter.
    0 - Host owns RxD and buffer.
    1 - The adapter owns RxD and buffer.
    Bit 8 - Fast_Path_Eligible When set, indicates that the
    received frame meets all of the criteria for fast path processing.
    The required criteria are as follows:
    !SYN &
    (Transfer_Code == "Transfer OK") &
    (!Is_IP_Fragment) &
    ((Is_IPv4 & computed_L3_checksum == 0xFFFF) \|
    (Is_IPv6)) &
    ((Is_TCP & computed_L4_checksum == 0xFFFF) \|
    (Is_UDP & (computed_L4_checksum == 0xFFFF \|
    computed \_L4_checksum == 0x0000)))
    (same meaning for all RxD buffer modes)
    Bit 9 - L3 Checksum Correct
    Bit 10 - L4 Checksum Correct
    Bit 11 - Reserved
    Bit 12 to 15 - This field is written by the adapter. It is
    used to report the status of the frame transfer to the host.
    0x0 - Transfer OK
    0x4 - RDA Failure During Transfer
    0x5 - Unparseable Packet, such as unknown IPv6 header.
    0x6 - Frame integrity error (FCS or ECC).
    0x7 - Buffer Size Error. The provided buffer(s) were not
    appropriately sized and data loss occurred.
    0x8 - Internal ECC Error. RxD corrupted.
    0x9 - IPv4 Checksum error
    0xA - TCP/UDP Checksum error
    0xF - Unknown Error or Multiple Error. Indicates an
    unknown problem or that more than one of transfer codes is set.
    Bit 16 - SYN The adapter sets this field to indicate that
    the incoming frame contained a TCP segment with its SYN bit
    set and its ACK bit NOT set. (same meaning for all RxD buffer
    modes)
    Bit 17 - Is ICMP
    Bit 18 - RTH_SPDM_HIT Set to 1 if there was a match in the
    Socket Pair Direct Match Table and the frame was steered based
    on SPDM.
    Bit 19 - RTH_IT_HIT Set to 1 if there was a match in the
    Indirection Table and the frame was steered based on hash
    indirection.
    Bit 20 to 23 - RTH_HASH_TYPE Indicates the function (hash
    type) that was used to calculate the hash.
    Bit 19 - IS_VLAN Set to '1' if the frame was/is VLAN
    tagged.
    Bit 25 to 26 - ETHER_ENCAP Reflects the Ethernet encapsulation
    of the received frame.
    0x0 - Ethernet DIX
    0x1 - LLC
    0x2 - SNAP (includes Jumbo-SNAP)
    0x3 - IPX
    Bit 27 - IS_IPV4 Set to '1' if the frame contains an IPv4 packet.
    Bit 28 - IS_IPV6 Set to '1' if the frame contains an IPv6 packet.
    Bit 29 - IS_IP_FRAG Set to '1' if the frame contains a fragmented
    IP packet.
    Bit 30 - IS_TCP Set to '1' if the frame contains a TCP segment.
    Bit 31 - IS_UDP Set to '1' if the frame contains a UDP message.
    Bit 32 to 47 - L3_Checksum[0:15] The IPv4 checksum value  that
    arrived with the frame. If the resulting computed IPv4 header
    checksum for the frame did not produce the expected 0xFFFF value,
    then the transfer code would be set to 0x9.
    Bit 48 to 63 - L4_Checksum[0:15] The TCP/UDP checksum value that
    arrived with the frame. If the resulting computed TCP/UDP checksum
    for the frame did not produce the expected 0xFFFF value, then the
    transfer code would be set to 0xA.

control_1
    Bits 0 to 1 - Reserved
    Bits 2 to 15 - Buffer0_Size.This field is set by the host and
    eventually overwritten by the adapter. The host writes the
    available buffer size in bytes when it passes the descriptor to
    the adapter. When a frame is delivered the host, the adapter
    populates this field with the number of bytes written into the
    buffer. The largest supported buffer is 16, 383 bytes.
    Bit 16 to 47 - RTH Hash Value 32-bit RTH hash value. Only valid if
    RTH_HASH_TYPE (Control_0, bits 20:23) is nonzero.
    Bit 48 to 63 - VLAN_Tag[0:15] The contents of the variable portion
    of the VLAN tag, if one was detected by the adapter. This field is
    populated even if VLAN-tag stripping is enabled.

buffer0_ptr
    Pointer to buffer. This field is populated by the driver.

.. _`vxge_hw_ring_rxd_1.description`:

Description
-----------

One buffer mode RxD for ring structure

.. _`vxge_hw_rth_hash_types`:

struct vxge_hw_rth_hash_types
=============================

.. c:type:: struct vxge_hw_rth_hash_types

    RTH hash types.

.. _`vxge_hw_rth_hash_types.definition`:

Definition
----------

.. code-block:: c

    struct vxge_hw_rth_hash_types {
        u8 hash_type_tcpipv4_en:1;
        u8 hash_type_ipv4_en:1:1;
        u8 hash_type_tcpipv6_en:1:1:1;
        u8 hash_type_ipv6_en:1:1:1:1;
        u8 hash_type_tcpipv6ex_en:1:1:1:1:1;
        u8 hash_type_ipv6ex_en:1:1:1:1:1:1;
    }

.. _`vxge_hw_rth_hash_types.members`:

Members
-------

hash_type_tcpipv4_en
    Enables RTH field type HashTypeTcpIPv4

hash_type_ipv4_en
    Enables RTH field type HashTypeIPv4

hash_type_tcpipv6_en
    Enables RTH field type HashTypeTcpIPv6

hash_type_ipv6_en
    Enables RTH field type HashTypeIPv6

hash_type_tcpipv6ex_en
    Enables RTH field type HashTypeTcpIPv6Ex

hash_type_ipv6ex_en
    Enables RTH field type HashTypeIPv6Ex

.. _`vxge_hw_rth_hash_types.description`:

Description
-----------

Used to pass RTH hash types to rts_rts_set.

.. _`vxge_hw_rth_hash_types.see-also`:

See also
--------

vxge_hw_vpath_rts_rth_set(), \ :c:func:`vxge_hw_vpath_rts_rth_get`\ .

.. _`vxge_hw_ring_rxd_size_get`:

vxge_hw_ring_rxd_size_get
=========================

.. c:function:: u32 vxge_hw_ring_rxd_size_get(u32 buf_mode)

    Get the size of ring descriptor.

    :param u32 buf_mode:
        Buffer mode (1, 3 or 5)

.. _`vxge_hw_ring_rxd_size_get.description`:

Description
-----------

This function returns the size of RxD for given buffer mode

.. _`vxge_hw_ring_rxds_per_block_get`:

vxge_hw_ring_rxds_per_block_get
===============================

.. c:function:: u32 vxge_hw_ring_rxds_per_block_get(u32 buf_mode)

    Get the number of rxds per block.

    :param u32 buf_mode:
        Buffer mode (1 buffer mode only)

.. _`vxge_hw_ring_rxds_per_block_get.description`:

Description
-----------

This function returns the number of RxD for RxD block for given buffer mode

.. _`vxge_hw_ring_rxd_1b_set`:

vxge_hw_ring_rxd_1b_set
=======================

.. c:function:: void vxge_hw_ring_rxd_1b_set(void *rxdh, dma_addr_t dma_pointer, u32 size)

    Prepare 1-buffer-mode descriptor.

    :param void \*rxdh:
        Descriptor handle.

    :param dma_addr_t dma_pointer:
        DMA address of a single receive buffer this descriptor
        should carry. Note that by the time vxge_hw_ring_rxd_1b_set is called,
        the receive buffer should be already mapped to the device

    :param u32 size:
        Size of the receive \ ``dma_pointer``\  buffer.

.. _`vxge_hw_ring_rxd_1b_set.description`:

Description
-----------

Prepare 1-buffer-mode Rx     descriptor for posting
(via \ :c:func:`vxge_hw_ring_rxd_post`\ ).

This inline helper-function does not return any parameters and always
succeeds.

.. _`vxge_hw_ring_rxd_1b_get`:

vxge_hw_ring_rxd_1b_get
=======================

.. c:function:: void vxge_hw_ring_rxd_1b_get(struct __vxge_hw_ring *ring_handle, void *rxdh, u32 *pkt_length)

    Get data from the completed 1-buf descriptor.

    :param struct __vxge_hw_ring \*ring_handle:
        *undescribed*

    :param void \*rxdh:
        Descriptor handle.

    :param u32 \*pkt_length:
        Length (in bytes) of the data in the buffer pointed by

.. _`vxge_hw_ring_rxd_1b_get.description`:

Description
-----------

Retrieve protocol data from the completed 1-buffer-mode Rx descriptor.
This inline helper-function uses completed descriptor to populate receive
buffer pointer and other "out" parameters. The function always succeeds.

.. _`vxge_hw_ring_rxd_1b_info_get`:

vxge_hw_ring_rxd_1b_info_get
============================

.. c:function:: void vxge_hw_ring_rxd_1b_info_get(struct __vxge_hw_ring *ring_handle, void *rxdh, struct vxge_hw_ring_rxd_info *rxd_info)

    Get extended information associated with a completed receive descriptor for 1b mode.

    :param struct __vxge_hw_ring \*ring_handle:
        *undescribed*

    :param void \*rxdh:
        Descriptor handle.

    :param struct vxge_hw_ring_rxd_info \*rxd_info:
        Descriptor information

.. _`vxge_hw_ring_rxd_1b_info_get.description`:

Description
-----------

Retrieve extended information associated with a completed receive descriptor.

.. _`vxge_hw_ring_rxd_private_get`:

vxge_hw_ring_rxd_private_get
============================

.. c:function:: void *vxge_hw_ring_rxd_private_get(void *rxdh)

    Get driver private per-descriptor data of 1b mode 3b mode ring.

    :param void \*rxdh:
        Descriptor handle.

.. _`vxge_hw_ring_rxd_private_get.return`:

Return
------

private driver      info associated with the descriptor.
driver requests      per-descriptor space via vxge_hw_ring_attr.

.. _`vxge_hw_fifo_txdl_cksum_set_bits`:

vxge_hw_fifo_txdl_cksum_set_bits
================================

.. c:function:: void vxge_hw_fifo_txdl_cksum_set_bits(void *txdlh, u64 cksum_bits)

    Offload checksum.

    :param void \*txdlh:
        Descriptor handle.

    :param u64 cksum_bits:
        Specifies which checksums are to be offloaded: IPv4,
        and/or TCP and/or UDP.

.. _`vxge_hw_fifo_txdl_cksum_set_bits.description`:

Description
-----------

Ask Titan to calculate IPv4 & transport checksums for \_this\_ transmit
descriptor.
This API is part of the preparation of the transmit descriptor for posting
(via \ :c:func:`vxge_hw_fifo_txdl_post`\ ). The related "preparation" APIs include
\ :c:func:`vxge_hw_fifo_txdl_mss_set`\ , \ :c:func:`vxge_hw_fifo_txdl_buffer_set_aligned`\ ,
and \ :c:func:`vxge_hw_fifo_txdl_buffer_set`\ .
All these APIs fill in the fields of the fifo descriptor,
in accordance with the Titan specification.

.. _`vxge_hw_fifo_txdl_mss_set`:

vxge_hw_fifo_txdl_mss_set
=========================

.. c:function:: void vxge_hw_fifo_txdl_mss_set(void *txdlh, int mss)

    Set MSS.

    :param void \*txdlh:
        Descriptor handle.

    :param int mss:
        MSS size for \_this\_ TCP connection. Passed by TCP stack down to the
        driver, which in turn inserts the MSS into the \ ``txdlh``\ .

.. _`vxge_hw_fifo_txdl_mss_set.description`:

Description
-----------

This API is part of the preparation of the transmit descriptor for posting
(via \ :c:func:`vxge_hw_fifo_txdl_post`\ ). The related "preparation" APIs include
\ :c:func:`vxge_hw_fifo_txdl_buffer_set`\ , \ :c:func:`vxge_hw_fifo_txdl_buffer_set_aligned`\ ,
and \ :c:func:`vxge_hw_fifo_txdl_cksum_set_bits`\ .
All these APIs fill in the fields of the fifo descriptor,
in accordance with the Titan specification.

.. _`vxge_hw_fifo_txdl_vlan_set`:

vxge_hw_fifo_txdl_vlan_set
==========================

.. c:function:: void vxge_hw_fifo_txdl_vlan_set(void *txdlh, u16 vlan_tag)

    Set VLAN tag.

    :param void \*txdlh:
        Descriptor handle.

    :param u16 vlan_tag:
        16bit VLAN tag.

.. _`vxge_hw_fifo_txdl_vlan_set.description`:

Description
-----------

Insert VLAN tag into specified transmit descriptor.
The actual insertion of the tag into outgoing frame is done by the hardware.

.. _`vxge_hw_fifo_txdl_private_get`:

vxge_hw_fifo_txdl_private_get
=============================

.. c:function:: void *vxge_hw_fifo_txdl_private_get(void *txdlh)

    Retrieve per-descriptor private data.

    :param void \*txdlh:
        Descriptor handle.

.. _`vxge_hw_fifo_txdl_private_get.description`:

Description
-----------

Retrieve per-descriptor private data.
Note that driver requests per-descriptor space via
struct vxge_hw_fifo_attr passed to
\ :c:func:`vxge_hw_vpath_open`\ .

.. _`vxge_hw_fifo_txdl_private_get.return`:

Return
------

private driver data associated with the descriptor.

.. _`vxge_hw_ring_attr`:

struct vxge_hw_ring_attr
========================

.. c:type:: struct vxge_hw_ring_attr

    Ring open "template".

.. _`vxge_hw_ring_attr.definition`:

Definition
----------

.. code-block:: c

    struct vxge_hw_ring_attr {
        enum vxge_hw_status (*callback)(struct __vxge_hw_ring *ringh,void *rxdh,u8 t_code,void *userdata);
        enum vxge_hw_status (*rxd_init)(void *rxdh,void *userdata);
        void (*rxd_term)(void *rxdh,enum vxge_hw_rxd_state state,void *userdata);
        void *userdata;
        u32 per_rxd_space;
    }

.. _`vxge_hw_ring_attr.members`:

Members
-------

callback
    Ring completion callback. HW invokes the callback when there
    are new completions on that ring. In many implementations
    the \ ``callback``\  executes in the hw interrupt context.

rxd_init
    Ring's descriptor-initialize callback.
    See vxge_hw_ring_rxd_init_f{}.
    If not NULL, HW invokes the callback when opening
    the ring.

rxd_term
    Ring's descriptor-terminate callback. If not NULL,
    HW invokes the callback when closing the corresponding ring.
    See also vxge_hw_ring_rxd_term_f{}.

userdata
    User-defined "context" of \_that\_ ring. Passed back to the
    user as one of the \ ``callback``\ , \ ``rxd_init``\ , and \ ``rxd_term``\  arguments.

per_rxd_space
    If specified (i.e., greater than zero): extra space
    reserved by HW per each receive descriptor.
    Can be used to store
    and retrieve on completion, information specific
    to the driver.

.. _`vxge_hw_ring_attr.description`:

Description
-----------

Ring open "template". User fills the structure with ring
attributes and passes it to \ :c:func:`vxge_hw_vpath_open`\ .

.. _`vxge_hw_vpath_attr`:

struct vxge_hw_vpath_attr
=========================

.. c:type:: struct vxge_hw_vpath_attr

    Attributes of virtual path

.. _`vxge_hw_vpath_attr.definition`:

Definition
----------

.. code-block:: c

    struct vxge_hw_vpath_attr {
        u32 vp_id;
        struct vxge_hw_ring_attr ring_attr;
        struct vxge_hw_fifo_attr fifo_attr;
    }

.. _`vxge_hw_vpath_attr.members`:

Members
-------

vp_id
    Identifier of Virtual Path

ring_attr
    Attributes of ring for non-offload receive

fifo_attr
    Attributes of fifo for non-offload transmit

.. _`vxge_hw_vpath_attr.description`:

Description
-----------

Attributes of virtual path.  This structure is passed as parameter
to the \ :c:func:`vxge_hw_vpath_open`\  routine to set the attributes of ring and fifo.

.. _`vxge_hw_device_link_state_get`:

vxge_hw_device_link_state_get
=============================

.. c:function:: enum vxge_hw_device_link_state vxge_hw_device_link_state_get(struct __vxge_hw_device *devh)

    Get link state.

    :param struct __vxge_hw_device \*devh:
        HW device handle.

.. _`vxge_hw_device_link_state_get.description`:

Description
-----------

Get link state.

.. _`vxge_hw_device_link_state_get.return`:

Return
------

link state.

.. _`vxge_debug_ll`:

vxge_debug_ll
=============

.. c:function::  vxge_debug_ll( level,  mask,  fmt,  ...)

    :param  level:
        level of debug verbosity.

    :param  mask:
        mask for the debug

    :param  fmt:
        printf like format string

    :param ... :
        variable arguments

.. _`vxge_debug_ll.description`:

Description
-----------

Provides logging facilities. Can be customized on per-module
basis or/and with debug levels. Input parameters, except
module and level, are the same as posix printf. This function
may be compiled out if DEBUG macro was never defined.

.. _`vxge_debug_ll.see-also`:

See also
--------

enum vxge_debug_level{}.

.. This file was automatic generated / don't edit.


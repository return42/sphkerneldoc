.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/igb/igb_main.c

.. _`igb_get_i2c_data`:

igb_get_i2c_data
================

.. c:function:: int igb_get_i2c_data(void *data)

    Reads the I2C SDA data bit

    :param data:
        *undescribed*
    :type data: void \*

.. _`igb_get_i2c_data.description`:

Description
-----------

Returns the I2C data bit value

.. _`igb_set_i2c_data`:

igb_set_i2c_data
================

.. c:function:: void igb_set_i2c_data(void *data, int state)

    Sets the I2C data bit

    :param data:
        pointer to hardware structure
    :type data: void \*

    :param state:
        I2C data value (0 or 1) to set
    :type state: int

.. _`igb_set_i2c_data.description`:

Description
-----------

Sets the I2C data bit

.. _`igb_set_i2c_clk`:

igb_set_i2c_clk
===============

.. c:function:: void igb_set_i2c_clk(void *data, int state)

    Sets the I2C SCL clock

    :param data:
        pointer to hardware structure
    :type data: void \*

    :param state:
        state to set clock
    :type state: int

.. _`igb_set_i2c_clk.description`:

Description
-----------

Sets the I2C clock line to state

.. _`igb_get_i2c_clk`:

igb_get_i2c_clk
===============

.. c:function:: int igb_get_i2c_clk(void *data)

    Gets the I2C SCL clock state

    :param data:
        pointer to hardware structure
    :type data: void \*

.. _`igb_get_i2c_clk.description`:

Description
-----------

Gets the I2C clock state

.. _`igb_get_hw_dev`:

igb_get_hw_dev
==============

.. c:function:: struct net_device *igb_get_hw_dev(struct e1000_hw *hw)

    return device

    :param hw:
        pointer to hardware structure
    :type hw: struct e1000_hw \*

.. _`igb_get_hw_dev.description`:

Description
-----------

used by hardware layer to print debugging information

.. _`igb_init_module`:

igb_init_module
===============

.. c:function:: int igb_init_module( void)

    Driver Registration Routine

    :param void:
        no arguments
    :type void: 

.. _`igb_init_module.description`:

Description
-----------

igb_init_module is the first routine called when the driver is
loaded. All it does is register with the PCI subsystem.

.. _`igb_exit_module`:

igb_exit_module
===============

.. c:function:: void __exit igb_exit_module( void)

    Driver Exit Cleanup Routine

    :param void:
        no arguments
    :type void: 

.. _`igb_exit_module.description`:

Description
-----------

igb_exit_module is called just before the driver is removed
from memory.

.. _`igb_cache_ring_register`:

igb_cache_ring_register
=======================

.. c:function:: void igb_cache_ring_register(struct igb_adapter *adapter)

    Descriptor ring to register mapping

    :param adapter:
        board private structure to initialize
    :type adapter: struct igb_adapter \*

.. _`igb_cache_ring_register.description`:

Description
-----------

Once we know the feature-set enabled for the device, we'll cache
the register offset the descriptor ring is assigned to.

.. _`igb_write_ivar`:

igb_write_ivar
==============

.. c:function:: void igb_write_ivar(struct e1000_hw *hw, int msix_vector, int index, int offset)

    configure ivar for given MSI-X vector

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param msix_vector:
        vector number we are allocating to a given ring
    :type msix_vector: int

    :param index:
        row index of IVAR register to write within IVAR table
    :type index: int

    :param offset:
        column offset of in IVAR, should be multiple of 8
    :type offset: int

.. _`igb_write_ivar.description`:

Description
-----------

This function is intended to handle the writing of the IVAR register
for adapters 82576 and newer.  The IVAR table consists of 2 columns,
each containing an cause allocation for an Rx and Tx ring, and a
variable number of rows depending on the number of queues supported.

.. _`igb_configure_msix`:

igb_configure_msix
==================

.. c:function:: void igb_configure_msix(struct igb_adapter *adapter)

    Configure MSI-X hardware

    :param adapter:
        board private structure to initialize
    :type adapter: struct igb_adapter \*

.. _`igb_configure_msix.description`:

Description
-----------

igb_configure_msix sets up the hardware to properly
generate MSI-X interrupts.

.. _`igb_request_msix`:

igb_request_msix
================

.. c:function:: int igb_request_msix(struct igb_adapter *adapter)

    Initialize MSI-X interrupts

    :param adapter:
        board private structure to initialize
    :type adapter: struct igb_adapter \*

.. _`igb_request_msix.description`:

Description
-----------

igb_request_msix allocates MSI-X vectors and requests interrupts from the
kernel.

.. _`igb_free_q_vector`:

igb_free_q_vector
=================

.. c:function:: void igb_free_q_vector(struct igb_adapter *adapter, int v_idx)

    Free memory allocated for specific interrupt vector

    :param adapter:
        board private structure to initialize
    :type adapter: struct igb_adapter \*

    :param v_idx:
        Index of vector to be freed
    :type v_idx: int

.. _`igb_free_q_vector.description`:

Description
-----------

This function frees the memory allocated to the q_vector.

.. _`igb_reset_q_vector`:

igb_reset_q_vector
==================

.. c:function:: void igb_reset_q_vector(struct igb_adapter *adapter, int v_idx)

    Reset config for interrupt vector

    :param adapter:
        board private structure to initialize
    :type adapter: struct igb_adapter \*

    :param v_idx:
        Index of vector to be reset
    :type v_idx: int

.. _`igb_reset_q_vector.description`:

Description
-----------

If NAPI is enabled it will delete any references to the
NAPI struct. This is preparation for igb_free_q_vector.

.. _`igb_free_q_vectors`:

igb_free_q_vectors
==================

.. c:function:: void igb_free_q_vectors(struct igb_adapter *adapter)

    Free memory allocated for interrupt vectors

    :param adapter:
        board private structure to initialize
    :type adapter: struct igb_adapter \*

.. _`igb_free_q_vectors.description`:

Description
-----------

This function frees the memory allocated to the q_vectors.  In addition if
NAPI is enabled it will delete any references to the NAPI struct prior
to freeing the q_vector.

.. _`igb_clear_interrupt_scheme`:

igb_clear_interrupt_scheme
==========================

.. c:function:: void igb_clear_interrupt_scheme(struct igb_adapter *adapter)

    reset the device to a state of no interrupts

    :param adapter:
        board private structure to initialize
    :type adapter: struct igb_adapter \*

.. _`igb_clear_interrupt_scheme.description`:

Description
-----------

This function resets the device so that it has 0 Rx queues, Tx queues, and
MSI-X interrupts allocated.

.. _`igb_set_interrupt_capability`:

igb_set_interrupt_capability
============================

.. c:function:: void igb_set_interrupt_capability(struct igb_adapter *adapter, bool msix)

    set MSI or MSI-X if supported

    :param adapter:
        board private structure to initialize
    :type adapter: struct igb_adapter \*

    :param msix:
        boolean value of MSIX capability
    :type msix: bool

.. _`igb_set_interrupt_capability.description`:

Description
-----------

Attempt to configure interrupts using the best available
capabilities of the hardware and kernel.

.. _`igb_alloc_q_vector`:

igb_alloc_q_vector
==================

.. c:function:: int igb_alloc_q_vector(struct igb_adapter *adapter, int v_count, int v_idx, int txr_count, int txr_idx, int rxr_count, int rxr_idx)

    Allocate memory for a single interrupt vector

    :param adapter:
        board private structure to initialize
    :type adapter: struct igb_adapter \*

    :param v_count:
        q_vectors allocated on adapter, used for ring interleaving
    :type v_count: int

    :param v_idx:
        index of vector in adapter struct
    :type v_idx: int

    :param txr_count:
        total number of Tx rings to allocate
    :type txr_count: int

    :param txr_idx:
        index of first Tx ring to allocate
    :type txr_idx: int

    :param rxr_count:
        total number of Rx rings to allocate
    :type rxr_count: int

    :param rxr_idx:
        index of first Rx ring to allocate
    :type rxr_idx: int

.. _`igb_alloc_q_vector.description`:

Description
-----------

We allocate one q_vector.  If allocation fails we return -ENOMEM.

.. _`igb_alloc_q_vectors`:

igb_alloc_q_vectors
===================

.. c:function:: int igb_alloc_q_vectors(struct igb_adapter *adapter)

    Allocate memory for interrupt vectors

    :param adapter:
        board private structure to initialize
    :type adapter: struct igb_adapter \*

.. _`igb_alloc_q_vectors.description`:

Description
-----------

We allocate one q_vector per queue interrupt.  If allocation fails we
return -ENOMEM.

.. _`igb_init_interrupt_scheme`:

igb_init_interrupt_scheme
=========================

.. c:function:: int igb_init_interrupt_scheme(struct igb_adapter *adapter, bool msix)

    initialize interrupts, allocate queues/vectors

    :param adapter:
        board private structure to initialize
    :type adapter: struct igb_adapter \*

    :param msix:
        boolean value of MSIX capability
    :type msix: bool

.. _`igb_init_interrupt_scheme.description`:

Description
-----------

This function initializes the interrupts and allocates all of the queues.

.. _`igb_request_irq`:

igb_request_irq
===============

.. c:function:: int igb_request_irq(struct igb_adapter *adapter)

    initialize interrupts

    :param adapter:
        board private structure to initialize
    :type adapter: struct igb_adapter \*

.. _`igb_request_irq.description`:

Description
-----------

Attempts to configure interrupts using the best available
capabilities of the hardware and kernel.

.. _`igb_irq_disable`:

igb_irq_disable
===============

.. c:function:: void igb_irq_disable(struct igb_adapter *adapter)

    Mask off interrupt generation on the NIC

    :param adapter:
        board private structure
    :type adapter: struct igb_adapter \*

.. _`igb_irq_enable`:

igb_irq_enable
==============

.. c:function:: void igb_irq_enable(struct igb_adapter *adapter)

    Enable default interrupt generation settings

    :param adapter:
        board private structure
    :type adapter: struct igb_adapter \*

.. _`igb_release_hw_control`:

igb_release_hw_control
======================

.. c:function:: void igb_release_hw_control(struct igb_adapter *adapter)

    release control of the h/w to f/w

    :param adapter:
        address of board private structure
    :type adapter: struct igb_adapter \*

.. _`igb_release_hw_control.description`:

Description
-----------

igb_release_hw_control resets CTRL_EXT:DRV_LOAD bit.
For ASF and Pass Through versions of f/w this means that the
driver is no longer loaded.

.. _`igb_get_hw_control`:

igb_get_hw_control
==================

.. c:function:: void igb_get_hw_control(struct igb_adapter *adapter)

    get control of the h/w from f/w

    :param adapter:
        address of board private structure
    :type adapter: struct igb_adapter \*

.. _`igb_get_hw_control.description`:

Description
-----------

igb_get_hw_control sets CTRL_EXT:DRV_LOAD bit.
For ASF and Pass Through versions of f/w this means that
the driver is loaded.

.. _`igb_config_tx_modes`:

igb_config_tx_modes
===================

.. c:function:: void igb_config_tx_modes(struct igb_adapter *adapter, int queue)

    Configure "Qav Tx mode" features on igb

    :param adapter:
        pointer to adapter struct
    :type adapter: struct igb_adapter \*

    :param queue:
        queue number
    :type queue: int

.. _`igb_config_tx_modes.description`:

Description
-----------

Configure CBS and Launchtime for a given hardware queue.
Parameters are retrieved from the correct Tx ring, so
\ :c:func:`igb_save_cbs_params`\  and \ :c:func:`igb_save_txtime_params`\  should be used
for setting those correctly prior to this function being called.

.. _`igb_setup_tx_mode`:

igb_setup_tx_mode
=================

.. c:function:: void igb_setup_tx_mode(struct igb_adapter *adapter)

    Switch to/from Qav Tx mode when applicable

    :param adapter:
        pointer to adapter struct
    :type adapter: struct igb_adapter \*

.. _`igb_setup_tx_mode.description`:

Description
-----------

Configure TQAVCTRL register switching the controller's Tx mode
if FQTSS mode is enabled or disabled. Additionally, will issue
a call to \ :c:func:`igb_config_tx_modes`\  per queue so any previously saved
Tx parameters are applied.

.. _`igb_configure`:

igb_configure
=============

.. c:function:: void igb_configure(struct igb_adapter *adapter)

    configure the hardware for RX and TX

    :param adapter:
        private board structure
    :type adapter: struct igb_adapter \*

.. _`igb_power_up_link`:

igb_power_up_link
=================

.. c:function:: void igb_power_up_link(struct igb_adapter *adapter)

    Power up the phy/serdes link

    :param adapter:
        address of board private structure
    :type adapter: struct igb_adapter \*

.. _`igb_power_down_link`:

igb_power_down_link
===================

.. c:function:: void igb_power_down_link(struct igb_adapter *adapter)

    Power down the phy/serdes link

    :param adapter:
        address of board private structure
    :type adapter: struct igb_adapter \*

.. _`igb_check_swap_media`:

igb_check_swap_media
====================

.. c:function:: void igb_check_swap_media(struct igb_adapter *adapter)

    :param adapter:
        address of the board private structure
    :type adapter: struct igb_adapter \*

.. _`igb_up`:

igb_up
======

.. c:function:: int igb_up(struct igb_adapter *adapter)

    Open the interface and prepare it to handle traffic

    :param adapter:
        board private structure
    :type adapter: struct igb_adapter \*

.. _`igb_set_fw_version`:

igb_set_fw_version
==================

.. c:function:: void igb_set_fw_version(struct igb_adapter *adapter)

    Configure version string for ethtool

    :param adapter:
        adapter struct
    :type adapter: struct igb_adapter \*

.. _`igb_init_mas`:

igb_init_mas
============

.. c:function:: void igb_init_mas(struct igb_adapter *adapter)

    init Media Autosense feature if enabled in the NVM

    :param adapter:
        adapter struct
    :type adapter: struct igb_adapter \*

.. _`igb_init_i2c`:

igb_init_i2c
============

.. c:function:: s32 igb_init_i2c(struct igb_adapter *adapter)

    Init I2C interface

    :param adapter:
        pointer to adapter structure
    :type adapter: struct igb_adapter \*

.. _`igb_probe`:

igb_probe
=========

.. c:function:: int igb_probe(struct pci_dev *pdev, const struct pci_device_id *ent)

    Device Initialization Routine

    :param pdev:
        PCI device information struct
    :type pdev: struct pci_dev \*

    :param ent:
        entry in igb_pci_tbl
    :type ent: const struct pci_device_id \*

.. _`igb_probe.description`:

Description
-----------

Returns 0 on success, negative on failure

igb_probe initializes an adapter identified by a pci_dev structure.
The OS initialization, configuring of the adapter private structure,
and a hardware reset occur.

.. _`igb_remove_i2c`:

igb_remove_i2c
==============

.. c:function:: void igb_remove_i2c(struct igb_adapter *adapter)

    Cleanup  I2C interface

    :param adapter:
        pointer to adapter structure
    :type adapter: struct igb_adapter \*

.. _`igb_remove`:

igb_remove
==========

.. c:function:: void igb_remove(struct pci_dev *pdev)

    Device Removal Routine

    :param pdev:
        PCI device information struct
    :type pdev: struct pci_dev \*

.. _`igb_remove.description`:

Description
-----------

igb_remove is called by the PCI subsystem to alert the driver
that it should release a PCI device.  The could be caused by a
Hot-Plug event, or because the driver is going to be removed from
memory.

.. _`igb_probe_vfs`:

igb_probe_vfs
=============

.. c:function:: void igb_probe_vfs(struct igb_adapter *adapter)

    Initialize vf data storage and add VFs to pci config space

    :param adapter:
        board private structure to initialize
    :type adapter: struct igb_adapter \*

.. _`igb_probe_vfs.description`:

Description
-----------

This function initializes the vf specific data storage and then attempts to
allocate the VFs.  The reason for ordering it this way is because it is much
mor expensive time wise to disable SR-IOV than it is to allocate and free
the memory for the VFs.

.. _`igb_sw_init`:

igb_sw_init
===========

.. c:function:: int igb_sw_init(struct igb_adapter *adapter)

    Initialize general software structures (struct igb_adapter)

    :param adapter:
        board private structure to initialize
    :type adapter: struct igb_adapter \*

.. _`igb_sw_init.description`:

Description
-----------

igb_sw_init initializes the Adapter private data structure.
Fields are initialized based on PCI device information and
OS network device settings (MTU size).

.. _`__igb_open`:

\__igb_open
===========

.. c:function:: int __igb_open(struct net_device *netdev, bool resuming)

    Called when a network interface is made active

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param resuming:
        *undescribed*
    :type resuming: bool

.. _`__igb_open.description`:

Description
-----------

Returns 0 on success, negative value on failure

The open entry point is called when a network interface is made
active by the system (IFF_UP).  At this point all resources needed
for transmit and receive operations are allocated, the interrupt
handler is registered with the OS, the watchdog timer is started,
and the stack is notified that the interface is ready.

.. _`__igb_close`:

\__igb_close
============

.. c:function:: int __igb_close(struct net_device *netdev, bool suspending)

    Disables a network interface

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param suspending:
        *undescribed*
    :type suspending: bool

.. _`__igb_close.description`:

Description
-----------

Returns 0, this is not allowed to fail

The close entry point is called when an interface is de-activated
by the OS.  The hardware is still under the driver's control, but
needs to be disabled.  A global MAC reset is issued to stop the
hardware, and all transmit and receive resources are freed.

.. _`igb_setup_tx_resources`:

igb_setup_tx_resources
======================

.. c:function:: int igb_setup_tx_resources(struct igb_ring *tx_ring)

    allocate Tx resources (Descriptors)

    :param tx_ring:
        tx descriptor ring (for a specific queue) to setup
    :type tx_ring: struct igb_ring \*

.. _`igb_setup_tx_resources.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`igb_setup_all_tx_resources`:

igb_setup_all_tx_resources
==========================

.. c:function:: int igb_setup_all_tx_resources(struct igb_adapter *adapter)

    wrapper to allocate Tx resources (Descriptors) for all queues

    :param adapter:
        board private structure
    :type adapter: struct igb_adapter \*

.. _`igb_setup_all_tx_resources.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`igb_setup_tctl`:

igb_setup_tctl
==============

.. c:function:: void igb_setup_tctl(struct igb_adapter *adapter)

    configure the transmit control registers

    :param adapter:
        Board private structure
    :type adapter: struct igb_adapter \*

.. _`igb_configure_tx_ring`:

igb_configure_tx_ring
=====================

.. c:function:: void igb_configure_tx_ring(struct igb_adapter *adapter, struct igb_ring *ring)

    Configure transmit ring after Reset

    :param adapter:
        board private structure
    :type adapter: struct igb_adapter \*

    :param ring:
        tx ring to configure
    :type ring: struct igb_ring \*

.. _`igb_configure_tx_ring.description`:

Description
-----------

Configure a transmit ring after a reset.

.. _`igb_configure_tx`:

igb_configure_tx
================

.. c:function:: void igb_configure_tx(struct igb_adapter *adapter)

    Configure transmit Unit after Reset

    :param adapter:
        board private structure
    :type adapter: struct igb_adapter \*

.. _`igb_configure_tx.description`:

Description
-----------

Configure the Tx unit of the MAC after a reset.

.. _`igb_setup_rx_resources`:

igb_setup_rx_resources
======================

.. c:function:: int igb_setup_rx_resources(struct igb_ring *rx_ring)

    allocate Rx resources (Descriptors)

    :param rx_ring:
        Rx descriptor ring (for a specific queue) to setup
    :type rx_ring: struct igb_ring \*

.. _`igb_setup_rx_resources.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`igb_setup_all_rx_resources`:

igb_setup_all_rx_resources
==========================

.. c:function:: int igb_setup_all_rx_resources(struct igb_adapter *adapter)

    wrapper to allocate Rx resources (Descriptors) for all queues

    :param adapter:
        board private structure
    :type adapter: struct igb_adapter \*

.. _`igb_setup_all_rx_resources.description`:

Description
-----------

Return 0 on success, negative on failure

.. _`igb_setup_mrqc`:

igb_setup_mrqc
==============

.. c:function:: void igb_setup_mrqc(struct igb_adapter *adapter)

    configure the multiple receive queue control registers

    :param adapter:
        Board private structure
    :type adapter: struct igb_adapter \*

.. _`igb_setup_rctl`:

igb_setup_rctl
==============

.. c:function:: void igb_setup_rctl(struct igb_adapter *adapter)

    configure the receive control registers

    :param adapter:
        Board private structure
    :type adapter: struct igb_adapter \*

.. _`igb_configure_rx_ring`:

igb_configure_rx_ring
=====================

.. c:function:: void igb_configure_rx_ring(struct igb_adapter *adapter, struct igb_ring *ring)

    Configure a receive ring after Reset

    :param adapter:
        board private structure
    :type adapter: struct igb_adapter \*

    :param ring:
        receive ring to be configured
    :type ring: struct igb_ring \*

.. _`igb_configure_rx_ring.description`:

Description
-----------

Configure the Rx unit of the MAC after a reset.

.. _`igb_configure_rx`:

igb_configure_rx
================

.. c:function:: void igb_configure_rx(struct igb_adapter *adapter)

    Configure receive Unit after Reset

    :param adapter:
        board private structure
    :type adapter: struct igb_adapter \*

.. _`igb_configure_rx.description`:

Description
-----------

Configure the Rx unit of the MAC after a reset.

.. _`igb_free_tx_resources`:

igb_free_tx_resources
=====================

.. c:function:: void igb_free_tx_resources(struct igb_ring *tx_ring)

    Free Tx Resources per Queue

    :param tx_ring:
        Tx descriptor ring for a specific queue
    :type tx_ring: struct igb_ring \*

.. _`igb_free_tx_resources.description`:

Description
-----------

Free all transmit software resources

.. _`igb_free_all_tx_resources`:

igb_free_all_tx_resources
=========================

.. c:function:: void igb_free_all_tx_resources(struct igb_adapter *adapter)

    Free Tx Resources for All Queues

    :param adapter:
        board private structure
    :type adapter: struct igb_adapter \*

.. _`igb_free_all_tx_resources.description`:

Description
-----------

Free all transmit software resources

.. _`igb_clean_tx_ring`:

igb_clean_tx_ring
=================

.. c:function:: void igb_clean_tx_ring(struct igb_ring *tx_ring)

    Free Tx Buffers

    :param tx_ring:
        ring to be cleaned
    :type tx_ring: struct igb_ring \*

.. _`igb_clean_all_tx_rings`:

igb_clean_all_tx_rings
======================

.. c:function:: void igb_clean_all_tx_rings(struct igb_adapter *adapter)

    Free Tx Buffers for all queues

    :param adapter:
        board private structure
    :type adapter: struct igb_adapter \*

.. _`igb_free_rx_resources`:

igb_free_rx_resources
=====================

.. c:function:: void igb_free_rx_resources(struct igb_ring *rx_ring)

    Free Rx Resources

    :param rx_ring:
        ring to clean the resources from
    :type rx_ring: struct igb_ring \*

.. _`igb_free_rx_resources.description`:

Description
-----------

Free all receive software resources

.. _`igb_free_all_rx_resources`:

igb_free_all_rx_resources
=========================

.. c:function:: void igb_free_all_rx_resources(struct igb_adapter *adapter)

    Free Rx Resources for All Queues

    :param adapter:
        board private structure
    :type adapter: struct igb_adapter \*

.. _`igb_free_all_rx_resources.description`:

Description
-----------

Free all receive software resources

.. _`igb_clean_rx_ring`:

igb_clean_rx_ring
=================

.. c:function:: void igb_clean_rx_ring(struct igb_ring *rx_ring)

    Free Rx Buffers per Queue

    :param rx_ring:
        ring to free buffers from
    :type rx_ring: struct igb_ring \*

.. _`igb_clean_all_rx_rings`:

igb_clean_all_rx_rings
======================

.. c:function:: void igb_clean_all_rx_rings(struct igb_adapter *adapter)

    Free Rx Buffers for all queues

    :param adapter:
        board private structure
    :type adapter: struct igb_adapter \*

.. _`igb_set_mac`:

igb_set_mac
===========

.. c:function:: int igb_set_mac(struct net_device *netdev, void *p)

    Change the Ethernet Address of the NIC

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param p:
        pointer to an address structure
    :type p: void \*

.. _`igb_set_mac.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`igb_write_mc_addr_list`:

igb_write_mc_addr_list
======================

.. c:function:: int igb_write_mc_addr_list(struct net_device *netdev)

    write multicast addresses to MTA

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`igb_write_mc_addr_list.description`:

Description
-----------

Writes multicast address list to the MTA hash table.

.. _`igb_write_mc_addr_list.return`:

Return
------

-ENOMEM on failure
0 on no addresses written
X on writing X addresses to MTA

.. _`igb_set_rx_mode`:

igb_set_rx_mode
===============

.. c:function:: void igb_set_rx_mode(struct net_device *netdev)

    Secondary Unicast, Multicast and Promiscuous mode set

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`igb_set_rx_mode.description`:

Description
-----------

The set_rx_mode entry point is called whenever the unicast or multicast
address lists or the network interface flags are updated.  This routine is
responsible for configuring the hardware for proper unicast, multicast,
promiscuous mode, and all-multi behavior.

.. _`igb_has_link`:

igb_has_link
============

.. c:function:: bool igb_has_link(struct igb_adapter *adapter)

    check shared code for link and determine up/down

    :param adapter:
        pointer to driver private info
    :type adapter: struct igb_adapter \*

.. _`igb_check_lvmmc`:

igb_check_lvmmc
===============

.. c:function:: void igb_check_lvmmc(struct igb_adapter *adapter)

    check for malformed packets received and indicated in LVMMC register

    :param adapter:
        pointer to adapter
    :type adapter: struct igb_adapter \*

.. _`igb_watchdog`:

igb_watchdog
============

.. c:function:: void igb_watchdog(struct timer_list *t)

    Timer Call-back

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`igb_update_ring_itr`:

igb_update_ring_itr
===================

.. c:function:: void igb_update_ring_itr(struct igb_q_vector *q_vector)

    update the dynamic ITR value based on packet size

    :param q_vector:
        pointer to q_vector
    :type q_vector: struct igb_q_vector \*

.. _`igb_update_ring_itr.description`:

Description
-----------

Stores a new ITR value based on strictly on packet size.  This
algorithm is less sophisticated than that used in igb_update_itr,
due to the difficulty of synchronizing statistics across multiple
receive rings.  The divisors and thresholds used by this function
were determined based on theoretical maximum wire speed and testing
data, in order to minimize response time while increasing bulk
throughput.
This functionality is controlled by ethtool's coalescing settings.

.. _`igb_update_ring_itr.note`:

NOTE
----

This function is called only when operating in a multiqueue
receive environment.

.. _`igb_update_itr`:

igb_update_itr
==============

.. c:function:: void igb_update_itr(struct igb_q_vector *q_vector, struct igb_ring_container *ring_container)

    update the dynamic ITR value based on statistics

    :param q_vector:
        pointer to q_vector
    :type q_vector: struct igb_q_vector \*

    :param ring_container:
        ring info to update the itr for
    :type ring_container: struct igb_ring_container \*

.. _`igb_update_itr.description`:

Description
-----------

Stores a new ITR value based on packets and byte
counts during the last interrupt.  The advantage of per interrupt
computation is faster updates and more accurate ITR for the current
traffic pattern.  Constants in this function were computed
based on theoretical maximum wire speed and thresholds were set based
on testing data as well as attempting to minimize response time
while increasing bulk throughput.
This functionality is controlled by ethtool's coalescing settings.

.. _`igb_update_itr.note`:

NOTE
----

These calculations are only valid when operating in a single-
queue environment.

.. _`igb_tx_timeout`:

igb_tx_timeout
==============

.. c:function:: void igb_tx_timeout(struct net_device *netdev)

    Respond to a Tx Hang

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

.. _`igb_get_stats64`:

igb_get_stats64
===============

.. c:function:: void igb_get_stats64(struct net_device *netdev, struct rtnl_link_stats64 *stats)

    Get System Network Statistics

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param stats:
        rtnl_link_stats64 pointer
    :type stats: struct rtnl_link_stats64 \*

.. _`igb_change_mtu`:

igb_change_mtu
==============

.. c:function:: int igb_change_mtu(struct net_device *netdev, int new_mtu)

    Change the Maximum Transfer Unit

    :param netdev:
        network interface device structure
    :type netdev: struct net_device \*

    :param new_mtu:
        new value for maximum frame size
    :type new_mtu: int

.. _`igb_change_mtu.description`:

Description
-----------

Returns 0 on success, negative on failure

.. _`igb_update_stats`:

igb_update_stats
================

.. c:function:: void igb_update_stats(struct igb_adapter *adapter)

    Update the board statistics counters

    :param adapter:
        board private structure
    :type adapter: struct igb_adapter \*

.. _`igb_set_uta`:

igb_set_uta
===========

.. c:function:: void igb_set_uta(struct igb_adapter *adapter, bool set)

    Set unicast filter table address

    :param adapter:
        board private structure
    :type adapter: struct igb_adapter \*

    :param set:
        boolean indicating if we are setting or clearing bits
    :type set: bool

.. _`igb_set_uta.description`:

Description
-----------

The unicast table address is a register array of 32-bit registers.
The table is meant to be used in a way similar to how the MTA is used
however due to certain limitations in the hardware it is necessary to
set all the hash bits to 1 and use the VMOLR ROPE bit as a promiscuous
enable bit to allow vlan tag stripping when promiscuous mode is enabled

.. _`igb_intr_msi`:

igb_intr_msi
============

.. c:function:: irqreturn_t igb_intr_msi(int irq, void *data)

    Interrupt Handler

    :param irq:
        interrupt number
    :type irq: int

    :param data:
        pointer to a network interface device structure
    :type data: void \*

.. _`igb_intr`:

igb_intr
========

.. c:function:: irqreturn_t igb_intr(int irq, void *data)

    Legacy Interrupt Handler

    :param irq:
        interrupt number
    :type irq: int

    :param data:
        pointer to a network interface device structure
    :type data: void \*

.. _`igb_poll`:

igb_poll
========

.. c:function:: int igb_poll(struct napi_struct *napi, int budget)

    NAPI Rx polling callback

    :param napi:
        napi polling structure
    :type napi: struct napi_struct \*

    :param budget:
        count of how many packets we should handle
    :type budget: int

.. _`igb_clean_tx_irq`:

igb_clean_tx_irq
================

.. c:function:: bool igb_clean_tx_irq(struct igb_q_vector *q_vector, int napi_budget)

    Reclaim resources after transmit completes

    :param q_vector:
        pointer to q_vector containing needed info
    :type q_vector: struct igb_q_vector \*

    :param napi_budget:
        Used to determine if we are in netpoll
    :type napi_budget: int

.. _`igb_clean_tx_irq.description`:

Description
-----------

returns true if ring is completely cleaned

.. _`igb_reuse_rx_page`:

igb_reuse_rx_page
=================

.. c:function:: void igb_reuse_rx_page(struct igb_ring *rx_ring, struct igb_rx_buffer *old_buff)

    page flip buffer and store it back on the ring

    :param rx_ring:
        rx descriptor ring to store buffers on
    :type rx_ring: struct igb_ring \*

    :param old_buff:
        donor buffer to have page reused
    :type old_buff: struct igb_rx_buffer \*

.. _`igb_reuse_rx_page.description`:

Description
-----------

Synchronizes page for reuse by the adapter

.. _`igb_add_rx_frag`:

igb_add_rx_frag
===============

.. c:function:: void igb_add_rx_frag(struct igb_ring *rx_ring, struct igb_rx_buffer *rx_buffer, struct sk_buff *skb, unsigned int size)

    Add contents of Rx buffer to sk_buff

    :param rx_ring:
        rx descriptor ring to transact packets on
    :type rx_ring: struct igb_ring \*

    :param rx_buffer:
        buffer containing page to add
    :type rx_buffer: struct igb_rx_buffer \*

    :param skb:
        sk_buff to place the data into
    :type skb: struct sk_buff \*

    :param size:
        size of buffer to be added
    :type size: unsigned int

.. _`igb_add_rx_frag.description`:

Description
-----------

This function will add the data contained in rx_buffer->page to the skb.

.. _`igb_is_non_eop`:

igb_is_non_eop
==============

.. c:function:: bool igb_is_non_eop(struct igb_ring *rx_ring, union e1000_adv_rx_desc *rx_desc)

    process handling of non-EOP buffers

    :param rx_ring:
        Rx ring being processed
    :type rx_ring: struct igb_ring \*

    :param rx_desc:
        Rx descriptor for current buffer
    :type rx_desc: union e1000_adv_rx_desc \*

.. _`igb_is_non_eop.description`:

Description
-----------

This function updates next to clean.  If the buffer is an EOP buffer
this function exits returning false, otherwise it will place the
sk_buff in the next buffer to be chained and return true indicating
that this is in fact a non-EOP buffer.

.. _`igb_cleanup_headers`:

igb_cleanup_headers
===================

.. c:function:: bool igb_cleanup_headers(struct igb_ring *rx_ring, union e1000_adv_rx_desc *rx_desc, struct sk_buff *skb)

    Correct corrupted or empty headers

    :param rx_ring:
        rx descriptor ring packet is being transacted on
    :type rx_ring: struct igb_ring \*

    :param rx_desc:
        pointer to the EOP Rx descriptor
    :type rx_desc: union e1000_adv_rx_desc \*

    :param skb:
        pointer to current skb being fixed
    :type skb: struct sk_buff \*

.. _`igb_cleanup_headers.description`:

Description
-----------

Address the case where we are pulling data in on pages only
and as such no data is present in the skb header.

In addition if skb is not at least 60 bytes we need to pad it so that
it is large enough to qualify as a valid Ethernet frame.

Returns true if an error was encountered and skb was freed.

.. _`igb_process_skb_fields`:

igb_process_skb_fields
======================

.. c:function:: void igb_process_skb_fields(struct igb_ring *rx_ring, union e1000_adv_rx_desc *rx_desc, struct sk_buff *skb)

    Populate skb header fields from Rx descriptor

    :param rx_ring:
        rx descriptor ring packet is being transacted on
    :type rx_ring: struct igb_ring \*

    :param rx_desc:
        pointer to the EOP Rx descriptor
    :type rx_desc: union e1000_adv_rx_desc \*

    :param skb:
        pointer to current skb being populated
    :type skb: struct sk_buff \*

.. _`igb_process_skb_fields.description`:

Description
-----------

This function checks the ring, descriptor, and packet information in
order to populate the hash, checksum, VLAN, timestamp, protocol, and
other fields within the skb.

.. _`igb_alloc_rx_buffers`:

igb_alloc_rx_buffers
====================

.. c:function:: void igb_alloc_rx_buffers(struct igb_ring *rx_ring, u16 cleaned_count)

    Replace used receive buffers; packet split

    :param rx_ring:
        *undescribed*
    :type rx_ring: struct igb_ring \*

    :param cleaned_count:
        *undescribed*
    :type cleaned_count: u16

.. _`igb_mii_ioctl`:

igb_mii_ioctl
=============

.. c:function:: int igb_mii_ioctl(struct net_device *netdev, struct ifreq *ifr, int cmd)

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

    :param ifr:
        *undescribed*
    :type ifr: struct ifreq \*

    :param cmd:
        *undescribed*
    :type cmd: int

.. _`igb_ioctl`:

igb_ioctl
=========

.. c:function:: int igb_ioctl(struct net_device *netdev, struct ifreq *ifr, int cmd)

    :param netdev:
        *undescribed*
    :type netdev: struct net_device \*

    :param ifr:
        *undescribed*
    :type ifr: struct ifreq \*

    :param cmd:
        *undescribed*
    :type cmd: int

.. _`igb_io_error_detected`:

igb_io_error_detected
=====================

.. c:function:: pci_ers_result_t igb_io_error_detected(struct pci_dev *pdev, pci_channel_state_t state)

    called when PCI error is detected

    :param pdev:
        Pointer to PCI device
    :type pdev: struct pci_dev \*

    :param state:
        The current pci connection state
    :type state: pci_channel_state_t

.. _`igb_io_error_detected.description`:

Description
-----------

This function is called after a PCI bus error affecting
this device has been detected.

.. _`igb_io_slot_reset`:

igb_io_slot_reset
=================

.. c:function:: pci_ers_result_t igb_io_slot_reset(struct pci_dev *pdev)

    called after the pci bus has been reset.

    :param pdev:
        Pointer to PCI device
    :type pdev: struct pci_dev \*

.. _`igb_io_slot_reset.description`:

Description
-----------

Restart the card from scratch, as if from a cold-boot. Implementation
resembles the first-half of the igb_resume routine.

.. _`igb_io_resume`:

igb_io_resume
=============

.. c:function:: void igb_io_resume(struct pci_dev *pdev)

    called when traffic can start flowing again.

    :param pdev:
        Pointer to PCI device
    :type pdev: struct pci_dev \*

.. _`igb_io_resume.description`:

Description
-----------

This callback is called when the error recovery driver tells us that
its OK to resume normal operation. Implementation resembles the
second-half of the igb_resume routine.

.. _`igb_rar_set_index`:

igb_rar_set_index
=================

.. c:function:: void igb_rar_set_index(struct igb_adapter *adapter, u32 index)

    Sync RAL[index] and RAH[index] registers with MAC table

    :param adapter:
        Pointer to adapter structure
    :type adapter: struct igb_adapter \*

    :param index:
        Index of the RAR entry which need to be synced with MAC table
    :type index: u32

.. _`igb_read_i2c_byte`:

igb_read_i2c_byte
=================

.. c:function:: s32 igb_read_i2c_byte(struct e1000_hw *hw, u8 byte_offset, u8 dev_addr, u8 *data)

    Reads 8 bit word over I2C

    :param hw:
        pointer to hardware structure
    :type hw: struct e1000_hw \*

    :param byte_offset:
        byte offset to read
    :type byte_offset: u8

    :param dev_addr:
        device address
    :type dev_addr: u8

    :param data:
        value read
    :type data: u8 \*

.. _`igb_read_i2c_byte.description`:

Description
-----------

Performs byte read operation over I2C interface at
a specified device address.

.. _`igb_write_i2c_byte`:

igb_write_i2c_byte
==================

.. c:function:: s32 igb_write_i2c_byte(struct e1000_hw *hw, u8 byte_offset, u8 dev_addr, u8 data)

    Writes 8 bit word over I2C

    :param hw:
        pointer to hardware structure
    :type hw: struct e1000_hw \*

    :param byte_offset:
        byte offset to write
    :type byte_offset: u8

    :param dev_addr:
        device address
    :type dev_addr: u8

    :param data:
        value to write
    :type data: u8

.. _`igb_write_i2c_byte.description`:

Description
-----------

Performs byte write operation over I2C interface at
a specified device address.

.. This file was automatic generated / don't edit.


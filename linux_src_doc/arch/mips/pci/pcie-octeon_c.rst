.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/pci/pcie-octeon.c

.. _`cvmx_pcie_get_io_base_address`:

cvmx_pcie_get_io_base_address
=============================

.. c:function:: uint64_t cvmx_pcie_get_io_base_address(int pcie_port)

    read/written as an offset from this address.

    :param pcie_port:
        PCIe port the IO is for
    :type pcie_port: int

.. _`cvmx_pcie_get_io_base_address.description`:

Description
-----------

Returns 64bit Octeon IO base address for read/write

.. _`cvmx_pcie_get_io_size`:

cvmx_pcie_get_io_size
=====================

.. c:function:: uint64_t cvmx_pcie_get_io_size(int pcie_port)

    \ :c:func:`cvmx_pcie_get_io_base_address`\ 

    :param pcie_port:
        PCIe port the IO is for
    :type pcie_port: int

.. _`cvmx_pcie_get_io_size.description`:

Description
-----------

Returns Size of the IO window

.. _`cvmx_pcie_get_mem_base_address`:

cvmx_pcie_get_mem_base_address
==============================

.. c:function:: uint64_t cvmx_pcie_get_mem_base_address(int pcie_port)

    read/written as an offset from this address.

    :param pcie_port:
        PCIe port the IO is for
    :type pcie_port: int

.. _`cvmx_pcie_get_mem_base_address.description`:

Description
-----------

Returns 64bit Octeon IO base address for read/write

.. _`cvmx_pcie_get_mem_size`:

cvmx_pcie_get_mem_size
======================

.. c:function:: uint64_t cvmx_pcie_get_mem_size(int pcie_port)

    \ :c:func:`cvmx_pcie_get_mem_base_address`\ 

    :param pcie_port:
        PCIe port the IO is for
    :type pcie_port: int

.. _`cvmx_pcie_get_mem_size.description`:

Description
-----------

Returns Size of the Mem window

.. _`cvmx_pcie_cfgx_read`:

cvmx_pcie_cfgx_read
===================

.. c:function:: uint32_t cvmx_pcie_cfgx_read(int pcie_port, uint32_t cfg_offset)

    registers of the form PCIEEP_CFG??? and PCIERC?_CFG???.

    :param pcie_port:
        PCIe port to read from
    :type pcie_port: int

    :param cfg_offset:
        Address to read
    :type cfg_offset: uint32_t

.. _`cvmx_pcie_cfgx_read.description`:

Description
-----------

Returns Value read

.. _`cvmx_pcie_cfgx_write`:

cvmx_pcie_cfgx_write
====================

.. c:function:: void cvmx_pcie_cfgx_write(int pcie_port, uint32_t cfg_offset, uint32_t val)

    registers of the form PCIEEP_CFG??? and PCIERC?_CFG???.

    :param pcie_port:
        PCIe port to write to
    :type pcie_port: int

    :param cfg_offset:
        Address to write
    :type cfg_offset: uint32_t

    :param val:
        Value to write
    :type val: uint32_t

.. _`__cvmx_pcie_build_config_addr`:

\__cvmx_pcie_build_config_addr
==============================

.. c:function:: uint64_t __cvmx_pcie_build_config_addr(int pcie_port, int bus, int dev, int fn, int reg)

    :param pcie_port:
        PCIe port to access
    :type pcie_port: int

    :param bus:
        Sub bus
    :type bus: int

    :param dev:
        Device ID
    :type dev: int

    :param fn:
        Device sub function
    :type fn: int

    :param reg:
        Register to access
    :type reg: int

.. _`__cvmx_pcie_build_config_addr.description`:

Description
-----------

Returns 64bit Octeon IO address

.. _`cvmx_pcie_config_read8`:

cvmx_pcie_config_read8
======================

.. c:function:: uint8_t cvmx_pcie_config_read8(int pcie_port, int bus, int dev, int fn, int reg)

    :param pcie_port:
        PCIe port the device is on
    :type pcie_port: int

    :param bus:
        Sub bus
    :type bus: int

    :param dev:
        Device ID
    :type dev: int

    :param fn:
        Device sub function
    :type fn: int

    :param reg:
        Register to access
    :type reg: int

.. _`cvmx_pcie_config_read8.description`:

Description
-----------

Returns Result of the read

.. _`cvmx_pcie_config_read16`:

cvmx_pcie_config_read16
=======================

.. c:function:: uint16_t cvmx_pcie_config_read16(int pcie_port, int bus, int dev, int fn, int reg)

    :param pcie_port:
        PCIe port the device is on
    :type pcie_port: int

    :param bus:
        Sub bus
    :type bus: int

    :param dev:
        Device ID
    :type dev: int

    :param fn:
        Device sub function
    :type fn: int

    :param reg:
        Register to access
    :type reg: int

.. _`cvmx_pcie_config_read16.description`:

Description
-----------

Returns Result of the read

.. _`cvmx_pcie_config_read32`:

cvmx_pcie_config_read32
=======================

.. c:function:: uint32_t cvmx_pcie_config_read32(int pcie_port, int bus, int dev, int fn, int reg)

    :param pcie_port:
        PCIe port the device is on
    :type pcie_port: int

    :param bus:
        Sub bus
    :type bus: int

    :param dev:
        Device ID
    :type dev: int

    :param fn:
        Device sub function
    :type fn: int

    :param reg:
        Register to access
    :type reg: int

.. _`cvmx_pcie_config_read32.description`:

Description
-----------

Returns Result of the read

.. _`cvmx_pcie_config_write8`:

cvmx_pcie_config_write8
=======================

.. c:function:: void cvmx_pcie_config_write8(int pcie_port, int bus, int dev, int fn, int reg, uint8_t val)

    :param pcie_port:
        PCIe port the device is on
    :type pcie_port: int

    :param bus:
        Sub bus
    :type bus: int

    :param dev:
        Device ID
    :type dev: int

    :param fn:
        Device sub function
    :type fn: int

    :param reg:
        Register to access
    :type reg: int

    :param val:
        Value to write
    :type val: uint8_t

.. _`cvmx_pcie_config_write16`:

cvmx_pcie_config_write16
========================

.. c:function:: void cvmx_pcie_config_write16(int pcie_port, int bus, int dev, int fn, int reg, uint16_t val)

    :param pcie_port:
        PCIe port the device is on
    :type pcie_port: int

    :param bus:
        Sub bus
    :type bus: int

    :param dev:
        Device ID
    :type dev: int

    :param fn:
        Device sub function
    :type fn: int

    :param reg:
        Register to access
    :type reg: int

    :param val:
        Value to write
    :type val: uint16_t

.. _`cvmx_pcie_config_write32`:

cvmx_pcie_config_write32
========================

.. c:function:: void cvmx_pcie_config_write32(int pcie_port, int bus, int dev, int fn, int reg, uint32_t val)

    :param pcie_port:
        PCIe port the device is on
    :type pcie_port: int

    :param bus:
        Sub bus
    :type bus: int

    :param dev:
        Device ID
    :type dev: int

    :param fn:
        Device sub function
    :type fn: int

    :param reg:
        Register to access
    :type reg: int

    :param val:
        Value to write
    :type val: uint32_t

.. _`__cvmx_pcie_rc_initialize_config_space`:

\__cvmx_pcie_rc_initialize_config_space
=======================================

.. c:function:: void __cvmx_pcie_rc_initialize_config_space(int pcie_port)

    :param pcie_port:
        PCIe port to initialize
    :type pcie_port: int

.. _`__cvmx_pcie_rc_initialize_link_gen1`:

\__cvmx_pcie_rc_initialize_link_gen1
====================================

.. c:function:: int __cvmx_pcie_rc_initialize_link_gen1(int pcie_port)

    port from reset to a link up state. Software can then begin configuring the rest of the link.

    :param pcie_port:
        PCIe port to initialize
    :type pcie_port: int

.. _`__cvmx_pcie_rc_initialize_link_gen1.description`:

Description
-----------

Returns Zero on success

.. _`__cvmx_pcie_rc_initialize_gen1`:

\__cvmx_pcie_rc_initialize_gen1
===============================

.. c:function:: int __cvmx_pcie_rc_initialize_gen1(int pcie_port)

    enumerate the bus.

    :param pcie_port:
        PCIe port to initialize
    :type pcie_port: int

.. _`__cvmx_pcie_rc_initialize_gen1.description`:

Description
-----------

Returns Zero on success

.. _`__cvmx_pcie_rc_initialize_link_gen2`:

\__cvmx_pcie_rc_initialize_link_gen2
====================================

.. c:function:: int __cvmx_pcie_rc_initialize_link_gen2(int pcie_port)

    port from reset to a link up state. Software can then begin configuring the rest of the link.

    :param pcie_port:
        PCIe port to initialize
    :type pcie_port: int

.. _`__cvmx_pcie_rc_initialize_link_gen2.description`:

Description
-----------

Return Zero on success.

.. _`__cvmx_pcie_rc_initialize_gen2`:

\__cvmx_pcie_rc_initialize_gen2
===============================

.. c:function:: int __cvmx_pcie_rc_initialize_gen2(int pcie_port)

    the bus.

    :param pcie_port:
        PCIe port to initialize
    :type pcie_port: int

.. _`__cvmx_pcie_rc_initialize_gen2.description`:

Description
-----------

Returns Zero on success.

.. _`cvmx_pcie_rc_initialize`:

cvmx_pcie_rc_initialize
=======================

.. c:function:: int cvmx_pcie_rc_initialize(int pcie_port)

    :param pcie_port:
        PCIe port to initialize
    :type pcie_port: int

.. _`cvmx_pcie_rc_initialize.description`:

Description
-----------

Returns Zero on success

.. _`octeon_pcie_pcibios_map_irq`:

octeon_pcie_pcibios_map_irq
===========================

.. c:function:: int octeon_pcie_pcibios_map_irq(const struct pci_dev *dev, u8 slot, u8 pin)

    :param dev:
        The Linux PCI device structure for the device to map
    :type dev: const struct pci_dev \*

    :param slot:
        The slot number for this device on \__BUS 0__. Linux
        enumerates through all the bridges and figures out the
        slot on Bus 0 where this device eventually hooks to.
    :type slot: u8

    :param pin:
        The PCI interrupt pin read from the device, then swizzled
        as it goes through each bridge.
        Returns Interrupt number for the device
    :type pin: u8

.. _`octeon_pcie_setup`:

octeon_pcie_setup
=================

.. c:function:: int octeon_pcie_setup( void)

    :param void:
        no arguments
    :type void: 

.. _`octeon_pcie_setup.description`:

Description
-----------

Returns

.. This file was automatic generated / don't edit.


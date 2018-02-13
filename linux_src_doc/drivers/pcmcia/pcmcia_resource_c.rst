.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pcmcia/pcmcia_resource.c

.. _`release_io_space`:

release_io_space
================

.. c:function:: void release_io_space(struct pcmcia_socket *s, struct resource *res)

    release IO ports allocated with \ :c:func:`alloc_io_space`\ 

    :param struct pcmcia_socket \*s:
        pcmcia socket

    :param struct resource \*res:
        resource to release

.. _`alloc_io_space`:

alloc_io_space
==============

.. c:function:: int alloc_io_space(struct pcmcia_socket *s, struct resource *res, unsigned int lines)

    allocate IO ports for use by a PCMCIA device

    :param struct pcmcia_socket \*s:
        pcmcia socket

    :param struct resource \*res:
        resource to allocate (begin: begin, end: size)

    :param unsigned int lines:
        number of IO lines decoded by the PCMCIA card

.. _`alloc_io_space.description`:

Description
-----------

Special stuff for managing IO windows, because they are scarce

.. _`pcmcia_access_config`:

pcmcia_access_config
====================

.. c:function:: int pcmcia_access_config(struct pcmcia_device *p_dev, off_t where, u8 *val, int (*accessf)(struct pcmcia_socket *s, int attr, unsigned int addr, unsigned int len, void *ptr))

    read or write card configuration registers

    :param struct pcmcia_device \*p_dev:
        *undescribed*

    :param off_t where:
        *undescribed*

    :param u8 \*val:
        *undescribed*

    :param int (\*accessf)(struct pcmcia_socket \*s, int attr, unsigned int addr, unsigned int len, void \*ptr):
        *undescribed*

.. _`pcmcia_access_config.description`:

Description
-----------

\ :c:func:`pcmcia_access_config`\  reads and writes configuration registers in
attribute memory.  Memory window 0 is reserved for this and the tuple
reading services. Drivers must use \ :c:func:`pcmcia_read_config_byte`\  or
\ :c:func:`pcmcia_write_config_byte`\ .

.. _`pcmcia_read_config_byte`:

pcmcia_read_config_byte
=======================

.. c:function:: int pcmcia_read_config_byte(struct pcmcia_device *p_dev, off_t where, u8 *val)

    read a byte from a card configuration register

    :param struct pcmcia_device \*p_dev:
        *undescribed*

    :param off_t where:
        *undescribed*

    :param u8 \*val:
        *undescribed*

.. _`pcmcia_read_config_byte.description`:

Description
-----------

\ :c:func:`pcmcia_read_config_byte`\  reads a byte from a configuration register in
attribute memory.

.. _`pcmcia_write_config_byte`:

pcmcia_write_config_byte
========================

.. c:function:: int pcmcia_write_config_byte(struct pcmcia_device *p_dev, off_t where, u8 val)

    write a byte to a card configuration register

    :param struct pcmcia_device \*p_dev:
        *undescribed*

    :param off_t where:
        *undescribed*

    :param u8 val:
        *undescribed*

.. _`pcmcia_write_config_byte.description`:

Description
-----------

\ :c:func:`pcmcia_write_config_byte`\  writes a byte to a configuration register in
attribute memory.

.. _`pcmcia_map_mem_page`:

pcmcia_map_mem_page
===================

.. c:function:: int pcmcia_map_mem_page(struct pcmcia_device *p_dev, struct resource *res, unsigned int offset)

    modify iomem window to point to a different offset

    :param struct pcmcia_device \*p_dev:
        pcmcia device

    :param struct resource \*res:
        iomem resource already enabled by \ :c:func:`pcmcia_request_window`\ 

    :param unsigned int offset:
        card_offset to map

.. _`pcmcia_map_mem_page.description`:

Description
-----------

\ :c:func:`pcmcia_map_mem_page`\  modifies what can be read and written by accessing
an iomem range previously enabled by \ :c:func:`pcmcia_request_window`\ , by setting
the card_offset value to \ ``offset``\ .

.. _`pcmcia_fixup_iowidth`:

pcmcia_fixup_iowidth
====================

.. c:function:: int pcmcia_fixup_iowidth(struct pcmcia_device *p_dev)

    reduce io width to 8bit

    :param struct pcmcia_device \*p_dev:
        pcmcia device

.. _`pcmcia_fixup_iowidth.description`:

Description
-----------

\ :c:func:`pcmcia_fixup_iowidth`\  allows a PCMCIA device driver to reduce the
IO width to 8bit after having called \ :c:func:`pcmcia_enable_device`\ 
previously.

.. _`pcmcia_fixup_vpp`:

pcmcia_fixup_vpp
================

.. c:function:: int pcmcia_fixup_vpp(struct pcmcia_device *p_dev, unsigned char new_vpp)

    set Vpp to a new voltage level

    :param struct pcmcia_device \*p_dev:
        pcmcia device

    :param unsigned char new_vpp:
        new Vpp voltage

.. _`pcmcia_fixup_vpp.description`:

Description
-----------

\ :c:func:`pcmcia_fixup_vpp`\  allows a PCMCIA device driver to set Vpp to
a new voltage level between calls to \ :c:func:`pcmcia_enable_device`\ 
and \ :c:func:`pcmcia_disable_device`\ .

.. _`pcmcia_release_configuration`:

pcmcia_release_configuration
============================

.. c:function:: int pcmcia_release_configuration(struct pcmcia_device *p_dev)

    physically disable a PCMCIA device

    :param struct pcmcia_device \*p_dev:
        pcmcia device

.. _`pcmcia_release_configuration.description`:

Description
-----------

\ :c:func:`pcmcia_release_configuration`\  is the 1:1 counterpart to
\ :c:func:`pcmcia_enable_device`\ : If a PCMCIA device is no longer used by any
driver, the Vpp voltage is set to 0, IRQs will no longer be generated,
and I/O ranges will be disabled. As \ :c:func:`pcmcia_release_io`\  and
\ :c:func:`pcmcia_release_window`\  still need to be called, device drivers are
expected to call \ :c:func:`pcmcia_disable_device`\  instead.

.. _`pcmcia_release_io`:

pcmcia_release_io
=================

.. c:function:: int pcmcia_release_io(struct pcmcia_device *p_dev)

    release I/O allocated by a PCMCIA device

    :param struct pcmcia_device \*p_dev:
        pcmcia device

.. _`pcmcia_release_io.description`:

Description
-----------

\ :c:func:`pcmcia_release_io`\  releases the I/O ranges allocated by a PCMCIA
device.  This may be invoked some time after a card ejection has
already dumped the actual socket configuration, so if the client is
"stale", we don't bother checking the port ranges against the
current socket values.

.. _`pcmcia_release_window`:

pcmcia_release_window
=====================

.. c:function:: int pcmcia_release_window(struct pcmcia_device *p_dev, struct resource *res)

    release reserved iomem for PCMCIA devices

    :param struct pcmcia_device \*p_dev:
        pcmcia device

    :param struct resource \*res:
        iomem resource to release

.. _`pcmcia_release_window.description`:

Description
-----------

\ :c:func:`pcmcia_release_window`\  releases \ :c:type:`struct resource <resource>`\  \*res which was
previously reserved by calling \ :c:func:`pcmcia_request_window`\ .

.. _`pcmcia_enable_device`:

pcmcia_enable_device
====================

.. c:function:: int pcmcia_enable_device(struct pcmcia_device *p_dev)

    set up and activate a PCMCIA device

    :param struct pcmcia_device \*p_dev:
        the associated PCMCIA device

.. _`pcmcia_enable_device.description`:

Description
-----------

\ :c:func:`pcmcia_enable_device`\  physically enables a PCMCIA device. It parses
the flags passed to in \ ``flags``\  and stored in \ ``p_dev``\ ->flags and sets up
the Vpp voltage, enables the speaker line, I/O ports and store proper
values to configuration registers.

.. _`pcmcia_request_io`:

pcmcia_request_io
=================

.. c:function:: int pcmcia_request_io(struct pcmcia_device *p_dev)

    attempt to reserve port ranges for PCMCIA devices

    :param struct pcmcia_device \*p_dev:
        the associated PCMCIA device

.. _`pcmcia_request_io.description`:

Description
-----------

\ :c:func:`pcmcia_request_io`\  attempts to reserve the IO port ranges specified in
\ :c:type:`struct pcmcia_device <pcmcia_device>`\  \ ``p_dev``\ ->resource[0] and \ ``p_dev``\ ->resource[1]. The
"start" value is the requested start of the IO port resource; "end"
reflects the number of ports requested. The number of IO lines requested
is specified in \ :c:type:`struct pcmcia_device <pcmcia_device>`\  \ ``p_dev``\ ->io_lines.

.. _`pcmcia_request_irq`:

pcmcia_request_irq
==================

.. c:function:: int pcmcia_request_irq(struct pcmcia_device *p_dev, irq_handler_t handler)

    attempt to request a IRQ for a PCMCIA device

    :param struct pcmcia_device \*p_dev:
        the associated PCMCIA device

    :param irq_handler_t handler:
        IRQ handler to register

.. _`pcmcia_request_irq.description`:

Description
-----------

\ :c:func:`pcmcia_request_irq`\  is a wrapper around \ :c:func:`request_irq`\  which allows
the PCMCIA core to clean up the registration in \ :c:func:`pcmcia_disable_device`\ .
Drivers are free to use \ :c:func:`request_irq`\  directly, but then they need to
call \ :c:func:`free_irq`\  themselfves, too. Also, only \ ``IRQF_SHARED``\  capable IRQ
handlers are allowed.

.. _`__pcmcia_request_exclusive_irq`:

\__pcmcia_request_exclusive_irq
===============================

.. c:function:: int __pcmcia_request_exclusive_irq(struct pcmcia_device *p_dev, irq_handler_t handler)

    attempt to request an exclusive IRQ first

    :param struct pcmcia_device \*p_dev:
        the associated PCMCIA device

    :param irq_handler_t handler:
        IRQ handler to register

.. _`__pcmcia_request_exclusive_irq.description`:

Description
-----------

\ :c:func:`pcmcia_request_exclusive_irq`\  is a wrapper around \ :c:func:`request_irq`\  which
attempts first to request an exclusive IRQ. If it fails, it also accepts
a shared IRQ, but prints out a warning. PCMCIA drivers should allow for
IRQ sharing and either use request_irq directly (then they need to call
\ :c:func:`free_irq`\  themselves, too), or the \ :c:func:`pcmcia_request_irq`\  function.

.. _`pcmcia_setup_isa_irq`:

pcmcia_setup_isa_irq
====================

.. c:function:: int pcmcia_setup_isa_irq(struct pcmcia_device *p_dev, int type)

    determine whether an ISA IRQ can be used \ ``p_dev``\  - the associated PCMCIA device

    :param struct pcmcia_device \*p_dev:
        *undescribed*

    :param int type:
        *undescribed*

.. _`pcmcia_setup_isa_irq.locking-note`:

locking note
------------

must be called with ops_mutex locked.

.. _`pcmcia_setup_irq`:

pcmcia_setup_irq
================

.. c:function:: int pcmcia_setup_irq(struct pcmcia_device *p_dev)

    determine IRQ to be used for device \ ``p_dev``\  - the associated PCMCIA device

    :param struct pcmcia_device \*p_dev:
        *undescribed*

.. _`pcmcia_setup_irq.locking-note`:

locking note
------------

must be called with ops_mutex locked.

.. _`pcmcia_request_window`:

pcmcia_request_window
=====================

.. c:function:: int pcmcia_request_window(struct pcmcia_device *p_dev, struct resource *res, unsigned int speed)

    attempt to reserve iomem for PCMCIA devices

    :param struct pcmcia_device \*p_dev:
        the associated PCMCIA device

    :param struct resource \*res:
        \ :c:type:`struct resource <resource>`\  pointing to p_dev->resource[2..5]

    :param unsigned int speed:
        access speed

.. _`pcmcia_request_window.description`:

Description
-----------

\ :c:func:`pcmcia_request_window`\  attepts to reserve an iomem ranges specified in
\ :c:type:`struct resource <resource>`\  \ ``res``\  pointing to one of the entries in
\ :c:type:`struct pcmcia_device <pcmcia_device>`\  \ ``p_dev``\ ->resource[2..5]. The "start" value is the
requested start of the IO mem resource; "end" reflects the size
requested.

.. _`pcmcia_disable_device`:

pcmcia_disable_device
=====================

.. c:function:: void pcmcia_disable_device(struct pcmcia_device *p_dev)

    disable and clean up a PCMCIA device

    :param struct pcmcia_device \*p_dev:
        the associated PCMCIA device

.. _`pcmcia_disable_device.description`:

Description
-----------

\ :c:func:`pcmcia_disable_device`\  is the driver-callable counterpart to
\ :c:func:`pcmcia_enable_device`\ : If a PCMCIA device is no longer used,
drivers are expected to clean up and disable the device by calling
this function. Any I/O ranges (iomem and ioports) will be released,
the Vpp voltage will be set to 0, and IRQs will no longer be
generated -- at least if there is no other card function (of
multifunction devices) being used.

.. This file was automatic generated / don't edit.


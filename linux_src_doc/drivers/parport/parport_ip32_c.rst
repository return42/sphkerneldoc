.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/parport/parport_ip32.c

.. _`parport_ip32_regs`:

struct parport_ip32_regs
========================

.. c:type:: struct parport_ip32_regs

    virtual addresses of parallel port registers

.. _`parport_ip32_regs.definition`:

Definition
----------

.. code-block:: c

    struct parport_ip32_regs {
        void __iomem *data;
        void __iomem *dsr;
        void __iomem *dcr;
        void __iomem *eppAddr;
        void __iomem *eppData0;
        void __iomem *eppData1;
        void __iomem *eppData2;
        void __iomem *eppData3;
        void __iomem *ecpAFifo;
        void __iomem *fifo;
        void __iomem *cnfgA;
        void __iomem *cnfgB;
        void __iomem *ecr;
    }

.. _`parport_ip32_regs.members`:

Members
-------

data
    Data Register

dsr
    Device Status Register

dcr
    Device Control Register

eppAddr
    EPP Address Register

eppData0
    EPP Data Register 0

eppData1
    EPP Data Register 1

eppData2
    EPP Data Register 2

eppData3
    EPP Data Register 3

ecpAFifo
    ECP Address FIFO

fifo
    General FIFO register.  The same address is used for:
    - cFifo, the Parallel Port DATA FIFO
    - ecpDFifo, the ECP Data FIFO
    - tFifo, the ECP Test FIFO

cnfgA
    Configuration Register A

cnfgB
    Configuration Register B

ecr
    Extended Control Register

.. _`parport_ip32_irq_mode`:

enum parport_ip32_irq_mode
==========================

.. c:type:: enum parport_ip32_irq_mode

    operation mode of interrupt handler

.. _`parport_ip32_irq_mode.definition`:

Definition
----------

.. code-block:: c

    enum parport_ip32_irq_mode {
        PARPORT_IP32_IRQ_FWD,
        PARPORT_IP32_IRQ_HERE
    };

.. _`parport_ip32_irq_mode.constants`:

Constants
---------

PARPORT_IP32_IRQ_FWD
    forward interrupt to the upper parport layer

PARPORT_IP32_IRQ_HERE
    interrupt is handled locally

.. _`parport_ip32_private`:

struct parport_ip32_private
===========================

.. c:type:: struct parport_ip32_private

    private stuff for \ :c:type:`struct parport <parport>`\ 

.. _`parport_ip32_private.definition`:

Definition
----------

.. code-block:: c

    struct parport_ip32_private {
        struct parport_ip32_regs regs;
        unsigned int dcr_cache;
        unsigned int dcr_writable;
        unsigned int pword;
        unsigned int fifo_depth;
        unsigned int readIntrThreshold;
        unsigned int writeIntrThreshold;
        enum parport_ip32_irq_mode irq_mode;
        struct completion irq_complete;
    }

.. _`parport_ip32_private.members`:

Members
-------

regs
    register addresses

dcr_cache
    cached contents of DCR

dcr_writable
    bit mask of writable DCR bits

pword
    number of bytes per PWord

fifo_depth
    number of PWords that FIFO will hold

readIntrThreshold
    minimum number of PWords we can read
    if we get an interrupt

writeIntrThreshold
    minimum number of PWords we can write
    if we get an interrupt

irq_mode
    operation mode of interrupt handler for this port

irq_complete
    mutex used to wait for an interrupt to occur

.. _`parport_ip32_dma_data`:

struct parport_ip32_dma_data
============================

.. c:type:: struct parport_ip32_dma_data

    private data needed for DMA operation

.. _`parport_ip32_dma_data.definition`:

Definition
----------

.. code-block:: c

    struct parport_ip32_dma_data {
        enum dma_data_direction dir;
        dma_addr_t buf;
        dma_addr_t next;
        size_t len;
        size_t left;
        unsigned int ctx;
        unsigned int irq_on;
        spinlock_t lock;
    }

.. _`parport_ip32_dma_data.members`:

Members
-------

dir
    DMA direction (from or to device)

buf
    buffer physical address

next
    address of next bytes to DMA transfer

len
    buffer length

left
    number of bytes remaining

ctx
    next context to write (0: context_a; 1: context_b)

irq_on
    are the DMA IRQs currently enabled?

lock
    spinlock to protect access to the structure

.. _`parport_ip32_dma_setup_context`:

parport_ip32_dma_setup_context
==============================

.. c:function:: void parport_ip32_dma_setup_context(unsigned int limit)

    setup next DMA context

    :param limit:
        maximum data size for the context
    :type limit: unsigned int

.. _`parport_ip32_dma_setup_context.description`:

Description
-----------

The alignment constraints must be verified in caller function, and the
parameter \ ``limit``\  must be set accordingly.

.. _`parport_ip32_dma_interrupt`:

parport_ip32_dma_interrupt
==========================

.. c:function:: irqreturn_t parport_ip32_dma_interrupt(int irq, void *dev_id)

    DMA interrupt handler

    :param irq:
        interrupt number
    :type irq: int

    :param dev_id:
        unused
    :type dev_id: void \*

.. _`parport_ip32_dma_start`:

parport_ip32_dma_start
======================

.. c:function:: int parport_ip32_dma_start(enum dma_data_direction dir, void *addr, size_t count)

    begins a DMA transfer

    :param dir:
        DMA direction: DMA_TO_DEVICE or DMA_FROM_DEVICE
    :type dir: enum dma_data_direction

    :param addr:
        pointer to data buffer
    :type addr: void \*

    :param count:
        buffer size
    :type count: size_t

.. _`parport_ip32_dma_start.description`:

Description
-----------

Calls to \ :c:func:`parport_ip32_dma_start`\  and \ :c:func:`parport_ip32_dma_stop`\  must be
correctly balanced.

.. _`parport_ip32_dma_stop`:

parport_ip32_dma_stop
=====================

.. c:function:: void parport_ip32_dma_stop( void)

    ends a running DMA transfer

    :param void:
        no arguments
    :type void: 

.. _`parport_ip32_dma_stop.description`:

Description
-----------

Calls to \ :c:func:`parport_ip32_dma_start`\  and \ :c:func:`parport_ip32_dma_stop`\  must be
correctly balanced.

.. _`parport_ip32_dma_get_residue`:

parport_ip32_dma_get_residue
============================

.. c:function:: size_t parport_ip32_dma_get_residue( void)

    get residue from last DMA transfer

    :param void:
        no arguments
    :type void: 

.. _`parport_ip32_dma_get_residue.description`:

Description
-----------

Returns the number of bytes remaining from last DMA transfer.

.. _`parport_ip32_dma_register`:

parport_ip32_dma_register
=========================

.. c:function:: int parport_ip32_dma_register( void)

    initialize DMA engine

    :param void:
        no arguments
    :type void: 

.. _`parport_ip32_dma_register.description`:

Description
-----------

Returns zero for success.

.. _`parport_ip32_dma_unregister`:

parport_ip32_dma_unregister
===========================

.. c:function:: void parport_ip32_dma_unregister( void)

    release and free resources for DMA engine

    :param void:
        no arguments
    :type void: 

.. _`parport_ip32_wakeup`:

parport_ip32_wakeup
===================

.. c:function:: void parport_ip32_wakeup(struct parport *p)

    wakes up code waiting for an interrupt

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

.. _`parport_ip32_interrupt`:

parport_ip32_interrupt
======================

.. c:function:: irqreturn_t parport_ip32_interrupt(int irq, void *dev_id)

    interrupt handler

    :param irq:
        interrupt number
    :type irq: int

    :param dev_id:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type dev_id: void \*

.. _`parport_ip32_interrupt.description`:

Description
-----------

Caught interrupts are forwarded to the upper parport layer if IRQ_mode is
\ ``PARPORT_IP32_IRQ_FWD``\ .

.. _`parport_ip32_read_econtrol`:

parport_ip32_read_econtrol
==========================

.. c:function:: unsigned int parport_ip32_read_econtrol(struct parport *p)

    read contents of the ECR register

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

.. _`parport_ip32_write_econtrol`:

parport_ip32_write_econtrol
===========================

.. c:function:: void parport_ip32_write_econtrol(struct parport *p, unsigned int c)

    write new contents to the ECR register

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

    :param c:
        new value to write
    :type c: unsigned int

.. _`parport_ip32_frob_econtrol`:

parport_ip32_frob_econtrol
==========================

.. c:function:: void parport_ip32_frob_econtrol(struct parport *p, unsigned int mask, unsigned int val)

    change bits from the ECR register

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

    :param mask:
        bit mask of bits to change
    :type mask: unsigned int

    :param val:
        new value for changed bits
    :type val: unsigned int

.. _`parport_ip32_frob_econtrol.description`:

Description
-----------

Read from the ECR, mask out the bits in \ ``mask``\ , exclusive-or with the bits
in \ ``val``\ , and write the result to the ECR.

.. _`parport_ip32_set_mode`:

parport_ip32_set_mode
=====================

.. c:function:: void parport_ip32_set_mode(struct parport *p, unsigned int mode)

    change mode of ECP port

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

    :param mode:
        new mode to write in ECR
    :type mode: unsigned int

.. _`parport_ip32_set_mode.description`:

Description
-----------

ECR is reset in a sane state (interrupts and DMA disabled), and placed in
mode \ ``mode``\ .  Go through PS2 mode if needed.

.. _`parport_ip32_read_data`:

parport_ip32_read_data
======================

.. c:function:: unsigned char parport_ip32_read_data(struct parport *p)

    return current contents of the DATA register

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

.. _`parport_ip32_write_data`:

parport_ip32_write_data
=======================

.. c:function:: void parport_ip32_write_data(struct parport *p, unsigned char d)

    set new contents for the DATA register

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

    :param d:
        new value to write
    :type d: unsigned char

.. _`parport_ip32_read_status`:

parport_ip32_read_status
========================

.. c:function:: unsigned char parport_ip32_read_status(struct parport *p)

    return current contents of the DSR register

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

.. _`__parport_ip32_read_control`:

\__parport_ip32_read_control
============================

.. c:function:: unsigned int __parport_ip32_read_control(struct parport *p)

    return cached contents of the DCR register

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

.. _`__parport_ip32_write_control`:

\__parport_ip32_write_control
=============================

.. c:function:: void __parport_ip32_write_control(struct parport *p, unsigned int c)

    set new contents for the DCR register

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

    :param c:
        new value to write
    :type c: unsigned int

.. _`__parport_ip32_frob_control`:

\__parport_ip32_frob_control
============================

.. c:function:: void __parport_ip32_frob_control(struct parport *p, unsigned int mask, unsigned int val)

    change bits from the DCR register

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

    :param mask:
        bit mask of bits to change
    :type mask: unsigned int

    :param val:
        new value for changed bits
    :type val: unsigned int

.. _`__parport_ip32_frob_control.description`:

Description
-----------

This is equivalent to read from the DCR, mask out the bits in \ ``mask``\ ,
exclusive-or with the bits in \ ``val``\ , and write the result to the DCR.
Actually, the cached contents of the DCR is used.

.. _`parport_ip32_read_control`:

parport_ip32_read_control
=========================

.. c:function:: unsigned char parport_ip32_read_control(struct parport *p)

    return cached contents of the DCR register

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

.. _`parport_ip32_read_control.description`:

Description
-----------

The return value is masked so as to only return the value of \ ``DCR_STROBE``\ ,
\ ``DCR_AUTOFD``\ , \ ``DCR_nINIT``\ , and \ ``DCR_SELECT``\ .

.. _`parport_ip32_write_control`:

parport_ip32_write_control
==========================

.. c:function:: void parport_ip32_write_control(struct parport *p, unsigned char c)

    set new contents for the DCR register

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

    :param c:
        new value to write
    :type c: unsigned char

.. _`parport_ip32_write_control.description`:

Description
-----------

The value is masked so as to only change the value of \ ``DCR_STROBE``\ ,
\ ``DCR_AUTOFD``\ , \ ``DCR_nINIT``\ , and \ ``DCR_SELECT``\ .

.. _`parport_ip32_frob_control`:

parport_ip32_frob_control
=========================

.. c:function:: unsigned char parport_ip32_frob_control(struct parport *p, unsigned char mask, unsigned char val)

    change bits from the DCR register

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

    :param mask:
        bit mask of bits to change
    :type mask: unsigned char

    :param val:
        new value for changed bits
    :type val: unsigned char

.. _`parport_ip32_frob_control.description`:

Description
-----------

This differs from \__parport_ip32_frob_control() in that it only allows to
change the value of \ ``DCR_STROBE``\ , \ ``DCR_AUTOFD``\ , \ ``DCR_nINIT``\ , and \ ``DCR_SELECT``\ .

.. _`parport_ip32_disable_irq`:

parport_ip32_disable_irq
========================

.. c:function:: void parport_ip32_disable_irq(struct parport *p)

    disable interrupts on the rising edge of nACK

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

.. _`parport_ip32_enable_irq`:

parport_ip32_enable_irq
=======================

.. c:function:: void parport_ip32_enable_irq(struct parport *p)

    enable interrupts on the rising edge of nACK

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

.. _`parport_ip32_data_forward`:

parport_ip32_data_forward
=========================

.. c:function:: void parport_ip32_data_forward(struct parport *p)

    enable host-to-peripheral communications

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

.. _`parport_ip32_data_forward.description`:

Description
-----------

Enable the data line drivers, for 8-bit host-to-peripheral communications.

.. _`parport_ip32_data_reverse`:

parport_ip32_data_reverse
=========================

.. c:function:: void parport_ip32_data_reverse(struct parport *p)

    enable peripheral-to-host communications

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

.. _`parport_ip32_data_reverse.description`:

Description
-----------

Place the data bus in a high impedance state, if \ ``p->modes``\  has the
PARPORT_MODE_TRISTATE bit set.

.. _`parport_ip32_init_state`:

parport_ip32_init_state
=======================

.. c:function:: void parport_ip32_init_state(struct pardevice *dev, struct parport_state *s)

    for core parport code

    :param dev:
        pointer to \ :c:type:`struct pardevice <pardevice>`\ 
    :type dev: struct pardevice \*

    :param s:
        pointer to \ :c:type:`struct parport_state <parport_state>`\  to initialize
    :type s: struct parport_state \*

.. _`parport_ip32_save_state`:

parport_ip32_save_state
=======================

.. c:function:: void parport_ip32_save_state(struct parport *p, struct parport_state *s)

    for core parport code

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

    :param s:
        pointer to \ :c:type:`struct parport_state <parport_state>`\  to save state to
    :type s: struct parport_state \*

.. _`parport_ip32_restore_state`:

parport_ip32_restore_state
==========================

.. c:function:: void parport_ip32_restore_state(struct parport *p, struct parport_state *s)

    for core parport code

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

    :param s:
        pointer to \ :c:type:`struct parport_state <parport_state>`\  to restore state from
    :type s: struct parport_state \*

.. _`parport_ip32_clear_epp_timeout`:

parport_ip32_clear_epp_timeout
==============================

.. c:function:: unsigned int parport_ip32_clear_epp_timeout(struct parport *p)

    clear Timeout bit in EPP mode

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

.. _`parport_ip32_clear_epp_timeout.description`:

Description
-----------

Returns 1 if the Timeout bit is clear, and 0 otherwise.

.. _`parport_ip32_epp_read`:

parport_ip32_epp_read
=====================

.. c:function:: size_t parport_ip32_epp_read(void __iomem *eppreg, struct parport *p, void *buf, size_t len, int flags)

    generic EPP read function

    :param eppreg:
        I/O register to read from
    :type eppreg: void __iomem \*

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

    :param buf:
        buffer to store read data
    :type buf: void \*

    :param len:
        length of buffer \ ``buf``\ 
    :type len: size_t

    :param flags:
        may be PARPORT_EPP_FAST
    :type flags: int

.. _`parport_ip32_epp_write`:

parport_ip32_epp_write
======================

.. c:function:: size_t parport_ip32_epp_write(void __iomem *eppreg, struct parport *p, const void *buf, size_t len, int flags)

    generic EPP write function

    :param eppreg:
        I/O register to write to
    :type eppreg: void __iomem \*

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

    :param buf:
        buffer of data to write
    :type buf: const void \*

    :param len:
        length of buffer \ ``buf``\ 
    :type len: size_t

    :param flags:
        may be PARPORT_EPP_FAST
    :type flags: int

.. _`parport_ip32_epp_read_data`:

parport_ip32_epp_read_data
==========================

.. c:function:: size_t parport_ip32_epp_read_data(struct parport *p, void *buf, size_t len, int flags)

    read a block of data in EPP mode

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

    :param buf:
        buffer to store read data
    :type buf: void \*

    :param len:
        length of buffer \ ``buf``\ 
    :type len: size_t

    :param flags:
        may be PARPORT_EPP_FAST
    :type flags: int

.. _`parport_ip32_epp_write_data`:

parport_ip32_epp_write_data
===========================

.. c:function:: size_t parport_ip32_epp_write_data(struct parport *p, const void *buf, size_t len, int flags)

    write a block of data in EPP mode

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

    :param buf:
        buffer of data to write
    :type buf: const void \*

    :param len:
        length of buffer \ ``buf``\ 
    :type len: size_t

    :param flags:
        may be PARPORT_EPP_FAST
    :type flags: int

.. _`parport_ip32_epp_read_addr`:

parport_ip32_epp_read_addr
==========================

.. c:function:: size_t parport_ip32_epp_read_addr(struct parport *p, void *buf, size_t len, int flags)

    read a block of addresses in EPP mode

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

    :param buf:
        buffer to store read data
    :type buf: void \*

    :param len:
        length of buffer \ ``buf``\ 
    :type len: size_t

    :param flags:
        may be PARPORT_EPP_FAST
    :type flags: int

.. _`parport_ip32_epp_write_addr`:

parport_ip32_epp_write_addr
===========================

.. c:function:: size_t parport_ip32_epp_write_addr(struct parport *p, const void *buf, size_t len, int flags)

    write a block of addresses in EPP mode

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

    :param buf:
        buffer of data to write
    :type buf: const void \*

    :param len:
        length of buffer \ ``buf``\ 
    :type len: size_t

    :param flags:
        may be PARPORT_EPP_FAST
    :type flags: int

.. _`parport_ip32_fifo_wait_break`:

parport_ip32_fifo_wait_break
============================

.. c:function:: unsigned int parport_ip32_fifo_wait_break(struct parport *p, unsigned long expire)

    check if the waiting function should return

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

    :param expire:
        timeout expiring date, in jiffies
    :type expire: unsigned long

.. _`parport_ip32_fifo_wait_break.description`:

Description
-----------

\ :c:func:`parport_ip32_fifo_wait_break`\  checks if the waiting function should return
immediately or not.  The break conditions are:
- expired timeout;
- a pending signal;
- nFault asserted low.
This function also calls \ :c:func:`cond_resched`\ .

.. _`parport_ip32_fwp_wait_polling`:

parport_ip32_fwp_wait_polling
=============================

.. c:function:: unsigned int parport_ip32_fwp_wait_polling(struct parport *p)

    wait for FIFO to empty (polling)

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

.. _`parport_ip32_fwp_wait_polling.description`:

Description
-----------

Returns the number of bytes that can safely be written in the FIFO.  A
return value of zero means that the calling function should terminate as
fast as possible.

.. _`parport_ip32_fwp_wait_interrupt`:

parport_ip32_fwp_wait_interrupt
===============================

.. c:function:: unsigned int parport_ip32_fwp_wait_interrupt(struct parport *p)

    wait for FIFO to empty (interrupt-driven)

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

.. _`parport_ip32_fwp_wait_interrupt.description`:

Description
-----------

Returns the number of bytes that can safely be written in the FIFO.  A
return value of zero means that the calling function should terminate as
fast as possible.

.. _`parport_ip32_fifo_write_block_pio`:

parport_ip32_fifo_write_block_pio
=================================

.. c:function:: size_t parport_ip32_fifo_write_block_pio(struct parport *p, const void *buf, size_t len)

    write a block of data (PIO mode)

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

    :param buf:
        buffer of data to write
    :type buf: const void \*

    :param len:
        length of buffer \ ``buf``\ 
    :type len: size_t

.. _`parport_ip32_fifo_write_block_pio.description`:

Description
-----------

Uses PIO to write the contents of the buffer \ ``buf``\  into the parallel port
FIFO.  Returns the number of bytes that were actually written.  It can work
with or without the help of interrupts.  The parallel port must be
correctly initialized before calling \ :c:func:`parport_ip32_fifo_write_block_pio`\ .

.. _`parport_ip32_fifo_write_block_dma`:

parport_ip32_fifo_write_block_dma
=================================

.. c:function:: size_t parport_ip32_fifo_write_block_dma(struct parport *p, const void *buf, size_t len)

    write a block of data (DMA mode)

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

    :param buf:
        buffer of data to write
    :type buf: const void \*

    :param len:
        length of buffer \ ``buf``\ 
    :type len: size_t

.. _`parport_ip32_fifo_write_block_dma.description`:

Description
-----------

Uses DMA to write the contents of the buffer \ ``buf``\  into the parallel port
FIFO.  Returns the number of bytes that were actually written.  The
parallel port must be correctly initialized before calling
\ :c:func:`parport_ip32_fifo_write_block_dma`\ .

.. _`parport_ip32_fifo_write_block`:

parport_ip32_fifo_write_block
=============================

.. c:function:: size_t parport_ip32_fifo_write_block(struct parport *p, const void *buf, size_t len)

    write a block of data

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

    :param buf:
        buffer of data to write
    :type buf: const void \*

    :param len:
        length of buffer \ ``buf``\ 
    :type len: size_t

.. _`parport_ip32_fifo_write_block.description`:

Description
-----------

Uses PIO or DMA to write the contents of the buffer \ ``buf``\  into the parallel
p FIFO.  Returns the number of bytes that were actually written.

.. _`parport_ip32_drain_fifo`:

parport_ip32_drain_fifo
=======================

.. c:function:: unsigned int parport_ip32_drain_fifo(struct parport *p, unsigned long timeout)

    wait for FIFO to empty

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

    :param timeout:
        timeout, in jiffies
    :type timeout: unsigned long

.. _`parport_ip32_drain_fifo.description`:

Description
-----------

This function waits for FIFO to empty.  It returns 1 when FIFO is empty, or
0 if the timeout \ ``timeout``\  is reached before, or if a signal is pending.

.. _`parport_ip32_get_fifo_residue`:

parport_ip32_get_fifo_residue
=============================

.. c:function:: unsigned int parport_ip32_get_fifo_residue(struct parport *p, unsigned int mode)

    reset FIFO

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

    :param mode:
        current operation mode (ECR_MODE_PPF or ECR_MODE_ECP)
    :type mode: unsigned int

.. _`parport_ip32_get_fifo_residue.description`:

Description
-----------

This function resets FIFO, and returns the number of bytes remaining in it.

.. _`parport_ip32_compat_write_data`:

parport_ip32_compat_write_data
==============================

.. c:function:: size_t parport_ip32_compat_write_data(struct parport *p, const void *buf, size_t len, int flags)

    write a block of data in SPP mode

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

    :param buf:
        buffer of data to write
    :type buf: const void \*

    :param len:
        length of buffer \ ``buf``\ 
    :type len: size_t

    :param flags:
        ignored
    :type flags: int

.. _`parport_ip32_ecp_write_data`:

parport_ip32_ecp_write_data
===========================

.. c:function:: size_t parport_ip32_ecp_write_data(struct parport *p, const void *buf, size_t len, int flags)

    write a block of data in ECP mode

    :param p:
        pointer to \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

    :param buf:
        buffer of data to write
    :type buf: const void \*

    :param len:
        length of buffer \ ``buf``\ 
    :type len: size_t

    :param flags:
        ignored
    :type flags: int

.. _`parport_ip32_ecp_supported`:

parport_ip32_ecp_supported
==========================

.. c:function:: unsigned int parport_ip32_ecp_supported(struct parport *p)

    check for an ECP port

    :param p:
        pointer to the \ :c:type:`struct parport <parport>`\  structure
    :type p: struct parport \*

.. _`parport_ip32_ecp_supported.description`:

Description
-----------

Returns 1 if an ECP port is found, and 0 otherwise.  This function actually
checks if an Extended Control Register seems to be present.  On successful
return, the port is placed in SPP mode.

.. _`parport_ip32_fifo_supported`:

parport_ip32_fifo_supported
===========================

.. c:function:: unsigned int parport_ip32_fifo_supported(struct parport *p)

    check for FIFO parameters

    :param p:
        pointer to the \ :c:type:`struct parport <parport>`\  structure
    :type p: struct parport \*

.. _`parport_ip32_fifo_supported.description`:

Description
-----------

Check for FIFO parameters of an Extended Capabilities Port.  Returns 1 on
success, and 0 otherwise.  Adjust FIFO parameters in the parport structure.
On return, the port is placed in SPP mode.

.. _`parport_ip32_make_isa_registers`:

parport_ip32_make_isa_registers
===============================

.. c:function:: void parport_ip32_make_isa_registers(struct parport_ip32_regs *regs, void __iomem *base, void __iomem *base_hi, unsigned int regshift)

    compute (ISA) register addresses

    :param regs:
        pointer to \ :c:type:`struct parport_ip32_regs <parport_ip32_regs>`\  to fill
    :type regs: struct parport_ip32_regs \*

    :param base:
        base address of standard and EPP registers
    :type base: void __iomem \*

    :param base_hi:
        base address of ECP registers
    :type base_hi: void __iomem \*

    :param regshift:
        how much to shift register offset by
    :type regshift: unsigned int

.. _`parport_ip32_make_isa_registers.description`:

Description
-----------

Compute register addresses, according to the ISA standard.  The addresses
of the standard and EPP registers are computed from address \ ``base``\ .  The
addresses of the ECP registers are computed from address \ ``base_hi``\ .

.. _`parport_ip32_probe_port`:

parport_ip32_probe_port
=======================

.. c:function:: struct parport *parport_ip32_probe_port( void)

    probe and register IP32 built-in parallel port

    :param void:
        no arguments
    :type void: 

.. _`parport_ip32_probe_port.description`:

Description
-----------

Returns the new allocated \ :c:type:`struct parport <parport>`\  structure.  On error, an error code is
encoded in return value with the ERR_PTR function.

.. _`parport_ip32_unregister_port`:

parport_ip32_unregister_port
============================

.. c:function:: __exit void parport_ip32_unregister_port(struct parport *p)

    unregister a parallel port

    :param p:
        pointer to the \ :c:type:`struct parport <parport>`\ 
    :type p: struct parport \*

.. _`parport_ip32_unregister_port.description`:

Description
-----------

Unregisters a parallel port and free previously allocated resources
(memory, IRQ, ...).

.. _`parport_ip32_init`:

parport_ip32_init
=================

.. c:function:: int parport_ip32_init( void)

    module initialization function

    :param void:
        no arguments
    :type void: 

.. _`parport_ip32_exit`:

parport_ip32_exit
=================

.. c:function:: void __exit parport_ip32_exit( void)

    module termination function

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.


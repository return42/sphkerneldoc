.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/pinctrl-adi2.c

.. _`gpio_port_saved`:

struct gpio_port_saved
======================

.. c:type:: struct gpio_port_saved

    GPIO port registers that should be saved between power suspend and resume operations.

.. _`gpio_port_saved.definition`:

Definition
----------

.. code-block:: c

    struct gpio_port_saved {
        u16 fer;
        u16 data;
        u16 dir;
        u16 inen;
        u32 mux;
    }

.. _`gpio_port_saved.members`:

Members
-------

fer
    PORTx_FER register

data
    PORTx_DATA register

dir
    PORTx_DIR register

inen
    PORTx_INEN register

mux
    PORTx_MUX register

.. _`gpio_pint`:

struct gpio_pint
================

.. c:type:: struct gpio_pint

    Pin interrupt controller device. Multiple ADI GPIO banks can be mapped into one Pin interrupt controller.

.. _`gpio_pint.definition`:

Definition
----------

.. code-block:: c

    struct gpio_pint {
        struct list_head node;
        void __iomem *base;
        int irq;
        struct irq_domain *domain[2];
        struct gpio_pint_regs *regs;
        struct gpio_pint_saved saved_data;
        int map_count;
        spinlock_t lock;
        int (*pint_map_port)(struct gpio_pint *pint, bool assign, u8 map, struct irq_domain *domain);
    }

.. _`gpio_pint.members`:

Members
-------

node
    All gpio_pint instances are added to a global list.

base
    PINT device register base address

irq
    IRQ of the PINT device, it is the parent IRQ of all
    GPIO IRQs mapping to this device.

domain
    [0] irq domain of the gpio port, whose hardware interrupts are
    mapping to the low 16-bit of the pint registers.
    [1] irq domain of the gpio port, whose hardware interrupts are
    mapping to the high 16-bit of the pint registers.

regs
    address pointer to the PINT device

saved_data
    *undescribed*

map_count
    No more than 2 GPIO banks can be mapped to this PINT device.

lock
    This lock make sure the irq_chip operations to one PINT device
    for different GPIO interrrupts are atomic.

pint_map_port
    Set up the mapping between one PINT device and
    multiple GPIO banks.

.. _`gpio_port`:

struct gpio_port
================

.. c:type:: struct gpio_port

    GPIO bank device. Multiple ADI GPIO banks can be mapped into one pin interrupt controller.

.. _`gpio_port.definition`:

Definition
----------

.. code-block:: c

    struct gpio_port {
        struct list_head node;
        void __iomem *base;
        int irq_base;
        unsigned int width;
        struct gpio_port_t *regs;
        struct gpio_port_saved saved_data;
        struct device *dev;
        struct gpio_pint *pint;
        u8 pint_map;
        bool pint_assign;
        spinlock_t lock;
        struct gpio_chip chip;
        struct irq_domain *domain;
    }

.. _`gpio_port.members`:

Members
-------

node
    All gpio_port instances are added to a list.

base
    GPIO bank device register base address

irq_base
    base IRQ of the GPIO bank device

width
    PIN number of the GPIO bank device

regs
    address pointer to the GPIO bank device

saved_data
    registers that should be saved between PM operations.

dev
    device structure of this GPIO bank

pint
    GPIO PINT device that this GPIO bank mapped to

pint_map
    GIOP bank mapping code in PINT device

pint_assign
    The 32-bit PINT registers can be divided into 2 parts. A
    GPIO bank can be mapped into either low 16 bits[0] or high 16
    bits[1] of each PINT register.

lock
    This lock make sure the irq_chip operations to one PINT device
    for different GPIO interrrupts are atomic.

chip
    abstract a GPIO controller

domain
    The irq domain owned by the GPIO port.

.. This file was automatic generated / don't edit.


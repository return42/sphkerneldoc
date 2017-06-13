.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/pinctrl-single.c

.. _`pcs_func_vals`:

struct pcs_func_vals
====================

.. c:type:: struct pcs_func_vals

    mux function register offset and value pair

.. _`pcs_func_vals.definition`:

Definition
----------

.. code-block:: c

    struct pcs_func_vals {
        void __iomem *reg;
        unsigned val;
        unsigned mask;
    }

.. _`pcs_func_vals.members`:

Members
-------

reg
    register virtual address

val
    register value

mask
    *undescribed*

.. _`pcs_conf_vals`:

struct pcs_conf_vals
====================

.. c:type:: struct pcs_conf_vals

    pinconf parameter, pinconf register offset and value, enable, disable, mask

.. _`pcs_conf_vals.definition`:

Definition
----------

.. code-block:: c

    struct pcs_conf_vals {
        enum pin_config_param param;
        unsigned val;
        unsigned enable;
        unsigned disable;
        unsigned mask;
    }

.. _`pcs_conf_vals.members`:

Members
-------

param
    config parameter

val
    user input bits in the pinconf register

enable
    enable bits in the pinconf register

disable
    disable bits in the pinconf register

mask
    mask bits in the register value

.. _`pcs_conf_type`:

struct pcs_conf_type
====================

.. c:type:: struct pcs_conf_type

    pinconf property name, pinconf param pair

.. _`pcs_conf_type.definition`:

Definition
----------

.. code-block:: c

    struct pcs_conf_type {
        const char *name;
        enum pin_config_param param;
    }

.. _`pcs_conf_type.members`:

Members
-------

name
    property name in DTS file

param
    config parameter

.. _`pcs_function`:

struct pcs_function
===================

.. c:type:: struct pcs_function

    pinctrl function

.. _`pcs_function.definition`:

Definition
----------

.. code-block:: c

    struct pcs_function {
        const char *name;
        struct pcs_func_vals *vals;
        unsigned nvals;
        const char **pgnames;
        int npgnames;
        struct pcs_conf_vals *conf;
        int nconfs;
        struct list_head node;
    }

.. _`pcs_function.members`:

Members
-------

name
    pinctrl function name

vals
    register and vals array

nvals
    number of entries in vals array

pgnames
    array of pingroup names the function uses

npgnames
    number of pingroup names the function uses

conf
    *undescribed*

nconfs
    *undescribed*

node
    list node

.. _`pcs_gpiofunc_range`:

struct pcs_gpiofunc_range
=========================

.. c:type:: struct pcs_gpiofunc_range

    pin ranges with same mux value of gpio function

.. _`pcs_gpiofunc_range.definition`:

Definition
----------

.. code-block:: c

    struct pcs_gpiofunc_range {
        unsigned offset;
        unsigned npins;
        unsigned gpiofunc;
        struct list_head node;
    }

.. _`pcs_gpiofunc_range.members`:

Members
-------

offset
    offset base of pins

npins
    number pins with the same mux value of gpio function

gpiofunc
    mux value of gpio function

node
    list node

.. _`pcs_data`:

struct pcs_data
===============

.. c:type:: struct pcs_data

    wrapper for data needed by pinctrl framework

.. _`pcs_data.definition`:

Definition
----------

.. code-block:: c

    struct pcs_data {
        struct pinctrl_pin_desc *pa;
        int cur;
    }

.. _`pcs_data.members`:

Members
-------

pa
    pindesc array

cur
    index to current element

.. _`pcs_data.revisit`:

REVISIT
-------

We should be able to drop this eventually by adding
support for registering pins individually in the pinctrl
framework for those drivers that don't need a static array.

.. _`pcs_soc_data`:

struct pcs_soc_data
===================

.. c:type:: struct pcs_soc_data

    SoC specific settings

.. _`pcs_soc_data.definition`:

Definition
----------

.. code-block:: c

    struct pcs_soc_data {
        unsigned flags;
        int irq;
        unsigned irq_enable_mask;
        unsigned irq_status_mask;
        void (*rearm)(void);
    }

.. _`pcs_soc_data.members`:

Members
-------

flags
    initial SoC specific PCS_FEAT_xxx values

irq
    optional interrupt for the controller

irq_enable_mask
    optional SoC specific interrupt enable mask

irq_status_mask
    optional SoC specific interrupt status mask

rearm
    optional SoC specific wake-up rearm function

.. _`pcs_device`:

struct pcs_device
=================

.. c:type:: struct pcs_device

    pinctrl device instance

.. _`pcs_device.definition`:

Definition
----------

.. code-block:: c

    struct pcs_device {
        struct resource *res;
        void __iomem *base;
        unsigned size;
        struct device *dev;
        struct device_node *np;
        struct pinctrl_dev *pctl;
        unsigned flags;
    #define PCS_QUIRK_SHARED_IRQ 1 << 2
    #define PCS_FEAT_IRQ 1 << 1
    #define PCS_FEAT_PINCONF 1 << 0
        struct property *missing_nr_pinctrl_cells;
        struct pcs_soc_data socdata;
        raw_spinlock_t lock;
        struct mutex mutex;
        unsigned width;
        unsigned fmask;
        unsigned fshift;
        unsigned foff;
        unsigned fmax;
        bool bits_per_mux;
        unsigned bits_per_pin;
        struct pcs_data pins;
        struct list_head gpiofuncs;
        struct list_head irqs;
        struct irq_chip chip;
        struct irq_domain *domain;
        struct pinctrl_desc desc;
        unsigned (*read)(void __iomem *reg);
        void (*write)(unsigned val, void __iomem *reg);
    }

.. _`pcs_device.members`:

Members
-------

res
    resources

base
    virtual address of the controller

size
    size of the ioremapped area

dev
    device entry

np
    device tree node

pctl
    pin controller device

flags
    mask of PCS_FEAT_xxx values

missing_nr_pinctrl_cells
    for legacy binding, may go away

socdata
    soc specific data

lock
    spinlock for register access

mutex
    mutex protecting the lists

width
    bits per mux register

fmask
    function register mask

fshift
    function register shift

foff
    value to turn mux off

fmax
    max number of functions in fmask

bits_per_mux
    number of bits per mux

bits_per_pin
    number of bits per pin

pins
    physical pins on the SoC

gpiofuncs
    list of gpio functions

irqs
    list of interrupt registers

chip
    chip container for this instance

domain
    IRQ domain for this instance

desc
    pin controller descriptor

read
    register read function to use

write
    register write function to use

.. _`pcs_add_pin`:

pcs_add_pin
===========

.. c:function:: int pcs_add_pin(struct pcs_device *pcs, unsigned offset, unsigned pin_pos)

    add a pin to the static per controller pin array

    :param struct pcs_device \*pcs:
        pcs driver instance

    :param unsigned offset:
        register offset from base

    :param unsigned pin_pos:
        *undescribed*

.. _`pcs_allocate_pin_table`:

pcs_allocate_pin_table
======================

.. c:function:: int pcs_allocate_pin_table(struct pcs_device *pcs)

    adds all the pins for the pinctrl driver

    :param struct pcs_device \*pcs:
        pcs driver instance

.. _`pcs_allocate_pin_table.description`:

Description
-----------

In case of errors, resources are freed in pcs_free_resources.

If your hardware needs holes in the address space, then just set
up multiple driver instances.

.. _`pcs_add_function`:

pcs_add_function
================

.. c:function:: struct pcs_function *pcs_add_function(struct pcs_device *pcs, struct device_node *np, const char *name, struct pcs_func_vals *vals, unsigned nvals, const char **pgnames, unsigned npgnames)

    adds a new function to the function list

    :param struct pcs_device \*pcs:
        pcs driver instance

    :param struct device_node \*np:
        device node of the mux entry

    :param const char \*name:
        name of the function

    :param struct pcs_func_vals \*vals:
        array of mux register value pairs used by the function

    :param unsigned nvals:
        number of mux register value pairs

    :param const char \*\*pgnames:
        array of pingroup names for the function

    :param unsigned npgnames:
        number of pingroup names

.. _`pcs_get_pin_by_offset`:

pcs_get_pin_by_offset
=====================

.. c:function:: int pcs_get_pin_by_offset(struct pcs_device *pcs, unsigned offset)

    get a pin index based on the register offset

    :param struct pcs_device \*pcs:
        pcs driver instance

    :param unsigned offset:
        register offset from the base

.. _`pcs_get_pin_by_offset.description`:

Description
-----------

Note that this is OK as long as the pins are in a static array.

.. _`pcs_parse_one_pinctrl_entry`:

pcs_parse_one_pinctrl_entry
===========================

.. c:function:: int pcs_parse_one_pinctrl_entry(struct pcs_device *pcs, struct device_node *np, struct pinctrl_map **map, unsigned *num_maps, const char **pgnames)

    parses a device tree mux entry

    :param struct pcs_device \*pcs:
        pinctrl driver instance

    :param struct device_node \*np:
        device node of the mux entry

    :param struct pinctrl_map \*\*map:
        map entry

    :param unsigned \*num_maps:
        number of map

    :param const char \*\*pgnames:
        pingroup names

.. _`pcs_parse_one_pinctrl_entry.description`:

Description
-----------

Note that this binding currently supports only sets of one register + value.

Also note that this driver tries to avoid understanding pin and function
names because of the extra bloat they would cause especially in the case of
a large number of pins. This driver just sets what is specified for the board
in the .dts file. Further user space debugging tools can be developed to
decipher the pin and function names using debugfs.

If you are concerned about the boot time, set up the static pins in
the bootloader, and only set up selected pins as device tree entries.

.. _`pcs_dt_node_to_map`:

pcs_dt_node_to_map
==================

.. c:function:: int pcs_dt_node_to_map(struct pinctrl_dev *pctldev, struct device_node *np_config, struct pinctrl_map **map, unsigned *num_maps)

    allocates and parses pinctrl maps

    :param struct pinctrl_dev \*pctldev:
        pinctrl instance

    :param struct device_node \*np_config:
        device tree pinmux entry

    :param struct pinctrl_map \*\*map:
        array of map entries

    :param unsigned \*num_maps:
        number of maps

.. _`pcs_irq_free`:

pcs_irq_free
============

.. c:function:: void pcs_irq_free(struct pcs_device *pcs)

    free interrupt

    :param struct pcs_device \*pcs:
        pcs driver instance

.. _`pcs_free_resources`:

pcs_free_resources
==================

.. c:function:: void pcs_free_resources(struct pcs_device *pcs)

    free memory used by this driver

    :param struct pcs_device \*pcs:
        pcs driver instance

.. _`pcs_irq_set`:

pcs_irq_set
===========

.. c:function:: void pcs_irq_set(struct pcs_soc_data *pcs_soc, int irq, const bool enable)

    enables or disables an interrupt

    :param struct pcs_soc_data \*pcs_soc:
        *undescribed*

    :param int irq:
        *undescribed*

    :param const bool enable:
        *undescribed*

.. _`pcs_irq_set.description`:

Description
-----------

Note that this currently assumes one interrupt per pinctrl
register that is typically used for wake-up events.

.. _`pcs_irq_mask`:

pcs_irq_mask
============

.. c:function:: void pcs_irq_mask(struct irq_data *d)

    mask pinctrl interrupt

    :param struct irq_data \*d:
        interrupt data

.. _`pcs_irq_unmask`:

pcs_irq_unmask
==============

.. c:function:: void pcs_irq_unmask(struct irq_data *d)

    unmask pinctrl interrupt

    :param struct irq_data \*d:
        interrupt data

.. _`pcs_irq_set_wake`:

pcs_irq_set_wake
================

.. c:function:: int pcs_irq_set_wake(struct irq_data *d, unsigned int state)

    toggle the suspend and resume wake up

    :param struct irq_data \*d:
        interrupt data

    :param unsigned int state:
        wake-up state

.. _`pcs_irq_set_wake.description`:

Description
-----------

Note that this should be called only for suspend and resume.
For runtime PM, the wake-up events should be enabled by default.

.. _`pcs_irq_handle`:

pcs_irq_handle
==============

.. c:function:: int pcs_irq_handle(struct pcs_soc_data *pcs_soc)

    common interrupt handler

    :param struct pcs_soc_data \*pcs_soc:
        *undescribed*

.. _`pcs_irq_handle.description`:

Description
-----------

Note that this currently assumes we have one interrupt bit per
mux register. This interrupt is typically used for wake-up events.
For more complex interrupts different handlers can be specified.

.. _`pcs_irq_handler`:

pcs_irq_handler
===============

.. c:function:: irqreturn_t pcs_irq_handler(int irq, void *d)

    handler for the shared interrupt case

    :param int irq:
        interrupt

    :param void \*d:
        data

.. _`pcs_irq_handler.description`:

Description
-----------

Use this for cases where multiple instances of
pinctrl-single share a single interrupt like on omaps.

.. _`pcs_irq_chain_handler`:

pcs_irq_chain_handler
=====================

.. c:function:: void pcs_irq_chain_handler(struct irq_desc *desc)

    handler for the dedicated chained interrupt case

    :param struct irq_desc \*desc:
        interrupt descriptor

.. _`pcs_irq_chain_handler.description`:

Description
-----------

Use this if you have a separate interrupt for each
pinctrl-single instance.

.. _`pcs_irq_init_chained_handler`:

pcs_irq_init_chained_handler
============================

.. c:function:: int pcs_irq_init_chained_handler(struct pcs_device *pcs, struct device_node *np)

    set up a chained interrupt handler

    :param struct pcs_device \*pcs:
        pcs driver instance

    :param struct device_node \*np:
        device node pointer

.. _`pcs_quirk_missing_pinctrl_cells`:

pcs_quirk_missing_pinctrl_cells
===============================

.. c:function:: int pcs_quirk_missing_pinctrl_cells(struct pcs_device *pcs, struct device_node *np, int cells)

    handle legacy binding

    :param struct pcs_device \*pcs:
        pinctrl driver instance

    :param struct device_node \*np:
        device tree node

    :param int cells:
        number of cells

.. _`pcs_quirk_missing_pinctrl_cells.description`:

Description
-----------

Handle legacy binding with no #pinctrl-cells. This should be
always two pinctrl-single,bit-per-mux and one for others.
At some point we may want to consider removing this.

.. This file was automatic generated / don't edit.


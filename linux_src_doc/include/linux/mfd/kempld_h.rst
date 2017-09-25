.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mfd/kempld.h

.. _`kempld_info`:

struct kempld_info
==================

.. c:type:: struct kempld_info

    PLD device information structure

.. _`kempld_info.definition`:

Definition
----------

.. code-block:: c

    struct kempld_info {
        unsigned int major;
        unsigned int minor;
        unsigned int buildnr;
        unsigned int number;
        unsigned int type;
        unsigned int spec_major;
        unsigned int spec_minor;
        char version[KEMPLD_VERSION_LEN];
    }

.. _`kempld_info.members`:

Members
-------

major
    PLD major revision

minor
    PLD minor revision

buildnr
    PLD build number

number
    PLD board specific index

type
    PLD type

spec_major
    PLD FW specification major revision

spec_minor
    PLD FW specification minor revision

version
    PLD version string

.. _`kempld_device_data`:

struct kempld_device_data
=========================

.. c:type:: struct kempld_device_data

    Internal representation of the PLD device

.. _`kempld_device_data.definition`:

Definition
----------

.. code-block:: c

    struct kempld_device_data {
        void __iomem *io_base;
        void __iomem *io_index;
        void __iomem *io_data;
        u32 pld_clock;
        u32 feature_mask;
        struct device *dev;
        struct kempld_info info;
        struct mutex lock;
    }

.. _`kempld_device_data.members`:

Members
-------

io_base
    Pointer to the IO memory

io_index
    Pointer to the IO index register

io_data
    Pointer to the IO data register

pld_clock
    PLD clock frequency

feature_mask
    PLD feature mask

dev
    Pointer to kernel device structure

info
    KEMPLD info structure

lock
    PLD mutex

.. _`kempld_platform_data`:

struct kempld_platform_data
===========================

.. c:type:: struct kempld_platform_data

    PLD hardware configuration structure

.. _`kempld_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct kempld_platform_data {
        u32 pld_clock;
        int gpio_base;
        struct resource *ioresource;
        void (*get_hardware_mutex) (struct kempld_device_data *);
        void (*release_hardware_mutex) (struct kempld_device_data *);
        int (*get_info) (struct kempld_device_data *);
        int (*register_cells) (struct kempld_device_data *);
    }

.. _`kempld_platform_data.members`:

Members
-------

pld_clock
    PLD clock frequency
    \ ``gpio_base``\                    GPIO base pin number

gpio_base
    *undescribed*

ioresource
    IO addresses of the PLD

get_hardware_mutex
    *undescribed*

release_hardware_mutex
    *undescribed*

get_info
    PLD specific get_info callback

register_cells
    PLD specific register_cells callback

.. This file was automatic generated / don't edit.


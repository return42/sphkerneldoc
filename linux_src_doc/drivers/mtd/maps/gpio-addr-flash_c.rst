.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/maps/gpio-addr-flash.c

.. _`async_state`:

struct async_state
==================

.. c:type:: struct async_state

    keep GPIO flash state

.. _`async_state.definition`:

Definition
----------

.. code-block:: c

    struct async_state {
        struct mtd_info *mtd;
        struct map_info map;
        struct gpio_descs *gpios;
        unsigned int gpio_values;
        unsigned int win_order;
    }

.. _`async_state.members`:

Members
-------

mtd
    MTD state for this mapping

map
    MTD map state for this flash

gpios
    Struct containing the array of GPIO descriptors

gpio_values
    cached GPIO values

win_order
    dedicated memory size (if no GPIOs)

.. _`gf_set_gpios`:

gf_set_gpios
============

.. c:function:: void gf_set_gpios(struct async_state *state, unsigned long ofs)

    set GPIO address lines to access specified flash offset

    :param state:
        GPIO flash state
    :type state: struct async_state \*

    :param ofs:
        desired offset to access
    :type ofs: unsigned long

.. _`gf_set_gpios.description`:

Description
-----------

Rather than call the GPIO framework every time, cache the last-programmed
value.  This speeds up sequential accesses (which are by far the most common
type).

.. _`gf_read`:

gf_read
=======

.. c:function:: map_word gf_read(struct map_info *map, unsigned long ofs)

    read a word at the specified offset

    :param map:
        MTD map state
    :type map: struct map_info \*

    :param ofs:
        desired offset to read
    :type ofs: unsigned long

.. _`gf_copy_from`:

gf_copy_from
============

.. c:function:: void gf_copy_from(struct map_info *map, void *to, unsigned long from, ssize_t len)

    copy a chunk of data from the flash

    :param map:
        MTD map state
    :type map: struct map_info \*

    :param to:
        memory to copy to
    :type to: void \*

    :param from:
        flash offset to copy from
    :type from: unsigned long

    :param len:
        how much to copy
    :type len: ssize_t

.. _`gf_copy_from.description`:

Description
-----------

The "from" region may straddle more than one window, so toggle the GPIOs for
each window region before reading its data.

.. _`gf_write`:

gf_write
========

.. c:function:: void gf_write(struct map_info *map, map_word d1, unsigned long ofs)

    write a word at the specified offset

    :param map:
        MTD map state
    :type map: struct map_info \*

    :param d1:
        *undescribed*
    :type d1: map_word

    :param ofs:
        desired offset to write
    :type ofs: unsigned long

.. _`gf_copy_to`:

gf_copy_to
==========

.. c:function:: void gf_copy_to(struct map_info *map, unsigned long to, const void *from, ssize_t len)

    copy a chunk of data to the flash

    :param map:
        MTD map state
    :type map: struct map_info \*

    :param to:
        flash offset to copy to
    :type to: unsigned long

    :param from:
        memory to copy from
    :type from: const void \*

    :param len:
        how much to copy
    :type len: ssize_t

.. _`gf_copy_to.description`:

Description
-----------

See \ :c:func:`gf_copy_from`\  caveat.

.. _`gpio_flash_probe`:

gpio_flash_probe
================

.. c:function:: int gpio_flash_probe(struct platform_device *pdev)

    setup a mapping for a GPIO assisted flash

    :param pdev:
        platform device
    :type pdev: struct platform_device \*

.. _`gpio_flash_probe.the-platform-resource-layout-expected-looks-something-like`:

The platform resource layout expected looks something like
----------------------------------------------------------

struct mtd_partition partitions[] = { ... };
struct physmap_flash_data flash_data = { ... };
static struct gpiod_lookup_table addr_flash_gpios = {
.dev_id = "gpio-addr-flash.0",
.table = {
GPIO_LOOKUP_IDX("gpio.0", 15, "addr", 0, GPIO_ACTIVE_HIGH),
GPIO_LOOKUP_IDX("gpio.0", 16, "addr", 1, GPIO_ACTIVE_HIGH),
);
};
gpiod_add_lookup_table(&addr_flash_gpios);

struct resource flash_resource[] = {
{
.name  = "cfi_probe",
.start = 0x20000000,
.end   = 0x201fffff,
.flags = IORESOURCE_MEM,
},
};
struct platform_device flash_device = {
.name          = "gpio-addr-flash",
.dev           = { .platform_data = \ :c:type:`struct flash_data <flash_data>`\ , },
.num_resources = ARRAY_SIZE(flash_resource),
.resource      = flash_resource,
...
};

.. This file was automatic generated / don't edit.


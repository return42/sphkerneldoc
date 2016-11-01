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
        size_t gpio_count;
        unsigned *gpio_addrs;
        int *gpio_values;
        unsigned long win_size;
    }

.. _`async_state.members`:

Members
-------

mtd
    MTD state for this mapping

map
    MTD map state for this flash

gpio_count
    number of GPIOs used to address

gpio_addrs
    array of GPIOs to twiddle

gpio_values
    cached GPIO values

win_size
    dedicated memory size (if no GPIOs)

.. _`gf_set_gpios`:

gf_set_gpios
============

.. c:function:: void gf_set_gpios(struct async_state *state, unsigned long ofs)

    set GPIO address lines to access specified flash offset

    :param struct async_state \*state:
        GPIO flash state

    :param unsigned long ofs:
        desired offset to access

.. _`gf_set_gpios.description`:

Description
-----------

Rather than call the GPIO framework every time, cache the last-programmed
value.  This speeds up sequential accesses (which are by far the most common
type).  We rely on the GPIO framework to treat non-zero value as high so
that we don't have to normalize the bits.

.. _`gf_read`:

gf_read
=======

.. c:function:: map_word gf_read(struct map_info *map, unsigned long ofs)

    read a word at the specified offset

    :param struct map_info \*map:
        MTD map state

    :param unsigned long ofs:
        desired offset to read

.. _`gf_copy_from`:

gf_copy_from
============

.. c:function:: void gf_copy_from(struct map_info *map, void *to, unsigned long from, ssize_t len)

    copy a chunk of data from the flash

    :param struct map_info \*map:
        MTD map state

    :param void \*to:
        memory to copy to

    :param unsigned long from:
        flash offset to copy from

    :param ssize_t len:
        how much to copy

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

    :param struct map_info \*map:
        MTD map state

    :param map_word d1:
        *undescribed*

    :param unsigned long ofs:
        desired offset to write

.. _`gf_copy_to`:

gf_copy_to
==========

.. c:function:: void gf_copy_to(struct map_info *map, unsigned long to, const void *from, ssize_t len)

    copy a chunk of data to the flash

    :param struct map_info \*map:
        MTD map state

    :param unsigned long to:
        flash offset to copy to

    :param const void \*from:
        memory to copy from

    :param ssize_t len:
        how much to copy

.. _`gf_copy_to.description`:

Description
-----------

See \ :c:func:`gf_copy_from`\  caveat.

.. _`gpio_flash_probe`:

gpio_flash_probe
================

.. c:function:: int gpio_flash_probe(struct platform_device *pdev)

    setup a mapping for a GPIO assisted flash

    :param struct platform_device \*pdev:
        platform device

.. _`gpio_flash_probe.the-platform-resource-layout-expected-looks-something-like`:

The platform resource layout expected looks something like
----------------------------------------------------------

struct mtd_partition partitions[] = { ... };
struct physmap_flash_data flash_data = { ... };
unsigned flash_gpios[] = { GPIO_XX, GPIO_XX, ... };
struct resource flash_resource[] = {
{
.name  = "cfi_probe",
.start = 0x20000000,
.end   = 0x201fffff,
.flags = IORESOURCE_MEM,
}, {
.start = (unsigned long)flash_gpios,
.end   = ARRAY_SIZE(flash_gpios),
.flags = IORESOURCE_IRQ,
}
};
struct platform_device flash_device = {
.name          = "gpio-addr-flash",
.dev           = { .platform_data = \ :c:type:`struct flash_data <flash_data>`\ , },
.num_resources = ARRAY_SIZE(flash_resource),
.resource      = flash_resource,
...
};

.. This file was automatic generated / don't edit.


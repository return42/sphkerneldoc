.. -*- coding: utf-8; mode: rst -*-

======
at24.h
======


.. _`at24_platform_data`:

struct at24_platform_data
=========================

.. c:type:: at24_platform_data

    data to set up at24 (generic eeprom) driver


.. _`at24_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct at24_platform_data {
    u32 byte_len;
    u16 page_size;
    u8 flags;
    #define AT24_FLAG_ADDR16	0x80
    #define AT24_FLAG_READONLY	0x40
    #define AT24_FLAG_IRUGO		0x20
    #define AT24_FLAG_TAKE8ADDR	0x10
    void (* setup) (struct nvmem_device *nvmem, void *context);
    void * context;
  };


.. _`at24_platform_data.members`:

Members
-------

:``byte_len``:
    size of eeprom in byte

:``page_size``:
    number of byte which can be written in one go

:``flags``:
    tunable options, check AT24_FLAG\_\* defines

:``setup``:
    an optional callback invoked after eeprom is probed; enables kernel

:``context``:
    optional parameter passed to :c:func:`setup`




.. _`at24_platform_data.description`:

Description
-----------

If you set up a custom eeprom type, please double-check the parameters.
Especially page_size needs extra care, as you risk data loss if your value
is bigger than what the chip actually supports!

An example in pseudo code for a :c:func:`setup` callback:

void get_mac_addr(struct mvmem_device \*nvmem, void \*context)
{
u8 \*mac_addr = ethernet_pdata->mac_addr;
off_t offset = context;

// Read MAC addr from EEPROM
if (nvmem_device_read(nvmem, offset, ETH_ALEN, mac_addr) == ETH_ALEN)
pr_info("Read MAC addr from EEPROM: ``pM``\ \n", mac_addr);

}

This function pointer and context can now be set up in at24_platform_data.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/ps3/os-area.c

.. _`os_area_header`:

struct os_area_header
=====================

.. c:type:: struct os_area_header

    os area header segment.

.. _`os_area_header.definition`:

Definition
----------

.. code-block:: c

    struct os_area_header {
        u8 magic_num[16];
        u32 hdr_version;
        u32 db_area_offset;
        u32 ldr_area_offset;
        u32 _reserved_1;
        u32 ldr_format;
        u32 ldr_size;
        u32 _reserved_2[6];
    }

.. _`os_area_header.members`:

Members
-------

magic_num
    Always 'cell_ext_os_area'.

hdr_version
    Header format version number.

db_area_offset
    Starting segment number of other os database area.

ldr_area_offset
    Starting segment number of bootloader image area.

\_reserved_1
    *undescribed*

ldr_format
    HEADER_LDR_FORMAT flag.

ldr_size
    Size of bootloader image in bytes.

\_reserved_2
    *undescribed*

.. _`os_area_header.description`:

Description
-----------

Note that the docs refer to area offsets.  These are offsets in units of
segments from the start of the os area (top of the header).  These are
better thought of as segment numbers.  The os area of the os area is
reserved for the os image.

.. _`os_area_params`:

struct os_area_params
=====================

.. c:type:: struct os_area_params

    os area params segment.

.. _`os_area_params.definition`:

Definition
----------

.. code-block:: c

    struct os_area_params {
        u32 boot_flag;
        u32 _reserved_1[3];
        u32 num_params;
        u32 _reserved_2[3];
        s64 rtc_diff;
        u8 av_multi_out;
        u8 ctrl_button;
        u8 _reserved_3[6];
        u8 static_ip_addr[4];
        u8 network_mask[4];
        u8 default_gateway[4];
        u8 _reserved_4[4];
        u8 dns_primary[4];
        u8 dns_secondary[4];
        u8 _reserved_5[8];
    }

.. _`os_area_params.members`:

Members
-------

boot_flag
    User preference of operating system, PARAM_BOOT_FLAG flag.

\_reserved_1
    *undescribed*

num_params
    Number of params in this (params) segment.

\_reserved_2
    *undescribed*

rtc_diff
    Difference in seconds between 1970 and the ps3 rtc value.

av_multi_out
    User preference of AV output, PARAM_AV_MULTI_OUT flag.

ctrl_button
    User preference of controller button config, PARAM_CTRL_BUTTON
    flag.

\_reserved_3
    *undescribed*

static_ip_addr
    User preference of static IP address.

network_mask
    User preference of static network mask.

default_gateway
    User preference of static default gateway.

\_reserved_4
    *undescribed*

dns_primary
    User preference of static primary dns server.

dns_secondary
    User preference of static secondary dns server.

\_reserved_5
    *undescribed*

.. _`os_area_params.description`:

Description
-----------

The ps3 rtc maintains a read-only value that approximates seconds since
2000-01-01 00:00:00 UTC.

User preference of zero for static_ip_addr means use dhcp.

.. _`os_area_db`:

struct os_area_db
=================

.. c:type:: struct os_area_db

    Shared flash memory database.

.. _`os_area_db.definition`:

Definition
----------

.. code-block:: c

    struct os_area_db {
        u8 magic_num[4];
        u16 version;
        u16 _reserved_1;
        u16 index_64;
        u16 count_64;
        u16 index_32;
        u16 count_32;
        u16 index_16;
        u16 count_16;
        u32 _reserved_2;
        u8 _db_data[1000];
    }

.. _`os_area_db.members`:

Members
-------

magic_num
    Always '-db-'.

version
    os_area_db format version number.

\_reserved_1
    *undescribed*

index_64
    byte offset of the database id index for 64 bit variables.

count_64
    number of usable 64 bit index entries

index_32
    byte offset of the database id index for 32 bit variables.

count_32
    number of usable 32 bit index entries

index_16
    byte offset of the database id index for 16 bit variables.

count_16
    number of usable 16 bit index entries

\_reserved_2
    *undescribed*

\_db_data
    *undescribed*

.. _`os_area_db.description`:

Description
-----------

Flash rom storage for exclusive use by guests running in the other os lpar.
The current system configuration allocates 1K (two segments) for other os
use.

.. _`os_area_db_owner`:

enum os_area_db_owner
=====================

.. c:type:: enum os_area_db_owner

    Data owners.

.. _`os_area_db_owner.definition`:

Definition
----------

.. code-block:: c

    enum os_area_db_owner {
        OS_AREA_DB_OWNER_ANY,
        OS_AREA_DB_OWNER_NONE,
        OS_AREA_DB_OWNER_PROTOTYPE,
        OS_AREA_DB_OWNER_LINUX,
        OS_AREA_DB_OWNER_PETITBOOT,
        OS_AREA_DB_OWNER_MAX
    };

.. _`os_area_db_owner.constants`:

Constants
---------

OS_AREA_DB_OWNER_ANY
    *undescribed*

OS_AREA_DB_OWNER_NONE
    *undescribed*

OS_AREA_DB_OWNER_PROTOTYPE
    *undescribed*

OS_AREA_DB_OWNER_LINUX
    *undescribed*

OS_AREA_DB_OWNER_PETITBOOT
    *undescribed*

OS_AREA_DB_OWNER_MAX
    *undescribed*

.. _`saved_params`:

struct saved_params
===================

.. c:type:: struct saved_params

    Static working copies of data from the PS3 'os area'.

.. _`saved_params.definition`:

Definition
----------

.. code-block:: c

    struct saved_params {
        unsigned int valid;
        s64 rtc_diff;
        unsigned int av_multi_out;
    }

.. _`saved_params.members`:

Members
-------

valid
    *undescribed*

rtc_diff
    *undescribed*

av_multi_out
    *undescribed*

.. _`saved_params.the-order-of-preference-we-use-for-the-rtc_diff-source`:

The order of preference we use for the rtc_diff source
------------------------------------------------------

1) The database value.
2) The game os value.
3) The number of seconds from 1970 to 2000.

.. _`os_area_set_property`:

os_area_set_property
====================

.. c:function:: void os_area_set_property(struct device_node *node, struct property *prop)

    Add or overwrite a saved_params value to the device tree.

    :param node:
        *undescribed*
    :type node: struct device_node \*

    :param prop:
        *undescribed*
    :type prop: struct property \*

.. _`os_area_set_property.description`:

Description
-----------

Overwrites an existing property.

.. _`os_area_get_property`:

os_area_get_property
====================

.. c:function:: void os_area_get_property(struct device_node *node, struct property *prop)

    Get a saved_params value from the device tree.

    :param node:
        *undescribed*
    :type node: struct device_node \*

    :param prop:
        *undescribed*
    :type prop: struct property \*

.. _`db_for_each_64`:

db_for_each_64
==============

.. c:function:: int db_for_each_64(const struct os_area_db *db, const struct os_area_db_id *match_id, struct db_iterator *i)

    Iterator for 64 bit entries.

    :param db:
        *undescribed*
    :type db: const struct os_area_db \*

    :param match_id:
        *undescribed*
    :type match_id: const struct os_area_db_id \*

    :param i:
        *undescribed*
    :type i: struct db_iterator \*

.. _`db_for_each_64.description`:

Description
-----------

A NULL value for id can be used to match all entries.
OS_AREA_DB_OWNER_ANY and OS_AREA_DB_KEY_ANY can be used to match all.

.. _`update_flash_db`:

update_flash_db
===============

.. c:function:: int update_flash_db( void)

    Helper for os_area_queue_work_handler.

    :param void:
        no arguments
    :type void: 

.. _`os_area_queue_work_handler`:

os_area_queue_work_handler
==========================

.. c:function:: void os_area_queue_work_handler(struct work_struct *work)

    Asynchronous write handler.

    :param work:
        *undescribed*
    :type work: struct work_struct \*

.. _`os_area_queue_work_handler.description`:

Description
-----------

An asynchronous write for flash memory and the device tree.  Do not
call directly, use \ :c:func:`os_area_queue_work`\ .

.. _`ps3_os_area_save_params`:

ps3_os_area_save_params
=======================

.. c:function:: void ps3_os_area_save_params( void)

    Copy data from os area mirror to \ ``saved_params``\ .

    :param void:
        no arguments
    :type void: 

.. _`ps3_os_area_save_params.description`:

Description
-----------

For the convenience of the guest the HV makes a copy of the os area in
flash to a high address in the boot memory region and then puts that RAM
address and the byte count into the repository for retrieval by the guest.
We copy the data we want into a static variable and allow the memory setup
by the HV to be claimed by the memblock manager.

The os area mirror will not be available to a second stage kernel, and
the header verify will fail.  In this case, the saved_params values will
be set from flash memory or the passed in device tree in \ :c:func:`ps3_os_area_init`\ .

.. _`ps3_os_area_init`:

ps3_os_area_init
================

.. c:function:: void ps3_os_area_init( void)

    Setup os area device tree properties as needed.

    :param void:
        no arguments
    :type void: 

.. _`ps3_os_area_get_rtc_diff`:

ps3_os_area_get_rtc_diff
========================

.. c:function:: u64 ps3_os_area_get_rtc_diff( void)

    Returns the rtc diff value.

    :param void:
        no arguments
    :type void: 

.. _`ps3_os_area_set_rtc_diff`:

ps3_os_area_set_rtc_diff
========================

.. c:function:: void ps3_os_area_set_rtc_diff(u64 rtc_diff)

    Set the rtc diff value.

    :param rtc_diff:
        *undescribed*
    :type rtc_diff: u64

.. _`ps3_os_area_set_rtc_diff.description`:

Description
-----------

An asynchronous write is needed to support writing updates from
the timer interrupt context.

.. _`ps3_os_area_get_av_multi_out`:

ps3_os_area_get_av_multi_out
============================

.. c:function:: enum ps3_param_av_multi_out ps3_os_area_get_av_multi_out( void)

    Returns the default video mode.

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.


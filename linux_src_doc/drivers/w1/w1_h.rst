.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/w1/w1.h

.. _`w1_reg_num`:

struct w1_reg_num
=================

.. c:type:: struct w1_reg_num

    broken out slave device id

.. _`w1_reg_num.definition`:

Definition
----------

.. code-block:: c

    struct w1_reg_num {
    #if defined(__LITTLE_ENDIAN_BITFIELD)
        __u64 family:8:48:8;
        __u64 id:8:48;
        __u64 crc:8;
    #elif defined(__BIG_ENDIAN_BITFIELD)
        __u64 crc:8;
        __u64 id:8:48;
        __u64 family:8:48:8;
    #else
    #error "Please fix <asm/byteorder.h>"
    #endif
    }

.. _`w1_reg_num.members`:

Members
-------

family
    identifies the type of device

id
    along with family is the unique device id

crc
    checksum of the other bytes

crc
    checksum of the other bytes

id
    along with family is the unique device id

family
    identifies the type of device

.. _`w1_slave`:

struct w1_slave
===============

.. c:type:: struct w1_slave

    holds a single slave device on the bus

.. _`w1_slave.definition`:

Definition
----------

.. code-block:: c

    struct w1_slave {
        struct module *owner;
        unsigned char name[W1_MAXNAMELEN];
        struct list_head w1_slave_entry;
        struct w1_reg_num reg_num;
        atomic_t refcnt;
        int ttl;
        unsigned long flags;
        struct w1_master *master;
        struct w1_family *family;
        void *family_data;
        struct device dev;
    }

.. _`w1_slave.members`:

Members
-------

owner
    Points to the one wire "wire" kernel module.

name
    Device id is ascii.

w1_slave_entry
    data for the linked list

reg_num
    the slave id in binary

refcnt
    reference count, delete when 0

ttl
    decrement per search this slave isn't found, deatch at 0

flags
    bit flags for W1_SLAVE_ACTIVE W1_SLAVE_DETACH

master
    bus which this slave is on

family
    module for device family type

family_data
    pointer for use by the family module

dev
    kernel device identifier

.. _`w1_bus_master`:

struct w1_bus_master
====================

.. c:type:: struct w1_bus_master

    operations available on a bus master

.. _`w1_bus_master.definition`:

Definition
----------

.. code-block:: c

    struct w1_bus_master {
        void *data;
        u8 (*read_bit)(void *);
        void (*write_bit)(void *, u8);
        u8 (*touch_bit)(void *, u8);
        u8 (*read_byte)(void *);
        void (*write_byte)(void *, u8);
        u8 (*read_block)(void *, u8 *, int);
        void (*write_block)(void *, const u8 *, int);
        u8 (*triplet)(void *, u8);
        u8 (*reset_bus)(void *);
        u8 (*set_pullup)(void *, int);
        void (*search)(void *, struct w1_master *,u8, w1_slave_found_callback);
    }

.. _`w1_bus_master.members`:

Members
-------

data
    the first parameter in all the functions below

read_bit
    Sample the line level \ ``return``\  the level read (0 or 1)

write_bit
    Sets the line level

touch_bit
    the lowest-level function for devices that really support the
    1-wire protocol.
    touch_bit(0) = write-0 cycle
    touch_bit(1) = write-1 / read cycle
    \ ``return``\  the bit read (0 or 1)

read_byte
    Reads a bytes. Same as 8 touch_bit(1) calls.
    \ ``return``\  the byte read

write_byte
    Writes a byte. Same as 8 touch_bit(x) calls.

read_block
    Same as a series of \ :c:func:`read_byte`\  calls
    \ ``return``\  the number of bytes read

write_block
    Same as a series of \ :c:func:`write_byte`\  calls

triplet
    Combines two reads and a smart write for ROM searches
    \ ``return``\  bit0=Id bit1=comp_id bit2=dir_taken

reset_bus
    long write-0 with a read for the presence pulse detection
    \ ``return``\  -1=Error, 0=Device present, 1=No device present

set_pullup
    Put out a strong pull-up pulse of the specified duration.
    \ ``return``\  -1=Error, 0=completed

search
    Really nice hardware can handles the different types of ROM search
    w1_master\* is passed to the slave found callback.
    u8 is search_type, W1_SEARCH or W1_ALARM_SEARCH

.. _`w1_bus_master.note`:

Note
----

read_bit and write_bit are very low level functions and should only
be used with hardware that doesn't really support 1-wire operations,
like a parallel/serial port.
Either define read_bit and write_bit OR define, at minimum, touch_bit and
reset_bus.

.. _`w1_master_flags`:

enum w1_master_flags
====================

.. c:type:: enum w1_master_flags

    bitfields used in w1_master.flags

.. _`w1_master_flags.definition`:

Definition
----------

.. code-block:: c

    enum w1_master_flags {
        W1_ABORT_SEARCH,
        W1_WARN_MAX_COUNT
    };

.. _`w1_master_flags.constants`:

Constants
---------

W1_ABORT_SEARCH
    abort searching early on shutdown

W1_WARN_MAX_COUNT
    limit warning when the maximum count is reached

.. _`w1_master`:

struct w1_master
================

.. c:type:: struct w1_master

    one per bus master

.. _`w1_master.definition`:

Definition
----------

.. code-block:: c

    struct w1_master {
        struct list_head w1_master_entry;
        struct module *owner;
        unsigned char name[W1_MAXNAMELEN];
        struct mutex list_mutex;
        struct list_head slist;
        struct list_head async_list;
        int max_slave_count;
        int slave_count;
        unsigned long attempts;
        int slave_ttl;
        int initialized;
        u32 id;
        int search_count;
        u64 search_id;
        atomic_t refcnt;
        void *priv;
        int enable_pullup;
        int pullup_duration;
        long flags;
        struct task_struct *thread;
        struct mutex mutex;
        struct mutex bus_mutex;
        struct device_driver *driver;
        struct device dev;
        struct w1_bus_master *bus_master;
        u32 seq;
    }

.. _`w1_master.members`:

Members
-------

w1_master_entry
    master linked list

owner
    module owner

name
    dynamically allocate bus name

list_mutex
    protect slist and async_list

slist
    linked list of slaves

async_list
    linked list of netlink commands to execute

max_slave_count
    maximum number of slaves to search for at a time

slave_count
    current number of slaves known

attempts
    number of searches ran

slave_ttl
    number of searches before a slave is timed out

initialized
    prevent init/removal race conditions

id
    w1 bus number

search_count
    number of automatic searches to run, -1 unlimited

search_id
    allows continuing a search

refcnt
    reference count

priv
    private data storage

enable_pullup
    allows a strong pullup

pullup_duration
    time for the next strong pullup

flags
    one of w1_master_flags

thread
    thread for bus search and netlink commands

mutex
    protect most of w1_master

bus_mutex
    pretect concurrent bus access

driver
    sysfs driver

dev
    sysfs device

bus_master
    io operations available

seq
    sequence number used for netlink broadcasts

.. _`w1_async_cmd`:

struct w1_async_cmd
===================

.. c:type:: struct w1_async_cmd

    execute callback from the w1_process kthread

.. _`w1_async_cmd.definition`:

Definition
----------

.. code-block:: c

    struct w1_async_cmd {
        struct list_head async_entry;
        void (*cb)(struct w1_master *dev, struct w1_async_cmd *async_cmd);
    }

.. _`w1_async_cmd.members`:

Members
-------

async_entry
    link entry

cb
    callback function, must list_del and destroy this list before
    returning

.. _`w1_async_cmd.description`:

Description
-----------

When inserted into the w1_master async_list, w1_process will execute
the callback.  Embed this into the structure with the command details.

.. This file was automatic generated / don't edit.


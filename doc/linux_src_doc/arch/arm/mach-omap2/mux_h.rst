.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/mux.h

.. _`omap_board_data`:

struct omap_board_data
======================

.. c:type:: struct omap_board_data

    board specific device data

.. _`omap_board_data.definition`:

Definition
----------

.. code-block:: c

    struct omap_board_data {
        int id;
        u32 flags;
        struct omap_device_pad *pads;
        int pads_cnt;
    }

.. _`omap_board_data.members`:

Members
-------

id
    instance id

flags
    additional flags for platform init code

pads
    array of device specific pads

pads_cnt
    \ :c:func:`ARRAY_SIZE`\  of pads

.. _`omap_mux_partition`:

struct omap_mux_partition
=========================

.. c:type:: struct omap_mux_partition

    contain partition related information

.. _`omap_mux_partition.definition`:

Definition
----------

.. code-block:: c

    struct omap_mux_partition {
        const char *name;
        u32 flags;
        u32 gpio;
        u32 phys;
        u32 size;
        void __iomem *base;
        struct list_head muxmodes;
        struct list_head node;
    }

.. _`omap_mux_partition.members`:

Members
-------

name
    name of the current partition

flags
    flags specific to this partition

gpio
    gpio mux mode

phys
    physical address

size
    partition size

base
    virtual address after ioremap

muxmodes
    list of nodes that belong to a partition

node
    list node for the partitions linked list

.. _`omap_mux`:

struct omap_mux
===============

.. c:type:: struct omap_mux

    data for omap mux register offset and it's value

.. _`omap_mux.definition`:

Definition
----------

.. code-block:: c

    struct omap_mux {
        u16 reg_offset;
        u16 gpio;
        #ifdef CONFIG_OMAP_MUX
        char  *muxnames[OMAP_MUX_NR_MODES];
        #ifdef CONFIG_DEBUG_FS
        char  *balls[OMAP_MUX_NR_SIDES];
        #endif
        #endif
    }

.. _`omap_mux.members`:

Members
-------

reg_offset
    mux register offset from the mux base

gpio
    GPIO number

muxnames
    available signal modes for a ball

balls
    available balls on the package

.. _`omap_ball`:

struct omap_ball
================

.. c:type:: struct omap_ball

    data for balls on omap package

.. _`omap_ball.definition`:

Definition
----------

.. code-block:: c

    struct omap_ball {
        u16 reg_offset;
        char  *balls[OMAP_MUX_NR_SIDES];
    }

.. _`omap_ball.members`:

Members
-------

reg_offset
    mux register offset from the mux base

balls
    available balls on the package

.. _`omap_board_mux`:

struct omap_board_mux
=====================

.. c:type:: struct omap_board_mux

    data for initializing mux registers

.. _`omap_board_mux.definition`:

Definition
----------

.. code-block:: c

    struct omap_board_mux {
        u16 reg_offset;
        u16 value;
    }

.. _`omap_board_mux.members`:

Members
-------

reg_offset
    mux register offset from the mux base

value
    *undescribed*

.. _`omap_device_pad`:

struct omap_device_pad
======================

.. c:type:: struct omap_device_pad

    device specific pad configuration

.. _`omap_device_pad.definition`:

Definition
----------

.. code-block:: c

    struct omap_device_pad {
        char *name;
        u8 flags;
        u16 enable;
        u16 idle;
        u16 off;
        struct omap_mux_partition *partition;
        struct omap_mux *mux;
    }

.. _`omap_device_pad.members`:

Members
-------

name
    signal name

flags
    pad specific runtime flags

enable
    runtime value for a pad

idle
    idle value for a pad

off
    off value for a pad, defaults to safe mode

partition
    mux partition

mux
    mux register

.. _`omap_mux_init_gpio`:

omap_mux_init_gpio
==================

.. c:function:: int omap_mux_init_gpio(int gpio, int val)

    initialize a signal based on the GPIO number

    :param int gpio:
        GPIO number

    :param int val:
        Options for the mux register value

.. _`omap_mux_init_signal`:

omap_mux_init_signal
====================

.. c:function:: int omap_mux_init_signal(const char *muxname, int val)

    initialize a signal based on the signal name

    :param const char \*muxname:
        Mux name in mode0_name.signal_name format

    :param int val:
        Options for the mux register value

.. _`omap_hwmod_mux_init`:

omap_hwmod_mux_init
===================

.. c:function:: struct omap_hwmod_mux_info *omap_hwmod_mux_init(struct omap_device_pad *bpads, int nr_pads)

    initialize hwmod specific mux data

    :param struct omap_device_pad \*bpads:
        Board specific device signal names

    :param int nr_pads:
        Number of signal names for the device

.. _`omap_hwmod_mux`:

omap_hwmod_mux
==============

.. c:function:: void omap_hwmod_mux(struct omap_hwmod_mux_info *hmux, u8 state)

    omap hwmod specific pin muxing

    :param struct omap_hwmod_mux_info \*hmux:
        Pads for a hwmod

    :param u8 state:
        Desired \_HWMOD_STATE

.. _`omap_hwmod_mux.description`:

Description
-----------

Called only from omap_hwmod.c, do not use.

.. _`omap_mux_get_gpio`:

omap_mux_get_gpio
=================

.. c:function:: u16 omap_mux_get_gpio(int gpio)

    get mux register value based on GPIO number

    :param int gpio:
        GPIO number

.. _`omap_mux_set_gpio`:

omap_mux_set_gpio
=================

.. c:function:: void omap_mux_set_gpio(u16 val, int gpio)

    set mux register value based on GPIO number

    :param u16 val:
        New mux register value

    :param int gpio:
        GPIO number

.. _`omap_mux_get`:

omap_mux_get
============

.. c:function:: struct omap_mux_partition *omap_mux_get(const char *name)

    get a mux partition by name

    :param const char \*name:
        Name of the mux partition

.. _`omap_mux_read`:

omap_mux_read
=============

.. c:function:: u16 omap_mux_read(struct omap_mux_partition *p, u16 mux_offset)

    read mux register

    :param struct omap_mux_partition \*p:
        *undescribed*

    :param u16 mux_offset:
        Offset of the mux register

.. _`omap_mux_write`:

omap_mux_write
==============

.. c:function:: void omap_mux_write(struct omap_mux_partition *p, u16 val, u16 mux_offset)

    write mux register

    :param struct omap_mux_partition \*p:
        *undescribed*

    :param u16 val:
        New mux register value

    :param u16 mux_offset:
        Offset of the mux register

.. _`omap_mux_write.description`:

Description
-----------

This should be only needed for dynamic remuxing of non-gpio signals.

.. _`omap_mux_write_array`:

omap_mux_write_array
====================

.. c:function:: void omap_mux_write_array(struct omap_mux_partition *p, struct omap_board_mux *board_mux)

    write an array of mux registers

    :param struct omap_mux_partition \*p:
        *undescribed*

    :param struct omap_board_mux \*board_mux:
        Array of mux registers terminated by MAP_MUX_TERMINATOR

.. _`omap_mux_write_array.description`:

Description
-----------

This should be only needed for dynamic remuxing of non-gpio signals.

.. _`omap2420_mux_init`:

omap2420_mux_init
=================

.. c:function:: int omap2420_mux_init(struct omap_board_mux *board_mux, int flags)

    initialize mux system with board specific set

    :param struct omap_board_mux \*board_mux:
        Board specific mux table

    :param int flags:
        OMAP package type used for the board

.. _`omap2430_mux_init`:

omap2430_mux_init
=================

.. c:function:: int omap2430_mux_init(struct omap_board_mux *board_mux, int flags)

    initialize mux system with board specific set

    :param struct omap_board_mux \*board_mux:
        Board specific mux table

    :param int flags:
        OMAP package type used for the board

.. _`omap3_mux_init`:

omap3_mux_init
==============

.. c:function:: int omap3_mux_init(struct omap_board_mux *board_mux, int flags)

    initialize mux system with board specific set

    :param struct omap_board_mux \*board_mux:
        Board specific mux table

    :param int flags:
        OMAP package type used for the board

.. _`omap4_mux_init`:

omap4_mux_init
==============

.. c:function:: int omap4_mux_init(struct omap_board_mux *board_subset, struct omap_board_mux *board_wkup_subset, int flags)

    initialize mux system with board specific set

    :param struct omap_board_mux \*board_subset:
        Board specific mux table

    :param struct omap_board_mux \*board_wkup_subset:
        Board specific mux table for wakeup instance

    :param int flags:
        OMAP package type used for the board

.. _`omap_mux_init`:

omap_mux_init
=============

.. c:function:: int omap_mux_init(const char *name, u32 flags, u32 mux_pbase, u32 mux_size, struct omap_mux *superset, struct omap_mux *package_subset, struct omap_board_mux *board_mux, struct omap_ball *package_balls)

    private mux init function, do not call

    :param const char \*name:
        *undescribed*

    :param u32 flags:
        *undescribed*

    :param u32 mux_pbase:
        *undescribed*

    :param u32 mux_size:
        *undescribed*

    :param struct omap_mux \*superset:
        *undescribed*

    :param struct omap_mux \*package_subset:
        *undescribed*

    :param struct omap_board_mux \*board_mux:
        *undescribed*

    :param struct omap_ball \*package_balls:
        *undescribed*

.. This file was automatic generated / don't edit.


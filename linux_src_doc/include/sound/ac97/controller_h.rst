.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/sound/ac97/controller.h

.. _`ac97_controller`:

struct ac97_controller
======================

.. c:type:: struct ac97_controller

    The AC97 controller of the AC-Link

.. _`ac97_controller.definition`:

Definition
----------

.. code-block:: c

    struct ac97_controller {
        const struct ac97_controller_ops *ops;
        struct list_head controllers;
        struct device adap;
        int nr;
        unsigned short slots_available;
        struct device *parent;
        struct ac97_codec_device *codecs[AC97_BUS_MAX_CODECS];
        void *codecs_pdata[AC97_BUS_MAX_CODECS];
    }

.. _`ac97_controller.members`:

Members
-------

ops
    the AC97 operations.

controllers
    linked list of all existing controllers.

adap
    the shell device ac97-%d, ie. ac97 adapter

nr
    the number of the shell device

slots_available
    the mask of accessible/scanable codecs.

parent
    the device providing the AC97 controller.

codecs
    the 4 possible AC97 codecs (NULL if none found).

codecs_pdata
    platform_data for each codec (NULL if no pdata).

.. _`ac97_controller.description`:

Description
-----------

This structure is internal to AC97 bus, and should not be used by the
controllers themselves, excepting for using \ ``dev``\ .

.. _`ac97_controller_ops`:

struct ac97_controller_ops
==========================

.. c:type:: struct ac97_controller_ops

    The AC97 operations

.. _`ac97_controller_ops.definition`:

Definition
----------

.. code-block:: c

    struct ac97_controller_ops {
        void (*reset)(struct ac97_controller *adrv);
        void (*warm_reset)(struct ac97_controller *adrv);
        int (*write)(struct ac97_controller *adrv, int slot, unsigned short reg, unsigned short val);
        int (*read)(struct ac97_controller *adrv, int slot, unsigned short reg);
    }

.. _`ac97_controller_ops.members`:

Members
-------

reset
    Cold reset of the AC97 AC-Link.

warm_reset
    Warm reset of the AC97 AC-Link.

write
    Write of a single AC97 register.

read
    Read of a single AC97 register.
    Returns the register value or a negative error code.

.. _`ac97_controller_ops.description`:

Description
-----------

These are the basic operation an AC97 controller must provide for an AC97
access functions. Amongst these, all but the last 2 are mandatory.
The slot number is also known as the AC97 codec number, between 0 and 3.

.. This file was automatic generated / don't edit.


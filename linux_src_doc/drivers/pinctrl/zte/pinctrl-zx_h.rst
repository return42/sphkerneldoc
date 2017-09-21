.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/zte/pinctrl-zx.h

.. _`zx_mux_desc`:

struct zx_mux_desc
==================

.. c:type:: struct zx_mux_desc

    hardware mux descriptor

.. _`zx_mux_desc.definition`:

Definition
----------

.. code-block:: c

    struct zx_mux_desc {
        const char *name;
        u8 muxval;
    }

.. _`zx_mux_desc.members`:

Members
-------

name
    mux function name

muxval
    mux register bit value

.. _`zx_pin_data`:

struct zx_pin_data
==================

.. c:type:: struct zx_pin_data

    hardware per-pin data

.. _`zx_pin_data.definition`:

Definition
----------

.. code-block:: c

    struct zx_pin_data {
        bool aon_pin;
        u16 offset;
        u16 bitpos;
        u16 width;
        u16 coffset;
        u16 cbitpos;
        struct zx_mux_desc *muxes;
    }

.. _`zx_pin_data.members`:

Members
-------

aon_pin
    whether it's an AON pin

offset
    register offset within TOP pinmux controller

bitpos
    bit position within TOP pinmux register

width
    bit width within TOP pinmux register

coffset
    pinconf register offset within AON controller

cbitpos
    pinconf bit position within AON register

muxes
    available mux function names and corresponding register values

.. _`zx_pin_data.description`:

Description
-----------

Unlike TOP pinmux and AON pinconf registers which are arranged pretty
arbitrarily, AON pinmux register bits are well organized per pin id, and
each pin occupies two bits, so that we can calculate the AON register offset
and bit position from pin id.  Thus, we only need to define TOP pinmux and
AON pinconf register data for the pin.

.. This file was automatic generated / don't edit.


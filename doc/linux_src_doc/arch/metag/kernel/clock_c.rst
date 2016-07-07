.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/metag/kernel/clock.c

.. _`init_metag_core_clock`:

init_metag_core_clock
=====================

.. c:function:: void init_metag_core_clock( void)

    Set up core clock from devicetree.

    :param  void:
        no arguments

.. _`init_metag_core_clock.description`:

Description
-----------

Checks to see if a "core" clock is provided in the device tree, and overrides
the get_core_freq callback to use it.

.. _`init_metag_clocks`:

init_metag_clocks
=================

.. c:function:: void init_metag_clocks( void)

    Set up clocks from devicetree.

    :param  void:
        no arguments

.. _`init_metag_clocks.description`:

Description
-----------

Set up important clocks from device tree. In particular any needed for clock
sources.

.. _`setup_meta_clocks`:

setup_meta_clocks
=================

.. c:function:: void setup_meta_clocks(struct meta_clock_desc *desc)

    Early set up of the Meta clock.

    :param struct meta_clock_desc \*desc:
        Clock descriptor usually provided by machine description

.. _`setup_meta_clocks.description`:

Description
-----------

Ensures all callbacks are valid.

.. This file was automatic generated / don't edit.


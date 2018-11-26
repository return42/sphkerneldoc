.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/zynqmp/clk-mux-zynqmp.c

.. _`zynqmp_clk_mux`:

struct zynqmp_clk_mux
=====================

.. c:type:: struct zynqmp_clk_mux

    multiplexer clock

.. _`zynqmp_clk_mux.definition`:

Definition
----------

.. code-block:: c

    struct zynqmp_clk_mux {
        struct clk_hw hw;
        u8 flags;
        u32 clk_id;
    }

.. _`zynqmp_clk_mux.members`:

Members
-------

hw
    handle between common and hardware-specific interfaces

flags
    hardware-specific flags

clk_id
    Id of clock

.. _`zynqmp_clk_mux_get_parent`:

zynqmp_clk_mux_get_parent
=========================

.. c:function:: u8 zynqmp_clk_mux_get_parent(struct clk_hw *hw)

    Get parent of clock

    :param hw:
        handle between common and hardware-specific interfaces
    :type hw: struct clk_hw \*

.. _`zynqmp_clk_mux_get_parent.return`:

Return
------

Parent index

.. _`zynqmp_clk_mux_set_parent`:

zynqmp_clk_mux_set_parent
=========================

.. c:function:: int zynqmp_clk_mux_set_parent(struct clk_hw *hw, u8 index)

    Set parent of clock

    :param hw:
        handle between common and hardware-specific interfaces
    :type hw: struct clk_hw \*

    :param index:
        Parent index
    :type index: u8

.. _`zynqmp_clk_mux_set_parent.return`:

Return
------

0 on success else error+reason

.. _`zynqmp_clk_register_mux`:

zynqmp_clk_register_mux
=======================

.. c:function:: struct clk_hw *zynqmp_clk_register_mux(const char *name, u32 clk_id, const char * const *parents, u8 num_parents, const struct clock_topology *nodes)

    Register a mux table with the clock framework

    :param name:
        Name of this clock
    :type name: const char \*

    :param clk_id:
        Id of this clock
    :type clk_id: u32

    :param parents:
        Name of this clock's parents
    :type parents: const char \* const \*

    :param num_parents:
        Number of parents
    :type num_parents: u8

    :param nodes:
        Clock topology node
    :type nodes: const struct clock_topology \*

.. _`zynqmp_clk_register_mux.return`:

Return
------

clock hardware of the registered clock mux

.. This file was automatic generated / don't edit.


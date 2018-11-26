.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/zynqmp/clk-gate-zynqmp.c

.. _`zynqmp_clk_gate`:

struct zynqmp_clk_gate
======================

.. c:type:: struct zynqmp_clk_gate

    gating clock

.. _`zynqmp_clk_gate.definition`:

Definition
----------

.. code-block:: c

    struct zynqmp_clk_gate {
        struct clk_hw hw;
        u8 flags;
        u32 clk_id;
    }

.. _`zynqmp_clk_gate.members`:

Members
-------

hw
    handle between common and hardware-specific interfaces

flags
    hardware-specific flags

clk_id
    Id of clock

.. _`zynqmp_clk_gate_enable`:

zynqmp_clk_gate_enable
======================

.. c:function:: int zynqmp_clk_gate_enable(struct clk_hw *hw)

    Enable clock

    :param hw:
        handle between common and hardware-specific interfaces
    :type hw: struct clk_hw \*

.. _`zynqmp_clk_gate_enable.return`:

Return
------

0 on success else error code

.. _`zynqmp_clk_gate_is_enabled`:

zynqmp_clk_gate_is_enabled
==========================

.. c:function:: int zynqmp_clk_gate_is_enabled(struct clk_hw *hw)

    Check clock state

    :param hw:
        handle between common and hardware-specific interfaces
    :type hw: struct clk_hw \*

.. _`zynqmp_clk_gate_is_enabled.return`:

Return
------

1 if enabled, 0 if disabled else error code

.. _`zynqmp_clk_register_gate`:

zynqmp_clk_register_gate
========================

.. c:function:: struct clk_hw *zynqmp_clk_register_gate(const char *name, u32 clk_id, const char * const *parents, u8 num_parents, const struct clock_topology *nodes)

    Register a gate clock with the clock framework

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

.. _`zynqmp_clk_register_gate.return`:

Return
------

clock hardware of the registered clock gate

.. This file was automatic generated / don't edit.


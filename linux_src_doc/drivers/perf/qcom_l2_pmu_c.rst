.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/perf/qcom_l2_pmu.c

.. _`set_l2_indirect_reg`:

set_l2_indirect_reg
===================

.. c:function:: void set_l2_indirect_reg(u64 reg, u64 val)

    write value to an L2 register

    :param reg:
        Address of L2 register.
    :type reg: u64

    :param val:
        *undescribed*
    :type val: u64

.. _`set_l2_indirect_reg.description`:

Description
-----------

Use architecturally required barriers for ordering between system register
accesses

.. _`get_l2_indirect_reg`:

get_l2_indirect_reg
===================

.. c:function:: u64 get_l2_indirect_reg(u64 reg)

    read an L2 register value

    :param reg:
        Address of L2 register.
    :type reg: u64

.. _`get_l2_indirect_reg.description`:

Description
-----------

Use architecturally required barriers for ordering between system register
accesses

.. This file was automatic generated / don't edit.


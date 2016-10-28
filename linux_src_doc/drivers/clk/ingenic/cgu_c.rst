.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/ingenic/cgu.c

.. _`ingenic_cgu_gate_get`:

ingenic_cgu_gate_get
====================

.. c:function:: bool ingenic_cgu_gate_get(struct ingenic_cgu *cgu, const struct ingenic_cgu_gate_info *info)

    get the value of clock gate register bit

    :param struct ingenic_cgu \*cgu:
        reference to the CGU whose registers should be read

    :param const struct ingenic_cgu_gate_info \*info:
        info struct describing the gate bit

.. _`ingenic_cgu_gate_get.description`:

Description
-----------

Retrieves the state of the clock gate bit described by info. The
caller must hold cgu->lock.

.. _`ingenic_cgu_gate_get.return`:

Return
------

true if the gate bit is set, else false.

.. _`ingenic_cgu_gate_set`:

ingenic_cgu_gate_set
====================

.. c:function:: void ingenic_cgu_gate_set(struct ingenic_cgu *cgu, const struct ingenic_cgu_gate_info *info, bool val)

    set the value of clock gate register bit

    :param struct ingenic_cgu \*cgu:
        reference to the CGU whose registers should be modified

    :param const struct ingenic_cgu_gate_info \*info:
        info struct describing the gate bit

    :param bool val:
        non-zero to gate a clock, otherwise zero

.. _`ingenic_cgu_gate_set.description`:

Description
-----------

Sets the given gate bit in order to gate or ungate a clock.

The caller must hold cgu->lock.

.. This file was automatic generated / don't edit.


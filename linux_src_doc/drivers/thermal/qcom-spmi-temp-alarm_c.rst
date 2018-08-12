.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thermal/qcom-spmi-temp-alarm.c

.. _`qpnp_tm_get_temp_stage`:

qpnp_tm_get_temp_stage
======================

.. c:function:: int qpnp_tm_get_temp_stage(struct qpnp_tm_chip *chip)

    return over-temperature stage

    :param struct qpnp_tm_chip \*chip:
        Pointer to the qpnp_tm chip

.. _`qpnp_tm_get_temp_stage.return`:

Return
------

stage (GEN1) or state (GEN2) on success, or errno on failure.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ptp/ptp_qoriq.c

.. _`qoriq_ptp_nominal_freq`:

qoriq_ptp_nominal_freq
======================

.. c:function:: u32 qoriq_ptp_nominal_freq(u32 clk_src)

    calculate nominal frequency according to reference clock frequency

    :param clk_src:
        reference clock frequency
    :type clk_src: u32

.. _`qoriq_ptp_nominal_freq.description`:

Description
-----------

The nominal frequency is the desired clock frequency.
It should be less than the reference clock frequency.
It should be a factor of 1000MHz.

Return the nominal frequency

.. _`qoriq_ptp_auto_config`:

qoriq_ptp_auto_config
=====================

.. c:function:: int qoriq_ptp_auto_config(struct qoriq_ptp *qoriq_ptp, struct device_node *node)

    calculate a set of default configurations

    :param qoriq_ptp:
        pointer to qoriq_ptp
    :type qoriq_ptp: struct qoriq_ptp \*

    :param node:
        pointer to device_node
    :type node: struct device_node \*

.. _`qoriq_ptp_auto_config.description`:

Description
-----------

If below dts properties are not provided, this function will be
called to calculate a set of default configurations for them.
"fsl,tclk-period"
"fsl,tmr-prsc"
"fsl,tmr-add"
"fsl,tmr-fiper1"
"fsl,tmr-fiper2"
"fsl,max-adj"

Return 0 if success

.. This file was automatic generated / don't edit.


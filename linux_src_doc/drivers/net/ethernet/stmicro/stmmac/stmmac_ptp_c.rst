.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/stmicro/stmmac/stmmac_ptp.c

.. _`stmmac_adjust_freq`:

stmmac_adjust_freq
==================

.. c:function:: int stmmac_adjust_freq(struct ptp_clock_info *ptp, s32 ppb)

    :param ptp:
        pointer to ptp_clock_info structure
    :type ptp: struct ptp_clock_info \*

    :param ppb:
        desired period change in parts ber billion
    :type ppb: s32

.. _`stmmac_adjust_freq.description`:

Description
-----------

this function will adjust the frequency of hardware clock.

.. _`stmmac_adjust_time`:

stmmac_adjust_time
==================

.. c:function:: int stmmac_adjust_time(struct ptp_clock_info *ptp, s64 delta)

    :param ptp:
        pointer to ptp_clock_info structure
    :type ptp: struct ptp_clock_info \*

    :param delta:
        desired change in nanoseconds
    :type delta: s64

.. _`stmmac_adjust_time.description`:

Description
-----------

this function will shift/adjust the hardware clock time.

.. _`stmmac_get_time`:

stmmac_get_time
===============

.. c:function:: int stmmac_get_time(struct ptp_clock_info *ptp, struct timespec64 *ts)

    :param ptp:
        pointer to ptp_clock_info structure
    :type ptp: struct ptp_clock_info \*

    :param ts:
        pointer to hold time/result
    :type ts: struct timespec64 \*

.. _`stmmac_get_time.description`:

Description
-----------

this function will read the current time from the
hardware clock and store it in \ ``ts``\ .

.. _`stmmac_set_time`:

stmmac_set_time
===============

.. c:function:: int stmmac_set_time(struct ptp_clock_info *ptp, const struct timespec64 *ts)

    :param ptp:
        pointer to ptp_clock_info structure
    :type ptp: struct ptp_clock_info \*

    :param ts:
        time value to set
    :type ts: const struct timespec64 \*

.. _`stmmac_set_time.description`:

Description
-----------

this function will set the current time on the
hardware clock.

.. _`stmmac_ptp_register`:

stmmac_ptp_register
===================

.. c:function:: void stmmac_ptp_register(struct stmmac_priv *priv)

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

.. _`stmmac_ptp_register.description`:

Description
-----------

this function will register the ptp clock driver
to kernel. It also does some house keeping work.

.. _`stmmac_ptp_unregister`:

stmmac_ptp_unregister
=====================

.. c:function:: void stmmac_ptp_unregister(struct stmmac_priv *priv)

    :param priv:
        driver private structure
    :type priv: struct stmmac_priv \*

.. _`stmmac_ptp_unregister.description`:

Description
-----------

this function will remove/unregister the ptp clock driver
from the kernel.

.. This file was automatic generated / don't edit.


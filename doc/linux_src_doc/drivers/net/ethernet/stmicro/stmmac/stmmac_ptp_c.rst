.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/stmicro/stmmac/stmmac_ptp.c

.. _`stmmac_adjust_freq`:

stmmac_adjust_freq
==================

.. c:function:: int stmmac_adjust_freq(struct ptp_clock_info *ptp, s32 ppb)

    :param struct ptp_clock_info \*ptp:
        pointer to ptp_clock_info structure

    :param s32 ppb:
        desired period change in parts ber billion

.. _`stmmac_adjust_freq.description`:

Description
-----------

this function will adjust the frequency of hardware clock.

.. _`stmmac_adjust_time`:

stmmac_adjust_time
==================

.. c:function:: int stmmac_adjust_time(struct ptp_clock_info *ptp, s64 delta)

    :param struct ptp_clock_info \*ptp:
        pointer to ptp_clock_info structure

    :param s64 delta:
        desired change in nanoseconds

.. _`stmmac_adjust_time.description`:

Description
-----------

this function will shift/adjust the hardware clock time.

.. _`stmmac_get_time`:

stmmac_get_time
===============

.. c:function:: int stmmac_get_time(struct ptp_clock_info *ptp, struct timespec64 *ts)

    :param struct ptp_clock_info \*ptp:
        pointer to ptp_clock_info structure

    :param struct timespec64 \*ts:
        pointer to hold time/result

.. _`stmmac_get_time.description`:

Description
-----------

this function will read the current time from the
hardware clock and store it in \ ``ts``\ .

.. _`stmmac_set_time`:

stmmac_set_time
===============

.. c:function:: int stmmac_set_time(struct ptp_clock_info *ptp, const struct timespec64 *ts)

    :param struct ptp_clock_info \*ptp:
        pointer to ptp_clock_info structure

    :param const struct timespec64 \*ts:
        time value to set

.. _`stmmac_set_time.description`:

Description
-----------

this function will set the current time on the
hardware clock.

.. _`stmmac_ptp_register`:

stmmac_ptp_register
===================

.. c:function:: int stmmac_ptp_register(struct stmmac_priv *priv)

    :param struct stmmac_priv \*priv:
        driver private structure

.. _`stmmac_ptp_register.description`:

Description
-----------

this function will register the ptp clock driver
to kernel. It also does some house keeping work.

.. _`stmmac_ptp_unregister`:

stmmac_ptp_unregister
=====================

.. c:function:: void stmmac_ptp_unregister(struct stmmac_priv *priv)

    :param struct stmmac_priv \*priv:
        driver private structure

.. _`stmmac_ptp_unregister.description`:

Description
-----------

this function will remove/unregister the ptp clock driver
from the kernel.

.. This file was automatic generated / don't edit.


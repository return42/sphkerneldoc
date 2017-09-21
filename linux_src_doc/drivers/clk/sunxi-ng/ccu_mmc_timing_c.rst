.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/sunxi-ng/ccu_mmc_timing.c

.. _`sunxi_ccu_set_mmc_timing_mode`:

sunxi_ccu_set_mmc_timing_mode
=============================

.. c:function:: int sunxi_ccu_set_mmc_timing_mode(struct clk *clk, bool new_mode)

    Configure the MMC clock timing mode

    :param struct clk \*clk:
        clock to be configured

    :param bool new_mode:
        true for new timing mode introduced in A83T and later

.. _`sunxi_ccu_set_mmc_timing_mode.description`:

Description
-----------

Returns 0 on success, -ENOTSUPP if the clock does not support
switching modes.

.. _`sunxi_ccu_get_mmc_timing_mode`:

sunxi_ccu_get_mmc_timing_mode
=============================

.. c:function:: int sunxi_ccu_get_mmc_timing_mode(struct clk *clk)

    Get the current MMC clock timing mode

    :param struct clk \*clk:
        clock to query

.. _`sunxi_ccu_get_mmc_timing_mode.description`:

Description
-----------

Returns 0 if the clock is in old timing mode, > 0 if it is in
new timing mode, and -ENOTSUPP if the clock does not support
this function.

.. This file was automatic generated / don't edit.


.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/memory/omap-gpmc.c

.. _`gpmc_get_clk_period`:

gpmc_get_clk_period
===================

.. c:function:: unsigned long gpmc_get_clk_period(int cs, enum gpmc_clk_domain cd)

    get period of selected clock domain in ps \ ``cs``\  Chip Select Region. \ ``cd``\  Clock Domain.

    :param int cs:
        *undescribed*

    :param enum gpmc_clk_domain cd:
        *undescribed*

.. _`gpmc_get_clk_period.description`:

Description
-----------

GPMC_CS_CONFIG1 GPMCFCLKDIVIDER for cs has to be setup
prior to calling this function with GPMC_CD_CLK.

.. _`get_gpmc_timing_reg`:

get_gpmc_timing_reg
===================

.. c:function:: int get_gpmc_timing_reg(int cs, int reg, int st_bit, int end_bit, int max, const char *name, const enum gpmc_clk_domain cd, int shift, bool raw, bool noval)

    read a timing parameter and print DTS settings for it.

    :param int cs:
        Chip Select Region

    :param int reg:
        GPMC_CS_CONFIGn register offset.

    :param int st_bit:
        Start Bit

    :param int end_bit:
        End Bit. Must be >= \ ``st_bit``\ .

    :param int max:
        *undescribed*

    :param const char \*name:
        DTS node name, w/o "gpmc,"

    :param const enum gpmc_clk_domain cd:
        Clock Domain of timing parameter.

    :param int shift:
        Parameter value left shifts \ ``shift``\ , which is then printed instead of value.

    :param bool raw:
        Raw Format Option.
        raw format:  gpmc,name = <value>
        tick format: gpmc,name = <value> /\ :c:type:`struct zwj <zwj>`;\* x ns -- y ns; x ticks \*\ :c:type:`struct zwj <zwj>`;/
        Where x ns -- y ns result in the same tick value.
        When \ ``max``\  is exceeded, "invalid" is printed inside comment.

    :param bool noval:
        Parameter values equal to 0 are not printed.

.. _`set_gpmc_timing_reg`:

set_gpmc_timing_reg
===================

.. c:function:: int set_gpmc_timing_reg(int cs, int reg, int st_bit, int end_bit, int max, int time, enum gpmc_clk_domain cd, const char *name)

    set a single timing parameter for Chip Select Region. Caller is expected to have initialized CONFIG1 GPMCFCLKDIVIDER prior to calling this function with \ ``cd``\  equal to GPMC_CD_CLK.

    :param int cs:
        Chip Select Region.

    :param int reg:
        GPMC_CS_CONFIGn register offset.

    :param int st_bit:
        Start Bit

    :param int end_bit:
        End Bit. Must be >= \ ``st_bit``\ .

    :param int max:
        Maximum parameter value.
        If 0, maximum is as high as \ ``st_bit``\  and \ ``end_bit``\  allow.

    :param int time:
        Timing parameter in ns.

    :param enum gpmc_clk_domain cd:
        Timing parameter clock domain.

    :param const char \*name:
        Timing parameter name.

.. _`gpmc_calc_waitmonitoring_divider`:

gpmc_calc_waitmonitoring_divider
================================

.. c:function:: int gpmc_calc_waitmonitoring_divider(unsigned int wait_monitoring)

    calculate proper GPMCFCLKDIVIDER based on WAITMONITORINGTIME WAITMONITORINGTIME will be \_at least\_ as long as desired, i.e. read  --> don't sample bus too early write --> data is longer on bus

    :param unsigned int wait_monitoring:
        WAITMONITORINGTIME in ns.

.. _`gpmc_calc_waitmonitoring_divider.formula`:

Formula
-------

gpmc_clk_div + 1 = ceil(ceil(waitmonitoringtime_ns / gpmc_fclk_ns)
/ waitmonitoring_ticks)
WAITMONITORINGTIME resulting in 0 or 1 tick with div = 1 are caught by
div <= 0 check.

.. _`gpmc_calc_divider`:

gpmc_calc_divider
=================

.. c:function:: int gpmc_calc_divider(unsigned int sync_clk)

    calculate GPMC_FCLK divider for sync_clk GPMC_CLK period.

    :param unsigned int sync_clk:
        GPMC_CLK period in ps.

.. _`gpmc_cs_set_timings`:

gpmc_cs_set_timings
===================

.. c:function:: int gpmc_cs_set_timings(int cs, const struct gpmc_timings *t, const struct gpmc_settings *s)

    program timing parameters for Chip Select Region.

    :param int cs:
        Chip Select Region.

    :param const struct gpmc_timings \*t:
        GPMC timing parameters.

    :param const struct gpmc_settings \*s:
        GPMC timing settings.

.. _`gpmc_cs_remap`:

gpmc_cs_remap
=============

.. c:function:: int gpmc_cs_remap(int cs, u32 base)

    remaps a chip-select physical base address

    :param int cs:
        chip-select to remap

    :param u32 base:
        physical base address to re-map chip-select to

.. _`gpmc_cs_remap.description`:

Description
-----------

Re-maps a chip-select to a new physical base address specified by
"base". Returns 0 on success and appropriate negative error code
on failure.

.. _`gpmc_configure`:

gpmc_configure
==============

.. c:function:: int gpmc_configure(int cmd, int wval)

    write request to configure gpmc

    :param int cmd:
        command type

    :param int wval:
        value to write
        \ ``return``\  status of the operation

.. _`gpmc_omap_get_nand_ops`:

gpmc_omap_get_nand_ops
======================

.. c:function:: struct gpmc_nand_ops *gpmc_omap_get_nand_ops(struct gpmc_nand_regs *reg, int cs)

    Get the GPMC NAND interface

    :param struct gpmc_nand_regs \*reg:
        *undescribed*

    :param int cs:
        GPMC chip select number on which the NAND sits. The
        register map returned will be specific to this chip select.

.. _`gpmc_omap_get_nand_ops.description`:

Description
-----------

Returns NULL on error e.g. invalid cs.

.. _`gpmc_cs_program_settings`:

gpmc_cs_program_settings
========================

.. c:function:: int gpmc_cs_program_settings(int cs, struct gpmc_settings *p)

    programs non-timing related settings

    :param int cs:
        GPMC chip-select to program

    :param struct gpmc_settings \*p:
        pointer to GPMC settings structure

.. _`gpmc_cs_program_settings.description`:

Description
-----------

Programs non-timing related settings for a GPMC chip-select, such as
bus-width, burst configuration, etc. Function should be called once
for each chip-select that is being used and must be called before
calling \ :c:func:`gpmc_cs_set_timings`\  as timing parameters in the CONFIG1
register will be initialised to zero by this function. Returns 0 on
success and appropriate negative error code on failure.

.. _`gpmc_read_settings_dt`:

gpmc_read_settings_dt
=====================

.. c:function:: void gpmc_read_settings_dt(struct device_node *np, struct gpmc_settings *p)

    read gpmc settings from device-tree

    :param struct device_node \*np:
        pointer to device-tree node for a gpmc child device

    :param struct gpmc_settings \*p:
        pointer to gpmc settings structure

.. _`gpmc_read_settings_dt.description`:

Description
-----------

Reads the GPMC settings for a GPMC child device from device-tree and
stores them in the GPMC settings structure passed. The GPMC settings
structure is initialised to zero by this function and so any
previously stored settings will be cleared.

.. _`gpmc_probe_generic_child`:

gpmc_probe_generic_child
========================

.. c:function:: int gpmc_probe_generic_child(struct platform_device *pdev, struct device_node *child)

    configures the gpmc for a child device

    :param struct platform_device \*pdev:
        pointer to gpmc platform device

    :param struct device_node \*child:
        pointer to device-tree node for child device

.. _`gpmc_probe_generic_child.description`:

Description
-----------

Allocates and configures a GPMC chip-select for a child device.
Returns 0 on success and appropriate negative error code on failure.

.. This file was automatic generated / don't edit.


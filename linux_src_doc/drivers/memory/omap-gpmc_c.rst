.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/memory/omap-gpmc.c

.. _`gpmc_get_clk_period`:

gpmc_get_clk_period
===================

.. c:function:: unsigned long gpmc_get_clk_period(int cs, enum gpmc_clk_domain cd)

    get period of selected clock domain in ps \ ``cs``\  Chip Select Region. \ ``cd``\  Clock Domain.

    :param cs:
        *undescribed*
    :type cs: int

    :param cd:
        *undescribed*
    :type cd: enum gpmc_clk_domain

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

    :param cs:
        Chip Select Region
    :type cs: int

    :param reg:
        GPMC_CS_CONFIGn register offset.
    :type reg: int

    :param st_bit:
        Start Bit
    :type st_bit: int

    :param end_bit:
        End Bit. Must be >= \ ``st_bit``\ .
    :type end_bit: int

    :param max:
        *undescribed*
    :type max: int

    :param name:
        DTS node name, w/o "gpmc,"
    :type name: const char \*

    :param cd:
        Clock Domain of timing parameter.
    :type cd: const enum gpmc_clk_domain

    :param shift:
        Parameter value left shifts \ ``shift``\ , which is then printed instead of value.
    :type shift: int

    :param raw:
        Raw Format Option.
        raw format:  gpmc,name = <value>
        tick format: gpmc,name = <value> /&zwj;\* x ns -- y ns; x ticks \*&zwj;/
        Where x ns -- y ns result in the same tick value.
        When \ ``max``\  is exceeded, "invalid" is printed inside comment.
    :type raw: bool

    :param noval:
        Parameter values equal to 0 are not printed.
    :type noval: bool

.. _`set_gpmc_timing_reg`:

set_gpmc_timing_reg
===================

.. c:function:: int set_gpmc_timing_reg(int cs, int reg, int st_bit, int end_bit, int max, int time, enum gpmc_clk_domain cd, const char *name)

    set a single timing parameter for Chip Select Region. Caller is expected to have initialized CONFIG1 GPMCFCLKDIVIDER prior to calling this function with \ ``cd``\  equal to GPMC_CD_CLK.

    :param cs:
        Chip Select Region.
    :type cs: int

    :param reg:
        GPMC_CS_CONFIGn register offset.
    :type reg: int

    :param st_bit:
        Start Bit
    :type st_bit: int

    :param end_bit:
        End Bit. Must be >= \ ``st_bit``\ .
    :type end_bit: int

    :param max:
        Maximum parameter value.
        If 0, maximum is as high as \ ``st_bit``\  and \ ``end_bit``\  allow.
    :type max: int

    :param time:
        Timing parameter in ns.
    :type time: int

    :param cd:
        Timing parameter clock domain.
    :type cd: enum gpmc_clk_domain

    :param name:
        Timing parameter name.
    :type name: const char \*

.. _`gpmc_calc_waitmonitoring_divider`:

gpmc_calc_waitmonitoring_divider
================================

.. c:function:: int gpmc_calc_waitmonitoring_divider(unsigned int wait_monitoring)

    calculate proper GPMCFCLKDIVIDER based on WAITMONITORINGTIME WAITMONITORINGTIME will be \_at least\_ as long as desired, i.e. read  --> don't sample bus too early write --> data is longer on bus

    :param wait_monitoring:
        WAITMONITORINGTIME in ns.
    :type wait_monitoring: unsigned int

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

    :param sync_clk:
        GPMC_CLK period in ps.
    :type sync_clk: unsigned int

.. _`gpmc_cs_set_timings`:

gpmc_cs_set_timings
===================

.. c:function:: int gpmc_cs_set_timings(int cs, const struct gpmc_timings *t, const struct gpmc_settings *s)

    program timing parameters for Chip Select Region.

    :param cs:
        Chip Select Region.
    :type cs: int

    :param t:
        GPMC timing parameters.
    :type t: const struct gpmc_timings \*

    :param s:
        GPMC timing settings.
    :type s: const struct gpmc_settings \*

.. _`gpmc_cs_remap`:

gpmc_cs_remap
=============

.. c:function:: int gpmc_cs_remap(int cs, u32 base)

    remaps a chip-select physical base address

    :param cs:
        chip-select to remap
    :type cs: int

    :param base:
        physical base address to re-map chip-select to
    :type base: u32

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

    :param cmd:
        command type
    :type cmd: int

    :param wval:
        value to write
        \ ``return``\  status of the operation
    :type wval: int

.. _`gpmc_omap_get_nand_ops`:

gpmc_omap_get_nand_ops
======================

.. c:function:: struct gpmc_nand_ops *gpmc_omap_get_nand_ops(struct gpmc_nand_regs *reg, int cs)

    Get the GPMC NAND interface

    :param reg:
        *undescribed*
    :type reg: struct gpmc_nand_regs \*

    :param cs:
        GPMC chip select number on which the NAND sits. The
        register map returned will be specific to this chip select.
    :type cs: int

.. _`gpmc_omap_get_nand_ops.description`:

Description
-----------

Returns NULL on error e.g. invalid cs.

.. _`gpmc_cs_program_settings`:

gpmc_cs_program_settings
========================

.. c:function:: int gpmc_cs_program_settings(int cs, struct gpmc_settings *p)

    programs non-timing related settings

    :param cs:
        GPMC chip-select to program
    :type cs: int

    :param p:
        pointer to GPMC settings structure
    :type p: struct gpmc_settings \*

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

    :param np:
        pointer to device-tree node for a gpmc child device
    :type np: struct device_node \*

    :param p:
        pointer to gpmc settings structure
    :type p: struct gpmc_settings \*

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

    :param pdev:
        pointer to gpmc platform device
    :type pdev: struct platform_device \*

    :param child:
        pointer to device-tree node for child device
    :type child: struct device_node \*

.. _`gpmc_probe_generic_child.description`:

Description
-----------

Allocates and configures a GPMC chip-select for a child device.
Returns 0 on success and appropriate negative error code on failure.

.. This file was automatic generated / don't edit.


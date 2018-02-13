.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/host/sdhci-of-arasan.c

.. _`sdhci_arasan_soc_ctl_field`:

struct sdhci_arasan_soc_ctl_field
=================================

.. c:type:: struct sdhci_arasan_soc_ctl_field

    Field used in sdhci_arasan_soc_ctl_map

.. _`sdhci_arasan_soc_ctl_field.definition`:

Definition
----------

.. code-block:: c

    struct sdhci_arasan_soc_ctl_field {
        u32 reg;
        u16 width;
        s16 shift;
    }

.. _`sdhci_arasan_soc_ctl_field.members`:

Members
-------

reg
    Offset within the syscon of the register containing this field

width
    Number of bits for this field

shift
    Bit offset within \ ``reg``\  of this field (or -1 if not avail)

.. _`sdhci_arasan_soc_ctl_map`:

struct sdhci_arasan_soc_ctl_map
===============================

.. c:type:: struct sdhci_arasan_soc_ctl_map

    Map in syscon to corecfg registers

.. _`sdhci_arasan_soc_ctl_map.definition`:

Definition
----------

.. code-block:: c

    struct sdhci_arasan_soc_ctl_map {
        struct sdhci_arasan_soc_ctl_field baseclkfreq;
        struct sdhci_arasan_soc_ctl_field clockmultiplier;
        bool hiword_update;
    }

.. _`sdhci_arasan_soc_ctl_map.members`:

Members
-------

baseclkfreq
    Where to find corecfg_baseclkfreq

clockmultiplier
    Where to find corecfg_clockmultiplier

hiword_update
    If true, use HIWORD_UPDATE to access the syscon

.. _`sdhci_arasan_soc_ctl_map.description`:

Description
-----------

It's up to the licensee of the Arsan IP block to make these available
somewhere if needed.  Presumably these will be scattered somewhere that's
accessible via the syscon API.

.. _`sdhci_arasan_data`:

struct sdhci_arasan_data
========================

.. c:type:: struct sdhci_arasan_data


.. _`sdhci_arasan_data.definition`:

Definition
----------

.. code-block:: c

    struct sdhci_arasan_data {
        struct sdhci_host *host;
        struct clk *clk_ahb;
        struct phy *phy;
        bool is_phy_on;
        bool has_cqe;
        struct clk_hw sdcardclk_hw;
        struct clk *sdcardclk;
        struct regmap *soc_ctl_base;
        const struct sdhci_arasan_soc_ctl_map *soc_ctl_map;
        unsigned int quirks;
    #define SDHCI_ARASAN_QUIRK_FORCE_CDTEST BIT(0)
    }

.. _`sdhci_arasan_data.members`:

Members
-------

host
    Pointer to the main SDHCI host structure.

clk_ahb
    Pointer to the AHB clock

phy
    Pointer to the generic phy

is_phy_on
    True if the PHY is on; false if not.

has_cqe
    *undescribed*

sdcardclk_hw
    Struct for the clock we might provide to a PHY.

sdcardclk
    Pointer to normal 'struct clock' for sdcardclk_hw.

soc_ctl_base
    Pointer to regmap for syscon for soc_ctl registers.

soc_ctl_map
    Map to get offsets into soc_ctl registers.

quirks
    *undescribed*

.. _`sdhci_arasan_syscon_write`:

sdhci_arasan_syscon_write
=========================

.. c:function:: int sdhci_arasan_syscon_write(struct sdhci_host *host, const struct sdhci_arasan_soc_ctl_field *fld, u32 val)

    Write to a field in soc_ctl registers

    :param struct sdhci_host \*host:
        The sdhci_host

    :param const struct sdhci_arasan_soc_ctl_field \*fld:
        The field to write to

    :param u32 val:
        The value to write

.. _`sdhci_arasan_syscon_write.description`:

Description
-----------

This function allows writing to fields in sdhci_arasan_soc_ctl_map.
Note that if a field is specified as not available (shift < 0) then
this function will silently return an error code.  It will be noisy
and print errors for any other (unexpected) errors.

.. _`sdhci_arasan_suspend`:

sdhci_arasan_suspend
====================

.. c:function:: int sdhci_arasan_suspend(struct device *dev)

    Suspend method for the driver

    :param struct device \*dev:
        Address of the device structure
        Returns 0 on success and error value on error

.. _`sdhci_arasan_suspend.description`:

Description
-----------

Put the device in a low power state.

.. _`sdhci_arasan_resume`:

sdhci_arasan_resume
===================

.. c:function:: int sdhci_arasan_resume(struct device *dev)

    Resume method for the driver

    :param struct device \*dev:
        Address of the device structure
        Returns 0 on success and error value on error

.. _`sdhci_arasan_resume.description`:

Description
-----------

Resume operation after suspend

.. _`sdhci_arasan_sdcardclk_recalc_rate`:

sdhci_arasan_sdcardclk_recalc_rate
==================================

.. c:function:: unsigned long sdhci_arasan_sdcardclk_recalc_rate(struct clk_hw *hw, unsigned long parent_rate)

    Return the card clock rate

    :param struct clk_hw \*hw:
        Pointer to the hardware clock structure.
        \ ``parent_rate``\          The parent rate (should be rate of clk_xin).
        Returns the card clock rate.

    :param unsigned long parent_rate:
        *undescribed*

.. _`sdhci_arasan_sdcardclk_recalc_rate.description`:

Description
-----------

Return the current actual rate of the SD card clock.  This can be used
to communicate with out PHY.

.. _`sdhci_arasan_update_clockmultiplier`:

sdhci_arasan_update_clockmultiplier
===================================

.. c:function:: void sdhci_arasan_update_clockmultiplier(struct sdhci_host *host, u32 value)

    Set corecfg_clockmultiplier

    :param struct sdhci_host \*host:
        The sdhci_host

    :param u32 value:
        *undescribed*

.. _`sdhci_arasan_update_clockmultiplier.description`:

Description
-----------

The corecfg_clockmultiplier is supposed to contain clock multiplier
value of programmable clock generator.

.. _`sdhci_arasan_update_clockmultiplier.notes`:

NOTES
-----

- Many existing devices don't seem to do this and work fine.  To keep
compatibility for old hardware where the device tree doesn't provide a
register map, this function is a noop if a soc_ctl_map hasn't been provided
for this platform.
- The value of corecfg_clockmultiplier should sync with that of corresponding
value reading from sdhci_capability_register. So this function is called
once at probe time and never called again.

.. _`sdhci_arasan_update_baseclkfreq`:

sdhci_arasan_update_baseclkfreq
===============================

.. c:function:: void sdhci_arasan_update_baseclkfreq(struct sdhci_host *host)

    Set corecfg_baseclkfreq

    :param struct sdhci_host \*host:
        The sdhci_host

.. _`sdhci_arasan_update_baseclkfreq.description`:

Description
-----------

The corecfg_baseclkfreq is supposed to contain the MHz of clk_xin.  This
function can be used to make that happen.

.. _`sdhci_arasan_update_baseclkfreq.notes`:

NOTES
-----

- Many existing devices don't seem to do this and work fine.  To keep
compatibility for old hardware where the device tree doesn't provide a
register map, this function is a noop if a soc_ctl_map hasn't been provided
for this platform.
- It's assumed that clk_xin is not dynamic and that we use the SDHCI divider
to achieve lower clock rates.  That means that this function is called once
at probe time and never called again.

.. _`sdhci_arasan_register_sdclk`:

sdhci_arasan_register_sdclk
===========================

.. c:function:: int sdhci_arasan_register_sdclk(struct sdhci_arasan_data *sdhci_arasan, struct clk *clk_xin, struct device *dev)

    Register the sdclk for a PHY to use

    :param struct sdhci_arasan_data \*sdhci_arasan:
        Our private data structure.

    :param struct clk \*clk_xin:
        Pointer to the functional clock

    :param struct device \*dev:
        Pointer to our struct device.
        Returns 0 on success and error value on error

.. _`sdhci_arasan_register_sdclk.description`:

Description
-----------

Some PHY devices need to know what the actual card clock is.  In order for
them to find out, we'll provide a clock through the common clock framework
for them to query.

.. _`sdhci_arasan_register_sdclk.note`:

Note
----

without seriously re-architecting SDHCI's clock code and testing on
all platforms, there's no way to create a totally beautiful clock here
with all clock ops implemented.  Instead, we'll just create a clock that can
be queried and set the CLK_GET_RATE_NOCACHE attribute to tell common clock
framework that we're doing things behind its back.  This should be sufficient
to create nice clean device tree bindings and later (if needed) we can try
re-architecting SDHCI if we see some benefit to it.

.. _`sdhci_arasan_unregister_sdclk`:

sdhci_arasan_unregister_sdclk
=============================

.. c:function:: void sdhci_arasan_unregister_sdclk(struct device *dev)

    Undoes \ :c:func:`sdhci_arasan_register_sdclk`\ 

    :param struct device \*dev:
        Pointer to our struct device.

.. _`sdhci_arasan_unregister_sdclk.description`:

Description
-----------

Should be called any time we're exiting and \ :c:func:`sdhci_arasan_register_sdclk`\ 
returned success.

.. This file was automatic generated / don't edit.


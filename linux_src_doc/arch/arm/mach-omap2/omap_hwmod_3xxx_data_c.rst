.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/omap_hwmod_3xxx_data.c

.. _`omap3xxx_hwmod_is_hs_ip_block_usable`:

omap3xxx_hwmod_is_hs_ip_block_usable
====================================

.. c:function:: bool omap3xxx_hwmod_is_hs_ip_block_usable(struct device_node *bus, const char *dev_name)

    is a security IP block accessible?

    :param bus:
        struct device_node \* for the top-level OMAP DT data
    :type bus: struct device_node \*

    :param dev_name:
        device name used in the DT file
    :type dev_name: const char \*

.. _`omap3xxx_hwmod_is_hs_ip_block_usable.description`:

Description
-----------

Determine whether a "secure" IP block \ ``dev_name``\  is usable by Linux.
There doesn't appear to be a 100% reliable way to determine this,
so we rely on heuristics.  If \ ``bus``\  is null, meaning there's no DT
data, then we only assume the IP block is accessible if the OMAP is
fused as a 'general-purpose' SoC.  If however DT data is present,
test to see if the IP block is described in the DT data and set to
'status = "okay"'.  If so then we assume the ODM has configured the
OMAP firewalls to allow access to the IP block.

.. _`omap3xxx_hwmod_is_hs_ip_block_usable.return`:

Return
------

0 if device named \ ``dev_name``\  is not likely to be accessible,
or 1 if it is likely to be accessible.

.. This file was automatic generated / don't edit.


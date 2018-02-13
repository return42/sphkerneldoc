.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/sunxi/clk-a20-gmac.c

.. _`sun7i_a20_gmac_gpit`:

SUN7I_A20_GMAC_GPIT
===================

.. c:function::  SUN7I_A20_GMAC_GPIT()

    Setup function for A20/A31 GMAC clock module

.. _`sun7i_a20_gmac_gpit.description`:

Description
-----------

This clock looks something like this
\________________________
MII TX clock from PHY >-----\|__________\_    \_________\|----> to GMAC core
GMAC Int. RGMII TX clk >----\|___________\__/__gate---\|----> to PHY
Ext. 125MHz RGMII TX clk >--\|__divider__/            \|
\|________________________\|

The external 125 MHz reference is optional, i.e. GMAC can use its
internal TX clock just fine. The A31 GMAC clock module does not have
the divider controls for the external reference.

To keep it simple, let the GMAC use either the MII TX clock for MII mode,
and its internal TX clock for GMII and RGMII modes. The GMAC driver should
select the appropriate source and gate/ungate the output to the PHY.

Only the GMAC should use this clock. Altering the clock so that it doesn't
match the GMAC's operation parameters will result in the GMAC not being
able to send traffic out. The GMAC driver should set the clock rate and
enable/disable this clock to configure the required state. The clock
driver then responds by auto-reparenting the clock.

.. This file was automatic generated / don't edit.


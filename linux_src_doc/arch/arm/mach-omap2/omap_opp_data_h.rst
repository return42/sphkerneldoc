.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/omap_opp_data.h

.. _`omap_opp_def`:

struct omap_opp_def
===================

.. c:type:: struct omap_opp_def

    OMAP OPP Definition

.. _`omap_opp_def.definition`:

Definition
----------

.. code-block:: c

    struct omap_opp_def {
        char *hwmod_name;
        unsigned long freq;
        unsigned long u_volt;
        bool default_available;
    }

.. _`omap_opp_def.members`:

Members
-------

hwmod_name
    Name of the hwmod for this domain

freq
    Frequency in hertz corresponding to this OPP

u_volt
    Nominal voltage in microvolts corresponding to this OPP

default_available
    True/false - is this OPP available by default

.. _`omap_opp_def.description`:

Description
-----------

OMAP SOCs have a standard set of tuples consisting of frequency and voltage
pairs that the device will support per voltage domain. This is called
Operating Points or OPP. The actual definitions of OMAP Operating Points
varies over silicon within the same family of devices. For a specific
domain, you can have a set of {frequency, voltage} pairs and this is denoted
by an array of omap_opp_def. As the kernel boots and more information is
available, a set of these are activated based on the precise nature of
device the kernel boots up on. It is interesting to remember that each IP
which belongs to a voltage domain may define their own set of OPPs on top
of this - but this is handled by the appropriate driver.

.. This file was automatic generated / don't edit.


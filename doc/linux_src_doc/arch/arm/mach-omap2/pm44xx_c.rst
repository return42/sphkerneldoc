.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/pm44xx.c

.. _`static_dep_map`:

struct static_dep_map
=====================

.. c:type:: struct static_dep_map

    Static dependency map

.. _`static_dep_map.definition`:

Definition
----------

.. code-block:: c

    struct static_dep_map {
        const char *from;
        const char *to;
    }

.. _`static_dep_map.members`:

Members
-------

from
    from clockdomain

to
    to clockdomain

.. _`omap_default_idle`:

omap_default_idle
=================

.. c:function:: void omap_default_idle( void)

    OMAP4 default ilde routine.'

    :param  void:
        no arguments

.. _`omap_default_idle.description`:

Description
-----------

Implements OMAP4 memory, IO ordering requirements which can't be addressed
with default \ :c:func:`cpu_do_idle`\  hook. Used by all CPUs with !CONFIG_CPU_IDLE and
by secondary CPU with CONFIG_CPU_IDLE.

.. _`omap4plus_init_static_deps`:

omap4plus_init_static_deps
==========================

.. c:function:: int omap4plus_init_static_deps(const struct static_dep_map *map)

    Initialize a static dependency map

    :param const struct static_dep_map \*map:
        Mapping of clock domains

.. _`omap4_pm_init_early`:

omap4_pm_init_early
===================

.. c:function:: int omap4_pm_init_early( void)

    Does early initialization necessary for OMAP4+ devices

    :param  void:
        no arguments

.. _`omap4_pm_init_early.description`:

Description
-----------

Initializes basic stuff for power management functionality.

.. _`omap4_pm_init`:

omap4_pm_init
=============

.. c:function:: int omap4_pm_init( void)

    Init routine for OMAP4+ devices

    :param  void:
        no arguments

.. _`omap4_pm_init.description`:

Description
-----------

Initializes all powerdomain and clockdomain target states
and all PRCM settings.

.. _`omap4_pm_init.return`:

Return
------

Returns the error code returned by called functions.

.. This file was automatic generated / don't edit.


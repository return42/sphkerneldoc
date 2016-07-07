.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/metag/include/asm/da.h

.. _`metag_da_enabled`:

metag_da_enabled
================

.. c:function:: bool metag_da_enabled( void)

    Find whether a DA is currently enabled.

    :param  void:
        no arguments

.. _`metag_da_enabled.return`:

Return
------

true if a DA was detected, false if not.

.. _`metag_da_probe`:

metag_da_probe
==============

.. c:function:: int metag_da_probe( void)

    Try and detect a connected DA.

    :param  void:
        no arguments

.. _`metag_da_probe.description`:

Description
-----------

This is used at start up to detect whether a DA is active.

.. _`metag_da_probe.return`:

Return
------

0 on detection, -err otherwise.

.. This file was automatic generated / don't edit.


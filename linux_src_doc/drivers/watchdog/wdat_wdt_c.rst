.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/watchdog/wdat_wdt.c

.. _`wdat_instruction`:

struct wdat_instruction
=======================

.. c:type:: struct wdat_instruction

    Single ACPI WDAT instruction

.. _`wdat_instruction.definition`:

Definition
----------

.. code-block:: c

    struct wdat_instruction {
        struct acpi_wdat_entry entry;
        void __iomem *reg;
        struct list_head node;
    }

.. _`wdat_instruction.members`:

Members
-------

entry
    Copy of the ACPI table instruction

reg
    Register the instruction is accessing

node
    Next instruction in action sequence

.. _`wdat_wdt`:

struct wdat_wdt
===============

.. c:type:: struct wdat_wdt

    ACPI WDAT watchdog device

.. _`wdat_wdt.definition`:

Definition
----------

.. code-block:: c

    struct wdat_wdt {
        struct platform_device *pdev;
        struct watchdog_device wdd;
        unsigned int period;
        bool stopped_in_sleep;
        bool stopped;
        struct list_head  *instructions[MAX_WDAT_ACTIONS];
    }

.. _`wdat_wdt.members`:

Members
-------

pdev
    Parent platform device

wdd
    Watchdog core device

period
    How long is one watchdog period in ms

stopped_in_sleep
    Is this watchdog stopped by the firmware in S1-S5

stopped
    Was the watchdog stopped by the driver in suspend

.. This file was automatic generated / don't edit.


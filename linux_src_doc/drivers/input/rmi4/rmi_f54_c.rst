.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/rmi4/rmi_f54.c

.. _`rmi_f54_report_type`:

enum rmi_f54_report_type
========================

.. c:type:: enum rmi_f54_report_type

    RMI4 F54 report types

.. _`rmi_f54_report_type.definition`:

Definition
----------

.. code-block:: c

    enum rmi_f54_report_type {
        F54_REPORT_NONE,
        F54_8BIT_IMAGE,
        F54_16BIT_IMAGE,
        F54_RAW_16BIT_IMAGE,
        F54_TRUE_BASELINE,
        F54_FULL_RAW_CAP,
        F54_FULL_RAW_CAP_RX_OFFSET_REMOVED,
        F54_MAX_REPORT_TYPE
    };

.. _`rmi_f54_report_type.constants`:

Constants
---------

F54_REPORT_NONE
    *undescribed*

F54_8BIT_IMAGE
    Normalized 8-Bit Image Report. The capacitance variance
    from baseline for each pixel.

F54_16BIT_IMAGE
    Normalized 16-Bit Image Report. The capacitance variance
    from baseline for each pixel.

F54_RAW_16BIT_IMAGE
    Raw 16-Bit Image Report. The raw capacitance for each
    pixel.

F54_TRUE_BASELINE
    True Baseline Report. The baseline capacitance for each
    pixel.

F54_FULL_RAW_CAP
    Full Raw Capacitance Report. The raw capacitance with
    low reference set to its minimum value and high
    reference set to its maximum value.

F54_FULL_RAW_CAP_RX_OFFSET_REMOVED
    Full Raw Capacitance with Receiver Offset Removed
    Report. Set Low reference to its minimum value and high
    references to its maximum value, then report the raw
    capacitance for each pixel.

F54_MAX_REPORT_TYPE
    *undescribed*

.. This file was automatic generated / don't edit.


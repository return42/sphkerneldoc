.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/i2c/tvp514x.h

.. _`tvp514x_input`:

enum tvp514x_input
==================

.. c:type:: enum tvp514x_input

    enum for different decoder input pin configuration.

.. _`tvp514x_input.definition`:

Definition
----------

.. code-block:: c

    enum tvp514x_input {
        INPUT_CVBS_VI1A,
        INPUT_CVBS_VI1B,
        INPUT_CVBS_VI1C,
        INPUT_CVBS_VI2A,
        INPUT_CVBS_VI2B,
        INPUT_CVBS_VI2C,
        INPUT_CVBS_VI3A,
        INPUT_CVBS_VI3B,
        INPUT_CVBS_VI3C,
        INPUT_CVBS_VI4A,
        INPUT_SVIDEO_VI2A_VI1A,
        INPUT_SVIDEO_VI2B_VI1B,
        INPUT_SVIDEO_VI2C_VI1C,
        INPUT_SVIDEO_VI2A_VI3A,
        INPUT_SVIDEO_VI2B_VI3B,
        INPUT_SVIDEO_VI2C_VI3C,
        INPUT_SVIDEO_VI4A_VI1A,
        INPUT_SVIDEO_VI4A_VI1B,
        INPUT_SVIDEO_VI4A_VI1C,
        INPUT_SVIDEO_VI4A_VI3A,
        INPUT_SVIDEO_VI4A_VI3B,
        INPUT_SVIDEO_VI4A_VI3C,
        INPUT_INVALID
    };

.. _`tvp514x_input.constants`:

Constants
---------

INPUT_CVBS_VI1A
    *undescribed*

INPUT_CVBS_VI1B
    *undescribed*

INPUT_CVBS_VI1C
    *undescribed*

INPUT_CVBS_VI2A
    *undescribed*

INPUT_CVBS_VI2B
    *undescribed*

INPUT_CVBS_VI2C
    *undescribed*

INPUT_CVBS_VI3A
    *undescribed*

INPUT_CVBS_VI3B
    *undescribed*

INPUT_CVBS_VI3C
    *undescribed*

INPUT_CVBS_VI4A
    *undescribed*

INPUT_SVIDEO_VI2A_VI1A
    *undescribed*

INPUT_SVIDEO_VI2B_VI1B
    *undescribed*

INPUT_SVIDEO_VI2C_VI1C
    *undescribed*

INPUT_SVIDEO_VI2A_VI3A
    *undescribed*

INPUT_SVIDEO_VI2B_VI3B
    *undescribed*

INPUT_SVIDEO_VI2C_VI3C
    *undescribed*

INPUT_SVIDEO_VI4A_VI1A
    *undescribed*

INPUT_SVIDEO_VI4A_VI1B
    *undescribed*

INPUT_SVIDEO_VI4A_VI1C
    *undescribed*

INPUT_SVIDEO_VI4A_VI3A
    *undescribed*

INPUT_SVIDEO_VI4A_VI3B
    *undescribed*

INPUT_SVIDEO_VI4A_VI3C
    *undescribed*

INPUT_INVALID
    *undescribed*

.. _`tvp514x_output`:

enum tvp514x_output
===================

.. c:type:: enum tvp514x_output

    enum for output format supported.

.. _`tvp514x_output.definition`:

Definition
----------

.. code-block:: c

    enum tvp514x_output {
        OUTPUT_10BIT_422_EMBEDDED_SYNC,
        OUTPUT_20BIT_422_SEPERATE_SYNC,
        OUTPUT_10BIT_422_SEPERATE_SYNC,
        OUTPUT_INVALID
    };

.. _`tvp514x_output.constants`:

Constants
---------

OUTPUT_10BIT_422_EMBEDDED_SYNC
    *undescribed*

OUTPUT_20BIT_422_SEPERATE_SYNC
    *undescribed*

OUTPUT_10BIT_422_SEPERATE_SYNC
    *undescribed*

OUTPUT_INVALID
    *undescribed*

.. _`tvp514x_platform_data`:

struct tvp514x_platform_data
============================

.. c:type:: struct tvp514x_platform_data

    Platform data values and access functions.

.. _`tvp514x_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct tvp514x_platform_data {
        bool clk_polarity;
        bool hs_polarity;
        bool vs_polarity;
    }

.. _`tvp514x_platform_data.members`:

Members
-------

clk_polarity
    Clock polarity of the current interface.

hs_polarity
    HSYNC Polarity configuration for current interface.

vs_polarity
    VSYNC Polarity configuration for current interface.

.. This file was automatic generated / don't edit.


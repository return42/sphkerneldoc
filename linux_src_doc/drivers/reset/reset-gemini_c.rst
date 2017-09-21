.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/reset/reset-gemini.c

.. _`gemini_reset`:

struct gemini_reset
===================

.. c:type:: struct gemini_reset

    gemini reset controller

.. _`gemini_reset.definition`:

Definition
----------

.. code-block:: c

    struct gemini_reset {
        struct regmap *map;
        struct reset_controller_dev rcdev;
    }

.. _`gemini_reset.members`:

Members
-------

map
    regmap to access the containing system controller

rcdev
    reset controller device

.. This file was automatic generated / don't edit.


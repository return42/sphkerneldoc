.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/mediatek/pinctrl-mt2701.c

.. _`mtk_spec_pinmux_set`:

struct mtk_spec_pinmux_set
==========================

.. c:type:: struct mtk_spec_pinmux_set

    - For special pins' mode setting

.. _`mtk_spec_pinmux_set.definition`:

Definition
----------

.. code-block:: c

    struct mtk_spec_pinmux_set {
        unsigned short pin;
        unsigned short offset;
        unsigned char bit;
    }

.. _`mtk_spec_pinmux_set.members`:

Members
-------

pin
    The pin number.

offset
    The offset of extra setting register.

bit
    The bit of extra setting register.

.. This file was automatic generated / don't edit.


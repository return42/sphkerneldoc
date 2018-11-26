.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/mediatek/pinctrl-mtk-common-v2.c

.. _`mtk_drive_desc`:

struct mtk_drive_desc
=====================

.. c:type:: struct mtk_drive_desc

    the structure that holds the information of the driving current

.. _`mtk_drive_desc.definition`:

Definition
----------

.. code-block:: c

    struct mtk_drive_desc {
        u8 min;
        u8 max;
        u8 step;
        u8 scal;
    }

.. _`mtk_drive_desc.members`:

Members
-------

min
    the minimum current of this group

max
    the maximum current of this group

step
    the step current of this group

scal
    the weight factor

.. _`mtk_drive_desc.formula`:

formula
-------

output = ((input) / step - 1) \* scal

.. This file was automatic generated / don't edit.


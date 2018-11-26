.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pinctrl/mediatek/pinctrl-mtk-common-v2.h

.. _`mtk_func_desc`:

struct mtk_func_desc
====================

.. c:type:: struct mtk_func_desc

    the structure that providing information all the funcs for this pin

.. _`mtk_func_desc.definition`:

Definition
----------

.. code-block:: c

    struct mtk_func_desc {
        const char *name;
        u8 muxval;
    }

.. _`mtk_func_desc.members`:

Members
-------

name
    the name of function

muxval
    the mux to the function

.. _`mtk_eint_desc`:

struct mtk_eint_desc
====================

.. c:type:: struct mtk_eint_desc

    the structure that providing information for eint data per pin

.. _`mtk_eint_desc.definition`:

Definition
----------

.. code-block:: c

    struct mtk_eint_desc {
        u16 eint_m;
        u16 eint_n;
    }

.. _`mtk_eint_desc.members`:

Members
-------

eint_m
    the eint mux for this pin

eint_n
    *undescribed*

.. _`mtk_pin_desc`:

struct mtk_pin_desc
===================

.. c:type:: struct mtk_pin_desc

    the structure that providing information for each pin of chips

.. _`mtk_pin_desc.definition`:

Definition
----------

.. code-block:: c

    struct mtk_pin_desc {
        unsigned int number;
        const char *name;
        struct mtk_eint_desc eint;
        u8 drv_n;
        struct mtk_func_desc *funcs;
    }

.. _`mtk_pin_desc.members`:

Members
-------

number
    unique pin number from the global pin number space

name
    name for this pin

eint
    the eint data for this pin

drv_n
    the index with the driving group

funcs
    all available functions for this pins (only used in
    those drivers compatible to pinctrl-mtk-common.c-like
    ones)

.. This file was automatic generated / don't edit.


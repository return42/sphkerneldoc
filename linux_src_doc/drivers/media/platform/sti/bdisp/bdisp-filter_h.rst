.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/sti/bdisp/bdisp-filter.h

.. _`bdisp_filter_h_spec`:

struct bdisp_filter_h_spec
==========================

.. c:type:: struct bdisp_filter_h_spec

    Horizontal filter specification

.. _`bdisp_filter_h_spec.definition`:

Definition
----------

.. code-block:: c

    struct bdisp_filter_h_spec {
        const u16 min;
        const u16 max;
        const u8 coef[BDISP_HF_NB];
    }

.. _`bdisp_filter_h_spec.members`:

Members
-------

min
    min scale factor for this filter (6.10 fixed point)

max
    max scale factor for this filter (6.10 fixed point)

coef
    *undescribed*

.. _`bdisp_filter_h_spec.coef`:

coef
----

filter coefficients

.. _`bdisp_filter_v_spec`:

struct bdisp_filter_v_spec
==========================

.. c:type:: struct bdisp_filter_v_spec

    Vertical filter specification

.. _`bdisp_filter_v_spec.definition`:

Definition
----------

.. code-block:: c

    struct bdisp_filter_v_spec {
        const u16 min;
        const u16 max;
        const u8 coef[BDISP_VF_NB];
    }

.. _`bdisp_filter_v_spec.members`:

Members
-------

min
    min scale factor for this filter (6.10 fixed point)

max
    max scale factor for this filter (6.10 fixed point)

coef
    *undescribed*

.. _`bdisp_filter_v_spec.coef`:

coef
----

filter coefficients

.. This file was automatic generated / don't edit.


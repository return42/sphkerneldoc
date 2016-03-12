.. -*- coding: utf-8; mode: rst -*-

==============
bdisp-filter.h
==============



.. _xref_struct_bdisp_filter_h_spec:

struct bdisp_filter_h_spec
==========================

.. c:type:: struct bdisp_filter_h_spec

    Horizontal filter specification



Definition
----------

.. code-block:: c

  struct bdisp_filter_h_spec {
    const u16 min;
    const u16 max;
  };



Members
-------

:``const u16 min``:
    min scale factor for this filter (6.10 fixed point)

:``const u16 max``:
    max scale factor for this filter (6.10 fixed point)




coef
----

filter coefficients




.. _xref_struct_bdisp_filter_v_spec:

struct bdisp_filter_v_spec
==========================

.. c:type:: struct bdisp_filter_v_spec

    Vertical filter specification



Definition
----------

.. code-block:: c

  struct bdisp_filter_v_spec {
    const u16 min;
    const u16 max;
  };



Members
-------

:``const u16 min``:
    min scale factor for this filter (6.10 fixed point)

:``const u16 max``:
    max scale factor for this filter (6.10 fixed point)




coef
----

filter coefficients



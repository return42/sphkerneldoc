.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/nouveau/nvkm/subdev/volt/gk20a.c

.. _`gk20a_volt_get_cvb_voltage`:

gk20a_volt_get_cvb_voltage
==========================

.. c:function:: int gk20a_volt_get_cvb_voltage(int speedo, int s_scale, const struct cvb_coef *coef)

    :param speedo:
        *undescribed*
    :type speedo: int

    :param s_scale:
        *undescribed*
    :type s_scale: int

    :param coef:
        *undescribed*
    :type coef: const struct cvb_coef \*

.. _`gk20a_volt_get_cvb_t_voltage`:

gk20a_volt_get_cvb_t_voltage
============================

.. c:function:: int gk20a_volt_get_cvb_t_voltage(int speedo, int temp, int s_scale, int t_scale, const struct cvb_coef *coef)

    ((c2 \* speedo / s_scale + c1) \* speedo / s_scale + c0) + ((c3 \* speedo / s_scale + c4 + c5 \* T / t_scale) \* T / t_scale)

    :param speedo:
        *undescribed*
    :type speedo: int

    :param temp:
        *undescribed*
    :type temp: int

    :param s_scale:
        *undescribed*
    :type s_scale: int

    :param t_scale:
        *undescribed*
    :type t_scale: int

    :param coef:
        *undescribed*
    :type coef: const struct cvb_coef \*

.. This file was automatic generated / don't edit.


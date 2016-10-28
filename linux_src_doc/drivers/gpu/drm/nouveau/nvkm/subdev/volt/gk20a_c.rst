.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/nouveau/nvkm/subdev/volt/gk20a.c

.. _`gk20a_volt_get_cvb_voltage`:

gk20a_volt_get_cvb_voltage
==========================

.. c:function:: int gk20a_volt_get_cvb_voltage(int speedo, int s_scale, const struct cvb_coef *coef)

    :param int speedo:
        *undescribed*

    :param int s_scale:
        *undescribed*

    :param const struct cvb_coef \*coef:
        *undescribed*

.. _`gk20a_volt_get_cvb_t_voltage`:

gk20a_volt_get_cvb_t_voltage
============================

.. c:function:: int gk20a_volt_get_cvb_t_voltage(int speedo, int temp, int s_scale, int t_scale, const struct cvb_coef *coef)

    ((c2 \* speedo / s_scale + c1) \* speedo / s_scale + c0) + ((c3 \* speedo / s_scale + c4 + c5 \* T / t_scale) \* T / t_scale)

    :param int speedo:
        *undescribed*

    :param int temp:
        *undescribed*

    :param int s_scale:
        *undescribed*

    :param int t_scale:
        *undescribed*

    :param const struct cvb_coef \*coef:
        *undescribed*

.. This file was automatic generated / don't edit.


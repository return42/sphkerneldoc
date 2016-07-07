.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/regulator/max14577-regulator.c

.. _`max14577_get_regmap`:

max14577_get_regmap
===================

.. c:function:: struct regmap *max14577_get_regmap(struct max14577 *max14577, int reg_id)

    different regmaps must be used for them.

    :param struct max14577 \*max14577:
        *undescribed*

    :param int reg_id:
        *undescribed*

.. _`max14577_get_regmap.description`:

Description
-----------

Returns proper regmap for accessing regulator passed by id.

.. This file was automatic generated / don't edit.


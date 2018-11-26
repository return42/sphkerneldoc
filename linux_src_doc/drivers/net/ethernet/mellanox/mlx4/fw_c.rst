.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/mellanox/mlx4/fw.c

.. _`mlx4_access_reg`:

mlx4_ACCESS_REG
===============

.. c:function:: int mlx4_ACCESS_REG(struct mlx4_dev *dev, u16 reg_id, enum mlx4_access_reg_method method, u16 reg_len, void *reg_data)

    Generic access reg command.

    :param dev:
        mlx4_dev.
    :type dev: struct mlx4_dev \*

    :param reg_id:
        register ID to access.
    :type reg_id: u16

    :param method:
        Access method Read/Write.
    :type method: enum mlx4_access_reg_method

    :param reg_len:
        register length to Read/Write in bytes.
    :type reg_len: u16

    :param reg_data:
        reg_data pointer to Read/Write From/To.
    :type reg_data: void \*

.. _`mlx4_access_reg.description`:

Description
-----------

Access ConnectX registers FW command.
Returns 0 on success and copies outbox mlx4_access_reg data
field into reg_data or a negative error code.

.. _`mlx4_access_ptys_reg`:

mlx4_ACCESS_PTYS_REG
====================

.. c:function:: int mlx4_ACCESS_PTYS_REG(struct mlx4_dev *dev, enum mlx4_access_reg_method method, struct mlx4_ptys_reg *ptys_reg)

    Access PTYs (Port Type and Speed) register

    :param dev:
        mlx4_dev.
    :type dev: struct mlx4_dev \*

    :param method:
        Access method Read/Write.
    :type method: enum mlx4_access_reg_method

    :param ptys_reg:
        PTYS register data pointer.
    :type ptys_reg: struct mlx4_ptys_reg \*

.. _`mlx4_access_ptys_reg.description`:

Description
-----------

Access ConnectX PTYS register, to Read/Write Port Type/Speed
configuration
Returns 0 on success or a negative error code.

.. This file was automatic generated / don't edit.


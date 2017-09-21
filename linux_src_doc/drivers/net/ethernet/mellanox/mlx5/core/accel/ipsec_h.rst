.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/mellanox/mlx5/core/accel/ipsec.h

.. _`mlx5_accel_ipsec_sa_cmd_exec`:

mlx5_accel_ipsec_sa_cmd_exec
============================

.. c:function:: void *mlx5_accel_ipsec_sa_cmd_exec(struct mlx5_core_dev *mdev, struct mlx5_accel_ipsec_sa *cmd)

    Execute an IPSec SADB command

    :param struct mlx5_core_dev \*mdev:
        mlx5 device

    :param struct mlx5_accel_ipsec_sa \*cmd:
        command to execute
        May be called from atomic context. Returns context pointer, or error
        Caller must eventually call mlx5_accel_ipsec_sa_cmd_wait from non-atomic
        context, to cleanup the context pointer

.. _`mlx5_accel_ipsec_sa_cmd_wait`:

mlx5_accel_ipsec_sa_cmd_wait
============================

.. c:function:: int mlx5_accel_ipsec_sa_cmd_wait(void *context)

    Wait for command execution completion

    :param void \*context:
        Context pointer returned from call to mlx5_accel_ipsec_sa_cmd_exec
        Sleeps (killable) until command execution is complete.
        Returns the command result, or -EINTR if killed

.. This file was automatic generated / don't edit.


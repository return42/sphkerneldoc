.. -*- coding: utf-8; mode: rst -*-

========
vx_cmd.h
========


.. _`vx_set_pipe_cmd_params`:

vx_set_pipe_cmd_params
======================

.. c:function:: void vx_set_pipe_cmd_params (struct vx_rmh *rmh, int is_capture, int param1, int param2)

    fill first command word for pipe commands

    :param struct vx_rmh \*rmh:
        the rmh to be modified

    :param int is_capture:
        0 = playback, 1 = capture operation

    :param int param1:
        first pipe-parameter

    :param int param2:
        second pipe-parameter



.. _`vx_set_stream_cmd_params`:

vx_set_stream_cmd_params
========================

.. c:function:: void vx_set_stream_cmd_params (struct vx_rmh *rmh, int is_capture, int pipe)

    fill first command word for stream commands

    :param struct vx_rmh \*rmh:
        the rmh to be modified

    :param int is_capture:
        0 = playback, 1 = capture operation

    :param int pipe:
        the pipe index (zero-based)

